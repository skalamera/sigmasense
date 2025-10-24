# AggVariant

# AggVariant

The **AggVariant** function calls a warehouse aggregate function that returns a Variant data type. This function is the aggregate version of [CallVariant](/docs/callvariant) and can be applied to identify distinct values from a lower grouped level in the parent/higher level grouping of a table.

## Syntax

```
AggVariant(function name, arguments...)
```

Function arguments**:**

* **function name** (required): The name of an aggregate function supported by your data warehouse.
* **arguments** (required): One or more arguments to be passed to the warehouse function. All arguments must meet the warehouse function’s input requirements.

## Example

A table contains an `ARRAY_UNIQUE_AGG` column that returns an array containing all the distinct customers who purchased at least one or more items per *Product Type*. You can pass Snowflake's [ARRAY\_UNION\_AGG](https://docs.snowflake.com/en/sql-reference/functions/array_union_agg) function to the **AggVariant** function to identify all distinct customers who made at least one purchase that week.

> 📘
>
> The `ARRAY_UNION_AGG` function takes in one column containing the arrays with distinct values as produced by Snowflake's [ARRAY\_UNIQUE\_AGG](https://docs.snowflake.com/en/sql-reference/functions/array_unique_agg) function.

```
AggVariant("ARRAY_UNION_AGG", [ARRAY_UNIQUE_AGG])
```

* Return an array that contains the union of distinct customers from the input arrays in the `ARRAY_UNIQUE_AGG` column.

![](https://files.readme.io/6e5114f-3.png)

Updated 3 days ago

---

Related resources

* [CallVariant](/docs/callvariant)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)