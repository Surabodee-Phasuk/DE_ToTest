# Databricks notebook source
# MAGIC %md
# MAGIC # If Else statement

# COMMAND ----------

record_count = 1500
threshold = 1000

if record_count > threshold:
    print("Batch size exceeded. Splitting data...")
elif record_count == 0:
    print("Warning: Received empty file.")
else:
    print("Batch size within limits. Proceeding.")

status = "High Volume" if record_count > 1000 else "Normal Volume"

# COMMAND ----------

# MAGIC %md
# MAGIC # For Loop statement

# COMMAND ----------

# 1. Iterating over a list (The most common way)
file_names = ["users_oct.csv", "orders_oct.csv", "logs_oct.csv"]

for file in file_names:
    print(f"Ingesting {file} into Bronze layer...")

# 2. Using range() for indexed loops
for i in range(1, 4):
    print(f"Retry attempt {i}...")


# COMMAND ----------

# MAGIC %md
# MAGIC # For Loop with break continue statement

# COMMAND ----------

raw_records = [
    {"id": 1, "data": "Valid"},
    {"id": 2, "data": None},  # Bad record
    {"id": 3, "data": "Valid"},
    {"id": 99, "data": "Kill Signal"} # Stop processing
]

for record in raw_records:
    if record["id"] == 99:
        print("Termination record found. Stopping.")
        break  # Exit loop
        
    if record["data"] is None:
        print(f"Skipping record {record['id']} due to null data.")
        continue # Skip to next record
        
    print(f"Processing record {record['id']}...")

# COMMAND ----------

# MAGIC %md
# MAGIC # Loop With Enumurate

# COMMAND ----------

rows = ["header", "row1", "row2", "row3"]

for index, row in enumerate(rows):
    if index == 0:
        print(f"Skipping Header: {row}")
        continue
    print(f"Processing Row {index}: {row}")