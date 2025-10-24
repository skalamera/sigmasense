# Connect to AlloyDB

# Connect to AlloyDB

Sigma supports secure connections to AlloyDB.

This document explains how to connect your organization to a AlloyDB database.

> 📘
>
> ### For information about Sigma feature compatibility with AlloyDB connections, see [Region, warehouse, and feature support](/docs/region-warehouse-and-feature-support).

## Requirements

* Admin privileges in your Sigma organization.  
  For more information, see [User account types](/docs/user-account-types).
* An AlloyDB data warehouse, and an account there.
* We recommend that you avoid granting excessive permissions to the account you use when connecting to your data store; for example, you do not require SYSADMIN-level access.

## Create an AlloyDB Connection

> 📘
>
> ### If your AlloyDB instance is on a VPC, you must take additional steps. For more information, see [Configure VPC Service Controls](https://cloud.google.com/alloydb/docs/vpc-sc/configure-vpc-service-controls).

Follow these steps to create a connection:

1. Click the user icon at the top right of your screen.  
   The user icon is usually composed of your initials.
2. In the drop-down menu, select **Add connection**.
3. The **Add new connections** page appears.
4. In the **Connection details**, specify the following:

   |  |  |
   | --- | --- |
   | **Name** | Enter a **Name** for the new connection. Sigma displays this name in the connection list. |
   | **Type** | Select **AlloyDB**. |
5. In the **Connection Credentials** section, specify the following:

Host
:   The path to your database. This can be a URL, or an IP address.
:   Enter your cluster's Endpoint URL. Sigma connects from IPs 104.197.169.18, and 104.197.193.23.

Port
:   The port that Sigma uses to connect to the host.

User
:   The username, or account, for connecting to AlloyDB.
:   For example, `test`.

Password
:   Enter the password that corresponds to the **User** on the AlloyDB account.

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

1. In the **Connection Features** section, specify the following:

   Connection timeout
   :   The time before timeout (or cancellation), in seconds, that Sigma waits for the query to return results.
   :   Default is 120, or 2 minutes.
   :   Maximum is 600, or 10 minutes.

   Use friendly names
   :   This toggle makes column names from the data source more readable.
   :   For example, a database column ORDER\_NUMBER or OrderNumber appears as Order Number.
   :   On by default.
2. In the **Write Access** section, decide if you require write access.  
   See [Set up write access](/docs/set-up-write-access).

   Enable write access
   :   Necessary for [CSV upload](https://help.sigmacomputing.com/docs/upload-csvs) and [Materialization](https://help.sigmacomputing.com/docs/materialization).
   :   Off by default.
   :   If on, specify the **Write schema** field.

   Write schema
   :   The schema where Sigma writes tables.
   :   Appears only if **Enable write access** is on.
3. After you specify all the parameters of the connection, click **Create.**
4. After you successfully create your connection, Sigma displays it on the screen.
5. To verify your connection, click **Browse Connection**, and then explore the visible databases and tables.
6. Click **Add Permission** to grant data access for users in your organization.  
   See [Data permissions](/docs/data-permissions).
7. The new connection also appears in the list of connections you have in your account.

## Locate your AlloyDB cluster credentials

1. In the Google Cloud console, navigate to the **Clusters** page.
2. Click the cluster that you plan to connect to Sigma.
3. A cluster page appears.  
   It lists the required credentials for connecting to Sigma.

Updated 3 days ago

---

Related resources

* [Connect to data sources](/docs/connect-to-data-sources)
* [Connect through SSH](/docs/connect-through-ssh)
* [Set up write access](/docs/set-up-write-access)
* [Data permissions](/docs/data-permissions)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Create an AlloyDB Connection](#create-an-alloydb-connection)
  + [Locate your AlloyDB cluster credentials](#locate-your-alloydb-cluster-credentials)