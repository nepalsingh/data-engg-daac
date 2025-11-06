User and Service Principal Creation in Databricks (AWS Cloud)
1. Overview
This document outlines the steps to create users and service principals in Databricks Account Console on AWS Cloud. Users are for human access, while service principals are for automated access (e.g., CI/CD pipelines, integrations).
2. Prerequisites
• Account Admin role in Databricks Account Console
• Access to https://accounts.cloud.databricks.com/
• Databricks account with Identity Federation enabled
• For API or Terraform automation, a valid Account-level Personal Access Token (PAT)
3. Create a User in Databricks Account Console
Follow these steps to add a user manually:
1. Log in to the Databricks Account Console: https://accounts.cloud.databricks.com/
2. Navigate to 'User management' → 'Users'.
3. Click 'Add user'.
4. Enter the user's email address.
5. (Optional) Assign account-level roles such as 'Account admin'.
6. Click 'Add'. The user receives an email invitation.
7. Assign the user to a workspace:
   - Go to 'Workspaces' → select the workspace → 'Manage users' → 'Add user'.
   - Select the user from the list and assign roles as needed.
4. Create a Service Principal (Service Account)
Service principals are used for automation, CI/CD, and non-human access.
Steps to create a service principal using the Account Console:
1. Log in to the Databricks Account Console.
2. Go to 'User management' → 'Service principals'.
3. Click 'Add service principal'.
4. Enter a display name (e.g., 'databricks-ci-cd-bot').
5. Leave 'Application ID' blank unless using an external IdP integration.
6. Click 'Add'.
7. Assign it to a workspace:
   - Go to 'Workspaces' → select workspace → 'Manage principals' → 'Add'.
   - Choose the new service principal.
8. Generate a Personal Access Token (PAT) for automation:
   - Within the workspace, go to the service principal's profile.
  

 AWS Single Sign-On (SSO) Configuration Guide
 Databricks supports authentication via OpenID Connect (OIDC), enabling users to log in with their corporate IdP credentials. Combined with SCIM provisioning, this allows automated user and group management in Databricks. OIDC is a modern, token-based alternative to SAML.

2. Prerequisites

Databricks workspace admin access.

Identity Provider (IdP) supporting OpenID Connect (e.g., Azure AD, Okta, Google Workspace).

Users and groups created in IdP.

Admin API token from Databricks workspace for SCIM provisioning.

Configure OIDC in Databricks

Log in to Databricks Admin Console.

Navigate to Authentication > OpenID Connect (OIDC).

Enter the following information from your IdP:

Client ID

Client Secret

Discovery URL / Issuer URL (e.g., https://login.microsoftonline.com/<tenant-id>/v2.0)

Set the Redirect URI as provided by Databricks.

Choose Provisioning Method: SCIM (for user/group sync).

Save configuration.

--------

Generate SCIM API Token in Databricks

In Databricks workspace, go to User Settings > Access Tokens.

Click Generate New Token, name it (e.g., OIDC_SCIM_Token), set expiration.

Copy and securely store the token.

5. Configure SCIM in Identity Provider
Azure AD (OIDC + SCIM)

In Azure AD, create a new enterprise application.

Set Single Sign-On method to OpenID Connect (OIDC).

Provide Client ID, Client Secret, and Redirect URI from Databricks.

Navigate to Provisioning > Automatic:

Enter SCIM endpoint URL from Databricks

Enter SCIM API token

Test connection and enable provisioning

Map attributes for users and groups:

userName → userPrincipalName

displayName → displayName

groups → memberOf




Driver=Databricks ODBC Driver;
Host=adb-1234567890123456.9.databricks.amazonaws.com;
Port=443;
HTTPPath=/sql/1.0/warehouses/abcd1234efgh5678;
AuthMech=3;
UID=token;
PWD=dapiXXXXXXXXXXXXXXXX;
SSL=1;
ThriftTransport=2;
SparkServerType=3;

