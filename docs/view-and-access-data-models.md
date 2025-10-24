# Navigate data models

# Navigate data models

A data model consists of two pages: a [workbook page](#data-model-workbook-page) and an [overview page](#data-model-overview-page). The workbook page allows you to create and transform reusable elements to build your data model, while the overview page provides context about the data model and general usage across your organization. Within the overview page, you can also access metadata to gain key insights into your data structure, quality, and lineage.

This document explains the structure and content of the workbook page and overview page to help you navigate data models.

## Data model workbook page

The workbook page enables you to create and manage various tables and input tables as reusable elements within a single data model. This format brings the ease and flexibility of Sigma's workbook structure to data model development. Consolidate and transform your data as you would in a workbook analysis, and control which elements can be reused as data sources across your organization.

![](https://files.readme.io/69f0d6c4cf15664222a65d94c437198d2d8bece72a5a43430ab6c1e22b851de4-image.png)

|  |  |  |
| --- | --- | --- |
| **a** | **Publish button** | Saves edits applied to the data model.  *Documents that reference the data model reflect the published state of its reusable elements. Drafted edits don't apply.* |
| **b** | **Control element** | Filters the data in one or more elements.  *When a reusable element is filtered, documents that reference it can only access data included in the published filtered state. For more information about using controls, see[Intro to control elements](/docs/intro-to-control-elements).* |
| **c** | **Reusable element** | Available as a data source (indicated by the  icon). |
| **d** | **Disabled element** | Not available as a data source (indicated by the  icon). |
| **e** | **Add element bar** | Allows you to add a new table, input table, control, or UI element. |

## Data model overview page

The overview page provides details about each reusable element in the data model for improved data visibility and management.

![Annotated screenshot pointing out key UI components in the data model overview page.](https://files.readme.io/f15860e040b41573d7192986baa5f0d45d687e963097e956f5e010ea7c00ba09-image.png)

|  |  |  |
| --- | --- | --- |
| **a** | **Edit button** | Opens the [data model workbook page](#data-model-workbook-page). |
| **b** | **Data model details** | Displays the data model description and identifies the model owner, location, relative time stamp of the last update, and number of reusable elements the model contains. |
| **c** | **Expanded element overview** | Displays the reusable element’s connection, relative time stamp of the last materialization, top three documents referencing it as a data source, top three organization members utilizing it, and the published state of the element’s data table. |
| **d** | **Collapsed element overviews** | Displays the reusable element’s title, number of documents referencing it as a data source, and number of rows and columns in its data table. |
| **e** | **View details button** | Opens a modal containing system-generated insights about the data structure, quality, distribution, and lineage for the reusable element. For more information, see the **[Data details](#details-view)** section in this document. |
| **f** | **Explore button** | Opens the reusable element in a new exploration. |

## Data details

The details view on the overview page provides access to metadata for individual reusable elements in the data model, revealing important insights for data profiling and lineage tracking.

### Columns

The **Columns** tab includes structural metadata (column name, data type, format, and description) and system-generated statistics that can help you assess data quality, distribution, and variability. With this information, you can better understand your data, identify potential issues, and improve data usability.

![Columns tab showing details described in surrounding text. The Sales Quantity column is highlighted for this table, and it has a description of Quantity of products ordered, information showing that it's a numeric column, the formula for the column, top values are 1, 2, 3, and 5, and a total number of values and nulls, as well as various statistics like sum and percentile values for the column.](https://files.readme.io/d7c97865495a162831dd2aa0ffec573980cc72264cce66ffb83e6afc9687d0e9-image.png)

Example insights from system-generated statistics:

* A high percentage of nulls suggests there are missing values and incomplete data.
* A low percentage of distinct values can indicate duplicate records causing unexpected data redundancy.
* Minimum and maximum values represent the data range, which can reveal outliers from possible data entry errors.
* A high standard deviation can be evidence of anomalies contributing to data inconsistency.

### Controls

The **Controls** tab lists information about the controls applied to the reusable element. This data transparency can help users understand how the data is filtered and transformed within the data model.

![Controls tab, showing the IDs of various controls that target the data model element, as well as the type and default value for the control, if one exists. ](https://files.readme.io/7cb0a7e33ddc784c55d8490c419084bdc57f005861b11d9643ed61e1e990f9c1-image.png)

### Lineage

The **Lineage** tab provides details about the reusable element's data sources and references (downstream dependencies), allowing users to identify where the data originates from and where it's used across your organization.

![Lineage tab showing 2 warehouse tables as sources, including the location and table descriptions for the warehouse tables. A separate section shows downstream dependencies. Document names, descriptions, last updated date, badges, and locations for each downstream workbook or data model is shown. ](https://files.readme.io/f50e3f3bf4fa8aea28dd5e0d87884d13295eafd92b1e0149e49a9ce7e011efb4-image.png)

## Explore highlighted metrics

If your data model contains metrics, up to 6 metrics display on the [data model overview](#data-model-overview-page) page. Users with edit access to the data model can [choose which metrics to highlight](/docs/create-and-manage-metrics#highlight-a-metric-in-the-data-model-overview), but anyone with access to the data model can explore the highlighted metrics.

To review details about a highlighted metric, open the data model and select a highlighted metric. A detailed profile page for the metric opens:

![Metrics explorer view for the data model, with a list of metrics in the left navigation panel and the metric title, formula, and details like data model name, description, documents using the metric, and a timeline view of the metric if one exists.](https://files.readme.io/b6c739630a20d27a194a428763b305d5aecf09f72010379abe2442240a6c09a6-dm-metric-profile.png)

For each metric defined in the data model, you can review the following:

* The metric name and formula.
* The name of the data model element that contains the metric.
* The description of the metric.
* Top documents using the metric. Click the document name to open the document in the same browser tab.
* If the metric has a timeline enabled, explore the timeline and KPI chart for the metric.

Select **Explore in workbook** to open a new workbook with the metric as a KPI chart.

Updated 3 days ago

---

[Create and manage data models](/docs/create-and-manage-data-models)[Define relationships in data models](/docs/define-relationships-in-data-models)

* [Table of Contents](#)
* + [Data model workbook page](#data-model-workbook-page)
  + [Data model overview page](#data-model-overview-page)
  + [Data details](#data-details)
  + - [Columns](#columns)
    - [Controls](#controls)
    - [Lineage](#lineage)
  + [Explore highlighted metrics](#explore-highlighted-metrics)