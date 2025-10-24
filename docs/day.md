# Day

# Day

Returns the day of the month of a date value as a number.

## Usage

```
Day(date, [timezone])
```

**date** (required) The date from which to extract the day component.

**timezone** (optional) Name of [IANA time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) to get the date part at (*e.g.,* “America/Los\_Angeles”). When calculating a time zone, input dates are treated as UTC.

## Example

```
Day(Date("2007-08-14"))
```

* Returns 14.

```
Day([Date])
```

* Returns the day of the month of each date value in the `[Date]` column as a number.

Updated 3 days ago

---

Related resources

* [DatePart](/docs/datepart)
* [Quickstart: Common date functions and use cases](https://quickstarts.sigmacomputing.com/guide/common_date_functions_and_use_cases)

* [Table of Contents](#)
* + [Usage](#usage)
  + [Example](#example)