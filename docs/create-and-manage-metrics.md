# Create and manage metrics

# Create and manage metrics

A metric is a custom aggregate calculation that can be reused across data elements that share a data source. If you define metrics in data models, datasets, or tables from a connected database or catalog, you can help users perform calculations in a consistent way both easily and efficiently.

This document explains how to create and manage metrics for improved metrics governance. For information about using metrics in workbook data elements, see [Use metrics in a workbook](/docs/use-metrics-in-a-workbook).

For more details about metrics, including limitations and best practices, see [About metrics](/docs/about-metrics).

## User requirements

The ability to create and manage metrics in *data models* requires the following:

* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Create, edit, and publish datasets** permission enabled.
* You must be the dataset owner or be granted **Can edit** [access](/docs/folder-and-document-permissions) to the data model.

The ability to create and manage metrics in *datasets* requires the following:

* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Create, edit, and publish datasets** permission enabled.
* You must be the dataset owner or be granted **Can edit** [access](/docs/folder-and-document-permissions) to the dataset.

The ability to create and manage metrics in *database or catalog tables* requires the following:

* You must be be granted **Can use & annotate** [data access](/docs/data-permissions-overview) for the specific table, or you must inherit the permission granted at the applicable connection, database or catalog, or schema level.

## Work with metrics in data models

Add, highlight, and update metrics in data models.

### Create a metric in a data model

1. Open the data model for editing.
2. Select the data model element that you want to add a metric to.
3. In the editor panel, select the **Modeling** tab.

   > 💡
   >
   > ### If you don't see a **Modeling** tab, you can also add a metric in the **Metrics** tab of the **Element Properties**.
4. In the **Metrics** section, select **+** (**Add metric**).

   The **Add a metric** modal appears.
