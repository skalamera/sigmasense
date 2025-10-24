# DateTrunc

# DateTrunc

Truncates the date to the specified date part.

## Usage

```
DateTrunc(precision, date, [timezone])
```

**precision** (required) Smallest date part to preserve, chosen from “year”, "quarter", “month”, “week”, "week\_starting\_sunday", "week\_starting\_monday", “day”, “hour”, “minute”, and “second”. If "week" is selected, DateTrunc will have weeks start on Sunday. Parameters can be used to specify precision.

**date** (required) Date to be truncated.

**timezone** (optional) Name of [IANA time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) to get the date part at, e.g.”America/Los\_Angeles”. When calculating a time zone, input dates are treated as UTC.

> 📘
>
> The output returned is presented in the organization's time zone. This may cause days, months, or years to appear offset if the specified time zone is ahead of the organization time zone. To view the output presented in the specified time zone, you can apply [ConvertTimezone](/docs/converttimezone) to it.

## Example

```
DateTrunc("hour", Date("1980-05-22 8:45:30"))
```

* Returns 1980-05-22 8:00:00, discarding the “minute” and”second” components of the date.

```
DateTrunc("day", Date("1980-05-22 8:45:30"))
```

* Returns 1980-05-22 00:00:00, discarding the time components of the date.

Updated 3 days ago

---

Related resources

* [Quickstart: Common date functions and use cases](https://quickstarts.sigmacomputing.com/guide/common_date_functions_and_use_cases)

* [Table of Contents](#)
* + [Usage](#usage)
  + [Example](#example)