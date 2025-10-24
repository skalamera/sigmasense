# EndOfMonth

# EndOfMonth

Returns the last day of the month of a Date value.

## Usage

`EndOfMonth(date)`

**date** (required) The date from which the end of month is to be computed.

## Example

Extract the last day of the month from the [Invoice Date] column:

```
EndOfMonth([Invoice Date])
```

![](https://files.readme.io/30861f6-Screen_Shot_2020-07-30_at_12.29.26_PM.png)

```
EndOfMonth(Date("2023-03-07"))
```

* Returns 2023-03-31 23:59:59.

Updated 3 days ago

---

Related resources

* [LastDay](/docs/lastday)
* [Quickstart: Common date functions and use cases](https://quickstarts.sigmacomputing.com/guide/common_date_functions_and_use_cases)

* [Table of Contents](#)
* + [Usage](#usage)
  + [Example](#example)