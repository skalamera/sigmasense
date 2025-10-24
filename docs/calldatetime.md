# CallDatetime

# CallDatetime

The **CallDatetime** function calls a warehouse function that returns a datetime data value. This function is often applied to display a time column or value in different formats that require conversion.

## Syntax

```
CallDatetime(function_name, argument)
```

Function arguments:

|  |  |
| --- | --- |
| **function\_name** | The warehouse function to call. |
| **argument** | One or more arguments to pass to the warehouse function. |

## Example

A table contains a *Daily Total Seconds* column that returns the session time (in seconds) for each customer as a Number type. You can pass Snowflake's [TO\_TIME](https://docs.snowflake.com/en/sql-reference/functions/to_time) function to the **CallDatetime** function to represent the number of seconds as hours, minutes, and seconds.

```
CallDatetime("TO_TIME", Text([Daily Total Seconds]))
```

* Converts the *Daily Total Seconds* column into hours, minutes, and seconds.

> 📘
>
> ### Apply custom formatting to the *CallDatetime* column using %H:%M:%S as the format string to only display the time portion of the timestamp returned by the TO\_TIME function.

![Screen_Shot_2023-04-28_at_3.03.06_PM.png](https://files.readme.io/801e8c9-4.png)

Updated 3 days ago

---

Related resources

* [CallLogical](/docs/calllogical)
* [CallNumber](/docs/callnumber)
* [CallVariant](/docs/callvariant)
* [CallText](/docs/calltext)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)