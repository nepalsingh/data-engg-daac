# Databricks Unity Catalog

## Topology: multi-region / multi-cloud UC
Powered by Delta Sharing
- Metastore boundary = region / cloud (due to latency, cost)
- Use single region Metastore for all SDLC scopes and business units
- Use Databricks-to-Databricks Delta Sharing between cloud regions and cloud providers

## Capability Chart
![Capability Chart](./images/capability-chart.png)


![Apache-ranger](./images/image.png)

## Unity-enabled jobs
- Use SINGLE USER policy for JOB CLUSTERS
- Set a SERVICE PRINCIPAL as the OWNER of prod jobs and RUN as that SP NOTE: Workspace Admins can change job ownership and by extension access data that service principals of the workspace can access
- Limit Workspace Admin role to required Dev Ops or IT Ops groups only
- Use a dedicated service principal for each job
- Use a dedicated job cluster for each job

## Catalog / schema / table setup
The catalog level of the
- 3-level namespace allows to structure databases
- Tables / views according to technical or business needs.

```mermaid

flowchart LR
    Header["Unity Metastore"]
    dev["dev"]
    test["test"]
    prod["prod"]
    bu_dev["bu_dev"]
    bu_test["bu_test"]
    bu_prod["bu_prod"]
    team_finance["team_finance"]
    team_hr["team_hr"]
    Schema_Dev["`Schema
                 Database`"]
    Schema_Test["`Schema
                 Database`"]
    Schema_Prod["`Schema
                  Database`"]
    Schema_Bu_Dev["`Schema
                    Database`"]
    Schema_Bu_Test["`Schema
                     Database`"]
    Schema_Bu_Prod["`Schema
                     Database`"]
    Schema_Team_Finance["`Schema
                         Database`"]
    Schema_Team_HR["`Schema
                     Database`"]
    table_dev["`Tables/
                Views`"]
    table_test["`Tables/
                 Views`"]
    table_prod["`Tables/
                  Views`"]
    table_bu_dev["`Tables/
                   Views`"]
    table_bu_test["`Tables/
                    Views`"]
    table_bu_prod["`Tables/
                    Views`"]
    table_team_finance["`Tables/
                        Views`"]
    table_team_hr["`Tables/
                    Views`"]

    SDLC["`Across SDLC
           evnironments scopes`"]
    BU["`Across Business Units
         scopes`"]
    Sandbox["`Across Teams
              Sandbox`"]
    Header --> dev
    Header --> test
    Header --> prod
    dev --> Schema_Dev
    test --> Schema_Test
    prod --> Schema_Prod
    Schema_Dev --> table_dev
    Schema_Test --> table_test
    Schema_Prod --> table_prod


    Header --> bu_dev
    Header --> bu_test
    Header --> bu_prod
    bu_dev --> Schema_Bu_Dev
    bu_test --> Schema_Bu_Test
    bu_prod --> Schema_Bu_Prod
    Schema_Bu_Dev --> table_bu_dev
    Schema_Bu_Test --> table_bu_test
    Schema_Bu_Prod --> table_bu_prod


    Header --> team_finance
    Header --> team_hr
    team_finance --> Schema_Team_Finance
    team_hr --> Schema_Team_HR
    Schema_Team_Finance --> table_team_finance
    Schema_Team_HR --> table_team_hr

    table_dev --> SDLC
    table_test --> SDLC
    table_prod --> SDLC
    table_bu_dev --> BU
    table_bu_test --> BU
    table_bu_prod --> BU
    table_team_finance --> Sandbox
    table_team_hr --> Sandbox

```


