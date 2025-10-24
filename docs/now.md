# Now

# Now

The **Now** function returns the current date and time and presents it in your [Account Time Zone](/docs/account-time-zone).

## Syntax

```
Now()
```

> 📘
>
> ### The **Now** function doesn't reference arguments. It can be used independently to generate the current date and time, or it can be used within another function to reference the current date and time.

## Examples

```
Now()
```

Returns the date and time of the moment the function was submitted or the last time the data was refreshed.

```
DateDiff(“minute”, [Invoice Date], Now())
```

Returns number of minutes between the date in the *Invoice Date* column based on the moment the function was submitted or the last time the data was refreshed.

Updated 3 days ago

---

Related resources

* [Today](/docs/today)
* [Quickstart: Common date functions and use cases](https://quickstarts.sigmacomputing.com/guide/common_date_functions_and_use_cases)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Examples](#examples)