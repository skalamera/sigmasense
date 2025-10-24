# AggLogical

# AggLogical

The **AggLogical** function calls a warehouse aggregate function that returns a Logical data type. This function is the aggregation version of [CallLogical](/docs/calllogical) and can be applied to evaluate array objects for analysis without traversing through the contents of an array.

## Syntax

```
AggLogical(function name, arguments...)
```

Function arguments:

* **function name** (required)- The name of an aggregate function supported by your data warehouse.
* **arguments** (required)- One or more arguments to be passed to the warehouse function. All arguments must meet the warehouse function’s input requirements.

## Example

A table contains a *Today SKU* column that returns an array of top SKU Numbers for each store and a LW Today SKU column that returns an array of top SKU Numbers from the previous week. The *CallLogical* column returns True if *Today SKU* and *LW Today SKU* arrays have at least one SKU Number in common.

You can pass Snowflake's [BOOLAND\_AGG](https://docs.snowflake.com/en/sql-reference/functions/booland_agg) function to the **AggLogical** function to check whether ***all*** stores in the West region had at least one high demand SKU Number from the previous week.

Similarly, Snowflake's [BOOLOR\_AGG](https://docs.snowflake.com/en/sql-reference/functions/boolor_agg)/[BOOLXOR\_AGG](https://docs.snowflake.com/en/sql-reference/functions/boolxor_agg) function can be used to check whether ***any*** store or ***exactly*** one store in the West region had at least one high demand SKU Number from the previous week.

```
AggLogical("BOOLAND_AGG", [CallLogical])
```

* Returns True if *all* values in the *CallLogical* column evaluate to True.

```
AggLogical("BOOLOR_AGG", [CallLogical])
```

* Returns True if *at least* one value in the *CallLogical* column evaluate to True.

```
AggLogical("BOOLXOR_AGG", [CallLogical])
```

* Returns True if *exactly* one value in the *CallLogical* column evaluate to True.

![](https://files.readme.io/229c4de-Screen_Shot_2023-04-28_at_2.36.06_PM.png)

Updated 3 days ago

---

Related resources

* [CallLogical](/docs/calllogical)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)