5. In the **Name** field, enter a name to use for the metric.
6. In the **Description** field, enter a description about what the metric does. The description appears when a user hovers over the metric.
7. In the **Formula** field, define the metric logic. You can use Sigma functions, reference any column in the data model table, or reference another metric.

   ![Add a metric modal described in surrounding text, showing a Total revenue metric with sum of revenue as the formula.](https://files.readme.io/4c93e56a2b6bb36f40629cceef2f4a5ffefdaa0c5b9c19cc1358f7b8d5905e2c-dm-add-metric.png)
8. [optional] Turn on the **Timeline** switch to display a timeline for the metric on the [data model overview](/docs/navigate-data-models#data-model-overview-page) page.

   1. For **Date**, choose a date column in your data to use for the timeline.
   2. For **Truncation**, choose a how to truncate the date, or choose to remove the date truncation and use the existing granularity of the date column.
   3. [optional] For **Compare period**, choose the comparison period for the metric, or choose **None**.
   4. [optional] For **Direction**, choose the direction for the comparison trend, or choose **None**.
9. Review the **Preview** for your metric and optionally define a format for the output of the metric.

   For example, you can specify the formula result as a currency or a percentage, set the number of decimal places, or select options from the full format menu by clicking the number format menu (![](https://files.readme.io/3d073dd-icon-number-format-menu.svg)).

   > 📘
   >
   > ### Metrics define aggregate calculations. If the preview displays a null value, your formula might be missing an aggregate function, such as `Sum()`, `Avg()`, or `Count()`.
10. Publish the data model to make the changes available downstream.

### Highlight a metric in the data model overview

By default, up to six metrics that you create in a data model appear on the [data model overview](/docs/navigate-data-models#data-model-overview-page) page. To change which metrics appear, you can choose to highlight specific metrics on the overview page and display only those.

1. Open the data model for editing.
2. Select the data model element that you want to add a metric to.
3. In the editor panel, select the **Modeling** tab.
4. In the **Modeling** tab of the editor panel, in the **Metrics** section, locate the metric.
5. For the metric, click **More** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg)), then select **Highlight in overview**.
6. Publish the data model to make the changes available.

   ![Data model overview showing a revenue forecast model with KPIs for two highlighted metrics, Total Revenue, featuring a timeline, and Total Products, which is shown over all time.](https://files.readme.io/f529d9f2d1ea4e921516e8c5a2cfc2356960b8b79ec51f34a6c47e9d16a6ef97-highlighted-metrics.png)

Highlighted metrics can be explored by anyone with access to the data model. For more details, see [Navigate data models](/docs/navigate-data-models).

### Edit a metric in a data model

To modify a metric, do the following:

1. Open the data model for editing.
2. Select the table on which the metric is defined.
3. In the **Modeling** tab of the editor panel, in the **Metrics** section, locate the metric.
4. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/edit.svg) (**Edit metric...**).
5. Make any desired changes, then click **Save**.
6. Publish the data model to make the changes available downstream.

   Columns and metrics that use the metric update to use the revised metric.

### Delete a metric in a data model

To delete a metric, do the following:

1. Open the data model for editing.
2. Select the table on which the metric is defined.
3. In the **Modeling** tab of the editor panel, in the **Metrics** section, locate the metric.
4. For the metric, click **More** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg)), then select **Delete**.
5. Publish the data model to make the changes available downstream.

   Any columns or metrics that rely on the deleted metric display an error.

## Work with metrics in datasets

Datasets and metrics in datasets are generally available.

### Create a metric in a dataset

Follow these steps to create a metric:

1. Open a dataset or database table.
2. In the header, click **Edit**.
3. Select the **Metrics** tab, then click **Create Metric** to open the metric builder.
4. In the **Name** field, enter the name of the metric.
5. In the **Description** field, enter details about the metric.

   This information displays when users apply metrics to a workbook element.
6. In the **Formula** field, define the metric logic.

   You can use Sigma functions, and reference any column in the open dataset or database table.

   You can also use an existing metric of the dataset; this is a very powerful practice to build reusable calculation components in your dataset.
7. Use the quick formatting tools and preview to customize the metric output.

   For example, you can specify the formula result as a currency or a percentage, set the number of decimal places, or select options from the full format menu by clicking the number format menu (![](https://files.readme.io/3d073dd-icon-number-format-menu.svg)).

   Metrics define aggregate calculations. If the metric builder preview returns a `null` value, your formula might be missing an aggregate function, such as `Sum()`, `Avg()`, `Count()`, and so on.
8. In the header, click **Publish** to save the metric.

   ![Annotated view of the datasets metric builder, with the Publish button highlighted.](https://files.readme.io/a400f0d-3.png)

### Edit a metric in a dataset

When you edit a metric, Sigma reflects your changes in workbook elements that link to the specific dataset or database table. All workbook references to the metric include name and description changes, and Sigma recalculates metric results based on formula updates.

To edit a metric, follow these steps:

1. Open the dataset or database table that contains the metric that you plan to edit.
2. Click **Edit**.
3. Select the **Metrics** tab.
4. Locate the metric in the list, and click its name to open the metric in the metric builder.
5. Edit the metric name, description, formula, and formatting as needed, then click **Publish** to update the metric.

### Delete a metric in a dataset

When you delete a metric, its calculation becomes invalid in workbook elements. Tables display error messages in columns that previously included metric output. Visualizations and pivot tables display an error message instead of the element.

1. Open the dataset or database table that contains the metric you plan to delete.
2. Click **Edit**.
3. Select the **Metrics** tab.
4. In the list of metrics, find the metric that you plan to delete.
5. For the metric, click **More** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg)), then select **Delete**.

   ![Metric list view on the Metrics tab, showing the more menu open with the Delete option hovered over.](https://files.readme.io/cb0d1c0-8.png)

   Alternatively, select the metric to open the metrics builder and locate the metric in the side panel. Next to the name of the metric, click **Delete metric** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/square_close.svg)).
6. ![Metric view for the selected metric, with the delete metric option highlighted next to the metric name.](https://files.readme.io/13798f1-9.png)

Updated 3 days ago

---

Related resources

* [Use metrics in a workbook](/docs/use-metrics-in-a-workbook)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Work with metrics in data models](#work-with-metrics-in-data-models)
  + - [Create a metric in a data model](#create-a-metric-in-a-data-model)
    - [Highlight a metric in the data model overview](#highlight-a-metric-in-the-data-model-overview)
    - [Edit a metric in a data model](#edit-a-metric-in-a-data-model)
    - [Delete a metric in a data model](#delete-a-metric-in-a-data-model)
  + [Work with metrics in datasets](#work-with-metrics-in-datasets)
  + - [Create a metric in a dataset](#create-a-metric-in-a-dataset)
    - [Edit a metric in a dataset](#edit-a-metric-in-a-dataset)
    - [Delete a metric in a dataset](#delete-a-metric-in-a-dataset)