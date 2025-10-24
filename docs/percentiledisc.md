# PercentileDisc

# PercentileDisc

The **PercentileDisc** function calculates the discrete kth percentile value for a column or group. It returns the percent of the total frequency under that number, demonstrating the relative position of the value compared to the entire set of data. You can use the **PercentileDisc** function on [BigQuery](/docs/connect-to-bigquery), [PostgreSQL](/docs/connect-to-postgresql), [Databricks](/docs/connect-to-databricks), [Snowflake](/docs/connect-to-snowflake), [Redshift](/docs/connect-to-redshift), [MySQL](/docs/connect-to-mysql), and [AlloyDB](/docs/connect-to-alloydb) connections.

## Syntax

`PercentileDisc(column, k)`

The function has the following arguments:

column
:   Required
:   The column to search.

k
:   Required
:   A number between `0` and `1`, which corresponds to the percent of data below that number.
:   `0 < k < 1`

## Example

A *Score* column contains values 2, 4, 6, 8, and 10.

```
PercentileDisc([Score], 0.7)
```

* The discrete 70th percentile of the *Score* column is 8. If a candidate scores in the 70th percentile, they have scored higher than 70% of test takers, putting them in the top 30%

Updated 3 days ago

---

Related resources

* [PercentileCont](/docs/percentilecont)
* [Avg](/docs/avg)
* [Median](/docs/median)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)