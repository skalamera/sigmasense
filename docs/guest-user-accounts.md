# Guest User Accounts

# Guest User Accounts

Guest user accounts are password authenticated and allow you to enforce strictly limited access to your organization. Among other security-based limitations, guest users cannot view or request access to content outside of their Admin-assigned team(s).

This feature is opt-in and must be enabled by an organization Admin before guest users can be invited to your organization.

Guest user accounts are recommended when working with external vendors.

## Requirements

* You must be an organization Admin to enable and/or use this feature; see [Account types](/docs/user-account-types).
* Guest user accounts do not work if your organization uses [SCIM for team and user provisioning](/docs/manage-users-and-teams-with-scim).

## Guest User Permissions

Guest users can be assigned to any non-Admin [account type](/docs/user-account-types).

Guest accounts are unique in that they only have access to [workspaces associated with teams](/docs/manage-teams) to which they are assigned. Unlike standard users:

* they do not have access to the organization’s **All Members** [workspace](/docs/manage-workspaces), and
* they will not automatically get access to folders and documents [shared](/docs/share-a-workbook) with **All Members**
* they cannot request access to documents
* they can only interact with organization members who are assigned to the same team(s)
* they cannot access Sigma’s developer API

All non-Viewer guest users automatically have access to [Sigma's Sample Connection](/docs/sigmas-sample-connection).

## Guest User Authentication

Guest user accounts are always password [authenticated](/docs/manage-authentication), regardless of whether the organization uses an identity provider (e.g. Okta, Azure) for other users.

If your organization transitions to [SCIM for team and user provisioning](/docs/manage-users-and-teams-with-scim), guest user accounts will no longer work and they will be unable to log in to Sigma.

## Allow Guest Users Accounts in Your Organization

1. [Open your Admin Portal](/docs/sigma-administration).
2. Click **Authentication** to open the authentication page.
3. Click the **Authentication Method & Options** section’s **Edit** button.![](https://files.readme.io/4a4ec9a-1.png)
4. Click the **Allow Guest Access** switch toggle.  
   ![](https://files.readme.io/6125c86-2.png)
5. Click the section’s **Save** button.![](https://files.readme.io/abab620-3.png)

## Invite a Guest User to Your Organization

1. Click your profile icon, located in the top right corner of the screen, to open the user menu.
2. In the menu, select **Invite Users.**  
   You will be redirected to the **Invite People to Use Sigma** modal, located on the **Users** page in your Admin Portal.  
   ![](https://files.readme.io/4bc335e-4.png)
3. Type the email address of the person you would like to invite under **Enter Email Address**.  
   If you are inviting multiple users, type each address separated by commas.  
   ![](https://files.readme.io/3b98443-5.png)
4. Check the **Invite as Guest Users** checkbox.  
   ![](https://files.readme.io/9c21b70-6.png)
5. Select an account type from the **Select Account Type** menu.  
   ![](https://files.readme.io/0f057c1-7.png)
6. [optional] Under **Add a custom message**, enter a message to include in the emailed invitation.
7. Select one or more teams from the **Assign Teams** list.  
   ***Note***\*: Guest users will only have access to workspaces associated with their assigned team(s).\*  
   ![](https://files.readme.io/23c4b61-8.png)
8. Click **Invite**.  
   ![](https://files.readme.io/39e1926-9.png)

## Disable Guest User Accounts

The following instructions will show you how to disable guest user accounts across your organization. If this feature is disabled, all existing guest accounts will automatically be deactivated.

To instead disable an individual guest user’s account, visit [Deactivate Users](/docs/deactivate-users).

1. [Open your Admin Portal](/docs/sigma-administration).
2. Click **Authentication** to open the authentication page.
3. Click the **Authentication Method & Options** section’s **Edit** button.  
   ![](https://files.readme.io/0daf057-10.png)
4. Click the **Allow Guest Access** switch.  
   ![](https://files.readme.io/442b559-11.png)
5. Click the section’s **Save** button.  
   ![](https://files.readme.io/9de587b-12.png)

Updated 3 days ago

---

Related resources

* [User account types](/docs/user-account-types)
* [Manage Teams](/docs/manage-teams)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Guest User Permissions](#guest-user-permissions)
  + [Guest User Authentication](#guest-user-authentication)
  + [Allow Guest Users Accounts in Your Organization](#allow-guest-users-accounts-in-your-organization)
  + [Invite a Guest User to Your Organization](#invite-a-guest-user-to-your-organization)
  + [Disable Guest User Accounts](#disable-guest-user-accounts)