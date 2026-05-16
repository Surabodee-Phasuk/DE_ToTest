-- Databricks notebook source
-- MAGIC %md
-- MAGIC ### **Easy**

-- COMMAND ----------

CREATE OR REPLACE TABLE session_3_sql.server_metrics (node_id INT, log_dt DATE, cpu_load INT);

INSERT INTO session_3_sql.server_metrics
  VALUES
    (1, '2026-04-01', 45),
    (1, '2026-04-02', 80),
    (2, '2026-04-01', 20),
    (2, '2026-04-02', 90),
    (2, '2026-04-03', 90);

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Basic Partitioned Summation**
-- MAGIC * **Task:**
-- MAGIC   1. Select `node_id`, `cpu_load`, and `SUM(cpu_load) OVER (PARTITION BY node_id)` as `total_node_load`.
-- MAGIC   2. Filter for `node_id = 1`.
-- MAGIC * **Expected Result:**
-- MAGIC | node_id | cpu_load | total_node_load |
-- MAGIC |---|---|---|
-- MAGIC | 1 | 45 | 125 |
-- MAGIC | 1 | 80 | 125 |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Sequential Row Numbering**
-- MAGIC * **Task:**
-- MAGIC   1. Assign a sequential ID using `ROW_NUMBER() OVER (PARTITION BY node_id ORDER BY log_dt ASC)`.
-- MAGIC   2. Filter for `cpu_load > 40`.
-- MAGIC * **Expected Result:**
-- MAGIC | node_id | log_dt | rn |
-- MAGIC |---|---|---|
-- MAGIC | 1 | 2026-04-01 | 1 |
-- MAGIC | 1 | 2026-04-02 | 2 |
-- MAGIC | 2 | 2026-04-02 | 1 |
-- MAGIC | 2 | 2026-04-03 | 2 |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### **Normal**

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Handling Ties with DENSE_RANK**
-- MAGIC * **Task:**
-- MAGIC   1. Select `node_id`, `cpu_load`, and `DENSE_RANK() OVER (PARTITION BY node_id ORDER BY cpu_load DESC)`.
-- MAGIC   2. Filter where `node_id = 2`. Notice it does not skip rank 2.
-- MAGIC * **Expected Result:**
-- MAGIC | node_id | cpu_load | dense_rnk |
-- MAGIC |---|---|---|
-- MAGIC | 2 | 90 | 1 |
-- MAGIC | 2 | 90 | 1 |
-- MAGIC | 2 | 20 | 2 |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Peeking at Previous Rows (LAG)**
-- MAGIC * **Task:**
-- MAGIC   1. Use `LAG(cpu_load) OVER (PARTITION BY node_id ORDER BY log_dt ASC)` to find the prior day's load.
-- MAGIC   2. Filter where `log_dt BETWEEN '2026-04-01' AND '2026-04-02'`.
-- MAGIC * **Expected Result:**
-- MAGIC | node_id | log_dt | cpu_load | prior_load |
-- MAGIC |---|---|---|---|
-- MAGIC | 1 | 2026-04-01 | 45 | null |
-- MAGIC | 1 | 2026-04-02 | 80 | 45 |
-- MAGIC | 2 | 2026-04-01 | 20 | null |
-- MAGIC | 2 | 2026-04-02 | 90 | 20 |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Basic CTE Abstraction**
-- MAGIC * **Task:**
-- MAGIC   1. Abstract the base table inside a CTE named `base_metrics`.
-- MAGIC   2. Query from `base_metrics` where `cpu_load IN (45, 20)`.
-- MAGIC * **Expected Result:**
-- MAGIC | node_id | log_dt | cpu_load |
-- MAGIC |---|---|---|
-- MAGIC | 1 | 2026-04-01 | 45 |
-- MAGIC | 2 | 2026-04-01 | 20 |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Running Cumulative Arithmetic**
-- MAGIC * **Task:**
-- MAGIC   1. Calculate a running total: `SUM(cpu_load) OVER (PARTITION BY node_id ORDER BY log_dt ASC)`.
-- MAGIC   2. Filter for `node_id = 1`.
-- MAGIC * **Expected Result:**
-- MAGIC | node_id | log_dt | cpu_load | running_load |
-- MAGIC |---|---|---|---|
-- MAGIC | 1 | 2026-04-01 | 45 | 45 |
-- MAGIC | 1 | 2026-04-02 | 80 | 125 |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### **Hard**

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Direct Qualify Filtering**
-- MAGIC * **Task:**
-- MAGIC   1. Use `QUALIFY ROW_NUMBER() OVER (PARTITION BY node_id ORDER BY cpu_load DESC) = 1` to find the peak load event for each node.
-- MAGIC   2. Filter for `log_dt >= '2026-04-01'`.
-- MAGIC * **Expected Result:**
-- MAGIC | node_id | log_dt | cpu_load |
-- MAGIC |---|---|---|
-- MAGIC | 1 | 2026-04-02 | 80 |
-- MAGIC | 2 | 2026-04-02 | 90 |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Windowed Delta Calculations**
-- MAGIC * **Task:**
-- MAGIC   1. Calculate the daily spike: `cpu_load - LAG(cpu_load) OVER (PARTITION BY node_id ORDER BY log_dt ASC)`.
-- MAGIC   2. Filter where `node_id = 2`.
-- MAGIC * **Expected Result:**
-- MAGIC | node_id | log_dt | load_spike |
-- MAGIC |---|---|---|
-- MAGIC | 2 | 2026-04-01 | null |
-- MAGIC | 2 | 2026-04-02 | 70 |
-- MAGIC | 2 | 2026-04-03 | 0 |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Nested Subquery Windowing**
-- MAGIC * **Task:**
-- MAGIC   1. Write a subquery generating a `RANK() OVER (ORDER BY cpu_load ASC)` alias as `global_rank`.
-- MAGIC   2. In the outer query, filter for `global_rank <= 2`.
-- MAGIC * **Expected Result:**
-- MAGIC | node_id | log_dt | cpu_load | global_rank |
-- MAGIC |---|---|---|---|
-- MAGIC | 2 | 2026-04-01 | 20 | 1 |
-- MAGIC | 1 | 2026-04-01 | 45 | 2 |

-- COMMAND ----------

