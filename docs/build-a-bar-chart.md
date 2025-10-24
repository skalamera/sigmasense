# Build a bar chart

# Build a bar chart

Bar charts are typically used to compare values across categories or groups of data. Create basic single-series bar charts, or build advanced charts to compare multiple variables, measure values against reference marks, evaluate parts of a whole, and more.

This document details basic bar chart requirements and introduces key properties and format options to help you enhance your workbook charts.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+Bar+Chart/bar-chart.png)

> 💡
>
> ### Example use cases:
>
> * **Store analytics**: Measure total sales by product category to identify top and bottom performing categories.
> * **Marketing analytics**: Track unique website page views by ad referral site (such as LinkedIn and GoogleAds) to understand ad performance trends and referral site effectiveness.
> * **Accounting analytics**: Monitor travel expenses by spend category to understand travel spend and identify categories that exceed expectations.
> * **Education analytics** (histogram): Count student exam results by score range to analyze frequency distribution and understand performance variability.

## User requirements

The ability to create bar charts and other charts requires the following:

* You must be assigned an [account type](/docs/user-account-types) with the **Edit Workbook** and/or **Explore Workbook** permission enabled.
* You must be the workbook owner or be granted **Can explore** or **Can edit** [workbook permission](/docs/folder-and-document-permissions).

> 🚧
>
> ### If you're granted **Can explore** access to the workbook, you can create and modify chart properties and formatting in **Explore** mode, but you cannot publish your changes.

## Basic bar chart requirements

To plot a bar chart, configure the following properties in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/wb-element_viz.svg) **Element properties** tab:

|  |  |
| --- | --- |
| **Chart** | Chart type displayed in the workbook |
| **X-axis** | Source column that defines the x-axis (horizontal axis) categories or variable |
| **Y-axis** | Source column that defines the y-axis (vertical axis) categories or variable |

In a bar chart, one axis typically represents ordinal or nominal categories (like stages, regions, departments) presented as vertical or horizontal bars. The other axis represents a variable that measures a value (like sales, leads, expenses) for each category and determines the height or length of the corresponding bar. The type of data affiliated with each axis depends on the chart orientation, which you can modify at any time.

> 🚩
>
> ### At the core of every chart is an underlying data table (derived from the data source) that supplies the information visualized by the chart. As you build a bar chart, Sigma automatically calculates and structures the data to map the element properties to source columns in the underlying data table. For information about how to view the underlying data while you configure the chart, see [Maximize or minimize a data element](/docs/maximize-or-minimize-a-data-element).

### Add a bar chart

Add a chart element to your workbook and designate it as a bar chart:

1. Open a workbook in **Explore** or **Edit** mode and add a new chart element.
2. In the **Chart** property, click the dropdown field and select **Bar** from the list.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+Bar+Chart/bar_visualization-type.png)
   > 📘
   >
   > ### You can also use this dropdown field to convert an existing chart to a different type. Sigma retains all property and format configurations shared by the initial and new type. Unshared properties and formatting are not saved or restored if you further convert the chart.

### Define the categories

Configure a source column to define the chart categories.

When building a vertical bar chart (default orientation), apply the following steps to the **X-axis** property. When building a horizontal bar chart, apply the steps to the **Y-axis** property. For information about chart orientation and how it affects chart axes, see [**Change orientation and stacking**](#change-orientation-and-stacking) in this document.

1. In the applicable axis property, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add column** and select an option from the menu:

   * To generate categories based on distinct values in an existing column, search or scroll the **Select column** list and select the preferred column name.
   * To generate categories based on a custom formula, select **New column** and enter the formula in the toolbar. For example, when building a histogram, create a custom formula using the [**BinRange**](/docs/binrange) or [**BinFixed**](/docs/binfixed) function to generate categories based on value ranges.
   > 💡
   >
   > ### You can also select or replace an existing column by dragging and dropping a column name from the Columns list to the applicable axis property.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+Bar+Chart/bar_define-categories_step-1.png)
2. [optional] Control how the source column data is categorized and displayed in the chart:

   1. Hover over the source column name, then click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu.
   2. Hover over any of the following items, then select the preferred option:

      |  |  |
      | --- | --- |
      | **Truncate date** | Categorize date values by the selected interval or unit of measure. |
      | **Transform** | Convert the column to the selected [data value type](/docs/data-types-and-formats) . |
      | **Format** | Display axis and data labels in the selected format. |
   > 📘
   >
   > ### Availability of column menu items and corresponding options varies depending on the column’s data value type (for example, Truncate date is available for date values only).

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+Bar+Chart/bar_define-categories_step-2.png)

