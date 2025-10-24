# DateFromUnix

# DateFromUnix

Convert a Unix timestamp to a Date data type.

> 📘
>
> ### The UNIX timestamp is the number of seconds (or milliseconds) elapsed since an absolute point in time, midnight of Jan 1 1970 in UTC time. (UTC is Greenwich Mean Time without Daylight Savings time adjustments.) Regardless of your time zone, the UNIX timestamp represents a moment that is the same everywhere.

## Usage

`DateFromUnix(number)`

**number** (required) A number or column of numbers, each of which represent a Unix-style timestamp.

> 📘
>
> When you enter a number, the [Date](/docs/date) function behaves the same as DateFromUnix.

## Examples

`DateFromUnix(0)`

* Returns 1970-01-01 00:00:00

`DateFromUnix(1503724894)`

* Returns 2017-08-26 05:21:34

Updated 3 days ago

---

Related resources

* [Date](/docs/date)
* [Quickstart: Common date functions and use cases](https://quickstarts.sigmacomputing.com/guide/common_date_functions_and_use_cases)

* [Table of Contents](#)
* + [Usage](#usage)
  + [Examples](#examples)