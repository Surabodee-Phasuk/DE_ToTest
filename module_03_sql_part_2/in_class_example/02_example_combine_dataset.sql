-- Databricks notebook source
-- MAGIC %run ./_init

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **table_name**: session_3_sql.shop_1_sales_transaction
-- MAGIC |txn_id|shop_id|quantity|txn_date|
-- MAGIC |---|---|---|---|
-- MAGIC |1|1|5|2026-02-01|
-- MAGIC |1|1|5|2026-02-01|
-- MAGIC |2|1|8|2026-02-01|
-- MAGIC |3|10|8|2026-02-02|
-- MAGIC |4|10|4|2026-02-02|

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **table_name**: session_3_sql.shop_2_sales_transaction
-- MAGIC |shop_id|txn_id|quantity|txn_date|
-- MAGIC |---|---|---|---|
-- MAGIC |2|1|7|2026-02-01|
-- MAGIC |2|1|7|2026-02-01|
-- MAGIC |2|2|8|2026-02-01|
-- MAGIC |2|3|2|2026-02-02|
-- MAGIC |2|4|3|2026-02-02|

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # Combining Two Datasets
-- MAGIC
-- MAGIC - **Union**: Combines datasets vertically (adds rows)
-- MAGIC   - `union`: Removes duplicate records
-- MAGIC   - `union all`: Keeps duplicate records
-- MAGIC
-- MAGIC - **Join**: Combines datasets horizontally (adds columns)
-- MAGIC   - `Inner Join`: Returns only matching records
-- MAGIC   - `Left Join`: Returns all records from the left dataset; unmatched columns from the right are null
-- MAGIC     - `Left Anti Join`: Returns only records from the left dataset that do not match any record in the right dataset
-- MAGIC     - `Left Semi Join`: Returns only records from the left dataset that have a match in the right dataset
-- MAGIC   - `Full Join`: Returns all matching and non-matching records from both datasets
-- MAGIC   - `Cross Join`: Returns the Cartesian product of both datasets

-- COMMAND ----------

-- DBTITLE 1,UNION: removes duplicates
select txn_id, shop_id, quantity, txn_date from session_3_sql.shop_1_sales_transaction
union
select txn_id, shop_id, quantity, txn_date from session_3_sql.shop_2_sales_transaction

-- COMMAND ----------

-- DBTITLE 1,UNION ALL: keeps duplicates
select txn_id, shop_id, quantity, txn_date from session_3_sql.shop_1_sales_transaction
union all
select shop_id, txn_id, quantity, txn_date from session_3_sql.shop_2_sales_transaction

-- COMMAND ----------

-- DBTITLE 1,INNER JOIN: only matching rows
select
  a.txn_id,
  a.shop_id,
  b.shop_name,
  a.quantity,
  a.txn_date
from
  session_3_sql.shop_1_sales_transaction a
    inner join session_3_sql.dim_shop_name b
    on a.shop_id = b.shop_id

-- COMMAND ----------

-- DBTITLE 1,LEFT JOIN: all rows from left, matching from right
select
  a.txn_id,
  a.shop_id,
  b.shop_name,
  a.quantity,
  a.txn_date
from
  session_3_sql.shop_1_sales_transaction a
    left join session_3_sql.dim_shop_name b
    on a.shop_id = b.shop_id

-- COMMAND ----------

-- DBTITLE 1,LEFT ANTI JOIN: rows in left not in right
select
  *
from
  session_3_sql.shop_1_sales_transaction a
    left anti join session_3_sql.dim_shop_name b
    on a.shop_id = b.shop_id

-- COMMAND ----------

-- DBTITLE 1,LEFT SEMI JOIN: rows in left with match in right
select
  *
from
  session_3_sql.shop_1_sales_transaction a
    left semi join session_3_sql.dim_shop_name b
    on a.shop_id = b.shop_id

-- COMMAND ----------

-- DBTITLE 1,FULL JOIN: all rows from both, matched where possible
select
  *
from
  session_3_sql.shop_1_sales_transaction a
    full join session_3_sql.dim_shop_name b
    on a.shop_id = b.shop_id

-- COMMAND ----------

-- DBTITLE 1,CROSS JOIN: all combinations
select
*
from
  session_3_sql.shop_1_sales_transaction a 
  cross join session_3_sql.shop_2_sales_transaction b