# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *
from datetime import date,datetime

sales_schema = "transaction_id int, shop_id int, sales_amount double, transaction_date string, is_active int"
sales_data = [
    (101, 1, 1500.50, "2025-10-01", 1),
    (102, 2, 800.00, "2025-10-15", 0),
    (103, 1, 2100.75, "2025-11-05", 1),
    (104, 3, 300.00, "2025-11-20", 1)
]
sales_df = spark.createDataFrame(sales_data, schema=sales_schema)

shop_schema = "shop_id int, shop_name string, region string, promo_start_date date, promo_end_date date"
shop_data = [
    (1, "Tech Haven", "North", date(2025,10,1), date(2025,10,31)),
    (2, "Electro World", "South", date(2025,11,1), date(2025,11,30)),
    (4, "Gadget Hub", "West", date(2025,12,1), date(2025,12,31))
]
shop_name_df = spark.createDataFrame(shop_data, schema=shop_schema)

# COMMAND ----------

# MAGIC %md 
# MAGIC ### **Easy**

# COMMAND ----------

# MAGIC %md
# MAGIC # Basic Data Type Casting
# MAGIC 1. Select `transaction_id` and `sales_amount` from `sales_df`.
# MAGIC 2. Cast `sales_amount` to an integer.
# MAGIC 3. Cast `is_active` to a boolean.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC | transaction_id | sales_amount_int | is_active_bool |
# MAGIC |---|---|---|
# MAGIC | 101 | 1500 | true |
# MAGIC | 102 | 800 | false |
# MAGIC | 103 | 2100 | true |
# MAGIC | 104 | 300 | true |

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # Simple Inner Join
# MAGIC 1. Perform an inner join between `sales_df` and `shop_name_df` on `shop_id`.
# MAGIC 2. Select `transaction_id`, `shop_name`, and `sales_amount`.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC | transaction_id | shop_name | sales_amount |
# MAGIC |---|---|---|
# MAGIC | 101 | Tech Haven | 1500.5 |
# MAGIC | 103 | Tech Haven | 2100.75 |
# MAGIC | 102 | Electro World | 800.0 |

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # Creating a Struct Type
# MAGIC 1. Create a new DataFrame from `shop_name_df`.
# MAGIC 2. Combine `promo_start_date` and `promo_end_date` into a struct named `promo_period`.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC | shop_id | shop_name | promo_period |
# MAGIC |---|---|---|
# MAGIC | 1 | Tech Haven | {"promo_start_date":"2025-10-01","promo_end_date":"2025-10-31"} |
# MAGIC | 2 | Electro World | {"promo_start_date":"2025-11-01","promo_end_date":"2025-11-30"} |
# MAGIC | 4 | Gadget Hub | {"promo_start_date":"2025-12-01","promo_end_date":"2025-12-31"} |

# COMMAND ----------



# COMMAND ----------

# MAGIC %md 
# MAGIC ### **Normal**

# COMMAND ----------

# MAGIC %md
# MAGIC # Left Join vs Left Semi Join
# MAGIC 1. Perform a left join of `sales_df` (left) and `shop_name_df` (right) on `shop_id`.
# MAGIC 2. Perform a left semi join of the same DataFrames on `shop_id`.
# MAGIC 3. Display both results to observe the difference.
# MAGIC
# MAGIC * **Expected Result (Left Semi Join):**
# MAGIC | transaction_id | shop_id | sales_amount | transaction_date | is_active |
# MAGIC |---|---|---|---|---|
# MAGIC | 101 | 1 | 1500.5 | 2025-10-01 | 1 |
# MAGIC | 103 | 1 | 2100.75 | 2025-11-05 | 1 |
# MAGIC | 102 | 2 | 800.0 | 2025-10-15 | 0 |

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # Complex Date String Casting
# MAGIC 1. Convert the `transaction_date` string in `sales_df` to a proper DateType.
# MAGIC 2. Create a timestamp column by appending " 12:00:00" to `transaction_date` and casting it to timestamp.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC |transaction_id|date_cast|timestamp_cast|
# MAGIC |---|---|---|
# MAGIC |101|2025-10-01|2025-10-01T12:00:00.000+00:00|
# MAGIC |102|2025-10-15|2025-10-15T12:00:00.000+00:00|
# MAGIC |103|2025-11-05|2025-11-05T12:00:00.000+00:00|
# MAGIC |104|2025-11-20|2025-11-20T12:00:00.000+00:00|

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # Join With Date Between Condition
# MAGIC 1. Join `sales_df` and `shop_name_df` where `shop_id` matches.
# MAGIC 2. Add an additional join condition where `transaction_date` (cast to date) is between `promo_start_date` and `promo_end_date`.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC | transaction_id | shop_name | transaction_date |
# MAGIC |---|---|---|
# MAGIC | 101 | Tech Haven | 2025-10-01 |

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # Array and Map Generation
# MAGIC 1. Select `shop_name` from `shop_name_df`.
# MAGIC 2. Create an array containing `region` and `shop_name`.
# MAGIC 3. Create a map where the key is the string literal "region_code" and the value is `region`.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC |shop_name|location_array|region_map|
# MAGIC |---|---|---|
# MAGIC |Tech Haven|["North","Tech Haven"]|{"region_code":"North"}|
# MAGIC |Electro World|["South","Electro World"]|{"region_code":"South"}|
# MAGIC |Gadget Hub|["West","Gadget Hub"]|{"region_code":"West"}|

# COMMAND ----------



# COMMAND ----------

# MAGIC %md 
# MAGIC ### **Hard**

# COMMAND ----------

# MAGIC %md
# MAGIC # Multiple Condition Join in List Format
# MAGIC 1. Add a dummy `country_code` column with value "US" to both `sales_df` and `shop_name_df`.
# MAGIC 2. Join them using the list syntax format `[condition1, condition2]` for both `shop_id` and `country_code`.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC |transaction_id|shop_id|shop_name|country_code|
# MAGIC |---|---|---|---|
# MAGIC |103|1|Tech Haven|US|
# MAGIC |101|1|Tech Haven|US|
# MAGIC |102|2|Electro World|US|

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # Decimal Casting and Struct
# MAGIC 1. Cast `sales_amount` to `decimal(10,2)`.
# MAGIC 2. Create a struct containing the casted decimal and the integer cast of `is_active`.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC |transaction_id|transaction_metrics|
# MAGIC |---|---|
# MAGIC |101|{"sales_amount":"1500.50","is_active":1}|
# MAGIC |102|{"sales_amount":"800.00","is_active":0}|
# MAGIC |103|{"sales_amount":"2100.75","is_active":1}|
# MAGIC |104|{"sales_amount":"300.00","is_active":1}|

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # Complex Map with String Types
# MAGIC 1. Create a map from `sales_df` containing two key-value pairs. Key 1: literal 1, Value 1: `transaction_id`. Key 2: literal 2, Value 2: `transaction_date`.
# MAGIC 2. *Hint*: Map values must be of the same type, so cast `transaction_id` to string.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC |transaction_id|mixed_map|
# MAGIC |---|---|
# MAGIC |101|{"1":"101","2":"2025-10-01"}|
# MAGIC |102|{"1":"102","2":"2025-10-15"}|
# MAGIC |103|{"1":"103","2":"2025-11-05"}|
# MAGIC |104|{"1":"104","2":"2025-11-20"}|

# COMMAND ----------