### Define the variable

Configure a source column to define the chart variable. Sigma automatically aggregates values associated with the same chart category.

Apply the following steps to the Y-axis property when building a vertical bar chart (default orientation) or the X-axis property when building a horizontal bar chart. For information about chart orientation and how it affects chart axes, see [Change orientation and stacking](#change-orientation-and-stacking) in this document.

1. In the applicable axis property, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add calculation** and select an option from the menu:

   * To aggregate values of an existing column, search or scroll the **Aggregate column** list and select the preferred column name.
   * To calculate values based on a custom formula, select **New column** and enter the formula in the toolbar.
   * To count the number of rows associated with each category, select **Row count**.
   > 📘
   >
   > ### Bar charts support up to 25,000 data points. If the configurations result in a data set that exceeds this limit, the chart displays the first 25,000 data points, and a warning message indicates that the chart is incomplete. To reduce the number of data points, aggregate the values or apply data filters to the chart or source element.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+Bar+Chart/bar_define-metric_step-1.png)
   > 💡
   >
   > ### You can also select an existing column by dragging and dropping a column name from the **Columns** list to the applicable axis property.
2. [optional] Control how the source column data is calculated and displayed in the chart:

   1. Hover over the source column name, then click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu.
   2. Hover over any of the following items, then select the preferred option:

      |  |  |
      | --- | --- |
      | **Set aggregate** | Calculate values based on the selected aggregation method. |
      | **Transform** | Convert the column to the selected data value type. |
      | **Format** | Display axis and data labels in the selected format. |
   > 📘
   >
   > ### To plot the source column data without aggregating values, clear the **Aggregate values** checkbox in the **Y-axis** property. If this results in an incomplete chart that exceeds the 25,000 data point limit, reaggregate the values or apply data filters to reduce the number of data points.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+Bar+Chart/bar_define-metric_step-2.png)
   > 💡
   >
   > ### You can also use the toolbar to change the aggregation method (using the formula) and data label format.
3. [optional] Repeat the previous steps to add multiple y-axis source columns. Sigma plots the columns as [stacked or clustered](#change-orientation-and-stacking) series.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+Bar+Chart/bar_define-metric_step-3.png)
4. [optional] Sigma auto-generates source column names and chart titles to reflect the visualized data, but you can customize these fields as needed:

   * To rename a source column, double-click the column name in the **X-axis** or **Y-axis** property, then enter a new name. Changes are reflected in the default chart title.
   * To edit the chart title, double-click the title in the chart, then enter a new title.
   > 📘
   >
   > ### Sigma auto-generates the default chart title only. Once the title is customized, it no longer reflects changes to source columns and their names.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+Bar+Chart/bar_define-metric_step-4.png)

## Advanced bar chart properties and formatting

Sigma features various properties and format options that give you the flexibility to build advanced bar charts and variations, including stacked, percent stacked, clustered (grouped), and dual-axis bar charts.

The following sections introduce configurations that can enhance your bar charts and help you deliver specific insights with meaningful and actionable information.

### Change orientation and stacking

Change bar chart orientation and stacking in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/wb-element_viz.svg) **Element properties** > **Chart** property to optimize the way you compare data across and within categories.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+Bar+Chart/bar_properties_orientation-stacking.png)

| Orientation |  |  |
| --- | --- | --- |
| **Vertical** | Categorize data on the x-axis and measure values on the y-axis to create vertical bar marks. |  |
| **Horizontal** | Categorize data on the y-axis and measure values on the x-axis to create horizontal bar marks. |  |

| Stacking |  |  |
| --- | --- | --- |
| **No stacking** | Plot multiple data series as separate bars within categories. Compare values across and within categories in the resulting clustered bar chart. |  |
| **Stacked** | Plot multiple data series as cumulative bar segments. Compare subcategory contributions to each category’s total sum value in the resulting stacked bar chart. |  |
| **Stacked 100%** | Plot multiple data series as stacked bars totaling 100% of each category’s total sum value. Compare subcategory distribution in the resulting percent stacked bar chart. |  |

