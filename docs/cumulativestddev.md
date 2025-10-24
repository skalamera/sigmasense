# CumulativeStdDev

# CumulativeStdDev

The **CumulativeStdDev** function calculates the standard deviation of a column up to and including the current row value.

## Syntax

```
CumulativeStdDev([Column])
```

Function Arguments:

* **[Column]** (required) - The column of numbers to evaluate the cumulative standard deviation.

Cumulative functions depend on the order of the given column. If you change the sorting you change the result.

## Example

```
CumulativeStdDev([Monthly Revenue])
```

A table contains the monthly revenue of a store. The **CumulativeStdDev** function can be used to find the standard deviation up to and including the current month.

![](https://files.readme.io/9712c3f-5.png)

Updated 3 days ago

---

Related resources

* [CumulativeVariance](/docs/cumulativevariance)
* [MovingStddev](/docs/movingstddev)
* [StdDev](/docs/stddev)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)