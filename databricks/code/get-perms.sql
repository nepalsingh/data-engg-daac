SELECT
    principal_name,
    object_type,
    object_name,
    privilege_type
FROM
    information_schema.object_privileges;

SHOW ROLES;
SHOW GRANT ROLE admin;
SHOW GRANT USER nsingh;
SELECT
    principal_name,
    object_type,
    object_name,
    privilege_type
FROM
    information_schema.object_privileges;
