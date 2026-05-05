-- Databricks notebook source
create schema if not exists workspace.session_2_sql

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # **DDL statement**
-- MAGIC   - CREATE
-- MAGIC     - `TBLPROPERTIES (
-- MAGIC       'delta.columnMapping.mode' = 'name'
-- MAGIC       ,'delta.enableTypeWidening' = 'true'
-- MAGIC       )`
-- MAGIC     - `create table <table_name>` - create table
-- MAGIC     - `create or replace table <table_name>` - create table , if table exists overwrite
-- MAGIC     - `create table if not exists <table_name>` - not create table , if table exists
-- MAGIC   - ALTER
-- MAGIC     - `alter table <table_name> add <column_name> (<new_column_name> <data_type>)` add column
-- MAGIC     - `alter table <table_name> drop <column_name> (<drop_column_name>)` drop column
-- MAGIC     - `alter table <table_name> rename <column_name> <old_column_name> to <new_column_name>` rename column
-- MAGIC     - `alter table table_name alter column <col_name> type (<new_datatype>)` change datatype
-- MAGIC       - note: cannot convert every datatype
-- MAGIC   - TRUNCATE
-- MAGIC   - DROP

-- COMMAND ----------

create or replace table session_2_sql.txn_shop (
   shop_id int
  ,sale_amount int
  ,remarks string
  ,txn_date date
  ,is_active boolean
) TBLPROPERTIES (
    'delta.columnMapping.mode' = 'name'
    ,'delta.enableTypeWidening' = 'true'
  )

-- COMMAND ----------

-- DBTITLE 1,alter table
-- alter table session_2_sql.txn_shop add column (new_column string)
-- alter table session_2_sql.txn_shop drop column (shop_id)
-- alter table session_2_sql.txn_shop rename column sale_amount to sale_amount_new
-- alter table session_2_sql.txn_shop alter column sale_amount type bigint

-- COMMAND ----------

-- DBTITLE 1,insert into
INSERT INTO session_2_sql.txn_shop VALUES
  (1, 20, 'so good', '2025-01-01', TRUE),
  (2, 40, 'so good', '2025-01-01', TRUE),
  (2, 20, 'so good', '2025-01-01', TRUE),
  (3, 20, 'so good', '2025-01-01', TRUE),
  (4, 20, 'so good', '2025-01-01', TRUE),
  (5, null, 'so good', '2025-01-01', TRUE),
  (5, null, 'so good', '2025-01-08', TRUE),
  (6, 30, '', '2025-01-01', TRUE)

-- COMMAND ----------

-- DBTITLE 1,truncate
select * from session_2_sql.txn_shop
truncate table session_2_sql.txn_shop

-- COMMAND ----------

-- DBTITLE 1,drop table
drop table session_2_sql.txn_shop

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # **DML statement**
-- MAGIC

-- COMMAND ----------

-- DBTITLE 1,insert into
INSERT INTO session_2_sql.txn_shop VALUES
  (1, 20, 'so good', '2025-01-01', TRUE),
  (2, 20, 'so good', '2025-01-01', TRUE)

-- COMMAND ----------

-- DBTITLE 1,update statement
update session_2_sql.txn_shop set sale_amount = 100 , remarks = "so baddd" , txn_date = current_date() where shop_id = 1

-- COMMAND ----------

-- DBTITLE 1,delete statement
delete from session_2_sql.txn_shop where shop_id = 2

-- COMMAND ----------

-- DBTITLE 1,select statement
select remarks ,txn_date , "hello" as new_column from session_2_sql.txn_shop

-- COMMAND ----------

-- DBTITLE 1,where condition
-- select * from session_2_sql.txn_shop where shop_id = 1
-- select * from session_2_sql.txn_shop where shop_id in (1,2)
-- select * from session_2_sql.txn_shop where sale_amount like ('1%')
-- select * from session_2_sql.txn_shop where sale_amount like ('1_')
-- select * from session_2_sql.txn_shop where txn_date between "2024-01-01" and "2026-02-06"
-- select * from session_2_sql.txn_shop where sale_amount is not null
-- select * from session_2_sql.txn_shop where remarks = ''

-- COMMAND ----------

-- DBTITLE 1,order by , limit
select shop_id,sale_amount from session_2_sql.txn_shop where remarks = "so good" order by sale_amount desc limit 2

-- COMMAND ----------

-- DBTITLE 1,group by
select
  shop_id,
  max(txn_date) as max_date,
  sum(sale_amount) as sum_sales
from
  session_2_sql.txn_shop
where
  shop_id > 2
group by
  shop_id
having
  max(txn_date) = '2025-01-01'