# Share a folder

# Share a folder

You can categorize and share documents with people using folders. You share folders with other users and teams by granting access to the folder. Folders support four levels of access permissions:

* **Can view**
* **Can explore**
* **Can contribute**
* **Can manage**

This document describes folder permissions and how to share folders. For more details on available permissions, see [Folder and document permissions](/docs/folder-and-document-permissions).

## User requirements

The ability to share a folder requires the following:

* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Share documents** permission enabled.
* You must be the folder owner or be granted **Can manage** [access to the folder](/docs/folder-and-document-permissions#folder-permissions).

## Permission types

Permission options are the same for folders and workspaces. Permissions set at the folder or workspace level apply to all documents within that workspace or folder.

| Permission | Folder access and capabilities |
| --- | --- |
| **Can view** | * View-only access to documents and folders in the shared space |
| **Can explore** | * Explore access to workbooks in the shared space * View-only access to all datasets in the shared space |
| **Can contribute** | * Create and edit their own documents and folders * View and explore others users’ documents and folders in the shared space * Manage anything they create. Includes deletion, renaming, moving of their own documents and folders   A user with **Can contribute** access to a workspace automatically gets **Can edit** access to all documents that they’ve personally created in that workspace. They also get **Can view** access to datasets in the workspace and **Can explore** access to workbooks in the workspace. |
| **Can manage** | * Create and edit their own documents and folders * Edit other’s documents and folders in the shared space * Manage anything in the shared space. Includes access management, sharing, deletion, renaming, and moving of anyone’s documents and folders.   + **Can manage** in a workspace or folder grants, **Can edit** on any docs within that folder. |

## Share a folder

You can share a folder of documents with other users or teams in Sigma in several ways.

### Share from within the folder

1. Open the folder.
2. Next to the folder's name on the top of the screen, click ![share icon](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/share-user.svg) **Share**. The **Share Folder** modal opens.
3. In the text box, type the names of individual users or teams you wish to add.
4. (Optional) To change the user's or team's level of access, click the dropdown to select a permission type for each team or member. If you do not select a permission, the default permission is set to **Can explore**.
5. (Optional) To notify users about being added to your folder, select the **Send email** checkbox. For **Add a message**, enter a message to be included in the email body.
6. Click **Save**.

### Share from a navigation page

1. Navigate to the folder you wish to share.
2. Open the folder's parent folder.
3. Next to the folder you want to share, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**.
4. Select **Share...** to open the **Share Folder** modal.
5. In the text box, type the names of individual users or teams you wish to add.
6. (Optional) To change the user's or team's level of access, click the dropdown to select a permission type for each team or member. If you do not select a permission, the default permission is set to **Can explore**.
7. (Optional) To notify users about being added to your folder, select the **Send email** checkbox. For **Add a message**, enter a message to be included in the email body.
8. Click **Save**.

## Modify or revoke access to a folder

If you need to change a user or team's level of access after you give them initial access to a folder, you can change the user or team's level of access to a folder or even revoke their access entirely at any time.

1. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** on the parent folder and select **Share...** or click ![share icon](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/share-user.svg) **Share** on the individual folder's page to open the **Share Folder** modal.
2. In the **Share Folder** modal, review the **Person or team with access** section.
3. Modify their access type or revoke access:
   * To select a new level of access, use the **Permission** dropdown menu.
   * To revoke access completely, hover over the team or member. Then click ![trash can icon](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/trash.svg) **Remove access**.
4. Click **Save**.

## Respond to request for access to content

If a user attempts to access your content and doesn't have permissions to do so, they can request access through the error page blocking their immediate access. This sends an email notification with the subject **Request for access** to the owner of the folder.

To respond to the request for access, do the following:

1. In the email notification, click **Respond to the request**. The **Share Folder** modal opens, allowing you to view the current access requests.
2. (Optional) Use the dropdown menu to set the user's level of access.

   > 📘
   >
   > ### The user cannot be granted access higher than what their account type allows.
3. Approve or deny the request:

   * To approve the request, click **Approve**. The request is removed from the **Share Folder** modal, and the user is listed in the **Person or team with access** tab.
   * To deny the request, click **Deny**. The request is removed from the **Share Folder** modal.
4. Close the **Share Folder** modal. The access that you granted or denied is saved after selecting **Approve** or **Deny**.

Updated 3 days ago

---

Related resources

* [Folder and Document Permissions](/docs/folder-and-document-permissions)
* [Share a workbook](/docs/share-a-workbook)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Permission types](#permission-types)
  + [Share a folder](#share-a-folder)
  + - [Share from within the folder](#share-from-within-the-folder)
    - [Share from a navigation page](#share-from-a-navigation-page)
  + [Modify or revoke access to a folder](#modify-or-revoke-access-to-a-folder)
  + [Respond to request for access to content](#respond-to-request-for-access-to-content)