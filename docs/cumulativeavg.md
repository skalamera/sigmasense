# CumulativeAvg

# CumulativeAvg

The **CumulativeAvg** function calculates the numerical average of the input column up to and including the current value.

## Syntax

```
CumulativeAvg([Column])
```

Function Arguments:

* **[Column]** (required) - The column of numbers to evaluate the cumulative average.

> 📘
>
> Cumulative functions depend on the order of the given column. If you change the sorting you will change the result.

## Example

```
CumulativeAvg([Monthly Revenue])
```

A table contains the monthly revenue of a store.  The **CumulativeAvg** function can be used to find the average up to and including the current value.

Updated 3 days ago

---

Related resources

* [Avg](/docs/avg)
* [MovingAvg](/docs/movingavg)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)