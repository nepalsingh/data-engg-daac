# Assuming you're using Databricks' `spark` instance

# Get all tables from information_schema
tables_df = spark.sql("""
    SELECT table_schema, table_name
    FROM information_schema.tables
    WHERE table_type = 'BASE TABLE'
""")

# Iterate through each table and check grants
user_or_group = "user_or_group_name"
for row in tables_df.collect():
    schema = row['table_schema']
    table = row['table_name']
    
    grants_df = spark.sql(f"SHOW GRANTS ON TABLE {schema}.{table}")
    if grants_df.filter(grants_df['grantee'] == user_or_group).count() > 0:
        print(f"{user_or_group} has access to {schema}.{table}")
