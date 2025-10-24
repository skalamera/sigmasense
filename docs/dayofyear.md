# DayOfYear

# DayOfYear

Converts a date to the number day of the year, from 1 (Jan 1) to 365 (Dec 31). Accounts for leap years.

## Syntax

```
DayOfYear(date, [timezone])
```

### Function arguments:

|  |  |
| --- | --- |
| **date** | (required) The date or column of date values to evaluate. |
| **timezone** | (optional) The [IANA timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) to get the day number for. If not specified, the date argument is treated as local time. |

## Examples

```
DayOfYear(Date("2023-01-01"))
```

Converts Jan 1, 2023 to the number day of the year, and returns `1`.

```
DayOfYear(Date("2023-12-31"))
```

Converts Dec 31, 2023 to the number day of the year, and returns `365`.

```
DayOfYear(Date("2023-03-01"))
```

Converts Mar 1, 2023 to the number day of the year, and returns `60`.

### Leap Year Examples

```
DayOfYear(Date("2024-12-31"))
```

Converts Dec 31, 2024 to the number day of the year, and returns `366`.

```
DayOfYear(Date("2024-03-01"))
```

Converts Mar 1, 2024 to the number day of the year, and returns `61`.

### Timezone Examples

```
DayOfYear(Date("2023-01-03 02:00:00Z"), "America/New_York")
```

Converts Jan 1, 2023 16:00:00Z to the number day of the year in New York, and returns `2`

```
DayOfYear(Date("2023-01-03 02:00:00Z"), "Australia/Sydney")
```

Converts Jan 3, 2023 02:00:00Z to the number day of the year in Sydney, and returns `3`

```
DayOfYear(Date("2023-01-15 18:00:00Z"), "Asia/Seoul")
```

Converts Jan 15, 2023 18:00:00Z to the number day of the year in Seoul, and returns `16`

```
DayOfYear(Date("2023-01-01 03:00:00Z"), "America/Los_Angeles")
```

Converts Jan 1, 2023 03:00:00Z to the number day of the year in Los Angeles, and returns `365`

Updated 3 days ago

---

[Day](/docs/day)[EndOfMonth](/docs/endofmonth)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + - [Function arguments:](#function-arguments)
  + [Examples](#examples)
  + - [Leap Year Examples](#leap-year-examples)
    - [Timezone Examples](#timezone-examples)