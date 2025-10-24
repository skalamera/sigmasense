# Working with pivot tables

# Working with pivot tables

With Sigma, you can create a pivot table to group and summarize your data in a particular way. Use a pivot table to present your data in two dimensions, automatically summarize your data based on groups, and view your data in various hierarchies.

You can group columns in a table to approximate some functionality in pivot tables, such as aggregating data for specific groups. See [Create and manage tables](/docs/create-and-manage-tables).

## Requirements

* To create or edit a data element, you must have **Can edit** access to the individual workbook.
* Some exploratory actions are also supported with **Can explore** access.

For more details, see [Folder and document permissions](/docs/folder-and-document-permissions).

## Create a pivot table

You can create a pivot table from an existing data element, or from the **Add element** bar by selecting **Data** > **Pivot table**. For more details, see [Create a data element](/docs/create-a-data-element).

A pivot table does not display data until you define the data source columns to use as pivot rows and/or pivot columns. Configure the following properties in the **Properties** tab of the editor panel:

* **Pivot rows**: Select one or more columns from your table to appear as rows in the pivot table. For example, to summarize total cost for product type, add the product type column as a Pivot row.

  ![](https://files.readme.io/6fd7287721b59c1407cc826eb2cb3c038ccc161b32f688f9624be2351f28e3d1-pivot-one-row.png)
* **Pivot columns**: Optional if you define one or more pivot rows. Select one or more columns to split the values in each row. For example, to summarize the total cost for each product type in each store region, add the store region column as a pivot column.

  ![Pivot table showing product type as the row and store region as the column](https://files.readme.io/9394cca08b38349c8d7e2fb4b5035b0ab740f5015a1ab704623c196d9e49bac2-pivot-row-column-foreal.png)
* **Values**: Select one or more columns to display the values for each pivot row and column. Columns added to **Values** are aggregated by default and the type of aggregation used depends on the data type of the original column. For example, add the cost column as a value, and leave the default aggregation of **Sum**, or adjust it by rounding. See [Change the aggregation of values](#change-the-aggregation-of-values).

  ![Pivot table with product type as a row, store region as columns, and sum of cost as the value.](https://files.readme.io/05af48a26bb503feba86d2186a46024c2446c4144f64f0a3cbf3202bfd27b18e-pivot-row-column-value.png)

## Pivot table formatting and customization options

You can customize the formatting and presentation of a pivot table in many ways. To show or hide totals in a pivot table, see [Pivot table totals and subtotals](/docs/pivot-table-subtotals).

**Before you start:** This task requires editing elements. You can edit an element by customizing or editing a workbook.

1. In the editor panel, select the **Format** tab.
2. Click a format category to view and edit its settings.

The following format categories are available for pivot tables:

* **Element Style**: See [Customize element background and styles](/docs/customize-element-background-and-styles).
* **Title**: See [Customize element title](/docs/customize-element-title).
* **Table style**: See [Format and customize a table](/docs/format-and-customize-a-table).
* **Totals**: See [Format pivot table totals](/docs/format-pivot-table-totals).
* **Format**: See [Specify empty cell display value](#empty-cell-display-value) and [Repeat row labels](#repeat-row-labels).

You can also format pivot table columns. See [Format pivot table columns](#format-pivot-table-columns).

### Empty cell display value

If you have empty values in a pivot table, you can specify a value to fill the empty cells.

1. Open a workbook for customizing or editing.
2. Select a pivot table element, then in the editor panel, select the **Format** tab.
3. Click **Format**.
4. For **Empty cell display value**, enter a value.

| Selected option | Example |
| --- | --- |
| Default |  |
| Empty cell display value |  |

### Repeat row labels

If you have multiple pivot rows defined, and you choose to display the pivot row groupings as separate columns, you can repeat the row labels:

1. Open a workbook for customizing or editing.
2. Select a pivot table element, then in the editor panel, select the **Format** tab.
3. Click **Format**.
4. For **Repeat row labels**, select the checkbox.

| Selected option | Example |
| --- | --- |
| Default |  |
| Repeat row labels |  |

## Format pivot table columns

The following column formatting options are available:

* **Alignment**
* **Font color**
* **Background color**
* [**Conditional formatting**](/docs/working-with-pivot-tables#apply-conditional-formatting)

### Apply basic visual column formatting

To change the alignment, font color, or background color of values in a column:

1. Select the column or cell that you want to format.
2. To set the background color, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/fill-color.svg) **Background color** in the formula bar.
3. To set the font color, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/text-color.svg) **Text color** in the formula bar.
4. To set the alignment of the data, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/text-align_left.svg) **Alignment** in the formula bar.

### Apply conditional formatting

You can apply conditional formatting to the columns, rows, and values in a pivot table. Use conditional formatting to show different background colors for different values, highlight discrepancies in data with a background or font scale, or display data bars to quickly visualize outlier values.

> 📘
>
> Conditional formatting takes precedence over [toolbar column formatting options](/docs/format-and-customize-a-table#format-column-data).

**Before you start:** This task requires editing elements. You can edit an element while customizing or editing a workbook.

1. Open a workbook for customizing or editing.
2. Select a pivot table element, then in the editor panel, select the **Format** tab.
3. Click **Conditional formatting**.
4. Click **+ Add rule**.
5. Customize the rule:

   * Choose a column to apply the formatting to
   * Choose whether to use a single color, color scale, or add data bars to cells
   * Select checkboxes to apply the formatting to values, subtotals, or grand totals.![Pivot table with background scale conditional formatting applied to sum of cost column, so all values for that column are highlighted with a blue default background scale. Grand total row and column are not formatting because the formatting is set to only apply to values.](https://files.readme.io/97ba76222412421ae945ba2abe556394ab67000e516d58d9838f3d14f743032b-pivot-condi-format.png)

## Change data presentation in a pivot table

While most complex data transformations for a pivot table should occur in the flattened source table, you can manipulate the presentation of data in a pivot table in several ways:

* [Change the aggregation of values](#change-the-aggregation-of-values)
* [Add a calculated column to a pivot table](#add-a-calculated-column-to-a-pivot-table)
* [Swap pivot columns and rows](#swap-pivot-columns-and-rows)
* [Display multiple pivot rows as separate columns](#display-multiple-pivot-rows-as-separate-columns)
* [Collapse grouped rows and columns](#collapse-grouped-rows-and-columns)
* [Define values hierarchy in a pivot table](#define-values-hierarchy-in-a-pivot-table)
* [Hide or show fixed pivot table headers (Beta)](#hide-or-show-fixed-pivot-table-headers-beta)

> 📘
>
> These tasks requires editing elements. You can edit an element while customizing or editing a workbook.

### Change the aggregation of values

When you add a data column to a pivot table’s **Values** field, the values are automatically [aggregated](/docs/aggregate-functions-overview) according to the data type. Numeric columns are aggregated by [Sum](/docs/sum), while text and date columns are aggregated by [Count](/docs/count).

To change a column's aggregation:

1. In the editor panel, hover over the column, and click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)).
   The column menu opens.
2. From the **Set aggregate** submenu, select a new aggregate. For example, choose one of Sum, Avg, Median, Percentile, Min, Max, First, Last, Count, CountDistinct, or more advanced calculations like percent of total.

### Add a calculated column to a pivot table

Add a calculated column to a pivot table to perform a calculation that repeats across the pivot, such as a percentage of total or a period-over-period analysis.

1. Select the pivot table element.
2. In the **Values** section, select **+** > **Add new column**.
   A new column titled **Calc** appears and the focus changes to the formula bar.
3. Enter a formula for the calculated column, then press Enter on your keyboard or select the checkmark to save. The column is automatically renamed after the formula.

   ![Formula for a calculated column using the PercentOfTotal formula on the Sum(Cost) source column.](https://files.readme.io/ab4cdda894a8c51f42486098735c1276156aa6cf1764279b4f996b296d471fd6-pivot-calc-column.png)

For guidance working with pivot table totals in calculated columns, see [Pivot table totals and subtotals](/docs/pivot-table-subtotals).

### Swap pivot columns and rows

You can change the layout of your pivot table and swap rows with columns:

1. Select the pivot table element.
2. In the editor panel, next to the **Pivot rows** header, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/swap-row-col.svg) **Swap rows with columns**.

   ![Pivot table with swap rows with columns option highlighted, with product type listed as pivot rows and store regions as pivot columns.](https://files.readme.io/3ca38ccd9f31250cf851bef8ca993d35e9996cf60658d888a86c43b4f02b760f-pivot-swap-rows-start.png)

   Pivot table rows are swapped with columns.

   ![Pivot table from earlier examples, with store regions listed as pivot rows and product type as pivot columns.](https://files.readme.io/3c68b2270e8141950bcb90c38156cc8f06022eb37687491ead106abee355b418-pivot-swap-rows-end.png)

### Display multiple pivot rows as separate columns

When you have multiple pivot rows, you can choose to display the data combined in one column, or as separate columns.

After adding a second data column as a pivot row, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/separate-columns.svg) **Display as separate columns**. To change the display back, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/single-column.svg) **Display as a single column**:

| Selected option | Example |
| --- | --- |
| Display as a single column |  |
| Display as separate columns |  |

### Collapse grouped rows and columns

If your pivot table has at least two data columns added as **Pivot rows** or **Pivot columns**, you can expand and collapse the rows and columns. To do so, click **+** or **-** next to the value of a pivot table row, column, or cell header.

![Gif showing a pivot table with multiple rows and columns being collapsed with the - option.](https://files.readme.io/5a0f74a72e4fb25f688b0a1d7225d582d4f5fc3fee2b017b81fd1949b4cc3323-pivot-expand-collapse-better.gif)

### Define values hierarchy in a pivot table

If you have multiple values in your pivot table, you can define the hierarchy and groupings of data columns, values, and rows to reflect the data summaries that you want to display.

To structure the hierarchy of values in your pivot table:

1. Select the pivot table element.
2. Add at least two columns as **Values**.

   A box labeled **Values** appears under **Pivot columns**:
   ![](https://files.readme.io/2d9a9ce-pivot-values-default.png)
3. To change the default hierarchy, drag and drop the **Values** box to another position under **Pivot columns** or to **Pivot rows**.
   ![](https://files.readme.io/721f69b56aa52c1ccee163560d5edca46f3ef5171f0715bde50b8f589fc62d36-pivot-values-move.gif)

The data presentation changes based on the location of the values:

| Values location | Example |
| --- | --- |
| Default, below pivot columns. |  |
| Above pivot columns. |  |
| Below pivot rows. |  |
| Above pivot rows. |  |

### Hide or show fixed pivot table headers (Beta)

> 🚩
>
> This documentation describes one or more public beta features that are in development. Beta features are subject to quick, iterative changes; therefore the current user experience in the Sigma service can differ from the information provided in this page.
>
> This page should not be considered official published documentation until Sigma removes this notice and the beta flag on the corresponding feature(s) in the Sigma service. For the full beta feature disclaimer, see [Beta features](/docs/sigma-product-releases#beta-features).

You can hide or show fixed row and column headers in pivot tables. This can be useful to create additional space within a table for summary statistics, or reduce the visual space a table occupies within a workbook.

To hide or show fixed pivot table headers:

1. Select your desired table. From the editor panel, select the **Format** tab.
2. Expand the **Table components** section.
3. Turn the **Show column headers toggle** and **Show row headers toggle** on or off to show/hide headers.

> 📘
>
> ### Hiding fixed column headers will also hide fixed value headers (the header in the upper left corner of your pivot table if you only have one **Values** column specified). If you have multiple **Values** columns, hiding column headers will not affect the appearance of value headers.

4. Select **Reset to default** to return to the default setting (show all row and column headers).

> 🚧
>
> ### Exporting workbooks with fixed pivot headers hidden is only supported for PDF and PNG exports. Changes to table formatting made with this feature will not be reflected in other export destinations.

## Maximize a pivot table to view the flattened table

When viewing, customizing, or editing a workbook, all [data elements](/docs/intro-to-data-elements) are minimized by default to display multiple elements in the canvas. You can maximize any data element to focus on its details and explore the underlying data.

Select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/maximize.svg) **Maximize element**, or press the space bar on your keyboard with an element selected, to view the underlying data.

When you maximize a pivot table, it expands to the full width of the workbook page and displays the underlying flattened data table. You can use this view to explore the grouping levels of the pivot table. Because the element and underlying data are inherently linked, changes applied to one are automatically reflected in the other.

> 📘
>
> ### You can only make changes to the underlying data of a data element while customizing or editing a document.

For more details, see [View underlying data](/docs/view-underlying-data).

Updated 3 days ago

---

Related resources

* [Workbooks overview](/docs/workbooks-overview)
* [Intro to data elements](/docs/intro-to-data-elements)
* [Create and manage tables](/docs/create-and-manage-tables)
* [Data Element Filters](/docs/data-element-filters)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Create a pivot table](#create-a-pivot-table)
  + [Pivot table formatting and customization options](#pivot-table-formatting-and-customization-options)
  + - [Empty cell display value](#empty-cell-display-value)
    - [Repeat row labels](#repeat-row-labels)
  + [Format pivot table columns](#format-pivot-table-columns)
  + - [Apply basic visual column formatting](#apply-basic-visual-column-formatting)
    - [Apply conditional formatting](#apply-conditional-formatting)
  + [Change data presentation in a pivot table](#change-data-presentation-in-a-pivot-table)
  + - [Change the aggregation of values](#change-the-aggregation-of-values)
    - [Add a calculated column to a pivot table](#add-a-calculated-column-to-a-pivot-table)
    - [Swap pivot columns and rows](#swap-pivot-columns-and-rows)
    - [Display multiple pivot rows as separate columns](#display-multiple-pivot-rows-as-separate-columns)
    - [Collapse grouped rows and columns](#collapse-grouped-rows-and-columns)
    - [Define values hierarchy in a pivot table](#define-values-hierarchy-in-a-pivot-table)
    - [Hide or show fixed pivot table headers (Beta)](#hide-or-show-fixed-pivot-table-headers-beta)
  + [Maximize a pivot table to view the flattened table](#maximize-a-pivot-table-to-view-the-flattened-table)