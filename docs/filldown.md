# FillDown

# FillDown

The **FillDown** function replaces all null values within a column with the closest, prior non-null value.

## Syntax

```
FillDown([Column])
```

Function Arguments:

* **Column** (required) The column to apply the fill down.

The results for this function can change if the workbook is refreshed and there is no sort applied to the table. The sort will change upon refresh.

## Example

```
FillDown([Date])
```

A table contains various dates.  The **FillDown** function will replace every null value within the `[Date]` column with the most recent non-null value.

![](https://files.readme.io/c058a19-7.png)

Updated 3 days ago

---

Related resources

* [Nth](/docs/nth)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)