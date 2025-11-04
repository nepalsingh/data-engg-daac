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

Overview AWS Single Sign-On (SSO), now called AWS IAM Identity Center, allows centralized access management across AWS accounts and cloud applications. Users can log in via corporate credentials managed by an external Identity Provider (IdP).

Prerequisites

AWS account with Administrator Access.

Identity Provider (IdP) supporting SAML 2.0 (e.g., Azure AD, Okta, Google Workspace).

User accounts in the IdP ready for AWS access.

Browser with admin access to AWS console and IdP.

Enable AWS IAM Identity Center

Log in to the AWS Management Console.

Navigate to IAM Identity Center.

Click Enable IAM Identity Center.

Select a default directory or integrate with AWS Managed Microsoft AD / AD Connector.

Note the IAM Identity Center URL for SSO login (e.g., https://.awsapps.com/start).

Configure Identity Source

In IAM Identity Center, navigate to Settings > Identity Source.

Choose External Identity Provider (SAML 2.0).

Upload the IdP metadata file or provide IdP metadata URL.

Save the configuration.

Configure SAML Integration in IdP

In your IdP (Azure AD, Okta, Google):

Create a New Enterprise Application / SAML App.

Set AWS SSO as the service provider.

Provide the AWS SSO ACS URL and Entity ID from AWS IAM Identity Center.

Configure User Attributes & Claims:

username → UserName

email → Email

firstName → FirstName

lastName → LastName

Assign users or groups who need AWS access.

Download IdP metadata file for AWS configuration.

Assign AWS Account Access

In IAM Identity Center, navigate to AWS Accounts > Assign Users.

Select the AWS accounts and permission sets to assign.

Create a Permission Set (predefined or custom):

Example: AdministratorAccess, PowerUserAccess, ReadOnlyAccess.

Map it to the appropriate groups or users from IdP.

Test SSO Login

Open the AWS SSO URL in a browser.

Sign in using IdP credentials.

Verify that the user can see assigned AWS accounts and assume the correct permission set.

Optional: Enable Auditing & Logging

Enable AWS CloudTrail to track SSO login events.

Monitor user activity for compliance and security.

Troubleshooting Tips

Ensure time synchronization between IdP and AWS.

Check SAML attribute mappings if users cannot access AWS accounts.

Verify that permission sets are correctly assigned.

Review IdP metadata for expired certificates.


