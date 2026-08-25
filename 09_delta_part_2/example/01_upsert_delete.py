# Databricks notebook source
# MAGIC %run ./_ddl

# COMMAND ----------

from pyspark.sql.functions import *
from delta import *

# COMMAND ----------

# DBTITLE 1,merge_scd_with_delete
reset_table_scd_type01_with_hash()
print("target as-is")
spark.table("session_9_delta.scd_type01_hash").display()
print("source")
source_df = (
    scd_type01_02_df
    .withColumn("hash_key",xxhash64("customer_id"))
    .withColumn("hash_value",xxhash64("name","city"))
    )
source_df.display()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
delta_obj = DeltaTable.forName(spark, "session_9_delta.scd_type01_hash")
log_df = (
    delta_obj.alias("target")
    .merge(source_df.alias("source"), "source.hash_key = target.hash_key")
    .whenMatchedUpdate(
        set = {
            "customer_id": col("source.customer_id")
            ,"name": col("source.name")
            ,"city": col("source.city")
            ,"update_date": current_date()
            ,"last_mod_ts": current_timestamp()
            ,"hash_key": col("source.hash_key")
            ,"hash_value": col("source.hash_value")
            }
        ,condition = "source.hash_value <> target.hash_value"
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
    .whenNotMatchedBySourceDelete()
    .execute()
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
print("target to-be")
spark.table("session_9_delta.scd_type01_hash").display()
print("log")
log_df.display()