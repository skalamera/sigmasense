# Set up write access

# Set up write access

Set up write access to enable the use of features like [input tables](/docs/create-and-manage-input-tables), [warehouse views](/docs/create-and-manage-workbook-warehouse-views), [materialization](/docs/materialization), and [CSV upload](/docs/upload-csv-data).

> 📘
>
> ### If your organization uses OAuth to authenticate your connection, there are additional configuration steps. See [Configure OAuth with write access](/docs/configure-oauth-with-write-access).

## System and user requirements

* You must be assigned the **Admin** [account type](/docs/user-account-types).
* You must have the necessary permissions in your cloud data warehouse (CDW) to create a write access destination and configure permissions.

## Set up destinations and permissions for write access in your data platform

To set up write access, ensure that Sigma has sufficient permissions in your data platform.

Each CDW has a unique database structure and permissions model. Follow the documentation for your CDW to create a destination that Sigma can use to write data back to, and apply the necessary permissions to allow Sigma to perform write back using the authentication you have configured.

> 💡
>
> ### By design, the destination that you configure for write access is not visible in the Sigma connection explorer pane. The data that Sigma writes to this destination is not formatted in a way that can be browsed and used. Configure a separate database or a database and schema combination for write-access purposes.

## Configure write access in Sigma

1. Select **Administration** in the user menu at the top right of your screen.
2. Select the **Connections** page from the left panel.
3. To view the connection, click on an existing connection in the list.
4. Click **Edit**.
5. Under **Write access**, switch on **Enable write access**.
6. Sigma requests additional information for write access; this information depends on the specifics of your CDW: [Snowflake](/docs/connect-to-snowflake#configure-write-access), [BigQuery](/docs/connect-to-bigquery), [PostgreSQL](/docs/connect-to-postgresql), [Redshift](/docs/connect-to-redshift), [Databricks](/docs/connect-to-databricks#configure-write-access), [AlloyDB](/docs/connect-to-alloydb), and [MySQL](/docs/connect-to-mysql).
7. After completing the form, click **Save**.

Updated 3 days ago

---

[Connect to SQL Server 2022 and Azure SQL Managed Instance](/docs/connect-to-sql-server-2022)[Configure OAuth with write access](/docs/configure-oauth-with-write-access)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Set up destinations and permissions for write access in your data platform](#set-up-destinations-and-permissions-for-write-access-in-your-data-platform)
  + [Configure write access in Sigma](#configure-write-access-in-sigma)