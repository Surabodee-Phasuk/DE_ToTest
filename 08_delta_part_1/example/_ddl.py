# Databricks notebook source
from pyspark.sql import *
from pyspark.sql.functions import *
import datetime

# COMMAND ----------

spark.sql("create schema if not exists session_8_delta")
spark.sql("drop table if exists session_8_delta.scd_type01")
spark.sql("drop table if exists session_8_delta.scd_type01_hash")
spark.sql("drop table if exists session_8_delta.scd_type02_hash")

# COMMAND ----------

# DBTITLE 1,prep data for scd type 01
scd_type01_data_01 = [
    Row(customer_id=1, name="Alice", city="New York",insert_date= datetime.date(2025,1,1),update_date =  datetime.date(2025,1,1),last_mod_ts = datetime.datetime.now()),
    Row(customer_id=2, name="Bob", city="Los Angeles",insert_date= datetime.date(2025,1,1),update_date = datetime.date(2025,1,1),last_mod_ts = datetime.datetime.now()),
    Row(customer_id=3, name="Charlie", city="Chicago",insert_date= datetime.date(2025,1,1),update_date =  datetime.date(2025,1,1),last_mod_ts = datetime.datetime.now()),
]
scd_type01_01_df = spark.createDataFrame(scd_type01_data_01,"customer_id int , name string,city string,insert_date date,update_date date,last_mod_ts timestamp")

scd_type01_data_02 = [
    Row(customer_id=4, name="New",  city="New York"),
    Row(customer_id=1, name="update", city="Los Angeles"),
    Row(customer_id=3, name="Charlie", city="Chicago"),
]
scd_type01_02_df = spark.createDataFrame(scd_type01_data_02,"customer_id int , name string,city string")

# COMMAND ----------

# DBTITLE 1,prep data for scd type 02
scd_type02_data_01 = [
    Row(customer_id=1, name="Alice", city="New York", start_date= datetime.date(2025,1,1),end_date =  datetime.date(9000,12,31),last_mod_ts = datetime.datetime.now()),
    Row(customer_id=2, name="Bob", city="Los Angeles",start_date= datetime.date(2025,1,1),end_date =  datetime.date(9000,12,31),last_mod_ts = datetime.datetime.now()),
    Row(customer_id=3, name="Charlie", city="Chicago",start_date= datetime.date(2025,1,1),end_date =  datetime.date(9000,12,31),last_mod_ts = datetime.datetime.now()),
]
scd_type02_01_df = spark.createDataFrame(scd_type02_data_01,"customer_id int, name string,city string,start_date date,end_date date,last_mod_ts timestamp")
scd_type02_data_02 = [
    Row(customer_id=4, name="New",  city="New York"),
    Row(customer_id=1, name="update", city="Los Angeles"),
    Row(customer_id=3, name="Charlie", city="Chicago"),
]
scd_type02_02_df = spark.createDataFrame(scd_type02_data_02,"customer_id int , name string,city string")

# COMMAND ----------

# DBTITLE 1,reset function
def reset_table_scd_type01() -> None:
    scd_type01_01_df.write.mode("overwrite").option("overwriteSchema",True).saveAsTable("session_8_delta.scd_type01")

def reset_table_scd_type01_with_hash() -> None:
    final_result = (
        scd_type01_01_df
        .withColumn("hash_key",xxhash64("customer_id"))
        .withColumn("hash_value",xxhash64("name","city"))
        )
    final_result.write.mode("overwrite").option("overwriteSchema",True).saveAsTable("session_8_delta.scd_type01_hash")

def reset_table_scd_type02_with_hash() -> None:
    final_result = (
        scd_type02_01_df
        .withColumn("hash_key",xxhash64("customer_id"))
        .withColumn("hash_value",xxhash64("name","city"))
    )
    final_result.write.mode("overwrite").option("overwriteSchema",True).saveAsTable("session_8_delta.scd_type02_hash")

# COMMAND ----------

reset_table_scd_type01()
reset_table_scd_type01_with_hash()
reset_table_scd_type02_with_hash()

# COMMAND ----------

print_str = """
dataframe list:
scd_type01_01_df
scd_type01_02_df
scd_type02_01_df
scd_type02_02_df

table list:
session_8_delta.scd_type01
session_8_delta.scd_type01_hash
session_8_delta.scd_type02_hash

function lists:
reset_table_scd_type01
reset_table_scd_type01_with_hash
reset_table_scd_type02_with_hash
"""

print(print_str)