# CallLogical

# CallLogical

The **CallLogical** function calls a warehouse function that returns a Logical datatype. This function if often applied to perform array comparison, creation, and manipulation for analysis.

## Syntax

```
CallLogical(function name, argument1, argument2, ...)
```

Function arguments:

* **function name** (required): The name of the warehouse function to call.
* **argument** (required): The argument(s) to pass into the warehouse function. Multiple arguments are supported.

## Example

A table contains a *Today SKU* column that returns an array of top SKU Numbers for each store and a LW Today SKU column that returns an array of top SKU Numbers from the previous week. You can pass Snowflake's [ARRAYS\_OVERLAP](https://docs.snowflake.com/en/sql-reference/functions/arrays_overlap) function to the **CallLogical** function to compare whether each store has at least one high demand SKU Number from the previous week.

```
CallLogical("ARRAYS_OVERLAP", [LW Today SKU], [Today SKU])
```

* Return True if *Today SKU* and *LW Today SKU* arrays have at least one SKU Number in common.

![](https://files.readme.io/b03c5d4-5.png)

Updated 3 days ago

---

Related resources

* [CallNumber](/docs/callnumber)
* [CallVariant](/docs/callvariant)
* [CallText](/docs/calltext)
* [CallDatetime](/docs/calldatetime)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)