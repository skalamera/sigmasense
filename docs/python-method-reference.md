# Python method reference (Beta)

# Python method reference (Beta)

> 🚩
>
> This documentation describes one or more public beta features that are in development. Beta features are subject to quick, iterative changes; therefore the current user experience in the Sigma service can differ from the information provided in this page.
>
> This page should not be considered official published documentation until Sigma removes this notice and the beta flag on the corresponding feature(s) in the Sigma service. For the full beta feature disclaimer, see [Beta features](/docs/sigma-product-releases#beta-features).

When writing Python code in a Python element in Sigma, the following methods are available:

* [sigma.get\_element()](#sigmaget_element)
* [sigma.output()](#sigmaoutput)
* [sigma.get\_control\_value()](#sigmaget_control_value)

> 📘
>
> This feature isn't supported by all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## sigma.get\_element()

Use the `sigma.get_element` method to reference another element in your workbook in your Python code. You can reference an input table, table, custom SQL element, or the output of another Python element.

### Syntax

Python

```
sigma.get_element("element_name")
```

### Arguments

* `element_name`: The title of a data element passed as a string literal. If using to reference the output of another Python element, must be the `reference_name` specified in the `sigma_output()` method.

### Output

The output of the `sigma.get_element` method depends on the connection:

* On a Databricks connection, the output is a PySpark DataFrame.
* On a Snowflake connection, the output is a SnowPark DataFrame.

### Usage notes

* The referenced element must be in the same workbook and use the same connection as the Python element.
* Element names are not guaranteed to be unique, so if your reference produces unexpected output, validate that the element name is unique in your workbook.

### Example: Reference columns in a data element

You can work with the specific columns in a referenced data element. To determine how the columns appear in the created DataFrame, describe the output with a statement like the following before using the columns in your statement:

Python

```
df = sigma.get_element('Custom SQL'); print(df.describe())
```

For example, reference a column titled "Order Number" as "order\_number":

Python

```
df = sigma.get_element("plugs")

df.select("order_number").show(10)
```

#### Example: Reference the output of another Python element

To reference the output of another Python element in your Python code, do the following:

1. Write a [`sigma_output()`](#sigmaoutput) statement in the Python element you want to reference.
2. In the new Python element, use the `sigma.get_element()` method with the `reference_name`.

For example, if you have a Python element with example code like the following:

Python

```
df = sigma.get_element("plugs")

filter = df.select("order_number","product_type").filter(df["order_number"] > 533000)

sigma.output('filtered_plugs_data', filter)
```

You can reference the output and work with it in another Python element:

Python

```
df = sigma.get_element("filtered_plugs_data")

df.groupby(df["product_type"]).count()
```

## sigma.output()

Use the `sigma.output()` method to make the contents of a Python variable available to other elements in your workbook. For example, work with the contents of a DataFrame as a Sigma table or display the output in a chart element. This method writes to a new table in the default or specified write-back destination.

### Syntax

Python

```
sigma.output('reference_name', var_name, [write-back_destination])
```

### Arguments

* `reference_name`: The name that you want to use to reference the contents of the specified Python variable. The `reference_name` cannot include spaces and must be a string literal.
* `var_name`: The name of the variable in your Python code that you want to make available to other elements.
* `write-back destination`: The path to the write-back destination that you want to make the output available from, in the format `CATALOG.SCHEMA`.

  + Include this argument only if you use OAuth to connect to your data platform.
  + Do not include this argument if you use an access token or key-pair to authenticate your connection. Instead, these connections use the write-back destination configured on the connection.

### Output

The output of the `sigma.output` method is a table written back to your data platform.

### Usage notes

* Add a `sigma.output()` statement for each variable that you want to make available to other Sigma elements.
* You can only output one variable per statement.
* `sigma.output()` must be called with a particular output unconditionally. You cannot use this method inside branching logic in your code, and Sigma strongly discourages using this method inside loops.

### Example

For example, for code like the following:

Python

```
df = sigma.get_element("plugs")

filter = df.select("order_number").filter(df["order_number"] > 533000)
```

To make the `filter` variable available to reference from other Sigma elements with a name such as `filtered_plugs_data`, add the following line to your code:

Python

```
sigma.output('filtered_plugs_data', filter)
```

## sigma.get\_control\_value()

If your workbook contains control elements, you can reference the control ID and retrieve the control value to use in your Python code, for example to use user input to change the variables assigned in your code.

### Syntax

Use the following syntax in your Python code:

Python

```
sigma.get_control_value("control_id")
```

### Arguments

* `control_id`: The control ID of the control element used for input.

### Usage notes

* For details on retrieving the control ID, see [Identify the control ID for a control](/docs/parameters-in-workbooks#identify-the-control-id-for-a-control).

### Output

Depending on the [output value of the control element](/docs/intro-to-control-elements) that you reference, the output of this method can be different:

* [Reference single value control output](#reference-single-value-control-output)
* [Reference number range, date range, or range slider control values](#reference-number-range-date-range-or-range-slider-control-values)
* [Reference multiple values from a multi-select list](#reference-multiple-values-from-a-multi-select-list)

### Reference single value control output

Controls that output a single value return one of string, int, float, datetime.datetime, or None, depending on the data type of the control value.

#### Supported control types

* Single select list
* Text input
* Text area
* Number input
* Date
* Segmented
* Slider
* Checkbox
* Switch
* Top N

#### Example: Reference the value of a slider control

For example, use the selected value of a slider control with the control ID `slider` in a filter for your DataFrame:

Python

```
df = sigma.get_element('plugs')

var = sigma.get_control_value("slider")

df.select("Cost").filter(df["Revenue"] > var).show(10)
```

#### Example: Reference the value of a text control

For example, use raw HTML entered into a text input control with the control ID `raw-html` as input to the `beautifulsoup` library to parse the plain text from the contents:

Python

```
from bs4 import BeautifulSoup

soup = BeautifulSoup(sigma.get_control_value('raw_html'), 'html.parser')

raw = soup.get_text()

sigma.output("plain_text", raw)
```

### Reference number range, date range, or range slider control values

Controls that output a range of values return an ordered pair (2-tuple) of int, float, or datetime.datetime, depending on the data type of the control value. The ordered pair is in the format `(low_value, high_value)`.

#### Supported control types

* Number range
* Date range
* Range slider

#### Example: Reference the maximum value of a range slider control

For example, use the maximum selected value from a range slider control with the control-ID `range-slider` in a filter for your DataFrame:

Python

```
df = sigma.get_element('plugs')

var = sigma.get_control_value("range-slider")

df.select("Cost").filter(df["Revenue"] > var[1]).show(10)
```

#### Reference multiple values from a multi-select list

Controls that output a list of values return a list in the data type of the control value, one of string, int, float, datetime.datetime, or None. For example, a multi-select list values control of text values returns a list of strings.

#### Supported control types

* List values
* Legend

#### Example: Reference the values of a multi-select list values control

For example, to filter the list of product names by specific product types selected in a multi-select list values control with the control-ID `list`:

Python

```
df = sigma.get_element('plugs')

var = sigma.get_control_value("list")

df.select("Product_Name").filter(df["Product_Type"].isin(var)).show(10)
```

Updated 3 days ago

---

[Write and run Python code in Sigma (Beta)](/docs/write-and-run-python-code)[Query](/docs/query)

* [Table of Contents](#)
* + [sigma.get\_element()](#sigmaget_element)
  + - [Syntax](#syntax)
    - [Arguments](#arguments)
    - [Output](#output)
    - [Usage notes](#usage-notes)
    - [Example: Reference columns in a data element](#example-reference-columns-in-a-data-element)
  + [sigma.output()](#sigmaoutput)
  + - [Syntax](#syntax-1)
    - [Arguments](#arguments-1)
    - [Output](#output-1)
    - [Usage notes](#usage-notes-1)
    - [Example](#example)
  + [sigma.get\_control\_value()](#sigmaget_control_value)
  + - [Syntax](#syntax-2)
    - [Arguments](#arguments-2)
    - [Usage notes](#usage-notes-2)
    - [Output](#output-2)
    - [Reference single value control output](#reference-single-value-control-output)
    - [Reference number range, date range, or range slider control values](#reference-number-range-date-range-or-range-slider-control-values)