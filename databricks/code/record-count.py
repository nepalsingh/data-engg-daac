# Specify the database you want to get the row counts for
database_name = "your_database_name"

# Step 1: Get all tables in the database
tables_df = spark.sql(f"SHOW TABLES IN {database_name}")

# Step 2: Initialize an empty list to store table names and row counts
table_row_counts = []

# Step 3: Loop through each table and get the row count
for row in tables_df.collect():
    table_name = row["tableName"]
    full_table_name = f"{database_name}.{table_name}"
    
    # Get the row count
    row_count = spark.sql(f"SELECT COUNT(*) AS row_count FROM {full_table_name}").collect()[0]["row_count"]
    
    # Append the table name and row count to the list
    table_row_counts.append((full_table_name, row_count))

# Step 4: Convert the list into a DataFrame
row_counts_df = spark.createDataFrame(table_row_counts, ["table_name", "row_count"])

# Step 5: Save the DataFrame as a new table in Databricks
output_table_name = "table_row_counts"
row_counts_df.write.mode("overwrite").saveAsTable(output_table_name)

# Verify the results
spark.sql(f"SELECT * FROM {output_table_name}").show()

# Step 1: Get all tables in the database
database_name = "your_database_name"
tables_df = spark.sql(f"SHOW TABLES IN {database_name}")

# Step 2: Initialize an empty list to store table names and row counts
table_row_counts = []

# Step 3: Loop through each table and get the row count
for row in tables_df.collect():
    table_name = row["tableName"]
    full_table_name = f"{database_name}.{table_name}"
    
    # Get the row count
    row_count = spark.sql(f"SELECT COUNT(*) AS row_count FROM {full_table_name}").collect()[0]["row_count"]
    
    # Append the table name and row count to the list
    table_row_counts.append((full_table_name, row_count))

# Step 4: Convert the list into a DataFrame
row_counts_df = spark.createDataFrame(table_row_counts, ["table_name", "row_count"])

# Step 5: Define the ADLS location (make sure you have proper permissions and set up the mount point if needed)
adls_location = "abfss://<container_name>@<storage_account_name>.dfs.core.windows.net/<folder_name>/table_row_counts.csv"

# Step 6: Save the DataFrame as a CSV file in ADLS
row_counts_df.coalesce(1).write.mode("overwrite").option("header", "true").csv(adls_location)

# Optional: Verify the file in ADLS by listing the folder
dbutils.fs.ls("abfss://<container_name>@<storage_account_name>.dfs.core.windows.net/<folder_name>/")


