# Quarter

# Quarter

The **Quarter** function returns an integer representing the quarter in which a specified date and time occurs.

## Syntax

```
Quarter(date)
```

Function arguments:

|  |  |
| --- | --- |
| **date** | The date or column containing date values from which the quarter component is determined. |

> 💡
>
> Sigma evaluates quarters based on the calendar year. The first quarter begins January 1, the second quarter begins April 1, the third quarter begins July 1, and the fourth quarter begins October 1. To learn how to create and use custom fiscal periods in Sigma, see [How to create custom fiscal year and fiscal quarters](https://community.sigmacomputing.com/t/how-to-create-custom-fiscal-year-and-fiscal-quarters/2613).

## Example

```
Quarter([Date])
```

Evaluates the month and day of each value in the *Date* column and returns an integer representing the quarter in which each date occurs.

```
Quarter(Date("2007-08-14 07:11:05"))
```

Evaluates the month and day of the specified date (August 14, 2007) and returns `3` to represent the third quarter of the calendar year.

Updated 3 days ago

---

Related resources

* [DatePart](/docs/datepart)
* [Second](/docs/second)
* [Minute](/docs/minute)
* [Month](/docs/month)
* [Year](/docs/year)
* [Quickstart: Common date functions and use cases](https://quickstarts.sigmacomputing.com/guide/common_date_functions_and_use_cases)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)