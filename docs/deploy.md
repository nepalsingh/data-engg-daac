Go to your GitHub repository → Actions tab.

Click on "Deploy Azure Data Factory" workflow.

Click "Run workflow".

From the dropdown:

Select the environment (dev, staging, or prod)

Specify the branch to deploy (e.g., main, release, feature-x)

Click Run workflow to trigger the deployment.

| Input Name    | Example Value              |
| ------------- | -------------------------- |
| `environment` | `dev`                      |
| `branch`      | `feature/datapipe-cleanup` |
