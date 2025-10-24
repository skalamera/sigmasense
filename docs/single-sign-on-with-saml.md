# Set up single sign-on with SAML

# Set up single sign-on with SAML

Sigma supports single sign-on (SSO) with SAML. SAML SSO can provide a more streamlined and secure sign in experience for users, by allowing users to sign in with one set of credentials - minimizing the opportunity for credential theft.

This document covers the following: an introduction to SAML, how to configure SAML SSO for your Sigma organization, and the behavior of a user’s account type and/or teams when configuring SAML.

## System and user requirements

* You must be assigned the Admin [account type](/docs/create-and-manage-account-types) to configure SAML SSO for your organization.
* An identity provider (IdP).

## Understanding SSO and SAML

#### What is SAML?

Security Assertion Markup Language (SAML) is a widely used security protocol. It provides secure authentication and authorization between a service provider (SP) and an identity provider (IdP).

A service provider is the web application that you would like to gain access to, such as Sigma.

An identity provider is a software service that performs authentication related services (SAML, account status verification, account attribute declaration). Examples of IdPs include Okta and Azure Entra ID.

#### Service Provider (SP) and Identity Provider (IdP) Authentication

By default, Sigma supports SP-initiated authentication via the Sigma login page. In order to additionally use IdP-initiated authentication from the IdP's console you must provide your IdP with a RelayState.

> 📘
>
> ### If your organization is currently using email/password authentication, all members of your organization will retain access to their assets after transitioning to SAML SSO authentication, as long as their email addresses remain the same.

## Configure SAML SSO for your Sigma Organization

Follow the steps below to configure SAML SSO for your Sigma organization. This is a multi-stage process that involves SAML configuration in both the IdP and Sigma:

