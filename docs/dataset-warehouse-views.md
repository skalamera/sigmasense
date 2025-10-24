# Create and manage dataset warehouse views

# Create and manage dataset warehouse views

Warehouse views are virtual tables in your data platform that you can query using Sigma or any other application in your data ecosystem. Create warehouse views based on the data you model in Sigma to simplify queries and retrieve relevant and up-to-date datasets directly from your database.

This document describes dataset warehouse views and how to utilize them. For details on creating warehouse views for workbooks or data models, see [Create and manage warehouse views](/docs/create-and-manage-workbook-warehouse-views).

## System requirements

To utilize dataset warehouse views, your organization must have [write access](/docs/set-up-write-access) enabled for the connection.

> 📘
>
> This feature isn't supported by all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## About dataset warehouse views

When write access is enabled for your supported connection, Sigma automatically creates a warehouse view for any dataset using the connection's data. Instead of storing the dataset as a database table, a warehouse view saves a SQL statement that expresses specific query logic defined by the dataset.

When Sigma creates a warehouse view, it establishes a live link between the data platform and Sigma. The view references the dataset as the source of truth and automatically updates to reflect the most recent version of the data.

## Dataset warehouse views vs. materializations

For any dataset, Sigma can create up to two views:

* A warehouse view that allows you to access the dataset's generated SQL.
* A materialized view that allows you to access the Sigma-generated [materialization](/docs/materialization) (if materializations are configured and scheduled for the dataset).

Sigma saves warehouse views every time dataset changes are published. Therefore, when you query a warehouse view, you retrieve live data from the data sources. When you query a materialized view, however, you retrieve data from the last scheduled materialized table, which means the retrieved data may differ from the live data.

## Query a dataset warehouse view

To reference a dataset warehouse view in a SQL query, use the view path.

1. Open the dataset in Sigma.
2. Click the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/info.svg) info icon to view the dataset details.
3. In the **Warehouse views** section, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** in the **Dataset** field and select **Copy path**. Use this path to access the dataset's modeled data from Sigma or any application in your data ecosystem that supports SQL.

## Limitations

* If a parameter is used in your dataset, the warehouse view will only reflect the parameter’s default value.
* If a SQL dataset uses non-qualified SQL (where the SQL paths are not explicitly defined), the view will show an error for that dataset and any dataset that references it.

## Insufficient database grants

If write access is enabled for the connection but you see an **Insufficient permissions** warning in the warehouse views details, you might have insufficient permissions in your data platform. To ensure all relevant access has been granted, see the instructions and commands outlined in [Set up write access](/docs/set-up-write-access) .

For example, in Snowflake you need `USAGE` privileges granted on the destination database, but also the following privileges granted on the write-back schema used by Sigma: `USAGE`, `CREATE TABLE`, `CREATE VIEW`, and `CREATE STAGE`.

Updated 3 days ago

---

Related resources

* [Materialization](/docs/materialization)
* [Create and manage workbook warehouse views](/docs/create-and-manage-workbook-warehouse-views)

* [Table of Contents](#)
* + [System requirements](#system-requirements)
  + [About dataset warehouse views](#about-dataset-warehouse-views)
  + [Dataset warehouse views vs. materializations](#dataset-warehouse-views-vs-materializations)
  + [Query a dataset warehouse view](#query-a-dataset-warehouse-view)
  + [Limitations](#limitations)
  + [Insufficient database grants](#insufficient-database-grants)