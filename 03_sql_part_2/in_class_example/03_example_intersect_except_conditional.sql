-- Databricks notebook source
-- MAGIC %md
-- MAGIC # INTERSECT
-- MAGIC   - **INTERSECT ALL**: Returns all rows that are **present** in both queries, including duplicates.
-- MAGIC   - **INTERSECT**: Returns distinct rows that are **present** in both queries.

-- COMMAND ----------

-- DBTITLE 1,intersect all
(select 'a' as letter, 1 as num
union all
select 'b', 2
union all
select 'b', 2
union all
select 'c', 3
union all
select 'c', 3)

intersect all

(select 'b', 2
union all
select 'b', 2
union all
select 'd', 4)

-- COMMAND ----------

-- DBTITLE 1,intersect
(select 'a' as letter, 1 as num
union all
select 'a' as letter, 1 as num
union all
select 'b' as letter, 2 as num)

intersect

(select 'a', 1
union all
select 'a', 1
union all
select 'b', 2
union all
select 'c', 2
)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # EXCEPT
-- MAGIC   - **EXCEPT ALL**: Returns all rows from the first query that are **not present** in the second query, including duplicates.
-- MAGIC   - **EXCEPT**: Returns distinct rows from the first query that are **not present** in the second query.

-- COMMAND ----------

-- DBTITLE 1,except all
(select 'a' as letter, 1 as num
union all
select 'b', 2
union all
select 'b', 2
union all
select 'c', 3
union all
select 'c', 3)

except all

(select 'b', 2
union all
select 'd', 4)

-- COMMAND ----------

-- DBTITLE 1,except
(select 'a' as letter, 1 as num
union all
select 'b', 2
union all
select 'b', 2
union all
select 'c', 3
union all
select 'c', 3)

except

(select 'b', 2
union all
select 'd', 4)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### conditional expression

-- COMMAND ----------

select *, case when quantity > 5 then 'high' else 'low' end as quantity_level from session_3_sql.shop_1_sales_transaction