1. [Configure your identity provider](/docs/single-sign-on-with-saml#step-1-configure-your-identity-provider)
   1. [Confirm your cloud service provider](/docs/single-sign-on-with-saml#confirm-your-cloud-service-provider)
   2. [Configure your IdP](/docs/single-sign-on-with-saml#configure-your-idp)
2. [Configure SAML SSO in Sigma](/docs/single-sign-on-with-saml#step-2-configure-saml-sso-in-sigma)

## Step 1: Configure your identity provider

### Confirm your cloud service provider

Sigma organizations can be hosted on Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP). Your IdP configuration will differ based on your cloud provider.
Before configuring SAML SSO, please confirm your organization's cloud provider:

* Go to **Administration** > **Account** > **General Settings**. Your cloud provider is listed in the **Site** section.

### Configure your IdP

#### Configure your IdP using an existing application

If your company uses Okta and your cloud platform is AWS (US West regions only)/GCP, you have the option to use a pre-configured application to set up SSO access to Sigma. See [Okta’s Sigma on AWS](https://www.okta.com/integrations/sigma-on-aws/)  or [Sigma on GCP](https://www.okta.com/integrations/sigma-on-gcp/) integrations. For more information on setting up SAML for specific IdPs, see the Sigma Community post on [Guidelines For Configuring OAuth and SAML Authentication](https://community.sigmacomputing.com/t/guidelines-for-configuring-oauth-and-saml-authentication/5427).

> 📘
>
> ### If using the GCP gallery SAML app, the following changes must be made:
>
> * For **Entity ID**, add a “/2” after “saml2”. Your Entity ID should be `https://api.sigmacomputing.com/api/v2/saml2/2/metadata.xml`, not `https://api.sigmacomputing.com/api/v2/saml2/metadata.xml`.
> * For **ACS URL**: If your organization is hosted on AWS, add in `aws-` before `api`. For example, `https://aws-api.sigmacomputing.com/api/v2/saml2/assert`.

#### Configure your IdP manually

If your company uses a different IdP, follow the documentation provided by that IdP on how to set up a SAML application. You can configure the required fields manually, or by importing them using the following Sigma metadata file:

```
https://{{prefix}}.sigmacomputing.com/api/v2/saml2/2/metadata.xml
```

The`{{prefix}}` must be replaced with the cloud prefix specific to your cloud provider, listed in the table below.

| Deployment | Prefix |
| --- | --- |
| GCP | `api` |
| AWS-US (West) | `aws-api` |
| AWS-US (East) | `api.us-a.aws` |
| AWS-CA | `api.ca.aws` |
| AWS-EU | `api.eu.aws` |
| AWS-UK | `api.uk.aws` |
| AWS-AU | `api.au.aws` |
| Azure-US | `api.us.azure` |
| Azure-EU | `api.eu.azure` |
| Azure-UK | `api.uk.azure` |

If you are manually entering the remaining configurations, there are several ways you can find the relevant configuration values:

* *From the Administration portal:* Go to **Administration** > **Authentication** > **Edit**, and your configuration values will be available under **Authentication Method & Options**. Your prefix will already be included in the values.
* *From the table below:* See the table below for more information. You will have to manually include your prefix.

| Field | Value |
| --- | --- |
| **Audience URI** | `https://{{prefix}}.sigmacomputing.com/api/v2/saml2/2/metadata.xml` |
| **Assertion consumer service, Consumer, Login or SSO URL** | `https://{{prefix}}.sigmacomputing.com/api/v2/saml2/assert` |
| **NameID format** | `email ("urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress")` |
| **Attributes** | **“fullName”** or **“firstName”**, **“lastName”**  To uniquely identify your SAML attributes and avoid overlap with other app configurations, use the Sigma namespace prefix (`https://schema.sigmacomputing.com/2025/01/claims`) for the “userRole” and “userGroups” attributes. For example, the “userRole” attribute name would look like “`https://schema.sigmacomputing.com/2025/01/claims/userRole`".  **"userRole"**  The userRole attribute can be set to `pro`, `lite`, `essential`, `view`, `act`, `analyze`, `build`, or `admin` (default account types). It also supports `viewer` and `creator` (former default account types).  If userRole isn't set in your IdP , `lite` is applied to new users by default. This can be helpful if a non-Sigma user in your organization signs up to view a shared dashboard. You can change this role in Sigma. See the [License and account type overview](/docs/license-and-account-type-overview).  This attribute is case-sensitive. When configuring default account types (Admin, View, Act, Analyze, Build), the value indicated should be lower case (e.g. `essential`). Other account type configurations are also case-sensitive, and the value set in your IdP must match the value in Sigma exactly, or errors may occur when trying to provision users.  If userRole isn't set in your IdP, existing users will keep their current account type.  It is possible to pass in multiple userRole values. The first valid account type in the list of userRole values will be assigned.  **"userGroups"**  Team assignments for a SAML user are automatically synced upon logging into Sigma, provided the Sigma [team name](/docs/manage-teams) matches the name in your IdP.  Changes to teams created in your IdP that do not match a Sigma team will be ignored. For example, if a user belongs to team “A” in your IdP but there is no team “A” in Sigma, they will not be added.  Additionally, users will be removed from any current Sigma teams that do not show up in the userGroups list. For example, a user belongs to teams “X”, “Y” and “Z” in Sigma. If they log in with a SAML request that says their userGroups are “X” and “Y”, they will be removed from team “Z” in Sigma.  See [Behavior of "userRole" and "userGroups" attributes](/docs/single-sign-on-with-saml#behavior-of-userrole-and-usergroups-attributes). |
| **RelayState** | `https://app.sigmacomputing.com/<YOUR-ORG>/finish-login`  Note that if you rename your Sigma organization, you will need to update your RelayState URL. Your organization's name can be accessed and edited from **Administration** > **Account** > **General Settings** > **Site**. |
| **Validator** | For Azure/GCP/AWS: `<prefix>.sigmacomputing.com/api/v2/saml2/assert` |

## Step 2: Configure SAML SSO in Sigma

To configure SAML SSO in Sigma:

1. Go to **Administration** > **Authentication**.
2. Select **Edit** in **Authentication Method and Options**.
3. Select **SAML or password** from the **Authentication Method** dropdown menu.

> 💡
>
> ### When transitioning authentication methods for your Sigma organization from basic authentication to SAML, the best practice is to transition first to the **SAML or password** option rather than directly to requiring SAML only login for all users. With the authentication method set to **SAML or password**, you retain the ability to log in with a password during the transition to your IdP based login, ensuring that you are not locked out during the configuration change. Once you have confirmed that users are able to log in using SAML, you can transition to SAML only login.

4. Enter your **Identity Provider Login URL**. This can be found in your IdP and may be listed as your SAML 2.0 Endpoint (HTTP).
5. Enter your **Identity Provider X.509 Certificate**. This can be found in your IdP.
6. (Optional) In the **Export Authentication** field, click **Edit** to allow exports to approved domains.
7. Select **Save**.
8. Test your SAML configuration by logging out and logging back into Sigma. Your organization’s login page should now display a "Log in with SSO" prompt.
9. After testing to ensure users are able to log in using SAML, you can update your selection in the **Authentication Method** dropdown to choose the **SAML** option, which enforces SAML login for all users.

## Update your SAML certificate in Sigma

To avoid losing access to your Sigma organization, ensure your SAML certificate is updated before it expires. You can view your SAML certificate’s expiration date in your IdP. Sigma will send you email notifications as this expiration date approaches at 30, 14, 7, and 1 days till your certificate expiration.

To update your certificate in Sigma:

1. Go to **Administration** > **Authentication**.
2. Select **Edit** in **Authentication Method and Options**.
3. In the **Identity Provider X.509 Certificate** field, enter the new certificate from your IdP.
4. Select **Save**.

> 📘
>
> ### It's recommended that you also configure certificate expiration notifications in your IdP.

If your SAML certificate has already expired and you are unable to sign in to your Sigma organization, contact your CSM or AE for assistance.

## Behavior of "userRole" and "userGroups" attributes

> 🚧
>
> ### If you make account type or team membership assignments in your IdP, do not change these assignments in Sigma. Configurations set in your IdP take precedence over any configurations in Sigma. For example, if you change a user's role in Sigma, this role will not be written back to your IdP. The next time you log into Sigma, the user’s role will be reset to their IdP declared role.

The expected behavior of the "userRole" and "userGroups" attributes depends on how they are configured in your IdP:

| Scenario | Behavior |
| --- | --- |
| No userRole is set in IdP, and no account type is set in Sigma. | The account type in Sigma defaults to `lite`. |
| No userGroups set in IdP, but team assignments are set in Sigma. | The team assignments in Sigma are preserved. |
| The userGroups in IdP and team assignments in Sigma do not match. | Group membership is recognized by name matching. Group assignments in your IdP that do not have a corresponding team in Sigma will be ignored, and users will be removed from any prior existing groups not included in the assertion.  For example, teams “A”, “B” and “C” exist in Sigma, and a user is assigned to team “B” and “C”. The userGroups assignment in your IdP for this user is set to “B”, “C” and “D”. The following will occur in Sigma: the user will be removed from team “A”, remain in team “B”, added to team “C”, and the “D” assignment will be ignored. |

Updated 3 days ago

---

Related resources

* [Manage Authentication](/docs/manage-authentication)
* [Manage Users and Teams with SCIM](/docs/manage-users-and-teams-with-scim)
* [How to Configure SAML 2.0 for [Okta and] Sigma on GCP (Okta documentation)](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Sigma.html)
* [How to Configure SAML 2.0 for [Okta and] Sigma on AWS (Okta documentation)](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Sigma-AWS)
* [Configure [Azure and] Sigma Computing for automatic user provisioning (Azure documentation)](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/sigma-computing-provisioning-tutorial)
* [Custom Session Timeouts for Okta](/docs/custom-session-timeouts-for-okta)
* [OAuth with Snowflake](/docs/oauth-with-snowflake)
* [Single Sign-On with Sigma and Okta (QuickStarts)](https://quickstarts.sigmacomputing.com/guide/administration_sso_okta/index.html?_gl=1*3jrgtl*_ga*ODkzMjkyNDY1LjE3MDAwMDU1NzM.*_ga_PMMQG4DCHC*MTcwMTMwMDg3Ni4yOC4xLjE3MDEzMDEzMDEuMzEuMC4w)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Understanding SSO and SAML](#understanding-sso-and-saml)
  + [Configure SAML SSO for your Sigma Organization](#configure-saml-sso-for-your-sigma-organization)
  + [Step 1: Configure your identity provider](#step-1-configure-your-identity-provider)
  + - [Confirm your cloud service provider](#confirm-your-cloud-service-provider)
    - [Configure your IdP](#configure-your-idp)
  + [Step 2: Configure SAML SSO in Sigma](#step-2-configure-saml-sso-in-sigma)
  + [Update your SAML certificate in Sigma](#update-your-saml-certificate-in-sigma)
  + [Behavior of "userRole" and "userGroups" attributes](#behavior-of-userrole-and-usergroups-attributes)