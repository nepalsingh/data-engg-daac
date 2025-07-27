from databricks.sdk import WorkspaceClient
from databricks.sdk.service import compute, command
import time

# Initialize
w = WorkspaceClient()

# Replace with your cluster ID
cluster_id = "<your-cluster-id>"

# Step 1: Get cluster status
cluster = w.clusters.get(cluster_id)

print(f"Cluster Name: {cluster.cluster_name}")
print(f"Cluster State: {cluster.state}")
print(f"State Message: {cluster.state_message}")

# Step 2: Check for known bad states
if cluster.state in ["TERMINATED", "ERROR", "INTERNAL_ERROR"]:
    print("❌ Cluster is crashed or terminated.")
elif cluster.state != "RUNNING":
    print("⚠️ Cluster is not in RUNNING state yet.")
else:
    # Step 3: Test responsiveness with a ping command
    try:
        cmd = w.command_execution.execute(
            cluster_id=cluster_id,
            language=compute.Language.PYTHON,
            command="print('ping')"
        )

        # Wait until command finishes
        timeout = time.time() + 30  # 30-second timeout
        while cmd.result.status == command.CommandStatus.RUNNING:
            if time.time() > timeout:
                print("❌ Cluster command timed out (non-responsive).")
                break
            time.sleep(2)
            cmd = w.command_execution.get_status(
                cluster_id=cluster_id,
                context_id=cmd.context_id,
                command_id=cmd.command_id
            )

        if cmd.result.status == command.CommandStatus.FINISHED:
            print("✅ Cluster is responsive.")
        else:
            print(f"❌ Cluster responded with status: {cmd.result.status}")
    except Exception as e:
        print(f"❌ Exception occurred when testing command: {e}")
