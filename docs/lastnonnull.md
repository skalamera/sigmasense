# LastNonNull

# LastNonNull

The **LastNotNull** function returns the last non-Null value in a column or grouping.

**LastNonNull** is either an aggregate function, or a window function. As a window function, it repeats the last non-Null value for every row in the column.

This is similar to the [Last](/docs/last) function, but excludes Null values.

Data sort order is important when using this function: Sigma applies sorting and filtering before the function. Your CDW determines the default sort order.

## Syntax

```
LastNonNull([Column])
```

The function has the following argument:

Column
:   The column input
:   Accepts all data types

## Examples

### Window function example

```
LastNonNull([Delivery Date])
```

Here the calculation references a column in a lower grouping level. This example shows the oldest non-null date from the **Delivery Date** column for each grouping under the **Order Number** column.

**Delivery Date** is in descending order sort. If **Delivery Date** is in ascending sort, the function returns the most recent non-Null date for each grouping.

![](https://files.readme.io/45fbc2f-LastNonNullExample1.png)

### Aggregate function example

```
LastNonNull([Delivery Date])
```

Here the calculation references a column in the same grouping level, so the first non-Null value  returns for every row.

Note how the resulting calculations depend on the group’s sort order. The sort on the **Product Family** affects the order of the **Delivery Date** column.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Functions/lastnonnullexample+%232.png)

Updated 3 days ago

---

Related resources

* [Last](/docs/last)
* [FirstNonNull](/docs/firstnonnull)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Examples](#examples)
  + - [Window function example](#window-function-example)
    - [Aggregate function example](#aggregate-function-example)