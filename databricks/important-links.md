# Documentation for databricks legacy permissions

## Databricks Legacy Permissions

Databricks provides a set of legacy permissions that can be used to control access to various resources within the platform. These permissions are based on the legacy access control model and are being replaced by the new Role-Based Access Control (RBAC) model. However, legacy permissions are still supported for backward compatibility.

[Hive metastore privileges and securable objects (legacy)](https://learn.microsoft.com/en-us/azure/databricks/data-governance/table-acls/object-privileges)

### Privileges you can grant on Hive metastore objects
- SELECT: gives read access to an object.
- CREATE: gives ability to create an object (for example, a table in a schema).
- MODIFY: gives ability to add, delete, and modify data to or from an object.
- USAGE: does not give any abilities, but is an additional requirement to perform any action on a schema object.
- READ_METADATA: gives ability to view an object and its metadata.
- CREATE_NAMED_FUNCTION: gives ability to create a named UDF in an existing catalog or schema.
- MODIFY_CLASSPATH: gives ability to add files to the Spark class path.
- ALL PRIVILEGES: gives all privileges (is translated into all the above privileges).

