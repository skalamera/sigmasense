# Create and manage account types

# Create and manage account types

> 🚩
>
> ### If your organization utilizes the Lite/Essential/Pro license model, refer to [this document](/docs/create-and-manage-account-types-2024).

Account types enable you to manage user access to specific features and capabilities available through each license tier. Default and custom account types add flexibility and scalability to Sigma’s access control methodology, allowing your organization to adapt to ongoing changes in your licensed user base and user requirements.

This document introduces default and custom account types and explains how to create, manage, and assign account types to organization users. For more information about account types as they relate to the licensing model, see [License and account type overview](/docs/account-type-and-license-overview).

## User requirements

To create and manage account types and user assignments, you must be assigned the Admin account type.

## Default and custom account types

Sigma supports default and custom account types that allow you to enable or disable any combination of permissions within the constraints of your organization’s license tiers.

For a comparison of available account type permissions by tier, see [Account type permission availability matrix](/docs/account-type-and-license-overview#account-type-permission-availability-matrix).

### Default account types

There are five default account types built into your organization: *View*, *Act*, *Analyze*, *Build*, and *Admin*. These account types reflect Sigma's [license tiers](/docs/account-type-and-license-overview#license-tiers) to support five standard roles or levels of access.

| Default account type | Description |
| --- | --- |
| View | Enables all *View* permissions.  *Recommended for users who need access to prepared data and insights.* |
| Act | Enables all *View* and *Act* permissions.  *Recommended for users who need to input and update data* |
| Analyze | Enables all *View*, *Act*, and *Analyze* permissions.  *Recommended for users who require more deep-dive capabilities without building workbooks themselves.* |
| Build | Enables all *View*, *Act*, and *Analyze* permissions and a selection of *Build* permissions.  *Recommended for users who model, transform, and analyze data.* |
| Admin | Enables all *View*, *Act*, *Analyze*, and *Build* permissions, plus administrative privileges.  *Recommended for system administrators who manage organization settings and users.* |

### Custom account types

Custom account types allow you to create additional roles and levels of access. You can enable and disable any combination of permissions to suit the needs of your organization users.

## Create and manage account types

The following procedures demonstrate how to create, edit, and delete account types. These tasks involve the account type details and permissions only. For information about assigning account types to users, see [View and manage account type assignments](#view-and-manage-account-type-assignments) in this document.

### Create a new custom account type

1. Go to **Administration** > **Account types**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Account types**.
2. In the **Account types** page, click **Create new account type**.

   ![Image of the Account types page with cursor hovering on "Create new account type" button.](https://files.readme.io/1cbcbe2e8b4cb9ff997fbf09322aae19681844ce5fe6696681e78e5c3e30c217-image.png)
3. In the **New account type** page, configure the custom account type:

   1. In the **Name** field, enter a unique name to identify the account type.
   2. In the **Description** field, enter a description about the account type (for example, context about its permissions or user role).
   3. In the permissions table, select the checkbox for each permission you want to enable. Clear the checkbox for each permission you want to disable.

      > 💡
      >
      > ### To select all permissions associated with the *View*, *Act*, *Analyze*, or *Build* license tier, select the checkbox in the applicable column header.

      Sigma automatically assigns a license to the account type based on the highest license tier of the enabled permissions. You can view the assigned license next to the account type name and description.

      ![Image showing an example new account type creation screen focused on the area under the Create button that shows what the license of the account type will be.](https://files.readme.io/073c24884346745a55c5d150d70aae71e4726bb462e0d943554a218d9e207642-image.png)
   4. Click **Create** to save the new account type.

### Edit an existing account type

1. Go to **Administration** > **Account types**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Account types**.
2. In the **Account types** page, search or browse the list of account types and select the one you want to edit.

   > 📘
   >
   > ### You cannot edit the default *Admin* account type.
3. In the account type’s overview, click **Edit**.

   ![Image of a custom account type summary screen with the lists of feature permissions enabled in the account type.](https://files.readme.io/e740e0f8ef18fcacd780e2f43a3f20df603f5d743629ddf1e7a9d41add315c08-image.png)
4. In the **Edit account type** page, edit the account type details and permissions as needed, then click **Save** to update the account type.

### Delete an existing custom account type

1. Go to **Administration** > **Account types**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Account types**.
2. In the **Account types** page, search or browse the list of account types to locate the one you want to delete, then click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** and select **Delete**.

   > 📘
   >
   > ### You can only delete custom account types. You cannot delete the default *View*, *Act*, *Analyze*, *Build*, and *Admin* account types.

   ![Image of the Account types page with the curson hovering over the Delete option in the More menu in the row for a custom account type. ](https://files.readme.io/bbf0e17b11688ff9f1771cee98f7255cf9f668b87559cc6ff33263bca81217a2-image.png)
3. In the **Delete Account Type** modal, choose an account type to move assigned users to, then click **Delete**.

   ![Image of the delete confirmation modal, showing that one user will be moved to a different account type.](https://files.readme.io/92d7ccd0458e5fb287bc0d8924e6fad20db94db31b35c1346aec13dbe5e56110-image.png)

## View and manage account type assignments

There are several ways to view and manage account type assignments in Sigma. The following procedures highlight the methods available within the **Administration** > **Account types** page.

### View users assigned a specific account type

1. Go to **Administration** > **Account types**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Account types**.
2. In the **Account types** page, search or browse the list of account types and select the one you want to view.
3. In the account type’s overview, go to the **Members Assigned this Account Type** section to view a list of users currently assigned the account type. You can search the list and filter it by date joined, status, and user type.

### Add users to a specific account type

> 📘
>
> ### If your organization uses an identity provider (IdP) to manage permissions, you must [assign users to Sigma account types in the IdP](/docs/use-custom-account-types-with-your-idp).

1. Go to **Administration** > **Account types**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Account types**.
2. In the **Account types** page, search or browse the list of account types and select the one you want to assign.
3. In the account type’s overview, go to the **Members Assigned this Account Type** section and click **Add members**.
4. In the **Assign Account Type to Existing Members** modal, search for and select one or more users to assign the account type, then click **Confirm**.

   Sigma immediately updates the account type assignment and sends an email to the added users to notify them of the change.

### Reassign users from a specific account type

> 📘
>
> ### If your organization uses an identity provider (IdP) to manage permissions, you must [reassign Sigma account types in the IdP](/docs/use-custom-account-types-with-your-idp).

1. Go to **Administration** > **Account types**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Account types**.
2. In the **Account types** page, search or browse the list of account types and select the one with users you want to reassign.
3. In the account type’s overview, go to the **Members Assigned this Account Type** section, locate the user you want to reassign, then click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** and select **Reassign account type**.

   Alternatively, to bulk reassign users, select the checkbox of each user you want to reassign, then click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/reassign-account-type.svg) **Reassign account type**.

   ![Image of the "Members Assigned this Account Type" section with the mouse hovering over the icon for "Reassign account type".](https://files.readme.io/5f34fb40b28d5ab7bcc50ed7cf2d2c663d609dd7bd6cf8a2f0bcdb4ea2d8c8e4-image.png)
4. In the **Reassign Account Type** modal, select the account type you want to reassign to the users, then click **Confirm**.

   Sigma immediately updates the account type assignment and sends an email to the users to notify them of the change.

   ![Image of the modal that appears to confirm account type reassignment. ](https://files.readme.io/9e05043f5e5b3c898f6fad79ada02f8c6a2cf501e3c59f2f0921fa9c3e689310-image.png)

## Manage default invitation account type

When you invite a new user to your organization, you can select the account type to assign. If you don’t manually select one, Sigma applies the default account type, which you can designate in the **Account Types** page.

> 📘
>
> ### The default invitation account type only applies to password-authenticated users [invited directly from the **Administration** portal](/docs/invite-new-organization-members). It doesn't apply when your organization uses [SAML or OAuth authentication methods](/docs/manage-authentication).

1. Go to **Administration** > **Account types**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Account types**.
2. In the **Account types** page, select an option in the **Invitation default** field.

   Sigma immediately applies the update to the invitation form fields.

   ![Image of the Account types page with the Invitation default menu open and the mouse hovering over "Act".](https://files.readme.io/a0ba9ef4d387c20e25d33c2269dec5f9cb7dcf9e4a607ccd032b2ec0f27004fa-image.png)

Updated 3 days ago

---

[Account type and license overview](/docs/account-type-and-license-overview)[Basic explore vs. Full explore](/docs/basic-explore-vs-full-explore)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Default and custom account types](#default-and-custom-account-types)
  + - [Default account types](#default-account-types)
    - [Custom account types](#custom-account-types)
  + [Create and manage account types](#create-and-manage-account-types)
  + - [Create a new custom account type](#create-a-new-custom-account-type)
    - [Edit an existing account type](#edit-an-existing-account-type)
    - [Delete an existing custom account type](#delete-an-existing-custom-account-type)
  + [View and manage account type assignments](#view-and-manage-account-type-assignments)
  + - [View users assigned a specific account type](#view-users-assigned-a-specific-account-type)
    - [Add users to a specific account type](#add-users-to-a-specific-account-type)
    - [Reassign users from a specific account type](#reassign-users-from-a-specific-account-type)
  + [Manage default invitation account type](#manage-default-invitation-account-type)