# Operational Guide for Azure Databricks with Legacy Hive Metastore

This guide provides an overview of key operations in Azure Databricks, including workspace management, cluster management, job scheduling, and the integration of a legacy Hive metastore. Each section outlines the necessary steps and considerations for effective operation within the Azure Databricks environment.

## 1. Workspace Management

### 1.1 Workspace Organization
- **Creating Notebooks**:
  - Navigate to the Databricks workspace and select your desired folder.
  - Click on the "Create" button and select "Notebook".
  - Name your notebook, choose a default language (Python, Scala, SQL, or R), and create it.
- **Managing Artifacts**:
  - Use folders to organize notebooks, libraries, and data.
  - Right-click on items to move, rename, or delete them.

### 1.2 User and Group Management
- **Adding Users and Groups**:
  - Go to the "Admin Console".
  - Select the "Users" or "Groups" tab to add new users or create groups.
  - Assign users to groups and set permissions accordingly.
- **Permissions Management**:
  - Click on the "Permissions" option of a folder or notebook.
  - Add users/groups and set appropriate permissions (Read, Write, Manage).

### 1.3 Collaboration Tools
- **Sharing Notebooks**:
  - Open a notebook and click "Share".
  - Enter the email addresses of collaborators and set their access level.
- **Version Control**:
  - Integrate with Git by navigating to the "Repos" tab.
  - Follow prompts to connect to a Git repository and manage notebook versions.

### 1.4 Environment Configuration
- **Cluster Libraries**:
  - Go to "Clusters", select your cluster, and navigate to the "Libraries" tab.
  - Install required libraries either from Maven, PyPI, CRAN, or by uploading a JAR/egg/whl file.

### 1.5 Security and Compliance
- **Role-Based Access Control (RBAC)**:
  - Use the "Admin Console" to configure roles and permissions.
- **Audit Logs**:
  - Enable and configure audit logging in the Azure Portal to monitor activities.

### 1.6 Data Management
- **Mounting Data Stores**:
  - Use Databricks File System (DBFS) to mount Azure Blob Storage or Data Lake Storage.
  - Example:
    ```python
    dbutils.fs.mount(
        source = "wasbs://<container>@<storage-account>.blob.core.windows.net",
        mount_point = "/mnt/<mount-name>",
        extra_configs = {"<conf-key>":dbutils.secrets.get(scope = "<scope-name>", key = "<key-name>")}
    )
    ```
- **Using Delta Lake**:
  - Convert Parquet files to Delta format with:
    ```python
    spark.sql("CONVERT TO DELTA parquet.`<path-to-parquet>`")
    ```

## 2. Cluster Management

### 2.1 Cluster Creation and Configuration
- **Creating Clusters**:
  - Navigate to the "Clusters" tab and click "Create Cluster".
  - Configure cluster name, Databricks Runtime version, and worker/driver node types.
- **Auto-Scaling**:
  - Enable auto-scaling by setting the min and max number of worker nodes.

### 2.2 Cluster Policies
- **Defining Policies**:
  - Go to the "Admin Console" and select "Cluster Policies".
  - Create policies to enforce configurations like instance types, auto-scaling limits, and termination timeouts.

### 2.3 Resource Allocation and Optimization
- **Spot Instances**:
  - Enable spot instances to reduce costs, but be aware of potential interruptions.
- **Performance Monitoring**:
  - Use Ganglia metrics and the Spark UI to monitor cluster performance.

### 2.4 Monitoring and Alerts
- **Setting Up Alerts**:
  - In the Azure Portal, configure alerts based on metrics like CPU usage, memory usage, and error rates.

### 2.5 Security Management
- **VNet Integration**:
  - When creating a cluster, configure it to use a VNet for network isolation.
- **Encryption**:
  - Ensure that encryption is enabled for data at rest and in transit.

### 2.6 Cluster Lifecycle Management
- **Managing Clusters**:
  - Use job clusters for ephemeral workloads.
  - Regularly terminate idle clusters to save costs.

## 3. Job Scheduling

### 3.1 Job Creation and Configuration
- **Creating Jobs**:
  - Navigate to the "Jobs" tab and click "Create Job".
  - Define job tasks, specifying notebooks, JARs, or Python scripts to run.
- **Setting Dependencies**:
  - Add multiple tasks and define dependencies between them.

### 3.2 Scheduling and Triggers
- **Time-Based Scheduling**:
  - Set cron expressions for job schedules.
- **Event-Based Triggers**:
  - Use event-driven architectures to trigger jobs based on data availability.

### 3.3 Resource Management
- **Job Clusters**:
  - Configure jobs to use job clusters, which are created and terminated automatically with the job run.

### 3.4 Monitoring and Reporting
- **Job Monitoring**:
  - Use the "Runs" tab to monitor the status of job executions.
- **Failure Alerts**:
  - Configure notifications for job failures or successes.

### 3.5 Error Handling
- **Retries and Alerts**:
  - Set up automatic retries for job failures and configure alert notifications.
- **Logging**:
  - Enable detailed logging to troubleshoot job issues.

### 3.6 Optimization
- **Optimizing Job Performance**:
  - Regularly review job run times and resource usage.
  - Tune Spark configurations and optimize data formats for better performance.

## 4. Legacy Hive Metastore Integration

### 4.1 Configuring Hive Metastore
- **Set Up Hive Metastore**:
  - Ensure the Hive metastore is accessible from Azure Databricks.
  - Configure network settings and security groups to allow communication between Databricks clusters and the Hive metastore.

### 4.2 Connecting to Hive Metastore
- **Spark Configuration**:
  - When creating a cluster, go to the "Advanced Options" and under "Spark Config", add the following configurations:
    ```shell
    spark.sql.hive.metastore.jars <path-to-hive-metastore-jars>
    spark.sql.hive.metastore.version <hive-metastore-version>
    spark.hadoop.hive.metastore.uris thrift://<hive-metastore-host>:<port>
    ```
- **Testing the Connection**:
  - Verify the connection by running a simple query to list Hive tables:
    ```python
    spark.sql("SHOW TABLES").show()
    ```

### 4.3 Using Hive Metastore in Notebooks
- **Querying Hive Tables**:
  - Use Spark SQL or DataFrame API to query tables stored in the Hive metastore:
    ```python
    df = spark.sql("SELECT * FROM <database>.<table>")
    df.show()
    ```
- **Metadata Management**:
  - Manage table metadata and perform operations such as creating, altering, and dropping tables using Hive SQL commands.

### 4.4 Security and Compliance
- **Access Control**:
  - Implement access controls to secure the Hive metastore. Use Hive's authorization mechanisms or integrate with Ranger or Sentry for fine-grained access control.
- **Audit Logging**:
  - Enable audit logging in Hive to track metadata changes and access patterns.

## Conclusion

By following this operational guide, you can effectively manage your Azure Databricks environment, ensuring efficient workspace organization, robust cluster management, reliable job scheduling, and seamless integration with a legacy Hive metastore. Regular monitoring, security best practices, and optimization techniques will help you maintain a productive and cost-effective Databricks setup.
