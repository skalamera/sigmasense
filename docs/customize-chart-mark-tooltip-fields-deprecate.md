# Customize chart mark tooltip fields

# Customize chart mark tooltip fields

Chart mark tooltips appear when you hover over individual data points in a visualization. Sigma auto-selects default tooltip fields, but you can customize them to display the metrics and data attributes most relevant to your use case.

> 📘
>
> ### Tooltips are featured in all visualization types but are not customizable in gauge charts and Sankey diagrams.

![Screenshot showing line chart with tooltip appearing when mouse hovers over line](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Customize+chart+tooltips/customize-chart-tooltip-fields_intro.png)

This document explains how to manage default and custom tooltip fields.

## User requirements

The ability to customize chart mark tooltip fields requires the following:

* To use this feature, you must have **Can edit** or **Can explore** [access](/docs/folder-and-document-permissions) to the individual workbook.
* You must be customizing or editing the workbook.

## Show or hide default tooltip fields

By default, tooltips display fields corresponding to source columns configured in the chart properties. For example, the columns defining axes, values, stages, and mark colors. You can show or hide these fields as needed.

1. On the workbook page, select the chart element you want to modify.
2. In the editor panel, hover over the relevant column in the **X-axis** or **Y-axis** field, then click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu.
3. Select **Show in tooltip** to change the tooltip visibility.

   * If the menu item displays a checkmark (✓), the corresponding tooltip field is currently shown. Click to hide the tooltip field.
   * If the menu item displays no checkmark, the corresponding tooltip field is currently hidden. Click to show the tooltip field.

   The change to the tooltip takes effect immediately. Hover over individual data points in the chart to view your changes.

   > 💡
   >
   > ### When you apply stacking in bar charts, you can also customize tooltips in the editor panel's **Format** > **Tooltip** section to display the variable value as a percentage of the cumulative stack. See **Customize tooltip fields and values** in [Build a bar chart](/docs/build-a-bar-chart).

## Display additional tooltip fields

To enhance your chart tooltips with additional fields, add new or existing columns to the **Tooltip** property.

1. On the workbook page, select the chart element you want to modify.
2. In the editor panel, click **Tooltip**.
3. In the **Select column** field, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add calculation...** and configure a source column for the new tooltip field:

   * To reference or aggregate data from an existing column, search or scroll the **Select column** or **Aggregate column** list and select a column name. You can change or remove the aggregation if needed.
   * To create a new column based on a custom formula, select **Add new column**, then enter the formula or value in the toolbar.
   * To create a new column based on the number of aggregated rows, select **Row count**.

   The new tooltip field is displayed when you hover over individual data points in the chart.

## Remove custom tooltip fields

To remove fields added to tooltips, remove columns configured in the **Tooltip** property.

1. On the workbook page, select the chart element you want to modify.
2. In the editor panel, click **Tooltip**.
3. In the **Tooltip** property, hover over the column you want to remove, then click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu.
4. To delete the column, select **Delete column** or remove it from the **Tooltip** property by clicking and dragging it back to the **Add column** list.

   The change to the tooltip takes effect immediately. Hover over individual data points in the chart to view your changes.

Updated 3 days ago

---

Related resources

* [Customize element background](/docs/customize-element-background)
* [Customize element title](/docs/customize-element-title)
* [Format chart legend](/docs/format-chart-legend)
* [Create and format trellis charts](/docs/create-and-format-trellis-charts)
* [Display chart data labels](/docs/display-chart-data-labels)
* [Display chart reference marks](/docs/display-chart-reference-marks)
* [Add trend lines](/docs/add-trend-lines)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Show or hide default tooltip fields](#show-or-hide-default-tooltip-fields)
  + [Display additional tooltip fields](#display-additional-tooltip-fields)
  + [Remove custom tooltip fields](#remove-custom-tooltip-fields)