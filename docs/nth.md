# Nth

# Nth

The **Nth** function repeats the Nth value of the the given column for every row in a column.

## Syntax

`Nth([Column], n)`

Function Arguments:

* **[Column]** (required) - A column of text, numbers, or dates to analyze.
* **n** (required) - Offset from top of column. Must be a constant integer greater than 0.

> 🚩
>
> ### When there is no sort specified on the table, the results for this function can change if you refresh the workbook. The sort is different upon refresh.

## Example

`Nth([Quarter], 2)`

Returns the 2nd result in the [Quarter] column for every row in the [Nth] column.

![Table with a Quarter column with rows of Q1, Q2, Q3, and Q4. The Nth column lists Q2 as the value for all rows.](https://files.readme.io/cc2ab6f-9.png)

Updated 3 days ago

---

Related resources

* [First](/docs/first)
* [Last](/docs/last)
* [FillDown](/docs/filldown)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)