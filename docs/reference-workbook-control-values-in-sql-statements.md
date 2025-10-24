# Reference workbook control values in SQL statements

# Reference workbook control values in SQL statements

When you [write SQL statements in Sigma](/docs/write-custom-sql), you can reference the value of a control in your SQL statement by wrapping the control ID in curly brackets:

`{{my-control-id}}`

You can find the control ID in the **Settings** tab for a control. For more details about control IDs, see [Reference control values in a formula](/docs/parameters-in-workbooks).

The exact syntax depends on the output type of the control:

* [Single value](#reference-single-value-control-output-in-sql) (Most control types)
* [Min/max values](#reference-number-range-or-range-slider-control-values-in-sql) (Number range or range slider)
* [Start/end values](#reference-date-range-control-values-in-sql) (Date range control)
* [Multiple values](#reference-multiple-values-from-a-multi-select-list-in-sql) (Multi-select list control)

## Limitations and warnings

* If changing the value of a control results in a statement that queries a table with a different schema, the query produces different columns than expected, resulting in errors.

## Reference single value control output in SQL

You can reference the selected or specified value in a specific control (the output) in a SQL statement. For a control that outputs a single value, use the syntax as follows.

### Supported control types

* Single select list
* Text input
* Text area
* Number input
* Date
* Segmented
* Drilldown
* Slider
* Checkbox
* Switch
* Top N

### Syntax

To reference the control value in a formula, enclose the control ID in double curly brackets and use the following syntax:  
`{{New-Control-ID}}`

## Reference number range or range slider control values in SQL

You can reference the selected or specified values in a specific control (the output) in a SQL statement. For a control that outputs a range of numeric values, use the syntax as follows.

### Supported control types

* Number range
* Range slider

### Syntax

To retrieve the minimum value, use the following syntax:  
`{{Range-Control-ID}}:min`

To retrieve the maximum value, use the following syntax:  
`{{Range-Control-ID}}:max`

### Example

To filter the PLUGS\_ELECTRONICS\_HANDS\_ON\_LAB\_DATA for products that sold a given quantity between the minimum and maximum values selected on a slider control with the control ID `slider-control-ID`, use the following example SQL:

SQL

```
SELECT *
from EXAMPLES.PLUGS_ELECTRONICS.PLUGS_ELECTRONICS_HANDS_ON_LAB_DATA
where QUANTITY between {{slider-control-ID}}:min and {{slider-control-ID}}:max
```

## Reference date range control values in SQL

You can reference the specified values in a date range control in a SQL statement.

### Supported control types

* Date range

### Syntax

To reference the start value of a date range control, use `{{#formula [Date-Range-Control].start}}`.

To reference the end value of a date range control, use `{{#formula [Date-Range-Control].end}}`.

There is also alternate syntax available depending on how your particular data platform interprets the control.

For example, to extract the start date of the date range control in custom SQL:

* In Snowflake, the control is a VARIANT data type, so you can use the following syntax:  
  `to_timestamp({{Date-Range-Control}}:start)`
* In BigQuery or Databricks, the control is a STRUCT data type, so you can use the following syntax:  
  `{{Date-Range-Control}}.start`
* In Amazon Redshift, the control is a SUPER data type, so you can use the following syntax:  
  `select date_range.start start from (select {{Date-Range-Control}} date_range)`
* In PostgreSQL, the control is a JSONB data type, so you can use the following syntax:  
  `({{Date-Range-Control}}->>‘start’)::timestamptz`
* In Azure SQL Server, the control is treated as a JSON data type, so you can use the following syntax: `CAST(JSON_VALUE({{Date-Range}}, '$.start') AS datetime2)`

To reference the end date of the range, reference `end` instead of `start`.

### Return output for a specific date range control

To return all rows from a table element named `PLUGS_ELECTRONICS_HANDS_ON_LAB_DATA` that have a value in the column *Date* between the start and end values of a date range control, use the following example SQL:

SQL

```
SELECT
  *
FROM
  sigma_element ('PLUGS_ELECTRONICS_HANDS_ON_LAB_DATA')
WHERE
  "Date" BETWEEN {{#formula [current-date-range-control].start}} AND {{#formula [current-date-range-control].end}}
```

This SQL returns all rows with a *Date* value in the range specified in the date range control `current-date-range-control`.

## Reference multiple values from a multi-select list in SQL

You can reference the selected or specified values in a specific control (the output) in a SQL statement. The values in a multi-select list are outputted as an array. For example:

`('apples','bananas','oranges')`

If the control value is output with single quotation marks, you can remove these quotation marks by prepending the keyword `#raw` before the control ID:

`{{#raw my-control-id}}`

> 🚧
>
> ### If you use the `#raw` configuration value, row-level security can be bypassed in the workbook or worksheet, creating a security vulnerability.

### Supported control types

* List values
* Legend

### Syntax

The exact syntax might be different for your connection depending on how your particular cloud data warehouse (CDW) interprets an array data type.

* For Snowflake, see Array in [Semi-structured data types](https://docs.snowflake.com/en/sql-reference/data-types-semistructured#label-data-type-array) in the official Snowflake Documentation.
* For Databricks, see [ARRAY type](https://docs.databricks.com/en/sql/language-manual/data-types/array-type.html) in the official Databricks documentation.
* For BigQuery, see [Work with arrays](https://cloud.google.com/bigquery/docs/arrays) in the official Google Cloud BigQuery documentation.
* For Amazon Redshift, see [SUPER type](https://docs.aws.amazon.com/redshift/latest/dg/r_SUPER_type.html) in the official Amazon Redshift Database Developer Guide.

For example:

SQL

```
select
  *
FROM
  APPLICATIONS.GOOGLE_ANALYTICS.EVENTS
WHERE
  TRAFFIC_SOURCE IN {{TRAFFIC_SOURCE}}
limit
  10
```

For a more detailed example, see [Return rows depending on the value of a multi-select control](#return-rows-depending-on-the-value-of-a-multi-select-control).

### Return rows depending on the value of a multi-select control

If you have a multi-select control called `City` and you run this SQL on a Snowflake connection, the following example query returns all rows where the `CITY` column value is listed in the selection for the `City` control. If there are no cities selected in the `City` control, all rows are returned:

SQL

```
SELECT *  
FROM EXAMPLES.BIKES.STATIONS  
WHERE  
CASE WHEN  
LEN(ARRAY_TO_STRING(ARRAY_CONSTRUCT{{City}},',') ) = 0  
THEN True  
ELSE CITY in {{City}} END
```

For more examples, see [Injecting multi-select parameters in Custom SQL](https://community.sigmacomputing.com/t/injecting-multi-select-parameters-in-custom-sql/2072) article in the Sigma Community.

Updated 3 days ago

---

[Write custom SQL](/docs/write-custom-sql)[Query a dbt Semantic Layer integration](/docs/query-a-dbt-semantic-layer-integration)

* [Table of Contents](#)
* + [Limitations and warnings](#limitations-and-warnings)
  + [Reference single value control output in SQL](#reference-single-value-control-output-in-sql)
  + - [Supported control types](#supported-control-types)
    - [Syntax](#syntax)
  + [Reference number range or range slider control values in SQL](#reference-number-range-or-range-slider-control-values-in-sql)
  + - [Supported control types](#supported-control-types-1)
    - [Syntax](#syntax-1)
    - [Example](#example)
  + [Reference date range control values in SQL](#reference-date-range-control-values-in-sql)
  + - [Supported control types](#supported-control-types-2)
    - [Syntax](#syntax-2)
    - [Return output for a specific date range control](#return-output-for-a-specific-date-range-control)
  + [Reference multiple values from a multi-select list in SQL](#reference-multiple-values-from-a-multi-select-list-in-sql)
  + - [Supported control types](#supported-control-types-3)
    - [Syntax](#syntax-3)
    - [Return rows depending on the value of a multi-select control](#return-rows-depending-on-the-value-of-a-multi-select-control)