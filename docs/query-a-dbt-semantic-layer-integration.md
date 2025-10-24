# Query a dbt Semantic Layer integration

# Query a dbt Semantic Layer integration

Sigma supports [dbt Semantic Layer](https://www.getdbt.com/product/semantic-layer) integrations, allowing you to leverage your predefined dbt metrics in Sigma workbooks for ad-hoc analysis, recurring reports, and organizational dashboards. This document explains how to query a dbt Semantic Layer in Sigma and how the query flow progresses.

## System and user requirements

In Sigma:

* To use this feature, you must be assigned an account type with the [permission to write custom SQL](/docs/license-and-account-type-overview).
* You must have the **Can use** data permission for your entire connection. See [Manage data permissions](/docs/manage-data-permissions).
* You must have write access configured on your connection. See [Set up write access](/docs/set-up-write-access).
* You must have a dbt Semantic Layer integration configured. See [Configure a dbt Semantic Layer integration](/docs/configure-a-dbt-semantic-layer-integration).

In dbt:

* You must have a semantic model and metrics created in dbt. See the dbt documentation on [dbt Semantic Layer](https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl).

## Query flow between Sigma and dbt Semantic Layer

When you enter a Semantic Layer query in Sigma, Sigma compiles your query into an intermediate representation and sends the query parameters to the dbt Semantic Layer [JDBC API](https://docs.getdbt.com/docs/dbt-cloud-apis/sl-jdbc) (step 1 in the following diagram):

![Query parameters are sent from Sigma to dbt Semantic Layer. dbt returns the SQL statement in the appropriate dialect to Sigma, which then executes the SQL against your connected data platform and returns query results, which Sigma displays as a table of results.](https://files.readme.io/a27389833b9750670592f46eac51e63765d927b79320c47a63199a2ce52d61c2-dbt_query_flow_diagram.png)

dbt then returns the SQL statement in the appropriate dialect to Sigma (step 2). Sigma executes the SQL against your connected data platform, and outputs a table similar to those from your other data platforms (steps 3, 4, and 5. These tables can be used like any other data table in Sigma. If the table is created in a data model, you can reuse the table across workbooks and data models, create and join the tables, build charts, and more.

## Query the dbt Semantic Layer Integration

To query the Semantic Layer, do the following:

1. Open a workbook for editing or customizing.
2. In the add element bar, select **Data** > **Table** to add a table element. When choosing the source, select **SQL** to use SQL as the source for your data element.
3. Enter your query. See the dbt documentation on [Querying the API for metric metadata](https://docs.getdbt.com/docs/dbt-cloud-apis/sl-jdbc#querying-the-api-for-metric-metadata) for query syntax.
4. Select **Run**.

Every time a Semantic Layer query is run, Sigma requests the latest definitions, so changes made to the Semantic Layer are reflected in Sigma. Changes made to the Semantic Layer are not reflected unless a new query is run.

## Reference Semantic Layer metrics

You can reference your semantic layer metrics using the template syntax of `{semantic_layer.metrics()}`, with the name of your metric in dbt within the parentheses. See the dbt documentation on [Querying the API for metric metadata](https://docs.getdbt.com/docs/dbt-cloud-apis/sl-jdbc#querying-the-api-for-metric-metadata) for more syntax guidance.

### Example 1: Surface and group dbt metrics in a Sigma workbook

You can surface your existing dbt metrics in a Sigma workbook, and group them by multiple dimensions. An example query might look like:

SQL

```
SELECT * 
FROM
{{ semantic_layer.query( metrics = ['new_customers', 'transactions', 'revenue_usd'],
group_by = [Dimension('metric_time').grain('month'), 'customer__customer_country'])
}}
```

The query surfaces three existing metrics (`'new_customers'`, `'transactions'`, `'revenue_usd'`) in the example dbt data, and groups them by both country and time (split by month intervals). This query generates the following result in Sigma:

![A table with 5 columns, METRIC_TIME_MONTH, CUSTOMER__CUSTOMER_COUNTRY, NEW_CUSTOMERS, REVENUE_USD, and TRANSACTIONS. There are 7 rows of data.](https://files.readme.io/a8345e9fb7b7134ee95f66525a54da606d1707b1c9e7d061700e82d32de380b8-surface_dbt_metrics.png)

### Example 2: Browse Semantic Layer metrics

You can obtain a list of all metrics available in the Semantic Layer in Sigma by running the following custom SQL:

SQL

```
select * from {{semantic_layer.metrics()}}
```

This produces a table of metric names and additional details, for example:

![A table of 10 columns and 12 rows of data, with column names Name, Description, Dimensions, Measures, Type, Type Params, Metadata, Queryable Granularities, Label, and Meta. The Type Params data is in JSON.](https://files.readme.io/320cc755f31e9a207047214bdcfe9ebcf26819ccb5ef45792cf9c13201a808b3-browse_metrics.png)

### Example 3: List all dimensions and time grains for a metric

You may want to obtain a list of all dimensions and time grains available for an existing dbt metric. For example, if you had an existing dbt metric named `'transactions'`, your query might look like:

SQL

```
select *  from {{semantic_layer.dimensions(metrics=['transactions'])}}
```

Running this SQL in Sigma produces the following result:

![Custom SQL output with 7 rows and 6 columns, with column names NAME, DESCRIPTION, TYPE, TYPE_PARAMS, QUERYABLE_GRANULARITIES, and LABEL.](https://files.readme.io/feb028759048b649aa18d4ec990c4560057eba158b90cb02f19d9c418872a476-list_dimensions.png)

## Reference control values when querying your dbt Semantic Layer

You can reference control values when querying your dbt Semantic Layer in Sigma, allowing you to take advantage of pre-aggregated data.

Use the following syntax:

```
{{#formula [control-ID]}}
```

### Example 1: Pass user input to a query

For example, you can allow a user to type the name of a dbt metric to query:

1. Set up a text input control element. Set the control ID to `metric-input-control`.
2. Add a data element sourced by a SQL query, and type the following query:

   SQL

   ```
   select * from {{semantic_layer.metrics( {{#formula [metric-input-control]}})}}
   ```

### Example 2: Reference different time grains with a segmented control

For example, you can reference different time grains:

1. Set up a segmented control for different time grains: day, month, quarter, and year. Set the control ID to `c-time-grain`.
2. Add a data element sourced by a SQL query and type the following query:

   SQL

   ```
   select * from {{semantic_layer.query(
     metrics = ['revenue'],
     group_by = ['pos_order_number__product_type', Dimension('metric_time').grain({{#formula [c-time-grain]}})])
   }}
   ```
3. Test the segmented control and query.

Updated 3 days ago

---

[Reference workbook control values in SQL statements](/docs/reference-workbook-control-values-in-sql-statements)[Ask natural language queries with Ask Sigma](/docs/ask-natural-language-queries-with-ask-sigma)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Query flow between Sigma and dbt Semantic Layer](#query-flow-between-sigma-and-dbt-semantic-layer)
  + [Query the dbt Semantic Layer Integration](#query-the-dbt-semantic-layer-integration)
  + [Reference Semantic Layer metrics](#reference-semantic-layer-metrics)
  + - [Example 1: Surface and group dbt metrics in a Sigma workbook](#example-1-surface-and-group-dbt-metrics-in-a-sigma-workbook)
    - [Example 2: Browse Semantic Layer metrics](#example-2-browse-semantic-layer-metrics)
    - [Example 3: List all dimensions and time grains for a metric](#example-3-list-all-dimensions-and-time-grains-for-a-metric)
  + [Reference control values when querying your dbt Semantic Layer](#reference-control-values-when-querying-your-dbt-semantic-layer)
  + - [Example 1: Pass user input to a query](#example-1-pass-user-input-to-a-query)
    - [Example 2: Reference different time grains with a segmented control](#example-2-reference-different-time-grains-with-a-segmented-control)