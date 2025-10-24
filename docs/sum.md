# Sum

# Sum

The **Sum** function adds the numerical values in a column or group.

> 📘
>
> ### This function must be used with aggregated data in a grouped table. For a detailed video walkthrough that uses this function, see [Using aggregate functions with groupings](https://www.sigmacomputing.com/resources/training-videos/table-grouping-and-functions#aggregate-functions).

## Syntax

`Sum(column)`

Function arguments:

* **column** (required) - The column of numbers to add together. Any Null or empty values are skipped.

## Example

```
Sum([Price]) - Sum([Cost])
```

* Finds the total Profit by finding the sum of the Prices and subtracting the sum of the Costs.

> 📘
>
> When performing [numeric operations](/docs/operators-overview) on values, such as using the addition operator + to sum together values, if one value is Null then the result of the entire numeric operation will be Null.

Updated 3 days ago

---

Related resources

* [SumIf](/docs/sumif)
* [MovingSum](/docs/movingsum)
* [CumulativeSum](/docs/cumulativesum)
* [SumProduct](/docs/sumproduct)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)