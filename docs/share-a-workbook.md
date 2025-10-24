# Share a workbook or data model

# Share a workbook or data model

If you own or have **Can Edit** permissions on a workbook or data model, you can share the document with individuals, teams, and everyone in your Sigma organization.

> 🚩
>
> ### When you share a document with someone, they are also granted **View** access to the data in the connection data sources.

If you want to share a document but only allow the user to access a specific version, see [Share tagged versions of a workbook or data model](#share-tagged-versions-of-a-workbook-or-data-model) .

## Requirements

The ability to share a document requires the following:

* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Share documents** permission enabled.
* You must be the workbook or data model owner or be granted **Can edit** [access to the document](/docs/folder-and-document-permissions).

## About sharing with users, teams, and all organization members

When you share a document with an individual user, the availability of permissions depends on the user's account type.

| Document access | Minimum required account type permission | Description |
| --- | --- | --- |
| **Can view** | **View workbooks** or **View datasets** | The user can view and interact with workbook elements in **View** mode. The user can view and interact with the [data model overview](/docs/navigate-data-models#data-model-overview-page). |
| **Can explore** | **Full explore** | Workbooks only.  In addition to **Can view** capabilities, the user can modify workbook elements to create custom views of the workbook in **Explore** mode. |
| **Can edit** | **Create, edit, and publish workbooks** or **Create, edit, and publish datasets** | In addition to **Can view** and **Can explore** capabilities, the user can manage the document (rename, move, or delete), view hidden pages, and update the published version.  If the **Share documents** account type permission is enabled, the user can also share the workbook with other organization members. |

When you share a document with all members of your organization or a specific team, individual user access is based on the most restrictive grant (the one with the least privileges) between the document access and account type permission.

For example, if you grant **Can edit** access to all members of your organization, but a user is assigned an account type with only **View workbooks** permissions enabled, that specific user is limited to **Can view** workbook access.

For more information about document access and modes, see [Folder and document permissions](/docs/folder-and-document-permissions#document-permissions) and [Workbook modes overview](/docs/workbook-modes-overview).

## Share a document with an organization member or team

You can share a draft or published document:

1. In the document header, click **Share** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/share-user.svg)) to open the **Share Workbook** or **Share Data model** modal. You can also share a document from the document menu.
2. In the search bar, enter the team or organization member with whom you want to share the workbook or data model.
3. For each team or user, select a **Permission** from the dropdown. If the document has tagged versions, you can also limit the permission to a specific version tag. See [Share tagged versions of a document](#share-tagged-versions-of-a-document).
4. Repeat as needed for additional teams or members.
5. (Optional) Add a message to be included in an email message to the users gaining access to the document.
6. By default, the Sigma service sends an email message. Deselect the checkbox if you don't want to send an email.
7. Click **Share**.

### Share tagged versions of a document

To control what users and teams can see in a given workbook, or what version of a data model users can access, share a tagged version with a user or a team.

When you share a document with access only to a specific version tag, you effectively revoke access to the published version of the document and limit access only to the shared tagged versions. You can use tagged versions like a published version of a document for a given user or team.

For example, you can make a version of a Sales workbook that is filtered entirely on the East region, tag that version with East, then share that tagged version with the Sales - East team. Members of the Sales - East team then have view (and explore) access to that version of the workbook, but cannot make any changes to the source workbook.

> 📘
>
> ### If the tagged version of a workbook allows users to access the data source, users with **Can explore** permissions on the tagged version of a workbook can select **Save As** and save a copy of the version tagged workbook for editing.

To share a tagged version of a workbook or data model, do the following:

1. In the document header, click **Share** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/share-user.svg)) to open the **Share Workbook** or **Share Data model** modal. You can also share a document from the document menu.
2. In the search bar, enter the team or organization member with whom you want to share the tagged version of the workbook or data model.
3. For each team or user, select a **Permission** from the dropdown, then hover over the permission to select a tag on the document to grant access to. Select **All** (default) to share all versions of the workbook with the user or team.  
   ![](https://files.readme.io/a5be3fb-vt-share-workbook.png)
4. Click **Share**.

If you [remove a tag from a document version](/docs/add-version-tags-to-workbooks-and-data-models#remove-a-tag-from-a-document-version), users and teams with access only to that tagged version of the document lose access to the document.

## Share a workbook with your organization

You can copy a link to the workbook and share it with users in your organization with the link. Guest users and external users cannot access a workbook shared with your organization.

1. In the workbook header, click **Share** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/share-user.svg)) to open the **Share Workbook** modal. You can also share a workbook from the document menu.
2. At the bottom of the modal, in the **General access link** section, toggle **Allow sharing by link**.
3. For **All members of your organization**, choose from the available permissions. The following permissions are available:

   * Can view
   * Can explore
   * Can edit

   For more information, see [About sharing with users, teams, and all organization members](#about-sharing-with-users-teams-and-all-organization-members) on this page.

   After you set the permission, the workbook can be shared.
4. Click **Copy Link** to copy the link to the workbook to share with others, then close the modal.

## Transfer ownership of a document

You can transfer ownership of a workbook or data model from one user to another. Before you transfer ownership of a document, make sure that the future owner either has access to the folder containing the document, or move the document.

> 📘
>
> ### You must be assigned the Admin [account type](/docs/user-account-types) to transfer ownership.

To transfer ownership of a workbook or data model, share the document with the future owner, then assign them as the owner:

1. In the document header, click **Share** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/share-user.svg)) to open the **Share workbook** or **Share data model** modal. You can also share a document from the document menu.
2. In the search bar, enter the user to whom you want to transfer ownership.
3. Grant the user any permission level.
4. Click **Share**.
5. In the document header, click **Share** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/share-user.svg)) to reopen the **Share workbook** or **Share data model** modal.
6. Locate the user to whom you want to transfer ownership.
7. In the permissions dropdown menu for the user, select **Owner**.  
   The changes save automatically.

