# Databricks notebook source
from pyspark.sql.functions import *

# COMMAND ----------

from pprint import pprint

"""collect"""
sales_collect = sales_df.collect()

"""retrive only column that we want by using list comprehension"""
sales_collect_2 = sales_df.select("shop_id","store_size").collect()

new_lists = [ (_.shop_id, _.store_size) for _ in sales_collect_2]

pprint(sales_collect)
pprint(sales_collect_2)
pprint(new_lists)

# COMMAND ----------

# Overwrite mode
sales_df.write.mode("overwrite").option("header", True).csv("/Volumes/dev_catalog/dwh/temp_volumn_session_6/sales_overwrite_csv")
sales_df.write.mode("overwrite").option("compression", "gzip").parquet("/Volumes/dev_catalog/dwh/temp_volumn_session_6/sales_overwrite_parquet")
sales_df.write.mode("overwrite").json("/Volumes/dev_catalog/dwh/temp_volumn_session_6/sales_overwrite_json")

# Append mode
sales_df.write.mode("append").option("header", True).csv("/Volumes/dev_catalog/dwh/temp_volumn_session_6/sales_append_csv")
sales_df.write.mode("append").parquet("/Volumes/dev_catalog/dwh/temp_volumn_session_6/sales_append_parquet")
sales_df.write.mode("append").json("/Volumes/dev_catalog/dwh/temp_volumn_session_6/sales_append_json")

# Ignore mode
sales_df.write.mode("ignore").option("header", True).csv("/Volumes/dev_catalog/dwh/temp_volumn_session_6/sales_ignore_csv")
sales_df.write.mode("ignore").parquet("/Volumes/dev_catalog/dwh/temp_volumn_session_6/sales_ignore_parquet")
sales_df.write.mode("ignore").json("/Volumes/dev_catalog/dwh/temp_volumn_session_6/sales_ignore_json")

# ErrorIfExists mode
sales_df.write.mode("error").option("header", True).csv("/Volumes/dev_catalog/dwh/temp_volumn_session_6/sales_errorifexists_csv")
sales_df.write.mode("error").parquet("/Volumes/dev_catalog/dwh/temp_volumn_session_6/sales_errorifexists_parquet")
sales_df.write.mode("error").json("/Volumes/dev_catalog/dwh/temp_volumn_session_6/sales_errorifexists_json")

# Additional options
sales_df.write.option("header", True).option("delimiter", ";").csv("/Volumes/dev_catalog/dwh/temp_volumn_session_6/sales_csv_delimiter")
sales_df.write.option("compression", "snappy").parquet("/Volumes/dev_catalog/dwh/temp_volumn_session_6/sales_parquet_snappy")
sales_df.write.option("timestampFormat", "yyyy-MM-dd HH:mm:ss").json("/Volumes/dev_catalog/dwh/temp_volumn_session_6/sales_json_timestamp")