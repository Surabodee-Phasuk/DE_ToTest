-- Databricks notebook source
-- MAGIC %md
-- MAGIC ### **Easy**

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Relational Environment Setup (DDL/DML)**

-- COMMAND ----------


CREATE OR REPLACE TABLE  session_3_sql.app_log_mobile (log_id INT, user_id INT, duration INT);
CREATE OR REPLACE TABLE  session_3_sql.app_log_web (log_id INT, user_id INT, duration INT);
CREATE OR REPLACE TABLE  session_3_sql.dim_users (user_id INT, status STRING);

INSERT INTO session_3_sql.app_log_mobile VALUES (1, 10, 500), (1, 10, 500), (2, 11, 200);
INSERT INTO session_3_sql.app_log_web VALUES (3, 12, 300), (1, 10, 100);
INSERT INTO session_3_sql.dim_users VALUES (10, 'Active'), (12, 'Inactive');

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Consolidating Event Streams (UNION)**
-- MAGIC * **Task:**
-- MAGIC   1. Use `UNION` to combine mobile and web logs, automatically removing duplicate events.
-- MAGIC   2. Filter the output for durations greater than 150.
-- MAGIC * **Expected Result:**
-- MAGIC | log_id | user_id | duration |
-- MAGIC |---|---|---|
-- MAGIC | 1 | 10 | 500 |
-- MAGIC | 2 | 11 | 200 |
-- MAGIC | 3 | 12 | 300 |

-- COMMAND ----------


SELECT * FROM session_3_sql.app_log_mobile WHERE duration > 150
UNION
SELECT * FROM session_3_sql.app_log_web WHERE duration > 150;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Master Identity Enrichment (Inner Join)**
-- MAGIC * **Task:**
-- MAGIC   1. Perform an `INNER JOIN` between `app_log_mobile` (a) and `dim_users` (b) on `user_id`.
-- MAGIC   2. Filter for logs where the status is 'Active'.
-- MAGIC * **Expected Result:**
-- MAGIC | log_id | status | duration |
-- MAGIC |---|---|---|
-- MAGIC | 1 | Active | 500 |
-- MAGIC | 1 | Active | 500 |

-- COMMAND ----------


SELECT a.log_id, b.status, a.duration 
FROM session_3_sql.app_log_mobile a
INNER JOIN session_3_sql.dim_users b ON a.user_id = b.user_id
WHERE b.status = 'Active';

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### **Normal**

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Raw Event Audit Tracking (Union All)**
-- MAGIC * **Task:**
-- MAGIC   1. Use `UNION ALL` to stack all mobile and web records directly, preserving any system duplicates.
-- MAGIC   2. Filter specifically for `user_id = 10`.
-- MAGIC * **Expected Result:**
-- MAGIC | log_id | user_id | duration |
-- MAGIC |---|---|---|
-- MAGIC | 1 | 10 | 500 |
-- MAGIC | 1 | 10 | 500 |
-- MAGIC | 1 | 10 | 100 |

-- COMMAND ----------


SELECT * FROM session_3_sql.app_log_mobile WHERE user_id = 10
UNION ALL
SELECT * FROM session_3_sql.app_log_web WHERE user_id = 10;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Detecting Unregistered Users (Left Anti Join)**
-- MAGIC * **Task:**
-- MAGIC   1. Use a `LEFT ANTI JOIN` from mobile logs to the user dimension to find events mapped to unknown IDs.
-- MAGIC   2. Filter where duration is exactly 200.
-- MAGIC * **Expected Result:**
-- MAGIC | log_id | user_id | duration |
-- MAGIC |---|---|---|
-- MAGIC | 2 | 11 | 200 |

-- COMMAND ----------


SELECT a.* FROM session_3_sql.app_log_mobile a
LEFT ANTI JOIN session_3_sql.dim_users b ON a.user_id = b.user_id
WHERE a.duration = 200;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Verifying Active Engagements (Left Semi Join)**
-- MAGIC * **Task:**
-- MAGIC   1. Use a `LEFT SEMI JOIN` from `dim_users` to `app_log_web` to find only users who have logged in via the web.
-- MAGIC   2. Filter for users with 'Inactive' status to find anomalies.
-- MAGIC * **Expected Result:**
-- MAGIC | user_id | status |
-- MAGIC |---|---|
-- MAGIC | 12 | Inactive |

