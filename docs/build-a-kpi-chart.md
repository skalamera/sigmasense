# Build a KPI chart

# Build a KPI chart

> 🚩
>
> Sigma's **KPI** chart element has replaced the **Single Value** visualization (SVV) option. For information about the SVV deprecation and benefits of KPI charts, see the [Sigma Community post](https://community.sigmacomputing.com/t/kpi-chart-to-replace-single-value-visualization-chart/2533).

Key performance indicator (KPI) charts highlight single metric values typically used to measure performance or progress toward goals. Create a KPI chart to summarize the total value of a metric for a specific period, or include additional data to compare the metric’s value over time and measure it against a benchmark or target value.

![KPI chart showing a single value with a trend indicator and an area chart that shows a benchmark and actual values line for a time period below the single value.](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+KPI+Chart/kpi-chart_intro.png)

> 💡
>
> ### Example use cases:
>
> * **Marketing analytics**: Track click-through rates to highlight email campaign performance over time.
> * **Executive dashboarding**: Measure monthly year-over-year revenue to understand how the current month’s revenue compares to the previous year benchmark.
> * **Manufacturing analytics**: Report cycle time to analyze the amount of time it takes a product to complete the manufacturing process.

## User requirements

The ability to create KPI charts and other charts requires the following:

* You must be assigned an [account type](/docs/user-account-types) with the **Edit Workbook** and/or **Explore Workbook** permission enabled.
* You must be the workbook owner or be granted **Can explore** or **Can edit** [workbook permission](/docs/folder-and-document-permissions).

> 🚧
>
> ### If you’re granted **Can explore** access to the workbook, you can create and modify chart properties and formatting in **Explore** mode, but you cannot publish your changes.

## KPI chart variations

Sigma’s KPI charts allow you to track and display metrics in various ways depending on how you configure the element properties.

### Static variations

|  |  |
| --- | --- |
|  | **Summary value**   Summarize the metric's global value to understand overall performance or magnitude.    The KPI chart highlights the global summary, which aggregates the metric values across the entire dataset.  Required element properties:   * [Value](#calculate-the-metric) |
|  | **Benchmark summary comparison**   Summarize a metric's global value against a benchmark or target value. Assess relative performance and gain insight into patterns, relationships, and correlations.    The KPI chart highlights the global summary, which aggregates the metric values across the entire dataset. It also displays a comparison as a percentage, delta, or absolute value.  Required element properties:   * [Value](#calculate-the-metric) * [Comparison](#select-a-comparison-value)   (Column) |

### Time series variations

