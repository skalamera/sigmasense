# Review and manage your data catalog

# Review and manage your data catalog

For each data source connected to Sigma, you can review and manage the data catalog. Explore the databases or catalogs, schemas, and tables available in Sigma, and add descriptions and other metadata to tables and columns.

> 💡
>
> Comments in your database or catalog information schema are automatically available in Sigma.

Table badges, descriptions, and column descriptions are available downstream, helping business users make decisions about which tables and columns to use in a given analysis.

To further model the data from your data platform, you can also create a data model or dataset in Sigma:

* [Create a data model from a table](/docs/create-and-manage-data-models).
* [Create a dataset from a table](/docs/create-and-manage-datasets).

## System and user requirements

The ability to manage your data catalog in Sigma requires the following:

* Your organization must be [connected to a data source](/docs/connect-to-data-sources).
* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Manage connections** permission enabled.
* You must be granted **Can use & annotate** [access](/docs/data-permissions-overview) to the connection.

## Annotate tables with metadata

Add metadata to data catalog tables in Sigma, such as table descriptions, a badge to indicate certification status, column descriptions and data types, and configure additional column settings.

Table and column descriptions are visible to business users interacting with the data table, either by hovering over a given column in a workbook or when viewing the lineage of a data model using the database table as a data source.

### Find relevant tables

Start by locating the relevant tables that you want to annotate:

1. From Sigma Home, select **Connections** to open the list of connected data sources.
2. Select the data connection with the data catalog that you want to view.
3. In the left navigation panel, search or browse the data catalog to locate the table that you want to annotate.

   ![Data catalog for the connected data source, with an EVENTS table selected.](https://files.readme.io/563a7477ed80e266ea5e279dd44c75a7901a1106c90c80eb74734bdeb270f6bf-view-data-catalog.png)

### Add table descriptions

After locating the table in your data catalog, add a description:

1. Navigate to the table in the data catalog.
2. Select the table name to open the table.
3. In the upper right, select **Edit**.
4. Next to the table name, select **More info** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/info-circle-filled.svg)).
5. In the popover that appears, enter a description in the **Description** field.

   ![More info options for sample EVENTS table, showing a description, badge, connection, last updated, and last synced information for the table.](https://files.readme.io/9427d4eb8011689db736f8f38af96a6abbdb7879c19a948db8c7182c9ea74769-edit-table-descr-db-table.png)
6. To save your changes, select **Publish**.

### Add or update a badge

Add or update a certification badge to indicate the status, quality, and reliability of the data.

1. Navigate to the table in the data catalog.
2. Select the table name to open the table.
3. Next to the table name, select **More info** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/info-circle-filled.svg)).
4. In the popover, select an option from the **Badge** dropdown.

   ![More info options for a sales targets table, showing available badge options of Endorsed, Warning, Deprecated or none.](https://files.readme.io/78287f84edecad3e43dfabc88333e7bd32f9c6cbb4c9ce786d540c74d33b48b2-2025-02-13_23-12-13.png)
5. (Optional) When you select a badge, the popover displays the **Badge note** field. Add a note to provide context about the badge.

   ![](https://files.readme.io/1f561bb406350a33516423ea091c28754a95019249c2f0705029bab7e324d188-2025-02-13_23-40-41.png)
   The badge is automatically saved and immediately reflected by the table icon in the left panel.

### Add column descriptions

Add descriptions to your columns to provide additional metadata and guidance for users of the data source:

1. Navigate to the table in the data catalog.
2. Select the table name to open the table.
3. In the upper right, select **Edit**.
4. Select the **Columns** tab.
5. In the **Description** column, add a description for any column in the table.

   ![Events table with the Columns tab open and the column name, friendly name, visibility type, format, and description columns shown.](https://files.readme.io/cb0b2139d79fbdf4299ff32ddec3e859ac7e12c2be26834f4ebbb2c2837eb53c-update-columns-db-table.png)
6. To save your changes, select **Publish**.

## Format columns

To change the format of data in a column, for example to display numeric data with currency formatting, format columns in the table:

1. Navigate to the table in the data catalog.
2. Select the table name to open the table.
3. In the upper right, select **Edit**.
4. Select the **Columns** tab.
5. Locate the column that you want to format.
6. For **Format**, choose the formatting option that you want to apply to the column. Formatting options depend on the data type of the column. For example, for a numeric column, select **Currency**.
7. To save your changes, select **Publish**.

## Specify a primary key (Beta)

> 🚩
>
> This documentation describes one or more public beta features that are in development. Beta features are subject to quick, iterative changes; therefore the current user experience in the Sigma service can differ from the information provided in this page.
>
> This page should not be considered official published documentation until Sigma removes this notice and the beta flag on the corresponding feature(s) in the Sigma service. For the full beta feature disclaimer, see [Beta features](/docs/sigma-product-releases#beta-features).

Specify a primary key column for a table in your data source that Sigma can use to optimize the SQL generated for performing joins when [related columns are added to a workbook](/docs/use-related-columns-in-a-workbook) and when [columns are added via lookup](/docs/add-columns-through-lookup), such as with the [Lookup()](/docs/lookup) function.

When related and lookup columns are added to a workbook, Sigma performs a lookup join. If you have a primary key specified on the data source table used in the [data model that is part of a relationship](/docs/define-relationships-in-data-models), Sigma can instead perform a more efficient left join, generating more performant SQL and making it more efficient to use related columns in workbooks. For more details, see See the Snowflake documentation on [Understanding How Snowflake Can Eliminate Redundant Joins](https://docs.snowflake.com/en/user-guide/join-elimination).

> 📘
>
> This functionality is only available to a limited number of organizations on Snowflake connections.

1. From Sigma Home, select **Connections** to open the list of connected data sources.
2. Select the data connection with the data catalog that you want to view.
3. In the left navigation panel, search or browse the data catalog to locate the table to which you want to add a primary key.
4. Select the table name to open the table.
5. In the upper right, select **Edit**.
6. Select the **Columns** tab.
7. In the **Primary key** section at the top of the columns list, choose a column to use as the primary key when performing joins.

   > 💡
   >
   > If you have a primary key specified on a table in your data platform, it is already selected.

   ![Data catalog open for the Sigma Sample Database connection, with the TRIPS tables selected and open for editing on the Columns tab. The primary key section at the top appears with a dropdown menu that lists the columns available.](https://files.readme.io/ff1371743750afa8009e3993543e8f8b4c3f019abfc6b0850e85acf9680e7c44-pk-columns.png)
8. Leave the **Trust uniqueness for optimization** checkbox selected to indicate that the selected column contains a unique value for every row in the table.

   ![TRIPS table selected and open for editing on the Columns tab. The ID column is selected as a primary key and the Trust uniqueness for optimization checkbox is automatically selected.](https://files.readme.io/688b85151e253d07387fd7eef636814fc9f86b11fd8cd0915c2ed742c0b053c3-pk-checkbox.png)

   If you have the RELY constraint property set in Snowflake for the table, the checkbox is automatically selected.
9. To save your changes, select **Publish**.

Updated 3 days ago

---

Related resources

* [Modeling Best Practices](/docs/modeling-best-practices)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Annotate tables with metadata](#annotate-tables-with-metadata)
  + - [Find relevant tables](#find-relevant-tables)
    - [Add table descriptions](#add-table-descriptions)
    - [Add or update a badge](#add-or-update-a-badge)
    - [Add column descriptions](#add-column-descriptions)
  + [Format columns](#format-columns)
  + [Specify a primary key (Beta)](#specify-a-primary-key-beta)