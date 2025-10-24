# Build a waterfall chart

# Build a waterfall chart

Waterfall charts are typically used to show changes in one or two categories of data over a period.

This document details basic waterfall chart requirements and introduces key properties and format options to help you enhance your workbook charts.

![Waterfall chart showing total sales quantity for each year, plotted as the difference from the prior year, with 2024 showing as a sharp decrease because the year is only half over.](https://files.readme.io/5633508-waterfall-thumbnail.png)

> 💡
>
> ### Example use cases:
>
> * **Accounting analytics**: Measure the positive and negative contributions to an overall budget.
> * **Financial analytics**: Track revenue and spend for a project, department, or an entire organization.
> * **Retail analytics**: Track positive and negative foot traffic over time for a store or region.
> * **HR analytics**: Measure employee retention rates as part of total employee headcount tracking.

## User requirements

The ability to create waterfall charts and other charts requires the following:

* You must be assigned an [account type](/docs/user-account-types) with the **Edit Workbook** and/or **Explore Workbook** permission enabled.
* You must be the workbook owner or be granted **Can explore** or **Can edit** [workbook permission](/docs/folder-and-document-permissions).

> 🚧
>
> If you're granted **Can explore** access to the workbook, you can create and modify visualization properties and formatting in **Explore** mode, but you cannot publish your changes.

  

## Basic waterfall chart requirements

To plot a waterfall chart, configure the following properties in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/wb-element_viz.svg) **Element properties** tab:

* **Chart**: Chart type displayed in the workbook
* **X-axis**: Source column that defines the x-axis (horizontal axis) categories or variable
* **Y-axis**: source column that defines the y-axis (vertical axis) categories or variable

In a waterfall chart, one axis typically represents ordinal or nominal categories (like stages, regions, departments) presented as vertical or horizontal bars. The other axis represents a variable that measures a value (like sales, leads, expenses) for each category and determines the height of the corresponding bar. The type of data affiliated with each axis depends on the chart orientation, which you can modify at any time.

> 🚩
>
> At the core of every visualization is an underlying data table (derived from the data source) that supplies the information visualized by the chart. As you build your chart, Sigma automatically calculates and structures the data to map the element properties to source columns in the underlying data table. For information about how to view the underlying data while you configure the chart, see [Maximize or minimize a data element](/docs/maximize-or-minimize-a-data-element).

  

### Add a waterfall chart

Add a new chart element and designate it as a waterfall chart.

1. Open a workbook in **Explore** or **Edit** mode and add a new chart element.
2. In the **Chart** property, click the dropdown field and select **Waterfall** from the list.

