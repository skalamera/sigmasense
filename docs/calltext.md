# CallText

# CallText

The **CallText** function sends a request to execute a warehouse function that returns a text value. This is often used to extract and display numbers in a more readable format or to join digits with text or symbols.

## Syntax

```
CallText(function_name, argument)
```

Function arguments:

|  |  |
| --- | --- |
| **function name** | The warehouse function to call. |
| **argument** | One or more arguments to pass to the warehouse function. |

> 🚧
>
> ### All arguments must meet the warehouse function’s input requirements. Unsupported arguments result in an invalid formula.

## Example

A table contains a *Revenue* column that provides restaurant revenue data as a number value. Using the **CallText** function, you can execute Snowflake's [TO\_CHAR](https://docs.snowflake.com/en/sql-reference/functions/to_char) function to extract digits and preserve the number format when combining *Revenue* and *Currency* values into a single text string.

```
Concat("$", CallText("TO_CHAR", [Revenue], "999,999,999,999.00"), " ", [Currency])
```

Returns the *Revenue* value as a text string and preserves the number format (999,999.999.00) upon text conversion.

![Screenshot_2023-04-21_at_10.34.01_AM.png](https://files.readme.io/cebd220-7.png)

Updated 3 days ago

---

Related resources

* [CallLogical](/docs/calllogical)
* [CallNumber](/docs/callnumber)
* [CallVariant](/docs/callvariant)
* [CallDatetime](/docs/calldatetime)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)