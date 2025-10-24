# Customize the sort order of data elements

# Customize the sort order of data elements

In Sigma, you can customize the sort order of tables, pivot tables, and charts. You can sort by any column in the data, even if the column is hidden or not used in a chart. For tables and pivot tables, you can also define the sort order for null values in a column.

## Customize the sort order of a chart

To customize the sort order of a chart, such as a bar chart, do the following:

**Before you start:** You must be editing or customizing the workbook to configure custom sort.

1. Right click anywhere on the chart or select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**.
2. In the menu that appears, select **Sort** > **Custom sort...**.
3. In the **Custom Sort** modal, for **Sort by**, select a column to sort by.
4. For **Order**, select **Ascending** or **Descending**.
5. For **Aggregation**, select an aggregation type. Text columns do not require an aggregation.
6. Click **Save**.

> 💡
>
> For a layered chart, such as an area chart or a scatter chart, the sort order of the values affects the order in which the layers are displayed.

## Customize the sort order of a pivot table

To sort a pivot table by one column, and choose the sort order for null values in that column, do the following:

**Before you start:** You must be editing or customizing the workbook to configure custom sort.

1. For a pivot column or pivot row, select the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu.
2. In the menu that appears, select **Sort** > **Custom sort...**.
3. In the **Custom Sort** modal, the selected column is shown.
4. For **Sort by**, select a column to sort the selected column by. The sort column must exist in the pivot table, even if it is not displayed.

   ![Custom sort modal with Risk Category chosen as the sort by column, Ascending as the order, and Nulls set to the default. It is a text column so there is no aggregation.](https://files.readme.io/818a65c3df11ebdd2fe96140ba5daa1de2a5c665810712f7ac0fc3225870e070-cs-pivot.png)
5. For **Order**, select **Ascending** or **Descending**.
6. For **Aggregation**, select an aggregation type. Text columns do not require an aggregation.
7. For **Nulls**, choose from **Connection Default**, **First**, or **Last**:

   * **Connection Default** matches the same ordering used by your data warehouse.
   * **First** lists null values first in a column, then sorts the rest of the column values by the sort order.
   * **Last** lists null values last in a column, after the sorted column values.
8. Click **Save**.

### Sort a specific values column

You can choose to sort a specific values column differently than other columns. For example, to sort only the *High Risk* column of a pivot table in descending order, do the following:

1. For a pivot table, locate the column that you want to sort differently, then right-click to open the context menu.

   ![Pivot table of business violations by risk category, with the high risk column context menu open.](https://files.readme.io/3526af8889adc0416f6eb14ea1fa7bdd31eac193a32cdb8368bbb16d7d156ba9-cs-pivot-context-menu.png)
2. Choose an ascending (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/sort_asc.svg)) or descending (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/sort_desc.svg)) sort for the values.
   The values in that column sort accordingly.
3. [optional] Adjust the custom sort, for example to change how null values are sorted in that column:

   1. For the relevant pivot rows, select the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu.

      ![Column menu open for the Business ID pivot row, selecting the custom sort option](https://files.readme.io/6f360eac14a20728c98cecc7213b7e71432afe6b3460db6c44a22b5a09ed9e98-cs-pivot-row-menu.png)
   2. In the menu that appears, select **Sort** > **Custom sort...**.

      ![Custom sort modal for the Business ID pivot row, showing that Business ID is being sorted by total violations in the high risk risk category.](https://files.readme.io/9b5c7309bdf4b81222253132fbd89c353b4b0113fab2d4dd0a1247b225b8419a-cs-custom-sort-pivot-val.png)
   3. Adjust the sort for the values as desired. For example, for **Nulls**, choose to sort the null values last.
   4. Click **Save**

## Customize the sort order of a table

You can sort a table by one or multiple columns, and choose the sort order for null values in those columns.

> 💡
>
> If you want to sort by multiple columns, define the sorting rules in the order that they should apply to the table. You cannot change the order of custom sorting rules after you define them.

**Before you start:** You must be editing or exploring the workbook to configure custom sort.

To customize the sort order of a table, do the following:

1. For any column in the table, select the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu.
2. In the menu that appears, next to the **Sort** option, select **Custom sort...** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/settings.svg)).
3. In the **Sort** modal, for **Column name**, select a column to sort by.
4. For **Sort order**, select **A to Z** or **Z to A**. Different columns show different options. Date columns can be sorted from **Oldest to Newest** or **Newest to Oldest** and number columns can be sorted from **Largest to smallest** or **Smallest to largest**
5. For **Nulls**, choose from **Default**, **First**, or **Last**:

   * **Default** matches the same ordering used by your data warehouse.
   * **First** lists null values first in a column, then sorts the rest of the column values by the sort order.
   * **Last** lists null values last in a column, after the sorted column values.
