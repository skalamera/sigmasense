# Create and format trellis charts

# Create and format trellis charts

Trellis charts (also known as small multiples or panel charts) allow you to compare and analyze multiple subsets of data within a single chart. The subsets are represented by smaller charts (or panels) arranged in rows and columns based on specific data dimensions. The division of data and resulting grid-like structure make it easier to identify patterns, trends, and relationships that can help you uncover valuable insights within large, complex datasets.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Create+and+format+trellis+charts/trellis-chart_intro.png)

This document introduces the concept and structure of trellis charts and explains how to use them to add clarity and value to your charts.

The following chart types support trellising:

* [Bar charts](/docs/build-a-bar-chart)
* [Line charts](/docs/build-a-line-chart)
* [Area charts](/docs/area-charts)
* [Scatter plots](/docs/build-a-scatter-plot)
* [Pie charts](/docs/pie-and-donut-charts)
* [Donut charts](/docs/pie-and-donut-charts)
* [Combo charts](/docs/combo-charts)

## User requirements

The ability to create and format trellis charts requires the following:

* To use this feature, you must have **Can edit** or **Can explore** [access](/docs/folder-and-document-permissions) to the individual workbook.
* You must be in a draft, custom view, or saved view of the workbook.

## Prerequisites

* You must have or create a chart that is compatible with trellising.

## Understanding trellis charts

Trellis charts enable you to quickly and effectively visualize multidimensional data subsets and explore them from different angles. Although you could build an individual chart element for each data subset, you can quickly create a trellis chart that offers several advantages that contribute to data coherence and ease of use, including the following:

* **Organization**: Data subsets are presented in a logical, organized structure that facilitates systematic comparison and exploration.
* **Scalability**: Data updates, including new attributes introduced to the dataset, are seamlessly incorporated into the chart’s dimensions.
* **Consistency**: The shared underlying data ensures consistent application of filters and aggregations, while the use of a single chart provides uniformity in scale, format, and styling.

### Trellis rows and columns

In a trellis chart, rows (vertical divisions) represent one dimension, while columns (horizontal divisions) represent another. The individual panels represent the intersections of specific row and column attributes, which visualize data subsets that are more digestible and easily compared in the context of the dimensions and corresponding attributes.

### Non-trellis vs. trellis

The following charts demonstrate how trellising can enhance data chart.

**No trellising**: This initial chart shows a basic view that compares total revenue per fiscal year from 2019 to 2023. The stacked bars differentiate revenue for each product family, providing an additional dimension to explore within and across each year.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Create+and+format+trellis+charts/trellis-chart_no-trellising.png)

**Trellis columns**: This second chart incorporates trellis columns to deepen the analysis. You can still analyze total revenue by fiscal year and product family, but the additional dimension allows you to compare these data points within and across smaller data subsets based on store region.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Create+and+format+trellis+charts/trellis-chart_trellis-columns.png)

**Trellis rows and columns**: This final chart incorporates trellis rows and columns for even more granular data subsets. As with the previous chart, you can still analyze total revenue by fiscal year and product family, but the two additional dimensions allow you to compare data points within and across data subsets based on the intersections of store regions and product types.

While the grid structure makes it easy to compare revenue between data subsets that share a common store region or product type (shared attributes across the same row or column), you can also obtain meaningful insights by exploring data points across the complete grid.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Create+and+format+trellis+charts/trellis-chart_trellis-rows-and-columns.png)

## Create a trellis chart

1. Select a chart on the workbook page.
2. In the editor panel, select **Trellis**.
3. Add columns to the **Trellis row** and **Trellis column** sections as needed.

   * To create a vertical comparison of data subsets, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add column** in the **Trellis row** property.
   * To create a horizontal comparison of data subsets, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add column** in the **Trellis column** property.
4. Select a column to add using one of the following methods:

   * To derive dimensions from an existing column in the data source, search or scroll the **Select column** list and select the desired column.
   * To create dimensions based on a new column, select **Add new column**, then enter a function or value in the formula bar.

