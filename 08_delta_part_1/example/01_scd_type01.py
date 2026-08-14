# Databricks notebook source
# MAGIC %run ./_ddl

# COMMAND ----------

# DBTITLE 1,preview dataset
from pyspark.sql.functions import *
from delta.tables import *

reset_table_scd_type01()
print("target")
spark.table("session_8_delta.scd_type01").display()
print("source")
scd_type01_02_df.display()

reset_table_scd_type01_with_hash()
print("target_with_hash")
spark.table("session_8_delta.scd_type01_hash").display()
print("source")
scd_type01_02_df.display()

# COMMAND ----------

# DBTITLE 1,merge_scd_type01
# merge_scd01
reset_table_scd_type01()
print("target as-is")
spark.table("session_8_delta.scd_type01").display()
source_df = scd_type01_02_df
print("source dataset")
source_df.display()

#-------------------------------------------------------------------------------------------------------------------------------------------------
delta_table = DeltaTable.forName(spark, "session_8_delta.scd_type01")
log_df = (
    delta_table.alias("target")
    .merge(source_df.alias("source"),'source.customer_id = target.customer_id')
    .whenMatchedUpdate(
        set={
             "name": col("source.name")
            ,"city": col("source.city")
            ,"update_date": current_date()
            ,"last_mod_ts": current_timestamp()
            }
        )
    .whenNotMatchedInsert(
        values = {
            "customer_id": col("source.customer_id")
            ,"name": col("source.name")
            ,"city": col("source.city")
            ,"insert_date": current_date()
            ,"update_date": current_date()
            ,"last_mod_ts": current_timestamp()
        }
    )
    .execute()
    )

print("target to-be")
spark.table("session_8_delta.scd_type01").display()

print("log_change")
log_df.display()

# COMMAND ----------

# DBTITLE 1,merge_scd_type01_with_hash
reset_table_scd_type01_with_hash()
print("target as-is")
spark.table("session_8_delta.scd_type01_hash").display()

update_df = (
    scd_type01_02_df
    .withColumn("hash_key",xxhash64("customer_id"))
    .withColumn("hash_value",xxhash64("name","city"))
    )
print("update dataset")
update_df.display()

#-------------------------------------------------------------------------------------------------------------------------------------------------
delta_table = DeltaTable.forName(spark, "session_8_delta.scd_type01_hash")
log_df = (
    delta_table.alias("target")
    .merge(update_df.alias("source"),'source.hash_key = target.hash_key')
    .whenMatchedUpdate(
        set={
             "name": col("source.name")
            ,"city": col("source.city")
            ,"update_date": current_date()
            ,"last_mod_ts": current_timestamp()
            ,"hash_value" : col("source.hash_value")
            }
        ,condition= "source.hash_value != target.hash_value"
        )
    .whenNotMatchedInsert(
        values = {
            "customer_id": col("source.customer_id")
            ,"name": col("source.name")
            ,"city": col("source.city")
            ,"insert_date": current_date()
            ,"update_date": current_date()
            ,"last_mod_ts": current_timestamp()
            ,"hash_key": col("source.hash_key")
            ,"hash_value": col("source.hash_value")
        }
    )
    .execute()
    )

print("target to-be")
spark.table("session_8_delta.scd_type01_hash").display()
print("log change")
log_df.display()