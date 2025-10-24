# Dataset Worksheet Columns

# Dataset Worksheet Columns

Columns are central to working in Sigma. When you create a dataset worksheet, you can structure and format your existing columns, create column calculations, and sort and filter your data.

## View columns in dataset worksheets

When working in the dataset’s worksheet, it will look like the screenshot below. This view provides you two ways to immediately start working with your columns: the worksheet spreadsheet and the column view panel.  When changes are made from one of these two components, your column(s) will automatically update in the other.

![dataset-worksheet.png](https://files.readme.io/3b0459e-dataset-worksheet.png)

### The spreadsheet interface

The worksheet spreadsheet interface is centrally located to provide an interactive spreadsheet-like interface. All column actions can be initiated from this table using the column menu.  
![24-worksheet-column-menu.gif](https://files.readme.io/0c2de26-24-worksheet-column-menu.gif)

### The column view panel

The column view panel can be found on the right side of your worksheet. It shows a high level editable view of your worksheet’s columns. Use this panel to search for columns and group data into levels. Like the spreadsheet, each column also has a [column menu](/docs/dataset-worksheet-columns#column-details).  
![25-worksheet-column-view-panel.gif](https://files.readme.io/9d41545-25-worksheet-column-view-panel.gif)

### Column details

Column details are available for all worksheet column types, except Json. To see details and statistics about an individual column, open the column menu and select **Column Details...**.

Contents of the modal vary depending on [column type](/docs/data-types-and-formats); however the overarching structure remains consistent.  
![26-column-details.png](https://files.readme.io/3a0aedc-26-column-details.png)

#### About

This section lists column type, name, and formula (fx).

#### Values

This section displays visual representations of the columns data. The Top Values list contains the column’s most common values. This information is available for Text, Number, and Date columns.  A Value Distribution histogram is also available for Number and Date columns.

#### Summary

This section lists key column totals: Values, Nulls, Row Count and Distinct Values. The percent column delineates the percentage of count out of total rows in the column.

* Values - The total number of non-null values (see [Count](/docs/count))
* Nulls - The total number of null values (see [CountIf](/docs/countif) and [IsNull](/docs/isnull))
* Row Count - The total number of rows in the column, regardless of value
* Distinct Values - The total number of unique values (see [CountDistinct](/docs/countdistinct))

#### Statistics

This section lists a variety of column statistics. Minimum and Maximum values are displayed for Date and Text columns. These and all other stats listed below are available for Number columns.

* Minimum - The column’s minimum value. Depending on column type, this will be the lowest number, the oldest date, or the first Text value when sorted alphabetically (see [Min](/docs/min))
* 25th Percentile - The number of values in the bottom 25th percentile of the columns values (see [PercentileCont](/docs/percentilecont))
* Median - The midpoint in a sorted list of column values. (see [Median](/docs/median))
* 75th Percentile - The number of values in the bottom 75th percentile of the columns values (see [PercentileCont](/docs/percentilecont))
* Maximum - The column’s maximum value. Depending on column type, this will be the highest number, the newest date, or the last Text value when sorted alphabetically (see [Max](/docs/max))
* Average - The average of all column values (see [Avg](/docs/avg))
* Standard Deviation - The column’s computed standard deviation (see [StdDev](/docs/stddev))
* Variance - The column’s statistical variance (see [Variance](/docs/variance))

## Work with existing columns

Column Menus

Column menus allow you to directly manipulate your worksheet's data. A few common column actions are sorting, formatting, hiding, deleting, filtering, and aggregating data.

A column’s menu can be found next to the column’s name in the worksheet spreadsheet and in the column view panel. To open the menu, hover over the column name and click the dropdown arrow that appears.

### Formatting columns

1. Open the column menu on the column you would like to format.
2. In the dropdown, hover over **Format**.
3. Select a format from the submenu.

***Note***: Format options are dependent on the column’s value type.

### Sorting columns

Individual columns can be sorted both ascending and descending directly from the column’s menu. Open the worksheet sort modal from any column’s column menu to define multi-column sorting.

### Moving columns

Individual columns can be moved using drag and drop. This is possible in both the spreadsheet interface and the column view panel.  
![27-move-worksheet-columns.gif](https://files.readme.io/91268fd-27-move-worksheet-columns.gif)

### Renaming columns

To rename a column, double-click on the column’s name or select **Rename Column** from the column menu.

Changing the name of a column in Sigma does not change its name in the database.

### Adding column descriptions

To add or edit a description to a column from the column menu:

1. Open the column’s menu.
2. Click **Add Description**.
3. Enter a description in the text input box.
4. Click **Save**.

To add or edit a description from the worksheet toolbar:

1. **Select** the column.
2. Click the **description icon** in the worksheet toolbar.  
   ![28-column-description.png](https://files.readme.io/ac38dfe-28-column-description.png)
3. Enter a description in the text input box.
4. Click **Save**.

### Viewing column descriptions

Columns with descriptions can be identified by a yellow marker in the top left corner of the column header. Hover over the column header to view the description.  
![29-view-column-description.png](https://files.readme.io/03cce34-29-view-column-description.png)

### Hide or unhide columns

Columns can be hidden using the 'Hide Column' action in the column menu. Hidden columns are not visible in the spreadsheet. However, they are still visible and actionable from the column view panel. In the column view panel, hidden columns display "grayed-out" compared to their visible neighbors (see 'Billing Country' in the screenshot below).  
![30-worksheet-column-menu.png](https://files.readme.io/3c13e66-30-worksheet-column-menu.png)

To unhide a hidden column, select the **Unhide Column** action from the column's menu.

You may also choose to use the **Hide Other Columns** action. This will show the selected column(s) and hide all other columns in the worksheet.

Hidden columns are only hidden from the spreadsheet. They can still be used elsewhere in the worksheet, such as in visualizations, filters, and calculated columns.

### Delete columns

Columns can be deleted using the 'Delete Column' action in the column menu.

Deleting a column will remove any related filters, effect any referencing [visualizations](/docs/intro-to-visualizations)[,](/docs/intro-to-visualizations) and break any referencing calculated columns.

As is the case with all worksheet column actions, deleting a column will not effect the data in the underlying data source.

### Multi-column selection

Multiple columns can be selected from both the spreadsheet and the column view panel. To select a range of columns, hold down the shift key when clicking the second endpoint in the range. To select and deselect multiple columns individually, hold down ⌘ as you click each column.

To perform actions on your selected columns, open the column menu on any selected column. Not all column actions can be applied multi-selected columns.  
![](https://files.readme.io/50d6726-31_-_column-multi-select.gif)

## Creating and calculating columns

Adding a New Column

To inject a new column into the middle of the table, select **Add New Column** from the menu belonging to the column located directly before where you would like to place your new column.

To add a new column at the end of the table or as the last column in a grouping level, click on the associated **Add New Column** button in the column view panel.  
![32-add-new-column.png](https://files.readme.io/d3ca22a-32-add-new-column.png)

### Use the formula bar

The formula bar is central to calculating data in worksheets. It is located near the top of the worksheet, above the spreadsheet and below the toolbar.

The formula in the formula bar always belongs to the column selected in the worksheet. No formula will be displayed if no columns or multiple columns are selected.

To calculate a new formula, first add a new column. Then type in your formula into the formula bar. As you type, it will suggest auto-completed function names and column names. After you complete your formula  click Enter or click the green check to the right of the formula bar.  
![33-formula-bar.png](https://files.readme.io/a349a8e-33-formula-bar.png)

[Visit Sigma's function index.](/docs/functions)

## Working with level groupings

Group your data:

1. On the right hand side of the screen, find the name of the column that you would like to Group By. Drag the column up to the box that says **Select Grouping Key**.  
   ![](https://files.readme.io/954af5e-36_-_create-grouping.gif)
2. Using the column menu, accessed by clicking the arrow on the right hand side of the column names at the top or side of the worksheet, you can easily create an aggregate column. When you create an aggregate column, it automatically nests under the next level Group.  
   If you Group by Holiday, and then create an aggregate column that sums your sales data, the new column will display the total sales per Holiday.
3. You can create additional groups as well. Locate the name of the column you want to group by in the list of column names on the right hand side of your screen. Click and drag the column name up above the Base Columns list, and an option to add a new level will appear. The worksheet will now show you two levels of data groupings. You can create aggregate columns of data under all of the group levels.

### Collapsing levels

Collapsing levels helps you see only the data you need. You can collapse and expand levels by clicking the double arrows at the left of the Base Columns label.   
![](https://files.readme.io/e6f8c78-35_-_collapse-grouping.gif)

## Extract semi-structured data

When Sigma detects JSON or Variant column types, ‘Extract Columns’ becomes and option in the column menu. If your data is semi-structured and you don’t see the ‘Extract Columns’ option, you can use the type function [JSON](/docs/json) or [Variant](/docs/variant) to change how Sigma interprets the column of data.

![](https://files.readme.io/2f108c1-39_-_json-data.png)
![](https://files.readme.io/2f67593-40_-_json-field-extract-modal.png)

Updated 3 days ago

---

[Dataset worksheet controls](/docs/dataset-worksheet-controls)[Dataset Totals](/docs/dataset-totals)

* [Table of Contents](#)
* + [View columns in dataset worksheets](#view-columns-in-dataset-worksheets)
  + - [The spreadsheet interface](#the-spreadsheet-interface)
    - [The column view panel](#the-column-view-panel)
    - [Column details](#column-details)
  + [Work with existing columns](#work-with-existing-columns)
  + - [Formatting columns](#formatting-columns)
    - [Sorting columns](#sorting-columns)
    - [Moving columns](#moving-columns)
    - [Renaming columns](#renaming-columns)
    - [Adding column descriptions](#adding-column-descriptions)
    - [Viewing column descriptions](#viewing-column-descriptions)
    - [Hide or unhide columns](#hide-or-unhide-columns)
    - [Delete columns](#delete-columns)
    - [Multi-column selection](#multi-column-selection)
  + [Creating and calculating columns](#creating-and-calculating-columns)
  + - [Use the formula bar](#use-the-formula-bar)
  + [Working with level groupings](#working-with-level-groupings)
  + - [Collapsing levels](#collapsing-levels)
  + [Extract semi-structured data](#extract-semi-structured-data)