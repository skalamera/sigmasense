# Minute

# Minute

The **Minute** function returns an integer representing the minute component of a specified date and time.

## Syntax

```
Minute(date, [timezone])
```

Function arguments:

* **date** (required) - the date or column containing date values from which the minute component is extracted
* **timezone** (optional) - the [IANA time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (e.g., `“America/Los_Angeles”`) to convert the date value to before extracting the minute component

> 📘
>
> When the **timezone** argument is omitted, the input date is evaluated in UTC time.

## Example

```
Minute(Date("2007-08-14 07:11:00"))
```

Extracts the minute component from the specified date and time and returns `11` to represent the eleventh minute of the hour.

Updated 3 days ago

---

Related resources

* [DatePart](/docs/datepart)
* [Second](/docs/second)
* [Month](/docs/month)
* [Quarter](/docs/quarter)
* [Year](/docs/year)
* [Quickstart: Common date functions and use cases](https://quickstarts.sigmacomputing.com/guide/common_date_functions_and_use_cases)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)