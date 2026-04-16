# Databricks notebook source
# MAGIC %md
# MAGIC **Ex 1 write ETL pipeline**
# MAGIC   - run %run ./_functions
# MAGIC   - ingest from kaggle dataset <https://www.kaggle.com/datasets>
# MAGIC     - copy file path from <> Code section
# MAGIC     - copy file name
# MAGIC     - use get_kaggle_dataset_to_df() function  to retrive data via api
# MAGIC     - select data with sql
# MAGIC   
# MAGIC   - transform data
# MAGIC     - filter data with sql statement
# MAGIC   
# MAGIC   - load data to data-lakehouse
# MAGIC     - use load_to_delta_table() function to load data to lakehouse

# COMMAND ----------

# MAGIC %run ../_functions

# COMMAND ----------

#extract
path = "<path_name>"
file_name = "<file_name>"

get_kaggle_dataset_to_df(path,file_name).createOrReplaceTempView("raw_kaggle_dataset")

# COMMAND ----------

#transform
sql_statement = """ <put sql statement here> """

spark.sql(sql_statement).createOrReplaceTempView("transform_kaggle_dataset")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from transform_kaggle_dataset

# COMMAND ----------

#load
load_to_delta_table("transform_kaggle_dataset","piti_employee_burn_out")

# COMMAND ----------

# MAGIC %md
# MAGIC **Ex2. convert from ETL pipeline to ELT pipeline**

# COMMAND ----------

# extract

# COMMAND ----------

#load

# COMMAND ----------

#tranform