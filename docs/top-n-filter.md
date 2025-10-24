# Top N filter

# Top N filter

It's very common to filter columns by Top N, the top number (N) of rows, based on the filter criteria. This is useful when you want to see the top values in a sorted list, instead of the whole list.

***Important***: Because of the way Sigma automatically handles aggregations and groupings, the Top N filter may behave slightly differently than what you may have experienced with other products. See the examples and tips below for details.

## Examples of Top N

### How Applying Top N Changes a Bar Chart

For example, you may be interested in the top 5 stores that move the most merchandise, sorted by state. Before applying the Top N filter, a bar chart may look like this:

![](https://files.readme.io/f23f6e9-1.png)

***Tip***: Maximize the chart to see its data table underneath. Sometimes it is helpful when applying filters to see how the filters change the table.

After applying Top N to the [Sum of Quantity], the chart looks like this:

![](https://files.readme.io/8c9a2df-2.png)

### Relationship of Top N Bar Chart to its Table

This example shows a maximized view of a chart, which includes its data table. The Top N filter is on the [Sum of Price] column. (If you put the filter on the [Store City] column, Sigma would filter the cities alphabetically.) This results in the list of 10 cities whose stores have the highest total prices of all things sold.

![](https://files.readme.io/28d37c0-3.png)

### Top N on a Pivot Table with Multiple Groupings

When there are multiple grouping levels, the Top N filter does not filter the overall top 10 items; instead it filters within a bin defined by the 2nd lowest grouping level. In this example, Top N will apply to the Top 10 [Store City] rather than the Top 10 [Store Region] or [Store State].

![](https://files.readme.io/819274d-4.png)

### Additional Examples

For more in-depth examples see the Community article [How to Use a Top N Filter Parameter for Visualizations](https://community.sigmacomputing.com/t/how-to-use-a-top-n-filter-control-for-visualizations/2055).

See also the video from [phData](https://www.phdata.io/), [Understanding Top N Filters in Sigma](https://youtu.be/eTqEodEPRZc).

### Related Filters: Bottom N, Top Percentile, Bottom Percentile

You can use the same process as described above to use the other filters in the same dropdown.

![](https://files.readme.io/4d51ccc-5.webp)

## How to Filter Using Top N

1. Set up the columns on a bar chart.
   * Select a new visualization using + ADD ELEMENT > DATA ELEMENTS > VIZ.
   * Add a column to the Y axis.
   * Add a column to the X axis. Keep the default aggregation.  
     **Important**: Sigma requires an aggregated column when using Top N.
2. If needed, set the sort criteria.
3. For the column you want to filter, select its menu > Filter.   
   ![column-menu-filter-option.png](https://files.readme.io/adabdf5-6.png)  
   **Important**: Set the Top N filter on the column you want to be ranked. This can be counter-intuitive. In the example above, you want to show the top 10 Stores, so you would rank on [Store Name] not on [Sum of Quantity].
4. In the Filter panel, click the 3 dots to see the options.  
   ![filters-panel-dotmenu.png](https://files.readme.io/7fd31c7-7.png)
5. Select Top N.  
   ![filters-panel-filtertype-menu.png](https://files.readme.io/f15e482-8.png)
6. Enter the number of results to display.  
   ![filter-options-topn.png](https://files.readme.io/4e85bbd-9.png)
7. Change the default chart header to best describe the filtered chart. For example, change "Sum of Quantity by Store Name", which is an internally-produced name, to "Top 10 Stores by Quantity Sold".

### Change the Ranking Function

By default the Top N filter uses the [Rank](/docs/rank) function. In some cases you may want to change it to the [RankDense](/docs/rankdense) or [RowNumber](/docs/rownumber) functions instead. The options are:

* **Rank**[:](/docs/rank) Assigns the same rank to duplicate values, and a gap is placed between the ranks. See [Rank](/docs/rank). Default.
* **Rank Dense**: Assigns the same rank to duplicate values, and there is no gap between ranks. See [RankDense](/docs/rankdense).
* **Row Number**: Ranks according to the highest row numbers. See [RowNumber.](/docs/rownumber)

To change the ranking function:

1. From the control's filter icon at the top right of the control, open the control's FILTERS & CONTROLS panel.
2. From the filter's **More** menu, select Ranking function.  
   ***Tip***: The text next to the menu option shows the currently-used function. By default it is Rank.
3. Select the type of rank you want.  
   ![filters-topn-change-rank.webp](https://files.readme.io/f1a2031-10.webp)

## Tips for Top N

* Maximize the chart so you can see the table fields as you apply filters.
* Only apply the top N filter to the column that is being ranked.   
  For example, you want a bar chart showing the top ten product types. You put [Product Type] on the X-axis and [Sum of Revenue] on the Y-axis, then put the Top N filter on the [Sum of Revenue] column. This gives you the top 10 values of [Sum of Revenue] grouped by [Product Type].  
  Otherwise, if you put Top N on the [Product Type] column the chart will sort the products alphabetically.
* Sigma requires an aggregated column for Top N.
* Top N applies only to columns of type text, number, or date.
* For a text column, the top N is determined by alphanumeric sorting.

Updated 3 days ago

---

Related resources

* [Rank](/docs/rank)
* [How to Use a Top N Filter Parameter for Visualizations (Community)](https://community.sigmacomputing.com/t/how-to-use-a-top-n-filter-parameter-for-visualizations/2055?_gl=1*muui57*_ga*ODkzMjkyNDY1LjE3MDAwMDU1NzM.*_ga_PMMQG4DCHC*MTcwMTIwOTMxNS4yNC4xLjE3MDEyMTcyMzAuNjAuMC4w)
* [Understanding Top N Filters in Sigma](https://youtu.be/eTqEodEPRZc)
* [phData](https://www.phdata.io/)

* [Table of Contents](#)
* + [Examples of Top N](#examples-of-top-n)
  + - [How Applying Top N Changes a Bar Chart](#how-applying-top-n-changes-a-bar-chart)
    - [Relationship of Top N Bar Chart to its Table](#relationship-of-top-n-bar-chart-to-its-table)
    - [Top N on a Pivot Table with Multiple Groupings](#top-n-on-a-pivot-table-with-multiple-groupings)
    - [Additional Examples](#additional-examples)
    - [Related Filters: Bottom N, Top Percentile, Bottom Percentile](#related-filters-bottom-n-top-percentile-bottom-percentile)
  + [How to Filter Using Top N](#how-to-filter-using-top-n)
  + - [Change the Ranking Function](#change-the-ranking-function)
  + [Tips for Top N](#tips-for-top-n)