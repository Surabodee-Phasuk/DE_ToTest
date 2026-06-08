# Databricks notebook source
# MAGIC %md
# MAGIC # Python Data Engineering Fundamentals - Object-Oriented Programming (OOP) Exercise
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Easy**
# MAGIC
# MAGIC **1. Creating a Basic Dataclass**
# MAGIC * **Task:** 
# MAGIC   1. Import `@dataclass` from `dataclasses`.
# MAGIC   2. Create a class `Server` using the `@dataclass` decorator.
# MAGIC   3. Add attributes `hostname` (str) and `cores` (int).
# MAGIC

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC **2. Instantiating and Accessing Attributes**
# MAGIC * **Task:** 
# MAGIC   1. Based on the `Server` class from Task 1, instantiate an object named `my_server` with hostname `"dbx-cluster-1"` and `cores=8`.
# MAGIC   2. Print the `hostname` attribute using dot notation.
# MAGIC

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ### **Medium**
# MAGIC
# MAGIC **3. Adding a Method to a Dataclass**
# MAGIC * **Task:** 
# MAGIC   1. Define a `@dataclass` named `DataPipeline`.
# MAGIC   2. Include attributes `name` (str) and `status` (str).
# MAGIC   3. Add a method `start_pipeline(self)` that prints `"Starting pipeline {self.name}"` and changes `self.status` to `"Running"`.
# MAGIC

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC **4. Adding Methods with Default Parameters**
# MAGIC * **Task:** 
# MAGIC   1. Modify the `DataPipeline` class to include a method `scale_cluster(self, nodes: int = 2) -> None`.
# MAGIC   2. Print `"Scaling {self.name} to {nodes} nodes"`.
# MAGIC   3. Instantiate the class and call `scale_cluster()` with no arguments, then call it again passing `4`.
# MAGIC

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC **5. Utilizing `__post_init__` for Data Formatting**
# MAGIC * **Task:** 
# MAGIC   1. Define a `@dataclass` named `Customer`.
# MAGIC   2. Include attributes `first_name` (str) and `last_name` (str).
# MAGIC   3. Add a `__post_init__(self)` method that automatically converts both `first_name` and `last_name` to title case (e.g., using `.title()`).
# MAGIC

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ### **Hard**
# MAGIC
# MAGIC **6. Derived Attributes using `__post_init__`**
# MAGIC * **Task:** 
# MAGIC   1. Define a `@dataclass` named `SensorData`.
# MAGIC   2. Include the attribute `temperature` (int).
# MAGIC   3. Inside `__post_init__(self)`, declare a new attribute `self.alert_level`. 
# MAGIC   4. If `temperature > 80`, set `alert_level = "High"`, otherwise set it to `"Normal"`.
# MAGIC   5. Instantiate the class with `temperature = 95` and print the `alert_level`.
# MAGIC
# MAGIC

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC **7. Stateful Interaction with Multiple Methods**
# MAGIC * **Task:** 
# MAGIC   1. Define a `@dataclass` named `DeltaTableSimulator`.
# MAGIC   2. Attributes: `table_name` (str) and `record_count` (int).
# MAGIC   3. Method 1: `insert_data(self, records: int) -> None` which adds to `record_count`.
# MAGIC   4. Method 2: `delete_data(self, records: int) -> None` which subtracts from `record_count`. 
# MAGIC   5. In `delete_data`, raise a `ValueError` if `records` to delete is greater than `record_count`.
# MAGIC

# COMMAND ----------

