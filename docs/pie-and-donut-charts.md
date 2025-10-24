# Pie and donut charts

# Pie and donut charts

Pie and donut charts are a good way to visualize data as a percentage of a total.

## Requirements

* To create a data element, you must have **Can Edit** [access](/docs/folder-and-document-permissions) to the individual workbook and be in Edit mode.
* Many exploratory actions are also supported in Explore mode; see [Workbook modes](/docs/workbook-modes-overview-view-explore-edit).

## Plot options

You can create pie and donut charts charts from the [**PAGE ELEMENTS** section](/docs/create-a-data-element) of your workbook's editor panel, or directly from [an existing data element](/docs/create-a-data-element).

![Image of a pie chart](https://files.readme.io/3df3bf42aca2297abd8b0f006d7e1fca738742c645fada211b9c6330bc18d0a5-piechartexmaple.png)

### Required fields

* **COLOR** (1 column)
* **VALUE** (1+ columns)
  Columns added to the **VALUE** field are aggregated by default. Aggregation type (e.g. Sum vs Count) is dependent on the original column’s value type (e.g. text, number, date, etc).
  **Example**: A numeric column [Sales Amount] will create a new calculated column [Sum of Sales Amount].

### Marks

* **TOOLTIP**: choose columns to show when hovering over points in the chart
* **TRELLIS**: select columns to serve as Trellis Rows or Columns, splitting the chart into separate charts

### Donut hole value

If you're creating a donut chart, you can optionally add a KPI to the hole of the donut.

1. Select the element.

   The editor panel opens to the **Element properties** section.
2. For **Donut hole value**, select the **+** to add a calculation.
3. Add a new column, select the row count, or choose a column to aggregate and display in the donut hole.

   The aggregate value appears with the column name as a default label. You can format the value using the format options.

![Screenshot of a donut chart open for editing with a Sum of Revenue column added to the donut hole, while the value for the donut chart is the sum of revenue split by store region, used for the color for the chart.](https://files.readme.io/28e40e4b9f692565e377f748bac844350a0c14a96d46d25c9f77728e500cf43f-donutholechartexample.png)

## Format options

To start editing the format options for a chart:

**Before you start:** This action uses the editor panel. If you have not done so already, open the editor panel from either Explore or Edit mode.

1. In the editor panel, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/element-format.svg) **Element format**.
2. Select a format option to view and edit its settings.

The following format categories are available for pie and donut charts:

* **BACKGROUND**
* **TITLE**
* **LEGEND**
* **DATA LABELS**
* **DONUT HOLE** (only for donut charts)

Updated 3 days ago

---

Related resources

* [Intro to charts](/docs/intro-to-visualizations)
* [Create a data element](/docs/create-a-data-element)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Plot options](#plot-options)
  + - [Required fields](#required-fields)
    - [Marks](#marks)
    - [Donut hole value](#donut-hole-value)
  + [Format options](#format-options)