-- Databricks notebook source
-- MAGIC %md
-- MAGIC ### **Easy**

-- COMMAND ----------

CREATE OR REPLACE TABLE session_3_sql.campaign_jan (customer_email STRING, segment STRING);

CREATE OR REPLACE TABLE session_3_sql.campaign_feb (customer_email STRING, segment STRING);

INSERT INTO session_3_sql.campaign_jan
  VALUES
    ('a@mail.com', 'VIP'),
    ('b@mail.com', 'Standard'),
    ('b@mail.com', 'Standard'),
    ('c@mail.com', 'Standard');

INSERT INTO session_3_sql.campaign_feb
  VALUES 
  ('b@mail.com', 'Standard'),
  ('d@mail.com', 'New');

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Sustained Engagement (INTERSECT)**
-- MAGIC * **Task:**
-- MAGIC   1. Find the distinct emails present in BOTH January and February campaigns using `INTERSECT`.
-- MAGIC * **Expected Result:**
-- MAGIC | customer_email | segment |
-- MAGIC |---|---|
-- MAGIC | b@mail.com | Standard |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Campaign Churn (EXCEPT)**
-- MAGIC * **Task:**
-- MAGIC   1. Use `EXCEPT` to identify distinct customers from January who did not participate in February.
-- MAGIC * **Expected Result:**
-- MAGIC | customer_email | segment |
-- MAGIC |---|---|
-- MAGIC | a@mail.com | VIP |
-- MAGIC | c@mail.com | Standard |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### **Normal**

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **New Audience Acquisition (EXCEPT)**
-- MAGIC * **Task:**
-- MAGIC   1. Use `EXCEPT` to locate customers entirely unique to the February campaign.
-- MAGIC * **Expected Result:**
-- MAGIC | customer_email | segment |
-- MAGIC |---|---|
-- MAGIC | d@mail.com | New |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Frequency Aware Exclusion (EXCEPT ALL)**
-- MAGIC * **Task:**
-- MAGIC   1. Use `EXCEPT ALL` on January minus February.
-- MAGIC   2. Notice how this keeps one duplicate of 'b@mail.com' because February only negated one of them.
-- MAGIC * **Expected Result:**
-- MAGIC | customer_email | segment |
-- MAGIC |---|---|
-- MAGIC | a@mail.com | VIP |
-- MAGIC | b@mail.com | Standard |
-- MAGIC | c@mail.com | Standard |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Simple Marketing Conditionals**
-- MAGIC * **Task:**
-- MAGIC   1. Select `customer_email` from January.
-- MAGIC   2. Create a column `action_plan` using `CASE WHEN segment = 'VIP' THEN 'Send Gift' ELSE 'Send Email' END`.
-- MAGIC   3. Filter where email ends with 'mail.com'.
-- MAGIC * **Expected Result:**
-- MAGIC | customer_email | action_plan |
-- MAGIC |---|---|
-- MAGIC | a@mail.com | Send Gift |
-- MAGIC | b@mail.com | Send Email |
-- MAGIC | b@mail.com | Send Email |
-- MAGIC | c@mail.com | Send Email |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Multi-Branch Tiering Logic**
-- MAGIC * **Task:**
-- MAGIC   1. Query February. Use `CASE` to apply priority logic: If email starts with 'b' THEN 'High', if email starts with 'd' THEN 'Low', `ELSE` 'Unknown'.
-- MAGIC   2. Filter for records where `segment` is NOT NULL.
-- MAGIC * **Expected Result:**
-- MAGIC | customer_email | priority |
-- MAGIC |---|---|
-- MAGIC | b@mail.com | High |
-- MAGIC | d@mail.com | Low |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### **Hard**

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Filter Injection before Sets**
-- MAGIC * **Task:**
-- MAGIC   1. Select only the `customer_email` from January where `segment` is 'Standard'.
-- MAGIC   2. `EXCEPT` select `customer_email` from February.
-- MAGIC * **Expected Result:**
-- MAGIC | customer_email |
-- MAGIC |---|
-- MAGIC | c@mail.com |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Nested CASE Expressions**
-- MAGIC * **Task:**
-- MAGIC   1. Query January. Create a nested `CASE`: If `segment = 'Standard'` THEN evaluate (CASE WHEN `customer_email = 'c@mail.com'` THEN 'Convert' ELSE 'Hold' END) ELSE 'Reward' END.
-- MAGIC   2. Filter where `segment IN ('Standard', 'VIP')`.
-- MAGIC * **Expected Result:**
-- MAGIC | customer_email | strategy |
-- MAGIC |---|---|
-- MAGIC | a@mail.com | Reward |
-- MAGIC | b@mail.com | Hold |
-- MAGIC | b@mail.com | Hold |
-- MAGIC | c@mail.com | Convert |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Conditional Summation in Aggregates**
-- MAGIC * **Task:**
-- MAGIC   1. Group January by `customer_email`.
-- MAGIC   2. Calculate `SUM(CASE WHEN segment = 'VIP' THEN 1 ELSE 0 END)` to count VIP instances.
-- MAGIC   3. Filter where the email contains an 'a'.
-- MAGIC * **Expected Result:**
-- MAGIC |customer_email|vip_count|
-- MAGIC |---|---|
-- MAGIC |a@mail.com|1|
-- MAGIC |b@mail.com|0|
-- MAGIC |c@mail.com|0|

-- COMMAND ----------

