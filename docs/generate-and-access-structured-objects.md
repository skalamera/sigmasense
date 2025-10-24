# Generate and access structured objects

# Generate and access structured objects

Record formulas improve data processing and interaction by enabling you to generate structured objects (like JSON) directly in workbooks and data models.

When Sigma processes structured objects, it preserves individual field data types and enforces type constraints. While this practice ensures data integrity and accuracy, it also allows you to easily access and manipulate object values *without performing type conversions*.

This document introduces record formulas and explains how to generate and access structured objects.

> 📘
>
> ### Record formulas are supported by AzureSQL, BigQuery, Databricks, MySQL, PostgreSQL, Redshift, and Snowflake.

## User requirements

To generate and access structured objects in workbooks and data models, you must be the document owner or be granted **Can explore** (applicable to workbooks only) or **Can edit** [document permission](/docs/folder-and-document-permissions).

## Use record formulas to generate structured objects

Record formulas can generate structured objects in calculated columns added to tables, pivot tables, input tables, and visualizations. Apply the formula syntax detailed in the following subsections to accurately define data types in structured objects.

### Record formula syntax

In the formula bar, construct a record formula using the following syntax:

```
{ key1: value1, key2: value2, key3: value3, ... }
```

You can specify any amount of key/value pairs, in which key components are constants that identify the object fields, and value components are [constants](#value-format-for-constants) or [other expressions](#value-format-for-other-expressions) that reference columns, control elements, and functions representing a [supported data type](/docs/data-types-and-formats).

### Value format for constants

When you assign a constant value, Sigma uses type inference to recognize text, number, and logical data types, and it relies on explicit function calls to identify date and variant data types.

The following table explains how to format constant values to define specific data types:

| Data type | Value format | Example |
| --- | --- | --- |
| Text | Text string enclosed in double quotes | `{ name: “Jane Doe” }` |
| Number | Numeric value (integer or floating point) | `{ employeeId: 2865 }` |
| Logical | Keyword `true` or `false` | `{ isActive: true }` |
| Date | Date string enclosed in double quotes and passed as an argument of the [Date](/docs/date) function | `{ startDate: Date(“2024-04-15”) }` |
| Variant | JSON string enclosed in double quotes and passed as an argument of the [Json](/docs/json) function  (Value format requirements detailed in this table also apply to values in the JSON string) | `{ location: Json({ city: "San Francisco", state: “CA”, zip: 94105}) }` |

### Value format for other expressions

When you assign a value that references a column, control element, or function, Sigma uses type inference to define the data type based on the context of the expression (for example, a function’s predefined return type).

The following table explains how to format values that reference columns, control elements, and functions:

| Reference | Reference format | Example |
| --- | --- | --- |
| Column | Column name enclosed in square brackets | `{ jobTitle: [Title] }` |
| Control element | Control ID enclosed in square brackets | `{ lastReview: [Review-date] }` |
| Function | Required function syntax  (See applicable function documentation) | `{ daysEmployed: DateDiff("day", [Hire Date], Today()) }` |

## Access and manipulate structured object values

To access and manipulate a specific field’s value in a structured object, set the path access using the following dot notation:

```
[Column Name].field
```

Because Sigma preserves data types in structured objects, you aren’t required to perform type conversions when you access the data or pass values to functions. This is in contrast to semi-structured objects, which are processed as [variant data](/docs/data-types-and-formats#variant) and may require type conversion to obtain the same output.

### Example: Structured vs. semi-structured path access

![Table showing Column A containing JSON objects with street, city, and state key/value pairs, and Column B joining Column A values as a single text string.](https://files.readme.io/ccdfc62-image.png)

#### Scenario 1: Column A contains structured objects

In the example table, Column A contains structured objects that store [text data](/docs/data-types-and-formats#text). To join the “street,” “city,” and “state” values into a single text string in Column B, you can use the following formula without type conversions:

```
Concat([Column A].street, ", ", [Column A].city, ", ", [Column A].state)
```

#### Scenario 2: Column A contains semi-structured objects

If Column A instead contains semi-structured objects, Sigma processes the object values as variant data. To join the values into a single text string in Column B, you must use the following formula, which requires the **[Text](/docs/text)** function to convert the values to text data before passing them to the **[Concat](/docs/concat)** function:

```
Concat(Text([Column A].street), ", ", Text([Column A].city), ", ", Text([Column A].state))
```

Updated 3 days ago

---

[Define custom datetime formats](/docs/define-custom-datetime-formats)[Data security](/docs/data-security)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Use record formulas to generate structured objects](#use-record-formulas-to-generate-structured-objects)
  + - [Record formula syntax](#record-formula-syntax)
    - [Value format for constants](#value-format-for-constants)
    - [Value format for other expressions](#value-format-for-other-expressions)
  + [Access and manipulate structured object values](#access-and-manipulate-structured-object-values)
  + - [Example: Structured vs. semi-structured path access](#example-structured-vs-semi-structured-path-access)