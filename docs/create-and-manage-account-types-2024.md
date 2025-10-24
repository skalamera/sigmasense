# Create and manage account types (Lite/Essential/Pro)

# Create and manage account types (Lite/Essential/Pro)

> 🚩
>
> ### If your organization utilizes the View/Act/Analyze/Build license model, refer to [this document](/docs/create-and-manage-account-types).

Account types enable you to manage user access to specific features and capabilities available through each license tier. Default and custom account types add flexibility and scalability to Sigma’s access control methodology, allowing your organization to adapt to ongoing changes in your licensed user base and user requirements.

This document introduces default and custom account types and explains how to create, manage, and assign account types to organization users. For more information about account types as they relate to the licensing model, see [License and account type overview](/docs/license-and-account-type-overview-2024).

## User requirements

To create and manage account types and user assignments, you must be assigned the Admin account type.

## Default and custom account types

Sigma supports default and custom account types that allow you to enable or disable any combination of permissions within the constraints of your organization’s license tiers.

For a comparison of available account type permissions by tier, see [Account type permission availability matrix](/docs/license-and-account-type-overview-2024#account-type-permission-availability-matrix).

### Default account types

There are four default account types built into your organization: Lite, Essential, Pro, and Admin. These account types reflect Sigma's [license tiers](/docs/license-and-account-type-overview-2024) and support four standard roles or levels of access.

| Default account type | Description |
| --- | --- |
| **Lite** *(Lite license)* | Enables all permissions available through the Lite license tier.  *Recommended for users who require access to prepared data and insights.* |
| **Essential** *(Essential license)* | Enables all permissions available through the Essential license tier.  *Recommended for users who require more deep-dive capabilities in published workbooks but don’t need to build workbooks themselves.* |
| **Pro** *(Pro license)* | Enables a selection of permissions available through the Pro license tier.  *Recommended for users who model, transform, and analyze data.* |
| **Admin** *(Pro license)* | Enables all permissions available through the Pro license tier and administrative privileges.  *Recommended for system administrators who manage organization settings and users.* |

### Custom account types

Custom account types allow you to create additional roles and variations of access within any license tier. You can enable or disable individual permissions for granular access control that suits any user of your organization.

## Create and manage account types

The following procedures demonstrate how to create, edit, and delete account types. These tasks involve the account type details and permissions only. For information about account type assignments, see [View and manage account type assignments](#view-and-manage-account-type-assignments) in this document.

### Create a new custom account type

1. Go to **Administration** > **Account Types**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Account Types**.
2. In the **Account Types** page, click **Create New Account Type**.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/create-and-manage-account-types/create-new-account-type.png)
3. In the **New Account Type** page, configure the custom account type:

   1. In the **Name** field, enter a unique name to identify the account type.
   2. In the **Description** field, enter a description about the account type (for example, context about its permissions or user role).
   3. In the permissions table, select the checkbox for each permission you want to enable, and clear the checkbox for each permission you want to disable.

      > 💡
      >
      > ### To select all permissions available through the Lite, Essential, or Pro license tier, select the checkbox in the applicable column header.
   4. Click **Create** to save the new account type.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/create-and-manage-account-types/create-account-type.png)

### Edit an existing account type

1. Go to **Administration** > **Account Types**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Account Types**.
2. In the **Account Types** page, search or browse the list of account types and select the one you want to edit.

   > 📘
   >
   > ### You cannot edit details and permissions of the default **Admin** account type.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/create-and-manage-account-types/select-existing-account-type.png)
3. In the account type’s overview, click **Edit**.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/create-and-manage-account-types/edit-account-type.png)
4. In the **Edit Account Type** page, edit the account type details and permissions as needed, then click **Save** to update the account type.

### Delete an existing account type

1. Go to **Administration** > **Account Types**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Account Types**.
2. In the **Account Types** page, search or browse the list of account types to locate the one you want to delete, then click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** and select **Delete**.

   > 📘
   >
   > ### You can only delete custom account types. You cannot delete the default **Admin**, **Pro**, **Essential**, or **Lite** account types.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/create-and-manage-account-types/delete-account-type.png)
3. In the **Delete Account Type** modal, select an account type to reassign users to, then click **Delete**.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/create-and-manage-account-types/delete-account-type_modal.png)

