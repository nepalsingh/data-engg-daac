from pyspark.sql import SparkSession
import os

databricks_instance = os.environ.get("DATABRICKS_INSTANCE")
access_token = os.environ.get("ACCESS_TOKEN")

# how to authenticate to Databricks
spark = SparkSession.builder.appName("my-app") \
    .config("spark.databricks.workspace.url", databricks_instance) \
    .config("spark.databricks.token", access_token) \
    .getOrCreate()

# add schema as variable
schema = "my_schema"
catalog = "hive_metastore"

# Initialize a SparkSession
spark = SparkSession.builder.getOrCreate()

# Read a table from Databricks
df = spark.sql(f"SELECT * FROM {catalog}.{schema}.my_table")

# Show the first few rows of the DataFrame
df.show()
