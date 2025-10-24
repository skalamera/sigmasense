# Mandatory two-factor authentication for accounts

# Mandatory two-factor authentication for accounts

Starting December 11, 2024, two-factor authentication (2FA) via email is enabled by default for all new and existing Sigma users that use password-based authentication.

This change protects against security threats. 2FA enhances security by adding an extra layer of protection to customer accounts.

As this is a mandatory requirement, you cannot apply for an exception to 2FA. After 2FA is enabled, it cannot be disabled.

There is no additional cost associated with enabling 2FA.

### When will this change take place?

The mandatory 2FA via email for password-based users is enforced starting **December 11, 2024**.

### Who is affected by this change?

All customers currently using password-based authentication are affected. Users with SAML or OAuth authentication methods are not affected.

Sigma automatically enables 2FA via email for all users with password-based accounts. During the sign in process, after entering their existing password, users receive a 2FA code sent to their registered email address. This code must be entered to complete the sign in process.

For password-based users, the mandatory 2FA process is available through email or through [app based authentication](/docs/app-based-authentication-for-users).

Organizations using SAML or OAuth may have other 2FA options available, depending on their organization infrastructure. If you want to switch from password-based authentication to SAML or OAuth, your organization's IT team must configure and enable SAML or OAuth in your environment. See [Manage authentication](/docs/manage-authentication) for more information. Contact [Sigma Support](/docs/sigma-support) for additional assistance.

### Are guest and embed users affected?

Embed users are not affected as they cannot to sign in to Sigma (the secure embed URLs use client ID and client secret for access).

If your organization has enabled guest users, they are required to sign in with 2FA. To access your authentication settings, see [Manage authentication method and options](/docs/manage-authentication#manage-authentication-method-and-options).

### Effects on organizations using SAML or OAuth

Authentication methods using SAML or OAuth only are not affected by this change. Any user account configured with a password option (such as [SAML or Password and OAuth or Password](/docs/manage-authentication#authentication-methods)) has 2FA enabled by default. If using the password option during sign-in, you will need to complete the email 2FA process.

Sigma encourages the use of stronger authentication mechanisms, such as SAML and OAuth, but they are not required at this time.

### How will this change affect the user experience and API access?

For users who continue using password-based authentication, the only change is the need to enter a 2FA code sent via email. For organizations using SAML or OAuth, there is no change in the login experience.

This change does not impact API access. The [authentication process](/reference/token) for our public API does not include 2FA.

### Troubleshooting

#### What if users forget their 2FA email or are locked out?

For further assistance, contact [Sigma Support](/docs/sigma-support) or your dedicated Sigma Account Executive.

#### Who can I contact for support or additional questions?

For further assistance, please reach out to Sigma’s support team or your dedicated Sigma account representative.

#### How will 2FA affect browser-based automation accounts (such as Cypress or Selenium testing accounts)?

These accounts may not be able to complete the 2FA process required to access Sigma. For automated testing, we recommend using the [Sigma REST API](/reference/get-started-sigma-api).

Updated 3 days ago

---

[Set up single sign-on with SAML](/docs/single-sign-on-with-saml)[Manage users and teams with SCIM](/docs/manage-users-and-teams-with-scim)

* [Table of Contents](#)
* + [When will this change take place?](#when-will-this-change-take-place)
  + [Who is affected by this change?](#who-is-affected-by-this-change)
  + [Are guest and embed users affected?](#are-guest-and-embed-users-affected)
  + [Effects on organizations using SAML or OAuth](#effects-on-organizations-using-saml-or-oauth)
  + [How will this change affect the user experience and API access?](#how-will-this-change-affect-the-user-experience-and-api-access)
  + [Troubleshooting](#troubleshooting)
  + - [What if users forget their 2FA email or are locked out?](#what-if-users-forget-their-2fa-email-or-are-locked-out)
    - [Who can I contact for support or additional questions?](#who-can-i-contact-for-support-or-additional-questions)
    - [How will 2FA affect browser-based automation accounts (such as Cypress or Selenium testing accounts)?](#how-will-2fa-affect-browser-based-automation-accounts-such-as-cypress-or-selenium-testing-accounts)