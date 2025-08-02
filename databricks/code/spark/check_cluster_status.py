from databricks.sdk import WorkspaceClient
import os

profile = os.environ.get("PROFILE", "default")
cluster_id = os.environ.get("CLUSTER_ID", "cls0-ddssdi-222")

# Initialize Databricks Workspace Client
w = WorkspaceClient(profile=profile)

# Get cluster info
cluster = w.clusters.get(cluster_id)

# Print cluster status
print(f"Cluster ID: {cluster_id}")
print(f"Cluster Name: {cluster.cluster_name}")
print(f"Cluster State: {cluster.state}")

# Check health and print message
if cluster.state not in ["RUNNING", "RESIZING"]:
    print("Cluster is not healthy and needs to be restarted.")
else:
    print("Cluster is healthy.")

# Run a simple command on the cluster to test accessibility
try:
    result = w.clusters.spark_submit(cluster_id, "--version")
    print("Cluster command executed successfully.")
    print("Result:", result)
except Exception as e:
    print("Failed to run command on cluster:", e)
