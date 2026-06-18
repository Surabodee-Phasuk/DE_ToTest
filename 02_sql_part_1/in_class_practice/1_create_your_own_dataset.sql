-- Databricks notebook source
-- MAGIC %run ./_init_database

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # task_1 create your own dataset (table)
-- MAGIC   - have atleast 4 columns
-- MAGIC     - 1 id column (int)
-- MAGIC     - 1 date column (date)
-- MAGIC     - 1 boolean column (boolean)

-- COMMAND ----------

-- DBTITLE 1,create statement
-- example
create table session_2_sql.sample_dataset (
  id int,
  item_id int,
  remarks string,
  create_date date,
  is_active boolean
)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # task_2 insert data to dataset(table)
-- MAGIC   - atleast 4 records
-- MAGIC     - 1 record contain null (any column)
-- MAGIC     - 1 record contain blank (any column)

-- COMMAND ----------

-- DBTITLE 1,insert statement
insert into session_2_sql.sample_dataset values 
  (1, 11, 'good', '2020-01-01', true),
  (2, 12, 'very_good', '2025-01-01', true),
  (2, 12, null, '2025-01-01', true),
  (2, 12, "", '2025-01-01', true)