-- COMMAND ----------


SELECT a.* FROM session_3_sql.dim_users a
LEFT SEMI JOIN session_3_sql.app_log_web b ON a.user_id = b.user_id
WHERE a.status = 'Inactive';

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Full System Discrepancy Map (Full Join)**
-- MAGIC * **Task:**
-- MAGIC   1. Apply a `FULL JOIN` between mobile logs and the user dimension on `user_id`.
-- MAGIC   2. Filter where either the log is missing (`a.user_id IS NULL`) OR the dimension is missing (`b.user_id IS NULL`).
-- MAGIC * **Expected Result:**
-- MAGIC | log_id | mobile_uid | duration | dim_uid | status |
-- MAGIC |---|---|---|---|---|
-- MAGIC | 2 | 11 | 200 | null | null |
-- MAGIC | null | null | null | 12 | Inactive |

-- COMMAND ----------


SELECT a.log_id, a.user_id AS mobile_uid, a.duration, b.user_id AS dim_uid, b.status 
FROM session_3_sql.app_log_mobile a
FULL JOIN session_3_sql.dim_users b ON a.user_id = b.user_id
WHERE a.user_id IS NULL OR b.user_id IS NULL;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### **Hard**

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Simulated Inequality Pairing (Cross Join)**
-- MAGIC * **Task:**
-- MAGIC   1. `CROSS JOIN` the user dimension against itself (alias as `u1` and `u2`).
-- MAGIC   2. Apply a strict inequality filter where `u1.user_id < u2.user_id` to prevent reverse duplicates.
-- MAGIC * **Expected Result:**
-- MAGIC | u1_id | u1_status | u2_id | u2_status |
-- MAGIC |---|---|---|---|
-- MAGIC | 10 | Active | 12 | Inactive |

-- COMMAND ----------


SELECT u1.user_id AS u1_id, u1.status AS u1_status, u2.user_id AS u2_id, u2.status AS u2_status 
FROM session_3_sql.dim_users u1
CROSS JOIN session_3_sql.dim_users u2
WHERE u1.user_id < u2.user_id;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Multi-Hop Exclusion Pipeline**
-- MAGIC * **Task:**
-- MAGIC   1. Create a `UNION` CTE of mobile and web logs.
-- MAGIC   2. Perform a `LEFT JOIN` from the `dim_users` table to this CTE.
-- MAGIC   3. Filter out mapped records (`WHERE cte.user_id IS NULL`) to find users with absolutely zero engagements across both platforms.
-- MAGIC * **Expected Result:**
-- MAGIC | user_id | status |
-- MAGIC |---|---|
-- MAGIC | (No rows in this dummy dataset, but tests the logic) |

-- COMMAND ----------


WITH global_logs AS (
  SELECT user_id FROM session_3_sql.app_log_mobile
  UNION
  SELECT user_id FROM session_3_sql.app_log_web
)
SELECT u.user_id, u.status 
FROM session_3_sql.dim_users u
LEFT JOIN global_logs gl ON u.user_id = gl.user_id
WHERE gl.user_id IS NULL;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Self-Join Event Duplication Detection**
-- MAGIC * **Task:**
-- MAGIC   1. `INNER JOIN` the `app_log_mobile` table to itself (alias `a` and `b`).
-- MAGIC   2. Join on `user_id` AND `duration`.
-- MAGIC   3. Filter using `a.log_id = b.log_id` AND `duration BETWEEN 400 AND 600`.
-- MAGIC * **Expected Result:**
-- MAGIC | a_log | b_log | duration |
-- MAGIC |---|---|---|
-- MAGIC | 1 | 1 | 500 |
-- MAGIC | 1 | 1 | 500 |
-- MAGIC | 1 | 1 | 500 |
-- MAGIC | 1 | 1 | 500 |

-- COMMAND ----------


SELECT a.log_id AS a_log, b.log_id AS b_log, a.duration 
FROM session_3_sql.app_log_mobile a
INNER JOIN session_3_sql.app_log_mobile b ON a.user_id = b.user_id AND a.duration = b.duration
WHERE a.log_id = b.log_id AND a.duration BETWEEN 400 AND 600;