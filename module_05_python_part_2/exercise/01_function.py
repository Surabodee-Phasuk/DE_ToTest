# Databricks notebook source
# MAGIC %md
# MAGIC ### **Easy**
# MAGIC
# MAGIC **1. Basic Function with Type Hinting**
# MAGIC * **Task:** 
# MAGIC   1. Define a function named `subtract_numbers`.
# MAGIC   2. Accept two parameters `a` and `b`, both type-hinted as `int`.
# MAGIC   3. Return the result of `a - b`, with the return type hinted as `int`.
# MAGIC

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC **2. Function with Default Parameters**
# MAGIC * **Task:** 
# MAGIC   1. Define a function named `greet_user`.
# MAGIC   2. Accept `name` (str) and `greeting` (str).
# MAGIC   3. Set the default value of `greeting` to `"Hello"`.
# MAGIC   4. Return the formatted string: `"{greeting} {name}"`.
# MAGIC

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ### **Medium**
# MAGIC
# MAGIC **3. Dynamic Inputs using \*args**
# MAGIC * **Task:** 
# MAGIC   1. Define a function named `sum_all_args`.
# MAGIC   2. Accept dynamic positional arguments using `*args: int`.
# MAGIC   3. Use the built-in `sum()` function to return the total sum of all provided arguments.
# MAGIC

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC **4. Dynamic Inputs using \*\*kwargs**
# MAGIC * **Task:** 
# MAGIC   1. Define a function named `print_config`.
# MAGIC   2. Accept dynamic keyword arguments using `**kwargs: str`.
# MAGIC   3. Iterate through `kwargs.items()` and print `"{key} is set to {value}"` for each item.
# MAGIC
# MAGIC

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC **5. Transforming Data with map()**
# MAGIC * **Task:** 
# MAGIC   1. Create a list of integers `[10, 20, 30]`.
# MAGIC   2. Define a function `add_five(num: int) -> int` that adds 5 to a number.
# MAGIC   3. Use `map()` to apply `add_five` to your list and convert the result back to a list.
# MAGIC
# MAGIC

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ### **Hard**
# MAGIC
# MAGIC **6. Extracting Data with filter()**
# MAGIC * **Task:** 
# MAGIC   1. Create a list of words `["cat", "elephant", "dog", "hippopotamus"]`.
# MAGIC   2. Define a function `is_short_word(word: str) -> bool` that returns `True` if the word length is less than 5.
# MAGIC   3. Use `filter()` to apply this condition to the list and convert the result back to a list.
# MAGIC

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC **7. Combining \*args, filter(), and map()**
# MAGIC * **Task:** 
# MAGIC   1. Define a function `process_pipeline(*args: int) -> list`.
# MAGIC   2. Inside the function, first use `filter()` to keep only even numbers from `args`.
# MAGIC   3. Then, use `map()` to multiply those remaining even numbers by 10.
# MAGIC   4. Return the final list.
# MAGIC
# MAGIC

# COMMAND ----------

