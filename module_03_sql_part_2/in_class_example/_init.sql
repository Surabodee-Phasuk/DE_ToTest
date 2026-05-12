-- Databricks notebook source
create schema if not exists workspace.session_3_sql

-- COMMAND ----------

create or replace table session_3_sql.shop_1_sales_transaction (
  txn_id int,
  shop_id int,
  quantity int,
  txn_date date
);

insert into session_3_sql.shop_1_sales_transaction
  values
    (1, 1, 5, '2026-02-01'),
    (1, 1, 5, '2026-02-01'),
    (2, 1, 8, '2026-02-01'),
    (3, 10, 8, '2026-02-02'),
    (4, 10, 4, '2026-02-02');

create or replace table session_3_sql.shop_2_sales_transaction (
  shop_id int,
  txn_id int,
  quantity int,
  txn_date date
);

insert into session_3_sql.shop_2_sales_transaction
  values
    (2, 1, 7, '2026-02-01'),
    (2, 1, 7, '2026-02-01'),
    (2, 2, 8, '2026-02-01'),
    (2, 3, 2, '2026-02-02'),
    (2, 4, 3, '2026-02-02');

create or replace table session_3_sql.dim_shop_name (
  shop_id int,
  shop_name string,
  update_date date
);

insert into session_3_sql.dim_shop_name values
(1, '@pitishop', '2026-01-01'),
(2, '@valentino', '2026-01-01'),
(3, '@datasparkTH', '2026-01-01');

create or replace table session_3_sql.profit_each_year (
  sales_year int,
  shop_name string,
  profit_baht int
);

insert into session_3_sql.profit_each_year values
(2022, '@pitishop', 5000),
(2023, '@pitishop', 1000),
(2024, '@pitishop', 7000),
(2025, '@pitishop', 10000),
(2022, '@valentino', 5000),
(2023, '@valentino', 1000),
(2024, '@valentino', 7000),
(2025, '@valentino', 10000)


-- COMMAND ----------

-- MAGIC %python
-- MAGIC print(
-- MAGIC     """
-- MAGIC these schema has been created
-- MAGIC workspace.session_3_sql
-- MAGIC
-- MAGIC these table has been created
-- MAGIC session_3_sql.shop_1_sales_transaction
-- MAGIC session_3_sql.shop_2_sales_transaction
-- MAGIC session_3_sql.dim_shop_name
-- MAGIC session_3_sql.profit_each_year
-- MAGIC     """
-- MAGIC     )