|  |  |
| --- | --- |
|  | **Period value** Measure a metric's period value to analyze performance during a specific time interval (like week, month, or year).    The KPI chart highlights the latest period value or global summary, and it can display a trend line that illustrates patterns and changes across sequential time periods.  Required element properties:   * [Value](#calculate-the-metric) * [Timeline](#define-the-reporting-period) |
|  | **Period comparison**   Measure a metric’s value in one period (like week, month, or year) against another to perform a sequential or period-over-period comparison.    The KPI chart highlights the latest period value or global summary, and it can display the comparison as a percentage, delta, or absolute value. It can also include a trend line that illustrates patterns and changes over time.  Required element properties:   * [Value](#calculate-the-metric) * [Timeline](#define-the-reporting-period) * [Comparison](#select-a-comparison-period)   (Period) |
|  | **Benchmark period comparison**   Compare a metric's period value against a benchmark or target to assess relative performance and gain insight into patterns, relationships, and correlations.    The KPI chart highlights the latest period value or global summary, and it can display a comparison as a percentage, delta, or absolute value. It can also include a trend line for both values to illustrate patterns and changes over time.  Required element properties:   * [Value](#calculate-the-metric) * [Timeline](#define-the-reporting-period) * [Comparison](#select-a-comparison-period)   (Column) |

> 🚀
>
> ### When loading or refreshing a workbook, Sigma typically sends a separate query for each data element. If the workbook contains multiple static KPI charts ([summary value](#summary-value) and [benchmark summary comparison](#benchmark-summary-comparison) variations) that share a data source, Sigma employs query batching. This consolidates the data requests from all applicable KPI charts into a single query to reduce query processing overhead and optimize performance. Time series KPI charts ([period value](#period-value), [period comparison](#period-comparison), and [benchmark period comparison](#benchmark-period-comparison) variations) send separate queries to the database and aren't included in query batching.

## Basic KPI chart configurations

Build a basic KPI chart by configuring the following element properties:

|  |  |
| --- | --- |
| **Chart** | Chart type displayed in the workbook |
| **Value** | Calculation that determines the metric value |
| **Timeline** | Date data that defines the reporting period |
| **Comparison** | Period or calculation that defines the comparison value |

> 🚩
>
> ### At the core of every chart element is its underlying data, which supplies the information the chart visualizes. As you build a KPI chart, Sigma automatically calculates and structures your data to associate element properties with columns ("source columns") in the underlying data table.
>
> When you configure a property by aggregating an existing column, adding a custom formula or value, or applying the row count, Sigma creates a new source column.
>
> For information about how to view the underlying data while you configure the chart, see [Maximize or minimize a data element](/docs/maximize-or-minimize-a-data-element).

### Add a KPI chart element

Add a chart element and designate it as a KPI chart.

> 💡
>
> ### You can also create a new KPI chart directly from a summary value in a table element. Right-click the table summary to open the menu, then select **Create KPI element**.

1. Open a workbook in **Explore** or **Edit** mode and [add a new chart element](/docs/create-a-data-element).
2. In the **Chart** property, click the dropdown field and select **KPI** from the list.

   ![Element properties sidebar open showing the visualization dropdown with KPI selected.](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+KPI+Chart/kpi_visualization-type.png)

### Calculate the metric

Configure the **Value** property to calculate the metric. This configuration is required to build any [KPI chart variation](#kpi-chart-variations).

1. In the **Value** property, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add calculation**, then use one of the following methods to calculate the metric:

   * To aggregate the values of an existing column, search or scroll the **Aggregate column** list and select the preferred column.
   * To add a custom calculation or value, select **Add new column**, then enter the calculation or value in the formula bar.
   * To count the number of rows in the underlying dataset, select **Row count**.
   > 💡
   >
   > ### You can also aggregate the values of an existing column by dragging and dropping a column name from the **Columns** list to the **Value** property.

   ![Add column menu open, showing a list of available aggregate columns and other options described.](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+KPI+Chart/kpi_define-metric-value_step-1a.png)

   When the [**Timeline** property](#define-the-reporting-period) is not configured, the chart displays the metric's global summary value, which aggregates all data points in the resulting **Value** property source column. If you deselect the **Aggregate values** checkbox, one value from the column is selected and displayed instead of a global summary. For information about the value displayed after configuring the **Timeline** property, see [Define the reporting period](#define-the-reporting-period) in this document.

   ![KPI showing the global summary of a sum of profit column with no timeline configured. The aggregate values checkbox is checked, and the column uses the Sum([Profit]) formula.](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+KPI+Chart/kpi_define-metric-value_step-1b.png)

   When you add a metric, the values are automatically aggregated and the **Aggregate values** checkbox is selected.
2. [optional] If you want to control how the metric is measured and formatted, leave the **Aggregate values** checkbox selected and adjust the aggregate, data type, or format of the metric value using the column menu or formula toolbar:

   1. In the **Value** property, hover over the column name, then click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu.
   2. Hover over any of the following items and select the preferred option:

      |  |  |
      | --- | --- |
      | **Set aggregate** | Measure the metric based on the selected aggregation method. |
      | **Transform** | Convert the column to the selected data value type. |
      | **Format** | Display the metric value in the selected format. |

   For example, you can format a sum of profit KPI to display using SI units:
   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+KPI+Chart/kpi_define-metric-value_step-2a.png)

   ![Sum of profit KPI with the SI formatting applied, showing as $71.4M](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+KPI+Chart/kpi_define-metric-value_step-2b.png)

### Define the reporting period

Configure the **Timeline** property to define the reporting period for the time series. This configuration is required to build a [period value](#period-value), [period comparison](#period-comparison), or [benchmark period comparison](#benchmark-period-comparison) KPI chart.

1. In the **Timeline** property, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add column**, then use one of the following methods to define the reporting period:

   * To derive the period from an existing date column, search or scroll the **Select column** list and select the preferred column.
   * To create a period based on a new date column, select **Add new column**, then enter a date function or value in the formula bar.
   > 📘
   >
   > ### The **Timeline** property supports date columns only. You cannot select or create a column that does not contain date data.

   ![Timeline menu open, with the Date column hovered over. Only the Date column is available to select. Non-date columns like Revenue or Profit are shown but grayed out and unavailable to select.](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+KPI+Chart/kpi_define-measurable-period_step-1a.png)

   When a source column is added to the **Timeline** property, two changes occur in the chart:

   * The chart now displays the metric's latest period value, which aggregates the **Value** property source column data for the most recent period. To change the default display value to the global summary, proceed to the next step.
   * If the element layout size allows, the chart displays a trend line, which you can hover over to view previous period values. For information about how to hide the trend line, see [Customize the trend line](#customize-the-trend-line) in this document.

   ![Sum of profit KPI shown with a line chart trend line and the month 2022-12 shown below the KPI value to indicate the date range for the latest period displayed on the chart.](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+KPI+Chart/kpi_define-measurable-period_step-1b.png)
2. [optional] Change the default display type (the value displayed when not interacting with the trend line):

   1. In the **Value** property, hover over the source column name, then click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu.
   2. Hover over **Default display type** and select an option:

      |  |  |
      | --- | --- |
      | **Latest period** | Display the aggregate value for the most recent period in the time series. |
      | **Global summary** | Display the aggregate value for all periods in the time series. |

   ![Column menu for the KPI metric with a timeline configured, open to show the Default display type options described in the text.](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+KPI+Chart/kpi_define-period_change-default-display-type.png)
3. [optional] Control how the period is measured and formatted:

   1. In the **Timeline** property, hover over the column name, then click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu.
   2. Hover over any of the following items and select the preferred option:

      |  |  |
      | --- | --- |
      | **Truncate date** | Measure the metric value based on the selected period. |
      | **Format** | Display the period date in the selected format. |

   ![Column menu for the timeline column open showing the options to truncate date or format. Format submenu is open and showing options like Automatic, Date, ISO date, Long date, Month year, and others.](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+KPI+Chart/kpi_define-measurable-period_step-2.png)

### Select a comparison period

Configure the **Comparison** > **Period** property to measure a sequential or period-over-period comparison for the metric. This configuration is required to build a [period comparison](#period-comparison) KPI chart.

When the benchmark or target value is `null` (for example, the first week in a sequential week-over-week analysis), the comparison value and label are hidden.

1. In the **Comparison** property, enable the **Period** option. If a source column is configured in the **Timeline** property, the option is automatically enabled.
2. Open the dropdown and select a type of period comparison.

> 📘
>
> ### Configuring a column in the **Timeline** property automatically engages the **Comparison** property. To build a KPI chart that highlights the period value of a metric without displaying a comparison, ensure the dropdown is set to **None**.

![Element properties for the KPI chart open, with the comparison property open and the period dropdown open to show default options for a Month column: Previous month, this month last quarter, this month last year, or none.](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+KPI+Chart/kpi_define-comparison-period_step-2a.png)

By default, a comparison value displays as a percentage. To instead display a delta or absolute value, [customize the comparison](#customize-the-comparison-display) in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/element-format.svg) **Element format** panel.

![KPI chart shown with a percentage comparison](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+KPI+Chart/kpi_define-comparison-period_step-2b.png)

### Select a comparison value

Configure the **Comparison** > **Column** property to measure the metric against a benchmark or target value. This configuration is required to build a [benchmark summary comparison](#benchmark-summary-comparison) or [benchmark period comparison](#benchmark-period-comparison) KPI chart.

1. In the **Comparison** property, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add calculation**, then use one of the following methods to calculate the benchmark or target value:

   * To aggregate values in an existing column, search or scroll the **Aggregate column** list and select the preferred column.
   * To add a custom calculation or value, select **Add new column**, then enter the calculation or value in the formula bar.
   * To count the number of rows in the underlying dataset, select **Row count**.

   ![Select column menu open for the Comparison option on the Element properties sidebar for the KPI chart, showing options as described.](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+KPI+Chart/kpi_define-comparison-value_step-2a.png)

   By default, a comparison value displays as a percentage. To instead display a delta or absolute value, [customize the comparison](#customize-the-comparison-display) in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/element-format.svg) **Element format** panel.

   ![KPI chart with a comparison value of the Sum of Revenue column set up as the comparator, rather than a period, and the comparison showing as a percentage.](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+KPI+Chart/kpi_define-comparison-value_step-2b.png)
2. [optional] Control how the benchmark or goal is measured and formatted:

   1. In the **Comparison** property, hover over the column name, then click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu.
   2. Hover over any of the following items and select the preferred option:

      |  |  |
      | --- | --- |
      | **Set aggregate** | Measure the metric based on the selected aggregation method. |
      | **Transform** | Convert the column to the selected data value type. |

   ![Column details menu open for the comparison value column, with the middle of the menu cropped to highlight the end of the menu options of Set aggregate and transform. Set aggregate submenu is open to show other options like Avg or Median, besides the default Sum aggregate.](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+KPI+Chart/kpi_define-comparison-value_step-3.png)

## Advanced KPI chart properties and formatting

Sigma features various properties and format options that give you the flexibility to build detailed KPI charts.

The following sections introduce configurations that can enhance your charts and help you deliver specific insights with meaningful and actionable information.

### Change the value color

Change the metric value’s font color in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/wb-element_viz.svg) **Element properties** > **Marks** > **Color** tab. This determines the default color of the metric value, which can be overridden by [conditional formatting](#add-conditional-formatting) rules.

> 📘
>
> ### The **Color** property (including conditional formatting) applies to the metric value only and doesn’t affect the element title or comparison font.

|  |  |
| --- | --- |
|  |  |

### Add conditional formatting

Configure formatting rules rules (click **+ Add rule**) in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/wb-element_viz.svg) **Element properties** > **Marks** > **Color** tab to change the metric value’s font color according to value-based conditions. This allows you to highlight or emphasize the value when it meets the specified conditions.

|  |  |
| --- | --- |
|  |  |

### Customize the value font

Customize the metric value’s font weight, color, and size in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/element-format.svg) **Element format** > **Value** section.

> 📘
>
> ### The **Value** format settings apply to the metric value only and don’t affect the element title or comparison font. If you change the font color in this section, the font color is also changed in the element’s **Color** property.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+KPI+Chart/kpi_format_value.png)

### Customize the comparison display

Customize the comparison display in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/element-format.svg) **Element format** > **Comparison** section.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+KPI+Chart/kpi_format_comparison.png)

In addition to modifying the color indicators, you can change the font size of the comparison value, show or hide the label, and customize the label content.

You can also select the type of comparison displayed and identify the favorable direction of the comparison. The **Direction** setting determines when the **Good color**, **Neutral color**, and **Bad color** indicators apply to the comparison value.

| Display |  |  |
| --- | --- | --- |
| **% difference from** | Display the percent of increase or decrease relative to the comparison value. |  |
| **Difference from** | Display the numerical increase or decrease relative to the comparison value. |  |
| **% of** | Display the percent of the comparison value. |  |
| **Absolute** | Display the absolute value of the comparison period or column. |  |

| Direction |  |  |
| --- | --- | --- |
| **Higher is better** | Apply the **Good color** selection to increased comparative values and the **Bad color** selection to decreased comparative values. |  |
| **Lower is better** | Apply the **Good color** selection to decreased comparative values and the **Bad color** selection to increased comparative values. |  |
| **None** | Apply no color indicator to the comparative value. |  |

### Customize the trend line

Customize the trend line in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/element-format.svg) **Element format** > **Trend** section.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+KPI+Chart/kpi_format_trend.png)

In addition to showing and hiding the trend line, you can select the trend line shape (line or area) and customize its colors.

| Shape |  |
| --- | --- |
| Line | Area |
|  |  |

You can also enable tooltips on hover, display the x-axis with timeline tick marks and labels, and display the y-axis with grid lines and labels.

| Display options |  |  |
| --- | --- | --- |
| Show tooltip | Show timeline axis | Show y-axis |
|  |  |  |

### Customize the chart layout

Customize the chart layout in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/element-format.svg) **Element format** > **Layout** section.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+KPI+Chart/kpi_format_layout.png)

