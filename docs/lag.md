# Lag

# Lag

The **Lag** function accesses data in preceding rows in the same result set, without having to join the table to itself. It references a column and returns its values in the offset position, shifting the output down by a fixed number of rows.

The **Lag** function typically shifts values down, while the [Lead](/docs/lead) function shifts values up.

## Syntax

```
Lag(value, offset, default)
```

These are the function arguments:

value
:   Required
:   The column of values that the function shifts

offset
:   Optional
:   The number of rows that the output shifts
:   This number must be constant (the same) for all rows
:   Must be an integer greater than `0`
:   Default, if omitted, is `1`

default
:   Optional
:   The value to return in the row(s) at the end of the table, which don't have a valid offset index
:   Default, if omitted, is `Null`

## Examples

TextText

```
Lag([Year of Date])
```

```
Lag([Year of Date],2)
```

In these examples, column **Lag** shows the [offset](/docs/lag#offset) lag as the default of 1 row and the [default](/docs/lag) is null, while column Lag 2 shows the [offset](/docs/lag#offset) lag as 2 rows and the [default](/docs/lag#default) is null.

![Default options for the Lag function](https://files.readme.io/885e5fb-t1.png)

```
Lag([Attendance], 1)
```

A table lists the total attendance for each game of an MLB team's 2021 season. You can use the **Lag** function to compare this value with the number of attendees recorded for the previous game.

The formula references the *Attendance* column and shifts its values down one row. The resulting output in each row of the *Previous Game* column indicates the number of people who attended the game that occurred immediately before the one referenced in the *Game Key* column.

![](https://files.readme.io/f784d6a-t2.png)

Updated 3 days ago

---

Related resources

* [Lead](/docs/lead)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Examples](#examples)