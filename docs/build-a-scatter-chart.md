# Build a scatter plot

# Build a scatter plot

Scatter plots are typically used to demonstrate a correlation (or lack thereof) between two different variables. Create basic scatter plots to assess patterns, trends, and outliers in your dataset. You can also build advanced charts to include additional variables, plot trend lines, and display data points across quadrants.

This document details basic scatter plot requirements and introduces key properties and format options to help you enhance your workbook charts.

![](https://files.readme.io/4a3a572-1.png)

> 💡
>
> ### Example use cases:
>
> * **Education analytics**: Assess college grades and post-college income to determine a possible correlation between academic performance and job earnings.
> * **Environmental health analytics**: Compare metro health index scores by neighborhood air pollution amount to analyze patterns and identify areas needing intervention.
> * **Retail analytics**: Track price changes and sales amounts by profit to understand consumer response to price changes and identify where pricing did not affect profit.

## User requirements

The ability to create scatter plots and other charts requires the following:

* You must be assigned an [account type](/docs/user-account-types) with the **Edit Workbook** and/or **Explore Workbook** permission enabled.
* You must be the workbook owner or be granted **Can explore** or **Can edit** [workbook permission](/docs/folder-and-document-permissions).

> 🚧
>
> ### If you're granted **Can explore** access to the workbook, you can create and modify chart properties and formatting in **Explore** mode, but you cannot publish your changes.

## Workbook prerequisite

Before you can build a scatter plot, you must [add a new chart element and select a data source](/docs/create-a-data-element).

At the core of every chart is an underlying data table (derived from the data source) that supplies the information visualized by the chart. As you build a scatter plot, Sigma automatically groups, aggregates, and calculates the underlying data to create source columns for various chart properties. You can [view the underlying data table](/docs/maximize-or-minimize-a-data-element) while configuring the chart to see how the data is applied.

> 🚩
>
> ### Scatter plots support up to 25,000 data points. If the configurations result in a data set that exceeds this limit, the chart displays the first 25,000 data points, and a warning message indicates that the chart is incomplete. To reduce the number of data points, aggregate the values or apply data filters to the chart or source element.

## Basic scatter plot requirements

To display a scatter plot, configure the following properties in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/wb-element_viz.svg) **Element properties** tab:

* **Chart** - chart type displayed in the workbook
* **X-axis** - source column that defines the x-axis (horizontal axis) variable
* **Y-axis** - source column that defines the y-axis (vertical axis) variable

In a scatter plot, data points express the intersection of different variables on the x- and y-axis (like revenue and COGS, temperature and precipitation, page views and clicks).

### Select the chart type

After you [add a new chart](/docs/create-a-data-element) to a workbook, select the visualization type:

