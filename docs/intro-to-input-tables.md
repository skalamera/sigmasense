# Intro to input tables

# Intro to input tables

> 🚩
>
> Input tables are generally available on Amazon Redshift, BigQuery, Databricks, and Snowflake connections when [write access](/docs/set-up-write-access) write-access is enabled.
>
> On PostgreSQL connections, input tables are a public beta feature in development. Beta features are subject to quick, iterative changes; therefore the current user experience in the Sigma service can differ from the information provided in this page.
>
> Official public beta support for input tables is available for connections to PostgreSQL 14 or higher running on one of the following self- or cloud-managed services:
>
> * PostgreSQL instance (self-managed)
> * Google Cloud SQL for PostgreSQL
> * Azure Database for PostgreSQL
> * Amazon RDS for PostgreSQL
>
> See [Connect to PostgreSQL](/docs/connect-to-postgresql#create-a-user-with-the-necessary-data-permissions) for information about schema grants.
>
> For PostgreSQL connections, this page should not be considered official published documentation until Sigma removes this notice and the beta flag on the corresponding features in the Sigma service. For the full beta feature disclaimer, see [Beta features](/docs/sigma-product-releases#beta-features).

Input tables are dynamic workbook elements that support structured data entry. They allow you to integrate new data points into your analysis and augment existing data from your data platform to facilitate rapid prototyping, advanced modeling, forecasting, what-if analysis, and more—without overwriting source data.

Use input tables as sources for tables, pivot tables, and visualizations, or incorporate the data using lookups and joins. And when you [create warehouse views](/docs/create-and-manage-workbook-warehouse-views) for input tables, you can reuse the manually entered data across your broader data ecosystem.

This document introduces the fundamentals of input tables (functionality, types, and columns), and explains how Sigma handles the data.

## Input table functionality

Input tables enable you to do the following:

* Add new rows (empty and CSV input tables only)
* Add new columns (including data entry, computed, row edit history, and system columns)
* Upload and edit CSV data (max 200 MB, UTF-8 only)
* Input values through keyboard entry
* Paste up to 2,000 rows and 25 columns from your clipboard
* Configure data entry permissions
* Configure data validation
* Protect columns to prevent edits

For information about using this functionality, see [Create new input tables](/docs/create-new-input-tables), [Configure data governance options in input tables](/docs/configure-data-governance-options-in-input-tables), and [Edit existing input table columns](/docs/edit-existing-input-table-columns).

## Types of input tables

Sigma offers three types of input tables:

* [Empty input tables](#empty-input-tables)
* [CSV input tables](#csv-input-tables)
* [Linked input tables](#linked-input-tables)

### Empty input tables

Empty input tables are blank tables that support data entry in standalone tables independent of existing data. You can edit data at the cell level and add editable rows and columns to construct your table as you see fit.

![](https://files.readme.io/2bc3261-image.png)

### CSV input tables

CSV input tables also support data entry in standalone tables; however, they allow you to pre-populate the table with uploaded CSV data (max 200 MB, UTF-8 only). You can then edit the uploaded data at the cell level and add other editable rows and columns to construct your table as you see fit.

### Linked input tables

Linked input tables support data entry alongside existing data from other elements in the same workbook.

As a child element, a linked input table includes one or more linked columns that reference data in the parent element. This includes a primary key column containing row identifiers that establish the table’s granularity. You can then add other columns to augment the linked data sourced from the parent element.

To maintain the data relationship between the input table rows and source data in the parent element, the primary key column must reference static values. All other linked columns can reference variable data, which is continually updated in the input table to reflect live data from the source.

> 🚧
>
> Do not use a calculated column as a primary key column. Using calculated columns, especially generated row numbers (such as from the [RowNumber()](/docs/rownumber) function) , as primary keys in linked input tables can lead to inconsistent behavior in your workbook. Since these keys are derived from calculations, they can change with data modifications, such as inserts, deletes or simple edits. This instability may result in:
>
> * **Duplicate Keys**: Changes in row order can lead to duplicates, violating key constraints.
> * **Data Integrity Issues**: Relationships relying on these keys may break, causing referential integrity problems.
>
> Primary keys should always be stable, unique identifiers, preferably derived from underlying stable data.

![](https://files.readme.io/3e77b05-image.png)

## Types of input table columns

Input tables support the following types of columns:

| Type | Description | Available columns |
| --- | --- | --- |
| Data entry column | Supports direct user input at the individual cell level | **Text**, **Number**, **Date**, **Checkbox**, **Multi-select** |
| Computed column | Generates values based on a user-defined formula or lookup | **Calculation**, **Via lookup** |
| Row edit history column | Displays system-generated metadata related to row-level edits | **Last updated at**, **Last updated by**, **Created at**, **Created by** |
| System column | Displays system-generated metadata related to table components | **Row ID**  *Available for empty or CSV input tables only* |

## Input table data governance

Data governance features (data validation and data entry permissions) allow you to preserve data integrity and enhance the security of input tables. You can also include system-generated columns (row edit history and row ID) to surface input table metadata for auditing and other data management purposes.

For more information, see the following documentation:

* [Apply data validation to input table columns](/docs/apply-data-validation-to-input-table-columns)
* [Customize data entry permission on input tables](/docs/customize-data-entry-permission-on-input-tables)
* [Add system-generated columns to input tables](/docs/add-system-generated-columns-to-input-tables)

## How input table data is handled

Sigma handles input tables in a distinct manner due to the ad hoc nature of the data. The following information explains how input table data is stored, retrieved, and removed.

### Storage

Sigma writes input table data to tables in a designated write-back schema in your data platform. This destination schema, identified in the connection's details (**Admin** > **Connections**), stores input table data separate from existing source data that Sigma cannot overwrite.

In addition to creating tables that store input table data, Sigma creates an edit log (also known as a write-ahead log or WAL) that contains a sequential record of all input table changes, including information related to user activity and resulting system operations. Tables containing input table data have object names prepended with `SIGDS`, and the table containing the edit log is prepended with `SIGDS_WAL`.

### Retrieval

Since Sigma writes input table data to a write-back schema optimized for storage, you cannot query the resulting tables directly. To access input table data in an indirect but query-friendly format, [create warehouse views](/docs/create-and-manage-workbook-warehouse-views) for individual input tables, then retrieve the data from the views using the SQL `FROM` clause.

### Removal

You can delete input table *elements* in workbooks, but Sigma does not delete the corresponding input table data written to your data platform. To remove this data, you must delete it directly in the data platform.

Updated 3 days ago

---

Related resources

* [Create and manage input tables](/docs/create-and-manage-input-tables)
* [Edit existing input table columns](/docs/edit-existing-input-table-columns)
* [Configure data governance options in input tables](/docs/configure-data-governance-options-in-input-tables)
* [Restore input table access for a Snowflake connection or user](/docs/restore-input-table-access-for-a-snowflake-connection-or-user)

* [Table of Contents](#)
* + [Input table functionality](#input-table-functionality)
  + [Types of input tables](#types-of-input-tables)
  + - [Empty input tables](#empty-input-tables)
    - [CSV input tables](#csv-input-tables)
    - [Linked input tables](#linked-input-tables)
  + [Types of input table columns](#types-of-input-table-columns)
  + [Input table data governance](#input-table-data-governance)
  + [How input table data is handled](#how-input-table-data-is-handled)
  + - [Storage](#storage)
    - [Retrieval](#retrieval)
    - [Removal](#removal)