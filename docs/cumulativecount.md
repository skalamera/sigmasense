# CumulativeCount

# CumulativeCount

The **CumulativeCount** function counts the number of non-null values of a column, up and including the current row value.

## Syntax

```
CumulativeCount([Column])
```

Function Arguments:

* **[Column]** (required) - A column of text, numbers or dates to count the number of non-null values up to and including the current row value.

Cumulative functions depend on the order of the given column. If you change the sorting, you change the result.

## Example

```
CumulativeCount([Number of Violations])
```

A table contains data for restaurant inspections by day.  The **CumulativeCount** function can be used to count the amount of days with at least one violation up to and including the current day.

![](https://files.readme.io/ca31e4c-5555.png)

Updated 3 days ago

---

Related resources

* [Count](/docs/count)
* [MovingCount](/docs/movingcount)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)