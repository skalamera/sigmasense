# Combo charts

# Combo charts

Combo charts are a type of chart that uses a mixture of chart types. Sigma combo charts support bars, lines, areas, and scatter plots.

## Requirements

* You must be assigned an [account type](/docs/user-account-types) with the **Edit Workbook** and/or **Explore Workbook** permission enabled.
* You must be the workbook owner or be granted **Can explore** or **Can edit** [workbook permission](/docs/folder-and-document-permissions).

> 🚧
>
> If you're granted **Can explore** access to the workbook, you can create and modify visualization properties and formatting in **Explore** mode, but you cannot publish your changes.

## Plot a combo chart

To plot a combo chart, configure the following properties in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/wb-element_viz.svg) **Element properties** tab:

| **Chart** | Chart type displayed in the workbook |
| --- | --- |
| **X-axis** | Source column that defines the x-axis (horizontal axis) categories or variable |
| **Y-axis** | Source column that defines the y-axis (vertical axis) categories or variable |

The chart is empty until all properties are configured.

### Add a combo chart to a workbook

1. Open a workbook in **Explore** or **Edit** mode and [add a new chart element](/docs/create-a-data-element).
2. In the **Chart** property, click the dropdown field and select **Combo** from the list.

### Define the x-axis categories

Configure a source column to define the x-axis categories.

