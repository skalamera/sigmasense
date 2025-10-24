# Connect to MySQL

# Connect to MySQL

Sigma supports secure connections to MySQL (release 8.x and higher). MariaDB and other variants are not supported at this time.

This document explains how to connect your organization to a MySQL database.

> 📘
>
> For information about Sigma feature compatibility with MySQL connections, see [Region, warehouse, and feature support](/docs/region-warehouse-and-feature-support).

**Customers**

Request access to this feature through your Account Representative.

**Prospects**

Request access to this feature through our [Sales team](https://www.sigmacomputing.com/request-a-demo).

## Requirements

* Admin privileges in your Sigma organization. For more information, see [User account types](/docs/user-account-types).
* A MySQL account with READ privileges for the relevant databases and tables. If you are planning to upload CSV data, the account must have WRITE privileges.
* Sigma supports MySQL version 8.0 and higher.
* We recommend that you avoid granting excessive permissions to the account you use when connecting to your data store; for example, you do not require SYSADMIN-level access.
* MySQL on Azure does not have named timezones by default, so you must load the timezone data into your MySQL database for Sigma to operate properly. Otherwise, you may have an error when setting up a connection. See Microsoft documentation on [Populating the time zone tables](https://learn.microsoft.com/en-us/azure/mysql/single-server/how-to-server-parameters#populating-the-time-zone-tables). This is not an issue for MySQL on AWS or GCP.

## Create a connection

Follow these basic steps to create a connection:

1. Click the user icon at the top right of your screen.
   The user icon is usually composed of your initials.
2. In the drop-down menu, select **Add connection**.
3. The **Add new connections** page appears.
4. In the **Connection details**, specify the following:

   |  |  |
   | --- | --- |
   | **Name** | Enter a **Name** for the new connection. Sigma displays this name in the connection list. |
   | **Type** | Select **MySQL**. |
5. In the **Connection Credentials** section, specify the following:

Host
:   The path to your database.
:   This can be a URL, or an IP address.

Port
:   The port that Sigma uses to connect to the host.
:   The default port for MySQL is `3306`

User
:   The username, or account, for connecting to the MySQL data warehouse.
:   For example, `test`.

Password
:   Enter the password that corresponds to the **User** on the MySQL account.

Database
:   The name of the database you plan to query.

Enable TLS
:   Optional.
:   This switch enables or disables TLS encryption on your connection.
:   Enabled by default.

SSH Tunnel
:   Optional.
:   This switch enables the SSH protocol for secure remote login. For details, see [Connect through SSH](https://help.sigmacomputing.com/docs/connect-through-ssh).
:   Disabled by default.
:   If on, specify the **Tunnel host** and **Tunnel port** fields.

Tunnel host
:   The path to the tunnel server.
:   This can be a URL, or an IP address.
:   Appears only if **SSH Tunnel** is on.

Tunnel port
:   The port where the tunnel connects.
:   Appears only if **SSH Tunnel** is on.

6. In the **Connection Features** section, specify the following:

   Connection timeout
   :   The time before timeout (or cancellation), in seconds, that Sigma waits for the query to return results.
   :   Default is 120, or 2 minutes.
   :   Maximum is 600, or 10 minutes.

   Use friendly names
   :   This toggle makes column names from the data source more readable.
   :   For example, a database column ORDER\_NUMBER or OrderNumber appears as Order Number.
   :   On by default.
7. In the **Write Access** section, decide if you require write access. See [Set up write access](/docs/set-up-write-access).

   Enable write access
   :   Necessary for [CSV upload](https://help.sigmacomputing.com/docs/upload-csvs) and [Materialization](https://help.sigmacomputing.com/docs/materialization).
   :   Off by default.
   :   If on, specify the **Write schema** field.

   Write schema
   :   The schema where Sigma writes tables.
   :   Appears only if **Enable write access** is on.
8. After you specify all the parameters of the connection, click **Create.**

   After you successfully create your connection, Sigma displays it on the screen.
9. To verify your connection, click **Browse Connection**, and then explore the visible databases and tables.
10. Click **Add Permission** to grant data access for users in your organization.
    See [Data permissions](/docs/data-permissions-overview).
11. The new connection also appears in the list of connections you have in your account.

Updated 3 days ago

---

Related resources

* [Connect to data sources](/docs/connect-to-data-sources)
* [Connect through SSH](/docs/connect-through-ssh)
* [Set up write access](/docs/set-up-write-access)
* [Data permissions](/docs/data-permissions)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Create a connection](#create-a-connection)