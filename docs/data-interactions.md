# Drill down into data

# Drill down into data

Sigma supports drilling down or up into data using drill paths, also called drill anywhere, for most [chart types](/docs/intro-to-visualizations). With a drill path, you can explore your data ad hoc, viewing different slices of the data to identify patterns or themes.

Only users with **Can edit** or **Can explore** access to the workbook can drill up or down into a chart. If you want users with **Can view** access to be able to drill up or down into data, or you found a particular drill path to be useful and you want to use it across multiple charts, create a [drill down control](/docs/drill-down-control) instead.

## Requirements

* To use [drill anywhere](#drill-anywhere-in-a-chart), you must have **Can edit** or **Can explore** [access](/docs/folder-and-document-permissions) to the workbook.
* To [customize the drill down column list](#customize-the-drill-down-column-list-for-a-chart) for a chart, you must have **Can edit** access.

## Drill anywhere in a chart

You can drill up or down in a chart to view different slices of the data. For example, if you view a bar chart that shows sales by year and want to explore how sales look split by store region instead, drill down in the chart.

1. Click a value on your chart to open the context menu, then click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/arrow-down-circle-outline.svg) (**Drill down**).

   ![Bar chart showing sales by year with the 2023 bar selected and the drill down option in the tooltip hovered over.](https://files.readme.io/7c30c7475404065360d207a1bc7c3c8f95792d7d4d225d7d039dea9f275752b2-dd-chart.png)
2. In the **Drill down** modal, select a column to drill into that data. For example, choose the *Store Region* column.

   ![Drill down modal showing a list of available columns, such as store region and product type.](https://files.readme.io/5ce2884fd3670e8c10cea7bc4d04580e16dbfbbf35adf70bc5bf5eed1c7769c1-dd-modal.png)

   The chart changes to show the new data slice. For example, when drilling into *Store Region* for the *Year* 2023, Sigma adds a date filter and changes the **X-axis** value from *Year* to *Store Region*. The resulting chart shows the sum of sales by region for the year 2023:

   ![Bar chart showing sales by store region filtered to the year 2023.](https://files.readme.io/7fbe776f1bc5a886e0434bbfe96b980237b297a1fed669cab7fcf52e26c4212c-dd-crop-output.png)

   If you [maximize the chart](/docs/view-underlying-data), you can see the structure of the underlying data table updates accordingly. Instead of being grouped by *Year*, the data is now grouped by *Store Region*:

   ![Bar chart showing sales by store region filtered to the year 2023, maximized to show the table groupings in the underlying data table.](https://files.readme.io/1d6ca26634683f90309f3a2b1c2f39f29c263788a6143cad7a2edb6f4c31e517-dd-maximized.png)
3. (Optional) After drilling down, you can select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/arrow-up-circle-outline.svg) **Drill up** to return to the original chart structure.

## Customize the drill down column list for a chart

To focus the available columns for drill anywhere to specific ones, for example, to limit the list of columns to only those that make sense with the **X-axis** of the current chart, edit the column list:

1. Open the workbook for editing.
2. Click a value on your chart to open the context menu, then click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/arrow-down-circle-outline.svg) (**Drill down**).
3. In the **Drill down** modal, click **Edit list**.

   ![Drill down modal with the edit list option hovered over, showing an underline to indicate that it can be clicked.](https://files.readme.io/d4a936c9ccae7ba15c3648ba97e54556eb94cb6f498819257ed3f3cb0ef19f50-dd-edit-list.png)
4. Use the checkboxes to select only the columns you want available. For example, deselect the checkbox for columns that might produce too many values to be viewed on the chart, or are otherwise not useful.

   ![Edited list of columns for the chart, with columns like Quantity deselected while columns like Product type remain selected.](https://files.readme.io/8b1f445bc878b80c261a612ee91c7f1c4b42a30bc9af19078711fddb47210cfe-dd-edited-list.png)
5. Click **Save** to return to the **Drill down** modal. The displayed options are limited to only the selected columns.

Updated 3 days ago

---

Related resources

* [Intro to visualizations](/docs/intro-to-visualizations)
* [Data Element Filters](/docs/data-element-filters)
* [Drill down control](/docs/drill-down-control)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Drill anywhere in a chart](#drill-anywhere-in-a-chart)
  + [Customize the drill down column list for a chart](#customize-the-drill-down-column-list-for-a-chart)