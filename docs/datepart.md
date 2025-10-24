# DatePart

# DatePart

The **DatePart** function extracts the specified date part from a date value.

Sigma returns the result(s) in your organization's time zone. This may cause days, months, or years to appear offset, if the specified time zone is ahead of the organization's time zone. To view the output presented in the specified time zone, apply the [ConvertTimezone](/docs/converttimezone) function.

**DatePart** is one of Sigma's [Date functions](/docs/date-functions-overview).

## Syntax

`DatePart(precision, date, [timezone])`

The function has the following arguments:

|  |  |
| --- | --- |
| **precision** | Required   The date part extracted. Can be one of “year”, "quarter", “month”, “week”, “day”, "weekday", "day\_of\_year", “hour”, “minute”, “second”, “millisecond”, or "epoch". |
| **date** | Required   Date or column of dates where Sigma extracts the date part.   The value must be a date. If the column is not in the appropriate format, use the [Date](/docs/date) function on the argument. |
| **timezone** | Optional   TZ identifier of the [IANA time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) for the date part. For example, ”America/Los\_Angeles”. If omitted, defaults to UTC. |

## Examples

`DatePart("year", [Invoice Date])`

Extracts the year from each value in the column of invoice dates.

`DatePart("week", Date("2007-01-10 10:00:00"))`

Returns 2, the week number of this date; weeks in Sigma start on Sunday, by default.

```
DatePart("year", [Date])
DatePart("quarter", [Date])
DatePart("month", [Date])
DatePart("week", [Date])
DatePart("day", [Date])
DatePart("weekday", [Date])
DatePart("day_of_year", [Date])
```

Based on the formulas above, the **DatePart** function returns the following values for the **Date** column:

![Table with a Date column, Year of Date, Quarter of Date, Month of Date, Week of Date, Day of Date, and Weekday of Date columns extracted.](https://files.readme.io/795b9947c78075faf2ea9247ffc9767c08b65d2aebfd52634c6dc205ba3c7320-Screenshot_2025-06-11_at_9.43.02_AM.png)

Note that in the `precision` argument, `day` returns the day of the month (1-31), `weekday` returns the day of the week (1-7, beginning on Sunday), and `day_of_year` returns the day of the year (1-366, accounting for leap years).

```
DatePart("year", [Date])
DatePart("hour", [Date])
DatePart("minute", [Date])
DatePart("second", [Date])
DatePart("millisecond", [Date])
DatePart("epoch", [Date])
```

Based on the formulas above, the **DatePart** function returns the following values for the **Date** column:

![](https://files.readme.io/e7e148c3c9e0412a2e9a2c954ca79c5846204b435d088c76d10683dc4b1279f7-Screenshot_2025-06-11_at_9.54.41_AM.png)

Note that in the `precision` argument, `epoch` refers to the [Unix epoch.](https://en.wikipedia.org/wiki/Unix_time)

Updated 3 days ago

---

Related resources

* [ConvertTimezone](/docs/converttimezone)
* [Date](/docs/date)
* [List of tz database time zones in Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
* [Quickstart: Common date functions and use cases](https://quickstarts.sigmacomputing.com/guide/common_date_functions_and_use_cases)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Examples](#examples)