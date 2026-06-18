# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

sales_schema = "shop_id int, sales_amount int, store_size string, q1_sales int, q2_sales int, q3_sales int, region string"
sales_data = [
    {"shop_id": 101, "sales_amount": 500, "store_size": "Small", "q1_sales": 100, "q2_sales": 200, "q3_sales": 200, "region": "North"},
    {"shop_id": 102, "sales_amount": 1500, "store_size": "Large", "q1_sales": 500, "q2_sales": 500, "q3_sales": 500, "region": "South"},
    {"shop_id": 201, "sales_amount": 1200, "store_size": None, "q1_sales": 400, "q2_sales": 400, "q3_sales": 400, "region": "East"},
    {"shop_id": 202, "sales_amount": 2500, "store_size": "Medium", "q1_sales": 1000, "q2_sales": 1000, "q3_sales": 500, "region": "West"},
    {"shop_id": 203, "sales_amount": 800, "store_size": "", "q1_sales": 200, "q2_sales": 300, "q3_sales": 300, "region": "North"},
    {"shop_id": 404, "sales_amount": 3000, "store_size": "Medium", "q1_sales": 1000, "q2_sales": 1000, "q3_sales": 1000, "region": "Central"},
    {"shop_id": 501, "sales_amount": 12000, "store_size": "Large", "q1_sales": 4000, "q2_sales": 4000, "q3_sales": 4000, "region": "North"},
    {"shop_id": 901, "sales_amount": 5000, "store_size": "Large", "q1_sales": 2000, "q2_sales": 2000, "q3_sales": 1000, "region": "South"},
    {"shop_id": 901, "sales_amount": 2000, "store_size": "Large", "q1_sales": 1000, "q2_sales": 500, "q3_sales": 500, "region": "South"} 
]

shop_schema = "shop_id int, shop_name string, region string"
shop_data = [
    {"shop_id": 101, "shop_name": "Bangkok Central", "region": "Central"},
    {"shop_id": 102, "shop_name": "Phuket Hub", "region": "South"}
]

master_sales_df = spark.createDataFrame(sales_data, schema=sales_schema)
master_shop_df = spark.createDataFrame(shop_data, schema=shop_schema)

# COMMAND ----------

# MAGIC %md
# MAGIC # Master Exercise Set: Basic Transformations
# MAGIC
# MAGIC ### **Easy**

# COMMAND ----------

# MAGIC %md
# MAGIC **Basic Selection & Aliasing**
# MAGIC 1. Using `master_sales_df`, select only the `shop_id` and `sales_amount` columns.
# MAGIC 2. Rename `shop_id` to `store_code` using `.alias()`.
# MAGIC 3. Limit the output to the first 2 rows.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC | store_code | sales_amount |
# MAGIC |---|---|
# MAGIC | 101 | 500 |
# MAGIC | 102 | 1500 |

# COMMAND ----------

 

# COMMAND ----------

# MAGIC %md
# MAGIC **Filtering Constants & Nulls**
# MAGIC 1. Using `master_sales_df`, filter the DataFrame to return ONLY rows where `store_size` is NOT null AND NOT an empty string `""`.
# MAGIC 2. Select `shop_id` and `store_size`.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC | shop_id | store_size |
# MAGIC |---|---|
# MAGIC | 101 | Small |
# MAGIC | 102 | Large |
# MAGIC | 202 | Medium |
# MAGIC | 404 | Medium |
# MAGIC | 501 | Large |
# MAGIC | 901 | Large |
# MAGIC | 901 | Large |

# COMMAND ----------

 

# COMMAND ----------

# MAGIC %md
# MAGIC **Simple Mathematical withColumn**
# MAGIC 1. Using `master_sales_df`, create a new column `projected_sales` which is `sales_amount` multiplied by `1.15`.
# MAGIC 2. Create a static column `fiscal_year` set to literal value `2026`.
# MAGIC 3. Show only `shop_id`, `sales_amount`, `projected_sales`, and `fiscal_year` for `shop_id` 101.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC | shop_id | sales_amount | projected_sales | fiscal_year |
# MAGIC |---|---|---|---|
# MAGIC | 101 | 500 | 575.0 | 2026 |

# COMMAND ----------

 

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Normal**

# COMMAND ----------