![Vizualiation dropdown with Bar currently selected, hovering over the option for Waterfall.](https://files.readme.io/68785d3-waterfall-in-menu.png)
> 📘
>
> ### You can also use this dropdown field to convert an existing chart to a different type. Sigma retains all property and format configurations shared by the initial and new type. Properties and formatting not shared by the new type are not retained.

### Define the categories

Define the categories for the chart by configuring a source column to use. Because waterfall charts are best for showing change over time, select a date column:

1. In the X-axis property, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add column** and select an option from the menu:

   * To generate categories based on distinct values in an existing column, search or scroll the **Select column** list and select the column name.
   * To generate categories based on a custom formula, select **New column** and enter the formula in the toolbar.

   Select or replace an existing column by dragging and dropping a column name from the Columns list to the applicable axis property.
2. [optional] Adjust how the source column data is categorized and displayed in the chart:

   1. Hover over the source column name, then click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu.
   2. Hover over any of the following items, then select option you want to use:

      * **Truncate date** - Categorize date values by the selected interval or unit of measure.
      * **Transform** - Convert the column to the selected [data value type](/docs/data-types-and-formats).
      * **Format** - Display axis and data labels in the selected format.
   > 📘
   >
   > ### Availability of column menu items and corresponding options varies depending on the data type of the column. For example, **Truncate date** is only available for date values.

### Define the variable

Define the chart variable, or what has changed over time, by configuring a source column. When you add a source column, Sigma automatically aggregates values associated with the same chart category.

1. In the Y-axis property, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add calculation** and select an option from the menu:

   * To aggregate values of an existing column, search or scroll the **Aggregate column** list and select the column name.
   * To calculate values based on a custom formula, select **New column** and enter the formula in the toolbar.
   * To use a count the number of rows associated with each category, select **Row count**.

   > 📘
   >
   > This visualization supports up to 25,000 data points. If the configurations result in a data set that exceeds this limit, the visualization displays the first 25,000 data points, and a warning message indicates that the chart is incomplete. To reduce the number of data points, aggregate the values or apply data filters to the visualization or source element.

![Select the plus to add a Y-axis column, then search for the column that you want to add.](https://files.readme.io/29cba4a-waterfall-add-column-x.png)
> 💡
>
> ### You can also select an existing column by dragging and dropping a column name from the **Columns** list to the applicable axis property.

2. [optional] Adjust how the source column data is calculated and displayed in the chart:

   1. Hover over the source column name, then click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu.
   2. Hover over any of the following items, then select the option you want to use:

      * **Set aggregate** - Calculate values based on the selected aggregation method.
      * **Transform** - Convert the column to the selected data value type.
      * **Format** - Display axis and data labels in the selected format.
   > 📘
   >
   > ### To plot the source column data without aggregating values, clear the **Aggregate values** checkbox in the **Y-axis** property. If this results in an incomplete chart that exceeds the 25,000 data point limit, aggregate the values again or apply data filters to reduce the number of data points.

   > 💡
   >
   > ### You can also use the toolbar to change the aggregation method (using the formula) and data label format.
3. [optional] Repeat the previous steps to add additional y-axis source columns and create a stacked waterfall chart.

By default, a waterfall chart shows the sum of values over time. If you only have one y-axis source column, you can change the display formatting to show the difference in values across each period. See [Customize waterfall shape](#customize-waterfall-shape).

## Customize your waterfall chart

Sigma auto-generates source column names and chart titles to reflect the visualized data, but you can customize these fields as needed:

* To rename a source column, double-click the column name in the **X-axis** or **Y-axis** property, then enter a new name. Changes are reflected in the default chart title.
* To edit the chart title, double-click the title in the chart, then enter a new title.

  > 📘
  >
  > ### Sigma auto-generates a default chart title. After you customize the title, the chart title no longer reflects changes to source columns and their names.

## Advanced waterfall chart properties and formatting

Sigma features various properties and format options that give you the flexibility to build advanced waterfall charts, including stacked waterfall charts.

The following sections introduce configurations that can enhance your charts and help you deliver specific insights with meaningful and actionable information.

### Change stacking

When you add multiple source columns, the values are stacked by default. You can change the chart formatting to remove the stacking.

![Icon options to choose no stacking or stacked below the option to select a visualization.](https://files.readme.io/3546315-waterfall-stack-options.png)

| Stacking |  |  |
| --- | --- | --- |
| **No stacking** | Plot multiple data series as separate waterfall charts with subtotals for each series. | Waterfall chart with two values for the y-axis, plotted as 2 separate bars on the waterfall chart. |
| **Stacked** | Plot multiple data series as cumulative waterfall segments. Compare subcategory contributions to each category’s total sum value in the resulting stacked waterfall chart. | Waterfall chart with multiple data series as cumulative waterfall segments. |

### Configure mark colors

Configure waterfall mark colors in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/wb-element_viz.svg) **Element properties** > **Marks** > **Color** tab to differentiate data and highlight specific values.

![Color options for waterfall, with an unlabeled color picker to choose the increase, decrease, and total values.](https://files.readme.io/56e7c00-mark-colors-waterfall.png)

| Mark colors |  |  |
| --- | --- | --- |
| **By series** | Select a color for the increase, decrease, and total values for the waterfall chart. For information about adding formatting rules, see [Add conditional formatting](#add-conditional-formatting) in this document. | Color picker open, with options to set a color for the Increase in values, the Decrease in values, and the Total values (start and end) in the waterfall chart. |

### Add conditional formatting

In the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/wb-element_viz.svg) **Element properties** > **Marks** > **Color** tab, you can configure formatting rules (**+ Add rule**) that determine waterfall mark colors according to value-based conditions, in addition to the increase and decrease colors used for the waterfall chart.

![Formatting rule options, for example, to apply conditional formatting to select columns (with a drop-down menu to adjust this), a formatting rule to specify Greater than a constant value that you can enter, and a style option to specify the color of the chart option. The greater than option is configurable. ](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+Bar+Chart/bar_conditional-formatting_rule.png)

Example:

|  |  |
| --- | --- |
| Conditional formatting rule set up to show a yellow color if the sum of sales quantity is less than 10,000,000. | Waterfall chart with sum calculations, where the value for 2024 is yellow and the values for 2020 (start year), 2021, 2022, and 2023 are green (or gray for the start year). |

> 💡
>
> ### When the conditions of multiple rules are met, Sigma applies the formatting rules in order of precedence, from top to bottom. Drag and drop rule blocks to reorder them as needed.

### Customize tooltip fields and values

Customize chart mark tooltip fields in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/wb-element_viz.svg) **Element properties** > **Marks** > **Tooltip** tab to display the most relevant metrics and data attributes. For more information, see [Customize chart mark tooltip fields](/docs/customize-chart-mark-tooltip-fields).

For example, you can customize the default tooltip by removing the X-axis chart value from the tooltip and adding a new aggregate column, showing a distinct count of SKU numbers, in the **Tooltip** tab.

| Default | Custom column in tooltip |
| --- | --- |
| Default tooltip value showing the value with SI units, showing +15.88M | Adjusting the tooltip value to use whole number formatting, so the same option on the chart shows +15,876,823. |

## Customize waterfall shape

You can customize the shape of the waterfall. In ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/element-format.svg) **Element format**, select **Waterfall shape** and configure the available options.

### Set the calculation to display

You can only choose the calculation to display for waterfall charts that display one source column (are not stacked).

|  |  |
| --- | --- |
| **Sum** displays the sum of the values over time. |  |
| **Difference** displays the difference in values between each period. |  |

### Configure the start value

Choose from several options for the start value of your waterfall chart:

|  |  |
| --- | --- |
| **First value in data** uses the first value in the data as the starting point for the chart. Default value. |  |
| **None** does not display a start value and the first value in the data displays as part of the waterfall. |  |
| **Custom** uses a constant value or an aggregated column as the starting value. If you select a **Custom** start value, you can customize the start value label. |  |

### Configure the end value

|  |  |
| --- | --- |
| Select the **Show end value** checkbox to display an end value. The end value is shown by default. |  |
| For **End value label**, enter a label to describe the end value on the waterfall chart. |  |

### Show connector lines

Select the **Show connector line** checkbox to show a line connecting the values on the waterfall chart. You can then select a **Connector line color**.

| Default | With connector lines |
| --- | --- |
|  |  |

## All waterfall chart format options

* [Background](/docs/customize-element-background)
* [Title](/docs/customize-element-title)
* [X-axis](/docs/format-chart-axis-position)
* [Y-axis](/docs/format-chart-axis-position)
* [Legend](/docs/format-chart-legend)
* [Data labels](/docs/visualization-data-labels)
* [Reference marks](/docs/visualization-reference-marks)

Updated 3 days ago

---

Related resources

* [Intro to charts](/docs/intro-to-visualizations)
* [Create a data element](/docs/create-a-data-element)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Basic waterfall chart requirements](#basic-waterfall-chart-requirements)
  + - [Add a waterfall chart](#add-a-waterfall-chart)
    - [Define the categories](#define-the-categories)
    - [Define the variable](#define-the-variable)
  + [Customize your waterfall chart](#customize-your-waterfall-chart)
  + [Advanced waterfall chart properties and formatting](#advanced-waterfall-chart-properties-and-formatting)
  + - [Change stacking](#change-stacking)
    - [Configure mark colors](#configure-mark-colors)
    - [Add conditional formatting](#add-conditional-formatting)
    - [Customize tooltip fields and values](#customize-tooltip-fields-and-values)
  + [Customize waterfall shape](#customize-waterfall-shape)
  + - [Set the calculation to display](#set-the-calculation-to-display)
    - [Configure the start value](#configure-the-start-value)
    - [Configure the end value](#configure-the-end-value)
    - [Show connector lines](#show-connector-lines)
  + [All waterfall chart format options](#all-waterfall-chart-format-options)