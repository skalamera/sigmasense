# Workbook versions and version history

# Workbook versions and version history

Workbooks have versions. The default versions are Published and Draft, and you can add new custom versions called "tagged versions". For more details about version tagging, see [Add version tags to workbooks and data models](/docs/add-version-tags-to-workbooks-and-data-models). For more details about editing and publishing workbooks, see [Edit, draft, and publish a workbook](/docs/edit-draft-and-publish-a-workbook).

Workbook version history contains a list of all previously published versions of a workbook and any pending draft changes. Each published version includes a detailed list of changes, called the edit history. You can use the version and edit history to review drafted changes, compare or revert to older published versions, identify who on your team made a specific edit or set of changes, or identify which version is tagged with a specific version tag. There is no limit to the retention period of workbook version history.

## Requirements

* Workbook version history, including edit history and any edits to the current draft, is only available for users with **Can Edit** permission on a workbook.
* Only users with **Can Edit** permission can restore old versions and changes of a workbook.

Edit history is not available for changes made prior to December 13, 2022. Beginning on December 13, 2022, all organizations with Live Edit enabled track edits in the edit history. Edits made prior to Live Edit being enabled remain untracked. For more information see [Collaborate with Live Edit in workbooks](/docs/workbook-collaboration-with-live-edit).

## About workbook versions

When you open a workbook, the current version is listed in the workbook header:

* If you're viewing a published workbook, the version is **PUBLISHED**.
* If you're viewing a tagged version, the name of the version tag is shown.
* If you open the workbook for editing, the version is **DRAFT**.

A workbook can have one of the following versions:

* **Draft**: While you are editing a workbook, it is in draft mode and the changes are visible only to you and others currently editing the workbook.
* **Published**: To make changes visible to others with view or explore access to the workbook, you publish it.
* **Tagged**: If you want to have a read-only version of a workbook available to specific users or for a specific purpose, you can apply a tag to a specific workbook version. For example, you may tag a workbook as "Development" or "Production". See [Add version tags to workbooks and data models](/docs/add-version-tags-to-workbooks-and-data-models).

For more information about the workbook version lifecycle, see [Edit, draft, and publish a workbook](/docs/edit-draft-and-publish-a-workbook).

## Open version history for a workbook

When you make changes to a workbook, the changes appear in the version history. When you publish a version, the version history updates.

You must have **Can Edit** permissions on the workbook to view the version history.

1. Open a workbook.
2. Click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) next to the document name, then select **Version history**. You can also select the name of the current version, then select **View version history**.

   The version history panel opens and displays the latest version and its changes. Previously published versions are listed below, and the version corresponding to the currently published version is labeled ***Current***.

   ![Example workbook with version history open, showing the Current published version because there are no pending draft changes. The latest version is expanded by default, showing scalar color changes and a filter on the main viz on the workbook, organic traffic by country.](https://files.readme.io/0194740807d15b795f80246ff4cf6000479c03ef296cb63e279a8a87db693814-workbook-vh-open.png)
3. Review the detailed edit history for a specific version by clicking the chevron next to the version timestamp, or see the workbook as it was for a specific version or change by selecting it.

   ![Workbook version history with a specific change in the edit history selected and highlighted in the version history. The change on which the element occurred is highlighted on the workbook canvas.](https://files.readme.io/0ca6cd62dd323090a666c58d665ec54fa14bd8eb46e4941adacb35d485b18b06-selected-change-vh.png)
4. To return to the latest version of the workbook, select **Go back to latest version**.
5. To close the version history panel, click **X**.

## Restore a draft to a previous change or version

To return a workbook to a previously published version, or to a specific change in the workbook version history, restore a previous change or version to draft. Any changes made before you restore a previous version remain in the version history.

You must have **Can Edit** permissions on the workbook to restore a previous version or change in the version history.

### Restore a draft to a previously published version

To restore a draft to a previously published version, do the following:

1. Open the version history for a workbook.
2. Locate the previously published version that you want to restore.
3. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**, then select **Restore version as draft**.

   The change appears in the version history as **Restored version from** with the timestamp of the version listed.
4. Make other changes as needed, or click **Publish** to publish the changes.

### Revert to a previous change in the version history

You can restore your workbook draft to a specific change in the edit history for a version or draft.

> 🚧
>
> ### If your workbook contains input tables and you restore your workbook to a previous change in the version history, the input table contents are *not restored* to that point in time and instead reflect the latest changes.
>
> Instead, you can restore the published version closest to the specific change, then restore the specific change.

To revert your draft to a previous change in the edit history, do the following:

1. Open the version history for a workbook.
2. Locate the version that contains the change that you want to revert your draft to.
3. If needed, expand the edit history of the version, then locate and select the change.
4. In the workbook header, select **Restore version as draft**.

   The change appears in the version history as **Restored from autosaved draft**.
5. Make other changes as needed, or click **Publish** to publish the changes.

## Work with previously published versions

When reviewing the version history for a workbook, you can perform several actions on previously published versions. Select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** to do any of the following:

* Select **Restore version as draft** to restore the version as a draft. See [Restore a draft to a previously published version](#restore-a-draft-to-a-previously-published-version).
* Select **Edit name and description** to change the name and description of a version. By default, a version is listed by timestamp.
* Select **Save as new workbook** to save the version as a new workbook.
* Select **Copy link** to copy a link to the previous workbook version. Only users with access to the workbook can view the link.
* Set a tag on the version. See [Add version tags to workbooks and data models](/docs/add-version-tags-to-workbooks-and-data-models).

Updated 3 days ago

---

Related resources

* [Edit, draft, and publish a workbook](/docs/edit-draft-and-publish-a-workbook)
* [Workbook lifecycle: explore, draft, and publish](/docs/workbook-lifecycle-explore-draft-and-publish)
* [Add version tags to workbooks and data models](/docs/add-version-tags-to-workbooks-and-data-models)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [About workbook versions](#about-workbook-versions)
  + [Open version history for a workbook](#open-version-history-for-a-workbook)
  + [Restore a draft to a previous change or version](#restore-a-draft-to-a-previous-change-or-version)
  + - [Restore a draft to a previously published version](#restore-a-draft-to-a-previously-published-version)
    - [Revert to a previous change in the version history](#revert-to-a-previous-change-in-the-version-history)
  + [Work with previously published versions](#work-with-previously-published-versions)