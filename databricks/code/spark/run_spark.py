from databricks.connect import DatabrickSession as DBS
from databricks.sdk.core import Config

import os

cluster_id = os.environ.get("CLUSTER_ID", "cls0-ddssdi-222",)
profile = os.environ.get("PROFILE", "default")


def run_spark(table_name: str, schema_name: str, profile: str, cluster_id: str):
    # Set up the Databricks session
    config = Config(profile, cluster_id=cluster_id)
    spark = DBS.builder.config(config).getOrCreate()
    return spark.sql(f"SELECT * FROM {catalog}.{schema_name}.{table_name}")


if __name__ == "__main__":
    table_name = "step"
    schema_name = "orchestration"
    catalog = "hive_metastore"
    data = run_spark(table_name, schema_name, profile, cluster_id)
    data.show()
