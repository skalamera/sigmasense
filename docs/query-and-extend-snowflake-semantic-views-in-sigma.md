# Query and extend Snowflake semantic views in Sigma (Beta)

# Query and extend Snowflake semantic views in Sigma (Beta)

> 🚩
>
> This documentation describes one or more public beta features that are in development. Beta features are subject to quick, iterative changes; therefore the current user experience in the Sigma service can differ from the information provided in this page.
>
> This page should not be considered official published documentation until Sigma removes this notice and the beta flag on the corresponding feature(s) in the Sigma service. For the full beta feature disclaimer, see [Beta features](/docs/sigma-product-releases#beta-features).

Snowflake semantic views are a new way to define governed, reusable business logic directly within Snowflake using SQL. Semantic views allow you to model metrics, dimensions, and relationships in a declarative, version-controlled, and queryable format. Rather than living in a third-party tool, this logic can now live directly next to your data in Snowflake. Semantic views are defined using SQL-based metadata definitions, and result in readable views that BI tools and AI agents can query via standard SQL

You can work with the metrics and related columns defined in the semantic view in Snowflake in your Sigma workbooks and data models to do the following:

* Build a table in a data model using the semantic view as a source.
* Add tables, pivot tables, and charts to a workbook that use the semantic view as a source.
* Query the view with custom SQL.
* Browse semantic views in the data catalog.

For more details about Snowflake semantic views, see [Overview of semantic views](https://docs.snowflake.com/en/user-guide/views-semantic/overview) in the Snowflake documentation.

## Limitations

The following is not yet supported:

* Performing a join, union, or transpose with a semantic view.
* When using a list values control or a segmented control, you cannot source the values for the control from a semantic view.
* You cannot target a semantic view data source with a control element.
* Semantic view elements on hidden pages in public embeds (page, element, and workbook) will not work.
* No public APIs are compatible with semantic views.

When working with semantic views in Sigma, the following limitations apply:

* Metrics defined in the semantic view are available only to the element directly sourced from the semantic view. Metrics are not available to child elements.
* Relationships defined in the semantic view are available only to the element directly sourced from the semantic view. Related columns are not available to child elements.

Due to other limitations, the following is also not yet supported:

* If your semantic view defines two dimensions with the same name, but from different tables, the semantic view cannot be queried and attempts to query it fail with an error.

## Requirements

The role used by the Snowflake connection in Sigma must be granted SELECT privileges on the semantic views that you want to work with in Sigma. For more details, see [Granting privileges on semantic views](https://docs.snowflake.com/en/user-guide/views-semantic/sql#label-semantic-views-privileges)

## Browse a Snowflake semantic view in the data catalog

If you have a semantic view defined in the Snowflake account connected to Sigma, you can browse the view, tables, dimensions, metrics, and relationships defined in the view in the [data catalog](/docs/manage-data-catalog).

For example, given a Snowflake semantic view with a definition that matches the example in the Snowflake documentation, [Using SQL commands to create and manage semantic views](https://docs.snowflake.com/en/user-guide/views-semantic/sql#using-the-create-semantic-view-command), with the following characteristics:

* A semantic view called `tpch_rev_analysis`.
* Tables in the view called `orders`, `lineitem`, and `customer`.
* Dimensions, for example, orders.order\_date AS orders.o\_orderdate
* Relationships between tables, for example, the `lineitem` table is related to the `orders` table.
* Metrics on specific tables, for example, the `order_count`, `order_average_value`, and `average_line_item_per_order` metrics on the `orders` table.

You can browse the semantic view in Sigma.

1. From Sigma Home, select **Connections** to open the list of connected data sources.
2. Select the data connection with the data catalog that you want to view.
3. In the left navigation panel, search or browse the data catalog to locate the semantic view that you want to browse.

   Select the semantic view name, for example, `TPCH_REV_ANALYSIS` to view access granted to the object.
4. In the semantic view, select an individual table to view more details. For example, select the `LINEITEM` table:

   * On the **Overview** tab, review the columns and data in the table.
   * On the **Columns** tab, review the column names, data types, formats, and description. You cannot modify the description of a column in a semantic view.
   * On the **Metrics** tab, review the names, formulas, data format, and descriptions of any metrics defined on the table in the semantic view.
   * On the **Relationships** tab, review the target table of the relationship and optionally click the link to open the table in a new tab. The source key and target key for the relationship are also listed.
   * On the **Lineage** tab, review any workbooks or data models that use the table as a source.
5. Click **Explore** to open the table in an exploration.

## Work with a Snowflake semantic view in a data element

You can use a semantic view as a source for a data element:

1. Open a data model or workbook for editing.
2. Add a data element to your document.
3. Browse to and select the semantic view in your Snowflake connection that you want to add.

   The semantic view functions like a folder, allowing you to choose one of the related tables in your workbook to use. The relationships in the semantic view are directional, so only dimensions from tables joined via one-to-one or many-to-one relationships are accessible.

   For example, to view all dimensions from the `LINEITEM`, `ORDERS`, and `CUSTOMERS` tables, choose the `LINEITEM` table as a data source.

   ![Select source open to the Snowflake connection with the TPCH_REV_ANALYSIS semantic view appearing as a folder, with the LINE_ITEMS, CUSTOMERS, and ORDERS tables listed and available to select.](https://files.readme.io/b71cc437b472c896dd3cae40d33f3038a8b3cbb9e743ea17cd90b2e7547c4c8b-sem-view-src-pick.png)
4. After you add the semantic view table as a data source, the relevant dimensions are available on the table. The default name for the element matches the semantic view name. For example, after you choose the `LINEITEM` table, the `ORDERKEY (LINEITEM)` and `PARTKEY (LINEITEM)` columns are available:

   ![Table element added to Sigma titled TPCH_REV_ANALYSIS with the dimensions from the LINE_ITEMS table, listed as columns titled ORDERKEY (LINEITEM) and PARTKEY (LINEITEM)](https://files.readme.io/e3973e2af453282b72af5794f9087fdd1290fb6feedc95e475cff9d6fd16ba66-sem-view-plain.png)
5. If the table is related to other tables in the semantic view, you can view the dimensions from the related tables and add them to your table element in Sigma. To review and add the dimensions from the related tables, open the **Source columns** for the data source.

   For example, the `LINEITEM` table is related to the `CUSTOMERS` and `ORDERS` tables, so you can add the *CUSTOMER\_ NAME* column from the `CUSTOMERS` table, or the *ORDER\_DATE* column.
6. If the table has any metrics defined from the semantic view, those are also accessible. To work with the metrics, click **Metrics** and add one or more metrics to the table.

   ![Table element selected with the metrics panel open and showing ORDER_AVERAGE_VALUE, ORDER_MAX_VALUE, and ORDER_SUM_VALUE metrics. The source columns list is also open and showing the dimensions available from related tables, CUSTOMERS table showing CUSTOMER_NAME and the ORDERS table showing ORDER_DATE, ORDER_DAY, ORDER_MONTH, and ORDER_YEAR dimensions.](https://files.readme.io/f9eef31ea86a2e046477f731142dd01fcf4bd0d59a42d93a4ae06125b7c2e0a7-sem-view-rel-metrics.png)

## Query a semantic view from Sigma

You can query a semantic view directly using a SQL query with the custom SQL functionality in Sigma. See [Write custom SQL](/docs/write-custom-sql).

Updated 3 days ago

---

[Ask natural language queries with Ask Sigma](/docs/ask-natural-language-queries-with-ask-sigma)[Manage a workbook](/docs/workbook-management)

* [Table of Contents](#)
* + [Limitations](#limitations)
  + [Requirements](#requirements)
  + [Browse a Snowflake semantic view in the data catalog](#browse-a-snowflake-semantic-view-in-the-data-catalog)
  + [Work with a Snowflake semantic view in a data element](#work-with-a-snowflake-semantic-view-in-a-data-element)
  + [Query a semantic view from Sigma](#query-a-semantic-view-from-sigma)