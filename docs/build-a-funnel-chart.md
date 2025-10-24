# Build a funnel chart

# Build a funnel chart

Funnel charts are typically used to measure values across sequential stages in a linear process. Create funnel charts to evaluate inputs across each stage and discover potential issues and bottlenecks in a workflow.

This document details basic funnel chart requirements and introduces key properties and format options to help you enhance your workbook visualizations.

![](https://files.readme.io/2c15a8a-1.png)

> 📘
>
> ### Example use cases:
>
> * **Product marketing analytics**: Monitor an email campaign pipeline to understand where most prospects are being lost, then assess opportunities for greater conversion.
> * **Sales analytics**: Track the number of prospects in each stage of the sales cycle to identify where most prospects are currently held, then assess investments in specific sales motions.
> * **HR analytics**: Analyze recruiting process stages by demographics (like age, gender, and application submitted) to measure pipeline dropoff rate for specific candidate groups, then determine if dropoff exceeds expectations and indicates a need for process refinement.

## User requirements

The ability to create funnel charts and other charts requires the following:

* You must be assigned an [account type](/docs/user-account-types) with the **Edit Workbook** and/or **Explore Workbook** permission enabled.
* You must be the workbook owner or be granted **Can explore** or **Can edit** [workbook permission](/docs/folder-and-document-permissions).

> 🚧
>
> ### If you're granted **Can explore** access to the workbook, you can create and modify chart properties and formatting in **Explore** mode, but you cannot publish your changes.

## Workbook prerequisite

Before you can build a funnel chart, you must [add a new chart element and select a data source](/docs/create-a-data-element).

At the core of every chart is an underlying data table (derived from the data source) that supplies the information visualized by the chart. As you build a funnel chart, Sigma automatically groups, aggregates, and calculates the underlying data to create source columns for various chart properties. You can [view the underlying data table](/docs/maximize-or-minimize-a-data-element) while configuring the chart to see how the data is applied.

## Basic funnel chart requirements

To display a funnel chart, configure the following properties in the ![](https://files.readme.io/9b2cac7-element-properties.svg) **Element properties** panel:

* **Chart** - chart type displayed in the workbook
* **Stage** - source column that defines the stages
* **Value** - source column that defines the variable

In a funnel chart, stages reference nominal categories (like campaign pipeline, sales pipeline, recruitment stages) presented as a horizontal bars. A variable measures a value (like number of leads, prospects, candidates) for each stage and determines the width of each bar.

The first stage, shown at the top of the chart, typically represents the initial input of the process and corresponds with the largest stage value (and widest bar). Because value dropoff occurs as data flows through the process, each stage measures a subset of the previous stage value. As a result, the chart progressively narrows and creates a funnel shape.

### Select the chart type

After you [add a new chart](/docs/create-a-data-element) to a workbook, select the chart type:

* In the **Chart** property, click the dropdown field and select **Funnel** from the list. ![](https://files.readme.io/d4675b9-2.png)

> 📘
>
> ### You can also use this dropdown field to convert an existing chart to a different type. Sigma retains all property and format configurations shared by the initial and new type. Unshared properties and formatting are not saved or restored if you further convert the chart.

### Define the stages

Select a source column to define the stages.

> 📘
>
> ### When your data source includes a single column with stage names as values, follow the steps below and add this column to the Stage property. Alternatively, if the data source breaks down each stage as a distinct column of data, skip this step and aggregate the individual stage columns in the Value property (see Define the Variable).

1. In the **Stage** property, click ![](https://files.readme.io/d477078-button-add.svg) **Add column** and select an option from the menu:

   * To generate stage names based on distinct values in an existing column, search or scroll the **Select column** list and select the preferred column name.
   * To generate stage names based on a custom formula, select **New column** and enter a formula in the toolbar.
   > 📘
   >
   > ### You can also select or replace an existing column by dragging and dropping a column name from the Columns list to the Stage property.

   ![](https://files.readme.io/67f6fc9-3.png)

### Define the variable

Configure a source column to define the variable. Sigma automatically aggregates column values associated with the same stage.

1. In the **Value** property, click ![](https://files.readme.io/a7f2ed8-button-add.svg) **Add calculation** and select an option from the menu:

   * To aggregate values of an existing column, search or scroll the **Aggregate column** list and select the preferred column name.
   * To calculate values based on a custom formula, select **New column** and enter a formula in the toolbar.
   * To count the number of rows associated with each stage, select **Row count**.![](https://files.readme.io/e27470a-4.png)
   > 📘
   >
   > ### You can also select an existing column by dragging and dropping a column name from the Columns list to the Value property.
2. [optional] Control how the source column data is calculated and displayed in the chart:

   1. Hover over the source column name, then click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu.
   2. Hover over any of the following items and select the preferred option:
      * **Set aggregate** - Calculate values based on the selected aggregation method.
      * **Transform** - Convert the column to the selected [data value type](/docs/data-types-and-formats).
      * **Format** - Display data labels in the selected format.
   > 📘
   >
   > ### To plot the source column data without aggregating values, clear the **Aggregate values** checkbox in the **Value** property. If this results in an incomplete chart that exceeds the 25,000 data point limit, reaggregate the values or apply data filters to reduce the number of data points.

   ![](https://files.readme.io/096013a-5.png)
   > 📘
   >
   > ### You can also use the toolbar to change the aggregation method (using the formula) and data label format.
3. [optional] Repeat the previous steps to configure multiple stage value source columns. Sigma plots the columns as stacked series on the chart. ![](https://files.readme.io/1957dac-6.png)
4. [optional] Sigma auto-generates source column names and chart titles to reflect the visualized data, but you can customize these fields as needed:

   * To rename a source column, double-click the column name in the **Stage** or **Value** property, then enter a new name. Changes are reflected in the default chart title.
   * To edit the chart title, double-click the title in the chart, then enter a new title.
   > 📘
   >
   > ### Sigma auto-generates the default chart title only. Once the title is customized, it no longer reflects changes to source columns and their names.

   ![](https://files.readme.io/53f9d41-7.png)

## Advanced funnel chart properties and formatting

Sigma features various properties and format options that give you the flexibility to build detailed funnel charts.

The following sections introduce configurations that can enhance your charts and help you deliver specific insights with meaningful and actionable information.

### Configure mark colors

Configure chart mark colors in the ![](https://files.readme.io/bb77e05-element-properties.svg) **Element properties** > **Marks** > **Color** tab to differentiate data.

![](https://files.readme.io/ad5b559-8.png)

| Mark color |  |  |
| --- | --- | --- |
| By category | If only one source column is configured in the **Value** property, the chart defaults to categorical colors that represent stages.  If multiple source columns are configured in the **Value** property, the chart defaults to stacked series with categorical colors that represent each of those columns.  To change the default categorical color variable, select a source column, then select or customize a color palette. |  |
| By scale | Select a source column to define a scaled color variable, then select a color range to apply to the marks. |  |

### Customize data labels

Customize data labels representing conversion rates, stage values, and stage names in the ![](https://files.readme.io/4fe9fc5-element-format.svg) **Element format** > **Data labels** section.

![](https://files.readme.io/75aad9b-9.png)

In addition to showing or hiding the different types of data labels, you can customize the font size and color of each.

You can also select the position of each data label type relative to the chart marks:

| Left | Inline | Right |
| --- | --- | --- |
|  |  |  |

> 📘
>
> ### The funnel chart’s **Color** property may determine the availability of specific data labels and positions. For example, stage names can only be displayed inline when the chart features categorical colors that represent stages (see the **By category** details in [Configure mark colors](/docs/build-a-funnel-chart)).

When you show conversion rates, you can choose a **Percentage style** option to determine how conversion rates are calculated:

| Percentage style | |
| --- | --- |
| % of total | Calculates the value of each stage against the value of the first stage (total value at the top of the funnel).  *Current stage / first stage = conversion rate* |
| % of prior | Calculates the value of each stage against the value of the preceding stage.  *Current stage / preceding stage = conversion rate* |

## All funnel chart format options

* [Background](/docs/customize-element-background)
* [Title](/docs/customize-element-title)
* [Legend](/docs/format-chart-legend)
* [Data labels](/docs/visualization-data-labels)

Updated 3 days ago

---

Related resources

* [Intro to charts](/docs/intro-to-visualizations)
* [Create a data element](/docs/create-a-data-element)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Workbook prerequisite](#workbook-prerequisite)
  + [Basic funnel chart requirements](#basic-funnel-chart-requirements)
  + - [Select the chart type](#select-the-chart-type)
    - [Define the stages](#define-the-stages)
    - [Define the variable](#define-the-variable)
  + [Advanced funnel chart properties and formatting](#advanced-funnel-chart-properties-and-formatting)
  + - [Configure mark colors](#configure-mark-colors)
    - [Customize data labels](#customize-data-labels)
  + [All funnel chart format options](#all-funnel-chart-format-options)