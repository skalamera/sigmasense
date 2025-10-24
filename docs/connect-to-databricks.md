# Connect to Databricks

# Connect to Databricks

Sigma supports secure connections to Databricks.

This document explains how to connect your organization to a Databricks warehouse.

> 📘
>
> ### For information about Sigma feature compatibility with Databricks connections, see [Region, warehouse, and feature support](/docs/region-warehouse-and-feature-support).

## Requirements

In your Sigma organization:

* You must be assigned the **Admin** [account type](/docs/user-account-types).

In Databricks:

* You must have access to a Databricks workspace with Databricks SQL access enabled. See [Manage entitlements](https://docs.databricks.com/en/security/auth/entitlements.html) in the Databricks documentation.
* You must have access to a Databricks SQL warehouse or have the ability to create one by either being an Admin or having the `Allow unrestricted cluster creation` user entitlement. See [Requirements](https://docs.databricks.com/en/compute/sql-warehouse/create.html#requirements) in the Databricks documentation.
* You must be able to either use your own personal access token (PAT) or one attached to a user or service principal who has permissions. See [Monitor and manage access to personal access tokens](https://docs.databricks.com/en/admin/access-control/tokens.html#monitor-and-manage-personal-access-tokens) in the Databricks documentation.

## Configure Databricks

Complete the following steps in Databricks before you add a Databricks connection to Sigma.

1. Create a Databricks SQL warehouse if one doesn't already exist. See [Create a SQL warehouse](https://docs.databricks.com/en/compute/sql-warehouse/create.html) in the Databricks documentation.
2. Confirm that the user or service principal you will use to connect to this SQL warehouse has `Can use` or `Can manage` permissions for the compute resource, and that all workspace users have `Can use` permissions.
3. Configure your **Auto stop** setting. For information on this setting, see [Configure SQL warehouse settings](https://docs.databricks.com/en/compute/sql-warehouse/create.html#configure-sql-warehouse-settings) in the Databricks documentation.

   * If you are running a Serverless SQL warehouse, Sigma recommends that you enable **Auto stop** and setting it to 10 or 15 minutes.
   * If you are running a Pro or Classic SQL warehouse, disable **Auto stop** on your Databricks endpoint so that your first query does not time out or run slowly when the SQL endpoint is in a suspended state.
4. Configure data access to the SQL warehouse. In order to query data using the Databricks SQL warehouse, the user, group, or service principal that you use to connect Databricks to Sigma needs underlying access to the data. For instructions on how to set these permissions in Unity Catalog, see [Manage privileges in Unity Catalog](https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/index.html) in the Databricks documentation.

   * At the catalog level, grant all account users `USE CATALOG` and `USE SCHEMA` privileges.
   * At the schema level, grant all account users `BROWSE`, `EXECUTE`, `READ VOLUME`, and `SELECT` privileges.
   * If you plan to enable write-access features on this connection, also grant all account users `MODIFY` and `CREATE TABLE` privileges at the schema level on the dedicated databases and schemas you've defined for write access.
     For details on these privileges, see [Unity Catalog privileges and securable objects](https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/privileges.html) in the Databricks documentation.

> 📘
>
> ### If you are using the legacy Hive metastore to manage permissions, the permissions model is different. To set up equivalent permissions with the legacy Hive metastore, see [Hive metastore privileges and securable objects (legacy)](https://docs.databricks.com/en/data-governance/table-acls/object-privileges.html) in the Databricks documentation. If you want to sync data from your `hive_metastore` catalog, the tables in that catalog require `READ_METADATA` privileges.

5. Obtain the **Server hostname** and **HTTP path** from your SQL warehouse’s **Connection details** screen. You need these values in the next step when you configure the Databricks connection in Sigma.
6. Create an access token for the user or service principal to use to connect to this SQL warehouse. The type of token you create depends on the authentication method you use when configuring the Databricks connection in Sigma. For token creation instructions, see [Authentication for Databricks tools and APIs](https://docs.databricks.com/dev-tools/api/latest/authentication.html) in the Databricks documentation.

## Create a Databricks connection in Sigma

To create a Databricks connection, perform the following steps in Sigma:

* [Add a connection and specify connection details](#add-a-connection-and-specify-connection-details)
* [Specify your connection credentials](#specify-your-connection-credentials)
* [Configure write access](#configure-write-access)
* [Configure connection features](#configure-connection-features)

### Add a connection and specify connection details

1. Click the user icon at the top right of your screen.
   The user icon is usually composed of your initials.
2. In the drop-down menu, select **Add connection**. The **Add new connection** page appears.
3. In the **Connection Details** section, specify the following:

   |  |  |
   | --- | --- |
   | **Name** | Enter a **Name** for the new connection. Sigma displays this name in the connection list. |
   | **Type** | Select **Databricks**. |

### Specify your connection credentials

In the **Connection Credentials** section, fill out the required fields:

1. In the **Host** field, enter the value of the **Server hostname** field in the **Connection details** screen of your SQL warehouse.
2. In the **HTTP path** field, enter the value of the **HTTP path** field in the **Connection details** screen of your SQL warehouse.
3. Click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) next to **Authentication**, then choose your authentication method.

   * If you want to authenticate your connection with OAuth, select **OAuth**.
   * Otherwise, select **Basic Auth**, then generate a token in Databricks to authenticate the Sigma connection. For instructions, see [Databricks personal access tokens for service principals](https://docs.databricks.com/en/dev-tools/auth/pat.html#databricks-personal-access-tokens-for-service-principals) in the Databricks documentation.

Next, see [Configure OAuth features](#configure-oauth-features) if you are using OAuth to authenticate your connection. If you are not using OAuth, skip to [Configure write access](/docs/connect-to-databricks#configure-write-access) and [Configure connection features](/docs/connect-to-databricks#configure-connection-features) for additional options. Or, if you are finished configuring your connection, click **Create** at the top right to create your connection.

### Configure OAuth features

If you selected OAuth as your authentication method for the connection, complete these steps.

1. [optional] If you are using OAuth to authenticate users to your Sigma organization with Databricks Authorization Server and you want to re-use that OAuth configuration for this connection, enable the toggle next to **Use organization-level OAuth configuration**. If you do not use OAuth as your authentication method for your Sigma organization, this option is not present. If you use an external IdP (Okta, Microsoft Entra ID, Auth0, or PingIndentity), do not enable this toggle because Databricks does not support authenticating using an external IdP. If you enable this toggle, skip to step 3.
2. If you do not have an organization-level OAuth configuration, or if you do not wish to re-use the your organization-level OAuth configuration, set up a unique OAuth configuration for this connection.

   > 📘
   >
   > ### The option to configure a unique OAuth application to authenticate users to a connection – in other words, opting to not re-use the OAuth configuration you use at the organization level – is a public beta feature and is subject to limitations.
   >
   > See [Use different OAuth configurations for authenticating users to your connections than you use for your Sigma organization](/docs/configure-oauth#use-different-oauth-configurations-for-authenticating-users-to-your-connections-than-you-use-for-your-sigma-organization).

   Complete the procedure in [Configure a custom OAuth application for Sigma in Databricks Authorization Server](/docs/configure-a-sigma-oauth-application#configure-a-custom-oauth-application-for-sigma-in-databricks-authorization-server) before filling out the fields in the **OAuth Features** section.

   1. [optional] Enter any additional **Scopes** to further specify the access of the OAuth token. The default scopes `openid`, `profile`, `email`, and `all-apis` are required. The default scope `offline_access` is not required.
   2. In the **Metadata URI** field, enter the OAuth metadata URI. For instructions on how to obtain this value, see [Determine your metadata URI for your Databricks Authorization Server](/docs/configure-a-sigma-oauth-application#determine-the-metadata-uri-for-your-databricks-authorization-server).
   3. In the **Redirect URI** field, use the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/copy.svg) icon to copy the redirect URI to your clipboard, to use when configuring your OAuth configuration in your IdP.
   4. In the **Client ID** field, enter the client ID from your OAuth application. For instructions on how to obtain this value, see [Configure a custom OAuth application for Sigma in Databricks Authorization Server](/docs/configure-a-sigma-oauth-application#configure-a-custom-oauth-application-for-sigma-in-databricks-authorization-server).
   5. In the **Client Secret** field, enter the client secret from your OAuth application. For instructions on how to obtain this value, see [Configure a custom OAuth application for Sigma in Databricks Authorization Server](/docs/configure-a-sigma-oauth-application#configure-a-custom-oauth-application-for-sigma-in-databricks-authorization-server).
      After you enter and save this value, Sigma does not display it.
3. Determine whether you will need a **Service Account**. There are three reasons to configure a service account:

   * If you enable write access on this connection, a service account is required. Sigma uses the service account to log all edits made to all input tables on this connection.
   * If you use Sigma’s [public embedding](/docs/public-embedding) features, a service account is required. Service account credentials are used to run queries on publicly embedded dashboards.
   * If you want admins to be able to configure individual workbooks to run using a service account rather than each individual’s OAuth credentials, a service account is required. See [Run a workbook with service account credentials](/docs/run-a-workbook-with-service-account-credentials).
4. If you need a service account, enable the toggle for **Service Account** and enter an **Access token** for that service account. For instructions, [Databricks personal access tokens for service principals](https://docs.databricks.com/en/dev-tools/auth/pat.html#databricks-personal-access-tokens-for-service-principals) in the Databricks documentation.

Next, see [Configure OAuth features](#configure-oauth-features) if you are using OAuth to authenticate your connection. If you are not using OAuth, skip to [Configure write access](/docs/connect-to-databricks#configure-write-access) and [Configure connection features](/docs/connect-to-databricks#configure-connection-features) for additional options. Or, if you are finished configuring your connection, click **Create** at the top right to create your connection.

### Configure write access

Write access is necessary for the following features:

* [CSV upload](/docs/upload-csv-data)
* [Materialization](/docs/materialization)
* [Input tables](/docs/intro-to-input-tables)
* [Warehouse views](/docs/create-and-manage-workbook-warehouse-views)
* [Write Python code](/docs/write-and-run-python-code)

The steps to configure write access differ depending on whether you are using OAuth or basic authentication for the connection. Follow the instructions that match your authentication option:

* [Configure write access on a connection with basic authentication](#configure-write-access-on-a-connection-with-basic-authentication)
* [Configure write access on a connection with OAuth](#configure-write-access-on-a-connection-with-oauth)

#### Configure write access on a connection with basic authentication

Configuring write access requires you to set up dedicated catalogs and schemas in Databricks that Sigma can use to write data and grant `MODIFY` and `CREATE TABLE` privileges on those schemas to the service account.

Turn on the switch next to **Enable write access**. Then, configure the following fields:

1. In the **Write catalog** field, enter the name of the catalog where Sigma should store write-back data.
2. In the **Write schema** field, enter the schema where Sigma should store write-back data.

#### Configure write access on a connection with OAuth

Configuring write access requires setting up dedicated databases and schemas in Databricks granting the necessary permissions. See [Configure OAuth with write access](/docs/configure-oauth-with-write-access) for all prerequisite steps.

1. Turn on the switch next to **Enable write access**.
2. Provide at least one **Destination** where Databricks should store write-back data from Sigma. Use the format CATALOG.SCHEMA.
3. [optional] Enter additional destinations as needed, depending on how you want to partition the data that Sigma writes back to your data warehouse. For example, you might create separate destinations for different teams and set up your team and schema permissions to ensure that each team has access to write to their designated destinations.
4. [optional, but required to use input tables] In the **Input table edit log destination** field, provide an additional CATALOG.SCHEMA destination to log all edits made to input tables on this connection. This CATALOG.SCHEMA should be used only for this purpose. Only your service account should have access to write to this schema. If you leave this field blank, input tables cannot be created on this connection.

### Configure connection features

In the **Connection Features** section, specify the following:

1. In the **Connection timeout** field, specify the amount of time, in seconds, that Sigma should wait for the query to return results before timing out. The default in 120 seconds. The maximum is 600 seconds (10 minutes).
2. [optional] If you do not want Sigma to automatically make column names from the data source more readable, turn off the **Use friendly names** switch. For example, with **Use friendly names** turned on, a database column ORDER\_NUMBER or OrderNumber appears as Order Number.
3. [optional] If you want to see and use your `hive_metastore` catalog in Sigma, turn on the **Enable Hive metastore** switch . Turned off by default.

### Enable Python

To enable Python on your Databricks connection, follow the steps to [Set up a Databricks connection for Python (Beta)](/docs/set-up-a-databricks-connection-for-python), including the Databricks configuration steps.

### Finish creating your connection

After you specify all the parameters of the connection, click **Create.**

1. Click **Create** at the top right of the screen to create your connection. Sigma displays a connection summary on the screen.
2. Click **Browse Connection**, then click **Add permission** to grant connection access for users in your organization. See [Data permissions](/docs/data-permissions-overview).

   ![The Permission summary on the connection, showing that no users have access to this connection yet.](https://files.readme.io/b31514d9ab39f7df1c969c6dc7b9abbbdd61d7eccd43909d8c72826a33ce7f7f-databricks-newly-created-connection.png)
3. Use the navigation in the left panel to explore the schemas and tables in your connection.

   ![The browse connection view, showing a table available through the connection](https://files.readme.io/fdbc21c43fc31c87438bba5aef11a8bdb03d055fcd10e4fe004485e7cd04fb12-databricks-browse-connection.png)

## Databricks Partner Connect

Databricks is one of Sigma's partners, so you can quickly establish a connection through the interface. See [What is Databricks Partner Connect?](https://docs.databricks.com/partner-connect/index.html) in the Databricks documentation.

Updated 3 days ago

---

Related resources

* [Databricks Partner Connect](https://docs.databricks.com/partner-connect/index.html)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Configure Databricks](#configure-databricks)
  + [Create a Databricks connection in Sigma](#create-a-databricks-connection-in-sigma)
  + - [Add a connection and specify connection details](#add-a-connection-and-specify-connection-details)
    - [Specify your connection credentials](#specify-your-connection-credentials)
    - [Configure OAuth features](#configure-oauth-features)
    - [Configure write access](#configure-write-access)
    - [Configure connection features](#configure-connection-features)
    - [Enable Python](#enable-python)
    - [Finish creating your connection](#finish-creating-your-connection)
  + [Databricks Partner Connect](#databricks-partner-connect)