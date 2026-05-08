-- Databricks notebook source
-- MAGIC %md
-- MAGIC ### **1. Table Initialization**
-- MAGIC * **Task:**
-- MAGIC   1. Create `session_2_sql.txn_agg_lab` with columns `shop_id` (int), `sales` (int), and `txn_date` (date).
-- MAGIC   2. Load the complete aggregate test dataset.

-- COMMAND ----------

CREATE OR REPLACE TABLE session_2_sql.txn_agg_lab (
  shop_id int, 
  sales int, 
  txn_date date
);

INSERT INTO session_2_sql.txn_agg_lab VALUES 
  (1, 10, '2025-01-01'), (1, 20, '2025-01-01'), (1, 30, '2025-01-01'), (1, 5, '2025-01-05'),
  (2, 20, '2025-01-02'), (2, 40, '2025-01-02'),
  (3, 500, '2025-01-10'), (3, 250, '2025-01-10'),
  (4, NULL, '2025-02-01'), (4, NULL, '2025-02-02'),
  (5, 100, '2026-03-01');

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### **Easy**

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **2. Basic Transaction Counts**
-- MAGIC * **Task:**
-- MAGIC   1. Select `shop_id`.
-- MAGIC   2. Count the total number of transaction records for each shop using `count(*)`.
-- MAGIC   3. Group the output by `shop_id`.
-- MAGIC * **Expected Result:**
-- MAGIC |shop_id|count(*)|
-- MAGIC |---|---|
-- MAGIC |1|4|
-- MAGIC |2|2|
-- MAGIC |3|2|
-- MAGIC |4|2|
-- MAGIC |5|1|

-- COMMAND ----------

SELECT shop_id, count(*) FROM session_2_sql.txn_agg_lab GROUP BY shop_id;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **3. Simple Financial Summary**
-- MAGIC * **Task:**
-- MAGIC   1. Calculate the `SUM` of `sales` grouped by `shop_id`.
-- MAGIC   2. Alias the sum column as `total_sales`.
-- MAGIC   3. Filter the aggregated list for `shop_id` values 1 and 2.
-- MAGIC * **Expected Result:**
-- MAGIC | shop_id | total_sales |
-- MAGIC |---|---|
-- MAGIC | 1 | 65 |
-- MAGIC | 2 | 60 |

-- COMMAND ----------


SELECT shop_id, SUM(sales) AS total_sales 
FROM session_2_sql.txn_agg_lab 
WHERE shop_id IN (1, 2)
GROUP BY shop_id;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **4. Latest Activity Review**
-- MAGIC * **Task:**
-- MAGIC   1. Retrieve the `MAX(txn_date)` for each shop.
-- MAGIC   2. Alias the result as `latest_transaction`.
-- MAGIC   3. Group by `shop_id`.
-- MAGIC * **Expected Result:**
-- MAGIC |shop_id|latest_transaction|
-- MAGIC |---|---|
-- MAGIC |1|2025-01-05|
-- MAGIC |2|2025-01-02|
-- MAGIC |3|2025-01-10|
-- MAGIC |4|2025-02-02|
-- MAGIC |5|2026-03-01|

-- COMMAND ----------


SELECT shop_id, MAX(txn_date) AS latest_transaction FROM session_2_sql.txn_agg_lab GROUP BY shop_id;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### **Normal**

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **5. Pre-Aggregation Filter Performance**
-- MAGIC * **Task:**
-- MAGIC   1. Apply a `WHERE` clause to filter for records where `shop_id` is greater than 2.
-- MAGIC   2. Calculate the total `SUM(sales)` for these specific shops.
-- MAGIC   3. Group the output by `shop_id`.
-- MAGIC * **Expected Result:**
-- MAGIC | shop_id | sum(sales) |
-- MAGIC |---|---|
-- MAGIC | 3 | 750 |
-- MAGIC | 4 | NULL |
-- MAGIC | 5 | 100 |

-- COMMAND ----------


SELECT shop_id, SUM(sales) 
FROM session_2_sql.txn_agg_lab 
WHERE shop_id > 2 
GROUP BY shop_id;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **6. Multi-Metric Performance Grid**
-- MAGIC * **Task:**
-- MAGIC   1. Select `shop_id`.
-- MAGIC   2. Calculate `MIN(sales)`, `MAX(sales)`, and `SUM(sales)` in a single query.
-- MAGIC   3. Group the entire result grid by `shop_id`.
-- MAGIC * **Expected Result:**
-- MAGIC |shop_id|MIN(sales)|MAX(sales)|SUM(sales)|
-- MAGIC |---|---|---|---|
-- MAGIC |1|5|30|65|
-- MAGIC |2|20|40|60|
-- MAGIC |3|250|500|750|
-- MAGIC |4|null|null|null|
-- MAGIC |5|100|100|100|

-- COMMAND ----------

