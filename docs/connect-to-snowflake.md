# Connect to Snowflake

# Connect to Snowflake

Sigma supports secure connections to Snowflake.

> 📘
>
> ### For information about Sigma feature compatibility with Snowflake connections, see [Region, warehouse, and feature support](/docs/region-warehouse-and-feature-support).

This document explains how to connect your organization to a Snowflake warehouse from Sigma.

> 📘
>
> ### If you do not already have a Sigma organization created, you can use Snowflake Partner Connect to create an organization and connect your Snowflake database with just a few clicks. You must have the `ACCOUNTADMIN` role in Snowflake to use Snowflake Partner Connect. To sign up with Snowflake Partner Connect, select Sigma from the Partner Connect list, then click **Connect** in the Connect to Sigma modal.

For an end-to-end walkthrough of an OAuth configuration using Snowflake and Okta, see the [Open Authorization (OAuth)](https://quickstarts.sigmacomputing.com/guide/security_oauth/index.html?index=..%2F..index#0) QuickStart.

## Requirements

* You must be assigned the **Admin** [account type](/docs/user-account-types).
* You must be able to provide the credentials for a Snowflake user with a role that has `USAGE` privileges to the necessary databases and schemas, and `SELECT` privileges to the necessary tables.
* If you configure Snowflake with key pair authentication, you must know the login\_name of the user associated with the public key, which can be different from the user name. Find the login\_name for any user by running the [DESCRIBE USER command in Snowflake](https://docs.snowflake.com/en/sql-reference/sql/desc-user). Find all valid names for the DESCRIBE USER command with the [ALL\_USER\_NAMES](https://docs.snowflake.com/en/sql-reference/functions/all_user_names) function.

> 🚩
>
> ### Sigma queries the Snowflake connection every 24 hours to index the databases, schemas, tables, and views. This process is automated, and reads from the Snowflake metadata in the cloud services layer. Under normal usage, this process results in minimal credit consumption; however in cases where there is minimal usage in a 24 hour period, higher credit consumption may occur. Snowflake connections without service accounts and authentication currently aren't indexed for cost reasons. To learn more about the cloud service layer and costs, see [Understanding overall cost](https://docs.snowflake.com/user-guide/cost-understanding-overall) in the Snowflake documentation.

## Create a Snowflake connection in Sigma

To create a Snowflake connection, perform the following steps in Sigma:

* [Add a connection and specify connection details](#add-a-connection-and-specify-connection-details)
* [Specify your connection credentials](#specify-your-connection-credentials)
* Configure an authentication method:
  + [Connect to Snowflake with key pair authentication](#connect-to-snowflake-with-key-pair-authentication)
  + [Connect to Snowflake with OAuth](#connect-to-snowflake-with-oauth)
  + [Connect to Snowflake with basic authentication](#connect-to-snowflake-with-basic-authentication)
* [Configure write access](#configure-write-access)
* [Configure connection features](#configure-connection-features)

### Add a connection and specify connection details

1. Click the user icon at the top right of your screen.
   The user icon is usually composed of your initials.
2. In the drop-down menu, select **Add connection**. The **Add new connection** page appears.
3. In the **Connection details**, specify the following:

|  |  |
| --- | --- |
| **Name** | Enter a **Name** for the new connection. Sigma displays this name in the connection list. |
| **Type** | Select **Snowflake**. |

### Specify your connection credentials

In the **Connection Credentials** section, fill out the required fields:

1. [optional] If you access Snowflake using a proxy server, turn on the **Use Custom Host** toggle, then enter the **Snowflake Custom Host** name.
2. In the **Account** field, enter the Snowflake account name. For details on how to format your account name, see [Using an account name as an identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier#label-account-name-using) in the Snowflake documentation.
3. In the **Warehouse** field, enter your warehouse’s name as listed in Snowflake.

> 📘
>
> ### To set the warehouse using user attributes, click **Set by user attributes** in the **Warehouse** field . See [Dynamically assign roles used by a connection](/docs/dynamically-assign-roles-used-by-a-connection).

4. If you set your **Warehouse** field using user attributes and you plan to use input tables on this connection, provide a warehouse name in the **Service Account Warehouse** field that the service account can use in cases of dynamic warehouse switching. See [Warehouse Switching](https://quickstarts.sigmacomputing.com/guide/embedding_09_dynamic_role_switching_snowflake/index.html#8) in the Dynamic Role Switching with Snowflake QuickStart.
5. Click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) next to **Authentication**, then choose your authentication method, and then fill in the required fields for the method you select:

   * [Connect to Snowflake with key pair authentication](#connect-to-snowflake-with-key-pair-authentication)
   * [Connect to Snowflake with OAuth](#connect-to-snowflake-with-oauth)
   * [Connect to Snowflake with basic authentication](#connect-to-snowflake-with-basic-authentication)

| Authentication Type | Considerations |
| --- | --- |
| **Key-Pair** | Authenticate to your Snowflake data warehouse using a private key.  You can delegate user access through the service account that the connection is configured with. You can parameterize this connection to use a different role and warehouse on a per-user or per-team basis with Sigma user attributes, so long as the service account has access to the requested role. Any form of authentication to Sigma is supported  This is recommended when your users don't have accounts in Snowflake, or when you don't want your Snowflake policies or grants to be inherited by users in Sigma. |
| **Connection level OAuth** | Authenticate to your data warehouse using the Snowflake's connection level OAuth configuration.  All users gain access to data in Sigma based on their roles in Snowflake. Policies you apply in Snowflake also apply in Sigma, such as RLS or other RBAC policies. For this method, you can sign into Sigma through any method while using the warehouse connection's own OAuth configuration. When users access data on the connection, they login and gain access as individual users to your Snowflake warehouse.  This method is recommended when your users have accounts in Snowflake and you want your Snowflake permissions and grants to be inherited in Sigma on a per-user basis, but you want to use other authentication methods for Sigma, or different OAuth servers to authenticate users into Sigma and Snowflake. |
| **Organization level OAuth** | Authenticate into your Snowflake warehouse using the same OAuth server that you use for your organization. When a user signs into Sigma through the OAuth server, Sigma receives an OAuth token which it uses to automatically sign the named user into Snowflake.  All user access to Snowflake is based on an individual user’s grants and access in Snowflake. Any policies you apply in Snowflake apply in Sigma, such as RLS or other RBAC policies.  This method is recommended when your users have accounts in Snowflake and you want your Snowflake permissions and grants to be inherited in Sigma on a per-user basis and you want to use the same OAuth server to authenticate both Sigma and Snowflake. |

> 🚩
>
> ### Snowflake will no longer be supporting username/password authentication, and recommends using key pair authentication or OAuth for programmatic service users, and you can enforce that with authentication policies. See [Snowflake Strengthens Security with Default Multi-Factor Authentication and Stronger Password Policies](https://www.snowflake.com/en/blog/multi-factor-identification-default/) in the Snowflake blog.

### Connect to Snowflake with key pair authentication

To authenticate the connection using a combination of public and private RSA key pairs, select **Key Pair** as your authentication method.

This method requires that you have a public and private key already created, and a Snowflake user configured with the public key. For instructions, see [Key-pair authentication and key-pair rotation](https://docs.snowflake.com/en/user-guide/key-pair-auth) in the Snowflake documentation. If you have a multi-factor authentication (MFA) policy applied, exclude this user from the MFA policy. For a full walkthrough of all prerequisite steps, as well as detailed steps on how to rotate your keys, see the [Snowflake Key-pair Auth QuickStart](https://quickstarts.sigmacomputing.com/guide/security_snowflake_keypair_rotation).

1. In the **User** field, enter the Snowflake login name that is configured with the public key. Retrieve the login name for a user by running the DESCRIBE USER command in Snowflake.
2. In the **Private Key** field, paste the private key text, including the header.

   ![Connection Credentials form with required fields for key-pair authentication filled in](https://files.readme.io/f0e02b9c4a1497cfdb9733877596878be2c3735b9f19fd8740cce5a780be9a5f-connection_credentials_private_key1.png)
3. [optional] If you configured one, enter the **Private Key Passphrase**.
4. [optional] Enter a Snowflake **Role** to be used on this connection. If no role is provided, the user's default role in Snowflake is used.

   > 📘
   >
   > ### To set the role using user attributes, click **Set by user attributes** in the **Role** field. See [Dynamically assign roles used by a connection](/docs/dynamically-assign-roles-used-by-a-connection).
5. If you set your **Role** field using user attributes and you plan to use input tables on this connection, provide a **Service Account Role** that the service account can use in cases of dynamic role switching. If not set, the service account's role will be the default role set for the user in Snowflake. See the [Dynamic Role Switching with Snowflake QuickStart](https://quickstarts.sigmacomputing.com/guide/embedding_09_dynamic_role_switching_snowflake/index.html#0).

Next, see [Configure write access](/docs/connect-to-snowflake#configure-write-access) and [Configure connection features](/docs/connect-to-snowflake#configure-connection-features) for additional options. Or, if you are finished configuring your connection, click **Create** at the top right to create your connection.

### Connect to Snowflake with OAuth

If you have OAuth enabled on your organization and you want to use it on the connection select **OAuth** as your authentication method.

1. [optional] If you are using OAuth to authenticate users to your Sigma organization with an external IdP (Okta, Microsoft Entra ID, Auth0, or PingIndentity) and you want to re-use that OAuth configuration for this connection, enable the toggle next to **Use organization-level OAuth configuration**. If you do not use OAuth as your authentication method for your Sigma organization, this option is not present. If you enable this toggle, skip to step 3.
2. If you do not have an organization-level OAuth configuration, or if you do not wish to re-use the your organization-level OAuth configuration, set up a unique OAuth configuration for this connection.

   See [Use different OAuth configurations for authenticating users to your connections than you use for your Sigma organization](/docs/configure-oauth#use-different-oauth-configurations-for-authenticating-users-to-your-connections-than-you-use-for-your-sigma-organization).

   Complete the procedure in [Configure a Sigma OAuth application](/docs/configure-a-sigma-oauth-application) before filling out the fields in the **OAuth Features** section.

   1. [optional] Enter any additional **[Scopes](https://docs.snowflake.com/en/user-guide/oauth-ext-overview#scopes)** to further specify the access of the OAuth token. The default scopes `openid`, `profile`, and `email` are required. You must enter a `session:role` scope. Sigma supports these role types that you can use define separate connections for custom or fixed roles, instead of just your default role:

      * `session:role-any`
      * `session:role:<_custom_role_>`
      * `session:role:public`

      You can find more information about Snowflakes external OAuth scopes, [External OAuth overview](https://docs.snowflake.com/en/user-guide/oauth-ext-overview#scopes) in the Snowflake documentation.

      The default scope `offline_access` is recommended but not required. For more information about these scopes, see Step 3: Create an authorization server in [Configure a Sigma OAuth application](/docs/configure-a-sigma-oauth-application#step-3-create-an-oauth-authorization-server).

      > 📘
      >
      > ### If you are using Microsoft Entra ID as your IdP, prepend any of the `session:role` role scopes with the application ID URI, found under "Scopes defined by this API" on the Expose an API page in Microsoft Entra ID. The resulting scope will follow this pattern as an example: `https://<your_azure_domain>/<your_app_UUID>/session:role-any`.
   2. In the **Metadata URI** field, enter the OAuth metadata URI. For instructions on how to obtain this value, see Step 3: Create an authorization server in [Configure a Sigma OAuth application](/docs/configure-a-sigma-oauth-application#step-3-create-an-oauth-authorization-server).
   3. In the **Redirect URI** field, use the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/copy.svg) icon to copy the redirect URI to your clipboard, to use when configuring your OAuth configuration in your IdP.
   4. In the **Client ID** field, enter the client ID from your OAuth application. For instructions on how to obtain this value, see Step 1: Create an app for Sigma in your IdP in [Configure a Sigma OAuth application](/docs/configure-a-sigma-oauth-application#step-1-create-an-app-for-sigma-in-your-idp).
   5. [optional] If you did not enable PKCE in your OAuth application, enter the client secret from your OAuth application in the **Client Secret** field. For instructions on how to obtain this value, see Step 1: Create an app for Sigma in your IdP in [Configure a Sigma OAuth application](/docs/configure-a-sigma-oauth-application#step-1-create-an-app-for-sigma-in-your-idp). After you enter and save this value, Sigma does not display it.
   6. [optional] Check the box next to **Require PKCE** if you want to use Proof Key for Code Exchange to further authenticate this connection. Only select this option if you configured your Sigma OAuth application to require PKCE. See Step 1: Create an app for Sigma in your IdP in in [Configure a Sigma OAuth application](/docs/configure-a-sigma-oauth-application#step-1-create-an-app-for-sigma-in-your-idp).
   7. [optional] Check the box next to **Use JWT bearer tokens** if you want to use JSON Web Tokens to further authenticate this connection. Only select this option if you configured your Sigma OAuth application to use JWT bearer tokens (or public key / private key). See Step 1: Create an app for Sigma in your IdP in [Configure a Sigma OAuth application](/docs/configure-a-sigma-oauth-application#step-1-create-an-app-for-sigma-in-your-idp).
3. Determine whether you need a **Service Account**. There are three reasons to configure a service account:

   * If you enable write access on this connection, a service account is required. Sigma uses the service account to log all edits made to all input tables on this connection.
   * If you use Sigma’s [public embedding](/docs/public-embedding) features, a service account is required. Service account credentials are used to run queries on publicly embedded dashboards.
   * If you want admins to be able to configure individual workbooks to run using a service account rather than each individual’s OAuth credentials, a service account is required. See [Run a workbook with service account credentials](/docs/run-a-workbook-with-service-account-credentials).

> 📘
>
> ### A **service account** is a Snowflake user created for administrative purposes in Sigma. It is the same as any other Snowflake user. The user must be granted the role you want to use for your connection, and that role must be granted `USAGE` privilege on the warehouse. If you have a multi-factor authentication (MFA) policy applied, exclude the service account from this policy.
>
> Your service account must be added to the OAuth user list like all other OAuth accounts on the connection. See [Configure a Sigma OAuth application](/docs/configure-a-sigma-oauth-application).

4. If you determine that you need a service account, turn on the **Service account** switch, then:

   1. Select **Key Pair** from the **Authentication** drop down menu.
   2. Enter the **User** and **Private key** for the Snowflake service account.
5. [optional] Enter the **Private key passphrase** for the Snowflake service account. This field is only required when your private key is encrypted.
6. [optional] Enter a Snowflake **Role** to be used on this connection. If no role is provided, the user's default role in Snowflake is used.

Next, see [Configure write access](#configure-write-access) and [Configure connection features](#configure-connection-features) for additional options. Or, if you are finished configuring your connection, click **Create** at the top right to create your connection.

### Connect to Snowflake with basic authentication

To connect with a username and password, select **Basic Auth** as your authentication method.

> 🚩
>
> ### Sigma Computing recommends transitioning away from using basic authentication when connecting to Snowflake. For improved security, use key pair or OAuth authentication instead.

> 🚩
>
> ### Snowflake will block all users, including service users, from using single-factor authentication by August 2026. You must transition to multi-factor authentication by that time. For full details on Snowflake's deprecation plan, see [Planning for the deprecation of single-factor password sign-ins](https://docs.snowflake.com/en/user-guide/security-mfa-rollout).

If you have a multi-factor authentication (MFA) policy applied, exclude this user from the MFA policy.

1. In the **User** field, enter a Snowflake login\_name. In Snowflake, login\_name is different from user name. Find login\_name for any user with the [describe user command in Snowflake](https://docs.snowflake.com/en/sql-reference/sql/desc-user). Find all valid names for the describe user command with the [all\_user\_names command in Snowflake](https://docs.snowflake.com/en/sql-reference/functions/all_user_names).
2. In the **Password** field, enter a Snowflake password.
3. [optional] Enter a Snowflake **Role** to be used on this connection. If no role is provided, the user’s default role in Snowflake is used.

   > 📘
   >
   > ### To set the role using user attributes, click **Set by user attributes** in the **Role** field. See [Dynamically assign roles used by a connection](/docs/dynamically-assign-roles-used-by-a-connection).
4. If you set your **Role** field using user attributes and you plan to use input tables on this connection, provide a **Service Account Role** that the service account can use in cases of dynamic role switching. If not set, the service account uses the default role set for the user in Snowflake. See the [Dynamic Role Switching with Snowflake QuickStart](https://quickstarts.sigmacomputing.com/guide/embedding_09_dynamic_role_switching_snowflake/index.html#0).

Next, see [Configure write access](#configure-write-access) and [Configure connection features](/docs/connect-to-snowflake#configure-connection-features) for additional options. Or, if you are finished configuring your connection, click **Create** at the top right to create your connection.

### Configure write access

Write access is necessary for the following features:

* [CSV upload](/docs/upload-csv-data)
* [Materialization](/docs/materialization)
* [Input tables](/docs/intro-to-input-tables)
* [Warehouse views](/docs/create-and-manage-workbook-warehouse-views)

> 📘
>
> ### Binary input and output needs to be set to the **hex** format. See the Snowflake documentation on [Binary input and output](doc:https://docs.snowflake.com/en/sql-reference/binary-input-output).

The steps to configure write access differ depending on the authentication method used for the connection. Follow the instructions that match your authentication option:

* [Configure write access on a connection with Basic Auth or Key Pair Auth](#configure-write-access-on-a-connection-with-basic-auth-or-key-pair-auth)
* [Configure write access on a connection with OAuth](#configure-write-access-on-a-connection-with-oauth)

#### Configure write access on a connection with Basic Auth or Key Pair Auth

Configuring write access requires setting up a dedicated database and schema in Snowflake and granting the necessary privileges.

Before enabling write access, grant the Snowflake user that you use to configure the Sigma connection a role with the following privileges:

| Object | Privilege |
| --- | --- |
| Database | `USAGE` |
| Schema | `USAGE`, `CREATE TABLE`, `CREATE VIEW`, `CREATE STAGE` |

> 📘
>
> ### To perform incremental materialization with dynamic tables, the primary role used by the connection must also be granted the privileges listed in [Privileges to create a dynamic table](https://docs.snowflake.com/en/user-guide/dynamic-tables-privileges#label-dynamic-tables-privileges) in the Snowflake documentation.

Turn on the **Enable write access** toggle, then configure the following fields:

1. In the **Write database** field, enter the name of the database where Sigma should store write-back data.
2. In the **Write schema** field, enter the database schema where Sigma should store write-back data.
3. [optional] In the **Materialization warehouse** field, enter a separate warehouse to run queries that perform materialization. If you don't specify a materialization warehouse, Sigma uses the primary warehouse for this connection.
4. [optional] By default, Sigma uses dynamic tables for incremental materialization. If you do not want to use dynamic tables, turn off the **Use dynamic tables** switch. See [About materialization](/docs/materialization) for more details.

Next, see [Configure connection features](/docs/connect-to-snowflake#configure-connection-features) for additional options. Or, if you are finished configuring your connection, click **Create** at the top right to create your connection.

#### Configure write access on a connection with OAuth

Configuring write access requires setting up dedicated databases and schemas in Snowflake and granting the necessary privileges. See [Configure OAuth with write access](/docs/configure-oauth-with-write-access) for all prerequisite steps.

Turn on the **Enable write access** toggle, then configure the following fields:

1. Provide at least one **Destination** where Snowflake should store write back data from Sigma. Use the format DATABASE.SCHEMA.
2. [optional] Enter additional destinations as needed, depending on how you want to partition the data that Sigma writes back to your data warehouse. For example, you might create separate destinations for different teams and set up your team and schema permissions to ensure that each team has access to their designated destinations.
3. [optional, but required to use input tables] In the **Input table edit log destination** field, provide an additional DATABASE.SCHEMA destination specifically to log all edits made to input tables on this connection. This DATABASE.SCHEMA should be used only for this purpose. Only your service account should have access to write to this schema. If you leave this field blank, input tables cannot be created on this connection.
4. [optional] In the **Materialization warehouse** field, enter a separate warehouse to run queries that perform materialization. If you don't specify a materialization warehouse, Sigma uses the primary warehouse for this connection.
5. [optional] By default, Sigma uses dynamic tables for incremental materialization. If you do not want to use dynamic tables, turn off the **Use dynamic tables** switch. See [About materialization (Beta)](/docs/materialization) for more details.

Next, see [Configure connection features](#configure-connection-features) for additional options. Or, if you are finished configuring your connection, click **Create** at the top right to create your connection.

### Configure connection features

In the **Connection Features** section, specify the following:

1. In the **Connection timeout** field, specify the amount of time, in seconds, that Sigma should wait for the query to return results before timing out. The default in 120 seconds. The maximum is 600 seconds (10 minutes).
2. [optional] If you do not want Sigma to automatically make column names from the data source more readable, turn off the **Use friendly names** switch. For example, with **Use friendly names** enabled, a database column ORDER\_NUMBER or OrderNumber appears as Order Number.
3. [optional] In the **Export warehouse** field, enter the name of the virtual warehouse created for export queries. For more details, see [Configure an export warehouse](/docs/configure-an-export-warehouse).

### Finish creating your connection

After you specify all of the parameters for the connection, click **Create.**

1. Click **Create** at the top right of the screen to create your connection. Sigma displays a connection summary on the screen.
2. Click **Browse Connection**, then click **Grant access** to grant data access for users in your organization. See [Data access overview](/docs/data-permissions-overview).
3. Use the navigation in the left panel to explore the schemas and tables in your connection.

   ![The browse connection view, showing a table available through the connection](https://files.readme.io/df1cae029a961e4beaffb79b6dca5804b6c2e02d17f610bd9d2d34a4bc750625-browse-snowflake-connection.png)

Updated 3 days ago

---

Related resources

* [Snowflake usage templates](/docs/snowflake-usage-templates)
* [Troubleshoot your connection](/docs/troubleshoot-your-connection)
* [Set up write access](/docs/set-up-write-access)
* [Configure OAuth with write access](/docs/configure-oauth-with-write-access)
* [Configure user attributes on a Snowflake connection](/docs/configure-user-attributes-on-a-snowflake-connection)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Create a Snowflake connection in Sigma](#create-a-snowflake-connection-in-sigma)
  + - [Add a connection and specify connection details](#add-a-connection-and-specify-connection-details)
    - [Specify your connection credentials](#specify-your-connection-credentials)
    - [Connect to Snowflake with key pair authentication](#connect-to-snowflake-with-key-pair-authentication)
    - [Connect to Snowflake with OAuth](#connect-to-snowflake-with-oauth)
    - [Connect to Snowflake with basic authentication](#connect-to-snowflake-with-basic-authentication)
    - [Configure write access](#configure-write-access)
    - [Configure connection features](#configure-connection-features)
    - [Finish creating your connection](#finish-creating-your-connection)