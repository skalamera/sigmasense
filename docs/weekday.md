# Weekday

# Weekday

The **Weekday** function evaluates a specified date and returns an integer representing the day of the week (with `1` representing Sunday, `2` representing Monday, `3` representing Tuesday, and so on).

## Syntax

```
Weekday(date, [timezone])
```

Function arguments:

* **date** (required) - the date or column containing date values from which the weekday is determined
* **timezone** (optional) - the [IANA time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (e.g., “America/Los\_Angeles”) to convert the date value to before evaluating the weekday

## Example

```
Weekday(Date("2017-12-01"))
```

Evaluates the specified date (December 1, 2017) to determine the day of the week and returns `6` to represent Friday, the sixth day of the week.

Updated 3 days ago

---

Related resources

* [DatePart](/docs/datepart)
* [Sigma Quickstart: Common date functions and use cases](https://quickstarts.sigmacomputing.com/guide/common_date_functions_and_use_cases)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)