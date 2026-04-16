# Databricks notebook source
dbutils.widgets.text("username", "default")
test = dbutils.widgets.get("username")
print(test)

# COMMAND ----------

dbutils.widgets.dropdown("username_dropdown","default",["default", "user1", "user2"])
test_dropdown = dbutils.widgets.get("username_dropdown")
print(test_dropdown)

# COMMAND ----------

dbutils.fs.ls("dbfs:/")