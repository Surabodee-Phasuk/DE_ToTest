# Databricks notebook source
#combine use
config = {"host": "localhost", "port": 5432, "db": "sales"}

# use .items() to iterate over the dictionary
for key, value in config.items():
    print(f"Setting {key} to {value}")

# use .values() to iterate over the dictionary
for value in config.values():
    print(f"Value: {value}")

# use .keys() to iterate over the dictionary
for key in config.keys():
    print(f"Key: {key}")

# use case: check if port is default and print message
if config["port"] == 5432:
    print("Default PostgreSQL port detected.")
else:
    print("Non-default port in use.")

# use case: loop and check if value is a string or integer
for key, value in config.items():
    if isinstance(value, str):
        print(f"{key} is a string.")
    elif isinstance(value, int):
        print(f"{key} is an integer.")
    else:
        print(f"{key} is of unknown type.")

# use case: loop and check for missing keys
required_keys = ["host", "port", "db", "user"]
for k in required_keys:
    if k in config:
        print(f"{k} found in config.")
    else:
        print(f"{k} missing from config.")