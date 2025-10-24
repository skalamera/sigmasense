# Build a Sankey diagram

# Build a Sankey diagram

Sankey diagrams are typically used to assess the flow and change of data between stages in a process or system. Create simple Sankey diagrams to demonstrate data distribution, workflows, networks, and more, or build advanced multi-level diagrams to analyze complex data relationships and identify changes in variables across stages, categories, or periods.

This document details basic Sankey diagram requirements and introduces key properties and format options to help you enhance your workbook charts.

> 📘
>
> ### Example use cases:
>
> * **Energy analytics**: Measure electricity load and consumption to understand facility performance and gain insight into the origins and transformation of energy.
> * **Financial analytics**: Track annual spend by department, division, and expense category to understand the flow of money and analyze budget vs. spend distribution.
> * **Marketing analytics**: Follow website visitor activity by parent domain and subsequent page visits to understand user navigation and assess website architecture deficiencies.

## User requirements

The ability to create Sankey diagrams and other charts requires the following:

* You must be assigned an [account type](/docs/user-account-types) with the **Edit Workbook** and/or **Explore Workbook** permission enabled.
* You must be the workbook owner or be granted **Can explore** or **Can edit** [workbook permission](/docs/folder-and-document-permissions).

> 🚧
>
> ### If you're granted **Can explore** access to the workbook, you can create and modify chart properties and formatting in **Explore** mode, but you cannot publish your changes.

## Workbook prerequisite

Before you can build a Sankey diagram, you must [add a new chart element and select a data source](/docs/create-a-data-element).

At the core of every chart is an underlying data table (derived from the data source) that supplies the information visualized by the chart. As you build a Sankey diagram, Sigma automatically groups, aggregates, and calculates the underlying data to create source columns for various chart properties. You can [view the underlying data table](/docs/maximize-or-minimize-a-data-element) while configuring the chart to see how the data is applied.

> 📘
>
> ### Sankey diagrams support up to 25,000 data points. If the configurations result in a data set that exceeds this limit, the chart displays the first 25,000 data points, and a warning message indicates that the chart is incomplete. To reduce the number of data points, aggregate the values or apply data filters to the chart or source element.

## Basic Sankey diagram requirements

To create a Sankey diagram, configure the following properties in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/wb-element_viz.svg) **Element properties** panel:

* **Chart** - chart type displayed in the workbook
* **Stages** - source columns that define the stages and categories
* **Value** - source column that defines the data path variable

In a Sankey diagram, stages consist of categories presented as individual rectangular nodes that represent data flow start and end points. Data paths illustrate the direction and quantity of data (like energy consumption, expense, page visitors) flowing between categories, with path widths proportional to the value of the data path variable.

### Select the chart type

After you [add a new chart](/docs/create-a-data-element) to a workbook, select the chart type:

* In the **Chart** property, click the dropdown field and select **Sankey** from the list.

> 📘
>
> ### You can also use this dropdown field to convert an existing chart to a different type. Sigma retains all property and format configurations shared by the initial and new type. Unshared properties and formatting are not saved or restored if you further convert the chart.

### Define the stages and categories

Configure source columns to define the stages and categories.

1. In the **Stage** property, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add column** and select an option from the menu:

   * To generate stage categories based on distinct values in an existing column, search or scroll the **Select column** list and select the preferred column name.
   * To generate stage categories based on a custom formula, select **New column** and enter the formula in the toolbar.
   > 📘
   >
   > ### You can also select or replace an existing column by dragging and dropping a column name from the Columns list to the Stage property.

   ![For the stage option, select new column then search for and select a column.](https://files.readme.io/3d946a5-3.png)
2. [optional] Control how the source column data is categorized and displayed in the chart:

   1. Hover over the source column name, then click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu.
   2. Hover over any of the following items, then select the preferred option:
      * **Truncate date** - Categorize date values by the selected interval or unit of measure.
      * **Transform** - Convert the column to the selected data value type.
      * **Format** - Display data labels in the selected format.
   > 📘
   >
   > ### Availability of column menu items and corresponding options varies depending on the column’s data value type (for example, **Truncate date** is available for date values only).
3. Repeat the previous steps to configure additional stages (a minimum of two stages are required).

   > 📘
   >
   > ### Sigma charts the stages (as start and end points) in order of precedence, from top to bottom. Drag and drop source column names in the Stage property to reorder them as needed.

   ![Select the + to add another stage and search or scroll to the column.](https://files.readme.io/02e110a-5.png)

### Define the variable

Configure a source column to define the data path variable. Sigma automatically aggregates column values associated with the initial stage categories to measure the data flow starting points. Within each of these categories, Sigma aggregates values associated with the subsequent stage categories, then plots these measures as data paths to the end points.

1. In the **Value** property, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add calculation** and select an option from the menu:

   * To aggregate values of an existing column, search or scroll the **Aggregate column** list and select the preferred column name.
   * To calculate values based on a custom formula, select **New column** and enter a formula in the toolbar.
   * To count the number of rows associated with each stage name, select **Row count**.![For the value section, select the + add calculation and select a column.](https://files.readme.io/e95a80b-6.png)
   > 📘
   >
   > ### You can also select an existing column by dragging and dropping a column name from the Columns list to the Value property.
2. [optional] Control how the source column data is calculated and displayed in the chart:

   1. To open the column menu, click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to the right of the source column name.
   2. Hover over any of the following items and select the preferred option:
      * **Set aggregate** - Calculate values based on the selected aggregation method.
      * **Transform** - Convert the column to the selected [data value type](/docs/data-types-and-formats).
      * **Format** - Display data labels in the selected format.
   > 📘
   >
   > ### You can also use the toolbar to change the aggregation method (using the formula) and data label format. If the configurations results in an incomplete chart that exceeds the 25,000 data point limit, apply data filters to reduce the number of data points.
3. [optional] Sigma auto-generates source column names and chart titles to reflect the visualized data, but you can customize these fields as needed:

   * To rename a source column, double-click the column name in the **Stage** or **Value** property, then enter a new name. Changes are reflected in the default chart title.
   * To edit the chart title, double-click the title in the chart, then enter a new title.![Editing the title of the Sankey visualization to read Product Type Revenue > Month of Season](https://files.readme.io/7feb851-8.png)
   > 📘
   >
   > ### Sigma auto-generates the default chart title only. Once the title is customized, it no longer reflects changes to source columns and their names. For information about title customization, see [Customize element title](/docs/customize-element-title).
4. [optional] In the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/wb-element_viz.svg) **Element properties** > **Marks** > **Color** section, select or customize a color palette to apply to the category nodes and paths.

   ![Color selection panel selected and open for the chart, with a predefined color scale selected.](https://files.readme.io/10cd47b-9.png)

## All Sankey diagram format options

* [Background](/docs/customize-element-background)
* [Title](/docs/customize-element-title)
* [Data labels](/docs/visualization-data-labels)

Updated 3 days ago

---

Related resources

* [Intro to charts](/docs/intro-to-visualizations)
* [Intro to data elements](/docs/intro-to-data-elements)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Workbook prerequisite](#workbook-prerequisite)
  + [Basic Sankey diagram requirements](#basic-sankey-diagram-requirements)
  + - [Select the chart type](#select-the-chart-type)
    - [Define the stages and categories](#define-the-stages-and-categories)
    - [Define the variable](#define-the-variable)
  + [All Sankey diagram format options](#all-sankey-diagram-format-options)