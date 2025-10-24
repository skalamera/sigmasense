# Create and edit period-over-period analysis

# Create and edit period-over-period analysis

Sigma’s guided workflow for building period-over-period analyses provides a quick and convenient way to evaluate performance over time. Generate dynamic period comparisons without entering complex custom formulas, then easily visualize the results to identify trends, patterns, and anomalies.

For example, you might compare sales revenue from one quarter to previous quarters, or review website traffic month-over-month, or other date period comparisons.

This document explains how to use the built-in period-over-period features in data elements (tables, pivot tables, and visualizations).

## User requirements

The ability to use Sigma’s built-in period-over-period features requires the following:

* You must be assigned an [account type](/docs/user-account-types) with the **Edit Workbook** and/or **Explore Workbook** permission enabled.
* You must be the workbook owner or be granted **Can explore** or **Can edit** [workbook permission](/docs/folder-and-document-permissions).

## Key terms

The following terminology is used throughout this document:

Current period
:   The reference period used as the starting point for the comparison.

Comparison period
:   The lookback period used as the end point for the comparison.

Period value
:   The metric value for the current period.

Comparison value
:   The metric value for the comparison period, or the value used to compare the current and comparison periods (depending on the comparison value type).

Comparison value type
:   The type of comparison generated (difference, % difference, or value).

## Build a period-over-period comparison

Jump-start your period-over-period analysis with Sigma’s guided workflow. Your input generates a comparison grouping that can be augmented, edited, and visualized as needed.

1. Open a workbook in **Explore** or **Edit** mode and select the data element you want to update. If working with a visualization, [maximize the element](/docs/maximize-or-minimize-a-data-element) to view and edit the underlying data table.
2. In the table, click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) in an existing column header to open the column menu.
3. Hover over **Add column via**, then select **Period over period comparison**.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Create+and+edit+period-over-period+analysis/pop_add-column-via-period-over-period-comparison.png)
4. In the **Add comparison** modal, configure the comparison, then click **Done**.

   * **Compare field**: Select a column containing the metric or variable you want to compare.
   * **Aggregate**: Select an aggregation method to calculate the period and comparison values.
   * **Using date column**: Select a [date column](/docs/data-types-and-formats) to aggregate for the current and comparison periods.
   * **Comparison time frame**: Select the comparison period to determine the lookback and date granularity.
   * **Output**: Select one or more comparison value types.

     Difference
     :   Period-over-period difference as a raw number.

     % difference
     :   Period-over-period difference as a percent.

     Value
     :   Total metric value for the comparison period as a raw number.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Create+and+edit+period-over-period+analysis/pop_add-comparison.png)

   In table elements, Sigma creates a period-over-period grouping with columns containing the current period, period value, and comparison value (demonstrated in the following screenshot).

   In pivot tables and visualizations, Sigma creates underlying data columns containing the truncated date (based on the selected comparison period) and comparison value. You can then use the new columns to configure the element properties.

   > 📘
   >
   > ### Regardless of data element type, when you select multiple comparison value types in the **Output** field, Sigma generates a separate column for each.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Create+and+edit+period-over-period+analysis/pop_add-comparison_results.png)

   > 💡
   >
   > ### Visualize your period-over-period comparison with a KPI chart. For more information, see [Build a KPI chart](/docs/build-a-kpi-chart).

## Add a comparison value

Add a comparison value to an existing period-over-period grouping.

1. In the table, locate the column containing the period value you want to compare, then click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) in the column header to open the column menu.
2. Hover over **Add column via**, then select an option in the **Comparison time frame** section.

   > 📘
   >
   > ### Available options depend on the date granularity of the existing comparison. For example, if the period value is aggregated by month, it can only be compared to other monthly periods. In this case, the **Comparison time frame** options include **Last month**, **Same month last quarter**, and **Same month last year**. Other comparisons like **Last year** or **Same week** last quarter aren’t available because they don’t provide proportionate period comparisons.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Create+and+edit+period-over-period+analysis/pop_add-column-via-comparison-time-frame.png)

   Sigma adds a new comparison value column to the same grouping.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Create+and+edit+period-over-period+analysis/pop_add-column-via-comparison-time-frame_results.png)

## Edit an existing comparison

Quickly change an existing comparison’s period, value type, and aggregation method.

> 💡
>
> ### Sigma calculates comparison values using the **[DateLookback](/docs/datelookback)** function. To make changes beyond comparison period, comparison value type, and aggregation method, edit the column’s Sigma-generated formula.

1. In the table, locate the column containing the comparison value you want to modify, then click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) in the column header to open the column menu.
2. Edit the comparison period, comparison value type, or aggregation method:

   * To change the comparison period or comparison value type, hover over **Edit comparison**, then select a different **Comparison time frame** or **Output** option.

     ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Create+and+edit+period-over-period+analysis/pop_edit-comparison.png)

     ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Create+and+edit+period-over-period+analysis/pop_edit-comparison_results.png)
   * To change the aggregation method, hover over **Set aggregate** and select a different option.

     ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Create+and+edit+period-over-period+analysis/pop_set-aggregate.png)

     ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Create+and+edit+period-over-period+analysis/pop_set-aggregate_results.png)

Updated 3 days ago

---

Related resources

* [DateLookback](/docs/datelookback)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Key terms](#key-terms)
  + [Build a period-over-period comparison](#build-a-period-over-period-comparison)
  + [Add a comparison value](#add-a-comparison-value)
  + [Edit an existing comparison](#edit-an-existing-comparison)