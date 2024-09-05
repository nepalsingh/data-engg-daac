import requests
import json

# Databricks workspace details
DATABRICKS_INSTANCE = '<databricks-instance-url>'  # e.g., https://<databricks-instance>.cloud.databricks.com
TOKEN = '<your-databricks-token>'
API_URL = f"{DATABRICKS_INSTANCE}/api/2.0/groups"

# Headers for API calls
HEADERS = {
    'Authorization': f"Bearer {TOKEN}",
    'Content-Type': 'application/json',
}

# Create a new group
def create_group(group_name):
    data = {
        "group_name": group_name
    }
    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(data))
    if response.status_code == 200:
        print(f"Group '{group_name}' created successfully.")
    else:
        print(f"Error creating group: {response.text}")

# Add a user to the group
def add_user_to_group(group_name, user_name):
    data = {
        "group_name": group_name,
        "parent_name": user_name
    }
    response = requests.post(f"{API_URL}/add-member", headers=HEADERS, data=json.dumps(data))
    if response.status_code == 200:
        print(f"User '{user_name}' added to group '{group_name}' successfully.")
    else:
        print(f"Error adding user: {response.text}")

# List all groups
def list_groups():
    response = requests.get(f"{API_URL}/list", headers=HEADERS)
    if response.status_code == 200:
        groups = response.json().get('group_names', [])
        print("Groups:", groups)
    else:
        print(f"Error fetching groups: {response.text}")

# Example usage
if __name__ == "__main__":
    group_name = "my_new_group"
    user_name = "user@example.com"

    create_group(group_name)
    add_user_to_group(group_name, user_name)
    list_groups()
