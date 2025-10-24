# Using multiple identity providers for your Sigma organization (Beta)

# Using multiple identity providers for your Sigma organization (Beta)

> 🚩
>
> This documentation describes one or more private beta features that are in development. Beta features are subject to quick, iterative changes; therefore the current user experience in the Sigma service can differ from the information provided in this page.
>
> This page should not be considered official published documentation until Sigma removes this notice and the beta flag on the corresponding feature(s) in the Sigma service. For the full beta feature disclaimer, see [Beta features](/docs/sigma-product-releases#beta-features).
>
> If you are interested in joining a limited test group and enabling this feature in your Sigma organization, [contact Support](/docs/sigma-support) or reach out to your Account Executive.

Sigma supports using multiple identity providers (IdPs) to sign into your Sigma organization, providing greater flexibility for organizations. For example, multiple IdPs can support scenarios where different departments in a company use different IdPs, or where contract and full-time employees use different IdPs.

This document provides an overview of using multiple IdPs, considerations for organizations with existing organization-level OAuth configurations, how to enable multiple IdPs for your Sigma organization, and best practices when using multiple IdPs.

## About using multiple IdPs for authentication

Connections that rely on org-level OAuth will no longer function unless updated to use connection-level OAuth. See [Considerations for existing organizations using organization-level OAuth](/docs/using-multiple-identity-providers-for-your-sigma-organization#considerations-for-existing-organizations-using-organization-level-oauth).

## Enabling multiple identity providers for your Sigma organization

If you would like to enable multiple identity providers for an existing Sigma organization, please contact [Sigma support](/docs/sigma-support).

When you enable the feature and add new authentication methods, you must configure each method separately.

## Considerations for existing organizations using organization-level OAuth

When you enable multiple IdPs for your organization, you can no longer use existing organization-level OAuth configurations to sign in to connections. If you would like to use the same OAuth application you use for org-level authentication to authenticate into specific connections, you will need to configure this at the connection level.

> 📘
>
> ### Configuring a unique OAuth application to authenticate users to a connection – in other words, opting to not re-use the OAuth configuration you use at the organization level – is in public beta.
>
> This documentation describes a public beta feature and is under construction. This documentation should not be considered part of our published documentation until this notice, and the corresponding Beta flag on the feature in Sigma, are removed. As with any beta feature, the feature discussed below is subject to quick, iterative changes. The latest experience in the Sigma service may differ from the contents of this document.
>
> Beta features are subject to the disclaimer on [Beta features](/docs/sigma-product-releases#beta-features).

To configure OAuth at the connection level once multiple IdPs have been enabled for your organization:

* For Snowflake connections: See [Connect to Snowflake with OAuth](/docs/connect-to-snowflake#connect-to-snowflake-with-oauth). If you would like to use the same OAuth application you use for org-level authentication to authenticate into your connection, you can copy the OAuth Features (such as **Metadata URI**, **Client ID**, etc.) being used for the org-level OAuth config.  
  If you are using OAuth to authenticate users to your Sigma organization with an external IdP, and do not have multiple identity providers enabled for your organization, you have the option to re-use your organization-level OAuth configuration for this connection. To re-use the existing OAuth configuration, turn on the feature toggle next to Use organization-level OAuth configuration. If you turn on this toggle, skip to step 3.
  + For Databricks connections: See [Configure OAuth features in Connect to Databricks](/docs/connect-to-databricks#configure-oauth-features). If you would like to use the same OAuth application you use for org-level authentication to authenticate into your connection, you can copy the OAuth Features (such as **Metadata URI**, **Client ID**, etc.) being used for the org-level OAuth app.  
    If you are using OAuth to authenticate users to your Sigma organization with Databricks Authorization Server, and your organization does not have multiple identity providers (IdPs) enabled, you have the option to re-use that OAuth configuration for this connection. To do so, enable the toggle next to **Use organization-level OAuth configuration**. If you enable this toggle, skip to step 3.  
    If you do not use OAuth as your authentication method for your Sigma organization, or have multiple identity providers enabled for your organization, this option is not present. If you use an external IdP (Okta, Microsoft Entra ID, Auth0, or PingIndentity), do not enable this toggle because Databricks does not support authenticating using an external IdP.

> 📘
>
> ### This process should be repeated for every connection you would like to use the OAuth application for.

## Best practices when using multiple IdPs

Best practices when using multiple IdPs include:

* When transitioning authentication methods, it is recommended to keep a password-based authentication option enabled. This ensures you aren’t locked out of your Sigma organization if configuration issues arise.
* For organizations using [SCIM](/docs/manage-users-and-teams-with-scim), ensure that any one user is provisioned by only one IdP at a time. Multiple SCIM provisioning configurations that use the same token are supported, but users should not be provisioned by more than one IdP as this is likely to cause access conflicts.
* Ensure that SCIM provisioning is not used for the same user across multiple IdPs. Users should be provisioned by a maximum of one IdP.
* Organizations with multiple identity providers enabled cannot use organization-level OAuth to log in to connections. You will have to create a unique OAuth configuration at the connection level. See [Considerations for existing organizations using organization-level OAuth](/docs/using-multiple-identity-providers-for-your-sigma-organization#considerations-for-existing-organizations-using-organization-level-oauth).

Updated 3 days ago

---

[About Sigma](/docs/about-sigma)

* [Table of Contents](#)
* + [About using multiple IdPs for authentication](#about-using-multiple-idps-for-authentication)
  + [Enabling multiple identity providers for your Sigma organization](#enabling-multiple-identity-providers-for-your-sigma-organization)
  + [Considerations for existing organizations using organization-level OAuth](#considerations-for-existing-organizations-using-organization-level-oauth)
  + [Best practices when using multiple IdPs](#best-practices-when-using-multiple-idps)