> 📘
>
> ### When you deactivate a user, you can transfer ownership of all their documents to another user. See [Deactivate a user](/docs/deactivate-users).

## Share a custom view of a workbook

If you customize a workbook and create a custom view, you can share a the custom view with others using a link:

1. In the document header, click **Share and export** > **Share**.
2. In the **Share Workbook** modal, confirm the checkbox to **Link to current custom view** is selected.
   * To share the link to the custom view with anyone, toggle **Allow general sharing by link**, select a permission, and copy the link.
   * To share the link to the custom view with other users that already have access to the workbook, select **Copy link**.

![](https://files.readme.io/e7a5030ee7b7c30b718d5a2f2825217611675ffd5eb60ad353b538658d1dc0ad-custom-view-link-share.png)
> 💡
>
> ### If you make changes to the custom view, you must create a new link to share the changes.

## Share an exploration

If you have not yet saved your workbook, you can still share the exploration. In the header, click **Share** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/share-user.svg)), then turn on **Allow access by link**.

![](https://files.readme.io/e6161703fe063c85e50be5973036d42f5b18faaf886898ef49cf58c8ea212aa3-wb-share-exploration.png)

## Limit access to workbook contents by hiding pages

You can hide pages in a workbook from users with only **Can Explore** and **Can View** permissions on a workbook. To hide a page, see [Manage workbook page visibility](/docs/manage-workbook-page-visibility).

## Respond to requests for access to content

As a workbook owner, if a user attempts to access your content and doesn't have permission to do so, they can request access through the error page blocking their immediate access. Access requests are emailed to the document owner.

To respond to a request to access the document, do the following:

1. Open the email notification, then click **Respond to the Request**.  
   ![](https://files.readme.io/c023140aafe7cda56a490017a129802a9c11519b9d639f1fc3c6fea7d109f06c-wb-share-email.png)

   A web browser window opens to the Sigma service. After logging in, the **Share Workbook** modal opens. You can see and respond to the access request.
2. (Optional) For the requesting user, click the permission dropdown menu to select the appropriate level of access. For a version tagged workbook, you can choose a specific permission and version tag combination to grant the user access to view or explore a specific tagged version of the workbook.

   > 📘
   >
   > ### The user can't be granted access higher than what their account type allows.

   ![](https://files.readme.io/8c5d9f1e54c9cf2fd6f1aba5226b3cb8a501273c5eb1c3aaad357b067cd504a5-share-wb-request.png)
3. To approve the request, click **Approve**.  
   The user is granted access to view the workbook and immediately shows up in the list of people and teams with access.

   To deny the request, click **Deny**.  
   Access to the workbook remains unchanged and the request is removed from the **Share Workbook** modal.
4. Click **Save**.

## Access shared content

When another user shares a document directly with you, it appears in the **Shared with Me** section of the [Sigma home page](/docs/get-around-in-sigma#sigma-home-page).

Documents shared with all users in a Sigma organization do not appear in **Shared with Me**.

* To access a data model shared with all users in a Sigma organization, search for it by name.
* To access a workbook shared with all users in a Sigma organization via a link, search the **Recents** section of the Sigma home page or access it via the link.

Updated 3 days ago

---

Related resources

* [Folder and Document Permissions](/docs/folder-and-document-permissions)
* [Send and schedule exports from workbooks](/docs/send-and-schedule-exports-from-workbooks)
* [Workbook embedding: an overview](/docs/workbook-embedding-an-overview)
* [Manage workbook page visibility (Beta)](/docs/manage-workbook-page-visibility)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [About sharing with users, teams, and all organization members](#about-sharing-with-users-teams-and-all-organization-members)
  + [Share a document with an organization member or team](#share-a-document-with-an-organization-member-or-team)
  + - [Share tagged versions of a document](#share-tagged-versions-of-a-document)
  + [Share a workbook with your organization](#share-a-workbook-with-your-organization)
  + [Transfer ownership of a document](#transfer-ownership-of-a-document)
  + [Share a custom view of a workbook](#share-a-custom-view-of-a-workbook)
  + [Share an exploration](#share-an-exploration)
  + [Limit access to workbook contents by hiding pages](#limit-access-to-workbook-contents-by-hiding-pages)
  + [Respond to requests for access to content](#respond-to-requests-for-access-to-content)
  + [Access shared content](#access-shared-content)