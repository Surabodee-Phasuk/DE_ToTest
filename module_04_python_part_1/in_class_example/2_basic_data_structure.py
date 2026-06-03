# Databricks notebook source
# MAGIC %md
# MAGIC # list

# COMMAND ----------

lst = [1, -2, 3, 4, -5]

print("lst[0] ->", lst[0])
print("lst[-1] ->", lst[-1])
print("lst[1:4] ->", lst[1:4])

print("len(lst) ->", len(lst))
print("sum(lst) ->", sum(lst))
print("min(lst) ->", min(lst))
print("max(lst) ->", max(lst))

# COMMAND ----------

data_buffer = ["sensor_1", "sensor_2"]
data_buffer.append("sensor_3")
print("data_buffer after append ->", data_buffer)

new_batch = ["sensor_4", "sensor_5"]
data_buffer.extend(new_batch)
print("data_buffer after extend ->", data_buffer)

data_buffer.insert(0, "timestamp_header")
print("data_buffer after insert ->", data_buffer)

last_item = data_buffer.pop()
print("last_item after pop ->", last_item)

data_buffer.remove("sensor_2")
print("data_buffer after remove ->", data_buffer)

data_buffer.clear()
print("data_buffer after clear ->", data_buffer)

# COMMAND ----------

sample_logs = ["ERROR", "INFO", "WARN", "ERROR", "INFO"]

error_count = sample_logs.count("ERROR")
print("error_count after count ->", error_count)

warn_position = sample_logs.index("WARN")
print("warn_position after index ->", warn_position)

total_records = len(sample_logs)
print("total_records after len ->", total_records)

# COMMAND ----------

user_ids = [502, 101, 305, 202]

user_ids.sort()
print("user_ids after sort ->", user_ids)

user_ids.sort(reverse=True)
print("user_ids after sort(reverse=True) ->", user_ids)

user_ids.reverse()
print("user_ids after reverse ->", user_ids)

# COMMAND ----------

# MAGIC %md
# MAGIC # set

# COMMAND ----------

raw_data = [1, 2, 2, 3, 4, 4, 4, 5]
unique_ids = set(raw_data)
empty_set = set()

print("unique_ids ->", unique_ids)
print("empty_set ->", empty_set)

total_unique = len(unique_ids)
print("len(unique_ids) ->", total_unique)

search_id = 3
print("search_id in unique_ids ->", search_id in unique_ids)

diff_ids = unique_ids - {2, 4}
print("unique_ids - {2, 4} ->", diff_ids)

# COMMAND ----------

st = {1, 2, 3}

st.add(4)
print("st after add(4) ->", st)

st.update([5, 6, 7])
print("st after update([5, 6, 7]) ->", st)

st.remove(1)
print("st after remove(1) ->", st)

st.discard(99)
print("st after discard(99) ->", st)

item = st.pop()
print("item after pop() ->", item)
print("st after pop() ->", st)

st.clear()
print("st after clear() ->", st)

# COMMAND ----------

yesterday_ids = {10, 20, 30, 40}
today_ids = {30, 40, 50, 60}

all_ids = yesterday_ids.union(today_ids)
print("all_ids after union ->", all_ids)

returning_ids = yesterday_ids.intersection(today_ids)
print("returning_ids after intersection ->", returning_ids)

churned_ids = yesterday_ids.difference(today_ids)
print("churned_ids after difference ->", churned_ids)

changed_ids = yesterday_ids.symmetric_difference(today_ids)
print("changed_ids after symmetric_difference ->", changed_ids)

# COMMAND ----------

# MAGIC %md
# MAGIC # dict

# COMMAND ----------

# 1. Creation
user_row = {"id": 1, "name": "Alice", "role": "Admin"}
empty_dict = dict() # or {}

print("user_row ->", user_row)
print("empty_dict ->", empty_dict)

# 2. Accessing (The 'Right' Way)
# Standard access: Raises KeyError if 'status' is missing
print("user_row['role'] ->", user_row["role"])

# Safe access: Returns None (or a default) if key is missing
print("user_row.get('status', 'Unknown') ->", user_row.get("status", "Unknown"))

# 3. Keys, Values, and Items
print("user_row.keys() ->", user_row.keys())
print("user_row.values() ->", user_row.values())
print("user_row.items() ->", user_row.items())

# COMMAND ----------

record = {"id": 101, "status": "pending"}

# 1. Update/Add a single key
record["status"] = "processed"
record["timestamp"] = "2023-10-01"
print("record after status/timestamp update ->", record)

# 2. Update with another dictionary (.update)
updates = {"status": "shipped", "tracking": "ABC-123"}
record.update(updates)
print("record after update(updates) ->", record)

# 3. The Merge Operator (Python 3.9+) - Very clean for pipelines
yesterday_cfg = {"retries": 3, "timeout": 30}
today_cfg = {"timeout": 60, "alert": True}

merged_cfg = yesterday_cfg | today_cfg
print("merged_cfg after | ->", merged_cfg)

# COMMAND ----------

meta = {"id": 5, "temp_flag": True, "token": "secret_abc"}

token = meta.pop("token")
print("token after pop('token') ->", token)
print("meta after pop('token') ->", meta)

last_item = meta.popitem()
print("last_item after popitem() ->", last_item)
print("meta after popitem() ->", meta)

meta["id"] = 5
del meta["id"]
print("meta after del meta['id'] ->", meta)

meta.clear()
print("meta after clear() ->", meta)