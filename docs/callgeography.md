# CallGeography

# CallGeography

The **CallGeography** function calls a warehouse function that returns a Geography data type.

You can use the **Geography** function on [Snowflake](/docs/connect-to-snowflake) and [BigQuery](/docs/connect-to-bigquery) connections.

**CallGeography** is one of Sigma's [Passthrough functions](/docs/passthrough-functions-overview).

## Syntax

```
CallGeography(function_name, argument1, ...)
```

The function has these arguments:

function\_name
:   Required
:   The name of the warehouse function that Sigma invokes

argument1 ...
:   Optional
:   The arguments of the invoked function
:   Functions may have `0` or more arguments

Updated 3 days ago

---

Related resources

* [AggGeography](/docs/agggeography)
* [Geography](/docs/geography)
* [Geography functions](/docs/geography-functions)

* [Table of Contents](#)
* + [Syntax](#syntax)