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
  

   - Click 'Generate new token' and securely store it.
<img width="432" height="646" alt="image" src="https://github.com/user-attachments/assets/08fff6d1-2776-45dc-9f3c-ab64e6caf337" />
