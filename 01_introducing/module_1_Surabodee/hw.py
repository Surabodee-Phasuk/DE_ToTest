# Databricks notebook source
# MAGIC %md
# MAGIC **Ex 1 write ETL pipeline**
# MAGIC   - run %run ./_functions
# MAGIC   - ingest from kaggle dataset <https://www.kaggle.com/datasets>
# MAGIC     - copy file path from <> Code section
# MAGIC     - copy file name
# MAGIC     - use get_kaggle_dataset_to_df() function  to retrive data via api
# MAGIC     - select data with sql
# MAGIC   
# MAGIC   - transform data
# MAGIC     - filter data with sql statement
# MAGIC   
# MAGIC   - load data to data-lakehouse
# MAGIC     - use load_to_delta_table() function to load data to lakehouse

# COMMAND ----------

# MAGIC %run ../_functions 

# COMMAND ----------

#extract
path = "joaocoelho03/pocket-tcg-dataset"
file_name = "pokemon_cards.csv"

get_kaggle_dataset_to_df(path,file_name).createOrReplaceTempView("raw_kaggle_dataset")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from raw_kaggle_dataset 

# COMMAND ----------

#transform
sql_statement = """ select * from raw_kaggle_dataset where card_rarity = "Double Rare" """

spark.sql(sql_statement).createOrReplaceTempView("transform_kaggle_dataset")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from transform_kaggle_dataset

# COMMAND ----------

#load
load_to_delta_table("transform_kaggle_dataset","Might_pokemon_cards")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from default.Might_pokemon_cards

# COMMAND ----------

# MAGIC %md
# MAGIC **Ex2. convert from ETL pipeline to ELT ![pipeline](path)**

# COMMAND ----------

# extract
path = "joaocoelho03/pocket-tcg-dataset"
file_name = "pokemon_cards.csv"
get_kaggle_dataset_to_df(path,file_name).createOrReplaceTempView("raw_kaggle_dataset")

# COMMAND ----------

#load
load_to_delta_table("raw_kaggle_dataset","All_pokemon_cards")

# COMMAND ----------

#tranform
sql_statement = """ select * from raw_kaggle_dataset where pack_name = "Promo A" """

spark.sql(sql_statement).createOrReplaceTempView("transformed_result_view")

# COMMAND ----------

load_to_delta_table("transformed_result_view", "Final_pokemon_Cards")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from default.Final_pokemon_cards

# COMMAND ----------