> 💡
>
> ### You can also select an existing column by dragging and dropping a column name from the **Columns** list to the **Trellis row** or **Trellis column** property.

### Create a trellis chart with multiple series

If your chart is a [bar](/docs/build-a-bar-chart), [line](/docs/build-a-line-chart), [area](/docs/area-charts), or [scatter](/docs/build-a-scatter-plot) chart containing multiple series, such as both *Revenue* and *Cost*, you can create a trellis chart for the series

1. Select a chart with at least two series on the workbook page.

   ![A bar chart with revenue and cost columns for the series, with fiscal year on the x-axis](https://files.readme.io/0e5fa5b5702dd7d3b4a692f5b27e7b3eaa3b09df27ac688167af4f62a6da5c62-bar-by-series.png)
2. In the editor panel, select **Trellis**.
3. For **Trellis by**, select **Series**.
4. For **Direction**, select **Row** (default) or **Column**.

![A bar chart with trellis columns, one column for revenue colored by category of product type, and one column for cost, with fiscal year on the x-axis for each chart.](https://files.readme.io/377a575a7ac3ab44c3041b5a10ae5cf37ff7d164fa23ca18d4d5188e3d119d8f-simple-series-trellis.png)
> 💡
>
> ### To remove a trellis by series and set up a trellis by category instead, select **Revert to default**.

## Customize trellis titles and labels

You can change the visibility of trellis titles and labels, customize the chart title, font size, and font color as needed.

1. Select the chart you want to modify on the workbook page.
2. In the editor panel, select **Format**, then click **Trellis** to expand the section.
3. Modify the available options for the trellis:

   * To modify the size of the trellis tiles within the chart, modify the **Tile size**. You can choose **Auto** or **Compact**.
   * For a trellis chart with rows or columns, you can choose to show or hide a border between rows and columns. To show the border, select the checkbox for **Show row border** or **Show column border**.
4. Configure the title and label for the trellis rows or columns in the chart:

   * To show the title, turn on the **Show title** toggle or turn it off to hide the title.
   * To show the label, turn on the **Show label** toggle or turn it off to hide the label.
   * To set the title or label's text, enter the title or label in the relevant text box.
   * To change the font size and color of trellis titles and labels, use the formatting tools:

     |  |  |  |
     | --- | --- | --- |
     |  | **Font size** | Select a font size (10-48px). |
     |  | **Text color** | Enter a hex value or select an option from the color palette or picker. |

## Customize shared trellis components

By default, Sigma displays shared x-axis labels for each column (cartesian charts only), shared y-axis labels for each row (cartesian charts only), and a shared legend for the entire grid. You can customize the trellis format to use shared components or display separate labels and legends for each panel.

1. Select the chart you want to modify.
2. In the editor panel, select **Format**, then click **Trellis** to expand the section.
3. To change the shared components, configure the **X-axis**, **Y-axis**, and **Color legends** fields:

   * To share the axis values or legend, turn on the **X-axis** toggle, **Y-axis** toggle, or both.
   * To display the axis values or legend in each panel, turn off the toggle for the desired axes.
4. To configure custom chart axis marks, such as ticks and grid lines, follow the steps in [Configure chart axis marks](/docs/configure-chart-axis-marks).

Updated about 11 hours ago

---

[Create sparklines in a table (Beta)](/docs/create-sparklines-in-a-table)[Customize chart mark tooltip fields](/docs/customize-chart-mark-tooltip-fields)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Prerequisites](#prerequisites)
  + [Understanding trellis charts](#understanding-trellis-charts)
  + - [Trellis rows and columns](#trellis-rows-and-columns)
    - [Non-trellis vs. trellis](#non-trellis-vs-trellis)
  + [Create a trellis chart](#create-a-trellis-chart)
  + - [Create a trellis chart with multiple series](#create-a-trellis-chart-with-multiple-series)
  + [Customize trellis titles and labels](#customize-trellis-titles-and-labels)
  + [Customize shared trellis components](#customize-shared-trellis-components)