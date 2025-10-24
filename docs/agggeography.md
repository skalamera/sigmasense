# AggGeography

# AggGeography

The **AggGeography** function calls a warehouse aggregate function that returns a Geography data type. This function is the aggregate version of [CallGeography](/docs/callgeography).

You can use the **AggGeography** function on [BigQuery](/docs/connect-to-bigquery), and [Snowflake](/docs/connect-to-snowflake) connections.

## Syntax

```
AggGeography(function_name, arguments...)
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

* [CallGeography](/docs/callgeography)
* [Geography](/docs/geography)
* [Geography functions](/docs/geography-functions)

* [Table of Contents](#)
* + [Syntax](#syntax)