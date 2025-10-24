# Configure a Sigma OAuth application

# Configure a Sigma OAuth application

This document guides you through steps to create a Sigma OAuth application in your IdP to enable authentication to be handled by your IdP. You can then configure Sigma to connect to your OAuth application, either as an authentication method for login to your Sigma organization, or to authenticate Sigma connections to your data platform, or both.

Follow the steps that match the type of IdP you are using:

* [Configure a Sigma OAuth application in an external IdP](#configure-a-sigma-oauth-application-in-an-external-idp)
* [Configure a custom OAuth application for Sigma in Databricks Authorization Server](#configure-a-custom-oauth-application-for-sigma-in-databricks-authorization-server)

> 💡
>
> ### As a best practice, configure whichever IdP you use to notify you when your OAuth credentials are nearing expiration to avoid users getting locked out of your Sigma organization or your data connections.

## Requirements

* A supported identity provider (IdP). Sigma supports Okta, Microsoft Entra ID, Auth0, PingIndentity, or Databricks Authorization Server.

## Configure a Sigma OAuth application in an external IdP

Follow these steps to configure an OAuth app for Sigma in an external IdP such as Okta, Microsoft Entra ID, Auth0, or PingIdentity. If you are using Databricks Authorization Server, refer instead to [Configure a custom OAuth application for Sigma in Databricks Authorization Server](#configure-a-custom-oauth-application-for-sigma-in-databricks-authorization-server). For more information on setting up OAuth for specific IdPs, see the Sigma Community post on [Guidelines For Configuring OAuth and SAML Authentication](https://community.sigmacomputing.com/t/guidelines-for-configuring-oauth-and-saml-authentication/5427).

### High-level overview

The exact implementation of these steps varies depending on your IdP. Visit your IdP’s documentation for detailed instructions.

* [Requirements](#requirements)
* [Configure a Sigma OAuth application in an external IdP](#configure-a-sigma-oauth-application-in-an-external-idp)
  + [High-level overview](#high-level-overview)
  + [Step 1: Create an app for Sigma in your IdP](#step-1-create-an-app-for-sigma-in-your-idp)
  + [Step 2: Add OAuth users to your app](#step-2-add-oauth-users-to-your-app)
  + [Step 3: Create an OAuth authorization server](#step-3-create-an-oauth-authorization-server)
  + [Step 4: Add an access policy for the authorization server](#step-4-add-an-access-policy-for-the-authorization-server)
  + [Step 5: Create a security integration (Snowflake only)](#step-5-create-a-security-integration-snowflake-only)
* [Configure a custom OAuth application for Sigma in Databricks Authorization Server](#configure-a-custom-oauth-application-for-sigma-in-databricks-authorization-server)
  + [Determine the metadata URI for your Databricks Authorization Server](#determine-the-metadata-uri-for-your-databricks-authorization-server)

### Step 1: Create an app for Sigma in your IdP

First, create a Web OpenID Connect app within your IdP for Sigma. The exact configuration steps and wording of the options differ depending on your IdP.

Within the app, do the following:

1. Enable the authorization code grant type.
2. [recommended] Enable the refresh token grant type. This step is required if you specify the offline\_access scope (recommended) when you create an authorization server in Step 3: Create an OAuth authorization server.
3. [optional] To require Proof Key for Code Exchange (PKCE) for additional verification, select that option in your app configuration.
   > 📘
   >
   > ### PKCE is not supported for organization-level authentication, so if you do enable it, do not use this app to authenticate users to your Sigma organization. Instead, create a separate app for organization-level authentication that does not use PKCE.
4. [optional] If you want to use JSON Web Tokens (JWTs) to authenticate with a public key and private key instead of a client secret, select that option in your app configuration. In your IdP, this may be called "JWT bearer tokens" or "Public key / Private key".
   > 📘
   >
   > ### JWTs are not supported for organization-level authentication, so if you do enable JWT authentication, do not use this app to authenticate users to your Sigma organization. Instead, create a separate app for organization-level authentication that does not use JWTs.
5. [optional] If you select the option to use JWTs, provide Sigma's public cert when prompted. Use the URL that matches your deployment.

| Deployment | Sigma's public cert |
| --- | --- |
| GCP | <https://api.sigmacomputing.com/api/v2/.well-known/jwks.json> |
| AWS-US (West) | <https://aws-api.sigmacomputing.com/api/v2/.well-known/jwks.json> |
| AWS-US (East) | <https://api.us-a.aws.sigmacomputing.com/api/v2/.well-known/jwks.json> |
| AWS-CA | <https://api.ca.aws.sigmacomputing.com/api/v2/.well-known/jwks.json> |
| AWS-EU | <https://api.eu.aws.sigmacomputing.com/api/v2/.well-known/jwks.json> |
| AWS-UK | <https://api.uk.aws.sigmacomputing.com/api/v2/.well-known/jwks.json> |
| AWS-AU | <https://api.au.aws.sigmacomputing.com/api/v2/.well-known/jwks.json> |
| Azure-US | <https://api.us.azure.sigmacomputing.com/api/v2/.well-known/jwks.json> |
| Azure-EU | <https://api.eu.azure.sigmacomputing.com/api/v2/.well-known/jwks.json> |
| Azure-CA | <https://api.ca.azure.sigmacomputing.com/api/v2/.well-known/jwks.json> |
| Azure-UK | <https://api.uk.azure.sigmacomputing.com/api/v2/.well-known/jwks.json> |

6. Set the login redirect URL that matches your deployment:

| Deployment | Login redirect URL |
| --- | --- |
| GCP | <https://api.sigmacomputing.com/api/v2/oauth/1/authcode> |
| AWS-US (West) | <https://aws-api.sigmacomputing.com/api/v2/oauth/1/authcode> |
| AWS-US (East) | <https://api.us-a.aws.sigmacomputing.com/api/v2/oauth/1/authcode> |
| AWS-CA | <https://api.ca.aws.sigmacomputing.com/api/v2/oauth/1/authcode> |
| AWS-EU | <https://api.eu.aws.sigmacomputing.com/api/v2/oauth/1/authcode> |
| AWS-UK | <https://api.uk.aws.sigmacomputing.com/api/v2/oauth/1/authcode> |
| AWS-AU | <https://api.au.aws.sigmacomputing.com/api/v2/oauth/1/authcode> |
| Azure-US | <https://api.us.azure.sigmacomputing.com/api/v2/oauth/1/authcode> |
| Azure-EU | <https://api.eu.azure.sigmacomputing.com/api/v2/oauth/1/authcode> |
| Azure-CA | <https://api.ca.azure.sigmacomputing.com/api/v2/oauth/1/authcode> |
| Azure-UK | <https://api.uk.azure.sigmacomputing.com/api/v2/oauth/1/authcode> |

Creating your Sigma OAuth app generates a **Client ID** and (optionally) a **Client Secret**. These fields are required to complete your OAuth configuration in Sigma in a later procedure.

### Step 2: Add OAuth users to your app

After creating your OAuth app, add a list of your OAuth users. If you use this OAuth configuration to authenticate connections to your data platform, then these users are mapped to both Sigma and your data platform.

All users must be granted sufficient privileges in the data platform that you want to use to run queries from Sigma.

### Step 3: Create an OAuth authorization server

An authorization server is used to grant tokens to your users that identify them to Sigma and/or your data platform. Create an authorization server in your IdP that grants tokens with the following scopes:

| Scope | Required? | Description |
| --- | --- | --- |
| session:role-any | Required | Requests that the access tokens received by Sigma have permission to assume any role the user has been granted in the data platform. |
| offline\_access | Recommended | Requests a refresh token that can be used to get new access tokens "offline" (without asking a human user to re-authenticate with the IdP). Without this scope, users have to log in every time their access token expires and any scheduled operations fail if they run for longer than the validity of the access token. |
| openid | Required | Requests an OpenID token that can be used to authenticate the user to Sigma. |
| email | Required | Requests that the OpenID token include the user's email. |
| profile | Required | Requests that the OpenID token include other information from the user's profile (including the user's full name). |

For example, if you are configuring the authorization server to connect to Sigma and Snowflake, enter the following values:

| Field | Example value for Snowflake |
| --- | --- |
| Audience | `https://<your-snowflake-account>.snowflakecomputing.com` |
| Scopes | `session:role-any, offline_access, openid, email, profile` |
| Claims | `snowflake_username = <username>`  *Claims allow you to connect your OAuth users to user roles in your data platform. Claim definitions are IdP dependent.*  *The above claim is an example for Snowflake. The claim field you use must match the value of`EXTERNAL_OAUTH_TOKEN_USER_MAPPING_CLAIM` in your security integration. The claim value must match the value specified in the security integration's `EXTERNAL_OAUTH_SNOWFLAKE_USER_MAPPING_ATTRIBUTE` field.* |

The authorization server provides a **metadata URI**. The metadata URI is required to complete your OAuth configuration in Sigma in a later procedure.

The server also provides an **issuer url** and **jws keys url**, both of which are needed for the Snowflake security integration, which is required if you are using your OAuth app to connect to a Snowflake warehouse ([step 5](#step-5-create-a-security-integration-snowflake-only)).

If you are using Okta, note that Okta requires Okta API Access Management to be enabled in your Okta instance to create an authorization server.

### Step 4: Add an access policy for the authorization server

1. Create and/or assign an access policy to your new app (created in step 1). Access policies define rules for access and token lifetimes on an individual app.
2. Within the access policy, define access and refresh token lifetimes as desired for all grant types, users, and scopes.

> 📘
>
> ### The refresh token TTL setting determines how long users can be logged into Sigma before being prompted to log in again. Set a value consistent with your organization's security policies. To avoid frequent interruptions for your users, Sigma Computing recommends a TTL value of 90 days. To avoid disruption to scheduled exports, do not set a value lower than 7 days.

### Step 5: Create a security integration (Snowflake only)

Create a security integration in Snowflake to allow Snowflake to trust your IdP.

> 📘
>
> ### This step is necessary only if you want to use this Sigma OAuth application to authenticate one or more Snowflake connections with OAuth. If you don't use Snowflake, or if you are configuring the OAuth application only for authenticating users to your Sigma organization, then this step of establishing the trust relationship between your authorization server and Snowflake is not necessary.

See the [CREATE SECURITY INTEGRATION](https://docs.snowflake.com/en/sql-reference/sql/create-security-integration.html#id4) command reference in the Snowflake documentation. When creating the security integration, you need to provide the **issuer url** and **jws keys url** (created in [step 3](#step-3-create-an-authorization-server)).

The following is an example of the SQL statement you run in Snowflake if Okta is your IdP, with placeholder values in angle brackets. The values vary depending on your IdP.

SQL

```
create security integration <name>
   type = external_oauth
   enabled = true
   external_oauth_type = okta
   external_oauth_issuer = 'https://<COMPANY>.okta.com/oauth2/<ID>'
   external_oauth_jws_keys_url = 'https://<COMPANY>.okta.com/oauth2/<ID>/v1/keys'
   external_oauth_token_user_mapping_claim = 'snowflake_username'
   external_oauth_snowflake_user_mapping_attribute = 'login_name'
   external_oauth_any_role_mode = 'ENABLE';

 
```

## Configure a custom OAuth application for Sigma in Databricks Authorization Server

Enable a custom OAuth application in your Databricks account. To complete these steps, you need Account Admin privileges in Databricks. See [What are account admins?](https://docs.databricks.com/en/admin/index.html#what-are-account-admins) in the Databricks documentation.See the Databricks documentation for detailed instructions:

* See [Enable custom OAuth applications using the Azure Databricks UI](https://learn.microsoft.com/en-us/azure/databricks/integrations/enable-disable-oauth#enable-custom-app-ui) for Databricks on Azure.
* See [Enable custom OAuth applications using the Databricks UI](https://docs.databricks.com/en/integrations/enable-disable-oauth.html#enable-custom-oauth-applications-using-the-databricks-ui) for Databricks on AWS.

When you create the connection for the application in Databricks, you have several configuration options.

Sigma requires the following configurations for your OAuth connection to work:

* **Redirect URLs**: Enter a redirect URL that matches your Sigma deployment.

| Deployment | Login redirect URL |
| --- | --- |
| GCP | `https://api.sigmacomputing.com/api/v2/oauth/1/authcode` |
| AWS-US (West) | `https://aws-api.sigmacomputing.com/api/v2/oauth/1/authcode` |
| AWS-US (East) | `https://api.us-a.aws.sigmacomputing.com/api/v2/oauth/1/authcode` |
| AWS-CA | `https://api-ca-aws.sigmacomputing.com/api/v2/oauth/1/authcode` |
| AWS-EU | `https://api-eu-aws.sigmacomputing.com/api/v2/oauth/1/authcode` |
| AWS-UK | `https://api-uk-aws.sigmacomputing.com/api/v2/oauth/1/authcode` |
| AWS-AU | `https://api-au-aws.sigmacomputing.com/api/v2/oauth/1/authcode` |
| Azure-US | `https://api.us.azure.sigmacomputing.com/api/v2/oauth/1/authcode` |
| Azure-EU | `https://api.eu.azure.sigmacomputing.com/api/v2/oauth/1/authcode` |

* **Access scopes**: When you are prompted to select an access scope, select **All APIs**. Keep the default scopes of **openid**, **email**, **profile**, and **offline\_access** selected.
* **Client secret**: Enable the option to generate a client secret, as Sigma requires this for secure connection.
* **Refresh token time-to-live (TTL)**: This value determines how long users can be logged into Sigma before being prompted to log in again. Set a value consistent with your organization's security policies. To avoid frequent interruptions for your users, Sigma Computing recommends a TTL value of 90 days. To avoid disruption to scheduled exports, do not set a value lower than 7 days.

Record your client ID and client secret. You need these values for the Sigma configuration.

### Determine the metadata URI for your Databricks Authorization Server

Determine the metadata URI that Sigma will require to complete the OAuth configuration. The metadata URI includes the unique ID for your Databricks account. For information about how to retrieve your Databricks account ID, see [Locate your account ID](https://docs.databricks.com/aws/en/admin/account-settings/#locate-your-account-id) in the Databricks documentation.

Form your metadata URI using your Databricks account ID. The format for your metadata URI required depends on your environment and configurations:

* Azure: `https://accounts.azuredatabricks.net/oidc/accounts/<your-databricks-account-id>/.well-known/openid-configuration`
* AWS:
  + If your organization uses workspace-level legacy SSO, and has [unified login](https://docs.databricks.com/aws/en/security/auth/single-sign-on/unified-login) enabled: `https://<server_hostname>/oidc/.well-known/openid-configuration`
  + If your organization does not use workspace-level legacy SSO, or does not have [unified login](https://docs.databricks.com/aws/en/security/auth/single-sign-on/unified-login) enabled: `https://accounts.cloud.databricks.com/oidc/accounts/<your-databricks-account-id>/.well-known/openid-configuration`

Updated 3 days ago

---

Related resources

* [Configure OAuth](/docs/configure-oauth)
* [Configure OAuth authentication for your Sigma organization](/docs/configure-oauth-authentication-for-your-sigma-organization)
* [Configure a Sigma OAuth application](/docs/configure-a-sigma-oauth-application)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Configure a Sigma OAuth application in an external IdP](#configure-a-sigma-oauth-application-in-an-external-idp)
  + - [High-level overview](#high-level-overview)
    - [Step 1: Create an app for Sigma in your IdP](#step-1-create-an-app-for-sigma-in-your-idp)
    - [Step 2: Add OAuth users to your app](#step-2-add-oauth-users-to-your-app)
    - [Step 3: Create an OAuth authorization server](#step-3-create-an-oauth-authorization-server)
    - [Step 4: Add an access policy for the authorization server](#step-4-add-an-access-policy-for-the-authorization-server)
    - [Step 5: Create a security integration (Snowflake only)](#step-5-create-a-security-integration-snowflake-only)
  + [Configure a custom OAuth application for Sigma in Databricks Authorization Server](#configure-a-custom-oauth-application-for-sigma-in-databricks-authorization-server)
  + - [Determine the metadata URI for your Databricks Authorization Server](#determine-the-metadata-uri-for-your-databricks-authorization-server)