# Window functions

# Window functions

> 📘
>
> These functions work best with aggregated data in a grouped table. For a video explanation of working with functions of this type, see [Getting started with functions and groupings in Sigma](https://www.sigmacomputing.com/resources/training-videos/table-grouping-and-functions).

Window functions perform operations across an entire table, table grouping (grouped rows), or defined window of rows. Sigma supports [cumulative](#cumulative-window-functions), [moving](#moving-window-functions), [shifting](#shifting-window-functions), and [ranking](#ranking-window-functions) window functions.

### Cumulative window functions

Cumulative window functions evaluate a specified column in a table or grouping and return the running total or cumulative value for all rows up to and including the current row. This differs from aggregate values that calculate a summary value for the entire table or grouping.

|  |  |
| --- | --- |
| [CumulativeAvg](/docs/cumulativeavg) | Calculates the running average up to and including the current row. |
| [CumulativeCorr](/docs/cumulativecorr) | Calculates the correlation coefficient between dependent and independent data columns up to and including the current row. |
| [CumulativeCount](/docs/cumulativecount) | Counts the number of non-null values up to and including the current row. |
| [CumeDist](/docs/cumedist) | Calculates the cumulative distribution of values relative to the current row value. |
| [CumulativeMax](/docs/cumulativemax) | Returns the largest value up to and including the current row. |
| [CumulativeMin](/docs/cumulativemin) | Returns the smallest value up to and including the current row. |
| [CumulativeStdDev](/docs/cumulativestddev) | Calculates the standard deviation of values up to and including the current row. |
| [CumulativeSum](/docs/cumulativesum) | Calculates the sum of values up to and including the current row. |
| [CumulativeVariance](/docs/cumulativevariance) | Calculates the variance of a column up to and including the current row. |

### Moving window functions

Moving window functions evaluate a specified column and return a value based on a defined window of rows that moves in relation to the current row.

|  |  |
| --- | --- |
| [MovingAvg](/docs/movingavg) | Calculates the numerical average of a column within a moving window. |
| [MovingCorr](/docs/movingcorr) | Calculates the correlation coefficient of two numerical columns within a moving window. See [Pearson (bivariate) correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) . |
| [MovingCount](/docs/movingcount) | Counts the number of non-Null values in a moving window. |
| [MovingMax](/docs/movingmax) | Finds the maximum value of a column within a moving window. |
| [MovingMin](/docs/movingmin) | Finds the minimum value of a column within a moving window. |
| [MovingStdDev](/docs/movingstddev) | Calculates the standard deviation of a column within a moving window. |
| [MovingSum](/docs/movingsum) | Calculates the sum of a column in a moving window. |
| [MovingVariance](/docs/movingvariance) | Calculates the statistical variance of a column in a moving window. |

### Shifting window functions

Shifting window functions evaluate a specified column in a table or grouping and return the value from a row that shifts in relation to the current row.

|  |  |
| --- | --- |
| [FillDown](/docs/filldown) | Replaces all `null` values in a column or grouping with the closest prior non-null value. |
| [First](/docs/first) | Returns the first row value of a column or grouping. |
| [FirstNonNull](/docs/firstnonnull) | Returns the first non-null value from a column or grouping. |
| [Lag](/docs/lag) | Returns the value from a preceding offset row in a column or grouping. |
| [Last](/docs/last) | Returns the last row value in a column or grouping. |
| [LastNonNull](/docs/lastnonnull) | Returns the last non-null value in a column or grouping. |
| [Lead](/docs/lead) | Returns the value from a subsequent offset row in a column or grouping. |
| [Nth](/docs/nth) | Returns the value from the nth row of a column or grouping. |

### Ranking window functions

Ranking window functions evaluate a specified column in a table or grouping and assign a rank to each row.

|  |  |
| --- | --- |
| [Ntile](/docs/ntile) | Assigns the specified rank, in order, to the column rows of a column, approximately equal number of rows for each rank. |
| [Rank](/docs/rank) | Assigns ranks to unique values in a column, from rank 1 onwards. Skips duplicate values. |
| [RankDense](/docs/rankdense) | Assigns ranks to all values in a column, from rank 1 onwards. Assigns the same rank to duplicate values. |
| [RankPercentile](/docs/rankpercentile) | Ranks the rows in the table by percentile. |
| [RowNumber](/docs/rownumber) | Numbers the table rows, starting with 1. |
| [VisibilityLimit](/docs/visibilitylimit) | Limits the values displayed in a column to the number of specified values according to an order calculated by another ranking function. |

Updated 3 days ago

---

[Variant](/docs/variant)[CumulativeAvg](/docs/cumulativeavg)