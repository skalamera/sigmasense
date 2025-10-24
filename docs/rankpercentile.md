# RankPercentile

# RankPercentile

Rank the rows in the table by percentile using the input column.

## Usage

`RankPercentile(column, [direction])`

**column** (required) The column used to order the table. The input column can be numbers, dates or text.

**direction** (optional) The direction to sort the input column. Default is to sort ascending.

> 📘
>
> ### The [percentile](https://en.wikipedia.org/wiki/Percentile) is a number between 0 and 1. The last row is always 1 and the first is 0, unless there is only 1 row or there is a tie for the top value. To display the result as percentages as opposed to numbers, change the column formatting from Automatic to Percent.

## Example

`RankPercentile([Population by State])`

* This assigns the state with the smallest population rank 0, the largest population is assigned rank 1.

`RankPercentile([Population 2010])`

![Screenshot of results showing the county with the lowest population for each state ranked with 0.00% percentile and the county with the largest population ranked with 100.00%](https://files.readme.io/ed21ebd-11.png)

`RankPercentile([COUNTY - Count])`

![Screenshot of results showing states listed by count of counties, with the state that has fewest counties listed with a RankPercentile value of 0.00% and the most counties visible on this screenshot being Idaho with 37.25%.](https://files.readme.io/ca7a4dc-22.png)

Updated 3 days ago

---

Related resources

* [CumeDist](/docs/cumedist)
* [PercentileCont](/docs/percentilecont)
* [Rank](/docs/rank)
* [RankDense](/docs/rankdense)
* [RowNumber](/docs/rownumber)

* [Table of Contents](#)
* + [Usage](#usage)
  + [Example](#example)