# MAGIC %md
# MAGIC **Chained Multi-Condition Filtering**
# MAGIC 1. Using `master_sales_df`, filter using chained logic: `sales_amount` between 1000 and 5000.
# MAGIC 2. AND `store_size` is either "Large" or "Medium" (use `.isin()`).
# MAGIC 3. Exclude `shop_id` equal to 404 using the `~` operator.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC | shop_id | sales_amount | store_size | q1_sales | q2_sales | q3_sales | region |
# MAGIC |---|---|---|---|---|---|---|
# MAGIC | 102 | 1500 | Large | 500 | 500 | 500 | South |
# MAGIC | 202 | 2500 | Medium | 1000 | 1000 | 500 | West |
# MAGIC | 901 | 5000 | Large | 2000 | 2000 | 1000 | South |
# MAGIC | 901 | 2000 | Large | 1000 | 500 | 500 | South |

# COMMAND ----------

 

# COMMAND ----------

# MAGIC %md
# MAGIC **Categorization via When/Otherwise**
# MAGIC 1. Using `master_sales_df`, create `performance_tier`: if sales > 10000 -> "Diamond", if > 5000 -> "Gold", otherwise -> "Silver".
# MAGIC 2. Create `size_flag`: if `store_size` is Null or empty -> "Unknown", otherwise keep the original `store_size`.
# MAGIC 3. Show for shop_ids: 501, 901, and 201.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC | shop_id | sales_amount | performance_tier | size_flag |
# MAGIC |---|---|---|---|
# MAGIC | 201 | 1200 | Silver | Unknown |
# MAGIC | 501 | 12000 | Diamond | Large |
# MAGIC | 901 | 5000 | Silver | Large |
# MAGIC | 901 | 2000 | Silver | Large |

# COMMAND ----------

 

# COMMAND ----------

# MAGIC %md
# MAGIC **Comprehensive GroupBy & Aggregation**
# MAGIC 1. Using `master_sales_df`, group by `store_size`.
# MAGIC 2. Aggregate to find: total unique shops (`countDistinct`), average sales, max sales, and minimum sales per size.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC | store_size | unique_shops | avg_sales | max_sales | min_sales |
# MAGIC |---|---|---|---|---|
# MAGIC | null | 1 | 1200.0 | 1200 | 1200 |
# MAGIC |  | 1 | 800.0 | 800 | 800 |
# MAGIC | Small | 1 | 500.0 | 500 | 500 |
# MAGIC | Medium | 2 | 2750.0 | 3000 | 2500 |
# MAGIC | Large | 3 | 5125.0 | 12000 | 1500 |

# COMMAND ----------

 

# COMMAND ----------

# MAGIC %md
# MAGIC **Dictionary-Driven Column Renaming**
# MAGIC 1. Define a Python dictionary mapping old column names to new ones: `{"shop_id": "identifier", "shop_name": "store_title", "region": "zone"}`.
# MAGIC 2. Use a Python `for` loop over the dictionary items to iteratively apply `.withColumnRenamed()` on `master_shop_df`.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC | identifier | store_title | zone |
# MAGIC |---|---|---|
# MAGIC | 101 | Bangkok Central | Central |
# MAGIC | 102 | Phuket Hub | South |

# COMMAND ----------

 

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Hard**

# COMMAND ----------

# MAGIC %md
# MAGIC **Dynamic Aggregation via List Comprehensions**
# MAGIC 1. Using `master_sales_df`, isolate the columns representing quarters (`q1_sales`, `q2_sales`, `q3_sales`).
# MAGIC 2. Use a Python list comprehension to dynamically generate a list of PySpark `sum()` aggregation expressions for all columns ending with `_sales`.
# MAGIC 3. Apply this dynamically generated list to a `.groupBy("region").agg(*exprs)` operation.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC | region | total_q1_sales | total_q2_sales | total_q3_sales |
# MAGIC |---|---|---|---|
# MAGIC | East | 400 | 400 | 400 |
# MAGIC | South | 3500 | 3000 | 2000 |
# MAGIC | Central | 1000 | 1000 | 1000 |
# MAGIC | West | 1000 | 1000 | 500 |
# MAGIC | North | 4300 | 4500 | 4500 |

# COMMAND ----------

 

# COMMAND ----------

# MAGIC %md
# MAGIC **Conditional Aggregation Pivot Simulation**
# MAGIC 1. Using `master_sales_df`, calculate the total sales for "Large" stores and "Small" stores as two separate columns alongside the `region` grouping (Do not use `.pivot()`).
# MAGIC 2. Use `sum()` wrapped around a `when()` condition to accomplish this.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC | region | large_store_sales | small_store_sales |
# MAGIC |---|---|---|
# MAGIC | East | 0 | 0 |
# MAGIC | South | 8500 | 0 |
# MAGIC | Central | 0 | 0 |
# MAGIC | West | 0 | 0 |
# MAGIC | North | 12000 | 500 |

# COMMAND ----------

 