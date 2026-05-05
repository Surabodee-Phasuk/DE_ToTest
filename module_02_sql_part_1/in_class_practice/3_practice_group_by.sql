-- Databricks notebook source
-- MAGIC %run ./_init_database

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### task_1 group by with different aggregation style
-- MAGIC   - 1.0 group by and count
-- MAGIC   - 1.1 group by and select min values
-- MAGIC   - 1.2 group by and select max valuse

-- COMMAND ----------

-- DBTITLE 1,group by
-- select
--   shop_id,
--   max(txn_date) as max_date,
--   sum(sale_amount) as sum_sales
-- from
--   session_2_sql.txn_shop
-- where
--   shop_id > 2
-- group by
--   shop_id

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### task_2 use having after group by to filter unncessery records
-- MAGIC   - 1.0 having if count > 1

-- COMMAND ----------

-- DBTITLE 1,group by with having
-- select
--   shop_id,
--   max(txn_date) as max_date,
--   sum(sale_amount) as sum_sales
-- from
--   session_2_sql.txn_shop
-- where
--   shop_id > 2
-- group by
--   shop_id
-- having
--   count(*) > 1