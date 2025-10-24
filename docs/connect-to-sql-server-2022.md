# Connect to SQL Server 2022 and Azure SQL Managed Instance

# Connect to SQL Server 2022 and Azure SQL Managed Instance

## Requirements

* Your SQL Server 2022 must be either: on a virtual machine, be publicly accessible via Internet, or be an [Azure SQL Managed Instance](https://azure.microsoft.com/en-us/products/azure-sql/managed-instance/). Other versions of SQL Server are not supported.
* You must be assigned the **Admin** [account type](/docs/user-account-types).
* You must have appropriate access in Azure to configure your database network settings.
* You must have a supported instance type. See [Verify my instance type](#verify-my-instance-type).

## Verify my instance type

To verify your instance type, run the following query on your database instance:

```
select serverproperty('ProductMajorVersion'),serverproperty('EngineEdition')
```

Instances with the following are supported:

* An `EngineEdition` of `1`, `2`, `3`, `4` and `ProductMajorVersion` of `16.x`
* An `EngineEdition` of `8`

If your `EngineEdition` is `5`, use the Azure SQL Database connection. See [Connect to Azure SQL Database](/docs/connect-to-azure-sql-database).

For information on interpreting the query output, see the Microsoft documentation on [SERVERPROPERTY](https://learn.microsoft.com/en-us/sql/t-sql/functions/serverproperty-transact-sql?view=sql-server-ver16).

## Create a SQL Server 2022 or Azure SQL Managed Instance connection

1. Click the user icon at the top right of your screen.
   The user icon is usually composed of your initials.
2. In the drop-down menu, select **Add connection**. The **Add new connection** page appears.
3. In the **Connection Details** section, specify the following:

   |  |  |
   | --- | --- |
   | **Name** | Enter a **Name** for the new connection. Sigma displays this name in the connection list. |
   | **Type** | Select **SQL Server**. |
4. You must configure your database network settings to allow Sigma IPs. To do this, refer to the Azure documentation on [Network Access Controls](https://learn.microsoft.com/en-us/azure/azure-sql/database/network-access-controls-overview?view=azuresql). The Sigma IPs can be found under the Server field in the Connection Credentials section.
5. In the **Connection Credentials** section, specify the following:

   |  |  |
   | --- | --- |
   | **Server** | A fully qualified hostname or IP address. Refer to the Microsoft documentation on [Connect to SQL Server](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/sql-vm-create-portal-quickstart?view=azuresql&tabs=conventional-vm#connect-to-sql-server). |
   | **Port** | The port through which Sigma can connect to your SQL Server. The default port is 1433. |
   | **User** | The username of the service account set up by your SQL Server administrator. |
   | **Password** | The password of the service account set up by your SQL Server administrator. |
6. In the **Connection Features** section, specify the following:

|  |  |
| --- | --- |
| **Connection Timeout** | The time before timeout (or cancellation), in seconds, that Sigma waits for the query to return results. The default is 120, or 2 minutes. The maximum is 600, or 10 minutes. |
| **Use friendly names** | This setting, which is on by default, makes column names from the data source more readable. For example, a database column ORDER\_NUMBER or OrderNumber appears as Order Number. |

7. Click **Browse Connection**, then click **Add permission** to grant data access for users in your organization.
8. Use the navigation in the left panel to explore the schemas and tables in your connection. The new connection will also appear in the list of connections you have in your account.

![](https://files.readme.io/c98c5ff04834a29fca916cd7b2f97d69392e38a7ab3fb0de743a4e509fc3d9cd-sqlserver.png)

## Configure write access

Write access is necessary for [materialization](/docs/materialization). Configuring write access requires setting up a dedicated database and schema and granting the necessary privileges. To configure write access:

1. Grant the SQL Server 2022/Azure SQL Managed Instance user that you use to configure the Sigma connection a role with the following privileges:

| Object | Privilege |
| --- | --- |
| Database | `CREATE TABLE` |
| Schema | `CREATE TABLE`, `CREATE VIEW`, `ALTER` |

2. In Sigma, go to **Connections**. Select your SQL Server 2022/Azure SQL Managed Instance connection, then select **Edit**.
3. Turn on the **Enable write access** toggle, then configure the following fields:
   * In the **Write database** field, enter the name of the database where Sigma should store write-back data.
   * In the **Write schema** field, enter the database schema where Sigma should store write-back data.

## Feature Limitations

Currently, SQL Server 2022/Azure SQL Managed Instance connections *don’t* support the following features:

* Dataset warehouse views created in Sigma
* Export to cloud storage
* OAuth connections
* Sigma result IDs cache
* User attributes for role and warehouse switching
* Write-back features: CSV uploads, Input tables, running Python code
* Geography data type
* All Geography functions
* The following Passthrough functions (including Call and Agg variations): Geography, Variant, Logical
* The following Window functions: CumulativeCorr, MovingCorr, Median, Corr, Nth
* The following Date functions: DateParse, LastDay
* The following Array functions: Array, ArrayTransform, ArrayFilter, SplitToArray
* The following Aggregate functions: ListAggDistinct, RegressionIntercept, RegressionR2, RegressionSlope
* The following Text functions: RegexpMatch, RegexpReplace, RegexpExtract, MD5, SHA256, SplitPart, Proper
* The following Math functions: BinFixed
* Regex text matching in filters
* Custom SQL containing CTE's
* Sample connections

Updated 3 days ago

---

[Connect to Azure SQL Database](/docs/connect-to-azure-sql-database)[Manage connections](/docs/connections)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Verify my instance type](#verify-my-instance-type)
  + [Create a SQL Server 2022 or Azure SQL Managed Instance connection](#create-a-sql-server-2022-or-azure-sql-managed-instance-connection)
  + [Configure write access](#configure-write-access)
  + [Feature Limitations](#feature-limitations)