# Limit displayed values in a data element

# Limit displayed values in a data element

You can limit which values are displayed for a column in a grouped table, pivot table, or chart.

For example, to only show the top 3 performing stores in each store region in a pivot table, you can limit the displayed stores to the top 3 sorted by total products sold:

![Pivot table showing Store region and store name columns with total quantity sold values. The Store name column is limited to the top 3 stores by total quantity sold, with the remainder showing as Others. Totals are hidden for the table.](https://files.readme.io/672d1aba471a903da827504b5c994c8437a38e4d9a2522e2ae6bf0dea4df286c-vislimit.png)

Different from a [Top N filter](/docs/top-n-filter) , limiting the display values lets you change which values are displayed without affecting the calculated totals and other values. You can also apply this limit using the [VisibilityLimit](/docs/visibilitylimit) function.

## Limit the display values

To limit which values are displayed in a grouped table, pivot table, or chart, do the following:

1. Select the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)), then select **Transform> Limit display values**.
2. For **Display**, choose whether to display the top or bottom number of values, and enter a number.

   For example, choose to display the bottom 10 values, and group the remaining values into an "Others" category.
3. For **by**, choose the function to use to order the aggregated column. Choose one of [**Rank**](/docs/rank), [**RankDense**](/docs/rankdense), or [**RowNumber**](/docs/rownumber).
4. For **Sort by**, select a column to sort the column by when choosing the top or bottom number of values. If the column is not aggregated, choose a function to aggregate by.
5. Click **Done**.

   If you chose to aggregate an unaggregated column, Sigma creates a grouping for your table with the column with limited display values as the group by column, and the aggregated column as the calculation in the grouping.

If you limit the display values in a pivot row or table columns, the Others category is added to the end of the list of columns.

### Remove a limit

After limiting display values, you can remove the limit:

1. For a column with display values limited, select the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu, then select **Transform> Limit display values**.
2. In the **Limit display values** modal, select **Remove limit**.

## Limitations

* You can only limit the display values of Text columns. Other data types, such as Number or Date, are not supported.
* If you change the sort order of the column used for to limit the display values, the values in the "Others" category change according to the sort because the Rank and RankDense functions rely on the sort order.

Updated 3 days ago

---

[Customize the sort order of data elements](/docs/configure-custom-sort)[About Sigma data apps](/docs/data-apps)

* [Table of Contents](#)
* + [Limit the display values](#limit-the-display-values)
  + - [Remove a limit](#remove-a-limit)
  + [Limitations](#limitations)