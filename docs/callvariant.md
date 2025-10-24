# CallVariant

# CallVariant

The **CallVariant** function calls a warehouse function that returns a Variant datatype. This function can be used in the case of string tokenization for cleaning unstructured text data.

## Syntax

```
CallVariant(function name, argument1, argument2, ...)
```

Function arguments:

* **function name** (required): The name of the warehouse function to call.
* **argument** (required): The argument(s) to pass into the warehouse function. Multiple arguments are supported.

## Example

A table contains a *Product Name* column that returns product information as a string. You can pass Snowflake's [STRTOK\_TO\_ARRAY](https://docs.snowflake.com/en/sql-reference/functions/strtok_to_array) function to the **CallVariant** function to tokenize the *Product Name* string by a delimiter and return the tokens in an array.

```
CallVariant("STRTOK_TO_ARRAY", [Product Name], "-")
```

* Returns an array that splits *Product Name* into Product ID, Name, and Color tokens

![](https://files.readme.io/eefc5a0-8.png)

You can use the *CallVariant* column to extract the desired fields for each product into their individual columns for further analysis.

Updated 3 days ago

---

Related resources

* [CallLogical](/docs/calllogical)
* [CallNumber](/docs/callnumber)
* [CallText](/docs/calltext)
* [CallDatetime](/docs/calldatetime)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)