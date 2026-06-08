# Databricks notebook source
# MAGIC %md
# MAGIC # Python Data Engineering Fundamentals - Error Handling Exercise
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Easy**
# MAGIC
# MAGIC **1. Catching ZeroDivisionError**
# MAGIC * **Task:** 
# MAGIC   1. Inside a `try` block, attempt to divide 50 by 0.
# MAGIC   2. Catch the `ZeroDivisionError`.
# MAGIC   3. Print `"Cannot divide by zero!"`.
# MAGIC

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC **2. Catching TypeError**
# MAGIC * **Task:** 
# MAGIC   1. Inside a `try` block, attempt to add `"Databricks"` and `10` together.
# MAGIC   2. Catch the `TypeError`.
# MAGIC   3. Print `"You cannot add a string and an integer."`.
# MAGIC

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ### **Medium**
# MAGIC
# MAGIC **3. Handling Multiple Specific Exceptions**
# MAGIC * **Task:** 
# MAGIC   1. Create a variable `val = "text"`.
# MAGIC   2. Use a `try` block to evaluate `100 / int(val)`.
# MAGIC   3. Add an `except` block for `ValueError` (printing "Value Error").
# MAGIC   4. Add an `except` block for `ZeroDivisionError` (printing "Zero Division Error").
# MAGIC

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC **4. Raising Custom Exceptions**
# MAGIC * **Task:** 
# MAGIC   1. Create a function `validate_temperature(temp: int)`.
# MAGIC   2. If the temperature is over 100, use `raise Exception("Temperature is critically high!")`.
# MAGIC   3. Test the function in a `try/except` block passing `105` and print the exception message.
# MAGIC

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC **5. Catching KeyError with Dictionary Access**
# MAGIC * **Task:** 
# MAGIC   1. Define a dictionary `config = {"mode": "append"}`.
# MAGIC   2. Inside a `try` block, attempt to print `config["path"]`.
# MAGIC   3. Catch the `KeyError` and print a fallback string `"Path not found in config"`.
# MAGIC

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ### **Hard**
# MAGIC
# MAGIC **6. Safe Type-Casting Wrapper**
# MAGIC * **Task:** 
# MAGIC   1. Create a function `safe_integer_cast(value)`.
# MAGIC   2. In a `try` block, convert and return `int(value)`.
# MAGIC   3. Catch both `ValueError` and `TypeError` using a single generic `Exception` block, and return `-1` if casting fails.
# MAGIC

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC **7. Uninterrupted Loop with Try/Except**
# MAGIC * **Task:** 
# MAGIC   1. Iterate over a mixed list `[10, 0, "5", "abc", 2]`.
# MAGIC   2. Inside the loop, use a `try` block to divide `20` by `int(item)`.
# MAGIC   3. Catch `Exception` to ignore any errors (ValueError, ZeroDivisionError), print the error, and use `continue` to move to the next iteration.
# MAGIC

# COMMAND ----------

