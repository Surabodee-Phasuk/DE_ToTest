-- Databricks notebook source
-- MAGIC %run ./_init

-- COMMAND ----------

-- MAGIC %md
-- MAGIC | Function | Detail |
-- MAGIC | :--- | :--- |
-- MAGIC | **SUM(quantity) OVER (PARTITION BY shop_id)** | Calculates the total quantity for the specific `shop_id`. |
-- MAGIC | **SUM(quantity) OVER (PARTITION BY shop_id ORDER BY txn_id)** | Calculates a Running Total (Cumulative Sum) for the shop, accumulating by `txn_id`. |
-- MAGIC | **RANK() OVER (PARTITION BY shop_id ORDER BY quantity DESC)** | Ranks transactions by quantity from highest to lowest. Ties get the same rank, and the next rank is skipped (e.g., 1, 1, 3). |
-- MAGIC | **DENSE_RANK() OVER (PARTITION BY shop_id ORDER BY txn_date)** | Ranks transactions by date. Ties get the same rank, and the next rank is not skipped (e.g., 1, 1, 2). |
-- MAGIC | **ROW_NUMBER() OVER (PARTITION BY shop_id ORDER BY txn_date, txn_id)** | Assigns a unique sequential integer to every row within the shop partition. |
-- MAGIC | **AVG(quantity) OVER (PARTITION BY shop_id)** | Calculates the average transaction size for that shop. |
-- MAGIC | **MAX(quantity) OVER (PARTITION BY txn_date)** | Finds the highest quantity sold on that specific date across all data (since the partition is `txn_date`, not `shop_id`). |
-- MAGIC | **MIN(quantity) OVER (PARTITION BY txn_id)** | Finds the minimum quantity for that specific transaction ID. *Note: If `txn_id` is unique, this simply returns the quantity itself.* |
-- MAGIC | **COUNT(*) OVER (PARTITION BY shop_id)** | Counts the total number of transactions associated with that shop. |
-- MAGIC | **LAG(quantity, 1) OVER (PARTITION BY shop_id ORDER BY txn_date)** | Returns the quantity from the *previous* row in the partition. Useful for calculating changes (e.g., "Growth since last sale"). |
-- MAGIC | **LEAD(quantity, 1) OVER (PARTITION BY shop_id ORDER BY txn_date)** | Returns the quantity from the *next* row in the partition. Useful for peeking ahead at upcoming values. |

-- COMMAND ----------

-- DBTITLE 1,window function with cte
with all_sales_transaction as (
  select txn_id,shop_id,quantity,txn_date from session_3_sql.shop_1_sales_transaction
  union all
  select txn_id,shop_id,quantity,txn_date from session_3_sql.shop_2_sales_transaction
)

SELECT
  shop_id,
  txn_id,
  quantity,
  txn_date,
  LAG(quantity) OVER (PARTITION BY shop_id ORDER BY txn_date),
  LEAD(quantity) OVER (PARTITION BY shop_id ORDER BY txn_date),
  SUM(quantity) OVER (PARTITION BY shop_id),
  SUM(quantity) OVER (PARTITION BY shop_id ORDER BY  txn_id),
  RANK() OVER (PARTITION BY shop_id ORDER BY quantity DESC),
  DENSE_RANK() OVER (PARTITION BY shop_id ORDER BY txn_date),
  ROW_NUMBER() OVER (PARTITION BY shop_id ORDER BY txn_date, txn_id),
  AVG(quantity) OVER (PARTITION BY shop_id),
  MAX(quantity) OVER (PARTITION BY txn_date),
  MIN(quantity) OVER (PARTITION BY txn_id),
  COUNT(*) OVER (PARTITION BY shop_id)
FROM all_sales_transaction


-- COMMAND ----------

-- DBTITLE 1,window function with subquery
SELECT
  shop_id,
  txn_id,
  quantity,
  txn_date,
  LAG(quantity) OVER (PARTITION BY shop_id ORDER BY txn_date),
  LEAD(quantity) OVER (PARTITION BY shop_id ORDER BY txn_date),
  SUM(quantity) OVER (PARTITION BY shop_id),
  SUM(quantity) OVER (PARTITION BY shop_id ORDER BY  txn_id),
  RANK() OVER (PARTITION BY shop_id ORDER BY quantity DESC),
  DENSE_RANK() OVER (PARTITION BY shop_id ORDER BY txn_date),
  ROW_NUMBER() OVER (PARTITION BY shop_id ORDER BY txn_date, txn_id),
  AVG(quantity) OVER (PARTITION BY shop_id),
  MAX(quantity) OVER (PARTITION BY txn_date),
  MIN(quantity) OVER (PARTITION BY txn_id),
  COUNT(*) OVER (PARTITION BY shop_id)
FROM (select txn_id,shop_id,quantity,txn_date from session_3_sql.shop_1_sales_transaction
  union all
  select txn_id,shop_id,quantity,txn_date from session_3_sql.shop_2_sales_transaction)

-- COMMAND ----------

-- DBTITLE 1,cte simple version
with rn_result as (
  select
    *,
    row_number() over (partition by shop_id order by quantity desc) as rn
  from
    session_3_sql.shop_1_sales_transaction
)

select
  * except (rn)
from
  rn_result
where
  rn = 1

-- COMMAND ----------

-- DBTITLE 1,sub_query window function
select
  * except (rn)
from
  (
    select
      *,
      row_number() over (partition by shop_id order by quantity desc) as rn
    from
      session_3_sql.shop_1_sales_transaction
  )
where
  rn = 1

-- COMMAND ----------

SELECT 
  *
FROM sales_transactions
QUALIFY ROW_NUMBER() OVER (PARTITION by shop_id ORDER BY order_date DESC) = 1

-- COMMAND ----------

WITH temp AS (
  SELECT 
  *
  , ROW_NUMBER() OVER(PARTITION by shop_id ORDER BY order_date DESC) AS rn 
FROM sales_transactions
)
select * from temp
where rn = 1

-- COMMAND ----------



-- COMMAND ----------

insert into sales_transactions values 
("1", "2026-01-01", 20)
, ("1", "2026-01-02", 30)
, ("2", "2026-01-01", 10)
, ("2", "2026-01-02", 15)

-- COMMAND ----------



-- COMMAND ----------

select
    shop_id, quantity, txn_date,
    row_number() over(partition by shop_id order by txn_date) as rn
from
    session_3_sql.shop_1_sales_transaction

-- COMMAND ----------

-- DBTITLE 1,qualify
select
    *
  from
    session_3_sql.shop_1_sales_transaction
  qualify row_number() over (partition by shop_id order by quantity desc) = 1