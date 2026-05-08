-- Databricks notebook source
-- MAGIC %md
-- MAGIC ### **1. Table Initialization**
-- MAGIC * **Task:** 
-- MAGIC   1. Create the dedicated table `session_2_sql.txn_dml_lab`.
-- MAGIC   2. Load all required test data for the exercises.

-- COMMAND ----------

CREATE OR REPLACE TABLE session_2_sql.txn_dml_lab (
  shop_id int, 
  amount int, 
  status string, 
  txn_date date
);

INSERT INTO session_2_sql.txn_dml_lab VALUES 
  (1, 100, 'active', '2025-01-01'),
  (2, 200, 'pending', '2025-01-02'),
  (3, 50, 'active', '2025-01-03'),
  (4, 150, 'active', '2025-01-04'),
  (5, NULL, 'archived', '2025-01-05'),
  (6, NULL, 'pending', '2025-01-06'),
  (10, 300, 'active', '2026-03-01'),
  (11, 10, 'open', '2025-05-01'),
  (12, 15, 'open', '2025-05-02'),
  (13, 0, 'locked', '2025-05-03');

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### **Easy**

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **2. Selective Retrieval & Formatting**
-- MAGIC * **Task:**
-- MAGIC   1. Select the `amount` and `status` columns.
-- MAGIC   2. Create a static column containing the text "LOCAL" aliased as `region`.
-- MAGIC   3. Filter the results to only show the record for `shop_id = 1`.
-- MAGIC * **Expected Result:**
-- MAGIC | amount | status | region |
-- MAGIC |---|---|---|
-- MAGIC | 100 | active | LOCAL |

-- COMMAND ----------


SELECT amount, status, 'LOCAL' AS region 
FROM session_2_sql.txn_dml_lab 
WHERE shop_id = 1;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **3. Basic Data Maintenance**
-- MAGIC * **Task:**
-- MAGIC   1. Delete the record where `shop_id = 2`.
-- MAGIC   2. Select all columns where the status is 'active'.
-- MAGIC   3. Sort the output by `shop_id` ascending.
-- MAGIC * **Expected Result:**
-- MAGIC | shop_id | amount | status | txn_date |
-- MAGIC |---|---|---|---|
-- MAGIC | 1 | 100 | active | 2025-01-01 |
-- MAGIC | 3 | 50 | active | 2025-01-03 |
-- MAGIC | ... | ... | ... | ... |

-- COMMAND ----------

DELETE FROM session_2_sql.txn_dml_lab WHERE shop_id = 2;

SELECT * FROM session_2_sql.txn_dml_lab WHERE status = 'active' ORDER BY shop_id ASC;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### **Normal**

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **4. Range and List Filtering**
-- MAGIC * **Task:**
-- MAGIC   1. Select all columns from `txn_dml_lab`.
-- MAGIC   2. Filter where the `amount` is between 80 and 160.
-- MAGIC   3. Ensure the `shop_id` is specifically in the list `(1, 4)`.
-- MAGIC * **Expected Result:**
-- MAGIC | shop_id | amount | status | txn_date |
-- MAGIC |---|---|---|---|
-- MAGIC | 1 | 100 | active | 2025-01-01 |
-- MAGIC | 4 | 150 | active | 2025-01-04 |

-- COMMAND ----------

SELECT * FROM session_2_sql.txn_dml_lab 
WHERE amount BETWEEN 80 AND 160 
AND shop_id IN (1, 4);

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **5. Multi-Column Record Update**
-- MAGIC * **Task:**
-- MAGIC   1. Update the record for `shop_id = 1`.
-- MAGIC   2. Change `status` to 'verified', `amount` to 120, and `txn_date` to '2025-02-01'.
-- MAGIC   3. Select the row for `shop_id = 1` to verify the changes.
-- MAGIC * **Expected Result:**
-- MAGIC | shop_id | amount | status | txn_date |
-- MAGIC |---|---|---|---|
-- MAGIC | 1 | 120 | verified | 2025-02-01 |

-- COMMAND ----------

UPDATE session_2_sql.txn_dml_lab
SET status = 'verified', amount = 120, txn_date = '2025-02-01' 
WHERE shop_id = 1;

SELECT * FROM session_2_sql.txn_dml_lab WHERE shop_id = 1;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **6. Advanced Wildcard Pattern Matching**
-- MAGIC * **Task:**
-- MAGIC   1. Use `LIKE` with `%` to find statuses starting with 'a'.
-- MAGIC   2. Use `LIKE` with `_` to ensure the status is at least 8 characters long.
-- MAGIC   3. Select the `shop_id` and `status` for matching rows.
-- MAGIC * **Expected Result:**
-- MAGIC | shop_id | status |
-- MAGIC |---|---|
-- MAGIC | 5 | archived |

-- COMMAND ----------

SELECT shop_id, status FROM session_2_sql.txn_dml_lab 
WHERE status LIKE 'a%' AND status LIKE '________%';

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **7. Handling Nulls and Static Logic**
-- MAGIC * **Task:**
-- MAGIC   1. Select all rows where `amount` is NOT NULL.
-- MAGIC   2. Add a column `is_valid` that contains the boolean TRUE for these records.
-- MAGIC   3. Limit the results to 3 rows.
-- MAGIC * **Expected Result:**
-- MAGIC | shop_id | amount | is_valid |
-- MAGIC |---|---|---|
-- MAGIC | 1 | 120 | true |
-- MAGIC | 3 | 50 | true |
-- MAGIC | 4 | 150 | true |

