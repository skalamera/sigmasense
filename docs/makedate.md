# MakeDate

# MakeDate

The **MakeDate** function evaluates specified values representing individual date (year, month, day) and time (hour, minute, second) components and returns a datetime value in ISO format.

## Syntax

```
MakeDate(year, month, day, [hour], [minute], [second])
```

Function arguments:

|  |  |
| --- | --- |
| **year** | (required) An integer representing the year. |
| **month** | (required) An integer representing the month. |
| **day** | (required) An integer representing the day of the month. |
| **hour** | (optional) An integer representing the hour (in the 24-hour format). |
| **minute** | (optional) An integer representing the minutes. |
| **second** | (optional) An integer representing the seconds. |

## Example

```
MakeDate(2019, 1, 31, 16, 30, 00)
```

Returns the datetime value `2019-01-31 16:30:00` (January 31, 2019 4:30 PM).

Updated 3 days ago

---

Related resources

* [DateFromUnix](/docs/datefromunix)
* [Quickstart: Common date functions and use cases](https://quickstarts.sigmacomputing.com/guide/common_date_functions_and_use_cases)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)