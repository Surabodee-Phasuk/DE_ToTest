# Databricks notebook source
!pip install pyspark-data-sources[all]

# COMMAND ----------

!pip install kagglehub

# COMMAND ----------

# MAGIC %restart_python

# COMMAND ----------

from pyspark_datasources import KaggleDataSource
from pyspark.sql.functions import col
from pyspark.sql import DataFrame

# COMMAND ----------

def get_kaggle_dataset_to_df(path:str , file_name:str) -> DataFrame:
    spark.dataSource.register(KaggleDataSource)
    df = spark.read.format("kaggle").options(handle=path).load(file_name)
    col_names = [col(col_name).alias(col_name.replace(" ", "_")) for col_name in df.columns]
    print(f"path: {path} \nfile_name: {file_name}")
    return df.select(col_names)

# COMMAND ----------

def load_to_delta_table(temp_name:str,target_table:str) -> None:
    temp_df = spark.table(temp_name)
    temp_df.write.mode("overwrite").saveAsTable(target_table)
    print(f"loaded to table: default.{target_table}")

# COMMAND ----------

print(
    """
    function_lists
    get_kaggle_dataset_to_df(path , file_name)
    load_to_delta_table(df,target_table)
    """
)