## View and manage account type assignments

There are several ways to view and manage account type assignments in Sigma. The following procedures highlight the methods available within the **Administration** > **Account Types** page.

### View users assigned a specific account type

1. Go to **Administration** > **Account Types**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Account Types**.
2. In the **Account Types** page, search or browse the list of account types and select the one you want to view.
3. In the account type’s overview, go to the **Members Assigned this Account Type** section to view a list of users currently assigned the account type. You can search the list and filter it by date joined, status, and user type.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/create-and-manage-account-types/members-assigned.png)

### Add users to a specific account type

> 📘
>
> ### If your organization uses an identity provider (IdP) to manage permissions, you must [assign users to Sigma account types in the IdP](/docs/use-custom-account-types-with-your-idp).

1. Go to **Administration** > **Account Types**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Account Types**.
2. In the **Account Types** page, search or browse the list of account types and select the one you want to assign.
3. In the account type’s overview, go to the **Members Assigned this Account Type** section and click **Add members**.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/create-and-manage-account-types/add-members.png)
4. In the **Assign Account Type to Existing Members** modal, search for and select one or more users to assign the account type, then click **Confirm**.

   Sigma immediately updates the account type assignment and sends an email to the added users to notify them of the change.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/create-and-manage-account-types/assign-account-type-to-existing-members_modal.png)

### Reassign users from a specific account type

> 📘
>
> ### If your organization uses an identity provider (IdP) to manage permissions, you must [reassign Sigma account types in the IdP](/docs/use-custom-account-types-with-your-idp).

1. Go to **Administration** > **Account Types**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Account Types**.
2. In the **Account Types** page, search or browse the list of account types and select the one with users you want to reassign.
3. In the account type’s overview, go to the **Members Assigned this Account Type** section, locate the user you want to reassign, then click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** and select **Reassign account type**.

   Alternatively, to bulk reassign users, select the checkbox of each user you want to reassign, then click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/reassign-account-type.svg) **Reassign account type**.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/create-and-manage-account-types/bulk-reassign-account-type.png)
4. In the **Reassign Account Type** modal, select the account type you want to reassign to the users, then click **Confirm**.

   Sigma immediately updates the account type assignment and sends an email to the users to notify them of the change.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/create-and-manage-account-types/reassign-account-type_modal.png)

## Manage default invitation account type

When you invite a new user to your organization, you can select the account type to assign. If you don’t manually select one, Sigma applies the default account type, which you can designate in the **Account Types** page.

> 📘
>
> ### The default invitation account type only applies to password-authenticated users [invited directly from the **Administration** portal](/docs/invite-new-organization-members). It doesn't apply when your organization uses [SAML or OAuth authentication methods](/docs/manage-authentication).

1. Go to **Administration** > **Account Types**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Account Types**.
2. In the **Account Types** page, select an option in the **Invitation Default** field.

   Sigma immediately applies the update to the invitation form fields.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/create-and-manage-account-types/invitation-default.png)
   Close
   Restore Version

Create and manage account types (Lite/Essential/Pro)
Description (optional)

Owlbert Ice Cream
Uh oh, something went wrong!
Don't worry, your content is safe.

Try refreshing the page, or switch to the raw mode editor.

Related resources
Tell your users what they should do after they've finished this page
You’re usingour new MDX engine! Pleasereport any rendering issues to our support team.

Updated 3 days ago

---

[About Sigma](/docs/about-sigma)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Default and custom account types](#default-and-custom-account-types)
  + - [Default account types](#default-account-types)
    - [Custom account types](#custom-account-types)
  + [Create and manage account types](#create-and-manage-account-types)
  + - [Create a new custom account type](#create-a-new-custom-account-type)
    - [Edit an existing account type](#edit-an-existing-account-type)
    - [Delete an existing account type](#delete-an-existing-account-type)
  + [View and manage account type assignments](#view-and-manage-account-type-assignments)
  + - [View users assigned a specific account type](#view-users-assigned-a-specific-account-type)
    - [Add users to a specific account type](#add-users-to-a-specific-account-type)
    - [Reassign users from a specific account type](#reassign-users-from-a-specific-account-type)
  + [Manage default invitation account type](#manage-default-invitation-account-type)