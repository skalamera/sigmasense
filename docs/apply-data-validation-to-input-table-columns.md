# Apply data validation to input table columns

# Apply data validation to input table columns

Data validation ensures data accuracy and consistency by restricting data entry to a set of specific values. When you apply data validation to an input table column, users can only enter or select one of the predefined values from a dropdown.

> 📘
>
> ### Sigma only supports data validation for text, number, and date columns. Data validation doesn’t apply to checkbox data columns because Sigma already restricts the values to true (selected) or false (cleared).

This document explains how to apply data validation to input tables.

## System and user requirements

The ability to apply data validation to input tables requires the following:

* Your organization must be connected to a data platform compatible with input tables. See [Region, warehouse, and feature support](/docs/region-warehouse-and-feature-support).
* You must be granted **Can use** [data permission](/docs/data-permissions-overview) for a connection with write access enabled. *If using an OAuth-enabled connection, see[Configure OAuth with write access](/docs/configure-oauth-with-write-access) for additional requirements.*
* You must be assigned an [account type](/docs/user-account-types) with the **Create input tables** and **Create, edit, and publish workbooks** permissions enabled.
* You must be the workbook owner or be granted **Can edit** [workbook permission](/docs/folder-and-document-permissions).

## Apply data validation

1. Click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) in a column header to open the column menu, then select **Data validation**.
2. In the **Data validation** modal, create a manual list of predefined values, or apply the values from a column in an existing data source or element in the workbook:

   * Create a manual list of values:

     1. In the **Value source** dropdown, select **Create manual list**.
     2. In the **Define values** field, enter values that align with the column’s data type.

        > 💡
        >
        > ### Enter individual values, or paste multiple values copied from Sigma or an external source (like a spreadsheet or text document).
     3. Click **Save**.
   * Apply values from a column in an existing data source or element:

     1. In the **Value source** dropdown, select a data source or element.
     2. In the secondary dropdown, select a source column to define the values.
     3. Review the column values, then click **Save** to proceed.

     Sigma checks existing data against the defined values and displays red indicators in cells that contain invalid data.

     > 📘
     >
     > ### Sigma supports data validation against up to 100,000 values.

     ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Input+Tables/Create+and+Manage+Input+Tables/input-tables_configure_data-validation_step-2b.png)
3. To replace invalid data, manually enter valid values, or click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) in the cell and select a predefined value from the dropdown.

Updated 3 days ago

---

[Configure data governance options for input tables](/docs/configure-data-governance-options-for-input-tables)[Customize data entry permission on input tables](/docs/customize-data-entry-permission-on-input-tables)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Apply data validation](#apply-data-validation)