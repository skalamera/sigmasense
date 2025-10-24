# Connect to Starburst

# Connect to Starburst

Sigma supports using Starburst Galaxy, a SaaS distribution of Trino, to connect to a Snowflake, Databricks, BigQuery, or PostgreSQL data warehouse.

This document explains how to connect your Sigma organization to your [Starburst Galaxy](https://docs.starburst.io/introduction/choose-your-starburst-product.html#starburst-galaxy) cluster.

> 📘
>
> ### For information about Sigma feature compatibility with Starburst connections, see [Region, warehouse, and feature support](/docs/region-warehouse-and-feature-support).

## Requirements

* You must be assigned the **Admin** [account type](/docs/user-account-types).
* You need the credentials for a Starburst Galaxy service account with `Select from table` privilege for all tables that Sigma needs to access and the `Use cluster` privilege on the cluster.

## Create a Starburst connection

1. Click the user icon at the top right of your screen. The user icon is usually composed of your initials.
2. In the drop-down menu, select **Add connection**.
3. The **Add new connection** page appears.
4. In the **Connection details**, specify the following:

   |  |  |
   | --- | --- |
   | **Name** | Enter a **Name** for the new connection. Sigma displays this name in the connection list. |
   | **Type** | Select **Starburst**. |
5. In the **Connection Credentials** section, complete the fields:

|  |  |
| --- | --- |
| **Host** | The address of your Starburst Galaxy cluster as a URL or an IP address. |
| **Port** | The port through which Sigma can connect to your Starburst Galaxy cluster. |
| **User** | The username of the service account set up by your Starburst administrator. |
| **Password** | The password for the service account set up by your Starburst administrator. |

6. (Optional) In the **Connection features** section, adjust the defaults if needed.

   |  |  |
   | --- | --- |
   | **Connection timeout** | The time before timeout (or cancellation), in seconds, that Sigma waits for the query to return results. The default is 120, or 2 minutes. The maximum is 600, or 10 minutes. |
   | **Use friendly names** | This setting, which is on by default, makes column names from the data source more readable. For example, a database column ORDER\_NUMBER appears as Order Number. |
7. After you specify all the parameters of the connection, click **Create**. Sigma displays a connection summary on the screen.

![The connection summary showing the newly created Starburst connection](https://files.readme.io/d0d5a22-connectionsummary.png)

8. Click **Browse Connection**, then click **Add permission** to grant data access for users in your organization.

![The Permission summary on the connection, showing that no users have access to this connection yet](https://files.readme.io/452f1a2-Addpermissions.png)

9. Use the navigation in the left panel to explore the databases and tables in your connection.

![The browse connection view, showing a table available through the connection](https://files.readme.io/5493f7d-exploreconnection.png)

10. The new connection also appears in the list of connections you have in your account.

Updated 3 days ago

---

[Connect to PostgreSQL](/docs/connect-to-postgresql)[Azure SQL Database](/docs/azure-sql-database)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Create a Starburst connection](#create-a-starburst-connection)