```
# Parameters
catalog = "main"
schema = "sales"
volume_path = "/Volumes/main/sales/raw_volume"

# List all files in volume
files = dbutils.fs.ls(volume_path)

for file in files:
    
    # Process only CSV files
    if file.path.endswith(".csv"):
        
        # Extract table name from file name
        table_name = file.name.replace(".csv", "")
        
        print(f"Processing file: {file.name}")
        
        # Read CSV
        df = spark.read \
            .option("header", "true") \
            .option("inferSchema", "true") \
            .csv(file.path)
        
        # Write as managed Delta table
        df.write \
            .mode("overwrite") \
            .saveAsTable(f"{catalog}.{schema}.{table_name}")
        
        print(f"Table created: {catalog}.{schema}.{table_name}")

print("All CSV files processed successfully.")


```

```
schema = "sales"

tables = spark.sql(f"SHOW TABLES IN hive_metastore.{schema}").collect()

for t in tables:
    table_name = t.tableName
    ddl = spark.sql(f"SHOW CREATE TABLE hive_metastore.{schema}.{table_name}").collect()[0][0]
    print(f"\n-- DDL for {table_name}\n")
    print(ddl)

```