Change the alignment of the text components, and select the location of the title and comparison value.

| Alignment |  |  |
| --- | --- | --- |
| Left | Center | Right |
|  |  |  |

| Title |  |
| --- | --- |
| Top | Bottom |
|  |  |

| Comparison value |  |
| --- | --- |
| Right | Below |
|  |  |

## All KPI chart format options

* [Background](/docs/customize-element-background)
* [Title](/docs/customize-element-title)
* [Value](#customize-the-value-font)
* [Comparison](#customize-the-comparison-display)
* [Trend](#customize-the-trend-line)
* [Reference marks](/docs/visualization-reference-marks)
* [Layout](#customize-the-chart-layout)

Updated 3 days ago

---

Related resources

* [Intro to charts](/docs/intro-to-visualizations)
* [Create a data element](/docs/create-a-data-element)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [KPI chart variations](#kpi-chart-variations)
  + - [Static variations](#static-variations)
    - [Time series variations](#time-series-variations)
  + [Basic KPI chart configurations](#basic-kpi-chart-configurations)
  + - [Add a KPI chart element](#add-a-kpi-chart-element)
    - [Calculate the metric](#calculate-the-metric)
    - [Define the reporting period](#define-the-reporting-period)
    - [Select a comparison period](#select-a-comparison-period)
    - [Select a comparison value](#select-a-comparison-value)
  + [Advanced KPI chart properties and formatting](#advanced-kpi-chart-properties-and-formatting)
  + - [Change the value color](#change-the-value-color)
    - [Add conditional formatting](#add-conditional-formatting)
    - [Customize the value font](#customize-the-value-font)
    - [Customize the comparison display](#customize-the-comparison-display)
    - [Customize the trend line](#customize-the-trend-line)
    - [Customize the chart layout](#customize-the-chart-layout)
  + [All KPI chart format options](#all-kpi-chart-format-options)