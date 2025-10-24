# Use custom account types with your IdP

# Use custom account types with your IdP

If your organization uses an identity provider (IdP) to centrally manage permissions, you must assign users to specific Sigma account types in the IdP.

This document explains how to use and assign [*custom* account types](/docs/create-and-manage-account-types) in your IdP.

> 📘
>
> ### The procedures detailed in this document apply to Okta and Azure IdPs only.

## Requirements

* Admin access to Sigma
* Administrator access to your IdP
* SCIM configured for Sigma and your IdP; see [Manage Users and Teams with SCIM](/docs/manage-users-and-teams-with-scim).

## General Instructions

1. Log in to Sigma and create a custom account type.
2. Log in to your IdP.
3. Create a new user type that matches your custom account type in Sigma. The identifier should be identical to its corresponding account type in Sigma.  
   After saving, you should now be able to assign existing or new users to your account type.

> 🚧
>
> ### The user type attribute is case-sensitive. When configuring default account types (Admin, Lite, Essential, Pro), the value indicated should be lower case (e.g. "essential"). Other account type configurations are also case-sensitive, and the value set in your IdP must match the value in Sigma exactly, or errors may occur when trying to provision users.

## Using Custom Account Types with Okta

1. Log in to Sigma and create a custom account type.
2. Log in to Okta and open your Sigma application.
3. Open the **Provisioning** tab.
4. Click the **Go to Profile Editor** button to open the **Profile Editor** page.
5. Click the **edit** button for the **User Type** attribute.
6. Under **Attribute members,** click **Add Another**.
7. Enter a **Display name** and **Value**. These identifiers must match the name of the custom account type in Sigma.
8. Click **Save Attribute**.  
   You can now assign this user type to new and existing users via your application’s **Assignments** tab.

## Using Custom Account Types with Azure

1. Log in to Sigma and create a custom account type.
2. Log in to Azure and open your Sigma application.  
   *Azure Active Directory -> App Registrations -> All Applications -> Search for and select your application.*
3. Go to the **App Roles** page.
4. Click **Create app role** to create a new app role.After the role is created, it should appear on the users / groups assignments page and can be assigned.

Updated 3 days ago

---

Related resources

* [Create and manage account types](/docs/create-and-manage-account-types)
* [Use Custom Account Types with your IdP](/docs/use-custom-account-types-with-your-idp)
* [Manage Users and Teams with SCIM](/docs/manage-users-and-teams-with-scim)
* [Manage Users and Teams with SCIM and Okta](/docs/manage-users-and-teams-with-scim-and-okta)
* [Configure [Azure and] Sigma Computing for automatic user provisioning (Azure documentation)](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/sigma-computing-provisioning-tutorial)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [General Instructions](#general-instructions)
  + [Using Custom Account Types with Okta](#using-custom-account-types-with-okta)
  + [Using Custom Account Types with Azure](#using-custom-account-types-with-azure)