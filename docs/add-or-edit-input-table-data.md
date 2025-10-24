# Add or edit input table data

# Add or edit input table data

Depending on your [workbook access](/docs/folder-and-document-permissions) and the [data entry permission](/docs/customize-data-entry-permission-on-input-tables) on individual input table elements, you can directly add or edit input table data in the draft or published version of a workbook.

This document explains how to identify editable input tables, access the editable state, and add or edit data based on the workbook version you're interacting with.

For more information about how to change the data entry permission on a specific input table, see [Customize data entry permission on input tables](/docs/customize-data-entry-permission-on-input-tables). For general information about input tables, see [Intro to input tables](/docs/intro-to-input-tables).

## System and user requirements

The ability to add or edit data in existing input table columns requires the following:

* In a workbook draft:

  + You must be assigned an [account type](/docs/user-account-types) with the **Create, edit, and publish workbooks** permission enabled.
  + You must be the workbook owner or be granted **Can edit** [access to the workbook.](/docs/folder-and-document-permissions)
* In a workbook's published version:

  + You must be assigned an [account type](/docs/user-account-types) with the **Basic explore** permission enabled.
  + You must be the workbook owner or be granted **Can explore** or **Can edit** [access to the workbook](/docs/folder-and-document-permissions).

For permissions required to create new input tables and manage table structure, see [Create new input tables](/docs/create-new-input-tables). For permissions required to configure data governance features, see [Configure data governance options for input tables](/docs/configure-data-governance-options-for-input-tables).

## Identify editable input tables

Data entry permission is configured at the individual input table level, which can result in workbooks containing some input tables that are editable in the draft only and others that are editable in the published version only. Refer to the following sections to determine whether a specific input table is editable in the draft or public version of a workbook.

