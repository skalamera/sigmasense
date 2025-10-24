# Count

# Count

The **Count** function returns the number of non-Null and non-empty values within a column or group.

## Syntax

`Count([Field])`

Arguments:

* **Field** (optional) The column of values to be counted. Null values are skipped.
  + If not supplied, `Count()` returns the number of rows in a table.

## Examples

`Count()`

* Counts number of rows in a table.

`Count([Funding Total Usd])`

* Counts number of companies with a disclosed funding total.

Updated 3 days ago

---

Related resources

* [CumulativeCount](/docs/cumulativecount)
* [MovingCount](/docs/movingcount)
* [CountIf](/docs/countif)
* [CountDistinct](/docs/countdistinct)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Examples](#examples)