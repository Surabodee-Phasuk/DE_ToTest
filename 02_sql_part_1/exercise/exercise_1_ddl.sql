-- Databricks notebook source
-- MAGIC %md
-- MAGIC ### **Easy**

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **1. Schema Setup**
-- MAGIC * **Task:**
-- MAGIC   1. Create the schema `workspace.session_2_sql` if it doesn't already exist.
-- MAGIC * **Expected Result:**
-- MAGIC | status |
-- MAGIC |---|
-- MAGIC | OK |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **2. Create Dedicated DDL Table**
-- MAGIC * **Task:**
-- MAGIC   1. Create a table named `session_2_sql.txn_ddl_lab`.
-- MAGIC   2. Add columns: `id` (int), `val` (int), and `description` (string).
-- MAGIC * **Expected Result:**
-- MAGIC | status |
-- MAGIC |---|
-- MAGIC | OK |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **3. Simple Column Addition**
-- MAGIC * **Task:**
-- MAGIC   1. Use `ALTER TABLE` to add a column named `is_processed` (boolean) to `txn_ddl_lab`.
-- MAGIC * **Expected Result:**
-- MAGIC | status |
-- MAGIC |---|
-- MAGIC | OK |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### **Normal**

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **4. Table Property Update**
-- MAGIC * **Task:**
-- MAGIC   1. Use `CREATE OR REPLACE TABLE` on `txn_ddl_lab`.
-- MAGIC   2. Include `TBLPROPERTIES` to enable `delta.enableTypeWidening` as `'true'`.
-- MAGIC   3. Include `TBLPROPERTIES` to enable `delta.columnMapping.mode` set to `'name'`.

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **5. Column Renaming**
-- MAGIC * **Task:**
-- MAGIC   1. Rename the column `val` to `sale_value` in the `txn_ddl_lab` table.

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **6. Datatype Conversion**
-- MAGIC * **Task:**
-- MAGIC   1. Alter the column `sale_value` in `txn_ddl_lab` to be of type `bigint`.

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **7. Column Dropping**
-- MAGIC * **Task:**
-- MAGIC   1. Remove the `id` column from `txn_ddl_lab` using the `DROP COLUMN` statement.

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **8. Conditional Table Creation**
-- MAGIC * **Task:**
-- MAGIC   1. Use the `CREATE TABLE IF NOT EXISTS` syntax to create a table named `session_2_sql.txn_ddl_check`.

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### **Hard**

-- COMMAND ----------

-- MAGIC %md
-- MAGIC **9. Multi-Column Alteration**
-- MAGIC * **Task:**
-- MAGIC   1. Use a single `ALTER TABLE` command to add columns `tag` (string) and `created_at` (timestamp).

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **10. Truncate Table Logic**
-- MAGIC * **Task:**
-- MAGIC   1. Use the `TRUNCATE TABLE` command on `session_2_sql.txn_ddl_lab` to clear data without removing the table structure.

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **11. Dropping Objects**
-- MAGIC * **Task:**
-- MAGIC   1. Completely remove the table `session_2_sql.txn_ddl_check` from the database.

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC **12. Final Schema Cleanup**
-- MAGIC * **Task:**
-- MAGIC   1. Write a command to drop the table `session_2_sql.txn_map_lab` only if it exists.

-- COMMAND ----------

