# ConvertTimezone

# ConvertTimezone

The **ConvertTimezone** function converts datetime values to the specified time zone.

## Syntax

```
ConvertTimezone(date, timezone, [from_timezone])
```

Function arguments:

|  |  |
| --- | --- |
| **date** | (required) The datetime value to convert. |
| **timezone** | (required) The TZ identifier of the IANA time zone *to* which the datetime value is converted. See [List of TZ database timezones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) for reference. |
| **from\_timezone** | (optional) The TZ identifier of the IANA time zone *from* which the datetime value is converted.  Defaults to the organization account time zone when the argument is unspecified. |

## Examples

```
ConvertTimezone([Date], "America/Los_Angeles")
```

Interprets values in the *Date* column as datetime values in the organization [account time zone](/docs/account-time-zone), then converts them to the equivalent datetime values in America/Los\_Angeles (Pacific) time.

```
ConvertTimezone(Date("2014-07-18 10:58:00"), "America/Los_Angeles", "America/New_York")
```

Interprets `2014-07-18 10:58:00` in America/New\_York (Eastern) time and converts it to `2014-07-18 07:58:00` in America/Los\_Angeles (Pacific) time.

Updated 3 days ago

---

Related resources

* [Date](/docs/date)
* [DateParse](/docs/dateparse)
* [DateTime](/docs/datetime)
* [Quickstart: Common date functions and use cases](https://quickstarts.sigmacomputing.com/guide/common_date_functions_and_use_cases)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Examples](#examples)