# Write custom SQL

# Write custom SQL

When you explore your data platform using the SQL editor, you can preview SQL queries and create workbooks, data models, and datasets directly from SQL.

This document describes how to do the following:

* [Create a workbook from SQL](#create-a-workbook-from-sql)
* [Create a SQL workbook element](#create-a-sql-workbook-element)
* [Reference existing Sigma workbook elements](#reference-existing-sigma-workbook-elements)
* Use [shortcuts](#shortcuts), including:
  + Toggle within SQL-based workbook data elements to an inline SQL editor with side-by-side display.
  + Auto-format your SQL query.
  + Use find and replace within your SQL query.

## Requirements

* To use this feature, you must be assigned an [account type](/docs/license-and-account-type-overview) with the **Write SQL** permission enabled.
* To run custom SQL, you must be granted **Can use** access for an entire connection. See [Manage access to data and connections](/docs/manage-data-permissions).
* The SQL editor only appears if you have connection-level access to at least one connection in your organization.

## Limitations and considerations

### Query limitations

* Sigma does not allow more than one query per custom SQL element. This limitation applies to statements such as `SET` and `USE DATABASE` run before another query.
  + To store and use a variable in custom SQL, consider [referencing a workbook control value](/docs/reference-workbook-control-values-in-sql-statements).
  + To change the database or schema, consider using [dynamic schema selection](/docs/reference-workbook-control-values-in-sql-statements#return-rows-based-on-a-schema-text-selector) or explicitly stating database and schema in your query.

### Row and column order limitations

* Because Sigma incorporates your SQL query into an optimized query with other workbook contents, sort orders defined in your custom SQL cannot be guaranteed. To guarantee sort order for records in a custom SQL element, apply a sort from the table UI.
* Because users can change column order in both the table UI and the SELECT statement of a SQL query, Sigma stores the column order according to the first query run for each custom SQL element. This has the following consequences:
  + Changes to column order made in the table UI after the first run will be respected, but changes to column order made in the SELECT statement after the first run may not be.
  + To return columns in the order defined in the SELECT statement of your custom SQL query, create a new custom SQL element, copy your query into it, and run your query. This must be the first query run in that custom SQL element.

### Considerations

* Sigma converts all timestamps to your organization’s timezone. This has the following consequences:
  + If a column in your data platform has timezone data, Sigma converts the timestamp to your organization’s timezone while preserving the moment in time. For example, a column stating the timestamp `2025-09-10 10:00:00.000` for the `America/New_York` timezone is converted to `2025-09-10 07:00:00.000` if your Sigma organization has the `America/Los_Angeles` timezone.
  + If a column in your data platform has no timezone, Sigma interprets it as if it is in your organization’s timezone, but does not convert the timestamp.

See [How Sigma displays date data](/docs/account-time-zone#how-sigma-displays-date-data) for more details.

## Create a workbook from SQL

To create a workbook from a SQL query, do the following:

1. Open **Sigma Home**.
2. In the navigation panel, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Create New**, then select **Write SQL** to open the SQL editor.

   ![Create New menu open and displaying the following options shown are Workbook, Dataset, Data Model, Write SQL, and Upload CSV.](https://files.readme.io/012c84e6e4c0d1dc1ea78ae375c0eb9f3019feddc58c57d4e6de7a49dd835548-sql-create-new.png)
3. In the side panel, click **Select a Connection** and select the connection you want to query.
4. In the query editor, enter your SQL query. Sigma provides autocomplete suggestions to guide you.

   ![SQL panel in a workbook with SQL syntax of select * from EXAMPLES., with an autocomplete dropdown suggesting multiple available schemas such as BITCOIN, BIKES, CENSUS, and more.](https://files.readme.io/771da6b1a1c971c1a9a8e7934cdb2943f6ac7965c03df86096a6b03f26da7ece-sql-better-exploration.png)
   > 💡
   >
   > You can reference workbook controls in your SQL by wrapping the control ID in curly brackets. See [Reference workbook controls](/docs/reference-workbook-control-values-in-sql-statements).
5. To run your SQL query, click **Run**, or use the keyboard shortcuts `⌘` + `return` on a Mac or `ctrl` + `enter` on a PC.
6. To save your unpublished workbook (exploration) as a workbook, click **Save As**.

> 💡
>
> To convert your SQL query to a data model, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** to open the element menu, then select **Advanced options** > **Create data model**.

## Create a SQL workbook element

To add a SQL element to an existing workbook and supplement existing analysis, do the following:

1. Open a workbook for editing.
2. In the add element bar, select the type of element you want to add, then choose a specific element type: **Data** > **Table**, **Data** > **Pivot Table** or **Chart** and any supported chart type.
3. In the **Select source** modal, choose the **SQL** option at the bottom.

   ![Select source popover modal showing the Sigma Sample Database selected in the Tables and Datasets tab, with four options at the bottom for CSV, SQL, Join, and Union.](https://files.readme.io/eaa2b6d9b9907a45801a87a2faeece3e576f135fdea3cb9814076115a9eda805-sql-source-pick.png)
4. Select the connection you want to query.

   An element appears in your workbook, prompting you to enter a SELECT statement to query the connection.
5. In the query editor, enter your custom SQL. Sigma provides autocomplete suggestions to guide you.

   ![SQL element in a workbook with SQL syntax of select * from EXAMPLES., with an autocomplete dropdown suggesting multiple available schemas such as BITCOIN, BIKES, CENSUS, and more.](https://files.readme.io/8042db867cdd5489a2b8a5d29ce7cc49a37dc71b82018f4698b3cab45659080a-sql-autocomplete.png)
   > 💡
   >
   > You can reference workbook controls in your SQL by wrapping the control ID in curly brackets. See [Reference workbook controls](/docs/reference-workbook-control-values-in-sql-statements).

## Reference existing Sigma workbook elements

To reference other data elements in your workbook in your SQL query, including other custom SQL elements, use the `sigma_element()` syntax.

For example, to query a data element in your workbook titled *Fiscal Year Forecast* and filter based on the values of the *Revenue* column in the element, write a SQL statement like the following:

SQL

```
SELECT * FROM sigma_element('Fiscal Year Forecast')
   WHERE "Revenue" > 100000
```

### Syntax and usage notes

Use the following syntax to reference a data element in the same workbook:

```
sigma_element('Element title')
```

When using this syntax, consider the following usage notes:

* You must use the exact element title in your SQL statement.
* The element title that you reference must be a string.
* Column names must be identifiers. Identifier syntax depends on your data platform. If your column name contains spaces and you run SQL with Snowflake, double quote the column names when referencing them in your SQL statement. If you run SQL with BigQuery, wrap column names with backticks (`).

### Limitations

* Using this syntax with AzureSQL connections is not yet supported.
* You cannot materialize an element that uses this syntax, including the output of a join with an element that uses this syntax.

## Reference user attributes with system functions

To reference attributes of the current user, use the `{{system::SystemFunction}}` syntax in your SQL statement. For a list of system functions you can use, see [System functions](/docs/system-functions).

For example, to query a data element in your workbook titled *PLUGS\_ELECTRONICS\_HANDS\_ON\_LAB\_DATA* for records where the *Customer Name* column matches the name of the current (signed-in) user, write a SQL statement like the following:

```
SELECT *
FROM sigma_element('PLUGS_ELECTRONICS_HANDS_ON_LAB_DATA')
WHERE "Customer Name" = {{system::CurrentUserFullName}}
```

Or, to query a data element in your workbook titled *PLUGS\_ELECTRONICS\_HANDS\_ON\_LAB\_DATA* for records where the *Store Region* columns matches the *Region* user attribute of the current (signed-in) user, write a SQL statement like the following:

```
SELECT *
FROM sigma_element('PLUGS_ELECTRONICS_HANDS_ON_LAB_DATA')
WHERE "Store Region" = {{system::CurrentUserAttributeText::Region}}
```

### Syntax and usage notes

Use the following syntax to reference data from a system function:

```
{{system::SystemFunction::SystemFunctionArgument}}
```

When using this syntax, consider the following usage notes:

* System functions in custom SQL are equivalent to system functions referenced in the formula bar (ie. `{{system::CurrentUserFullName}}` is equivalent to `CurrentUserFullName()`)
* When using the functions [CurrentUserAttributeText](/docs/currentuserattributetext) and [CurrentUserInTeam](/docs/currentuserinteam), you must use the exact attribute or team name as it appears in the admin panel. For more details, see [Configure user attributes](/docs/user-attributes) and [Configure row-level security by team](/docs/set-up-row-level-security#configure-row-level-security-by-team).

## Shortcuts

Some shortcuts exist to make working with SQL in Sigma easier.

### Toggle SQL editor in the element menu

When a workbook is published, the SQL element displays only the results. When you edit or explore the workbook, you can toggle the SQL editor to show the SQL query that generates the results.

Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/sql-editor.svg) **Toggle SQL Editor** to switch back and forth between the data element and the SQL query editor.

### Maximize the SQL element

To maximize the SQL element in your workbook canvas and make it easier to write a long complex SQL query, press the space bar or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/maximize.svg) **Maximize element** to expand the element to full screen mode.

### Format SQL

To quickly format long blocks of SQL text, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/text-align_left.svg) **Format SQL**.

![](https://files.readme.io/77596fe-formatsql.gif)

### Find and replace

To search within your SQL query, and optionally replace instances of the searched term, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/search.svg) **Search SQL** or use the keyboard shortcut `⌘ + F`.

![SQL editor with find and replace option open, searching for the word Cost in a SQL query and replacing it with the word Price.](https://files.readme.io/020b488-Screenshot_2024-05-15_at_3.35.57_PM.png)

### Access custom SQL from the lineage view

View and edit custom SQL from the lineage view of a workbook or data model. Copy the full query to your clipboard or click **Edit SQL** to go to the inline SQL editor for the element.

![Lineage view for a workbook showing two elements for custom SQL, the SQL query itself and the custom SQL element on the workbook canvas. The SQL query is selected and the details pane shows the SQL query, querying the EXAMPLES.BIKES.STATION table and limiting to 5 results.](https://files.readme.io/c5ab9c054a92da392aaa2554814f02e4b971ea3b16ef77665031ed5f2565c281-sql-lineage.png)

For more details about working with lineage, see [View workbook and data model data lineage](/docs/workbook-data-lineage).

### View the query history

When you use the SQL editor, you can access the history of the queries recently run against the current connection.

![Connection panel open with the History tab selected, showing 2 recent queries, both SELECT from EXAMPLES.SF_RESTAURANTS... queries, with the specific timestamps for each query.](https://files.readme.io/fe62cf3964dcfcaf8dea2f3a7fc27ff8aedb4e553c59df3647a35be57860ebd3-sql-qh.png)

To access this history, click the **DB** tab in the side panel, then select the **History** tab.

To see the query history for all elements in a specific workbook or data model, see [Examine workbook queries](/docs/examine-workbook-queries).

### View table previews

When writing your query, you can use the side panel to explore tables in your data platform. You can navigate to a specific table and select **Preview** to open a preview of the columns and rows in the table, helping you decide whether to add that table to your existing SQL query.

For a given table, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** and choose **Place name in SQL** or **Place select statement in SQL** to easily reference a new table in your SQL query.

## Examples

For more advanced custom SQL cases, refer to these examples.

### Change output based on a user attribute

If you have user attributes defined in your organization, you can reference an attribute to limit the results returned from a SQL query based on the value of the user attribute for the current user.

For example, for the example Plugs Electronics data, return results only with the store region that the current user can access based on the `store_region` user attribute assigned to them:

SQL

```
SELECT
  *
FROM
  EXAMPLES.PLUGS_ELECTRONICS.PLUGS_ELECTRONICS_HANDS_ON_LAB_DATA
WHERE 
  {{system::CurrentUserAttributeText::store_region}} = STORE_REGION
```

As another example, return results filtered by the `customer_name` that the current user has access to view, based on the value of the `organization_name` user attribute assigned to them:

SQL

```
SELECT 
  * 
FROM 
  test.orders 
WHERE 
  customer_name = {{system::CurrentUserAttributeText::organization_name}}
```

For more details about the function syntax, see [CurrentUserAttributeText](/docs/currentuserattributetext). For more details about user attributes and assignment, see [User Attributes](/docs/user-attributes).

### Return output for a specific date range control

For an example returning rows only when a date column matches the value specified in a date range control, refer to the example SQL in [Reference workbook control values in SQL statements](/docs/reference-workbook-control-values-in-sql-statements#return-output-for-a-specific-date-range-control).

### Return rows depending on the value of a multi-select control

For an example returning rows depending on the value of a multi-select list control, refer to the example SQL in [Reference workbook control values in SQL statements](/docs/reference-workbook-control-values-in-sql-statements).

### Return rows based on a schema text selector

If you have a single-select or text control called `schema-param` that has a valid selection (a schema in your connected CDW), and the `STATIONS` table exists in the specified schema, the following example SQL returns all columns from the `STATIONS` column in the specified schema:

SQL

```
SELECT *
FROM {{#raw schema-param}}.STATIONS
```

> 🚩
>
> Sigma does not recommend using the `#raw` configuration value for use cases outside of dynamic schema selection. When used improperly, it can pose security risks, such as allowing users to bypass row-level security.

When using this parameter to swap table, schema, or database names, the column names referenced in the SQL must be identical.

Updated 3 days ago

---

Related resources

* [Keyboard shortcuts: Mac OS](/docs/keyboard-shortcuts-in-sigma-mac-os)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Limitations and considerations](#limitations-and-considerations)
  + - [Query limitations](#query-limitations)
    - [Row and column order limitations](#row-and-column-order-limitations)
    - [Considerations](#considerations)
  + [Create a workbook from SQL](#create-a-workbook-from-sql)
  + [Create a SQL workbook element](#create-a-sql-workbook-element)
  + [Reference existing Sigma workbook elements](#reference-existing-sigma-workbook-elements)
  + - [Syntax and usage notes](#syntax-and-usage-notes)
    - [Limitations](#limitations)
  + [Reference user attributes with system functions](#reference-user-attributes-with-system-functions)
  + - [Syntax and usage notes](#syntax-and-usage-notes-1)
  + [Shortcuts](#shortcuts)
  + - [Toggle SQL editor in the element menu](#toggle-sql-editor-in-the-element-menu)
    - [Maximize the SQL element](#maximize-the-sql-element)
    - [Format SQL](#format-sql)
    - [Find and replace](#find-and-replace)
    - [Access custom SQL from the lineage view](#access-custom-sql-from-the-lineage-view)
    - [View the query history](#view-the-query-history)
    - [View table previews](#view-table-previews)
  + [Examples](#examples)
  + - [Change output based on a user attribute](#change-output-based-on-a-user-attribute)
    - [Return output for a specific date range control](#return-output-for-a-specific-date-range-control)
    - [Return rows depending on the value of a multi-select control](#return-rows-depending-on-the-value-of-a-multi-select-control)
    - [Return rows based on a schema text selector](#return-rows-based-on-a-schema-text-selector)