# Year

# Year

The **Year** function returns an integer representing the year component of a specified date and time.

## Syntax

```
Year(date, [timezone])
```

Function arguments:

|  |  |
| --- | --- |
| **date** | The date or column containing date values from which the year component is extracted. |
| **timezone** | [optional] The [IANA time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (e.g., `“America/Los_Angeles”`) to convert the date value to before extracting the year component. When the **timezone** argument is omitted, the input date is evaluated in UTC time. |

> 💡
>
> To learn how to create and use custom fiscal periods in Sigma, see [How to create custom fiscal year and fiscal quarters](https://community.sigmacomputing.com/t/how-to-create-custom-fiscal-year-and-fiscal-quarters/2613).

## Example

```
Year(Date("2007-08-14"))
```

Extracts the year component from the specified date (August 14, 2007) and returns `2007` to represent the year.

Updated 3 days ago

---

Related resources

* [DatePart](/docs/datepart)
* [Second](/docs/second)
* [Minute](/docs/minute)
* [Month](/docs/month)
* [Quarter](/docs/quarter)
* [Quickstart: Common date functions and use cases](https://quickstarts.sigmacomputing.com/guide/common_date_functions_and_use_cases)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)