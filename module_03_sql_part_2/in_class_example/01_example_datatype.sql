-- Databricks notebook source
-- MAGIC %md
-- MAGIC ### Data Type Casting and Conversion Summary
-- MAGIC * **Numeric to String:** Converts numeric values into text strings.
-- MAGIC * **Integer Casting:** Explicitly defines values as standard integers.
-- MAGIC     * **Range:** -2,147,483,648 to 2,147,483,647 (4 bytes).
-- MAGIC * **Decimal to Integer (Truncation):** Casts decimal numbers to integers. **Note:** This truncates the decimal rather than rounding.
-- MAGIC * **Floating Point & Decimal:** Converts values to floating-point numbers or fixed-precision decimals (e.g., `decimal(10,2)`).
-- MAGIC * **Big Integer:** Casts values to `BIGINT` (8-byte integer).
-- MAGIC     * **Range:** -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807.
-- MAGIC * **String & Boolean Literals:** Explicitly casts values to String or Boolean types to ensure strict schema adherence.
-- MAGIC * **Date Parsing:** Uses `to_date` to convert strings into Date objects (Year-Month-Day).
-- MAGIC * **Timestamp Parsing:** Uses `to_timestamp` to convert strings into Timestamp objects (includes specific time).

-- COMMAND ----------

-- DBTITLE 1,cast datatype
select
  cast(123456 as string),
  cast(789 as int), 
  cast('2026' as string),
  cast(99.99 as int),
  cast(199.99 as float),
  cast(12.34 as decimal(10,2)),
  cast(56789 as bigint),
  cast('123.45' as string),
  cast(true as boolean),
  cast('High' as string),
  to_date('2026-02-10', 'yyyy-MM-dd'),
  to_date('2026/02/10', 'yyyy/MM/dd'),
  to_timestamp('2026-02-10 00:00:00', 'yyyy-MM-dd HH:mm:ss')

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Safe Type Conversion with TRY_CAST
-- MAGIC This query demonstrates the error-handling capability of `TRY_CAST` compared to the standard `CAST` function:
-- MAGIC
-- MAGIC * **Handling Invalid Input (`try_cast("hello" as int)`):**
-- MAGIC     * **Result:** `NULL`
-- MAGIC     * **Reason:** The string "hello" cannot be converted into an integer. Instead of throwing a runtime error (which standard `CAST` would do), `TRY_CAST` safely returns `NULL`, allowing the query to continue running.
-- MAGIC * **Handling Valid Input (`try_cast("200" as int)`):**
-- MAGIC     * **Result:** `200`
-- MAGIC     * **Reason:** The string "200" is a valid integer representation, so the function successfully converts it to the integer type.
-- MAGIC
-- MAGIC **Key Takeaway:** Use `TRY_CAST` when cleaning "dirty" data where some values might not match the expected target type, preventing your entire pipeline from crashing due to a single bad record.

-- COMMAND ----------

-- DBTITLE 1,try_cast
select 
    try_cast("hello" as int),
    try_cast("200" as int)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # sql basic functions
-- MAGIC #### 1. String Manipulation
-- MAGIC * **`length` / `upper` / `lower`**: Basic casing and length checks.
-- MAGIC * **`concat` / `substr`**: Joins strings or extracts substrings (1-based index).
-- MAGIC * **`trim` / `ltrim` / `rtrim`**: Removes whitespace from ends.
-- MAGIC * **`replace` / `regexp_replace`**: Replaces text literals or patterns (regex).
-- MAGIC
-- MAGIC #### 2. Numeric & Math
-- MAGIC * **`abs` / `pow` / `mod`**: Absolute value, power, and modulo (remainder).
-- MAGIC * **`ceil` / `floor` / `round`**: Rounding up, down, or to the nearest integer.
-- MAGIC * **`greatest` / `least`**: Selects the max/min value from a list of columns/values.
-- MAGIC
-- MAGIC #### 3. Date & Timestamp (Critical for ETL)
-- MAGIC * **`current_date` / `current_timestamp`**: Returns the current server date/time.
-- MAGIC * **`date_add` / `date_sub`**: Adds or subtracts days (useful for sliding windows).
-- MAGIC * **`datediff`**: Returns the difference in **days** between two dates.
-- MAGIC * **`trunc`**: Truncates a date to the specified unit (e.g., `'MM'` returns the 1st of the month).
-- MAGIC * **`last_day`**: Returns the last day of the current month (useful for month-end reporting).
-- MAGIC * **`year` / `month` / `dayofweek`**: Extracts specific components of a date.
-- MAGIC * **`date_format`**: Converts a timestamp into a custom string format.
-- MAGIC
-- MAGIC #### 4. NULL Handling (Critical for Data Quality)
-- MAGIC
-- MAGIC * **`coalesce`**: The "Swiss Army Knife" of NULL handling. Returns the **first non-null** value from a list.
-- MAGIC * **`ifnull`**: A simplified 2-argument version of `coalesce`.
-- MAGIC * **`nullif`**: Returns `NULL` if two arguments are equal.
-- MAGIC     * *Use Case:* Preventing "Divide by Zero" errors (e.g., `profit / NULLIF(revenue, 0)`).

