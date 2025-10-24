# VisibilityLimit

# VisibilityLimit

The **VisibilityLimit** function limits the values displayed in a column to the number of specified values according to an order calculated by one of the [Rank](/docs/rank) (default), [RankDense](/docs/rankdense), or [RowNumber](/docs/rownumber) functions. The order used by the ranking function relies on the sort applied to the data element.

This function is used to limit displayed values in a data element. For more granular control over which values are displayed, such as to specify the bottom N values or choose a specific aggregate values column in a pivot table to use to sort the output column, see [Limit displayed values in a data element](/docs/limit-displayed-values-in-a-data-element).

## Syntax

```
VisibilityLimit(output, limit, [rank_type])
```

### Function arguments

|  |  |
| --- | --- |
| **output** | Column to contain the limited output. Must be Text data type. |
| **limit** | Number of values to limit the visibility. |
| **rank\_type** | The ranking function to use to limit the output column. Specify one of [Rank](/docs/rank) (default), [RankDense](/docs/rankdense), or [RowNumber](/docs/rownumber). |

## Notes

* Use this function with sorted, aggregated data.
* You cannot use the function multiple times in one formula. For example, attempting to concatenate values with a formula like the following is not supported:  
  `VisibilityLimit([PLUGS_ELECTRONICS_HANDS_ON_LAB_DATA/Store Region], 3) & VisibilityLimit([Store State], 4)`

## Example

In a pivot table with pivot rows of *Store Region* and *Store Name*, and a values column *Total Sold*, you can limit the store names to the top 3 in each region:

```
VisibilityLimit([Store Name], 3)
```

In this case, the ranking function is applied to the *Store Name* column, and displays the first three stores alphabetically, grouping the remainder into an *Others* category.

![Pivot table with store region and store name columns. Visibility limit function is applied to the store name column as described, showing the top 3 store names in each region, such as Angrave Store, Arline Store, and Arline Store in the South region.](https://files.readme.io/ec16f424b1b9675f3631cbfec4faea366c55d826b2c5e04f55c90bb7fed7c81c-vislimit-unsorted.png)

If you want to display the top 3 stores by total amount sold, sort the *Total Sold* column descending.

![Pivot table with store region and store name columns. Visibility limit function is applied to the store name column as described, showing the top 3 store names in each region, but ordered by total sold. For example, the Southwest region lists Others, Emily Store, then Collins Store #355 and Collins Store #911.](https://files.readme.io/c6a45de87d4c463d944d55a71ad81f4c3f47c099ec9eb656720b54f282a58969-vislimit-sorted.png)

If you want to specify a different column to use for the ranking function, limit the visibility of displayed values from the column details menu. See [Limit displayed values in a data element](/docs/limit-displayed-values-in-a-data-element).

Updated 3 days ago

---

[RowNumber](/docs/rownumber)[Operators overview](/docs/operators-overview)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + - [Function arguments](#function-arguments)
  + [Notes](#notes)
  + [Example](#example)