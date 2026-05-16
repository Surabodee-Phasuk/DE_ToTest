-- Databricks notebook source
-- MAGIC %md
-- MAGIC ### **Easy**

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Environment Setup (DDL/DML)**

-- COMMAND ----------

CREATE OR REPLACE TABLE  session_3_sql.raw_web_events (
  event_uid STRING,
  visit_date STRING,
  user_tier STRING,
  time_on_page STRING,
  device_os STRING
);

INSERT INTO session_3_sql.raw_web_events VALUES
  ('E1A', '2026-03-01', 'Premium', '120.5', ' iOS '),
  ('E2B', '20260305', 'STANDARD', 'invalid_time', 'Android'),
  ('E3C', '2026/03/10', 'premium', '45.0', ' Windows '),
  ('E4D', '03-12-2026', 'guest', '300.99', NULL),
  ('E5E', '2026-03-15', 'PREMIUM', '15.2', 'iOS');

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Whitespace Standardization**
-- MAGIC * **Task:**
-- MAGIC   1. Select `event_uid`.
-- MAGIC   2. Use the `trim()` function on `device_os` to remove hidden spaces.
-- MAGIC   3. Filter the query strictly for records where `user_tier` is 'Premium' (case-sensitive).
-- MAGIC * **Expected Result:**
-- MAGIC | event_uid | clean_os |
-- MAGIC |---|---|
-- MAGIC | E1A | iOS |

-- COMMAND ----------

SELECT event_uid, trim(device_os) AS clean_os 
FROM session_3_sql.raw_web_events 
WHERE user_tier = 'Premium';

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Basic String Concatenation**
-- MAGIC * **Task:**
-- MAGIC   1. Use the `concat()` function to merge the string 'LOG_' with the `event_uid`.
-- MAGIC   2. Filter for events where `time_on_page` is greater than '100' (evaluating as strings).
-- MAGIC * **Expected Result:**
-- MAGIC |sys_log_id|
-- MAGIC |---|
-- MAGIC |LOG_E1A|
-- MAGIC |LOG_E2B|
-- MAGIC |LOG_E3C|
-- MAGIC |LOG_E4D|
-- MAGIC |LOG_E5E|
-- MAGIC

-- COMMAND ----------

SELECT concat('LOG_', event_uid) AS sys_log_id 
FROM session_3_sql.raw_web_events 
WHERE time_on_page > '100';

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### **Normal**

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Safe Numeric Parsing**
-- MAGIC * **Task:**
-- MAGIC   1. Use `try_cast()` to convert `time_on_page` to `DECIMAL(10,2)` to prevent pipeline failures on bad data.
-- MAGIC   2. Filter where the `user_tier` contains the text 'STANDARD' (using `upper()` to normalize the filter check).
-- MAGIC * **Expected Result:**
-- MAGIC | event_uid | safe_time |
-- MAGIC |---|---|
-- MAGIC | E2B | null |

-- COMMAND ----------

SELECT event_uid, TRY_CAST(time_on_page AS DECIMAL(10,2)) AS safe_time 
FROM session_3_sql.raw_web_events 
WHERE upper(user_tier) = 'STANDARD';

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Missing Metadata Fallbacks**
-- MAGIC * **Task:**
-- MAGIC   1. Use `coalesce()` to return the cleaned `device_os`, and if it is NULL, return 'UNKNOWN_DEVICE'.
-- MAGIC   2. Filter for records where the `visit_date` pattern matches '%2026%'.
-- MAGIC * **Expected Result:**
-- MAGIC | event_uid | active_device |
-- MAGIC |---|---|
-- MAGIC | E1A | iOS |
-- MAGIC | E2B | Android |
-- MAGIC | E3C | Windows |
-- MAGIC | E4D | UNKNOWN_DEVICE |
-- MAGIC | E5E | iOS |

-- COMMAND ----------

