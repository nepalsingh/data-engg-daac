### sales connection 


``` python code
# Databricks Notebook
# ==========================================
# Create Salesforce OAuth Access Token
# ==========================================

# COMMAND ----------

# Install requests package if needed
# %pip install requests

# COMMAND ----------

import requests
import json

# COMMAND ----------

# ==========================================
# Salesforce OAuth Configuration
# ==========================================

# Recommended:
# Store these in Databricks Secrets

CLIENT_ID = dbutils.secrets.get("salesforce", "client_id")
CLIENT_SECRET = dbutils.secrets.get("salesforce", "client_secret")
USERNAME = dbutils.secrets.get("salesforce", "username")
PASSWORD = dbutils.secrets.get("salesforce", "password")
SECURITY_TOKEN = dbutils.secrets.get("salesforce", "security_token")

# Salesforce login URL
# Production:
SF_LOGIN_URL = "https://login.salesforce.com"

# Sandbox example:
# SF_LOGIN_URL = "https://test.salesforce.com"

# COMMAND ----------

# ==========================================
# OAuth Token Endpoint
# ==========================================

token_url = f"{SF_LOGIN_URL}/services/oauth2/token"

payload = {
    "grant_type": "password",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "username": USERNAME,
    "password": PASSWORD + SECURITY_TOKEN
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# COMMAND ----------

# ==========================================
# Request Access Token
# ==========================================

response = requests.post(
    token_url,
    data=payload,
    headers=headers
)

# COMMAND ----------

# ==========================================
# Handle Response
# ==========================================

if response.status_code == 200:

    token_response = response.json()

    access_token = token_response.get("access_token")
    instance_url = token_response.get("instance_url")
    issued_at = token_response.get("issued_at")
    signature = token_response.get("signature")

    print("===================================")
    print("Salesforce OAuth Token Created")
    print("===================================")

    print(f"Instance URL : {instance_url}")
    print(f"Issued At    : {issued_at}")
    print(f"Signature    : {signature}")

    print("\nAccess Token:")
    print(access_token)

else:

    print("===================================")
    print("Failed to Generate Token")
    print("===================================")

    print(f"Status Code : {response.status_code}")
    print("Response:")
    print(response.text)

# COMMAND ----------

# ==========================================
# OPTIONAL:
# Store Access Token in Spark Config
# ==========================================

spark.conf.set("salesforce.access.token", access_token)

print("Token stored in Spark session config")

# COMMAND ----------

# ==========================================
# OPTIONAL:
# Save Token to Secret Scope
# (Run manually via CLI if preferred)
# ==========================================

# Example:
# databricks secrets put --scope salesforce --key access_token

# COMMAND ----------

# ==========================================
# Example Usage with SpringML Connector
# ==========================================

sfOptions = {
    "sfURL": instance_url,
    "sfUser": USERNAME,
    "sfPassword": PASSWORD,
    "sfSecurityToken": SECURITY_TOKEN
}

df = spark.read.format("com.springml.spark.salesforce") \
    .options(**sfOptions) \
    .option("query", "SELECT Id, Name FROM Account LIMIT 10") \
    .load()

display(df)

```
