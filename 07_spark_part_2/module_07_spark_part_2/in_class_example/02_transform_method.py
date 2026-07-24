# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.window import *

# COMMAND ----------

# MAGIC %md
# MAGIC # Initial DataFrame

# COMMAND ----------

sales_df = (
    spark.table("dev_catalog.dwh.sales_by_store")
    .withColumn("shop_id_2",lit("1"))
    .withColumn("date_str",lit("2025-01-01"))
    )

shop_name_df = (
    spark.table("dev_catalog.dwh.shop_name")
    .withColumn("shop_id_2",lit("1"))
    )

# COMMAND ----------

sales_by_store = spark.read.table("dev_catalog.dwh.sales_by_store")

# COMMAND ----------

# MAGIC %md
# MAGIC # Basic Method

# COMMAND ----------

"""ordery by"""
sorted_df = sales_df.orderBy(col("date").desc() , "sales_amount")
print("sorted_df")
sorted_df.display()

"""limit"""
limit_df = sales_df.limit(10)
print('limit_df')
limit_df.display()

"""drop"""
drop_df = sales_df.drop("date")
print("drop_date")
drop_df.display()

"""drop duplication / distinct"""
drop_dup_df = sales_df.select("shop_id","shop_id_2").distinct()
print("drop_dup_df")
drop_dup_df.display()

drop_dup_with_col_df = sales_df.dropDuplicates(["shop_id"])
print("drop_dup_with_col_df")
drop_dup_with_col_df.display()

"""drop na"""
drop_na_df = sales_df.dropna()
print("drop which has column that has null value")
drop_na_df.display()

"""drop null with specific subset"""
drop_na_df = sales_df.dropna(subset=["store_size"])
print("drop null with specific subset")
drop_na_df.display()

"""fill na with specific value"""
drop_na_df = sales_df.fillna("0")
print("fill na with specific value")
drop_na_df.display()

"""fill na with specific value and column"""
drop_na_col_df = sales_df.fillna(0,subset=["store_size"])
print("fill na with specific value and column")
drop_na_col_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC # union
# MAGIC - union
# MAGIC - union all
# MAGIC - union by name
# MAGIC - union by name allowMissingColumns

# COMMAND ----------

"""union / union all / union by name"""
union_df = (
    sales_df
    .union(sales_df)
)
print("union")
union_df.display()

union_all_df = (
    sales_df
    .unionAll(sales_df)
)
print("union all")
union_all_df.display()

union_by_name_df = (
    sales_df.select("shop_id","date","store_size","sales_amount","shop_id_2")
    .unionByName(sales_df.select("date","shop_id","store_size","sales_amount","shop_id_2"))
)
print("union by name")
union_by_name_df.display()


union_by_name_allow_missing_df = (
    sales_df.select("shop_id","date")
    .unionByName(sales_df,allowMissingColumns=True)
)
print("union by name allowMissingColumns")
union_by_name_allow_missing_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC # Intersect
# MAGIC - intersect
# MAGIC - intersectAll

# COMMAND ----------

print("sample_dataset")
sales_df.select("shop_id","store_size").display()

print("intersect")
sales_df.select("shop_id","store_size").intersect(sales_df.select("shop_id","store_size")).display()
print("intersectAll")
sales_df.select("shop_id","store_size").intersectAll(sales_df.select("shop_id","store_size")).display()

# COMMAND ----------

# MAGIC %md
# MAGIC # Except
# MAGIC - exceptAll
# MAGIC - subtract (except)

# COMMAND ----------

new_sales_1 = sales_df.select("shop_id","store_size")
new_sales_2 = sales_df.select("shop_id","store_size").distinct()

print("new_sales_1")
new_sales_1.display()
print("new_sales_2")
new_sales_2.display()
print("exceptAll")
new_sales_1.exceptAll(new_sales_2).display()
print("subtract")
new_sales_1.subtract(new_sales_2).display()

# COMMAND ----------

# MAGIC %md
# MAGIC # Complex DataType
# MAGIC - struct
# MAGIC - map
# MAGIC - split
# MAGIC - get_item
# MAGIC - split_part
# MAGIC - explode
# MAGIC - array_contains
# MAGIC - collect_list / collect_set

# COMMAND ----------

#struct
struct_df = (
    sales_df
    .select(
        "shop_id"
        ,struct(
            col("store_size")
            ,col("sales_amount")
        ).alias("store_detail")
    )
    )

#map
map_df = (
    sales_df
    .select(
        col("shop_id")
        ,create_map(
            lit(1),col("store_size"),lit(2),col("sales_amount").cast("string")
            )
        )
    )

map_df.display()

# COMMAND ----------

"""split"""
split_df = (
    sales_df
    .withColumn("date_split",split(col("date"),"-"))
    .withColumn("year",col("date_split")[0])
    .withColumn("mm",col("date_split").getItem(1))
    .withColumn("dd",col("date_split").getItem(2))
    .withColumn("date_split_part_year",split_part(col("date"),lit("-"),lit(1)))
)
print("split")
split_df.display()

"""get_item"""
get_item_df = (
    split_df
    .select(
        "date_split"
        ,col("date_split").getItem(0)
        )
    )
get_item_df.display()

"""split_part"""
split_part_df = (
    split_df
    .select(
        "date"
        ,split_part(col("date"),lit("-"),lit(1))
        ,split_part(col("date"),lit("-"),lit(-1))
        )
    )
split_part_df.display()

"""explode"""
explode_df = (
    sales_df
    .withColumn("date_split",split(col("date"),"-"))
    .withColumn("date_split",explode(col("date_split")))
)
print("explode")
explode_df.display()

