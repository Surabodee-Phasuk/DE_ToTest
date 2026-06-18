-- Databricks notebook source
-- MAGIC %md
-- MAGIC ### **Easy**

-- COMMAND ----------

CREATE OR REPLACE TABLE session_3_sql.hr_payroll (yr INT, dept STRING, budget INT);

INSERT INTO session_3_sql.hr_payroll
  VALUES
    (2025, 'Engineering', 100),
    (2025, 'Sales', 200),
    (2026, 'Engineering', 150),
    (2026, 'Sales', 300);

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Baseline Group By check**
-- MAGIC * **Task:**
-- MAGIC   1. Ensure the data aggregates properly: Select `yr` and `SUM(budget)`. Group by `yr`.
-- MAGIC   2. Filter for `yr = 2025`.
-- MAGIC * **Expected Result:**
-- MAGIC | yr | sum(budget) |
-- MAGIC |---|---|
-- MAGIC | 2025 | 300 |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Standard 2-Column PIVOT**
-- MAGIC * **Task:**
-- MAGIC   1. PIVOT `SUM(budget)` FOR `dept` IN ('Engineering', 'Sales').
-- MAGIC   2. Filter the outer query for `yr = 2026`.
-- MAGIC * **Expected Result:**
-- MAGIC | yr | Engineering | Sales |
-- MAGIC |---|---|---|
-- MAGIC | 2026 | 150 | 300 |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### **Normal**

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Pivoting Maximum Thresholds**
-- MAGIC * **Task:**
-- MAGIC   1. PIVOT using `MAX(budget)` instead of SUM, FOR `dept` IN ('Engineering', 'Sales').
-- MAGIC   2. Filter for records where the `Sales` column is greater than 250.
-- MAGIC * **Expected Result:**
-- MAGIC | yr | Engineering | Sales |
-- MAGIC |---|---|---|
-- MAGIC | 2026 | 150 | 300 |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Inverting Dimensions (Years as Columns)**
-- MAGIC * **Task:**
-- MAGIC   1. PIVOT the `SUM(budget)` FOR `yr` IN (2025, 2026).
-- MAGIC   2. Filter where `dept` is 'Engineering'.
-- MAGIC * **Expected Result:**
-- MAGIC | dept | 2025 | 2026 |
-- MAGIC |---|---|---|
-- MAGIC | Engineering | 100 | 150 |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Pre-Filtering via Subqueries before PIVOT**
-- MAGIC * **Task:**
-- MAGIC   1. In a subquery, filter `WHERE yr = 2025`.
-- MAGIC   2. PIVOT that subquery `SUM(budget)` FOR `dept` IN ('Sales').
-- MAGIC * **Expected Result:**
-- MAGIC | yr | Sales |
-- MAGIC |---|---|
-- MAGIC | 2025 | 200 |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Post-Pivot Arithmetic**
-- MAGIC * **Task:**
-- MAGIC   1. Wrap the standard pivot in a CTE.
-- MAGIC   2. Query the CTE to select `yr` and calculate the variance `(Sales - Engineering)` as `diff`.
-- MAGIC   3. Filter where `yr = 2026`.
-- MAGIC * **Expected Result:**
-- MAGIC | yr | diff |
-- MAGIC |---|---|
-- MAGIC | 2026 | 150 |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### **Hard**

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Conditional PIVOT Segregation**
-- MAGIC * **Task:**
-- MAGIC   1. In a CTE, create a conditional string: `CASE WHEN yr=2025 THEN 'Archived' ELSE 'Current' END` as `era`.
-- MAGIC   2. PIVOT `SUM(budget)` FOR `era` IN ('Archived', 'Current').
-- MAGIC   3. Filter where `dept = 'Sales'`.
-- MAGIC * **Expected Result:**
-- MAGIC | dept | Archived | Current |
-- MAGIC |---|---|---|
-- MAGIC | Sales | 200 | 300 |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **Custom Column Aliasing inside Pivot**
-- MAGIC * **Task:**
-- MAGIC   1. Use the syntax `IN ('Engineering' AS Eng_Budget, 'Sales' AS Sales_Budget)` to override default column headers.
-- MAGIC   2. Filter for `yr = 2025`.
-- MAGIC * **Expected Result:**
-- MAGIC | yr | Eng_Budget | Sales_Budget |
-- MAGIC |---|---|---|
-- MAGIC | 2025 | 100 | 200 |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **String Maximization Pivot Matrix**
-- MAGIC * **Task:**
-- MAGIC   1. PIVOT `MAX(dept)` FOR `yr` IN (2025, 2026). This produces strings inside the matrix.
-- MAGIC   2. Filter where `budget = 100`.
-- MAGIC * **Expected Result:**
-- MAGIC | budget | 2025 | 2026 |
-- MAGIC |---|---|---|
-- MAGIC | 100 | Engineering | null |

-- COMMAND ----------

