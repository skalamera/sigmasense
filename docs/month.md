# Month

# Month

The **Month** function returns an integer representing the month component of a specified date and time.

## Syntax

```
Month(date, [timezone])
```

The Month function has the following arguments:

date
:   Required
:   The date or the column that contains date values where Sigma extracts the month component

timezone
:   Optional
:   The [IANA time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones); for example, (e.g., `“America/Los_Angeles”`, used to convert the date value before extracting the month component.
:   When omitted, **timezone** Sigma evaluates the date in UTC time.

## Examples

```
Month(Date("2007-08-14"))
```

Extracts the month component from the specified date (August 14, 2007) and returns `8` to represent the eighth month of the year.

```
Month([Date])
```

The **Month** function returns the following values for the **Date** column:

![](https://files.readme.io/535a2fe-function-month-example.png)

Updated 3 days ago

---

Related resources

* [MonthName](/docs/monthname)
* [DatePart](/docs/datepart)
* [Second](/docs/second)
* [Minute](/docs/minute)
* [Quarter](/docs/quarter)
* [Year](/docs/year)
* [Quickstart: Common date functions and use cases](https://quickstarts.sigmacomputing.com/guide/common_date_functions_and_use_cases)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Examples](#examples)