-- COMMAND ----------

-- DBTITLE 1,sql functions
SELECT
  -- String functions
  length('Databricks'),
  upper('databricks'),
  lower('DATABRICKS'),
  concat('Data', 'bricks'),
  concat_ws(" ","Data","bricks"),
  substr('Databricks', 1, 4),
  trim('  Databricks  '),
  ltrim('  Databricks'),
  rtrim('Databricks  '),
  replace('Databricks', 'bricks', 'SQL'),
  regexp_replace('Databricks123', '[0-9]', ''),

  -- Int functions
  abs(-123),
  ceil(123.45),
  floor(123.45),
  round(123.45),
  pow(2, 3),
  mod(10, 3),
  greatest(10, 20, 30),
  least(10, 20, 30),

  -- Date & Timestamp Functions
  current_date(),
  current_timestamp(),
  date_add(current_date(), 1),
  date_sub(current_date(), 1),
  datediff('2026-12-31', current_date()),
  trunc(current_date(), 'MM'),
  last_day(current_date()),
  year(current_date()),
  month(current_date()),
  dayofweek(current_date()), -- 1=Sunday, 7=Saturday
  date_format(current_timestamp(), 'yyyy-MM-dd HH:mm:ss') ,
  to_timestamp('2026-02-12 10:00:00', 'yyyy-MM-dd HH:mm:ss') ,

  -- NULL Handling Functions
  coalesce(NULL, NULL, 'Third Choice', 'Fourth Choice'),
  ifnull(NULL, 'Default Value'),
  nullif('same', 'same') -- Returns NULL if equal

-- COMMAND ----------

select abs(-123) , pow(5,2), mod(20,15) , greatest("10","20","30"), least(10,20,30)

-- COMMAND ----------

select current_date(),year(current_date()) ,"20250102" , add_months(current_date())

-- COMMAND ----------

select null as col1 , "dataspark" as col2 , "piti" as col3 , coalesce(col3,col2,col1) , ifnull(col2,"is null"), nullif(col2,"piti")

-- COMMAND ----------

select to_date("20250102","yyyyMMdd") , to_date("2025/01/02","yyyy/MM/dd") ,to_date("02/01/2026","dd/MM/yyyy")

-- COMMAND ----------

create or replace table session_3_sql.multiple_date_format(
  date_format string
);

insert into session_3_sql.multiple_date_format values
("2026-01-01")
,("2026/01/01")
,("20260101")

-- COMMAND ----------

select date_format, 
  coalesce(
    try_to_date(date_format,"yyyy-MM-dd")
    ,try_to_date(date_format,"yyyyMMdd")
    ,try_to_date(date_format,"yyyy/MM/dd")
    ) from session_3_sql.multiple_date_format

-- COMMAND ----------

select * from session_2_sql.sales_by_store

-- COMMAND ----------

select store_size,store_size <> '' from session_2_sql.sales_by_store where store_size <> ''

-- COMMAND ----------

select store_size, not equal_null(store_size,'') from session_2_sql.sales_by_store

-- COMMAND ----------

select equal_null(null,'')