# MonthName

# MonthName

The **MonthName** function returns the name of the month component from a specified datetime value.

## Syntax

```
MonthName(date)
```

Function arguments:

|  |  |
| --- | --- |
| **date** | The value or column to reference when evaluating the month component.   * Must be a datetime value or column containing [date data](/docs/data-types-and-formats#date). |

## Notes

* If the **date** argument references text or number data, use the **[Date](/docs/date)** function to convert the value or column to the [date data type](/docs/data-types-and-formats#date).

## Examples

### Example 1

```
MonthName(Date("2023-05-04"))
```

Evaluates `2023-05-04` as a datetime value and returns `May` as the name of the month component.

### Example 2

```
MonthName([Order Date])
```

References the *Order Date* column and returns the name of the corresponding month component for each row.

![](https://files.readme.io/a4496fa-image.png)

Updated 3 days ago

---

Related resources

* [Month](/docs/month)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Notes](#notes)
  + [Examples](#examples)
  + - [Example 1](#example-1)
    - [Example 2](#example-2)