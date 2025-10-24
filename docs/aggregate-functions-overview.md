# Aggregate functions

# Aggregate functions

> 📘
>
> These functions work best with aggregated data in a grouped table. For a video explanation of working with functions of this type, see [Getting started with functions and groupings in Sigma](https://www.sigmacomputing.com/resources/training-videos/table-grouping-and-functions).

Aggregate functions evaluate multiple rows of data to return a single value. For example, you can use aggregate functions to perform group calculations (like **Sum** and **Avg**), retrieve specific values (like **Min** and **Max**), assess the data to provide insights (like **Count** and **CountDistinct**), or join multiple values (like **ArrayAgg** and **ListAgg**).

|  |  |
| --- | --- |
| [ArrayAgg](/docs/arrayagg) | Identifies non-null row values in a column or group and aggregates them into a single array. |
| [ArrayAggDistinct](/docs/arrayaggdistinct) | Identifies distinct non-null row values in a column or group and aggregates them into a single array. |
| [Avg](/docs/avg) | Calculates the average value of a column or group. |
| [AvgIf](/docs/avgif) | Calculates the average value of a column or group *when the specified condition is* `True`. |
| [Corr](/docs/corr) | Calculates the Pearson correlation coefficient (bivariate correlation) of two columns. |
| [Count](/docs/count) | Counts the number of non-null and non-empty values in a column or group. |
| [CountDistinct](/docs/countdistinct) | Counts the number of unique non-null and non-empty values in a column or group. Does not count duplicate values. (Same as **[Ndv](/docs/ndv)**.) |
| [CountDistinctIf](/docs/countdistinctif) | Counts the number of unique non-null and non-empty values in a column or group *when the specified condition is* `True`. Does not count duplicate values. |
| [CountIf](/docs/countif) | Counts the number of non-null and non-empty values in a column or group *when the specified condition is* `True`. |
| [GrandTotal](/docs/grandtotal) | Calculates the grand total for column or group. |
| [ListAgg](/docs/listagg) | Joins the values of a group or column into a single text string. |
| [ListAggDistinct](/docs/listaggdistinct) | Joins the unique values of a group or column into a single text string. Does not include duplicate values. |
| [Max](/docs/max) | Retrieves the maximum (largest or latest) value in a column or group. |
| [MaxIf](/docs/maxif) | Retrieves the maximum (largest or latest) value in a column or group *when the specified condition is* `True`. |
| [Median](/docs/median) | Determines the median (midpoint) value of a column or group. |
| [Min](/docs/min) | Retrieves the minimum (smallest or earliest) value in a column or group. |
| [MinIf](/docs/minif) | Retrieves the minimum (smallest or earliest) value in a column or group *when the specified condition is* `True`. |
| [PercentileCont](/docs/percentilecont) | Calculates the continuous kth percentile of a column or group. |
| [PercentileDisc](/docs/percentiledisc) | Calculates the discrete kth percentile of a column or group. |
| [PercentOfTotal](/docs/percentoftotal) | Calculates the percentage a value contributes to the specified aggregate total. |
| [RegressionIntercept](/docs/regressionintercept) | Calculates the y-intercept of the linear regression line. |
| [RegressionR2](/docs/regressionr2) | Calculates the coefficient of determination of the linear regression line. |
| [RegressionSlope](/docs/regressionslope) | Calculates the slope of the linear regression line. |
| [StdDev](/docs/stddev) | Calculates the standard deviation of a column or group. |
| [Subtotal](/docs/subtotal) | Calculates the subtotal of a column or group. |
| [Sum](/docs/sum) | Calculates the sum of a column or group. |
| [SumIf](/docs/sumif) | Calculates the sum of a column or group *when the specified condition is* `True`. |
| [SumProduct](/docs/sumproduct) | Calculates the product of row values across specified columns, then calculates the sum of the resulting products for a column or group. |
| [Variance](/docs/variance) | Estimates the sample variance (spread of distribution) of a column or group. |
| [VariancePop](/docs/variancepop) | Calculates the population variance (spread of distribution) of a column or group. |

Updated 3 days ago

---

[Function index](/docs/function-index)[ArrayAgg](/docs/arrayagg)