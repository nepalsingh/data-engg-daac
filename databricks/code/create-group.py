import requests
import json

# vaye


# Databricks workspace details
# e.g., https://<databricks-instance>.cloud.databricks.com
DATABRICKS_INSTANCE = '<databricks-instance-url>'
TOKEN = '<your-databricks-token>'
API_URL = f"{DATABRICKS_INSTANCE}/api/2.0/preview/scim/v2/Groups"

# Headers for API calls
HEADERS = {
    'Authorization': f"Bearer {TOKEN}",
    'Content-Type': 'application/json',
}

# Create a new group


def create_group(group_name):
    data = {
        "displayName": group_name
    }
    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(data))
    if response.status_code == 201:
        print(f"Group '{group_name}' created successfully.")
    else:
        print(f"Error creating group: {response.text}")

# Add a user to the group


def add_user_to_group(group_id, user_id):
    data = {
        "schemas": ["urn:ietf:params:scim:schemas:core:2.0:PatchOp"],
        "Operations": [
            {
                "op": "add",
                "path": "members",
                "value": [
                    {
                        "value": user_id
                    }
                ]
            }
        ]
    }
    response = requests.patch(
        f"{API_URL}/{group_id}", headers=HEADERS, data=json.dumps(data))
    if response.status_code == 200:
        print(f"User '{user_id}' added to group '{group_id}' successfully.")
    else:
        print(f"Error adding user: {response.text}")

# List all groups


def list_groups():
    response = requests.get(API_URL, headers=HEADERS)
    if response.status_code == 200:
        groups = response.json().get('Resources', [])
        print("Groups:")
        for group in groups:
            print(group['displayName'], "ID:", group['id'])
    else:
        print(f"Error fetching groups: {response.text}")


# Example usage
if __name__ == "__main__":
    group_name = "my_new_group"
    user_id = "user_id_example"  # You need the user_id from the SCIM API to add a user

    # Create a group
    create_group(group_name)

    # List groups to find group_id
    list_groups()

    # Example of adding a user to a group
    # Replace `group_id` and `user_id` with actual IDs
    # add_user_to_group(group_id="group_id_example", user_id=user_id)