-- COMMAND ----------

SELECT shop_id, amount, TRUE AS is_valid 
FROM session_2_sql.txn_dml_lab 
WHERE amount IS NOT NULL
LIMIT 3;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **8. Conditional Bulk Cleanup**
-- MAGIC * **Task:**
-- MAGIC   1. Use `DELETE` to remove any record where `amount` is NULL.
-- MAGIC   2. Use `DELETE` to remove any record with a status of 'verified'.
-- MAGIC   3. Select the count of remaining rows in the table.
-- MAGIC * **Expected Result:**
-- MAGIC | count(1) |
-- MAGIC |---|
-- MAGIC | 6 |

-- COMMAND ----------

DELETE FROM session_2_sql.txn_dml_lab WHERE amount IS NULL;
DELETE FROM session_2_sql.txn_dml_lab WHERE status = 'verified';

SELECT count(*) FROM session_2_sql.txn_dml_lab;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### **Hard**

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **9. Top-Tier Performance Analysis**
-- MAGIC * **Task:**
-- MAGIC   1. Select all columns and order them by `amount` in descending order.
-- MAGIC   2. Use the `LIMIT` clause to only show the top 2 highest amounts.
-- MAGIC   3. Ensure the results only include records where the status is NOT NULL.
-- MAGIC * **Expected Result:**
-- MAGIC | shop_id | amount | status |
-- MAGIC |---|---|---|
-- MAGIC | 10 | 300 | active |
-- MAGIC | 4 | 150 | active |

-- COMMAND ----------

SELECT shop_id, amount, status 
FROM session_2_sql.txn_dml_lab 
WHERE status IS NOT NULL 
ORDER BY amount DESC 
LIMIT 2;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **10. Time-Based Analysis**
-- MAGIC * **Task:**
-- MAGIC   1. Select all columns where the `txn_date` is after '2025-12-31'.
-- MAGIC   2. Filter for amounts that are strictly greater than 0.
-- MAGIC   3. Order by `txn_date` ascending.
-- MAGIC * **Expected Result:**
-- MAGIC | shop_id | txn_date | amount |
-- MAGIC |---|---|---|
-- MAGIC | 10 | 2026-03-01 | 300 |

-- COMMAND ----------

SELECT shop_id, txn_date, amount 
FROM session_2_sql.txn_dml_lab 
WHERE txn_date > '2025-12-31' 
AND amount > 0
ORDER BY txn_date ASC;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **11. Data Restoration Simulation**
-- MAGIC * **Task:**
-- MAGIC   1. Use `UPDATE` to set the status of `shop_id = 3` to 'restored'.
-- MAGIC   2. Set the `amount` for shop 3 to 999.
-- MAGIC   3. Select the `shop_id`, `amount`, and `status` for shop 3.
-- MAGIC * **Expected Result:**
-- MAGIC | shop_id | amount | status |
-- MAGIC |---|---|---|
-- MAGIC | 3 | 999 | restored |

-- COMMAND ----------

UPDATE session_2_sql.txn_dml_lab SET status = 'restored', amount = 999 WHERE shop_id = 3;

SELECT shop_id, amount, status FROM session_2_sql.txn_dml_lab WHERE shop_id = 3;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **12. Multi-Shop Verification**
-- MAGIC * **Task:**
-- MAGIC   1. Select shops that have an 'open' or 'locked' status.
-- MAGIC   2. Use an `IN` clause to filter for `shop_id` values 11, 12, or 13.
-- MAGIC   3. Order the final output by `amount` descending.
-- MAGIC * **Expected Result:**
-- MAGIC | shop_id | status | amount |
-- MAGIC |---|---|---|
-- MAGIC | 12 | open | 15 |
-- MAGIC | 11 | open | 10 |
-- MAGIC | 13 | locked | 0 |

-- COMMAND ----------

SELECT shop_id, status, amount
FROM session_2_sql.txn_dml_lab 
WHERE status IN ('open', 'locked') AND shop_id IN (11, 12, 13) 
ORDER BY amount DESC;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **13. Final Precision Scrub**
-- MAGIC * **Task:**
-- MAGIC   1. Delete all records where `status` is exactly 4 characters long (e.g., 'open').
-- MAGIC   2. Select all remaining rows from the table.
-- MAGIC   3. Sort them by `amount` descending.
-- MAGIC * **Expected Result:**
-- MAGIC | shop_id | amount | status |
-- MAGIC |---|---|---|
-- MAGIC | 3 | 999 | restored |
-- MAGIC | 10 | 300 | active |
-- MAGIC | 4 | 150 | active |
-- MAGIC | 13 | 0 | locked |

-- COMMAND ----------

DELETE FROM session_2_sql.txn_dml_lab WHERE status LIKE '____';

SELECT shop_id, amount, status FROM session_2_sql.txn_dml_lab ORDER BY amount DESC;