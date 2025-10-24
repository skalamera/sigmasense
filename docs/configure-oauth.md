# Configure OAuth

# Configure OAuth

You can configure OAuth as an authentication method for your Sigma organization, for your connections to your data platforms, or both.

Using OAuth has several advantages:

* Authenticating Sigma users with OAuth minimizes the risk of password leaks or misuse, which is crucial for maintaining data security and privacy.
* Connections authenticated with OAuth allow your users to read data and use write-back features like input tables, warehouse views, materializations, and CSV uploads with their own individual credentials instead of a service account.
* Admins have the option to configure individual workbooks to run queries using the service account instead of each user’s OAuth credentials. See [Run a workbook with service account credentials](/docs/run-a-workbook-with-service-account-credentials).

## Requirements

* You must be assigned the **Admin** [account type](/docs/user-account-types) to manage authentication for your Sigma organization.

> 💡
>
> ### When transitioning authentication methods for your Sigma organization from basic authentication to OAuth, the best practice is to transition first to the **OAuth or password** option rather than directly to requiring OAuth only login for all users. With the authentication method set to **OAuth or password**, you retain the ability to log in with a password during the transition to your IdP based login, ensuring that you are not locked out during the configuration change. Once you have confirmed that users are able to log in using OAuth, you can transition to OAuth only login.

## About OAuth for permissions management

OAuth is an authorization framework that allows your users to securely log in to applications without the need for a username and password. This authorization happens between a client (you and your users) and one or more resources (i.e. Sigma and your data platform) via your Identity Provider (IdP). Your IdP uses an authorization server and short-lived tokens to authenticate your application’s users.

The OAuth framework supports the OpenID Connect (OIDC) open authentication protocol, which verifies user identities and authorizes access to digital services. In Sigma's product and documentation, the term OAuth is used to refer to both the OAuth framework and the OIDC protocol for authentication.

Configuring OAuth on the connections between Sigma and your data platforms allows your users to see only the data that they are permitted to see in the data platform. This is accomplished by establishing a chain of trust between your IdP, your data platform, and Sigma.

## Use different OAuth configurations for authenticating users to your connections than you use for your Sigma organization

You can enable OAuth as the method of authenticating users to your Sigma organization, or on a per-connection basis in Sigma for any of your connections that support OAuth, or both. If you use multiple IdPs and data platforms, you can create connections with different OAuth configurations.

> 🚧
>
> ### While this feature is in public beta, if you choose the option to use a unique OAuth configuration at the connection level rather than re-using your organization-level OAuth configuration, users need the **View connections** permission, as well as a grant on the OAuth connection, to access and sign into the connection. See [License and account type overview](/docs/license-and-account-type-overview). To avoid this restriction and still use OAuth to authenticate a connection, configure OAuth at the organization level and then re-use that configuration when you create your connection.

## Limitations of using OAuth in Sigma

When authenticating a connection with OAuth, note the following:

* OAuth is only supported for the following connection types:
  + Snowflake
  + Databricks
* OAuth tokens can expire if the owner goes a significant amount of time without logging in to Sigma. If this happens, scheduled exports and other schedules fail. This limitation can be avoided by running the workbook as a service account. See [Run a workbook with service account credentials](/docs/run-a-workbook-with-service-account-credentials).
* Any Sigma user that is not provisioned with an account in your IdP cannot access data on OAuth-authenticated connections. These users are still able to see data from these connections in workbooks that are run with service account credentials.

When authenticating users to your Sigma organization with OAuth, note the following:

* When users configured in your IdP do not already have a Sigma account associated with their email address, Sigma auto-provisions them with a Sigma account with a Lite account type upon their first login. To change the account type for these users, an admin needs to manually adjust the account type assignments in Sigma. See [Reassign members from a specific account type](/docs/create-and-manage-account-types#reassign-members-from-a-specific-account-type). This manual reassignment of account types is not required if you use SCIM for user and account management. ​​See [Manage users and teams with SCIM](/docs/manage-users-and-teams-with-scim).

## Plan your OAuth configuration

1. Configure a Sigma OAuth application to enable authentication via your IdP. See [Configure a Sigma OAuth application](/docs/configure-a-sigma-oauth-application).
2. [optional] If you want to use OAuth to authenticate users to your Sigma organization, configure OAuth as your authentication method. See [Configure OAuth authentication for your Sigma organization](/docs/configure-oauth-authentication-for-your-sigma-organization).
3. [optional] If you require write-back features in OAuth-enabled connections, prepare your schema in your data platform. See [Configure OAuth with write access](/docs/configure-oauth-with-write-access).
4. [optional] Update existing connections to use OAuth, or create new ones. See:
   * [Connect to Snowflake](/docs/connect-to-snowflake)
   * [Connect to Databricks](/docs/connect-to-databricks)

Updated 3 days ago

---

Related resources

* [Configure a Sigma OAuth application](/docs/configure-a-sigma-oauth-application)
* [Configure OAuth authentication for your Sigma organization](/docs/configure-oauth-authentication-for-your-sigma-organization)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [About OAuth for permissions management](#about-oauth-for-permissions-management)
  + [Use different OAuth configurations for authenticating users to your connections than you use for your Sigma organization](#use-different-oauth-configurations-for-authenticating-users-to-your-connections-than-you-use-for-your-sigma-organization)
  + [Limitations of using OAuth in Sigma](#limitations-of-using-oauth-in-sigma)
  + [Plan your OAuth configuration](#plan-your-oauth-configuration)