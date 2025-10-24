# Connect to PostgreSQL

# Connect to PostgreSQL

Sigma supports secure connections to PostgreSQL.

This document explains how to connect your organization to a PostgreSQL database.

> 📘
>
> For information about Sigma feature compatibility with PostgreSQL connections, see [Region, warehouse, and feature support](/docs/region-warehouse-and-feature-support).

## Requirements

* Admin privileges in your Sigma organization; see [Account types](/docs/user-account-types).
* A PostgreSQL data warehouse
* Sigma recommends not granting excessive permissions to the account used to connect to your data store; for example, you do not require SYSADMIN-level access.

## Create a PostgreSQL connection

Follow these basic steps to create a connection:

1. Click the user icon at the top right of your screen.
   The user icon is usually composed of your initials.
2. In the drop-down menu, select **Add connection**.
3. The **Add new connections** page appears.
4. In the **Connection details**, specify the following:

**Name**
:   Enter a **Name** for the new connection. Sigma displays this name in the connection list.

**Type**
:   Select **PostgreSQL**.

5. In the **Connection Credentials** section, specify the following fields.

Host
:   The path to your database.
:   This can be a URL or an IP address depending on the configuration of your PostgreSQL instance.

Port
:   The port that Sigma uses to connect to the host.
:   The default port for PostgreSQL is `5432`

User
:   The username, or account, for connecting to the PostgreSQL data warehouse.
:   See [Create a user with the necessary data permissions](https://help.sigmacomputing.com/docs/connect-to-postgresql#create-a-user-with-the-necessary-data-permissions) for more information.

Password
:   Enter the password that corresponds to the **User** on the PostgreSQL account.

Database
:   The name of the database you plan to query.

Enable TLS
:   (Optional) Enable or disable TLS encryption on your connection.
:   Enabled by default.

SSH Tunnel
:   (Optional) This switch enables the SSH protocol for secure remote login. For details, see [Connect through SSH](https://help.sigmacomputing.com/docs/connect-through-ssh).
:   Disabled by default.
:   If on, specify the **Tunnel host** and **Tunnel port** fields.

Tunnel host
:   The path to the tunnel server. This can be a URL or IP address. Appears only if **SSH Tunnel** is on.

Tunnel port
:   The port where the tunnel connects. Appears only if **SSH Tunnel** is on.

6. In the **Connection Features** section, specify the following:

Connection timeout
:   The time before timeout (or cancellation), in seconds, that Sigma waits for the query to return results.
:   Default is 120, or 2 minutes.
:   Maximum is 600, or 10 minutes.

Use friendly names
:   This toggle makes column names from the data source more readable.
:   For example, a database column ORDER\_NUMBER or OrderNumber appears as Order Number.
:   On by default.

7. In the **Write Access** section, decide if you require write access.
   See [Set up write access](/docs/set-up-write-access).

Enable write access
:   Off by default. Necessary for features like [Input tables](https://help.sigmacomputing.com/docs/intro-to-input-tables) and [Materialization](https://help.sigmacomputing.com/docs/materialization).
:   If on, specify the **Write schema** field.

Write schema
:   The schema where Sigma writes tables. Appears only if **Enable write access** is on.

8. After you specify all the parameters of the connection, click **Create**.
9. After you successfully create your connection, Sigma displays it on the screen.
10. To verify your connection, click **Browse Connection**, and then explore the visible databases and tables.
11. Click **Add Permission** to grant data access for users in your organization.
    See [Data access overview](/docs/data-permissions-overview).
12. The new connection also appears in the list of connections you have in your account.

## Create a user with the necessary data permissions

When configuring your PostgreSQL connection, you can use an existing PostgreSQL user or create a new user.

If you don’t want to use an existing PostgreSQL user, create a new user for Sigma. If you want to leverage write access, create a schema for Sigma and grant all privileges to your user on that schema. Be sure to GRANT USAGE on all schemas, and GRANT SELECT on all tables that you plan to access in Sigma.

SQL

```
create user sigma_user password '123';
create schema sigma_write;
grant all privileges on schema sigma_write to sigma_user;
grant usage on schema public to sigma_user;
grant select on all tables in schema public to sigma_user;
```

> 💡
>
> Sigma recommends using a strong username and password for your PostgreSQL user. The sample credentials shown above are for demonstration only.

Updated 3 days ago

---

Related resources

* [Connect through SSH](/docs/connect-through-ssh)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Create a PostgreSQL connection](#create-a-postgresql-connection)
  + [Create a user with the necessary data permissions](#create-a-user-with-the-necessary-data-permissions)