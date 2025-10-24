# Create and manage datasets

# Create and manage datasets

If you want to model your data in Sigma, you can create a dataset. Creating a dataset allows you to bundle formulas, data transformations, filters, groupings, and parameters into a rich data source that others can build on. You can also [materialize datasets](/docs/schedule-materialization-for-a-dataset), helping accelerate data analysis.

> 💡
>
> Consider creating a data model instead of a dataset. Data models improves key dataset features like relationships (links), metrics, and column-level security (CLS) and adds new features like live editing with other modelers, an entity relationship diagram (ERD), and more. See [Get started with data modeling](/docs/get-started-with-data-modeling).

You can create a dataset from a table in your data platform, from a CSV file, or from a custom SQL statement:

* [Create a dataset from a table](#create-a-dataset-from-a-table)
* [Create a dataset from a CSV file](/docs/using-csvs-in-datasets)
* [Create a dataset from SQL](/docs/create-a-dataset-from-sql)

## User requirements

To create and manage datasets, you must be assigned an [account type](/docs/license-and-account-type-overview) with the **Create, edit, and publish datasets** permission enabled.

## Create a dataset from a table

To create a dataset from a table in a connected data source:

1. From **Sigma Home**, select **Connections** to open the list of connected data sources.
2. Select the data connection with the data catalog that you want to view.
3. In the left navigation panel, search or browse the data catalog to locate the table.
4. Select the table name to open the table.

   ![Data catalog for the connected data source, with an EVENTS table selected.](https://files.readme.io/563a7477ed80e266ea5e279dd44c75a7901a1106c90c80eb74734bdeb270f6bf-view-data-catalog.png)
5. Next to **Explore**, select the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to **Use this table**, then choose **Create Dataset**.
6. Name the dataset and choose a location in which to save it, then click **Create**.

## Modify dataset metadata

You can modify the metadata of the dataset, adding a description with usage guidance, provide documentation for specific columns, or apply a badge, for example, to label the dataset contents as high quality, deprecated, or irrelevant.

### Add a dataset description

To add a description to the dataset:

1. Open the dataset, then select **Edit**.
2. Next to the dataset name, select **More info** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/info-circle-filled.svg)).
3. In the **Description** field, enter a description for the dataset.
4. To save the description, publish the dataset.

### Add or update a dataset badge

Add or update a certification badge to indicate the status, quality, and reliability of the data.

1. Open the dataset.
2. In the header, select **More info** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/info-circle-filled.svg)).
3. In the popover, select an option from the **Badge** dropdown.

   ![More info for a sales targets dataset, with badge drop down open showing available badges of endorsed, deprecated, and warning.](https://files.readme.io/cd187ccbc76e4fecde9d0f17612432daf3ba0914f9c0f0e934d2dc34511a83b8-2025-02-13_23-25-54.png)
4. (Optional) When you select a badge, the popover displays the **Badge note** field. Add a note to provide context about the badge.

   ![More info for the sales targets dataset, with a badge note providing context that the data is verified and authorized for use, accompanying the endorsed badge.](https://files.readme.io/5aac68f70f462ac91619f31e45d2721631771954fddde7e459a7261799826075-2025-02-13_23-33-20.png)

   The badge is automatically saved and immediately reflected in the dataset header.

![Dataset header displaying the endorsed badge next to the dataset name.](https://files.readme.io/f58ae3ac97e5a41634693591d4c86aee2f3ff6f2c16ffe8707a15accda535b95-2025-02-13_23-28-42.png)

## Delete a dataset

To delete a dataset you must be the owner of the dataset, have **Can edit** access to the dataset, or be assigned the **Admin** account type.

1. Next to the dataset name, click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)), then click **Delete...**.
2. On the **Confirm Deletion** modal, click **Delete**.

### Recover a deleted dataset

To recover a dataset that has been deleted, you must be the owner of the dataset or have the **Admin** account type.

1. Go to your ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/home.svg) **Home** page.
2. In the navigation menu, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/trash-fill.svg) **Trash**.
3. In the **Trash** page, search the list of deleted documents and click the one you want to recover. You can sort the **Name**, **Deleted on**, or **Deleted by** columns to help identify the applicable document.
4. In the **Document has been deleted** modal, click **Recover**. Sigma immediately opens the recovered document.

Updated 3 days ago

---

[Datasets](/docs/datasets)[Dataset best practices](/docs/dataset-best-practices)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Create a dataset from a table](#create-a-dataset-from-a-table)
  + [Modify dataset metadata](#modify-dataset-metadata)
  + - [Add a dataset description](#add-a-dataset-description)
    - [Add or update a dataset badge](#add-or-update-a-dataset-badge)
  + [Delete a dataset](#delete-a-dataset)
  + - [Recover a deleted dataset](#recover-a-deleted-dataset)