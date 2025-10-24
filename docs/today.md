# Today

# Today

The **Today** function returns the current date in ISO format and presents it in your [Account Time Zone](/docs/account-time-zone).

## Syntax

```
Today()
```

> 📘
>
> The **Today** function doesn't reference arguments. Use it independently to generate the current date, or in another function to reference the current date.

## Examples

```
Today()
```

Returns the date of the moment the function was submitted or the last time the data was refreshed.

```
DateDiff(“day”, [Invoice Date], Today())
```

Returns the number of days between the date in the *Invoice Date* column and the current date based on the moment the function was submitted or the last time the data was refreshed.

```
DateAdd(“day”, -1, Today())
```

Returns the previous day's date relative to the date of the moment the function was submitted or the last time the data was refreshed.

Updated 3 days ago

---

Related resources

* [Now](/docs/now)
* [ConvertTimezone](/docs/converttimezone)
* [Quickstart: Common date functions and use cases](https://quickstarts.sigmacomputing.com/guide/common_date_functions_and_use_cases)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Examples](#examples)