# Add version tags to workbooks and data models

# Add version tags to workbooks and data models

Add a tag to a workbook or data model version to create a read-only view of that document version. You can then share the tagged version with another team for their exclusive use, embed the tagged version of the workbook in your application, or implement a development lifecycle with version control using tagged versions.

When you tag a workbook or data model version, you can continue iterating on the source document in a typical draft and publish workflow, without affecting the tagged version. For more details, see [Version tagging workflow](#version-tagging-workflow).

You can tag multiple versions of a workbook or data model, but you cannot have multiple versions of a document tagged with the same tag.

Admins can create and manage version tags, including creating protected tags that require an approval flow. See [Create and manage version tags](/docs/create-and-manage-version-tags).

## Version tagging workflow

All workbooks and data models have published versions and drafts. All changes made to a document are visible in the [version history](/docs/workbook-versions-and-version-history).

You can tag a specific document version to indicate something about the status of that document version. For example, tag a version of a workbook to indicate that the contents need to be reviewed for accuracy, or that it is ready to be used in production.

![Diagram showing the version tagging workflow, where you tag the latest version of a workbook or data model with 'testing' to send a read-only version of the document to the testing team, then if everything looks good, that team can tag that version with the 'production' tag and remove the testing tag. If that doesn't look good, the testing team can let the development team know that additional changes are needed and the dev team can revert the current draft to the version tagged version, make changes, and publish the changes. They can then restart the tag workflow by tagging the new version with 'testing'.](https://files.readme.io/4be75c3ec3cb8eaefd59cade127457cb1258bb6afa73e321f0aa15e50a019c95-version-tag-workflow.png)

You can also tag data models, and use a similar workflow to tag specific data model versions for testing or production use.

You can continue iterating on the draft while a tagged version is being reviewed. Changes made to the draft or published version do not affect the tagged version. See [Make changes to a tagged workbook version](/docs/add-version-tags-to-workbooks-and-data-models#make-changes-to-a-tagged-workbook-version) for more details.

![Diagram showing a tagged version of a document, where the past versions of the document have continued to update while the version tagged version of the document is associated with a past version. The latest draft is unsaved so does not have a version number and is not reflected by the published version, and cannot be tagged.](https://files.readme.io/6d1aa5d397ed3e77e4b4c358aba2e9e35d18a529aed6b3f1faeffa61e457880a-draft-publish-tag-workflow.png)

### How version tagging affects datasets and data models

When you tag a workbook version that uses a dataset as the data source, a copy of the dataset version in use is created to use with the tagged workbook version. The dataset associated with the tagged workbook version no longer updates even if changes are made to the original dataset, effectively freezing the version of the dataset that was in use when the workbook version was tagged. The data source itself is not affected in any way by a version tag.

![Diagram showing the fact that datasets used as the source for a version tagged workbook rely on a copy of a dataset version.](https://files.readme.io/4dac999-vt-diagram-dataset.png)

Workbooks that use a data model as the data source work differently. When you tag a workbook version that uses a data model as the data source, the workbook version is tagged but the data model version is not. Any future changes made to the data model, such as adding new columns or changing the data type of an existing column, are synced with the versions of the workbook that depend on the data model.

![Diagram showing the described way that the published version of a data model remains synced with a version tagged workbook.](https://files.readme.io/841bfca-vt-diagram-data-model.png)

If you want to "freeze" the data model used as the data source of a tagged version of a workbook, you can tag both the data model and the workbook, and use the tagged data model as the data source for the tagged version of the workbook. See [Swap the source of a tagged workbook version](#swap-the-source-of-a-tagged-workbook-version).

### Embedding tagged workbook versions

If you embed your workbook, you can use version tags to manage promoting content between environments. For example, use "test" and "production" tags to help manage changes and protect the version that is used in production. You can then use a link directly to a tagged version in your embed. See [Link to a tagged version of a workbook](#link-to-a-tagged-version-of-a-workbook).

For more details about version tag workflows and restricting access to tagged versions of workbooks, see [Make changes to a tagged workbook version](#make-changes-to-a-tagged-workbook-version) and [Share tagged versions of a document](/docs/share-a-workbook#share-tagged-versions-of-a-document).

For details about creating tags and protecting tags to enforce a request approval flow, see [Create and manage version tags](/docs/create-and-manage-version-tags).

If you want to integrate version tagging in Sigma with the source control platforms already integrated with your development workflow, you can use the Sigma REST API. For a recipe, see [QuickStart - Embedding 10: Version Tagging](https://quickstarts.sigmacomputing.com/guide/embedding_10_version_tagging_v3/index.html).

### Version tagging and materialization

When you tag a version of your workbook that relies on a materialized data source, the tagged version might not use the materialized data source.

* Materialized dataset: The materialized dataset is not used by the tagged version of the workbook. Instead, the tagged version of the workbook relies on a copy of the dataset made when the tag was applied.
* Materialized data model: The materialized data model is used unless you use a tagged version of the data model, such as when swapping sources for the tagged workbook version. Tagged versions of data models cannot be materialized.

| Object | Is materialized version used? | Details |
| --- | --- | --- |
| Dataset | no Materialized version is not used. | The tagged version of the workbook uses a copy of the dataset instead of the original dataset. |
| Data model | yes Materialized version is used. | The tagged version of the workbook uses the data model, remaining in sync with any changes made to the data model and using the materialized results. |
| Tagged data model | no Materialized version is not used. | The tagged version of the workbook uses a tagged version of the data model, which cannot be materialized at this time. |

See [About materialization](/docs/materialization) for more details on materialization.

## Tag a workbook or data model version

You can tag a version of a workbook or a data model. When you tag a document, you create a read-only version of the document that you can then share with others or embed.

> 🚧
>
> ### Tagged versions of data models are not available to Ask Sigma. If an admin chooses a data model to include in the data sources available to Ask Sigma, only the published version of that data model is available, and only users who have access to the published version can receive answers from Ask Sigma that reference that data model. For more information, see [Configure AI features for your organization](/docs/configure-ai-features-for-your-organization).

### User requirements

To tag a document version, the following must be true

* You are granted **Can Edit** permissions [on the document](/docs/folder-and-document-permissions).
* You are granted an [account type](/docs/license-and-account-type-overview) with the **Apply Tag** and **Create, edit, and publish workbooks** permissions enabled.

Some tags might be protected and require additional permissions to set on a document. To set a protected tag, you must also be assigned the Admin account type or be granted access to set the protected tag. If you do not have access to set the protected tag, you can send a request for it to be added. See [Create and manage version tags](/docs/create-and-manage-version-tags).

### Set a tag on a document

To set a tag on a document, follow these steps.

1. Open the document and locate the version that you want to tag:

   * To tag the latest published version of the document:

     1. Next to the document name, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the document menu.
     2. Select **Versions** > **Tag this version**. If the document is in draft and has unpublished edits, you instead see **Tag latest published version**.
   * To tag a specific version of the document:

     1. Next to the document name, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the document menu.
     2. Select **Versions** > **Version history**, then locate the version you want to tag.
     3. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Set tag on this version**.

   The **Set tag on version** modal appears.
2. For **Choose tag**, select a tag.

   If you choose a protected tag that you do not have permission to apply, you're prompted to send a request to approvers for the tag:

   1. For **Request reason**, enter a message to include in the email request to justify why you want to apply the protected tag to the document.
   2. Click **Request tag on version**.

      Sigma sends an email to users that can approve the request.
3. (Optional) If you want the tagged version of the document to use a different data source, select the checkbox for **Swap sources of the tagged version**. For example, use a different connection, database or catalog, table, data model, or dataset for the tagged version. See [Swap the source of a tagged version](#swap-the-source-of-a-tagged-workbook-version).

   > 📘
   >
   > ### If your document contains input tables or tables created through CSV uploads, do not choose this option. These elements cannot be migrated across connections.
4. (Optional) If you want users that only have access to the tagged version of the document to open the tagged version by default, select the checkbox for **Set this tag as default**. See [Set a default version tag for a document](#set-a-default-version-tag-for-a-document).
5. For a version tagged workbook, if you want to grant **Can view** access to the data sources used in the workbook, select the checkbox for **Allow user to use data sources when they "Save as"**. If this checkbox is not selected, users access the tagged version of the workbook without data.
6. Click **Set tag**.

> 🚩
>
> If your workbook has an input table, the tagged version of the workbook contains an empty copy of the input table that is separate from the input table in the source workbook. If you want to include the data present in the source workbook input table in the version tagged version, you must:
>
> 1. Change the data entry permission for the input table to allow editing ​​only on the published version in view/explore mode.
> 2. Apply the version tag.
> 3. Manually copy and paste the data into the empty table.
>
> If you want to migrate data from an input table in one data model version to a tagged data model version, you cannot add data in the published version of an input table in a data model so this workaround is unavailable.

### Set a default version tag for a document

When you apply a tag to a workbook or data model, you can set the tag as the default. The default tag determines what version of a document is displayed by default to a user who does not have access to the published version. If a user does have access to the published version, the published version takes precedence over the default tag.

> 📘
>
> ### If a user does not have access to the published version of a document and there is no default version tag set, the document loads the latest created tagged version that the user has access to.

Any user with **Can edit** access to a document can set a tag as the default:

1. Next to the document name, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the document menu.
2. Select **Versions** > **Version history**.
3. Locate the tagged version that you want to set as a default version, then select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**.
4. Click **Set tag as default**.

To remove a tag as default without replacing it with a different default tag, follow these steps:

1. Next to the document name, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the document menu.
2. Select **Versions** > **Version history**.
3. Next to the default version tag, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**.
4. Click **Remove as default**.

   ![Version history open displaying the East tag with the More menu open, showing Remove this tag and Remove as default options.](https://files.readme.io/14a319c-Screenshot_2024-05-29_at_10.29.24_AM.png)

### Remove a tag from a document version

When you remove a tag from a workbook or data model version, the version is still accessible from the version history, but anyone who only has access to the tagged version of the document loses access to the document.

> 💡
>
> You might remove a tag from a document version if you tagged the wrong document version or if you want to restrict access to users that only have access to the tagged version. If you want to update a tagged version, see [Make changes to a tagged workbook version](#make-changes-to-a-tagged-workbook-version) in this document.

To remove a tag from a document version:

1. Next to the document name, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the document menu.
2. Select **Versions** > **Version history**.

   > 💡
   >
   > To collapse the details changes for each version, select the down arrow next to the most recent version.
3. Locate the tagged version and select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Remove this tag**.

   The tagged version is shown on the canvas when you remove the tag.

## Swap the source of a tagged workbook version

> 📘
>
> ### If your workbook contains elements from multiple data sources, you cannot swap the source of the tagged workbook version.

To swap the source of a tagged workbook version, for example to use a test data connection for a workbook tagged "testing" and swap to a production data connection for a workbook tagged "production", follow these steps. The steps are different if your workbook uses a data model for the data source or not:

* [Swap the data model source used by a tagged workbook version](#swap-the-data-model-source-used-by-a-tagged-workbook-version).
* [Swap the dataset or connection source used by a tagged workbook version](#swap-the-dataset-or-connection-source-used-by-a-tagged-workbook-version).

For more details about changing a workbook data source, see [Change the data source for a workbook or element](/docs/change-the-data-source-for-a-workbook-or-element).

## Swap the data model source used by a tagged workbook version

If your workbook uses a data model as the data source and you want the tagged workbook version to use a different data source than the published version, first tag the data model and swap the source of the tagged data model, then tag the workbook and use the tagged data model as the source.

If the data model used by the workbook as a data source is based on another data model, tag the source data model as well.

> 💡
>
> If you swap the connection used by a data source, swapping the source by tagging a data model version instead of a workbook version helps you more easily manage and control access to data sources.

### Tag the data model and swap the source

1. Open the data model for editing, then choose the version to tag:

   * To tag the latest published version of the document:

     1. Next to the document name, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the document menu.
     2. Select **Versions** > **Tag this version**. If the document is in draft and has unpublished edits, you instead see **Tag latest published version**.
   * To tag a specific version of the document:

     1. Next to the document name, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the document menu.
     2. Select **Versions** > **Version history**, then locate the version you want to tag.
     3. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Set tag on this version**.

   The **Set tag on version** modal appears.
2. For **Choose tag**, choose a tag to apply to the data model. Choose the same tag that you plan to use with the workbook.
3. Select the checkbox for **Swap sources of the tagged version**.
4. Click **Set tag**.
5. In the **Swap sources** modal, in **Sources of tagged data model**, select a new data source to use for the tagged version. If you want to instead change the database or catalog, schema, or table, hover over the current object name, then click **Select** and choose a different object, then click **Confirm**.
6. Select **Swap and tag**.

### Tag the workbook and swap the source to the tagged data model

1. Open the workbook for editing, then choose the version to tag:

   * To tag the latest published version of the document:

     1. Next to the document name, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the document menu.
     2. Select **Versions** > **Tag this version**. If the document is in draft and has unpublished edits, you instead see **Tag latest published version**.
   * To tag a specific version of the document:

     1. Next to the document name, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the document menu.
     2. Select **Versions** > **Version history**, then locate the version you want to tag.
     3. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Set tag on this version**.

   The **Set tag on version** modal appears.
2. For **Choose tag**, choose the tag to apply to the workbook version.
3. Select the checkbox for **Swap sources of the tagged version**.
4. Click **Set tag**.
5. In the **Swap sources** modal, for **Sources of tagged workbook** open the drop-down menu and choose the corresponding tagged version of the data model.

   ![Modal as described, with a data model called Example Data Model and a table element called Events, showing the option to swap to a different tag of the same data model.](https://files.readme.io/4d1886d275d99028df07190d15f257e727a53b91005e44a9125b8fcdd967ada9-dm-swap-sources.png)
   > 📘
   >
   > ### If the workbook contains multiple data sources, you see the option to swap sources for each data source.
6. Select **Swap and tag**

## Swap the dataset or connection source used by a tagged workbook version

To select a different connection path, database, or schema for a tagged workbook version, do the following:

1. Open the workbook for editing, then choose the version to tag:

   * To tag the latest published version of the document:

     1. Next to the document name, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the document menu.
     2. Select **Versions** > **Tag this version**. If the document is in draft and has unpublished edits, you instead see **Tag latest published version**.
   * To tag a specific version of the document:

     1. Next to the document name, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the document menu.
     2. Select **Versions** > **Version history**, then locate the version you want to tag.
     3. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Set tag on this version**.

   The **Set tag on version** modal appears.
2. For **Choose tag**, choose the tag to apply to the workbook version.
3. Select the checkbox for **Swap sources of the tagged version**, then click **Set tag**
4. In the **Swap sources** modal, in **Sources of tagged data model**, select a new data source to use for the tagged version. If you want to instead change the database or catalog, schema, or table, hover over the current object name, then click **Select** and choose a different object, then click **Confirm**.
5. Click **Swap and tag**.

   The tagged version of the workbook is updated to use the new connection. If your workbook uses a dataset, a copy of the dataset is created on the new connection.

## Make changes to a tagged workbook version

If you want to make changes to a tagged version of a workbook, you must first return the tagged version to a draft, then make changes, publish the changes, and re-tag the version.

For example, if you follow a development lifecycle where you tag a workbook version with the "testing" tag before tagging a workbook with the "production" tag to indicate that it is ready to use in production, you might want to iterate on the testing tag.

To update the "testing" tagged version of the workbook, do the following:

1. Open the workbook for editing.
2. Next to the document name, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the document menu.
3. Select **Versions** > **Version history**.
4. Locate the tagged version and select the date of the associated version to open it.

   ![Version history showing a version published August 7, 2024 by Sigma Docs tagged with Staging.](https://files.readme.io/4f7450e-vt-staging-history.png)
5. For the version, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Restore version as draft**.

   ![Same version visible in version history, with the more menu open and showing options including Restore version as draft.](https://files.readme.io/13529dd-vt-restore-history.png)
6. Make your desired changes in the draft.
7. When you finish making changes, publish your changes.

   ![August 7 version showing as the current version of the document.](https://files.readme.io/f6c513b-vt-published-revert-edit-history.png)
8. Reopen the version history by clicking the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the document menu, then selecting **Versions** > **Version history**.

   In the version history, you see a line item for **Restored version from <date>**, then additional changes listed above that version.
9. For the latest published version that contains your changes, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More > Set tag on this version**.

   ![Same version visible in version history, with the more menu open and showing options including Set tag on this version.](https://files.readme.io/e86c23b-vt-set-tag-restored-version.png)

   The latest version is tagged, and the contents are updated to match. The version that was previously tagged is listed with a grayed-out version of the version tag.

   ![Version history showing a collapsed list of individual versions. The previously tagged version has a gray dot next to the Staging tag, while the currently tagged version has a brown dot, the color of the version tag, next to the Staging tag.](https://files.readme.io/7735fe3-vt-current-previous-tagged-versions.png)

> 📘
>
> ### Do not remove the testing tag from the previous version. If you do so, anyone that has access only to that tagged version of the workbook will lose access. If you re-tag a different version, sharing is preserved.

If you had other changes that you want to preserve and continue working with, return to the version before you restored the tagged version as the latest draft, and select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More > Restore version as draft**.

![Version history open and showing that the latest draft was restored from a version published at 12:20pm, which is the version just before the version that was edited and restored from the previously tagged staging version. It isn't super clear in the screenshot either.](https://files.readme.io/9713aa2-vt-restore-previous-draft-pub.png)

### Update a tagged version to use another tag

For example, if you want to promote a tagged workbook version from the "staging" version tag to the "production" version tag, do the following:

1. Open the workbook for editing.
2. Next to the document name, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the document menu.
3. Select **Versions**, then choose the tag that you want to view. For example, "Staging".

   The tagged version opens.
4. Open the document menu, then choose **Versions** > **Tag this version**.

   The **Set tag on version** modal opens.
5. In the modal, select any relevant options, then select **Set tag**.

   The "Production" tag is added to the version.
6. Next, remove the "Staging" tag from the version. Open the document menu, then select **Versions** > **Version history**.
7. In the version history, locate the version with the "Staging" tag applied, then select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Remove this tag**.

   ![August 7 version of the document showing both Production and Staging tags, with the more menu open and showing options including Remove this tag.](https://files.readme.io/1712217-vt-remove-staging-from-prod.png)
8. In the modal, acknowledge that users granted access only to this tagged version, or embeds that use the link to the tagged version, lose access to the tagged version after removing the tag by selecting **Remove**.

   The version appears with a current tag of "Production" and a previous tag of "Staging".

   ![August 7 version of the document showing both Production and Staging tags, but the color of the staging tag is Gray and if you hover over the tag it displays inactive.](https://files.readme.io/c46e9cc-vt-removed-staging.png)

## Restrict access to a folder using a version tag

If you use version tags to manage access to documents, you can set up a workspace or folder to manage access more easily.

You can share a workspace or folder with a user or teams, and grant those users or teams access to a specific tag. If you do so, workbooks or data models in that workspace or folder must have that tag applied to be accessible to those users or teams.

For example, if you have a sales organization that covers 5 regions, you can create a workspace for each region and grant each sales team **Can explore** access to their workspace with a tag for their region:

![Share folder modal open for a workspace, with the Sales US-East team listed with the Explore permission and hovering over the East tag for that permission level.](https://files.readme.io/570a7efde9e49719dd2bca78e939a1c5c4cde6a6e0dc011591348706cc44bb8d-share-folder.png)

If you do so, all documents in the workspace must have a corresponding tagged version. In this example, all workbooks in the Sales US-East workspace must have a version tagged **East** so that the members of the Sales US-East team can view and explore the **East** versions of the workbooks.

If you grant elevated permissions on the workspace to the team members, such as **Can contribute** or **Can manage**, those team members can access all versions of documents in the workspace.

Permissions set at the workspace and folder level are inherited by the workbooks and documents in the workspace or folder. For more details, see [Share a folder](/docs/share-a-folder).

## Link to a tagged version of a workbook

If you want to link directly to a tagged version of a workbook, for example to embed the tagged version of the workbook, reference the tag name in the URL.

For example, if you add a `staging` tag to a workbook, the URL for the workbook version tagged with `staging` contains the following:

```
/workbook/My-Workbook-{workbook_id}/tag/staging
```

To securely embed the tagged version of the workbook, use the URL containing the tag name.

The same construct applies for public embeds. The `staging` tag is appended to the URL:

```
/embed/{embed_id}/tag/staging
```

Like other URL parameters, version tag names with a space or special characters are encoded. For example, `staging%20copy` for a version tag named "Staging Copy". See [Embed URL parameters](/docs/embed-url-parameters).

Updated 3 days ago

---

[Workbook versions and version history](/docs/workbook-versions-and-version-history)[Workbook performance](/docs/workbook-performance)

* [Table of Contents](#)
* + [Version tagging workflow](#version-tagging-workflow)
  + - [How version tagging affects datasets and data models](#how-version-tagging-affects-datasets-and-data-models)
    - [Embedding tagged workbook versions](#embedding-tagged-workbook-versions)
    - [Version tagging and materialization](#version-tagging-and-materialization)
  + [Tag a workbook or data model version](#tag-a-workbook-or-data-model-version)
  + - [User requirements](#user-requirements)
    - [Set a tag on a document](#set-a-tag-on-a-document)
    - [Set a default version tag for a document](#set-a-default-version-tag-for-a-document)
    - [Remove a tag from a document version](#remove-a-tag-from-a-document-version)
  + [Swap the source of a tagged workbook version](#swap-the-source-of-a-tagged-workbook-version)
  + [Swap the data model source used by a tagged workbook version](#swap-the-data-model-source-used-by-a-tagged-workbook-version)
  + - [Tag the data model and swap the source](#tag-the-data-model-and-swap-the-source)
    - [Tag the workbook and swap the source to the tagged data model](#tag-the-workbook-and-swap-the-source-to-the-tagged-data-model)
  + [Swap the dataset or connection source used by a tagged workbook version](#swap-the-dataset-or-connection-source-used-by-a-tagged-workbook-version)
  + [Make changes to a tagged workbook version](#make-changes-to-a-tagged-workbook-version)
  + - [Update a tagged version to use another tag](#update-a-tagged-version-to-use-another-tag)
  + [Restrict access to a folder using a version tag](#restrict-access-to-a-folder-using-a-version-tag)
  + [Link to a tagged version of a workbook](#link-to-a-tagged-version-of-a-workbook)