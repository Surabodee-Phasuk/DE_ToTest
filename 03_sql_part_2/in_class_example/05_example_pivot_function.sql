-- Databricks notebook source
-- MAGIC %run ./_init

-- COMMAND ----------

-- MAGIC %md
-- MAGIC as-is
-- MAGIC |sales_year|shop_name|profit_baht|
-- MAGIC |---|---|---|
-- MAGIC |2022|@pitishop|5000|
-- MAGIC |2023|@pitishop|1000|
-- MAGIC |2024|@pitishop|7000|
-- MAGIC |2025|@pitishop|10000|
-- MAGIC |2022|@valentino|5000|
-- MAGIC |2023|@valentino|1000|
-- MAGIC |2024|@valentino|7000|
-- MAGIC |2025|@valentino|10000|

-- COMMAND ----------

-- MAGIC %md
-- MAGIC to-be
-- MAGIC |sales_year|@pitishop|@valentino|
-- MAGIC |---|---|---|
-- MAGIC |2022|5000|5000|
-- MAGIC |2023|1000|1000|
-- MAGIC |2024|7000|7000|
-- MAGIC |2025|10000|10000|

-- COMMAND ----------

select * from session_3_sql.profit_each_year pivot (sum(profit_baht) for shop_name in ('@pitishop','@valentino'))

-- COMMAND ----------

select * from session_3_sql.profit_each_year 

-- COMMAND ----------

select * from session_3_sql.profit_each_year pivot (sum(profit_baht) for shop_name in ('@pitishop','@valentino'))

-- COMMAND ----------

-- MAGIC %python
-- MAGIC import ast
-- MAGIC
-- MAGIC a = [{"key_1": "value_2"}, {"key_2": "value_3"}]
-- MAGIC
-- MAGIC spark.createDataFrame(a).createTempView("test")

-- COMMAND ----------

select * from test