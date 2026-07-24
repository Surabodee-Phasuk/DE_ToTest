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

q1_df = transactions_df.dropDuplicates().dropna(subset=["store_size"])
display(q1_df)

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

q2_df = transactions_df.orderBy(col("amount").desc()).limit(2)
display(q2_df)

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

q3_df = transactions_df.select(
    upper(col("category")).alias("category_upper"),
    substring(upper(col("category")), 1, 3).alias("category_sub")
).dropDuplicates()
display(q3_df)

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

q4_df = transactions_df.select(
    "txn_id",
    coalesce(col("store_size"), lit("Unknown")).alias("store_size_clean")
)
display(q4_df.filter(col("txn_id") == "T3"))

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

q5_df = (
    transactions_df
    .withColumn("date_parts", split(col("txn_date"), "-"))
    .withColumn("month", col("date_parts").getItem(1))
    .select("txn_id", "txn_date", "month")
)
display(q5_df)

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

df1 = transactions_df.select("txn_id", "amount")
df2 = refunds_df

q6_df = df1.unionByName(df2, allowMissingColumns=True)
display(q6_df.filter(col("txn_id").isin("T1", "T5")))

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

q7_df = (
    transactions_df
    .withColumn("actual_date", to_date(col("txn_date")))
    .select(
        "txn_date",
        date_add(col("actual_date"), 7).alias("plus_7_days"),
        dayofweek(col("actual_date")).alias("day_of_week")
    )
    .distinct()
)
display(q7_df)

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

window_spec = Window.partitionBy("category").orderBy(col("amount").desc())

q8_df = (
    transactions_df
    .select(
        "category",
        "amount",
        row_number().over(window_spec).alias("row_num"),
        dense_rank().over(window_spec).alias("d_rank")
        )
    .filter(col("category") == "Laptops")
    )
display(q8_df)

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

window_spec_time = Window.orderBy("txn_date")

q9_df = (
    transactions_df.filter(col("customer_id") == 501)
    .select(
        "txn_date",
        "amount",
        lag("amount", 1).over(window_spec_time).alias("prev_amount"),
        lead("amount", 1).over(window_spec_time).alias("next_amount")
    )
)
display(q9_df)

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

grouped_df = transactions_df.groupBy("category").agg(collect_set("customer_id").alias("customer_ids"))

laptops_only = grouped_df.filter(col("category") == "Laptops")
except_df = grouped_df.exceptAll(laptops_only)

display(except_df)