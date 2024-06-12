# pip install msal requests


import msal
import requests
import json

# Azure AD configuration
client_id = "<your-client-id>"
tenant_id = "<your-tenant-id>"
username = "<your-username>"
password = "<your-password>"
authority = f"https://login.microsoftonline.com/{tenant_id}"
scope = ["https://databricks.azure.net/.default"]

# Databricks workspace URL
databricks_instance = "https://<your-databricks-instance>"

# Initialize the MSAL public client application
app = msal.PublicClientApplication(client_id, authority=authority)

# Acquire a token using username and password
token_response = app.acquire_token_by_username_password(
    username=username,
    password=password,
    scopes=scope
)

if "access_token" in token_response:
    # Extract the access token from the response
    access_token = token_response["access_token"]
    print("Azure AD Access Token:", access_token)

    # Now use this token to authenticate with Databricks API
    api_endpoint = f"{databricks_instance}/api/2.0/token/create"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "lifetime_seconds": 3600,  # Token validity in seconds (e.g., 1 hour)
        "comment": "Generated via API"
    }

    # Make a POST request to create a new token
    response = requests.post(
        api_endpoint, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        # Successful request
        new_token = response.json()["token_value"]
        print("New Databricks Token:", new_token)
    else:
        # Request failed
        print(f"Error: {response.status_code}, {response.text}")
else:
    print("Failed to obtain Azure AD access token")