1. In the **X-axis** property, click ![](https://files.readme.io/65a9b53-button-add.svg) **Add column** and select an option from the menu:

   * To generate categories based on distinct values in an existing column, search or scroll the **Select column** list and select the preferred column name.
   * To generate categories based on a custom formula, select **New column** and enter the formula in the toolbar.
   > 💡
   >
   > ### You can also select or replace an existing column by dragging and dropping a column name from the **Columns** list to the **X-axis** property.
2. [optional] Control how the source column data is categorized and displayed in the chart:

   1. Hover over the source column name, then click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu.
   2. Hover over any of the following items, then select the preferred option:

      |  |  |
      | --- | --- |
      | **Truncate date** | Categorize date values by the selected interval or unit of measure. |
      | **Transform** | Convert the column to the selected data value type. |
      | **Format** | Display axis and data labels in the selected format. |
   > 📘
   >
   > ### Availability of column menu items and corresponding options varies depending on the column’s data value type (for example, **Truncate date** is available for date values only).

### Define the y-axis variable

Configure a source column to define the y-axis variable. Sigma automatically aggregates values associated with the same x-axis category, and the aggregation type depends on the data type of the column.

By default, the first column placed on the y-axis is displayed as a bar chart and all additional columns are plotted as lines.

1. In the **Y-axis** property, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add calculation** and select an option from the menu:

   * To aggregate values of an existing column, search or scroll the **Aggregate column** list and select the preferred column name.
   * To calculate values based on a custom formula, select **New column** and enter the formula in the toolbar.
   * To count the number of rows associated with each category, select **Row count**.  
   > 💡
   >
   > ### You can also select an existing column by dragging and dropping a column name from the **Columns** list to the **Y-axis** property.
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

   > 💡
   >
   > ### You can also use the toolbar to change the aggregation method (using the formula) and data label format.
3. [optional] Repeat the previous steps to configure multiple y-axis source columns. Sigma plots each further column as a separate line series on the chart, but you can change the shape of any plotted column from the column menu. See [Change the chart type for a plotted column)](#change-the-chart-type-for-a-plotted-column).
4. [optional] Sigma auto-generates source column names and chart titles to reflect the visualized data, but you can customize these fields as needed:

   * To rename a source column, double-click the column name in the **X-axis** or **Y-axis** property, then enter a new name. Changes are reflected in the default chart title.
   * To edit the chart title, double-click the title in the chart, then enter a new title.
   > 📘
   >
   > ### Sigma auto-generates the default chart title. After the title is customized, it no longer reflects changes to source columns and their names.

![Combo chart showing a bar chart with a line chart superimposed over the bars, with a different y-axis.](https://files.readme.io/e522f53-combo-nice.png)

## Combo chart properties

You can configure the following properties for combo charts:

* [Set up colors](#configure-a-chart-color-by-category).
* [Customize tooltip fields and values](/docs/customize-chart-mark-tooltip-fields).
* Use a [trellis format](/docs/create-and-format-trellis-charts).

### Configure a chart color by category

If your combo chart includes bars, you can set a column to use as a category and split the bar colors by category.

Configure combo chart colors in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/wb-element_viz.svg) **Element properties** > **Marks** > **Color** tab.

You can use color to differentiate data, highlight specific column values, and split the chart bars by category.

|  |  |  |
| --- | --- | --- |
| **Single color** | For each data series, enter a hex code or select an option from the color palette or color picker. | Color mark option with single color displaying for bar series and a drop down available to set the color, and a separate section for other series and a dropdown to set the relevant colors. |
| **By category** | If your combo chart includes bars, select a source column to define color categories for the bar series, then select or customize a color palette for the resulting stacks or clusters. Setting a color by category is not possible for line or other series that do not use bar. | Color mark option with by category displaying for bar series and a drop down available to set the color scale for the series, and a separate section for other series and a dropdown to set the relevant colors. |

![Combo chart showing total products as a count of SKU number compared to quantity sold for each year, split by product type](https://files.readme.io/0833b940bb0ef1e5a69a0672bf67107655d23b57337ad1780b98a3b736f1104a-combo-split-by-color.png)
> 📘
>
> ### Multiple variables in the y-axis result in a stacked or clustered bar series in which each data series represents a measure of a different variable. The **By category** color setting can also generate bar stacks or clusters, but the resulting series represent sub-categories within the configured chart categories that measure the same variable.

## Change the chart type for a plotted column

The chart type for a column plotted on a combo chart can be one of four options: bar, line, area, or scatter.

**Before you start:** This action uses the editor panel. If you have not done so already, open the editor panel from either Explore or Edit mode. See [Workbook modes](/docs/workbook-modes-overview-view-explore-edit).

To change the chart type, do the following:

1. In the editor panel, hover over the column and click the caret ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg).  
   The column menu opens.
2. In the **Shape** submenu, choose **Bar**, **Line**, **Area**, or **Point**.  
   ![Column details menu as described with shape option open to show options of bar, line, area, or point.](https://files.readme.io/5ff3589-combo-line-chart-choose.png)

## Format options

To begin editing a chart's format options:

**Before you start:** This action uses the editor panel. If you have not done so already, open the editor panel from either Explore or Edit mode; see [Workbook modes](/docs/workbook-modes-overview-view-explore-edit).

1. Select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/element-format.svg) **Element format** in the side navigation.
2. Select a format option to view and edit its settings.

### Format categories

The following format categories are available for combo charts:

* **[Element style](/docs/customize-element-background-and-styles)**
* **[Title](/docs/customize-element-title)**
* **X-axis**
* **Y-axis**

  + You can add a secondary y-axis for a column on the left or right side of the chart. See [Format chart axis position](/docs/format-chart-axis-position).
* **[Legend](/docs/format-chart-legend)**
* **Gaps**
* **[Reference marks](/docs/display-chart-reference-marks)**
* **[Trend lines](/docs/add-trend-lines)**
* **[Data labels](/docs/visualization-data-labels)**
* **Area/line style**

Updated 3 days ago

---

Related resources

* [Intro to charts](/docs/intro-to-visualizations)
* [Create a data element](/docs/create-a-data-element)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Plot a combo chart](#plot-a-combo-chart)
  + - [Add a combo chart to a workbook](#add-a-combo-chart-to-a-workbook)
    - [Define the x-axis categories](#define-the-x-axis-categories)
    - [Define the y-axis variable](#define-the-y-axis-variable)
  + [Combo chart properties](#combo-chart-properties)
  + - [Configure a chart color by category](#configure-a-chart-color-by-category)
  + [Change the chart type for a plotted column](#change-the-chart-type-for-a-plotted-column)
  + [Format options](#format-options)
  + - [Format categories](#format-categories)