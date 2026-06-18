# Databricks notebook source
# MAGIC %md
# MAGIC # STRING

# COMMAND ----------

text = "  pyThon proGramming "
print("text" ,text)

print("text.lower()  ->",text.lower())
print("text.upper()  ->",text.upper())
print("text.capitalize()  ->",text.capitalize())
print("text.title()  ->",text.title())

print("text.strip()  ->",text.strip())
print("text.lstrip()  ->",text.lstrip())
print("text.rstrip()  ->",text.rstrip())

print('text.replace("pyt","eiei") -> ',text.replace("pyt","eiei"))
print('text.replace("py","eiei") -> ',text.replace("py","eiei"))

# COMMAND ----------

# Split
sentence = "apple,banana,cherry"
fruits_list = sentence.split(",")
print("sentence.split(",")  ->",fruits_list)

# Join string
new_sentence = ' - '.join(fruits_list)
print("' - '.join(fruits_list)  ->",new_sentence)

# COMMAND ----------

# search for word
filename = "report.pdf"

print('filename.startswith(".pdf")  ->',filename.startswith(".pdf"))
print('filename.startswith("report")  ->',filename.startswith("report"))
print('filename.endswith(".pdf")  ->',filename.endswith(".pdf"))
print('filename.find(".")  ->',filename.find("."))

# COMMAND ----------

string_1 = "hello"
string_2 = "world"

print(string_1 + string_2)
print(string_1,string_2)
print("{} {}".format(string_1,string_2))
print(f"{string_1} {string_2} eiei")
print(f"string_1: {string_1}",f"string_2: {string_2}")
print(f"{string_1 = }",f"{string_2 = }")

# COMMAND ----------

# MAGIC %md
# MAGIC # INT

# COMMAND ----------

num = -12345

print("abs(num) ->", abs(num))
print("num + 10 ->", num + 10)
print("num - 5 ->", num - 5)
print("num * 2 ->", num * 2)
print("num // 3 ->", num // 3)
print("num / 3 ->", num / 3)
print("num % 7 ->", num % 7)
print("num ** 2 ->", num ** 2)
print("-num ->", -num)
print("+num ->", +num)
print("int('101', 2) ->", int('101', 2))

# COMMAND ----------

# MAGIC %md
# MAGIC # float

# COMMAND ----------

num_float = -123.456

print("abs(num_float) ->", abs(num_float))
print("round(num_float) ->", round(num_float))
print("round(num_float, 2) ->", round(num_float, 2))
print("num_float + 10.5 ->", num_float + 10.5)
print("num_float - 5.1 ->", num_float - 5.1)
print("num_float * 2.0 ->", num_float * 2.0)
print("num_float / 3.0 ->", num_float / 3.0)
print("num_float // 3.0 ->", num_float // 3.0)
print("num_float % 7.0 ->", num_float % 7.0)
print("num_float ** 2 ->", num_float ** 2)
print("-num_float ->", -num_float)
print("+num_float ->", +num_float)
print("float('123.45') ->", float('123.45'))

# COMMAND ----------

# MAGIC %md
# MAGIC # boolean

# COMMAND ----------

bool_true = True
bool_false = False

print("bool_true == bool_false ->", bool_true == bool_false)
print("bool_true != bool_false ->", bool_true != bool_false)
print("bool_true == True ->", bool_true == True)
print("bool_false == False ->", bool_false == False)
print("bool_true > bool_false ->", bool_true > bool_false)
print("bool_true < bool_false ->", bool_true < bool_false)
print("bool_true + bool_false ->", bool_true + bool_false)
print("bool_true + 1 ->", bool_true + 1)
print("bool_false + 1 ->", bool_false + 1)

print("bool_true and bool_false ->", bool_true and bool_false)
print("bool_true or bool_false ->", bool_true or bool_false)
print("not bool_true ->", not bool_true)
print("not bool_false ->", not bool_false)
print("bool(True) ->", bool(True))
print("bool(False) ->", bool(False))
print("bool(1) ->", bool(1))
print("bool(0) ->", bool(0))
print("bool('') ->", bool(''))
print("bool('hello') ->", bool('hello'))
print("bool([]) ->", bool([]))
print("bool([1, 2]) ->", bool([1, 2]))
print("bool(None) ->", bool(None))
print("bool({}) ->", bool({}))
print("bool({'a': 1}) ->", bool({'a': 1}))
print("isinstance(bool_true, bool) ->", isinstance(bool_true, bool))
print("isinstance(bool_false, bool) ->", isinstance(bool_false, bool))