SELECT event_uid, COALESCE(trim(device_os), 'UNKNOWN_DEVICE') AS active_device 
FROM session_3_sql.raw_web_events 
WHERE visit_date LIKE '%2026%';

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Mathematical Floor Rounding**
-- MAGIC * **Task:**
-- MAGIC   1. Use `floor()` on the `time_on_page` (cast to float) to determine full minutes spent.
-- MAGIC   2. Filter for records where the raw `time_on_page` is NOT equal to 'invalid_time'.
-- MAGIC * **Expected Result:**
-- MAGIC | event_uid | full_minutes |
-- MAGIC |---|---|
-- MAGIC | E1A | 120 |
-- MAGIC | E3C | 45 |
-- MAGIC | E4D | 300 |
-- MAGIC | E5E | 15 |

-- COMMAND ----------

SELECT event_uid, floor(CAST(time_on_page AS FLOAT)) AS full_minutes 
FROM session_3_sql.raw_web_events 
WHERE time_on_page <> 'invalid_time';

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Standard Date Format Extraction**
-- MAGIC * **Task:**
-- MAGIC   1. Parse `visit_date` using `to_date(..., 'yyyy-MM-dd')` and wrap it in the `month()` function.
-- MAGIC   2. Filter for accounts explicitly in the 'PREMIUM' or 'premium' tier using an `IN` clause.
-- MAGIC * **Expected Result:**
-- MAGIC | event_uid | visit_month |
-- MAGIC |---|---|
-- MAGIC | E3C | null |
-- MAGIC | E5E | 3 |

-- COMMAND ----------

SELECT event_uid, month(try_to_date(visit_date, 'yyyy-MM-dd')) AS visit_month 
FROM session_3_sql.raw_web_events 
WHERE user_tier IN ('PREMIUM', 'premium');

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### **Hard**

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Complex Data Unification & Date Math**
-- MAGIC * **Task:**
-- MAGIC   1. Use `coalesce()` with multiple `try_to_date()` functions to parse 'yyyy-MM-dd', 'yyyyMMdd', and 'yyyy/MM/dd' formats.
-- MAGIC   2. Wrap the result in `date_add()` to project a 14-day follow-up window.
-- MAGIC   3. Filter out rows where the `device_os` IS NULL.
-- MAGIC * **Expected Result:**
-- MAGIC | event_uid | follow_up_date |
-- MAGIC |---|---|
-- MAGIC | E1A | 2026-03-15 |
-- MAGIC | E2B | 2026-03-19 |
-- MAGIC | E3C | 2026-03-24 |
-- MAGIC | E5E | 2026-03-29 |

-- COMMAND ----------

SELECT event_uid, 
  date_add(
    coalesce(
      try_to_date(visit_date, 'yyyy-MM-dd'),
      try_to_date(visit_date, 'yyyyMMdd'),
      try_to_date(visit_date, 'yyyy/MM/dd')
    ), 14
  ) AS follow_up_date 
FROM session_3_sql.raw_web_events 
WHERE device_os IS NOT NULL;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Dynamic Ceilings & Substrings**
-- MAGIC * **Task:**
-- MAGIC   1. Use `greatest()` to compare the float-cast `time_on_page` against a baseline minimum of 60.0.
-- MAGIC   2. Use `substr()` to extract just the first two characters of the `event_uid`.
-- MAGIC   3. Filter where the raw `visit_date` string contains hyphens '-'.
-- MAGIC * **Expected Result:**
-- MAGIC | event_prefix | adjusted_time |
-- MAGIC |---|---|
-- MAGIC | E1 | 120.5 |
-- MAGIC | E4 | 300.99 |
-- MAGIC | E5 | 60.0 |

-- COMMAND ----------

SELECT substr(event_uid, 1, 2) AS event_prefix, 
       greatest(try_cast(time_on_page AS FLOAT), 60.0) AS adjusted_time 
FROM session_3_sql.raw_web_events 
WHERE visit_date LIKE '%-%';