SELECT shop_id, MIN(sales), MAX(sales), SUM(sales)
FROM session_2_sql.txn_agg_lab 
GROUP BY shop_id;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **7. Daily Shop Reporting**
-- MAGIC * **Task:**
-- MAGIC   1. Group your results by BOTH `shop_id` and `txn_date`.
-- MAGIC   2. Calculate the total `SUM(sales)` for each combination.
-- MAGIC   3. Order the results by `txn_date` descending.
-- MAGIC * **Expected Result:**
-- MAGIC |shop_id|txn_date|SUM(sales)|
-- MAGIC |---|---|---|
-- MAGIC |5|2026-03-01|100|
-- MAGIC |4|2025-02-02|null|
-- MAGIC |4|2025-02-01|null|
-- MAGIC |3|2025-01-10|750|
-- MAGIC |1|2025-01-05|5|
-- MAGIC |2|2025-01-02|60|
-- MAGIC |1|2025-01-01|60|

-- COMMAND ----------


SELECT shop_id, txn_date, SUM(sales) 
FROM session_2_sql.txn_agg_lab 
GROUP BY shop_id, txn_date
ORDER BY txn_date DESC;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **8. Data Integrity Audit**
-- MAGIC * **Task:**
-- MAGIC   1. Use a `WHERE` clause to exclude any rows where `sales` is NULL.
-- MAGIC   2. Group by `shop_id`.
-- MAGIC   3. Count how many valid (non-null) transactions each shop has.
-- MAGIC * **Expected Result:**
-- MAGIC | shop_id | count(*) |
-- MAGIC |---|---|
-- MAGIC | 1 | 4 |
-- MAGIC | 2 | 2 |
-- MAGIC | 3 | 2 |
-- MAGIC | 5 | 1 |

-- COMMAND ----------


SELECT shop_id, COUNT(*) 
FROM session_2_sql.txn_agg_lab 
WHERE sales IS NOT NULL 
GROUP BY shop_id;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **9. Sorted Revenue Leaderboard**
-- MAGIC * **Task:**
-- MAGIC   1. Calculate the total `SUM(sales)` grouped by `shop_id`.
-- MAGIC   2. Order the list by the total sales in descending order.
-- MAGIC   3. Limit the result set to the top 3 highest-earning shops.
-- MAGIC * **Expected Result:**
-- MAGIC | shop_id | sum(sales) |
-- MAGIC |---|---|
-- MAGIC | 3 | 750 |
-- MAGIC | 5 | 100 |
-- MAGIC | 1 | 65 |

-- COMMAND ----------


SELECT shop_id, SUM(sales) 
FROM session_2_sql.txn_agg_lab 
GROUP BY shop_id 
ORDER BY SUM(sales) DESC
LIMIT 3;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### **Hard**

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **10. Post-Aggregation Thresholds (HAVING)**
-- MAGIC * **Task:**
-- MAGIC   1. Aggregate the total sales by `shop_id`.
-- MAGIC   2. Alias the sum column as `high_revenue`.
-- MAGIC   3. Use the `HAVING` clause to only display shops where the total sum is greater than 100.
-- MAGIC * **Expected Result:**
-- MAGIC | shop_id | high_revenue |
-- MAGIC |---|---|
-- MAGIC | 3 | 750 |

-- COMMAND ----------


SELECT shop_id, SUM(sales) AS high_revenue 
FROM session_2_sql.txn_agg_lab 
GROUP BY shop_id 
HAVING SUM(sales) > 100;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **11. Average Transaction Quality Control**
-- MAGIC * **Task:**
-- MAGIC   1. Calculate the average `AVG(sales)` for each shop.
-- MAGIC   2. Apply a `WHERE` filter to only look at shops with `shop_id < 5`.
-- MAGIC   3. Use `HAVING` to only show results where the average sale is strictly above 50.
-- MAGIC * **Expected Result:**
-- MAGIC | shop_id | avg(sales) |
-- MAGIC |---|---|
-- MAGIC | 3 | 375.0 |

-- COMMAND ----------


SELECT shop_id, AVG(sales) 
FROM session_2_sql.txn_agg_lab 
WHERE shop_id < 5 
GROUP BY shop_id 
HAVING AVG(sales) > 50;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **12. Recent Performance Review**
-- MAGIC * **Task:**
-- MAGIC   1. Identify the latest transaction date for each shop using `MAX(txn_date)`.
-- MAGIC   2. Group the output by `shop_id`.
-- MAGIC   3. Use `HAVING` to strictly filter for shops whose latest transaction was after '2025-01-31'.
-- MAGIC * **Expected Result:**
-- MAGIC | shop_id | max(txn_date) |
-- MAGIC |---|---|
-- MAGIC | 4 | 2025-02-02 |
-- MAGIC | 5 | 2026-03-01 |

-- COMMAND ----------


SELECT shop_id, MAX(txn_date) 
FROM session_2_sql.txn_agg_lab 
GROUP BY shop_id 
HAVING MAX(txn_date) > '2025-01-31';

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **13. Error Entry Tracking**
-- MAGIC * **Task:**
-- MAGIC   1. Use a `WHERE` clause to target rows where the `sales` value is NULL.
-- MAGIC   2. Group by `shop_id` and count the number of these NULL entries.
-- MAGIC   3. Use a `HAVING` clause to only show shops that have more than 1 NULL entry.
-- MAGIC * **Expected Result:**
-- MAGIC | shop_id | null_count |
-- MAGIC |---|---|
-- MAGIC | 4 | 2 |

-- COMMAND ----------


SELECT shop_id, COUNT(*) AS null_count 
FROM session_2_sql.txn_agg_lab 
WHERE sales IS NULL 
GROUP BY shop_id 
HAVING COUNT(*) > 1;