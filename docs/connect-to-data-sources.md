# Connect to data sources

# Connect to data sources

A data source connection enables Sigma to communicate with your data warehouse. An open and available connection is necessary for Sigma to send commands and receive answers in the form of data result sets.

To connect to a data source, every application (including Sigma) must provide a connection string that consists of the address or location of the data, appropriate user validations (user id and password), specific database configuration options, security options, and many more. Data source connections are expensive to create, relative to the time of operations that you can subsequently perform on them. Therefore, we open a connection and keep it active to perform a series of discrete operations. We manage the "closing" and refreshing of the connections regularly, so when you work with Sigma the next day, you can continue with your work and use the same connection, seamlessly.

While connections are a very powerful tool, consider carefully before creating multiple connections to the same database entity. Because you cannot move data across connections, you cannot perform cross-table calculations. For example, if you access Table1 from Connection1 and Table2 from Connection2, you cannot look at these tables as a collective entity, even if they are in the same database.

## Requirements

* Admin privileges in your Sigma organization.
  For more information, see [User account types](/docs/user-account-types).
* A data warehouse that Sigma supports.
  These include [Snowflake](/docs/connect-to-snowflake), [BigQuery](/docs/connect-to-bigquery), [Redshift](/docs/connect-to-redshift), [Databricks](/docs/connect-to-databricks), [PostgreSQL](/docs/connect-to-postgresql), [AlloyDB](/docs/connect-to-alloydb), and [MySQL](/docs/connect-to-mysql) .

## Create a connection to the data warehouse

Each warehouse type takes different input parameters. Use the following instructions for your connection method:

* [Connect to AlloyDB](/docs/connect-to-alloydb)
* [Connect to Azure SQL Database](/docs/connect-to-azure-sql-database)
* [Connect to BigQuery](/docs/connect-to-bigquery)
* [Connect to Databricks](/docs/connect-to-databricks)
* [Connect to MySQL](/docs/connect-to-mysql)
* [Connect to PostgreSQL](/docs/connect-to-postgresql)
* [Connect to Redshift](/docs/connect-to-redshift)
* [Connect to Snowflake](/docs/connect-to-snowflake)
* [Connect to Starburst](/docs/connect-to-starburst)
* [Connect to SQL Server 2022 and Azure SQL Managed Instance](/docs/connect-to-sql-server-2022)

## Add Sigma IPs to the allowlist

When your warehouse is closed to external connections because of firewalls, security groups, or other IP-based security policies, you have to add Sigma's IP addresses to the allowlist, so you can successfully connect to your data.

Sigma's egress IP addresses are listed on all individual connection pages in your Sigma Administration portal.

To view them:

1. Open your Administration portal, then click **Connections** in the left navigation.
2. Select any connection or click **Create Connection**.
3. Look for the IP addresses listed under connection credentials.
   ![](https://files.readme.io/5fadef2fcabd4138883618c1e3a1646dc64b96361b7ccc1d3d437aba240e3d42-connection-credentials-IPs.png)

> 📘
>
> The IP addresses listed on the connections summary are not applicable to connections over Private Link. If you need the IP addresses for a Private Link connection, [contact Sigma Support](/docs/submit-a-support-request).

## Write access

You can [enable write access](/docs/set-up-write-access) on your connection. Write access is required for [materialization](/docs/materialization), [CSV uploads](/docs/upload-csvs), [input tables](/docs/intro-to-input-tables), and [warehouse views](/docs/create-and-manage-workbook-warehouse-views).

## Permissions

After creating a connection, you can selectively share access with other people in your organization. For more information, see [Data Permissions](/docs/data-permissions-overview).

## Query timeouts

By default, Sigma sets query timeouts to 120 seconds (2 minutes). When queries hit the timeout limit, Sigma will cancel the query. Under **Connection Features**, you can set a custom query timeout for your connection.

Updated 3 days ago

---

Related resources

* [Connect to AlloyDB](/docs/connect-to-alloydb)
* [Connect to BigQuery](/docs/connect-to-bigquery)
* [Connect to Databricks](/docs/connect-to-databricks)
* [Connect to MySQL](/docs/connect-to-mysql)
* [Connect to PostgreSQL](/docs/connect-to-postgresql)
* [Connect to Redshift](/docs/connect-to-redshift)
* [Connect to Snowflake](/docs/connect-to-snowflake)
* [Connect to Starburst](/docs/connect-to-starburst)
* [Connect to Azure SQL Database](/docs/connect-to-azure-sql-database)
* [Connect to SQL Server 2022 and Azure SQL Managed Instance](/docs/connect-to-sql-server-2022)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Create a connection to the data warehouse](#create-a-connection-to-the-data-warehouse)
  + [Add Sigma IPs to the allowlist](#add-sigma-ips-to-the-allowlist)
  + [Write access](#write-access)
  + [Permissions](#permissions)
  + [Query timeouts](#query-timeouts)