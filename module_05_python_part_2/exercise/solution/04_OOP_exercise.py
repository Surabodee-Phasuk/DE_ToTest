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

from dataclasses import dataclass

@dataclass
class Server:
    hostname: str
    cores: int

# COMMAND ----------

# MAGIC %md
# MAGIC **2. Instantiating and Accessing Attributes**
# MAGIC * **Task:** 
# MAGIC   1. Based on the `Server` class from Task 1, instantiate an object named `my_server` with hostname `"dbx-cluster-1"` and `cores=8`.
# MAGIC   2. Print the `hostname` attribute using dot notation.
# MAGIC

# COMMAND ----------

my_server = Server("dbx-cluster-1", 8)
print(my_server.hostname)

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

from dataclasses import dataclass

@dataclass
class DataPipeline:
    name: str
    status: str
    
    def start_pipeline(self):
        print(f"Starting pipeline {self.name}")
        self.status = "Running"

pipeline = DataPipeline("Sales_Ingestion", "Stopped")
pipeline.start_pipeline()
print(pipeline.status)

# COMMAND ----------

# MAGIC %md
# MAGIC **4. Adding Methods with Default Parameters**
# MAGIC * **Task:** 
# MAGIC   1. Modify the `DataPipeline` class to include a method `scale_cluster(self, nodes: int = 2) -> None`.
# MAGIC   2. Print `"Scaling {self.name} to {nodes} nodes"`.
# MAGIC   3. Instantiate the class and call `scale_cluster()` with no arguments, then call it again passing `4`.
# MAGIC

# COMMAND ----------

@dataclass
class DataPipeline:
    name: str
    status: str
    
    def scale_cluster(self, nodes: int = 2) -> None:
        print(f"Scaling {self.name} to {nodes} nodes")

pipeline = DataPipeline("Sales_Ingestion", "Running")
pipeline.scale_cluster()
pipeline.scale_cluster(4)

# COMMAND ----------

# MAGIC %md
# MAGIC **5. Utilizing `__post_init__` for Data Formatting**
# MAGIC * **Task:** 
# MAGIC   1. Define a `@dataclass` named `Customer`.
# MAGIC   2. Include attributes `first_name` (str) and `last_name` (str).
# MAGIC   3. Add a `__post_init__(self)` method that automatically converts both `first_name` and `last_name` to title case (e.g., using `.title()`).
# MAGIC

# COMMAND ----------

from dataclasses import dataclass

@dataclass
class Customer:
    first_name: str
    last_name: str

    def __post_init__(self):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()

cust = Customer("john", "doe")
print(cust.first_name, cust.last_name)

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

from dataclasses import dataclass

@dataclass
class SensorData:
    temperature: int

    def __post_init__(self):
        self.alert_level = "High" if self.temperature > 80 else "Normal"

sensor_reading = SensorData(95)
print(sensor_reading.alert_level)

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

from dataclasses import dataclass

@dataclass
class DeltaTableSimulator:
    table_name: str
    record_count: int

    def insert_data(self, records: int) -> None:
        self.record_count += records
        print(f"Inserted {records}. Total is now {self.record_count}")

    def delete_data(self, records: int) -> None:
        if records > self.record_count:
            raise ValueError("Cannot delete more records than currently exist.")
        self.record_count -= records
        print(f"Deleted {records}. Total is now {self.record_count}")

# Testing the logic
table = DeltaTableSimulator("bronze_sales", 100)
table.insert_data(50)
try:
    table.delete_data(200)
except ValueError as e:
    print(f"Error: {e}")