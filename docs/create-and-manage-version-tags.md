# Create and manage version tags

# Create and manage version tags

As an admin, you can create and manage version tags. Users can tag specific versions of workbooks and data models to support workbook testing and publishing workflows. See [Add version tags to workbooks and data models](/docs/add-version-tags-to-workbooks-and-data-models).

## Create a version tag

To create a version tag, you must be assigned the Admin [account type](/docs/user-account-types).

> 💡
>
> ### Use a protected tag to enforce a request approval process for setting tags on workbook and data model versions.

1. Open the Admin portal, then select **Tags**.
2. Click **Create Tag**.
3. Enter a **Name** for the version tag. The name must be unique and is not case sensitive.
4. (Optional) Enter a **Description** for the version tag. For example, describe the intended purpose of the tag.
5. Select a color for the tag.
6. In the **Permission** section, choose whether to create a **Public** or **Protected** tag and control who can add the tag to a workbook or data model.
   1. A public tag can be added by anyone with **Can Edit** permissions.
   2. A protected tag can be added by any admin or any user with **Can edit** permissions in the list of users or teams that you specify. Users and teams that you do not specify must submit a request to apply the tag, which must be approved by users that you specify.
7. [optional] If you select **Protected**, search for users or teams that you want to be able to add the protected tag to any workbooks or data models that they can access, without requesting permission. The users or teams that you specify also receive requests to apply the tag from users without access to apply the tag.
8. Click **Create**.

> 💡
>
> ### Avoid creating a large number of tags, which could lead to multiple versions of a single workbook. Use descriptive names and create tags to support the teams that might need to access different versions of a workbook based on their job functions. For example, QA, UAT, or Production.

## Manage version tags

After creating a tag, you can select the tag and view the workbooks and data models that have the tag set on a version.

To manage a version tag, you must be assigned the Admin [account type](/docs/user-account-types).

1. Open the Admin portal, then select **Tags**.
2. Locate and select a tag that you want to view. You can sort the columns in the table to list tags alphabetically, or order by the number of workbooks tagged with the tag.

   A table lists the workbooks and data models with the tag applied.

### Delete a version tag

You can delete a version tag at any time. When you delete a tag, any tagged data model and workbook versions are also deleted. While the tagged version is deleted, the version is not removed from the version history of the workbook or data model. The source workbooks and data models remain unchanged.

To delete a version tag, do the following:

1. Open the Admin portal, then select **Tags**.
2. Locate and select a tag that you want to delete.
3. Select **Delete Tag**.
4. Review the affected data model and workbook versions, if any, then select **Delete**.  
   The tag is deleted and the list of **Tags** opens.

## Approve a request to apply a protected version tag

If a user wants to apply a protected tag to a workbook or data model version, the users and team members added as approvers for the version tag (the same users that can directly apply the tag) receive an email with the request.

If you receive an email requesting to apply a protected tag to a version, do the following:

1. Open the email.
2. Review the details of the request, such as the tag name, workbook or data model name, and the message from the user that wants to tag the workbook or data model.  
   ![](https://files.readme.io/a34f55f-Screenshot_2024-05-29_at_9.56.20_AM.png)
3. Click **Respond To The Request**.
4. The workbook or data model opens in Sigma. The version history is open to the specific version that the user requested to tag.  
   ![](https://files.readme.io/310b279-Screenshot_2024-05-29_at_10.05.11_AM.png)
5. Select **Deny** or **Approve**. To apply the requested tag, click **Approve**.
6. In the **Set Tag on Version** modal, make any necessary adjustments. See [Tag a workbook or data model version](/docs/add-version-tags-to-workbooks-and-data-models).

The requestor receives an email notifying them that their request was approved or denied.

Updated 3 days ago

---

[Recover deleted documents](/docs/recover-deleted-documents)[Audit and usage](/docs/audit-and-usage)

* [Table of Contents](#)
* + [Create a version tag](#create-a-version-tag)
  + [Manage version tags](#manage-version-tags)
  + - [Delete a version tag](#delete-a-version-tag)
  + [Approve a request to apply a protected version tag](#approve-a-request-to-apply-a-protected-version-tag)