"""array_contain"""
array_contains_df = (
    sales_df
    .withColumn("date_split",split(col("date"),"-"))
    .withColumn("is_contain_02",array_contains(col("date_split"),lit("02")))
)
print("array_contains")
array_contains_df.display()

"""collect list / collect_set"""
collect_list_df = (
    sales_df
    .groupBy("shop_id")
    .agg(collect_list(col("shop_id_2")).alias("shop_id_2_list"))
)
print("collect_list")
collect_list_df.display()

collect_set_df = (
    sales_df
    .groupBy("shop_id")
    .agg(collect_set(col("shop_id_2")).alias("shop_id_2_list"))
)
print("collect_set")
collect_set_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC # string function
# MAGIC - upper
# MAGIC - lower
# MAGIC - regexp_replace
# MAGIC - length
# MAGIC - substring
# MAGIC - trim

# COMMAND ----------

"""string function"""
string_df = (
    sales_df
    .withColumn("store_size_upper", upper(col("store_size")))
    .withColumn("store_size_lower", lower(col("store_size")))
    .withColumn("store_size_replace", regexp_replace(col("store_size"), "l", "L"))
    .withColumn("store_size_length", length(col("store_size")))
    .withColumn("store_size_substring", substring(col("store_size"), 1, 3))
    .withColumn("store_size_trim", trim(col("store_size")))
)

string_df.display()

# COMMAND ----------

"""date /datetime function"""
date_df = (
    sales_df
    .withColumn("date_add_7", date_add(col("date"), 7))
    .withColumn("date_sub_7", date_sub(col("date"), 7))
    .withColumn("datediff_from_2025_01_01", datediff(lit("2025-01-01"), col("date")))
    .withColumn("year", year(col("date")))
    .withColumn("month", month(col("date")))
    .withColumn("day", day(col("date")))
    .withColumn("weekofyear", weekofyear(col("date")))
    .withColumn("dayofweek", dayofweek(col("date")))
    .withColumn("dayofmonth", dayofmonth(col("date")))
    .withColumn("dayofyear", dayofyear(col("date")))
    .withColumn("current_date", current_date())
    .withColumn("current_timestamp", current_timestamp())
    .withColumn("last_day", last_day(col("date")))
    .withColumn("next_friday", next_day(col("date"), "Friday"))
    .withColumn("add_months_2", add_months(col("date"), 2))
    .withColumn("months_between_2025_01_01", months_between(lit("2025-01-01"), col("date")))
    .withColumn("to_date", to_date(col("date")))
    .withColumn("to_timestamp", to_timestamp(col("date")))
)

date_df.display()

# COMMAND ----------

"""window function"""
partition_by_shop_id = Window.partitionBy("shop_id").orderBy(col("sales_amount").desc())
window_function_df = (
    sales_df
    .withColumn("row_number", row_number().over(partition_by_shop_id))
    .withColumn("rank", rank().over(partition_by_shop_id))
    .withColumn("dense_rank", dense_rank().over(partition_by_shop_id))
    .withColumn("lag_sales_amount", lag("sales_amount", 1).over(partition_by_shop_id))
    .withColumn("lead_sales_amount", lead("sales_amount", 1).over(partition_by_shop_id))
    .withColumn("first_sales_amount", first("sales_amount").over(partition_by_shop_id))
    .withColumn("min_sales_amount", min("sales_amount").over(partition_by_shop_id))
    .withColumn("max_sales_amount", max("sales_amount").over(partition_by_shop_id))
    .withColumn("sum_sales_amount", sum("sales_amount").over(partition_by_shop_id))
    .withColumn("avg_sales_amount", avg("sales_amount").over(partition_by_shop_id))
    .withColumn("count_sales_amount", count("sales_amount").over(partition_by_shop_id))
)

window_function_df.display()

# COMMAND ----------

from pyspark.sql.functions import coalesce

coalesce_df = (
    sales_df
    .withColumn("store_size_new",coalesce(col("store_size"), lit("store_not_found")))
    )

display(coalesce_df)

# COMMAND ----------

sales_df.groupBy("shop_id").agg(count("*")).display()
sales_df.groupBy("shop_id").count().display()

# COMMAND ----------

"""window function"""
partition_by_shop_id = Window.partitionBy("shop_id").orderBy(col("sales_amount").desc())
window_function_df = (
    sales_df
    .withColumn("row_number", row_number().over(partition_by_shop_id))
    .withColumn("rank", rank().over(partition_by_shop_id))
    .withColumn("dense_rank", dense_rank().over(partition_by_shop_id))
    .withColumn("ntile_3", ntile(3).over(partition_by_shop_id))
    .withColumn("percent_rank", percent_rank().over(partition_by_shop_id))
    .withColumn("cume_dist", cume_dist().over(partition_by_shop_id))
    .withColumn("lag_sales_amount", lag("sales_amount", 1).over(partition_by_shop_id))
    .withColumn("lead_sales_amount", lead("sales_amount", 1).over(partition_by_shop_id))
    .withColumn("first_sales_amount", first("sales_amount").over(partition_by_shop_id))
    .withColumn("last_sales_amount", last("sales_amount").over(partition_by_shop_id))
    .withColumn("min_sales_amount", min("sales_amount").over(partition_by_shop_id))
    .withColumn("max_sales_amount", max("sales_amount").over(partition_by_shop_id))
    .withColumn("sum_sales_amount", sum("sales_amount").over(partition_by_shop_id))
    .withColumn("avg_sales_amount", avg("sales_amount").over(partition_by_shop_id))
    .withColumn("count_sales_amount", count("sales_amount").over(partition_by_shop_id))
    .withColumn("nth_value_sales_amount", nth_value("sales_amount", 2).over(partition_by_shop_id))
)

window_function_df.display()