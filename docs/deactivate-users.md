# Deactivate users

# Deactivate users

This article describes how to deactivate users and allocate their documents to active users, and how to reactivate inactive users.

If your organization uses SAML + [SCIM](/docs/manage-users-and-teams-with-scim), you must deactivate users through your identity provider. If you deactivate in Okta, the user is marked as **inactive** in Sigma. The admin who set up provisioning also inherits the Sigma content of the deactivated user. If you deactivate a user in Azure, the user is set to **inactive** in Sigma for 30 days. After 30 days, the user is marked **archived**.

If your organization only uses SAML, you must deactivate the user in Sigma.

> 🚧
>
> ### If you deactivate a user, their client credentials (API and embed) will also be deactivated. References to these credentials will result in an invalid request error.

To deactivate users and allocate their documents to an active user, do the following:

1. [Open the Admin Portal](/docs/sigma-administration).
2. Click **Users**.
3. On the **Members** tab, select the checkbox next to each user you want to deactivate. To select all users, select the checkbox to the left of **Name**.

   > 📘
   >
   > ### When you check the box to the left of **Name**, it only selects the users in your view. If you scroll down, more users appear and can be selected.

   The numbers to the right of **Account type** show the number of users currently displayed out of the total number of users.
4. After selecting users, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/deactivate-user.svg) (**Deactivate**).

   > 💡
   >
   > You can also click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** for a selected user and then select **Deactivate**. This deactivates all selected users.
5. On the **Deactivate User** popup, the users you chose to deactivate are shown. For **Select new owner**, choose a new owner for the deactivated user's documents. By default, your user is selected. A user must have **Create, edit, and publish workbooks** permissions to be eligible as the new owner. You can click the **x** to remove yourself and search for a new user to be the owner.

   ![](https://files.readme.io/d5054e143945726d1495bb6b07b81f76efcc3a762efb4f2da694e88ca20a49b8-deactivate-users.png)
6. Click **Confirm**.

## Deactivated user documents

When you deactivate a user, you do not need to manually transfer the documents created by the user, Sigma does this for you. Ownership of documents such as workbooks, data models, datasets, including materialization and export schedules for the documents, are transferred.

After deactivation, the user's documents in their **My Documents** folder are automatically migrated to the selected new owner's **My Documents** folder, added at the following location: **My Documents** > **Archived Users** > **<Deactivated User>**. The folder title is the deactivated user's name. If you use SAML and SCIM, the user's documents are also located in **My Documents** > **Archived Users** > **<Deactivated User>**. To share, rename, move, or delete the folder, click![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**.

Any documents that the deactivated user owned in shared folders also transfer to the new owner, but their location does not change.

## Deactivated user accounts and reactivation

After an account is deactivated, it still appears in the **Members** tab on the **Users** page with a status of **Inactive**.

Inactive users are filtered out of the **Members** list by default. Use the list's filter menu to show all users.

To reactivate a user, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Reactivate**.

## Deactivate or reactivate user accounts via API

An admin in Sigma can use the [Deactivate member API endpoint](/reference/deletemember) to deactivate a user. This reassigns the deactivated user's documents to the user with API credentials.

To deactivate a user and reassign their documents to a specific user, [make a PATCH request to the Update member API endpoint](/reference/updatemember). Set the `newOwnerId` to the user ID of the desired document owner, and `isArchived` to `True`.

When you use the Update member API endpoint to deactivate a user, you can also choose to archive all documents owned by the user rather than transferring them, or archive the export schedules when you transfer the documents to a new owner.

## Reactivate disabled users in bulk

To reactivate users in bulk, do the following:

> 📘
>
> ### This operation is limited to organizations that do not use an IdP for authentication.

1. In the Admin portal, open **Users**.
2. On the **Members** tab, remove the **Active** filter, then select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/filter.svg) and select **Deactivated** to show only deactivated users.
3. Select the checkbox next to each user that you want to reactivate. To select all deactivated users, select the checkbox next to **Name**.
4. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/share-user.svg) (**Reactivate**).
5. Click **Confirm**.

Updated 3 days ago

---

Related resources

* [Invite people to your organization](/docs/invite-people-to-your-organization)
* [User account types](/docs/user-account-types)

* [Table of Contents](#)
* + [Deactivated user documents](#deactivated-user-documents)
  + [Deactivated user accounts and reactivation](#deactivated-user-accounts-and-reactivation)
  + [Deactivate or reactivate user accounts via API](#deactivate-or-reactivate-user-accounts-via-api)
  + [Reactivate disabled users in bulk](#reactivate-disabled-users-in-bulk)