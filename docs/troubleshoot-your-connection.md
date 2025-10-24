# Troubleshoot your connection

# Troubleshoot your connection

If you need to troubleshoot issues with your connection, such as missing tables or an inability to connect, follow the guidance on this page.

## Add Sigma IPs to the allowlist

In some cases, you might need to add Sigma's IP addresses to the allowlist to successfully connect to your data. This is a necessary step when your warehouse is closed to external connections due to firewalls, security groups, or other IP-based security policies.

Sigma lists its egress IP addresses on all individual **Connection** page. To see them, follow these steps:

1. Open the **Administration > Connections** page.
2. Select the relevant connection. 
   If you don't have a connection to the data source, click **Create Connection.**
3. In the Connection Credentials section, see the IPs listed under the **Host** field.

> 📘
>
> The IP addresses listed on the connections summary are not applicable to connections over Private Link. If you need the IP addresses for a Private Link connection, [contact Sigma Support](/docs/submit-a-support-request).

For more guidance specific to individual data platforms:

* **PostgreSQL**: Sigma must be authenticated either at the Network level, or through 
  [Client Authentication](https://www.postgresql.org/docs/8.2/auth-pg-hba-conf.html).
* **Redshift**: See [Amazon Redshift cluster security groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html).
* **Snowflake**: See [Network Policies](https://docs.snowflake.com/en/user-guide/network-policies).

## Permissions for the Snowflake user role

Sigma uses the Snowflake user role specified on the connection. Unless you have the correct privileges granted to the role in Snowflake, you cannot see the data in Sigma.

If the connection uses [OAuth](/docs/configure-oauth-with-snowflake), the connection inherits the permissions for each member of the organization directly from Snowflake. To troubleshoot permissions for an individual user or a service account user, confirm the following:

* The primary role granted to the user provides the relevant access in Snowflake.
* The user inherits the intended role through your OAuth provider.

## Syncing your data and connection indexing

Connection indexing is the process where Sigma scans your data warehouse to discover and catalog all available objects (databases, schemas, tables, views, stored procedures, etc.). This creates Sigma's internal catalog that powers the UI browsing experience and ensures users can find and access their objects.

Sigma automatically syncs your connection's metadata on a nightly basis to index various information from your data warehouse. These long-running overnight queries include:

* Catalog scans that enumerate tables, views, and schemas in your warehouse.
* Metadata queries to discover column names, data types, and table structures.
* Permission checks to determine what objects users can access.

Why they happen regularly:

* Data freshness - new tables, columns, or schema changes need to be discovered.
* Permission changes - user access to objects may have changed.
* Reliability - ensures Sigma's catalog stays in sync with your actual warehouse state.
* User experience - keeps the data browser up-to-date and responsive.

Sigma also automatically syncs your connections when a user accesses a schema that hasn't been checked recently, or when it detects that a catalog may be outdated and has stale data.

### Manually sync your data

When you make changes in your cloud data warehouse, such as updating the schema for a table or view, you must perform a manual sync so these changes are reflected in Sigma. Syncs can be performed at the connection, database, schema, or table level.

> 🚩
>
> Syncing only occurs at the level selected. To see changes at all levels, you must perform a manual sync at all levels.

You can perform a manual sync using the UI, or programmatically. For guidance on performing a manual sync using the Sigma REST API, see [Sync a connection by path](/reference/syncconnectionpath).

To perform the manual sync in the UI, follow these steps:

1. Navigate to **Administration > Connections**.
2. Select the relevant connection from the list.
3. Click **Browse connection**.
4. To sync the connection, which discovers updates to the databases available on that connection, click **Sync connection metadata** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/refresh.svg)) for the connection.
   ![](https://files.readme.io/6e4207a1be172fae03ec9164700145f0390ec759c52f92dec40622c8c6004f2e-sync-connection.png)
5. To sync an individual database or schema, locate the relevant database, and click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** next to the name of the database or schema. Alternatively, find the database or schema by searching for the name.

   From the drop-down menu, select **Sync now**.
   ![](https://files.readme.io/def7ca074d3294111ee40c06923a7d37abf66b395bac25031fffa32b56555485-sync-db.png)
6. To sync an individual table, expand the connection, find the database that contains the table, expand that database, find the table, and then click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** next to the name of the table. Alternatively, you can find the table by name by searching for it.

   From the drop-down menu, select **Sync now**.
   ![](https://files.readme.io/f82a7fe29dce4658620d32720f484b4800de06f2df957f84de5f645875b5717e-sync-table.png)

Sigma recommends that you manually sync your connections when:

* You added objects to your database or catalog that do not yet appear in Sigma, such as new tables or views.
* There are schema changes, like column additions, type changes, or renamed objects.
* User permissions and access have changed and the catalog needs refreshing.
* Expected objects like tables aren't showing up when browsing your connection in Sigma.
* Object counts or schemas are outdated.

Updated 1 day ago

---

[Azure Private Link Connections](/docs/azure-private-link-connections)[Troubleshoot input table connection issues](/docs/troubleshoot-input-table-connection-issues)

* [Table of Contents](#)
* + [Add Sigma IPs to the allowlist](#add-sigma-ips-to-the-allowlist)
  + [Permissions for the Snowflake user role](#permissions-for-the-snowflake-user-role)
  + [Syncing your data and connection indexing](#syncing-your-data-and-connection-indexing)
  + - [Manually sync your data](#manually-sync-your-data)