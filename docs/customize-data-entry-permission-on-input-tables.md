# Customize data entry permission on input tables

# Customize data entry permission on input tables

Data entry permission allows you to control who can edit input table data and when. For individual input tables, you can specify which workbook version (draft or published) allows users to add rows and edit cell values.

This document explains how to change the data entry permission on individual input tables.

## System and user requirements

The ability to configure data entry permission on input tables requires the following:

* Your organization must be connected to a data platform compatible with input tables. See [Supported regions, data platforms, and features](/docs/region-warehouse-and-feature-support).
* You must be granted **Can use** [data permission](/docs/data-permissions-overview) for a connection with write access enabled. *If using an OAuth-enabled connection, see Configure OAuth with write access for additional requirements.*
* You must be assigned an [account type](/docs/create-and-manage-account-types) with the **Create input tables** and **Create, edit, and publish workbooks** permissions enabled.
* You must be the workbook owner or be granted **Can edit** [workbook permission](/docs/folder-and-document-permissions).

## Set the data entry permission

Set the data entry permission on an individual input table to specify which workbook version (draft or published) allows users to add rows and edit values to that specific input table.

> 📘
>
> The ability to create and build input tables is always restricted to the draft version, meaning only users granted **Can edit** workbook permission can [add new input tables](/docs/create-new-input-tables#create-a-new-input-table) to the workbook and [modify the table structure](/docs/create-new-input-tables#customize-input-table-structure). By default, data entry is also limited to the draft version of the workbook, but you can change the permission on individual input tables to instead allow edits in the published version. When an input table is editable in the published version, users with either **Can explore** or **Can edit** workbook permission can interact with the input table data.

For more information about the data entry workflow in a workbook draft versus the published version, see [Edit existing input table columns](/docs/edit-existing-input-table-columns).

1. Open the draft version of the workbook containing the input table you want to update.
2. In the input table element, click the **Editable in** label and select one of the following options from the dropdown:

   |  |  |
   | --- | --- |
   | **Only editable in draft** | Allows users granted **Can edit** workbook permission to edit input table data in the draft version of the workbook. |
   | **Only editable in published version** | Allows users granted **Can explore** or **Can edit** workbook permission to edit input table data in the published version of the workbook, including custom views. |

   > 📘
   >
   > You can toggle data entry between the draft and published versions as needed, but the workbook cannot support data entry in both simultaneously.

   ![](https://files.readme.io/cc6ab366922a8a0667e785e100653f462454da97e230ee5857623dfd0fd31666-image.png)
3. Before you publish the workbook with the updated data entry permission, the input table element displays a **Pending publish** notification to indicate that the selected permission is not yet in effect. To apply the data entry permission update, click **Publish** in the workbook header.

   ![](https://files.readme.io/e927c83d2679f9e2ecd467d5165d6eca19e9ed65ef82eb4b05c33deef949c4e6-image.png)

Updated 3 days ago

---

[Apply data validation to input table columns](/docs/apply-data-validation-to-input-table-columns)[Add system-generated columns to input tables](/docs/add-system-generated-columns-to-input-tables)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Set the data entry permission](#set-the-data-entry-permission)