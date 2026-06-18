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

