-- Databricks notebook source
-- MAGIC %run ./_init_database

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # task_1 use select statement
-- MAGIC   - 1.0 select all column with *
-- MAGIC   - 1.1 select just only 1 column
-- MAGIC   - 1.2 select all column and add 1 more column with select statement  

-- COMMAND ----------

-- DBTITLE 1,select statement
-- select * from session_2_sql.txn_shop
-- select column_1 from session_2_sql.txn_shop
-- select * , "hello" as new_column from session_2_sql.txn_shop

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # task_2 use where statement
-- MAGIC   - 2.0 where condition with 1 element
-- MAGIC   - 2.1 where condiiton with multiple element (using IN statement)
-- MAGIC   - 2.2 where condition with wildcard (%,_)
-- MAGIC   - 2.3 where condition with between (date or number)
-- MAGIC   - 2.4 where null
-- MAGIC   - 2.5 where blank

-- COMMAND ----------

-- DBTITLE 1,shere statement
-- select * from session_2_sql.txn_shop where shop_id = 1
-- select * from session_2_sql.txn_shop where shop_id in (1,2)
-- select * from session_2_sql.txn_shop where sale_amount like ('1%')
-- select * from session_2_sql.txn_shop where sale_amount like ('1_')
-- select * from session_2_sql.txn_shop where txn_date between "2024-01-01" and "2026-02-06"
-- select * from session_2_sql.txn_shop where sale_amount is not null
-- select * from session_2_sql.txn_shop where remarks = ''

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # task_3 use order_by clause

-- COMMAND ----------

-- DBTITLE 1,order by
-- select shop_id,sale_amount from session_2_sql.txn_shop where remarks = "so good" order by sale_amount desc limit 2