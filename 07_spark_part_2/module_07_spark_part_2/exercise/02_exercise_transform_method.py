# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.window import Window
from pyspark.sql.types import *

txn_schema = "txn_id string, customer_id int, store_size string, category string, amount double, txn_date string"
txn_data = [
    ("T1", 501, "Large", "Laptops", 1200.0, "2025-01-05"),
    ("T2", 502, "Medium", "Phones", 800.0, "2025-01-06"),
    ("T3", 501, None, "Accessories", 50.0, "2025-01-06"),
    ("T4", 503, "Large", "Laptops", 1500.0, "2025-01-07"),
    ("T4", 503, "Large", "Laptops", 1500.0, "2025-01-07") # Duplicate
]
transactions_df = spark.createDataFrame(txn_data, schema=txn_schema)

refund_schema = "txn_id string, customer_id int, refund_amount double"
refund_data = [
    ("T2", 502, 800.0),
    ("T5", 504, 100.0)
]
refunds_df = spark.createDataFrame(refund_data, schema=refund_schema)

# COMMAND ----------

# MAGIC %md 
# MAGIC ### **Easy**

# COMMAND ----------

# MAGIC %md
# MAGIC # Remove Duplicates and Nulls
# MAGIC 1. Drop duplicate rows from `transactions_df`.
# MAGIC 2. Drop any rows where `store_size` is null.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC | txn_id | customer_id | store_size | category | amount | txn_date |
# MAGIC |---|---|---|---|---|---|
# MAGIC | T1 | 501 | Large | Laptops | 1200.0 | 2025-01-05 |
# MAGIC | T2 | 502 | Medium | Phones | 800.0 | 2025-01-06 |
# MAGIC | T4 | 503 | Large | Laptops | 1500.0 | 2025-01-07 |

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # OrderBy and Limit
# MAGIC 1. Order `transactions_df` by `amount` descending.
# MAGIC 2. Limit the result to the top 2 records.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC | txn_id | customer_id | store_size | category | amount | txn_date |
# MAGIC |---|---|---|---|---|---|
# MAGIC | T4 | 503 | Large | Laptops | 1500.0 | 2025-01-07 |
# MAGIC | T4 | 503 | Large | Laptops | 1500.0 | 2025-01-07 |

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # Basic String Manipulation
# MAGIC 1. Convert `category` to uppercase.
# MAGIC 2. Get the substring of the first 3 characters of the new uppercase category.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC |category_upper|category_sub|
# MAGIC |---|---|
# MAGIC |LAPTOPS|LAP|
# MAGIC |PHONES|PHO|
# MAGIC |ACCESSORIES|ACC|

# COMMAND ----------



# COMMAND ----------

# MAGIC %md 
# MAGIC ### **Normal**

# COMMAND ----------

# MAGIC %md
# MAGIC # Coalesce Missing Values
# MAGIC 1. Use the `coalesce` function to replace null values in `store_size` with the literal string "Unknown".
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC | txn_id | store_size_clean |
# MAGIC |---|---|
# MAGIC | T3 | Unknown |

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # Date Splitting and Extraction
# MAGIC 1. Split the `txn_date` column by the hyphen "-".
# MAGIC 2. Use `getItem(1)` to extract the month into a new column.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC |txn_id|txn_date|month|
# MAGIC |---|---|---|
# MAGIC |T1|2025-01-05|01|
# MAGIC |T2|2025-01-06|01|
# MAGIC |T3|2025-01-06|01|
# MAGIC |T4|2025-01-07|01|
# MAGIC |T4|2025-01-07|01|

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # Union By Name with Missing Columns
# MAGIC 1. Select `txn_id` and `amount` from `transactions_df`.
# MAGIC 2. Union this with `refunds_df` which has `txn_id`, `customer_id`, and `refund_amount`.
# MAGIC 3. Allow missing columns so the schema merges properly.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC | txn_id | amount | customer_id | refund_amount |
# MAGIC |---|---|---|---|
# MAGIC | T1 | 1200.0 | null | null |
# MAGIC | T5 | null | 504 | 100.0 |

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # Date Math
# MAGIC 1. Convert `txn_date` to an actual DateType.
# MAGIC 2. Add 7 days to the date using `date_add`.
# MAGIC 3. Find the day of the week using `dayofweek`.
# MAGIC 4. Drop all duplicate record by using `distinct`
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC |txn_date|plus_7_days|day_of_week|
# MAGIC |---|---|---|
# MAGIC |2025-01-05|2025-01-12|1|
# MAGIC |2025-01-06|2025-01-13|2|
# MAGIC |2025-01-07|2025-01-14|3|

# COMMAND ----------



# COMMAND ----------

# MAGIC %md 
# MAGIC ### **Hard**

# COMMAND ----------

# MAGIC %md
# MAGIC # Window Function: Ranking
# MAGIC 1. Create a Window partitioned by `category` and ordered by `amount` descending.
# MAGIC 2. Calculate the `row_number()` and `dense_rank()` for each row within its category.
# MAGIC 3. Filter only category `Laptops`
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC | category | amount | row_num | d_rank |
# MAGIC |---|---|---|---|
# MAGIC | Laptops | 1500.0 | 1 | 1 |
# MAGIC | Laptops | 1500.0 | 2 | 1 |
# MAGIC | Laptops | 1200.0 | 3 | 2 |

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # Window Function: Lag and Lead
# MAGIC 1. Filter `transactions_df` for `customer_id` 501.
# MAGIC 2. Create a Window ordered by `txn_date`.
# MAGIC 3. Find the `lag` (previous) amount and `lead` (next) amount for this customer's purchases.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC |txn_date|amount|prev_amount|next_amount|
# MAGIC |---|---|---|---|
# MAGIC |2025-01-05|1200|null|50|
# MAGIC |2025-01-06|50|1200|null|

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # Collect Set and ExceptAll
# MAGIC 1. Group `transactions_df` by `category` and use `collect_set` on `customer_id`.
# MAGIC 2. Create another DataFrame of just category `Laptops` and its customer set. Use `exceptAll` to find categories *other* than `Laptops`.
# MAGIC
# MAGIC * **Expected Result (Grouping Output):**
# MAGIC |category|customer_ids|
# MAGIC |---|---|
# MAGIC |Accessories|[501]|
# MAGIC |Phones|[502]|

# COMMAND ----------