* [Identify editable input tables in a workbook draft](#identify-editable-input-tables-in-a-workbook-draft)
* [Identify editable input tables in a workbook's published version](#identify-editable-input-tables-in-a-workbooks-published-version)

### Identify editable input tables in a workbook draft

When interacting with a workbook draft, an input table element displays an **Editable in** label above the table, which indicates whether data entry is allowed in the draft or published version.

> 📘
>
> Data entry permission only affects your ability to add or edit data in existing input table columns. In the workbook draft, you can still customize the table structure, manage column settings, and configure data governance options, regardless of the data entry permission.

* If the element displays an **Editable in draft** label, the input table data is immediately editable. See [Add or edit data in a workbook draft](#add-or-edit-data-in-a-workbook-draft).

  ![](https://files.readme.io/70cfaf42f167d0b3dcb336fe264b455563ea512b6cd195ce3e3f0e411a6f6b18-image.png)
  > 🚧
  >
  > Input tables can be restricted from all edits when the connection used to write input table data to your data platform is unavailable or misconfigured. When this occurs, the element displays an "Editing restricted" warning message next to the **Editable in draft** label, and you cannot add or edit the input table data. If you encounter this restriction, contact your Sigma organization admin to resolve the issue. For more information, see [Input table error handling](/docs/troubleshoot-input-table-connection-issues#input-table-error-handling).
* If the element displays an **Editable in published version** label, the input table data is not immediately editable. To add or edit data, you can [change the data entry permission](/docs/customize-data-entry-permission-on-input-tables) or [switch to the workbook's published version](#add-or-edit-data-in-a-workbooks-published-version).

  ![](https://files.readme.io/ffcf57d70f399a180549fccd404b0b7347754a943c1b4b2d9f640db7948803f6-image.png)

### Identify editable input tables in a workbook's published version

When interacting with a workbook's published version, an input table element displays an ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/edit.svg) **Edit data** button if data entry is allowed in the publish version. Additional factors, described below, can determine whether you can access the editable state to add or edit data.

* If the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/edit.svg) **Edit data** button is displayed and enabled, you can access the editable state and directly add or edit data in existing columns. See [Add or edit data in a workbook's published version](#add-or-edit-data-in-a-workbooks-published-version).

  ![](https://files.readme.io/1c171986473a16e098212b31b571d8cc7ad3ff15dd1d43597bea34ed046cbc80-image.png)
* If the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/edit.svg) **Edit data** button is displayed but disabled, the input table is editable in the published version, but you cannot currently access the editable state to add or edit data. This restriction is likely due to insufficient workbook access. If necessary, contact the workbook owner to request an access upgrade.

  ![](https://files.readme.io/b52cd07cb24f79acac429ae90c3fd57b49b1ba41b6d695c7559b202dbda349f3-image.png)
  > 🚧
  >
  > Input table edits can also be restricted when the connection used to write input table data to your data platform is unavailable or misconfigured. When this occurs, the element displays an "Editing restricted" warning message next to the disabled button. If you encounter this restriction, contact your Sigma organization admin to resolve the issue. For more information, see [Input table error handling](/docs/troubleshoot-input-table-connection-issues#input-table-error-handling).
* If the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/edit.svg) **Edit data** button is not displayed, the input table is not editable in the published version. If you have the applicable workbook access, you can add or edit input table data in the draft (see [Add or edit data in a workbook draft](#add-or-edit-data-in-a-workbook-draft)). Otherwise, you can only view the input table.

  ![](https://files.readme.io/d048d7d3851dd1135c5f177131e1c54f0f164da220a2de052b5d50686fafa3fb-image.png)

## Add or edit data

When adding or editing input table data, the entry point to the editable state and the mechanism for saving your changes depend on the workbook version you're interacting with. Refer to the following workflows to add or edit input table data in the workbook draft or published version.

* [Add or edit data in a workbook draft](#add-or-edit-data-in-a-workbook-draft)
* [Add or edit data in a workbook's published version](#add-or-edit-data-in-a-workbooks-published-version)

### Add or edit data in a workbook draft

When an input table's data entry permission allows edits in the workbook draft, you can immediately add or edit data directly in the editable columns.

1. Open the draft of a workbook and locate the input table you want to edit.
2. If the input table element displays an **Editable in draft** label above the table, you can immediately add or edit data in editable columns using the following methods. If the element displays an **Editable in published version** label, you must first [change the data entry permission](/docs/customize-data-entry-permission-on-input-tables) or [switch to the workbook's published version](#add-or-edit-data-in-a-workbooks-published-version).

   > 📘
   >
   > Editable columns display a pencil icon (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/edit.svg)) in the column header. Linked columns (in linked input tables), calculations, lookups, and system columns are not editable.

   * To enter data through keyboard entry, select a cell and enter a value.
   * To paste copied values, select a cell or range of cells, then right-click the selection and select **Paste** (or use the `⌘`+`V` or `Ctrl`+`V` keyboard shortcut).

     > 💡
     >
     > You can select and paste values in up to 2,000 rows and 25 columns, including column headers. When you copy multiple rows of data and select a column header or range of cells that include a column header in the input table, the first row of copied data is pasted in the header.
   * To change a cell value in a checkbox column, click the checkbox to toggle between `true` (selected) and `false` (cleared). To remove the checkbox and generate a null value, select the cell and press `Delete`.
   * To select a predefined value in a [single-select column](/docs/configure-single-select-and-multi-select-columns-on-input-tables#add-a-single-select-column-to-an-input-table), a [multi-select column](/docs/configure-single-select-and-multi-select-columns-on-input-tables#add-a-multi-select-column-to-an-input-table), or a column containing [data validation](/docs/apply-data-validation-to-input-table-columns), click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) in a cell (or double-click the cell), then select an option from the dropdown.
   * To define values in a calculation column, click the column header or any cell in the column, then enter an expression in the formula bar.

     > 💡
     >
     > If the formula bar is not visible, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/show-panels.svg) **Show panels** in the workbook header to reveal the toolbar (containing the formula bar) and editor panel.
3. Sigma automatically saves all edits to the draft. To save your changes to the workbook's published version, click **Publish** in the workbook header.

   > 🚧
   >
   > Input table edits can be unsuccessful due to configuration or availability issues in the connection or data platform (which must be resolved by the customer). To improve data integrity and prevent unexpected data loss when a connection is misconfigured or unavailable, Sigma blocks edits to relevant input tables and displays an "Editing restricted" message directly on the input table elements. If you're restricted from editing an input table due to a misconfigured or unavailable connection, contact your Sigma organization admin to resolve the issue. For more information, see [Input table error handling](/docs/troubleshoot-input-table-connection-issues#input-table-error-handling).

### Add or edit data in a workbook's published version

When an input table's data entry permission allows edits in the workbook's published version, you can access the input table's editable state to add or edit data directly in existing editable columns.

1. Open the published version of a workbook and locate the input table you want to edit.

   To switch from the draft to the published version, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) next to the **Publish** button in the workbook header, then select **Go to published version**.

   ![](https://files.readme.io/1d6590faf9632ac68b5580dd4445384bc5272f9fd7c861e33a5dd2ec9ad1fa12-image.png)
2. In the input table element, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/edit.svg) **Edit data** to enable editing.

   If the button is disabled, you cannot access the editable state. See [Identify editable input tables in a workbook's published version](#identify-editable-input-tables-in-a-workbooks-published-version) for more information.
3. Use the following methods to add or edit data in existing editable columns:

   > 📘
   >
   > Editable columns display a pencil icon (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/edit.svg)) in the column header. Linked columns (in linked input tables), calculations, lookups, and system columns are not editable.

   * To enter data through keyboard entry, select a cell and enter a value.
   * To paste copied values, select a cell or range of cells, then right-click the selection and select **Paste**, or use the `⌘`+`V` or `Ctrl`+`V` keyboard shortcut.

> 💡
>
> You can select and paste values in up to 2,000 rows and 25 columns, not including column headers since you cannot edit headers in the published version of a workbook.

* To change a cell value in a checkbox column, click the checkbox to toggle between `true` (selected) and `false` (cleared). To remove the checkbox and generate a null value, select the cell and press `Delete`.
* To select a predefined value in a [single-select column](/docs/configure-single-select-and-multi-select-columns-on-input-tables#add-a-single-select-column-to-an-input-table), a [multi-select column](/docs/configure-single-select-and-multi-select-columns-on-input-tables#add-a-multi-select-column-to-an-input-table), or a column containing [data validation](/docs/apply-data-validation-to-input-table-columns), click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) in a cell (or double-click the cell), then select an option from the dropdown.
* To define values in a calculation column, click the column header or any cell in the column, then enter an expression in the formula bar.

> 💡
>
> If the formula bar is not visible, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/show-panels.svg) **Show panels** in the workbook header to reveal the toolbar (containing the formula bar) and editor panel.

4. The input table displays yellow cell indicators to mark cells with unsaved data. Click **Save** to apply your changes to the draft and published version.

   ![](https://files.readme.io/33b5500bf0374df21faaae9c8d24ea652c717fda236c9126fb0c2374cf390709-image.png)
   > 🚧
   >
   > Input table edits can be unsuccessful due to configuration or availability issues in the connection or data platform (which must be resolved by the customer). To improve data integrity and prevent unexpected data loss when a connection is misconfigured or unavailable, Sigma blocks edits to relevant input tables and displays an "Editing restricted" message directly on the input table elements. If you're restricted from editing an input table due to a misconfigured or unavailable connection, contact your Sigma organization admin to resolve the issue. For more information, see [Input table error handling](/docs/troubleshoot-input-table-connection-issues#input-table-error-handling).

Updated 3 days ago

---

[Create new input tables](/docs/create-new-input-tables)[Configure single-select or multi-select columns on input tables (Beta)](/docs/configure-single-select-and-multi-select-columns-on-input-tables)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Identify editable input tables](#identify-editable-input-tables)
  + - [Identify editable input tables in a workbook draft](#identify-editable-input-tables-in-a-workbook-draft)
    - [Identify editable input tables in a workbook's published version](#identify-editable-input-tables-in-a-workbooks-published-version)
  + [Add or edit data](#add-or-edit-data)
  + - [Add or edit data in a workbook draft](#add-or-edit-data-in-a-workbook-draft)
    - [Add or edit data in a workbook's published version](#add-or-edit-data-in-a-workbooks-published-version)