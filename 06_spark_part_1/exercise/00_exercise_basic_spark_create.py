# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC **1. Create csv file in directory**
# MAGIC 1. Create file in exerice directory.
# MAGIC 2. Add data in the files
# MAGIC 3. Can create with variety of delimiter
# MAGIC     - `|`
# MAGIC     - `,`
# MAGIC     - `-`

# COMMAND ----------

# MAGIC %md
# MAGIC **2. Create Volume with Sql Statement**
# MAGIC 1. use `CREATE VOLUME IF NOT EXISTS session_6_spark.volume_staging` to create volume_staging.
# MAGIC 2. Check the results in catalog session_6_spark.

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS workspace.session_6_spark;
# MAGIC CREATE VOLUME IF NOT EXISTS session_6_spark.volume_staging

# COMMAND ----------

# MAGIC %md
# MAGIC **3. Move file to Volume with functions**
# MAGIC 1. Using copy_file_to_volume functions to copy file from workspace to volume.
# MAGIC 2. Check the results in volume.

# COMMAND ----------

def copy_file_to_volume(file_name:str) -> None:
    volume_taget = "/Volumes/workspace/session_6_spark/volume_staging"
    current_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
    current_path = "/".join(current_path.split("/")[1:-1])
    current_path = f'/Workspace/{current_path}/{file_name}'

    dbutils.fs.cp(current_path,volume_taget)
    print(f"file {file_name} copied to {volume_taget}")

copy_file_to_volume('test_csv.csv')

# COMMAND ----------

spark.read.format("csv").load("/Volumes/workspace/session_6_spark/volume_staging/test_csv.csv").display()

# COMMAND ----------

# MAGIC %md
# MAGIC **4. Read file from Volume with PySpark**
# MAGIC
# MAGIC 1. Check the volume path in catalog
# MAGIC 2. Use the following code to read the CSV into a DataFrame:
# MAGIC    ```python
# MAGIC    read_csv_df = (
# MAGIC        spark.read
# MAGIC        .format("csv")
# MAGIC        .option("header", True)
# MAGIC        .option("delimiter", "|")
# MAGIC        .load('<file_path>')
# MAGIC    )
# MAGIC    ```
# MAGIC 3. Use `.display()` to show data in spark object

# COMMAND ----------

read_csv_df = (
    spark.read
    .format("csv")
    .option("header", True)
    .option("delimiter", "|")
    .load('/Volumes/workspace/session_6_spark/volume_staging')
)
read_csv_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC **5. Spark Attribute**
# MAGIC 1. list all Column using `.columns` attribute
# MAGIC 2. list all schema using `.dtypes` attribute
# MAGIC 3. list all schema as a struct object with `.schema` attribute

# COMMAND ----------

 

# COMMAND ----------

# MAGIC %md
# MAGIC **6. Spark Method**
# MAGIC 1. use `.display()` to display data in dataframe.
# MAGIC 2. use `.collect()` to collect data as python object.
# MAGIC 3. use `.limit(<number of records>)` to limit the number of record data.

# COMMAND ----------

 