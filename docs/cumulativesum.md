# CumulativeSum

# CumulativeSum

The **CumulativeSum** function calculates the sum of the input column up to and including the current row value.

> 📘
>
> ### This function must be used with aggregated data in a grouped table. For a detailed video walkthrough that uses this function, see [Advanced window functions](https://www.sigmacomputing.com/resources/training-videos/table-grouping-and-functions#advanced-window-functions).

## Syntax

```
CumulativeSum([Column])
```

Function Arguments:

* **[Column]** (required) - The column of numbers to evaluate the cumulative sum.

Cumulative functions depend on the order of the given column. If you change the sorting you will change the result.

## Example

```
CumulativeSum([Monthly Revenue])
```

A table contains the monthly revenue of a store for the year 2022. The **CumulativeSum** function can be used to find the total yearly revenue up to and including that month.

![](https://files.readme.io/79042d8-6.png)

Updated 3 days ago

---

Related resources

* [Sum](/docs/sum)
* [MovingSum](/docs/movingsum)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)