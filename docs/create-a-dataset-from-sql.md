# Create a dataset from SQL

# Create a dataset from SQL

One way that you can create datasets is by writing SQL against the data in your warehouse. SQL-based datasets take SQL queries and turn them into reusable data sources that people can use as the basis for additional analysis. [Datasets can also be materialized](/docs/schedule-materialization-for-a-dataset) to your database, helping speed up queries. Any changes made to a dataset propagate to downstream dependencies.

For details about creating datasets, see [Create and manage datasets](/docs/create-and-manage-datasets).

## Requirements

* To use this feature, you must be assigned an [account type](/docs/license-and-account-type-overview) with the **Write SQL** and **Create, edit, and publish datasets** permissions enabled.
* To run custom SQL, you must have **Can use** access to the entire connection. See [Data permissions](/docs/manage-data-permissions). The SQL editor only appears if you have connection-level access to at least one connection in your organization.
* To reference existing Sigma datasets and workbook elements in your SQL, you must have [write access](/docs/set-up-write-access) configured on your connection.

## Create a dataset by writing custom SQL

To create a dataset by writing your own SQL query against your data:

1. Open **Sigma Home**.
2. In the navigation panel, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Create New**, then select **Dataset**.
3. On the Select a Data Source page, select the **SQL** option.
4. In the side panel, click **Select a Connection** and choose the connection that you want to query.
5. In the query editor, enter your custom SQL. Sigma provides autocomplete suggestions to guide you.
6. Select **Run** to run your SQL query. You can also use keyboard shortcuts: CTRL-Enter on Windows or CMD-Return on a Mac.
7. After confirming that the results look as desired, select **Get Started** to create a dataset.

For more details about writing custom SQL, see [Write custom SQL](/docs/write-custom-sql).

### Modify a dataset created from SQL

To edit the SQL used to create your dataset, do the following:

1. Open the dataset that you want to modify.
2. Click **Edit**, then select the **Worksheet** tab.
3. In the side panel, open the data sources panel.
4. For **Custom SQL**, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Edit Source**.
   ![](https://files.readme.io/c7f2e313d5fa0904b4898e4eef2e9b9896bb168a71b8074b3a1b1cc504b8fa8a-dataset-sql-edit.png)
5. In the query editor that opens, modify the custom SQL. Click **Run** to validate that your query returns the desired results.
6. Click **Done** to save the query.
7. Click **Publish** to update the dataset.

## Reference existing Sigma datasets

You can reference your existing Sigma dataset in your SQL by using the fully qualified name of the [warehouse view](/docs/dataset-warehouse-views) created in your data platform. If your dataset does not have a location or dataset warehouse view available, create one.

The fully qualified name is a combination of the dataset location in your data platform and the name of the warehouse view:

`SELECT * FROM <location>.<dataset_warehouse_view_name>`

To determine the fully qualified name of the dataset, select **More info** ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/info-circle-filled.svg) when viewing a dataset:

![Dataset information panel, showing the Location and Dataset fields in the Warehouse Views section.](https://files.readme.io/52cf6e5-Screenshot_2024-05-20_at_11.58.22_AM.png)

The **Location** field provides the database or catalog and schema in your data platform that contains the dataset, and the **Dataset** field provides the view name that you can reference.

> 💡
>
> To copy the fully qualified name to your clipboard, click **More** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg)), then select **Copy path**.

To reference individual columns from your Sigma dataset in your SQL statement, wrap the column name in double quotes. For example:

SQL

```
SELECT "Customer Id" FROM DATABASE.SCHEMA.DATASET_WAREHOUSE_VIEW_NAME
```

For more details about writing custom SQL, see [Write custom SQL](/docs/write-custom-sql).

## Reference dataset parameters

You can reference dataset parameters in your SQL by wrapping the name of the parameter in curly brackets:
`{{my_parameter_name}}`

For more details, see [Reference control values in SQL statements](/docs/reference-workbook-control-values-in-sql-statements).

Updated 3 days ago

---

[Dataset Links](/docs/dataset-links)[Create and manage dataset warehouse views](/docs/dataset-warehouse-views)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Create a dataset by writing custom SQL](#create-a-dataset-by-writing-custom-sql)
  + - [Modify a dataset created from SQL](#modify-a-dataset-created-from-sql)
  + [Reference existing Sigma datasets](#reference-existing-sigma-datasets)
  + [Reference dataset parameters](#reference-dataset-parameters)