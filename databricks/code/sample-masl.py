import msal
import databricks.sql

# Replace with your actual Databricks and Azure AD credentials
TENANT_ID = 'your-tenant-id'
CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'
SERVER_HOSTNAME = 'your-server-hostname'
HTTP_PATH = 'your-http-path'

# Authority URL
authority_url = f"https://login.microsoftonline.com/{TENANT_ID}"

# Scope for Databricks SQL
scope = ["https://databricks.azure.net/.default"]

# Create a ConfidentialClientApplication instance
app = msal.ConfidentialClientApplication(
    client_id=CLIENT_ID,
    authority=authority_url,
    client_credential=CLIENT_SECRET
)

# Acquire a token
result = app.acquire_token_for_client(scopes=scope)

if "access_token" in result:
    access_token = result["access_token"]

    # Create a connection to Databricks SQL
    connection = databricks.sql.connect(
        server_hostname=SERVER_HOSTNAME,
        http_path=HTTP_PATH,
        access_token=access_token
    )

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    # Example query
    cursor.execute("SELECT * FROM your_table")

    # Fetch the results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor and connection
    cursor.close()
    connection.close()
else:
    print("Failed to obtain access token.")
