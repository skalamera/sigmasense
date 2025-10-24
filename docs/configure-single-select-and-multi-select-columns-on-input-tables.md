# Configure single-select or multi-select columns on input tables (Beta)

# Configure single-select or multi-select columns on input tables (Beta)

> 🚩
>
> This documentation describes one or more public beta features that are in development. Beta features are subject to quick, iterative changes; therefore the current user experience in the Sigma service can differ from the information provided in this page.
>
> This page should not be considered official published documentation until Sigma removes this notice and the beta flag on the corresponding feature(s) in the Sigma service. For the full beta feature disclaimer, see [Beta features](/docs/sigma-product-releases#beta-features).

Use single-select and multi-select columns in input tables to enable users to add discrete values as follows:

* Single-select: Users can select one value per row from a predefined list of values. When a user makes a new selection, it replaces the existing row value.
* Multi-select: Users can select one or more values per row from a predefined list of values. When a user makes a new selection, it adds the selected value to the existing row values.

You can manually create and manage a list of distinct and repeatable values, or you can populate the list of values from a column in an existing data source or element in the workbook. Values can then be formatted as pills and assigned different colors for visual differentiation and clarity.

This document explains how to add a single-select or multi-select column to an input table and configure the list of values available for users to select. For information about using single-select and multi-select columns, see [Add or edit input table data](/docs/add-or-edit-input-table-data).

## System and user requirements

The ability to create a new input table and configure a single-select or multi-select column requires the following:

* You must have **Can use** access to a connection that supports input tables and has write access enabled.
  + If using input tables on an OAuth-enabled connection, see [Configure OAuth with write access](/docs/configure-oauth-with-write-access) for additional requirements.
  + If using input tables on an Amazon Redshift connection, the `enable_case_sensitive_identifier` configuration value in Redshift must be set to `false`. If set to `true`, attempts to create or edit input tables will fail.
* You must be assigned an [account type](/docs/account-type-and-license-overview) with the **Create input tables** and **Create, edit, and publish workbooks** permissions enabled.
* You must be the workbook owner or have **Can edit** access to the workbook. *Unlike other workbook elements, input tables cannot be created in custom views. You can only create new input tables in the workbook draft.*

For information about permissions required to edit input table data, see [Add or edit input table data](/docs/add-or-edit-input-table-data).

## Add a single-select column to an input table

Add a single-select column that allows users to select one value per row from a predefined list of values. Single-select columns support text, number, and date data.

1. [Create a new input table](/docs/create-new-input-tables) or select an existing one.
2. In the input table, click the plus (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg)) icon at the end of the column header, then hover over **Single-select** and select a data type (**Text**, **Number**, or **Date**) from the dropdown.

   ![](https://files.readme.io/c3a61d3081cad550d47bc4fd48ecd0be6459a70a93446434af7c49c8bdb52a33-image.png)

   Sigma adds a single-select column to the input table and opens the **Edit values** popover, which allows you to [define and format a list of available values](#define-and-format-the-list-of-available-values).

   ![](https://files.readme.io/e822580b8ace4d536d330420aa3439705dab4fa0ed0626058fcac941d4cb3d68-image.png)

## Add a multi-select column to an input table

Add a multi-select column that allows users to select one or more values per row from a predefined list of values. Multi-select columns are variant columns that support text arrays.

1. [Create a new input table](/docs/create-new-input-tables) or select an existing one.
2. In the input table, click the plus (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg)) icon at the end of the column header, then select **Multi-select** from the dropdown.

   ![](https://files.readme.io/59548a17a45bc87ed9d107262cec0066daea8503fba30dc1da235c609ec39504-image.png)

   Sigma adds a multi-select column to the input table and opens the **Edit values** popover, which allows you to [define and format a list of available values](#define-and-format-the-list-of-available-values).

   ![](https://files.readme.io/3e284d130ef544f6988beb215c9a719dd4400e3a3fbca3c62d7a19b428dbe754-image.png)

## Define and format the list of available values

There are two ways to define the list of available values in a single-select or multi-select column:

* [Manually create and manage the list of values](#manually-create-and-manage-the-list-of-values)
* [Choose an existing data source or element to populate the list of values](#choose-an-existing-data-source-or-element-to-populate-the-list-of-values)

Multi-select column values are always formatted as pills (with a round-ended background behind the text) in both the cell and the value selection dropdown. The pill format helps differentiate between individual values. When managing a single-select column, however, you can choose whether or not to format values as pills.

### Manually create and manage the list of values

Manually create a list of available values, then customize the order and (optionally) assign a display color to each value. For single-select columns, you can also choose whether or not to format values as pills.

1. In the single-select or multi-select column's header, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) and select **Edit values** from the column menu.
2. In the **Edit values** modal, configure the list of available values:

   1. In the **Value source** field, select **Create manual list**.
   2. In the **Define values** section, add, edit, or remove values:

      * To add a new value, click the **Add text value** (for single-select) or **Add value** (for multi-select) input field, then enter a value. Press the `Enter` key to open a new input field and add another value.
      * To edit an existing value, click the applicable field and edit the value.
      * To remove a specific value, hover over the applicable field and click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/square_close.svg) **Remove**.
      * To remove all values, click **Clear all**.
   3. [optional] To reorder the list, click and drag any value's drag handle (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/drag-handle-dots.svg)).
   4. [optional] If managing a single-select column, select the **Format as pills** checkbox to display values as pills. Clear the **Format as pills** checkbox to display unstyled values.
   5. [optional] Assign pill colors to individual values:

      * To manually assign a color to each value, click the applicable color swatch, then choose a color from the color picker.
      * To automatically assign a color to each value as it's added, select the **Assign categorical colors when items are added** checkbox. Only values added after you change the setting are affected—colors assigned to existing values do not change.
   6. Click **Save**.

      > 📘
      >
      > With multi-select columns, you can also add to the list of available values by entering a new value directly in a cell (in the workbook draft only). To reorder or manually assign a pill color to a new value, however, you must access the **Edit values** modal.

      ![](https://files.readme.io/c4d8ebde86d94c280aa7c69dfa4088ffd814d091f91124fc4f2fe848433cb655-image.png)

### Choose an existing data source or element to populate the list of values

Automatically populate a list of available values by referencing a column from an existing data source or element in the current workbook. The values users can select in the single-select or multi-select column are based on values in the source column and can change in real time as the source column values are updated.

> 📘
>
> * You can only reference a text, number, or date column.
> * When referencing a source column for single-select column values, the data type automatically changes to the source column data type when it's text, number, or date.
> * When referencing a source column for multi-select column values, the data type is always text. Numbers and dates convert to text.

1. In the single-select or multi-select column's header, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) and select **Edit values** from the column menu.
2. In the **Edit values** modal, configure the list of available values:

   1. In the **Value source** field, select a data source or element.
   2. In the secondary field, select a column from the selected data source or element.
   3. In the **Preview values** section, confirm that these are the values users must be able to select in the column.
   4. [optional] If managing a single-select column, select the **Format as pills** checkbox to display values as pills. Clear the **Format as pills** checkbox to display unstyled values.
   5. [optional] Assign pill colors to individual values:

      * To manually assign a color to each value, click the applicable color swatch, then choose a color from the color picker.
      * To automatically assign a color to each value, select the **Assign categorical colors to items** checkbox.
   6. Click **Save**.

      ![](https://files.readme.io/09fb2da17fa8969af5c986371f20472e784ca5a597f19565886e3f84558588f8-image.png)

Updated 3 days ago

---

[Add or edit input table data](/docs/add-or-edit-input-table-data)[Configure data governance options for input tables](/docs/configure-data-governance-options-for-input-tables)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Add a single-select column to an input table](#add-a-single-select-column-to-an-input-table)
  + [Add a multi-select column to an input table](#add-a-multi-select-column-to-an-input-table)
  + [Define and format the list of available values](#define-and-format-the-list-of-available-values)
  + - [Manually create and manage the list of values](#manually-create-and-manage-the-list-of-values)
    - [Choose an existing data source or element to populate the list of values](#choose-an-existing-data-source-or-element-to-populate-the-list-of-values)