# Databricks notebook source
# MAGIC %run ./_ddl

# COMMAND ----------

from pyspark.sql.functions import *
from delta import *

# COMMAND ----------

#scd type02
reset_table_scd_type02_with_hash()
spark.table("session_8_delta.scd_type02_hash").display()
scd_type02_02_df.display()

# COMMAND ----------

#prepare staging before merge
source_df = (
    scd_type02_02_df
    .withColumn("hash_key",xxhash64("customer_id"))
    .withColumn("hash_value",xxhash64("name","city"))
    )

# check which record is change / insert / no_change
target_df = (
    spark.table("session_8_delta.scd_type02_hash")
    .filter(col("end_date") == '9000-12-31')
    )

# join source with target
# 1 if hash_key is null which mean new record
# 2 if hash_value is same which mean no change
# 3 if hash_value is different which mean change
source_transform_df = (
    source_df.alias("source")
    .join(target_df.alias("target"),[col("source.hash_key") == col("target.hash_key")],"left")
    .withColumn("record_status",
                when(col("target.hash_key").isNull(),lit("insert"))
                .when(col("target.hash_value") == col("source.hash_value"),lit("no_change"))
                .otherwise(lit("change"))
                )
    .select("source.*","record_status")
    )
#extract only insert record generate merge_key null (force insert)
new_df = (
    source_transform_df
    .filter(col("record_status") == 'insert')
    .withColumn("merge_key",lit(None))
    )

#extract only change record
change_df = (
    source_transform_df
    .filter(col("record_status") == 'change')
    )

# generate 2 merge_key for change record
# 1. close old record -> merge_key = hash_key
# 2. insert new record -> merge_key = None
final_change_df = (
    change_df.withColumn("merge_key",lit(None))
    .unionByName(change_df.withColumn("merge_key",col("hash_key")))
    )

#union new and change record
final_result_df = (
    new_df
    .unionByName(final_change_df)
)
print("final_source")
final_result_df.display()
print("target_table as-is")
spark.table("session_8_delta.scd_type02_hash").display()

# COMMAND ----------

delta_scd02_obj = DeltaTable.forName(spark,"session_8_delta.scd_type02_hash")

result_log = (
    delta_scd02_obj.alias("target")
    .merge(final_result_df.alias("source"),"target.hash_key = source.merge_key")
    .whenMatchedUpdate(
        set = {
            "end_date": current_date()
            ,"last_mod_ts": current_timestamp()
            }
        ,condition = col("target.end_date") == '9000-12-31'
    )
    .whenNotMatchedInsert(
        values = {
            "customer_id": col("source.customer_id")
            ,"name": col("source.name")
            ,"city": col("source.city")
            ,"start_date": current_date()
            ,"end_date": lit('9000-12-31')
            ,"last_mod_ts": current_timestamp()
            ,"hash_key": col("source.hash_key")
            ,"hash_value": col("source.hash_value")
        }
    )
    .execute()
    )

print("target_table to-be")
spark.table("session_8_delta.scd_type02_hash").display()
print("log")
result_log.display()