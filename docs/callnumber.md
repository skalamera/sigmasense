# CallNumber

# CallNumber

The **CallNumber** function calls a warehouse function that returns a Number datatype. This function can be used in the case of generating random samples of data for analysis.

## Syntax

`CallNumber(function name, argument1, argument2, ...)`

Function arguments:

* **function name** (required): The name of the warehouse function to call.
* **argument** (required): The argument(s) to pass into the warehouse function. Multiple arguments are supported.

## Example

A table contains a Cust Key column that serves as the unique identifier for each customer. You can pass Snowflake's [UNIFORM](https://docs.snowflake.com/en/sql-reference/functions/uniform) function to the **CallNumber** function to generate a uniformly distributed set of random numbers when creating a filter column *Flag* to randomly select *n* number of customers.

`CallNumber("uniform", 1, 10, CallNumber("random"))`

* Return a list of random generated numbers between 1-10 to map to each customer.

Snowflake's [RANDOM](https://docs.snowflake.com/en/sql-reference/functions/random) function is used as the **`<gen>`** argument of the UNIFORM function to generate a list of pseudo-random 64-bit integers within the specified range.

![](https://files.readme.io/ed7f32d-6.png)

Updated 3 days ago

---

Related resources

* [CallLogical](/docs/calllogical)
* [CallVariant](/docs/callvariant)
* [CallText](/docs/calltext)
* [CallDatetime](/docs/calldatetime)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)