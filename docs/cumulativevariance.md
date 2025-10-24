# CumulativeVariance

# CumulativeVariance

The **CumulativeVariance** function calculates the variance of a column up to and including the current row value.

## Syntax

```
CumulativeVariance([field])
```

Function argument:

|  |  |
| --- | --- |
| **field** | The column to reference when calculating cumulative variance. |

> 📘
>
> ### Cumulative functions depend on the order of the given column. If you change the sorting you will change the result.

## Example

```
CumulativeVariance([Close Price])
```

A table contains the daily close price of a stock in 2016. Variance can be used to show the volatility of a stock, where a higher variance indicates higher risk. We can use the **CumulativeVariance** function to identify the change in variance over time.

![](https://files.readme.io/715c9a3-image.png)

Updated 3 days ago

---

Related resources

* [CumulativeStdDev](/docs/cumulativestddev)
* [MovingVariance](/docs/movingvariance)
* [Variance](/docs/variance)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)