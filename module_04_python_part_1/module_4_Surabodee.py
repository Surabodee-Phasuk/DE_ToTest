# Databricks notebook source
raw_orders = ["  ORD100:Electronics:250.50  ", "  ORD101:Apparel:45.00  ", "  ORD102:Electronics:invalid  ", "  ORD103:Home:-10.0  "]
config = {"min_threshold": 0.0, "currency": "USD"}

# COMMAND ----------

# MAGIC %md
# MAGIC ### Sub-task 2: String Sanitization
# MAGIC Create an empty list called `cleaned_orders`. Loop through `raw_orders`, strip whitespaces, and convert them to uppercase.
# MAGIC
# MAGIC * **Expected Result:** `['ORD100:ELECTRONICS:250.50', 'ORD101:APPAREL:45.00', 'ORD102:ELECTRONICS:INVALID', 'ORD103:HOME:-10.0']`

# COMMAND ----------

cleaned_orders = []
for order in raw_orders:
  cleaned_orders.append(order.strip().upper())
print(cleaned_orders)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Sub-task 3: Parsing and Type Conversion
# MAGIC Iterate through `cleaned_orders`. Split each string by `:`. 
# MAGIC Try to convert the price (the third element) to a float. If it fails (e.g., "INVALID"), skip that record using `continue`.
# MAGIC
# MAGIC * **Expected Result:** (Filtered list of components in memory)

# COMMAND ----------

parsed_records = []
for order in cleaned_orders:
  parts = order.split(":")
  try:
    parts[2] = float(parts[2])
    parsed_records.append(parts)
  except ValueError:
    print(f"Error parsing order: {parts[0]}")
    continue

# COMMAND ----------

# MAGIC %md
# MAGIC ### Sub-task 4: Business Logic Validation
# MAGIC From the `parsed_records`, remove any order where the price is less than or equal to `config["min_threshold"]`.
# MAGIC
# MAGIC * **Expected Result:** `[['ORD100', 'ELECTRONICS', 250.5], ['ORD101', 'APPAREL', 45.0]]`

# COMMAND ----------

valid_records = []
for record in parsed_records:
  if record[2] > config["min_threshold"]:
    valid_records.append(record)
print(valid_records)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Sub-task 5: Dictionary Transformation
# MAGIC Convert the `valid_records` list into a list of dictionaries with keys: `id`, `category`, and `price`.
# MAGIC
# MAGIC * **Expected Result:** `[{'id': 'ORD100', 'category': 'ELECTRONICS', 'price': 250.5}, {'id': 'ORD101', 'category': 'APPAREL', 'price': 45.0}]`

# COMMAND ----------

order_dicts = []
for record in valid_records:
    order_dicts.append({"id": record[0], "category": record[1], "price": record[2]})
print(order_dicts)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Sub-task 6: Category Aggregation (Sets)
# MAGIC Extract all unique categories from `order_dicts` using a set.
# MAGIC
# MAGIC * **Expected Result:** `{'ELECTRONICS', 'APPAREL'}`

# COMMAND ----------

unique_categories = set()
for order in order_dicts:
  unique_categories.add(order["category"])
print(unique_categories)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Sub-task 7: Discount Calculation
# MAGIC For every order in the "ELECTRONICS" category, apply a 10% discount to the price. Round to 2 decimals.
# MAGIC
# MAGIC * **Expected Result:** Price for ORD100 becomes `225.45`

# COMMAND ----------

for order in order_dicts:
  if order["category"] == "ELECTRONICS":
    new_price = order["price"] * 0.0 + (order["price"] * 0.9) 
    order["price"] = round(new_price,2)
print(order_dicts)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Sub-task 8: Summary Statistics
# MAGIC Calculate the total revenue of all orders in `order_dicts`.
# MAGIC
# MAGIC * **Expected Result:** `270.45` (225.45 + 45.0)

# COMMAND ----------

# DBTITLE 1,Cell 15
total_revenue = sum(o["price"]
for o in order_dicts)
print(total_revenue)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Sub-task 9: Final Reporting
# MAGIC Using a loop and `enumerate`, print a final report for each order in the format: 
# MAGIC `Item 1: [ID] - [PRICE] USD`
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC `Item 1: ORD100 - 225.45 USD`
# MAGIC `Item 2: ORD101 - 45.0 USD`

# COMMAND ----------

for index, order in enumerate(order_dicts, 1):
  print(f"Item: {index}: {order['id']} - {order['price']} {config['currency']}", end=" ")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Sub-task 10: System Log & Cleanup
# MAGIC Add a `status` key to the `config` dictionary with the value `"Complete"`. Clear the `raw_orders` list to save memory.
# MAGIC
# MAGIC * **Expected Result:**
# MAGIC `config: {'min_threshold': 0.0, 'currency': 'USD', 'status': 'Complete'}`
# MAGIC `raw_orders: []`

# COMMAND ----------

config["status"] = "Complete"
raw_orders.clear()
print(f"config: {config}", end=" ")
print(f"raw_orders: {raw_orders}")

# COMMAND ----------

