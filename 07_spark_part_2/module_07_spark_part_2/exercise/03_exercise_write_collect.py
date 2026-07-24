# Databricks notebook source
from pyspark.sql.functions import *
from pprint import pprint

spark.sql("create schema if not exists session_7_spark")

inv_schema = "item_id string, category string, stock int, warehouse string, last_updated string"
inv_data = [
    ("I001", "Laptops", 150, "NY", "2025-01-01 10:00:00"),
    ("I002", "Phones", 0, "CA", "2025-01-02 11:30:00"),
    ("I003", "Accessories", 45, "NY", "2025-01-03 09:15:00"),
    ("I004", "Laptops", 30, "CA", "2025-01-04 14:20:00")
]
inventory_df = spark.createDataFrame(inv_data, schema=inv_schema)

# COMMAND ----------

# MAGIC %md 
# MAGIC ### **Normal**

# COMMAND ----------

# MAGIC %md
# MAGIC # 1. Basic Collect
# MAGIC 1. Collect all rows from `inventory_df` into a variable named `inv_collect`.
# MAGIC 2. Print the `item_id` of the first row.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC `I001`

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # 2. Collect with List Comprehension
# MAGIC 1. Select the `item_id` and `stock` columns from `inventory_df` and collect them.
# MAGIC 2. Use a list comprehension to iterate through the collected rows and create a list of tuples `(item_id, stock)`.
# MAGIC 3. Print the new list using `pprint`.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC `[('I001', 150), ('I002', 0), ('I003', 45), ('I004', 30)]`

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # 3. Save as Table: Overwrite Mode
# MAGIC 1. Write `inventory_df` as a Delta table named `session_7_spark.inv_overwrite`.
# MAGIC 2. Set the write mode to `overwrite`.
# MAGIC 3. *Note: Databricks defaults to Delta format when using saveAsTable.*

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # 4. Save as Table: Append Mode
# MAGIC 1. Write `inventory_df` to an existing Delta table named `session_7_spark.inv_append`.
# MAGIC 2. Set the write mode to `append`.

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # 5. Save as Table: Ignore Mode
# MAGIC 1. Write `inventory_df` to a Delta table named `session_7_spark.inv_ignore`.
# MAGIC 2. Set the write mode to `ignore`, which will safely skip the operation if the table already exists.

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # 6. Save as Table: ErrorIfExists Mode
# MAGIC 1. Write `inventory_df` to a Delta table named `session_7_spark.inv_error`.
# MAGIC 2. Set the write mode to `error` (or `errorifexists`) so it intentionally fails if the table is already present.

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # 7. Save as Table: Explicit Delta Format
# MAGIC 1. Write `inventory_df` to a table named `session_7_spark.inv_explicit_delta`.
# MAGIC 2. Explicitly set the format to `delta`. 
# MAGIC 3. Use `overwrite` mode.

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # 8. Save as Table: Partition By
# MAGIC 1. Write `inventory_df` to a Delta table named `session_7_spark.inv_partitioned`.
# MAGIC 2. Partition the table by the `warehouse` column.
# MAGIC 3. Use `overwrite` mode.

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # 9. Save as Table: Merge Schema Option (Append)
# MAGIC 1. Create a modified DataFrame by adding a literal column `is_active` (boolean `True`) to `inventory_df`.
# MAGIC 2. Write this modified DataFrame to `session_7_spark.inv_append` (from question 4) using `append` mode.
# MAGIC 3. Pass the standard Delta option `mergeSchema` as `True` to allow the new column to be added to the target table.

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # 10. Save as Table: Overwrite Schema Option
# MAGIC 1. Take the `modified_inv_df` (with the new `is_active` column).
# MAGIC 2. Write it to `session_7_spark.inv_overwrite` (from question 3) using `overwrite` mode.
# MAGIC 3. Because the schema has changed, pass the standard Delta option `overwriteSchema` as `True` to completely replace the table structure.

# COMMAND ----------

