# Databricks notebook source
from pyspark.sql.functions import * 

# COMMAND ----------

# DBTITLE 1,initial spark object
sales_df = (
    spark.table("session_6_spark.sales_by_store")
    .withColumn("shop_id_2",lit("1"))
    .withColumn("date_str",lit("2025-01-01"))
    )
shop_name_df = (
    spark.table("session_6_spark.shop_name")
    .withColumn("shop_id_2",lit("1"))
    )

sales_df.display()
shop_name_df.display()

# COMMAND ----------

# DBTITLE 1,cast / convert data type sample
cast_number_df = (
    sales_df
    .select(
        "shop_id",
        # basic type
        col("shop_id").cast(StringType()),
        col("shop_id").cast("string"),
        col("shop_id").cast("tinyint"),
        col("shop_id").cast("short"),
        col("shop_id").cast("int"),
        col("shop_id").cast("long"),
        col("shop_id").cast("float"),
        col("shop_id").cast("double"),
        col("shop_id").cast("decimal(10,2)"),
        lit("2025-01-01").cast("date").alias("date_sample_1"),
        to_date(lit("2025/01/01"), "yyyy/mm/dd").alias("date_sample_2"),
        lit("2025-01-01 23:00:00").cast("timestamp").alias("ts_sample"),
        lit(1).cast("boolean").alias("1"),
        lit(0).cast("boolean").alias("2"),
        lit(3).cast("boolean").alias("3"),
        # complex type
        array(lit(1), lit(2)).alias("array_sample"),
        create_map(lit(1), lit(1),lit(2),lit(2)).alias("map_sample"),
        struct(lit(1).alias("a"), lit(2).alias("b")).alias("struct_sample")
    )
)

cast_number_df.display()

# COMMAND ----------

# DBTITLE 1,different style of join
"""join condition"""

join_alternative_df = (
    sales_df.alias("sales")
    .join(shop_name_df.alias("shop") ,sales_df.shop_id == shop_name_df.shop_id, "inner")
    .select(
         sales_df.date
         ,sales_df.shop_id
         ,sales_df.store_size
         ,sales_df.sales_amount
         ,shop_name_df.shop_name
    )
)

join_1_df = (
    sales_df.alias("sales")
    .join(shop_name_df.alias("shop") ,["shop_id","shop_id_2"], "inner")
    .select(
         "sales.date"
        ,"sales.shop_id"
        ,"sales.store_size"
        ,"sales.sales_amount"
        ,"shop.shop_name"
    )
)

join_2_df = (
    sales_df.alias("sales")
    .join(shop_name_df.alias("shop"),
          (col("sales.shop_id")     == col("shop.shop_id"))
          & (col("sales.shop_id_2") == col("shop.shop_id_2"))
          , "inner")
    .select(
         col("sales.date")
        ,col("sales.shop_id")
        ,col("sales.store_size")
        ,col("sales.sales_amount")
        ,col("shop.shop_name")
    )
)

join_3_df = (
    sales_df.alias("sales")
    .join(shop_name_df.alias("shop"),
          [
             col("sales.shop_id")   == col("shop.shop_id")
            ,col("sales.shop_id_2") == col("shop.shop_id_2")
            ]
          , "inner")
    .select(
         col("sales.date")
        ,col("sales.shop_id")
        ,col("sales.store_size")
        ,col("sales.sales_amount")
        ,col("shop.shop_name")
    )
)

# COMMAND ----------

# DBTITLE 1,join_4_df with date BETWEEN
join_4_df = (
    sales_df.alias("sales")
    .join(
        shop_name_df.alias("shop"),
        (
            (col("sales.shop_id") == col("shop.shop_id")) &
            (col("sales.date") >= col("shop.date_start")) &
            (col("sales.date") <= col("shop.date_end"))
        ),
        "inner"
    )
    .select(
        col("sales.shop_id"),
        col("sales.date"),
        col("sales.sales_amount"),
        col("shop.shop_name"),
        col("shop.date_start"),
        col("shop.date_end")
    )
)
display(join_4_df)

# COMMAND ----------

# DBTITLE 1,left_join vd left_semi
"""left join vs left semi join"""
join_4_left_df = (
    sales_df.alias("sales")
    .join(shop_name_df.alias("shop") ,[col("sales.shop_id") == col("shop.shop_id_2")], "left")
    .select(
         "sales.*"
    )
)

join_4_left_semi_df = (
    sales_df.alias("sales")
    .join(shop_name_df.alias("shop") ,[col("sales.shop_id") == col("shop.shop_id_2")], "left_semi")
)

print("sales_df")
sales_df.display()
print("shop_name_df")
shop_name_df.display()
print("join_4_left_df")
join_4_left_df.display()
print("join_4_left_semi_df")
join_4_left_semi_df.display()