# Configure OAuth authentication for your Sigma organization

# Configure OAuth authentication for your Sigma organization

This document guides you through configuring Sigma to authenticate your organization member accounts through OAuth single sign-on (SSO).

## Prerequisite

* You must have already configured a Sigma OAuth application in your IdP. If you have not yet completed this prerequisite step, see [Configure a Sigma OAuth application](/docs/configure-a-sigma-oauth-application).

## Requirements

* You must be assigned the Admin [account type](/docs/user-account-types) to manage authentication for your Sigma organization.

## Configure OAuth as the authentication method for your Sigma organization

In Sigma, configure your organization to use OAuth as the authentication method.

> 💡
>
> ### When transitioning authentication methods for your Sigma organization from basic authentication to OAuth, the best practice is to transition first to the **OAuth or password** option rather than directly to requiring OAuth only login for all users. With the authentication method set to **OAuth or password**, you retain the ability to log in with a password during the transition to your IdP based login, ensuring that you are not locked out during the configuration change. Once you have confirmed that users are able to log in using OAuth, you can transition to OAuth only login.

This configuration requires the values for three fields you obtained when configuring your Sigma OAuth application in your IdP.

* Client ID and Client Secret:
  + If you are using an external IdP, you obtained these values here: [Step 1: Create an app for Sigma in your IdP](/docs/configure-a-sigma-oauth-application#step-1-create-an-app-for-sigma-in-your-idp).
  + If you are using Databricks as your IdP, you obtained these values here: [Configure a custom OAuth application for Sigma in Databricks Authorization Server](/docs/configure-a-sigma-oauth-application#configure-a-custom-oauth-application-for-sigma-in-databricks-authorization-server).
* Metadata URI:
  + If you are using an external IdP, you obtained this value here: [Step 3: Create an authorization server](/docs/configure-a-sigma-oauth-application#step-3-create-an-oauth-authorization-server).
  + If you are using Databricks as your IdP, you obtained this value here: [Determine your metadata URI for your Databricks Authorization Server](/docs/configure-a-sigma-oauth-application#determine-the-metadata-uri-for-your-databricks-authorization-server).

1. Go to **Administration > Authentication**.
2. In the **Authentication Method and Options** section, locate the **Authentication Method** setting and click **Edit**.
3. In the **Authentication Method & Options** page, configure OAuth authentication:
   1. In the **Authentication Method** dropdown, select the **OAuth** or **OAuth or password** options.
   2. To enable guest users to access permitted content, turn on the **Allow Guest Access** switch. Guest users must have user accounts in your data platform and be added as OAuth users in your IdP in order to access Sigma.
   3. In the **Metadata URI** field, enter the OAuth metadata URI.
   4. In the **Client ID** field, enter the client ID from your OAuth application.
   5. In the **Client Secret** field, enter the client secret from your OAuth application.
      After you enter and save this value, Sigma does not display it.
   6. Click **Save** to apply the changes.
4. Test your OAuth configuration by logging out and logging back into Sigma. Your organization’s login page should now display a "Log in with SSO" prompt.
5. After testing to ensure users are able to log in using OAuth, you can update your selection in the **Authentication Method** dropdown to choose the **OAuth** option, which enforces OAuth login for all users.

Updated 3 days ago

---

Related resources

* [Configure OAuth](/docs/configure-oauth)
* [Configure a Sigma OAuth application](/docs/configure-a-sigma-oauth-application)

* [Table of Contents](#)
* + [Prerequisite](#prerequisite)
  + [Requirements](#requirements)
  + [Configure OAuth as the authentication method for your Sigma organization](#configure-oauth-as-the-authentication-method-for-your-sigma-organization)