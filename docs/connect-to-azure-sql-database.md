# Connect to Azure SQL Database

# Connect to Azure SQL Database

Sigma supports secure connections to Azure SQL Database, a fully managed platform as a service (PaaS) database engine.

This document explains how to connect your Sigma organization to your [Azure SQL Database](https://azure.microsoft.com/en-us/products/azure-sql/database).

## Requirements

* You must be assigned the **Admin** [account type](/docs/user-account-types).
* You must have appropriate access in Azure to configure your database network settings.
* Your database must be a supported instance type. For more information, see [Verify your database instance type](#verify-your-database-instance-type). *This is the only method of confirming whether or not Sigma can connect to your database.*

## Verify your database instance type

Run the following query to verify your database instance type and confirm support:

```
select serverproperty('ProductMajorVersion'),serverproperty('EngineEdition')
```

Sigma supports connections to instances with an `EngineEdition` of `5`.

If the `EngineEdition` is not `5` but it meets one of the following criteria, you must use the [SQL Server 2022 connection](/docs/connect-to-sql-server-2022):

* `EngineEdition` is `1`, `2`, `3`, `4` *and* `ProductMajorVersion` is `16.x`
* `EngineEdition` is `8`

For information about interpreting the query output, see the Microsoft documentation on [SERVERPROPERTY](https://learn.microsoft.com/en-us/sql/t-sql/functions/serverproperty-transact-sql?view=sql-server-ver16).

## Create an Azure SQL Database connection

1. Click the user icon at the top right of your screen.
   The user icon is usually composed of your initials.
2. In the drop-down menu, select **Add connection**. The **Add new connection** page appears.
3. In the **Connection Details** section, specify the following:

   |  |  |
   | --- | --- |
   | **Name** | Enter a **Name** for the new connection. Sigma displays this name in the connection list. |
   | **Type** | Select **Azure SQL DB**. |
4. You must configure your Azure database network settings to allow Sigma IP addresses. To do this, refer to the Azure documentation on [Network Access Controls](https://learn.microsoft.com/en-us/azure/azure-sql/database/network-access-controls-overview?view=azuresql). The necessary Sigma IPs can be found under the **Server** field in the **Connection Credentials** section.
5. In the **Connection Credentials** section, specify the following:

   |  |  |
   | --- | --- |
   | **Server** | A fully qualified hostname or IP address. Refer to the Microsoft documentation on how to [Get server connection information](https://learn.microsoft.com/en-us/azure/azure-sql/database/connect-query-content-reference-guide?view=azuresql#get-server-connection-information/) |
   | **Database** | The name of the database you want to query. |
   | **Port** | The port through which Sigma can connect to your Azure SQL Database cluster. The default port is 1433. |
   | **User** | The username of the service account set up by your Azure SQL Database administrator. |
   | **Password** | The password of the service account set up by your Azure SQL Database administrator. |
6. In the **Connection Features** section, specify the following:

   |  |  |
   | --- | --- |
   | **Connection Timeout** | The time before timeout (or cancellation), in seconds, that Sigma waits for the query to return results.  The default is 120, or 2 minutes.  The maximum is 600, or 10 minutes. |
   | **Use friendly names** | This setting, which is on by default, makes column names from the data source more readable.  For example, a database column ORDER\_NUMBER or OrderNumber appears as Order Number. |
7. Click **Browse Connection**, then click **Add permission** to grant data access for users in your organization.

![](https://files.readme.io/ac37e8ccb166eb967cdf44116ebcd3dc0889558b0e8197cb7f212ec930490c20-add_permissions_azure_SQL.png)

8. Use the navigation in the left panel to explore the schemas and tables in your connection. The new connection will also appear in the list of connections you have in your account.

![](https://files.readme.io/364e0a03c67526eff757f6341665cc849508ec6038fb2ab3c8038100f7b20f1d-sampleschematable.png)

## Configure write access

Write access is necessary for [materialization](/docs/materialization). Configuring write access requires setting up a dedicated database and schema and granting the necessary privileges. To configure write access:

1. Grant the Azure SQL Database user that you use to configure the Sigma connection a role with the following privileges:

| Object | Privilege |
| --- | --- |
| Schema | `CREATE TABLE`, `CREATE VIEW`, `ALTER` |

2. In Sigma, go to **Connections**, select your Azure SQL Database connection, then select **Edit**.
3. Turn on the **Enable write access** toggle, then configure the following:
   * In the **Write schema** field, enter the database schema where Sigma should store write-back data.

## Feature Limitations

Currently, Azure SQL Database connections *don’t* support the following features:

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

Updated 2 days ago

---

[Connect to Starburst](/docs/connect-to-starburst)[SQL Server 2022 and Azure SQL Managed Instance](/docs/sql-server)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Verify your database instance type](#verify-your-database-instance-type)
  + [Create an Azure SQL Database connection](#create-an-azure-sql-database-connection)
  + [Configure write access](#configure-write-access)
  + [Feature Limitations](#feature-limitations)