### Configure mark colors

You can configure the bar mark colors in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/wb-element_viz.svg) **Element properties** > **Marks** > **Color** tab to differentiate data, highlight specific values, use color to split bar values by category, or apply a color scale.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+Bar+Chart/bar_marks_color.png)

| Mark color |  |  |
| --- | --- | --- |
| **Single color** | For each data series, enter a hex code or select an option from the color palette or color picker.  For information about adding formatting rules, see [Add conditional formatting](#add-conditional-formatting) in this document. |  |
| **By category** | Select a source column to define color categories, then select or customize a color palette for the resulting stacks or clusters. |  |
| **By scale** | Select a source column to define the color scale, then select a color range to apply to the marks. |  |

> 📘
>
> ### Multiple variables in the y-axis (in a vertical bar chart) or x-axis (in a horizontal bar chart) result in a stacked or clustered bar chart in which each data series represents a measure of a different variable. The **By category** color setting can also generate bar stacks or clusters, but the resulting series represent sub-categories (within the configured chart categories) that measure the same variable.

### Add conditional formatting

When you select **Single color** in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/wb-element_viz.svg) **Element properties** > **Marks** > **Color** tab, you can configure formatting rules (**+ Add rule**) that determine bar mark colors according to value-based conditions. This creates exceptions to the single-color selection, allowing you to highlight values that meet the specified conditions.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+Bar+Chart/bar_conditional-formatting_rule.png)

Example:

|  |  |
| --- | --- |
|  |  |

> 💡
>
> ### When the conditions of multiple rules are met, Sigma applies the formatting rules in order of precedence, from top to bottom. Drag and drop rule blocks to reorder them as needed.

### Customize tooltip fields and values

Customize chart mark tooltip fields in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/wb-element_viz.svg) **Element properties** > **Marks** > **Tooltip** tab to display the most relevant metrics and data attributes. For more information, see [Customize chart mark tooltip fields](/docs/customize-chart-mark-tooltip-fields) in this document.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+Bar+Chart/bar_marks_tooltip.png)

When you apply [chart stacking](#change-orientation-and-stacking), you can also customize tooltips in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/element-format.svg) **Element format** > **Tooltip** section to display the variable value as a percentage of the cumulative stack.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+Bar+Chart/bar_format_tooltip.png)

| Tooltip value display |  |
| --- | --- |
| Default | Percent |
|  |  |

### Resize gap width

Resize gaps between bar marks in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/element-format.svg) **Element format** > **Gaps** section. Gap widths are auto-sized to optimize readability, but Sigma gives you the flexibility to customize bar chart spacing.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+Bar+Chart/bar_format_gap-width.png)

| Gap width |  |  |
| --- | --- | --- |
| Small | Medium | Large |
|  |  |  |

## All bar chart format options

* [Background](/docs/customize-element-background)
* [Title](/docs/customize-element-title)
* [X-axis](/docs/format-chart-axis-position)
* [Y-axis](/docs/format-chart-axis-position)
* [Legend](/docs/format-chart-legend)
* [Trellis](/docs/create-and-format-trellis-charts)
* [Data labels](/docs/visualization-data-labels)
* [Gaps](#resize-gap-width)
* [Tooltip](#customize-tooltip-fields-and-values)1
* [Reference marks](/docs/visualization-reference-marks)
* [Trend lines](/docs/add-trend-lines)

1Tooltip formatting is supported by stacked bar charts only.

Updated 3 days ago

---

Related resources

* [Intro to charts](/docs/intro-to-visualizations)
* [Create a data element](/docs/create-a-data-element)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Basic bar chart requirements](#basic-bar-chart-requirements)
  + - [Add a bar chart](#add-a-bar-chart)
    - [Define the categories](#define-the-categories)
    - [Define the variable](#define-the-variable)
  + [Advanced bar chart properties and formatting](#advanced-bar-chart-properties-and-formatting)
  + - [Change orientation and stacking](#change-orientation-and-stacking)
    - [Configure mark colors](#configure-mark-colors)
    - [Add conditional formatting](#add-conditional-formatting)
    - [Customize tooltip fields and values](#customize-tooltip-fields-and-values)
    - [Resize gap width](#resize-gap-width)
  + [All bar chart format options](#all-bar-chart-format-options)