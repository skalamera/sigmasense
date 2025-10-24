# DateAdd

# DateAdd

The **DateAdd** function adds a specified amount of time to a date.

## Syntax

```
DateAdd(unit, amount, date)
```

Function arguments:

|  |  |
| --- | --- |
| **unit** | (required) The unit of time to add (i.e., year, quarter, month, week, day, hour, minute, or second). |
| **amount** | (required) The number of units to add. |
| **date** | (required) The date value or column of date values to which the function adds time. |

> 📘
>
> ### When the **amount** argument is a decimal value, the function rounds the input to the nearest integer.

## Examples

```
DateAdd("minute", 60, Date("1999-12-31 23:00:00"))
```

Adds 60 minutes to the specified date and returns `2000-01-01 00:00:00`.

```
DateAdd(“day”, 7, [Date])
```

Adds seven days to every date in the *Date* column.

```
DateAdd(“year”, -1, [Date])
```

Subtracts one year from every date in the *Date* column.

Updated 3 days ago

---

Related resources

* [Sigma Quickstart: Common date functions and use cases](https://quickstarts.sigmacomputing.com/guide/common_date_functions_and_use_cases)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Examples](#examples)