6. To sort by multiple columns, select **Add new** and repeat the steps for another column.
7. Click **Save**.

## Example: Use a helper column to sort an unordered column

Because you can customize the sort order by hidden columns, you can create a helper column to define an order for a column of string values. You can create a helper column to sort a column of weekday names in order, month names in order, or another text column according to an order that you define.

For example, in the Sigma Sample Database, the `EXAMPLES.SF_RESTAURANTS.VIOLATION_TYPES` table includes a *Risk Category* column that lists 3 types of risk: "High Risk", "Moderate Risk", and "Low Risk". If you want to sort the risk categories in order from most to least severe, you can create a column to define the sort order, then set up a custom sort for a visualization that uses that helper column:

1. While editing a workbook, add a table that uses the `VIOLATION_TYPES` table from the Examples schema of the Sigma Sample Database as a data source.
2. Add a column to the table, named *Risk Category Sort*. For the column, use the following formula:

   ```
   Switch([Risk Category], "High Risk", 1, "Moderate Risk", 2, "Low Risk", 3)
   ```

   The formula applies a numeric value to each text value from the *Risk Category* column, from most to least severe.
3. Create a bar chart as a child element from the table, using the *Risk Category* column as the X-axis and *Violation Type Id* as the Y-axis. The *Violation Type Id* column is aggregated to become a count of all violations.

   ![Bar chart showing the count of violation type IDs by risk category, in the order of High Risk, Low Risk, then Moderate Risk.](https://files.readme.io/058bc05f3054c96827f8beb36ce2bf2ef1183af2ff22c49b93ae6f80fed01797-custom-sort-pre.png)
4. Sort the bar chart by selecting ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Sort** > **Custom sort...**.
5. For **Sort By**, select the *Risk Category Sort* column.

   ![Dropdown showing available columns in the visualization data, including columns that are not visualized, such as Risk Category Sort](https://files.readme.io/eb2984e33a03b45a19d378032e58fcf406479378d1af408aaaa1b883fabf313d-custom-sort-modal.png)
6. For **Order**, leave the default of **Ascending** selected to sort from most severe (1) to least severe (3).
7. For **Aggregation**, choose **Sum**. The aggregation is irrelevant in this example.
8. Click **Save** and confirm that your chart is sorted as you expect.

   ![Bar chart showing the count of violation type IDs by risk category, in the order of High Risk, Moderate Risk, then Low Risk.](https://files.readme.io/757021b7a5701564c906599bb374b1cd244f5005b67188b3ecbc479eb4b273f3-custom-sort-after.png)

For another example, see [How to sort a fiscal date column](https://community.sigmacomputing.com/t/how-to-sort-a-fiscal-date-column/2544/1) in the Sigma Community.

Updated 3 days ago

---

[Customize element background and styles](/docs/customize-element-background-and-styles)[Limit displayed values in a data element](/docs/limit-displayed-values-in-a-data-element)

* [Table of Contents](#)
* + [Customize the sort order of a chart](#customize-the-sort-order-of-a-chart)
  + [Customize the sort order of a pivot table](#customize-the-sort-order-of-a-pivot-table)
  + - [Sort a specific values column](#sort-a-specific-values-column)
  + [Customize the sort order of a table](#customize-the-sort-order-of-a-table)
  + [Example: Use a helper column to sort an unordered column](#example-use-a-helper-column-to-sort-an-unordered-column)