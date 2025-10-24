# Manage authentication

# Manage authentication

Sigma supports a variety of authentication methods, such as username and password authentication, or SAML or OAuth single sign-on methods. If you use password authentication, two-factor authentication is enabled by default. For more information, see [Mandatory two-factor authentication for accounts](/docs/mandatory-two-factor-authentication-for-accounts).

## User requirements

To manage authentication methods and options for your organization, you must be assigned the **Admin** [account type](/docs/user-account-types).

## Authentication methods

Password
:   Sigma prompts new organization members to create a unique password for their Sigma account that is at least 8 characters long and not a commonly-used or similar password.

SAML
:   Sigma authenticates organization member accounts through the single sign-on (SSO) protocol you provide. See [SSO with SAML](https://help.sigmacomputing.com/docs/single-sign-on-with-saml).

SAML or Password
:   Organization members authenticate with either SSO or a unique password.

OAuth
:   Sigma authenticates organization member accounts through OAuth single sign-on (SSO).

OAuth or Password
:   Sigma authenticates organization member accounts through OAuth single sign-on (SSO) or a unique password.

> 🚧
>
> If you change the authentication method from password to SSO or OAuth, user emails must exactly match for the user to maintain their account.

## Manage authentication method and options

To manage the authentication method and options for your organization, do the following:

1. Open your Admin Portal by selecting **Administration** in the user menu at the top right of your screen.
2. Select **Authentication** in the left navigation panel.
3. Under **Authentication Method & Options**, click **Edit**.
4. For **Authentication Method**, select an authentication method from the dropdown menu.

   * If you select **SAML** or **SAML or password**, see [Single Sign On with SAML](/docs/single-sign-on-with-saml).
   * If you select **OAuth** or **OAuth or password**, see [Configure OAuth](/docs/configure-oauth).
   * If you select **Password**, continue to follow these steps.
5. [optional] Users can enable app based authentication for their Sigma account from their user profile page. See [App based authentication for users](/docs/app-based-authentication-for-users).
6. [optional] To enable guest user accounts, turn on the toggle for **Allow Guest Access**. See [Guest User Accounts](/docs/guest-user-accounts).
7. [optional] To customize how frequently users are prompted to re-authenticate, set a **Session Length in Hours**. This setting only applies to users logging in with SAML or a password.
8. [optional] To authorize anyone with an email from one or more domains to create an account in your organization without a personalized invite, specify one or more comma-separated email domains under **Company Domain Signup**. For more details, see [Company domain signup](#company-domain-signup).
9. After configuring authentication for your organization, click **Save**.

### Company domain signup

When you use an authentication method that supports **Password** authentication, you can choose to add domains to an allowlist. By default, new users can only [sign up when they receive an invitation](/docs/invite-people-to-your-organization). Adding your company's email domain lets anyone with a company email address create a Sigma account without a personalized invitation.

Sigma prompts new users to enter their email from a domain on the allowlist. After confirming their email, the user can create an account and register as a Sigma user.

## Admin-initiated password reset

If you are assigned the **Admin** [account type](/docs/user-account-types) and your organization is using a password-based authentication method, you can send password reset emails to users in your organization:

1. In the Admin Portal, click the **People tab**.
2. On the **Members** tab, search or browse to locate the user. You can search by name or email address.
3. For the user, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Reset user password**.

   Sigma sends a reset password email to the user. The email informs the user that the organization admin has requested that they reset their password.

   ![Admin page showing the menu options.](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/Users/Invites/Admin+init.png)

### Bulk password reset

If you are assigned the **Admin** [account type](/docs/user-account-types) and your organization is using a password-based authentication method, you can initiate a password reset for multiple users.

1. In the Admin Portal, click the **People tab**.
2. On the **Members** tab, for each user, select the checkbox to the left of their name.
3. In the toolbar, click **Reset password**.
4. Review your selection and click **Confirm**.

   The selected users receive an email informing them that the admin has requested that they reset their password.

Updated 3 days ago

---

Related resources

* [Single Sign-On with SAML](/docs/single-sign-on-with-saml)
* [Invite people to your organization](/docs/invite-people-to-your-organization)
* [User account types](/docs/user-account-types)
* [Single Sign-On with Sigma and Okta (QuickStarts)](https://quickstarts.sigmacomputing.com/guide/administration_sso_okta/index.html?_gl=1*radife*_ga*ODkzMjkyNDY1LjE3MDAwMDU1NzM.*_ga_PMMQG4DCHC*MTcwMTMwMDg3Ni4yOC4xLjE3MDEzMDEyMDIuNDIuMC4w#0)
* [Configure OAuth](/docs/configure-oauth)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Authentication methods](#authentication-methods)
  + [Manage authentication method and options](#manage-authentication-method-and-options)
  + - [Company domain signup](#company-domain-signup)
  + [Admin-initiated password reset](#admin-initiated-password-reset)
  + - [Bulk password reset](#bulk-password-reset)