* In the **Chart** property, click the dropdown field and select **Scatter** from the list.

  ![](https://files.readme.io/d78616a-2.png)

> 📘
>
> ### You can also use this dropdown field to convert an existing chart to a different type. Sigma retains all property and format configurations shared by the initial and new type. Unshared properties and formatting are not saved or restored if you further convert the chart.

### Define the x-axis variable

Configure a source column to define the x-axis variable.

1. In the **X-axis** property, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add column** and select an option from the menu:

   * To plot values from an existing column, search or scroll the **Select column** list and select the preferred column name.
   * To plot values based on a custom formula, select **New column** and enter a formula in the toolbar.
   > 💡
   >
   > ### You can also select or replace an existing column by dragging and dropping a column name from the **Columns** list to the **X-axis** property.

   ![](https://files.readme.io/11bb699-3.png)
2. [optional] Control how the source column data is grouped and displayed in the chart:

   1. Hover over the source column name, then click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu.
   2. Hover over any of the following items, then select the preferred option
      * **Truncate date** - Group date values by the selected interval or unit of measure.
      * **Transform** - Convert the column to the selected [data value type](/docs/data-types-and-formats).
      * **Format** - Display axis and data labels in the selected format.
   > 📘
   >
   > ### Availability of column menu items and corresponding options varies depending on the column’s data value type (for example, **Truncate date** is available for date values only).

   ![](https://files.readme.io/046b373-4.png)

### Define the y-axis variable

Configure a source column to define the y-axis variable. Sigma aggregates y-axis values that correlate with the same x-axis value.

1. In the **Y-axis** property, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add calculation** and select an option from the menu:

   * To aggregate values of an existing column, search or scroll the **Aggregate column** list and select the preferred column name.
   * To calculate values based on a custom formula, select **New column** and enter the formula in the toolbar.
   * To count the number of rows associated with each category, select **Row count**.![](https://files.readme.io/22cff53-5.png)
   > 💡
   >
   > ### You can also select an existing column by dragging and dropping a column name from the **Columns** list to the **Y-axis** property.
2. [optional] Control how the source column data is calculated and displayed in the chart:

   1. Hover over the source column name, then click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu.
   2. Hover over any of the following items, then select the preferred option:
      * **Set aggregate** - Calculate values based on the selected aggregation method.
      * **Transform** - Convert the column to the selected [data value type](/docs/data-types-and-formats).
      * **Format** - Display axis and data labels in the selected format.
   > 📘
   >
   > ### To plot the source column data without aggregating values, clear the **Aggregate values** checkbox in the \*\*Y-axis \*\*property. If this results in an incomplete chart that exceeds the 25,000 data point limit, reaggregate the values or apply data filters to reduce the number of data points.

   ![](https://files.readme.io/cdb77a6-6.png)
   > 💡
   >
   > ### You can also use the toolbar to change the aggregation method (using the formula) and data label format.
3. [optional] Repeat the previous steps to add multiple y-axis source columns. Sigma plots each as a separate point series on the chart.
   ![](https://files.readme.io/62915fa-7.png)
4. [optional] Sigma auto-generates source column names and chart titles to reflect the visualized data, but you can customize these fields as needed:

   * To rename a source column, double-click the column name in the **X-axis** or **Y-axis** property, then enter a new name. Changes are reflected in the default chart title.
   * To edit the chart title, double-click the title in the chart, then enter a new title.
   > 📘
   >
   > ### Sigma auto-generates the default chart title only. Once the title is customized, it no longer reflects changes to source columns and their names.

   ![](https://files.readme.io/da99c50-8.png)

## Advanced scatter plot properties and formatting

Sigma features various properties and format options that give you the flexibility to build advanced scatter plots and variations, including bubble charts and quadrant charts.

The following sections introduce configurations that can enhance your scatter plots and help you deliver specific insights with meaningful and actionable information.

### Configure mark colors

Configure point mark colors in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/wb-element_viz.svg) **Element properties** > **Marks** > **Color** tab to differentiate data, add a color category, or create a color scale.

![](https://files.readme.io/ba82973-9.png)

| Mark colors |  |  |
| --- | --- | --- |
| **Single color** | For each data series, enter a hex code or select an option from the color palette or color picker.  See [Add conditional formatting](#add-conditional-formatting) for information about adding formatting rules. |  |
| **By category** | Select a source column to define color categories, then select or customize a color palette for the resulting multiple series. |  |
| **By scale** | Select a source column to define a color scale, then select a color range to apply to the marks. |  |

> 📘
>
> ### Multiple variables in the y-axis result in a multi-series scatter plot in which each data series represents a measure of a different variable. The **By category** color setting can also generate a multi-series scatter plot, but the resulting series represent sub-categories that measure the same variable.

> 💡
>
> ### As with axis variables, you can control how color category and color scale source column data is calculated and displayed in the chart.

### Add conditional formatting

When you select **Single color** in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/wb-element_viz.svg) **Element properties** > **Marks** > **Color** tab, you can configure formatting rules (**+ Add rule**) that determine point mark colors according to value-based conditions. This creates exceptions to the single-color selection, allowing you to highlight values that meet the specified conditions.

![](https://files.readme.io/37515e1-10.png)

Example:

|  |  |
| --- | --- |
|  |  |

  
> 💡
>
> ### When the conditions of multiple rules are met, Sigma applies the formatting rules in order of precedence, from top to bottom. Drag and drop rule blocks to reorder them as needed.

### Configure mark size

Configure point mark size in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/wb-element_viz.svg) **Element properties** > **Marks** > **Size** tab to add a size variable and create a bubble chart.

![](https://files.readme.io/b372aa7-11.png)

Select a source column to define the size variable. Sigma aggregates values that correlate with the same x-axis value, then proportions the points based on an auto-generated size range. To modify the relative sizing, see [Customize Point Style](/docs/build-a-scatter-plot) below.

![](https://files.readme.io/5883395-12.png)
> 📘
>
> ### As with the axis variables, you can control how the size variable source column data is calculated and displayed in the chart.

### Customize point style

Customize point styles in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/element-format.svg) **Element format** > **Point style** section. When the scatter plot contains multiple y-axis variables, you can modify the different data series individually or together.

![](https://files.readme.io/c5e565b-13.png)

By default, scatter plot points are circular. You can change the point shape to differentiate multiple data series:

| Point shape |  |  |  |  |
| --- | --- | --- | --- | --- |
| Circle | Square | Cross | Diamond | Triangle |
|  |  |  |  |  |

If the chart doesn’t include a [size variable](/docs/build-a-scatter-plot), you can customize the point size in pixels (2-15px) to optimize readability. Otherwise, you can apply relative sizing to change the minimum point size in the range:

| Point size |  |  |
| --- | --- | --- |
| Small | Medium | Large |
|  |  |  |

### Add reference marks

Add reference marks in the ![](https://files.readme.io/64aea4a-element-format.svg) **Element format** > **Reference marks** section to demarcate goals, baselines, or other benchmarks. With scatter plots, you can also use reference marks to create quadrant charts.

![](https://files.readme.io/11b8678-14.png)

| Quadrant chart |  |  |
| --- | --- | --- |
| Reference line | Create vertical and horizontal lines to divide the chart into four segments. |  |
| Reference band | Create vertical and horizontal bands to differentiate segments by color. |  |

## All scatter plot format options

* [Background](/docs/customize-element-background)
* [Title](/docs/customize-element-title)
* [X-axis](/docs/format-chart-axis-position)
* [Y-axis](/docs/format-chart-axis-position)
* [Legend](/docs/format-chart-legend)
* [Trellis](/docs/create-and-format-trellis-charts)
* [Data labels](/docs/visualization-data-labels)
* [Reference marks](/docs/visualization-reference-marks)
* [Trend lines](/docs/add-trend-lines)
* [Point style](/docs/build-a-scatter-plot)

Updated 3 days ago

---

Related resources

* [Intro to charts](/docs/intro-to-visualizations)
* [Create a data element](/docs/create-a-data-element)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Workbook prerequisite](#workbook-prerequisite)
  + [Basic scatter plot requirements](#basic-scatter-plot-requirements)
  + - [Select the chart type](#select-the-chart-type)
    - [Define the x-axis variable](#define-the-x-axis-variable)
    - [Define the y-axis variable](#define-the-y-axis-variable)
  + [Advanced scatter plot properties and formatting](#advanced-scatter-plot-properties-and-formatting)
  + - [Configure mark colors](#configure-mark-colors)
    - [Add conditional formatting](#add-conditional-formatting)
    - [Configure mark size](#configure-mark-size)
    - [Customize point style](#customize-point-style)
    - [Add reference marks](#add-reference-marks)
  + [All scatter plot format options](#all-scatter-plot-format-options)