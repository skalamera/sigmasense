# Hour

# Hour

Returns the hour component of the given Date as a number.

## Usage

`Hour(date, [timezone])`

**date** (required) The Date from which to extract the hour component.

**timezone** (optional) Name of [IANA time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) to get the date part at (*e.g.,* “America/Los\_Angeles”). When calculating a time zone, input dates are treated as UTC.

## Example

```
Hour(Date("2007-08-14 07:11:00"))
```

* Returns 7.

Updated 3 days ago

---

Related resources

* [DatePart](/docs/datepart)
* [Quickstart: Common date functions and use cases](https://quickstarts.sigmacomputing.com/guide/common_date_functions_and_use_cases)

* [Table of Contents](#)
* + [Usage](#usage)
  + [Example](#example)