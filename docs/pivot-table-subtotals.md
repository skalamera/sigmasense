# Pivot table totals and subtotals

# Pivot table totals and subtotals

Grouped tables and pivot tables calculate totals and subtotals. If your pivot table contains aggregated values, such as the sum or count of a value, totals are shown by default.

You can hide, manage, customize, and perform additional calculations with totals and subtotals in a grouped table or pivot table.

* To hide totals, see [Show and hide totals in a pivot table](#show-and-hide-totals-in-a-pivot-table) or [Show totals in a grouped table](/docs/create-and-manage-tables#show-totals-in-a-grouped-table)
* To customize the formula used to calculate totals, see [Customize totals and subtotals](#customize-totals-and-subtotals)
* To format totals, such as by highlighting totals or changing the font color, see [Format pivot table totals](/docs/format-pivot-table-totals).

For more details about tables, see [Create and manage tables](/docs/create-and-manage-tables).
For more details about pivot tables, see [Working with pivot tables](/docs/working-with-pivot-tables).

## Definitions and key concepts

Grand totals are calculated if a pivot table contains values, or a grouping in a table contains calculations. Subtotals are calculated if a pivot table contains values and has more than one column added as a pivot row or pivot column, or a table contains multiple groupings with calculations.

By default, totals are calculated using the same formula as the corresponding value in a pivot table or table grouping, but applied to a higher-level grouping of the data. If you want to change the formula used to calculate totals, see [Customize totals and subtotals](#customize-totals-and-subtotals).

Grand total calculations are performed against the entire table or pivot table, and subtotal calculations are performed against each grouping of the data:

* **Grand total**: The aggregated calculation of **all** values for a pivot row, pivot column, or grouping calculations. In the example screenshot, grand totals are highlighted in pink.
* **Subtotal**: The aggregated calculation of values in **a group** of pivot rows, pivot columns, or a given table grouping. In the example screenshot, subtotals are highlighted in yellow.

![Pivot table showing the sales quantities for store regions and states, with columns for each quarter. The row for the East region displays totals for each quarter and a total for all quarters in a totals column. This row contains the parent row totals because the region is higher in the hierarchy than states (a parent). Each state shows a row total in the totals column, which is a grand total for each row. At the bottom of the pivot table there is a Grand totals row that shows the subtotals for each quarter.](https://files.readme.io/72f217fd346ae1aed207284f3bad55f71659a063d3cdf91bee6f4851bd8c69eb-pivot-totals-all.png)

In a grouped table, only the grand totals for each grouping are available for use in formulas. For a pivot table, depending on how many pivot rows, columns, or values exist, other calculated totals might be available to use in formulas, such as with the [Subtotal](docs:subtotal) or [PercentOfTotal](/docs/percentoftotal) functions:

* **Row Total**: The grand total for the row. Calculates the aggregate of the values across the pivot row. If there are multiple pivot rows, this is the grand total for the lowest-level row in the grouping. In the example screenshot, the values in the **Total** column for Maine, 248 and 316, are row totals.
* **Parent Row Total**: The grand total for the parent row, equivalent to the aggregate of the column totals in the grouping. Functions as a subtotal for each group of rows in the pivot table. In the example screenshot, the values for the **East** and **West** row are the parent row totals for the child rows. For example, 32995 is the parent row total for each **Store State** row in the **East** grouping for the month column 2023-01.
* **Column Total**: The grand total for the column. Calculates the aggregate of the values in the pivot column. In the example screenshot, the values in the **Total** row for specific months are column totals. For example, for the month column of 2023-01, 81643 is the column total. For 2023-02, 74664 is the column total.
* **Parent Column Total**: The grand total for the parent column, equivalent to the aggregate of the row totals in the grouping. Functions as a subtotal for each group of columns in the pivot table. In the example screenshot, the values in the **Total** column at the parent column level contains the parent column totals. For example, 564 is the parent column total for **Maine**.

In the screenshot, the **East** and **West** rows each show a parent row total calculating the sum of all states in the region. These two parent row totals are subtotals, and are summed to calculate the pivot table grand totals. There are also column subtotals in the **Total** column in the month level.

For examples working with pivot table totals in calculated columns, see the following tutorials:

* [Tutorial: Calculate a percentage for subtotals in a pivot table](#tutorial-calculate-a-percentage-for-subtotals-in-a-pivot-table)
* [Tutorial: Calculate a percentage for row subtotals](#tutorial-calculate-a-percentage-for-row-subtotals)

## Show and hide totals in a pivot table

You can choose to show or hide totals in a pivot table for specific pivot rows and columns. Totals are shown by default in a pivot table. Totals appear differently depending on whether the pivot table displays rows as a single column or separate columns. See [Display multiple pivot rows as separate columns](/docs/working-with-pivot-tables#display-multiple-pivot-rows-as-separate-columns) for more details about that setting.

> 💡
>
> ### Totals are available when your pivot table contains aggregated values, such as sums or counts.

For details about showing or hiding totals in a grouped table, see [Show totals in a grouped table](/docs/create-and-manage-tables#show-totals-in-a-grouped-table).

### Hide grand totals

To hide or remove all grand totals for your pivot table, do the following:

1. Start customizing a workbook or open it for editing.
2. Select the pivot table that you want to modify.
3. In the side panel, select **Format**, then click the **Totals** header to expand the section.
4. For **Show grand totals**, turn off the toggle.

   All grand totals (the **Grand total** column and **Grand total** row) are removed from the pivot table.

   ![Pivot table showing the sales quantities for store regions and states, with columns for each quarter. Subtotals appear for the West and East regions, but no grand totals are shown.](https://files.readme.io/a4831ed686053c9b5f8d8929a500f185f4993a64c34c847d2dfc4c37ed63d588-pt-hide-grand-totals.png)

To hide or remove only the column-level grand total, do the following:

1. On the pivot table or in the editor panel, select the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) next to the column name. In this example, the **Quarter of Date** column.
2. In the dropdown menu, select **Totals of *Column Name***, then select **Show grand total** so that the checkmark disappears.

   The **Grand total** column is removed from the pivot table.

   ![Pivot table showing the sales quantities for store regions and states, with columns for each quarter. Subtotals appear for the West and East regions, and a Total row is shown.](https://files.readme.io/7b33242fa64c7579671908578493701660a0a0cc049030da9a2c574a00a645ff-pt-hide-column-grand.png)

### Hide parent row totals

To hide or remove only the row-level grand total, do the following:

1. On the pivot table or in the editor panel, select the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) next to the column name. In this example, the **Store Region** column.
2. In the dropdown menu, select **Totals of *Column Name***, then select **Show grand total** so that the checkmark disappears.

   The **Grand total** row is removed from the pivot table.

   ![Pivot table showing the sales quantities for store regions and states, with columns for each quarter. Subtotals appear for the West and East regions, and a Total column is shown.](https://files.readme.io/58d7fb9002dbb01e6e8019b3a3eb34a3353e32f4b7973b7d08ea71102cde56a9-pt-hide-row-grand.png)

### Hide subtotals

To hide or remove subtotals in a pivot table, do the following:

1. Start customizing a workbook or open it for editing.
2. Select the pivot table that you want to modify.
3. In the side panel, select **Format**, then click the **Totals** header to expand the section.
4. For **Show subtotals**, turn off the toggle.

   All subtotals are removed from the pivot table. In this example, the **Total** row for each store region is removed.

   ![Pivot table showing the sales quantities for store regions and states, with columns for each quarter. Subtotals do not appear for the West and East regions, and a Total row and a Total column are shown.](https://files.readme.io/fd304efb7993ce0978f6dcaeccbfe6607e8772d39d7b90be399171f758486b6f-pt-hide-subtotals.png)

If your pivot table displays displays rows as a single column and the rows are collapsed, hiding subtotals removes the total values from the pivot table:

![Pivot table showing the sales quantities for store regions and states, with columns for each quarter. Subtotal values do not appear for the West and East regions and instead the rows are highlighted yellow with no values. A grand total row and a grand total column are shown.](https://files.readme.io/fe7582ca74277fa76c47c1015bb79e9f69e5ea498e89d7d4a59c03bd2594574b-pt-hide-subtotals-collapse.png)
> 💡
>
> ### You can also hide a specific subtotal level by deselecting **Show subtotals** in the column menu for the child pivot row. In this example, open the column menu for the **Store Region** column to hide the subtotal for all store states in each region.

## Customize totals and subtotals

Build more flexible reports by customizing the formula used to calculate totals and subtotals for grouped tables and pivot tables. Choose to set a different aggregate or write a custom formula to set a custom total or custom subtotal. You can also [customize the labels](#customize-total-labels) used for totals and subtotals, even if you don't customize the aggregate formula.

### Change aggregate of a subtotal

To change the aggregate of a subtotal in a pivot table or grouped table, such as from calculating a Sum() to an Avg(), do the following:

> 📘
>
> ### Before you start, make sure that the totals that you want to adjust are visible. See [Show and hide totals in a pivot table](#show-and-hide-totals-in-a-pivot-table) or [Show totals in a grouped table](/docs/create-and-manage-tables#show-totals-in-a-grouped-table).

1. Select a pivot table or grouped tables with totals.
2. For a subtotal or total, locate and select the total row or column.
3. Do one of the following:

   * Right-click any cell in the totals row or column to open the context menu.
   * For the relevant pivot row, column, or higher-level table grouping column, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu.
4. Select ***`<Column>`* totals** , then choose **Set aggregate** and select the relevant aggregate function. The default is **Auto** (Sum).

   ![Column menu open showing Product Type totals with Set aggregate selected and Avg hovered over in the last submenu.](https://files.readme.io/10f87fdd591832fc1e09e07ab7afdc89f329979309e8ecbde88ee826f8288f8f-cs-set-agg-menu.png)

   The table updates to reflect the change:

   ![Grouped table with subtotals showing averages instead of totals.](https://files.readme.io/f8f610d2db58346dbbe8fb2cec6f6d964f53120e5da55de8a64567445400ab81-cs-grouped-subtotal-avg.png)

#### Example: Customize grouped table subtotals

For example, if you have a grouped table that shows sales for specific product types in different stadium levels throughout a baseball season, you can set the subtotals for each stadium level to show the average sales, but keep the grand total as a sum.

1. Add a table to your workbook and use the MLB\_STADIUM\_SALES\_HANDS\_ON\_LAB table as your data source.
2. Configure the grouped table:

   1. Create one grouping with the *Product Type* column and a calculation of *Sales Quantity*, which auto-aggregates to *Sum of Sales Quantity*. Rename the column *Total Quantity Sold*.
   2. Add a second grouping with the *Stadium Level* column and a calculation of *Sales Quantity*, which auto-aggregates to *Sum of Sales Quantity*. Rename the column *Total Quantity Sold per Level*.
   3. Hide the ungrouped columns.
3. Right-click a table cell to open the context menu, then choose **Show all totals**.

   > 📘
   >
   > ### In this example, subtotals are highlighted in blue and grand total cells in brown using conditional formatting, and a filter limits the number of product types visible.

   The grouped table looks something like the following:

   ![Grouped table showing Product Type grouping with a grand total appearing under Total Quantity Sold and a second grouping for Stadium Level with Total Quantity Sold per Level, with subtotals for each product type showing Apparel total, Food total, and Premium Food total.](https://files.readme.io/95cd0a9b9b047c4be08fb626bab399937fe9518101bb8dad6edb9c2371b68489-cs-grouped-totals.png)
4. Change the subtotal for each product type to calculate an average amount of sales, instead of a sum:

   1. Click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) for the *Product Type* column to open the column menu, or right-click any cell in the totals row to open the context menu.

      ![Column menu open for the Product Type column, showing Product Type totals menu option selected, then Set aggregate chosen, hovering over the Avg aggregate option.](https://files.readme.io/5d1cad19294b4d28122671cba30821f5f6e4d647b4bd6f621a31c37e8f340790-cs-set-agg-menu.png)
   2. Select ***`<Column>`* totals**, then choose **Set aggregate** and select the **Avg** aggregate function. The default is **Auto** (Sum).

      The subtotal values and labels update accordingly:

      ![Grouped table showing Product Type grouping with a grand total appearing under Total Quantity Sold and a second grouping for Stadium Level with Total Quantity Sold per Level, with subtotals for each product type now showing Apparel avg, Food avg, Premium Food avg with updated values.](https://files.readme.io/ebcf20647f7d135814ec57c2a44f1db5416f191f47b6e5d13fcaac63c3cdc379-cs-grouped-subtotal-avg.png)
5. [optional] Modify the label for the *Product Type* subtotals. Double click on the total label to update it to *Average Sales Volume Per Purchase*. All labels for the subtotal update.

### Write a custom formula for a subtotal or grand total

To write a custom formula to calculate a subtotal or grand total, do the following:

> 📘
>
> ### Before you start, make sure that the totals that you want to adjust are visible. See [Show and hide totals in a pivot table](#show-and-hide-totals-in-a-pivot-table) or [Show totals in a grouped table](/docs/create-and-manage-tables#show-totals-in-a-grouped-table).

1. Locate the total row or column that you want to customize.
2. In the total row or column, select a cell to view the formula in the formula bar.

   ![Pivot table with the first values cell in the grand total row selected and showing a formula of Sum([Sales Quantity]) in the formula bar](https://files.readme.io/6ebec90d4074d31ab021d4e20e2d1e6b3d0b921feae468f0bfc73539d656479e-cs-pivot-formula.png)
3. Update the formula in the formula bar.

   For example, to calculate the total for all product types for each *Stadium Level* but remove the minimum performing product type from the grand total, replace `Sum([Quantity])` with `Sum([Quantity]) - Min([Sum of Quantity (Parent Row Total)])`.

   > 📘
   >
   > ### Your formula must apply to an aggregated value, not a top-level value, otherwise it might show unaggregated results.

   The formula updates for all *Stadium Level* grand totals and the grand total label changes to *Custom grand total*.

   ![Same pivot table with the first values cell in the grand total row selected and showing a formula in the formula bar as described in the example.](https://files.readme.io/775fdf901c6924bd9520d12b6abe90ebb8b95e8ec0799047a199552c270792d6-cs-pivot-end.png)
4. [optional] Modify the label for the total row. See [Customize total labels](#customize-total-labels).

#### Example: Customize pivot table grand totals

For example, if you have a pivot table that shows sales for specific product types and product lines in different levels of a baseball stadium, you can set the grand total to a formula that removes the sales for the lowest-performing product type for a given stadium level, to see how overall sales would be affected if you stopped selling a given product type in a specific stadium level.

1. Add a pivot table to your workbook and use the MLB\_STADIUM\_SALES\_HANDS\_ON\_LAB table as your data source
2. Configure your pivot table like follows:

   1. Add the *Product Type* and *Product Line* columns as pivot rows.
   2. Add the *Stadium Level* column as a pivot column.
   3. Add the *Sales Quantity* column as a pivot value, which is automatically aggregated as *Sum of Sales Quantity*. Rename the column *Total Sales Volume*.
   4. Set the display of your pivot table to **Display as separate columns**.
   > 📘
   >
   > ### In this example, subtotals are highlighted in blue and grand total cells in brown using conditional formatting, and a filter limits the number of product types visible.

   ![Pivot table configured as described, with a grand total for stadium level 100 of 2150526, level 200 of 1178868, level 300 of 1478297, and for all levels 48078691.](https://files.readme.io/776a16dee7e8cca360d4be551b4eb7ae42658626a7eecddf3835498949c03154-cs-pivot-start.png)
3. To change the grand total to a custom formula that removes sales for the lowest-performing product line for each stadium level, locate the grand total row.

   The grand total column calculates the total sales volume for each product line across all stadium levels, while the grand total row calculates the total sales volume for all product types for each stadium level.
4. Select a cell in the grand total row, then modify the formula from `Sum([Sales Quantity])` to `Sum([Sales Quantity]) - Min([Total Sales Volume (Parent Row Total)])`.

   ![Same pivot table with the first values cell in the grand total row selected and showing a formula of Sum([Sales Quantity]) in the formula bar](https://files.readme.io/6ebec90d4074d31ab021d4e20e2d1e6b3d0b921feae468f0bfc73539d656479e-cs-pivot-formula.png)

   The grand total values update for the row and the label updates to *Custom grand total*.

   ![Same pivot table with the first values cell in the grand total row selected and showing a formula in the formula bar as described in the example, with a custom grand total for stadium level 100 of 1549154, level 200 of 915776, level 300 of 1188849, and for all levels of 4544599.](https://files.readme.io/775fdf901c6924bd9520d12b6abe90ebb8b95e8ec0799047a199552c270792d6-cs-pivot-end.png)

### Customize total labels

You can customize the label for a subtotal or grand total in a table or pivot table:

1. Locate the total label that you want to rename on the table or pivot table.
2. Double-click the label to make it editable, then enter a new label.

   ![Label for a subtotal in a grouped table highlighted for editing](https://files.readme.io/4daaa66fe8c0a4ccc641987e79970d9ca71d0e3898bc4cf8f18e27d658cf8d40-cs-rename-start.png)

   > 📘
   >
   > ### If you change the label for a subtotal, all subtotal labels change for that level and value combination.
3. Press enter on your keyboard, or click outside of the cell, to save the new label.

   ![](https://files.readme.io/507f4cf608e62796334e474459ac631144cfdb458241fea2aff340d2f5c7bef1-cs-rename-end.png)

> 💡
>
> ### To revert to the default label for a total or subtotal, remove the existing label. Double-click the label and delete the existing label, then press enter to save your changes.

### Limitations when customizing totals and subtotals

* Renamed subtotal and grand total labels are not updated downstream. Child tables created from a pivot table or grouped table with custom formulas for totals display the original column names. Any formulas, such as summary metrics, that reference the total or subtotal values must instead reference the original column names:

  + *<Values Column Name> (Parent Row Total)* for subtotals on a pivot row.
  + *<Values Column Name> (Row Total)* for grand totals of a pivot row.
  + *<Values Column Name> (Parent Column Total)* for subtotals of a pivot column.
  + *<Values Column Name> (Column Total)* for grand totals of a pivot column.
  + *<Values Column Name> (Grand Total)* for the grand total of the value for both rows and columns for a pivot table or grouped table.
* After customizing a subtotal formula, cells where subtotals interact might be blank if the intersecting total does not make sense. For example, if one subtotal calculates an average and the other subtotal calculates the maximum value:

  ![Pivot table with subtotals row with an average aggregate intersecting with a column subtotal showing max values, and the intersecting cells are blank.](https://files.readme.io/71b0b0ae9e9b875bdadc35c92de22376567acdab091cc2383c22ae323a6a23f9-cs-pivot-intersect.png)

## Tutorial: Calculate a percentage for subtotals in a pivot table

In this example, calculate the percent of total units sold in a given region. This example uses the PLUGS\_ELECTRONICS\_HANDS\_ON\_LAB\_DATA table included in the Sigma Sample Database.

Start with a pivot table with pivot rows **Store Region** and **Store State** and an aggregate value of **Sum of Quantity**.

![Pivot table with the specified rows and value. To make the pivot table smaller, only the West and East regions are shown.](https://files.readme.io/e69da542d55256a592d975d370456bddfab9ed06e4ba32ff7a175f4d89671238-pt-tutorial-sub-1.png)

To calculate the percentage of total units sold, add a new column to the pivot table:

1. In the editor panel, in the **Values** header, click **Add calculation...** (**+**).
2. Select **Add new column**.
3. In the formula bar for the new column, enter:

   ```
   [Sum of Quantity (Row Total)] / [Sum of Quantity (Parent Row Total)]
   ```

   ![Formula bar for the new column, with the drop-down menu open showing auto-complete options for the Parent Row Total column.](https://files.readme.io/34cbbed8961d8012d770e09bed0bed1f04fdc2ea57edc86a3124ba15c92f0746-pt-tutorial-sub-2.png)
4. Press **Enter** or click the checkmark to save the formula.
5. To format the calculated column as a percentage, in the workbook toolbar, click **Format as percent** (%).

   The result appears as follows:
   ![](https://files.readme.io/92d5b7ac1da57a78a4f740cd2465a6b1fbec0a020d22cfbe5fbe63d5d8903b0a-pt-tutorial-sub-3.png)

## Tutorial: Calculate a percentage for row subtotals

In this tutorial, calculate the percent of total state retail sales broken down by region and sales quarter.

Start with a pivot table with pivot rows **Store Region** and **Store State**, a pivot column of **Date**, truncated to display **Quarter of Date**, and an aggregate value of **Sum of Quantity**.

![Pivot table showing the sales quantities for store regions and states, with columns for each quarter.](https://files.readme.io/7a7844b77c8a4545162f561ba2f944b15c856fde706b849529ae53889d0a798b-pt-tutorial-row.png)

1. In the editor panel, in the **Values** header, click **Add calculation...** (**+**).
2. Select **Add new column**.
3. In the formula bar for the new column, enter:

   ```
   [Sum of Quantity] / [Sum of Quantity (Parent Row Total)]
   ```

   ![Formula bar open showing the auto complete for the different types of totals, with Parent Row Total selected for the second half of the formula.](https://files.readme.io/f4010aba3aa2bada24be625dd91c9d5b668dd0eadcc417ce59f5c7842b427f08-pt-tutorial-row-2.png)
4. Press **Enter** or click the checkmark to save the formula.
5. To format the calculated column as a percentage, in the workbook toolbar, click **Format as percent** (%).

   The result appears as follows:
   ![](https://files.readme.io/075907424344253b327b9891d127285922ca2db0ce8b513ae1c16221622ba666-pt-tutorial-row-3.png)

Updated 3 days ago

---

Related resources

* [Working with Pivot Tables](/docs/working-with-pivot-tables)
* [Format pivot table totals](/docs/format-pivot-table-totals)
* [PercentOfTotal](/docs/percentoftotal)
* [Subtotal](/docs/subtotal)

* [Table of Contents](#)
* + [Definitions and key concepts](#definitions-and-key-concepts)
  + [Show and hide totals in a pivot table](#show-and-hide-totals-in-a-pivot-table)
  + - [Hide grand totals](#hide-grand-totals)
    - [Hide parent row totals](#hide-parent-row-totals)
    - [Hide subtotals](#hide-subtotals)
  + [Customize totals and subtotals](#customize-totals-and-subtotals)
  + - [Change aggregate of a subtotal](#change-aggregate-of-a-subtotal)
    - [Write a custom formula for a subtotal or grand total](#write-a-custom-formula-for-a-subtotal-or-grand-total)
    - [Customize total labels](#customize-total-labels)
    - [Limitations when customizing totals and subtotals](#limitations-when-customizing-totals-and-subtotals)
  + [Tutorial: Calculate a percentage for subtotals in a pivot table](#tutorial-calculate-a-percentage-for-subtotals-in-a-pivot-table)
  + [Tutorial: Calculate a percentage for row subtotals](#tutorial-calculate-a-percentage-for-row-subtotals)