# Use metrics in a workbook

# Use metrics in a workbook

Metrics are custom aggregate calculations that you can reuse across workbook [data elements](/docs/intro-to-data-elements) that share the same data source: a dataset or a connection table. Define metrics at the level of the data source, and apply them to workbooks to ensure consistent metric logic across tables, visualizations, and pivot tables.

This document explains how to use metrics in a workbook to perform standard calculations with ease and efficiency. For more details about metrics in data models, datasets, and database tables, see [About metrics](/docs/about-metrics). To create or manage metrics, see [Create and manage metrics](/docs/create-and-manage-metrics).

Because metrics are aggregate calculations, add them to aggregated data:

* [Grouped tables](#add-a-metric-to-a-grouped-table)
* [Summary metrics for a table](#add-a-metric-to-the-summary-bar)
* [Visualizations](#add-a-metric-to-a-visualization)
* [Pivot table values](#add-a-metric-as-a-pivot-value)

You can also [use metrics in formulas](#use-a-metric-in-a-calculated-column).

## Requirements

To use metrics in workbooks, you must have the following access:

* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Full explore** or **Create, edit, and publish workbooks** permissions enabled.
* You must be the workbook owner, or have **Can Explore** or **Can Edit** [workbook permissions](/docs/folder-and-document-permissions).

## View metric details

* In a workbook, you can view available metrics of a data element in the **Element properties** > **Metrics** tab.
* Hover over any metric to see its title, description, and formula.
* Metrics are specific to an element's data source. All defined metrics appear in the **Metrics** tab. To create new metrics, see [Create and manage metrics](/docs/create-and-manage-metrics).
* Metric suggestions also appear in the formula bar. Start typing the name of the metric to see auto-complete suggestions. To find which metrics are available, type "metrics", and scroll through the available options. Descriptions of the metrics appear as you scroll through the menu.

## Add a metric to a grouped table

To calculate a metric as an aggregate within a grouping:

1. Select a table with at least one column grouping.
2. For **Calculations**, select **+** (**Add column...**) and select the metric.

## Add a metric to the summary bar

To calculate a metric as an aggregate for the entire table:

1. In the summary bar, click **^** to expand the summary bar, then select **+** (**Add summary...**).
2. Choose the metric name from the list of available metrics and columns.

> 📘
>
> ### Do not add another aggregation on the metric, because the metric is already aggregated.

## Add a metric to a visualization

You can use a metric like any aggregate calculation in a visualization. Add a metric to a chart as the value axis or add the metric to a tooltip. Depending on the chart, you can also use a metric to specify the color scale, and more.

### Chart a metric on the value axis

To add a metric to the value axis, usually the y-axis, of a visualization:

1. Next to the name of the axis, click **+** (**Add column...**).
2. In the menu that appears, under the **Metrics** header, select the metric.

### Add a metric to a tooltip

To add a metric to a visualization's tooltip, follow these steps:

1. Under the **Marks** options, select the **Tooltip** tab.
2. Click **Metrics**.
3. Choose the metric from the list, and drag it to the **Select column** area.
4. Alternatively, click the plus icon, , in the **Select column** area, and choose the metric from the drop-down menu.

## Add a metric as a pivot table value

In pivot tables, you can add metrics to the **Values** area.

1. In the **Values** section of the pivot table, select **+** (**Add column...**).
2. In the menu that appears, under the **Metrics** header, select the metric.

## Use a metric in a calculation column

Reference metrics in formulas to generate dynamic values in calculation columns. Use the syntax `[Metrics/<Metric Name>]` to reference a specific metric.

For example, the following formula references a metric named *Unique Users*:

```
If([Metrics/Unique Users] > 500, "Popular", "Unpopular")
```

> 💡
>
> ### While you cannot directly reference metrics in [dynamic text](/docs/text-elements#add-dynamic-text-based-on-your-data), you can include metric output using calculation columns. Create a calculation column that references the metric, then reference that column in the dynamic text formula.

Updated 3 days ago

---

Related resources

* [Create and manage metrics](/docs/create-and-manage-metrics)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [View metric details](#view-metric-details)
  + [Add a metric to a grouped table](#add-a-metric-to-a-grouped-table)
  + [Add a metric to the summary bar](#add-a-metric-to-the-summary-bar)
  + [Add a metric to a visualization](#add-a-metric-to-a-visualization)
  + - [Chart a metric on the value axis](#chart-a-metric-on-the-value-axis)
    - [Add a metric to a tooltip](#add-a-metric-to-a-tooltip)
  + [Add a metric as a pivot table value](#add-a-metric-as-a-pivot-table-value)
  + [Use a metric in a calculation column](#use-a-metric-in-a-calculation-column)