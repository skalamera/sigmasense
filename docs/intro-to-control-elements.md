# Intro to control elements

# Intro to control elements

Add control elements to a workbook to provide predefined interactions to users viewing or customizing a workbook, such as inputs that modify data, selections to filter data or change displayed data, drilldown paths, or other ways of manipulating data.

You can also add control elements to data models, centralizing filter management and allowing you to reference control values as parameters in calculated columns.

Control elements provide powerful configuration options to a workbook:

* Build interactivity in a workbook, such as by adding a text input control that passes data to an AI query in a calculated column. See [Perform AI queries](/docs/perform-ai-queries).
* Reference control values in formulas, enabling calculated columns that change based on user input. See [Reference control values as parameters](/docs/parameters-in-workbooks).
* Perform dynamic filtering in SQL statements by referencing control values. See [Reference workbook control values in SQL statements](/docs/reference-workbook-control-values-in-sql-statements).
* Change the granularity of data displayed in a workbook based on user selection. See [Create and configure a segmented control](/docs/segmented-control).
* Enable predefined drilldown and drill up paths for one or more visualizations. See [Drill down control](/docs/drill-down-control).
* Build a form to enter data into an input table and write back to your data platform.
* Define an action that sets a control value, allowing you to build a complex workflow. See [Create actions that manage control values](/docs/create-actions-that-manage-control-values).
* Burst different copies of a report to different recipients based on the available values of a control. See [Export as email burst](/docs/export-as-email-burst).

> 🚧
>
> When executing a scheduled export or direct download to PDF or PNG formats, Sigma may store applicable control values as URL parameters in trace logs used for debugging and troubleshooting purposes. Exercise caution when using controls to filter sensitive data.

## Filters and controls

You can filter a data element in several different ways:

* Filter one data element by adding filters to directly on columns in the data element. After you create a filter on a data element, you can convert it to a control. See [Filter data in data elements](/docs/data-element-filters).
* Filter the data sources of a workbook and one or more data elements in a workbook by adding a control element and adding targets to each data element. See [Create and manage a control element](/docs/create-and-manage-a-control-element).
* Filter data directly in the query by adding a control and referencing the control in a SQL statement. See [Reference workbook control values in SQL statements](/docs/reference-workbook-control-values-in-sql-statements).
* Filter data elements with the same control settings on multiple pages by adding a page control with synced copies. See [Synced controls](/docs/synced-controls).

When you filter data in a data element, the filtering affects downstream and child elements. If you create a filter on a parent element, the filter cannot be viewed or modified from child elements. See [Filter data in data elements](/docs/data-element-filters).

For more best practices, see [Best practices for using filters, controls, and parameters](/docs/dynamically-filter-and-modify-data-in-sigma#best-practices-for-using-filters-controls-and-parameters).

## About control IDs

When you add a control to a workbook, Sigma automatically generates a control ID. You can use the ID to reference values of the control when exporting a workbook or target elements, in custom SQL statements, when constructing an embed URL, or when using different Sigma REST API endpoints. The ID is also used internally for references between controls and their targets.

You can change a control ID, but doing so might break existing references to the control. You can always update the control label.

When you duplicate a control, the new control has the same behavior and formatting as the original, but the ID is updated to be unique.

When you sync controls, they share the same ID. See [Synced controls](/docs/synced-controls).

## Types of controls

Control elements support a wide range of options, including all filter types:

* [List values](#list-values)
* [Text input](#text-input)
* [Text area](#text-area)
* [Segmented control](#segmented-control)
* [Number input](#number-input)
* [Number range](#number-range)
* [Slider](#slider)
* [Range slider](#range-slider)
* [Date](#date)
* [Date range](#date-range)
* [Top N](#top-n)
* [Drill down](#drill-down)
* [Switch](#switch)
* [Checkbox](#checkbox)
* [Legend](#legend)

To create a control, see [Create and manage a control element](/docs/create-and-manage-a-control-element) .

### List values

Include or exclude selected values in a list. Up to 200 values can be displayed in the list control.

* **Input type**: List of selectable values.
* **[Supported data types](/docs/data-types-and-formats)**: Text, Number, Date, Logical
* **Parameter output type**:
  + If multiple selection is enabled, array of data type selected.
  + If multiple selection is disabled, single value of data type selected.
* **Examples**:
  + Select multiple page paths to include for several elements on a website analytics workbook.
  + Select relevant ID numbers to exclude from a table.
  + Choose the current and previous quarter from a list to include only those quarters in a chart.
  + Select false and null values for a survey column to include only those in a table.

#### Interactive example of a list values control

In the following interactive example, interact with the **Year** list values control. Click to open the dropdown menu, then select the sales years you want to show in the chart. Both targeted data elements respond to your changes.

### Text input

Search values in the targeted data element column(s) for full and partial matches between the text input and your data’s values.

* **Input type**: Enter text in a text box. If the option is shown, the user can select an operator.
* **[Supported data types](/docs/data-types-and-formats)**: Text
* **Parameter output type**: Single value text string. Operators are not available with the control value.
* **Examples**:
  + View data where the text contains "Total".
  + View data for host names that start with "https://www".
  + View data where the text does not contain "Not Applicable".
  + View data where the text ends with "EOF", case sensitive.
  + View data where the text matches "total" or "subtotal" using a regular expression `total|subtotal`.

![Text input control with operator of Equal to shown.](https://files.readme.io/24b11cf061d2997bb0f0b1c33c75cd331453d6201def728100d3840f566c5acd-ctrl-text-input.png)

#### Configure text input

You can configure operators for a text input control which control the matching conditions for the inputted text, including Contains, Starts with, Ends with, and Like, as well as the corresponding exclude operators: Does not contain, Does not start with, Does not end with, and Not like. You can also provide regular expressions with Matches Regexp and Does not match RegExp operators.

### Text area

Search for full and partial matches between the inputted text and the targeted data values. Also useful for providing text input to a formula by referencing the control as a parameter.

* **Input type**: Enter text into a text area.
* **[Supported data types](/docs/data-types-and-formats)**: Text
* **Parameter output type**: Single value text string.
* **Examples**:
  + Provide a text prompt to pass to an AI query function.
  + Add notes from a conversation in a form to update an input table.

![Text area control](https://files.readme.io/e53835710f7b558782a569023952c291693504010cf8bdd4eff92dd8135a6efc-ctrl-text-area.png)

### Segmented control

Provide a single-select limited set of options for users to select from.

* **Input type**: Select a segment.
* **[Supported data types](/docs/data-types-and-formats)**: Text, Number, Date, Logical
* **Parameter output type**: Single value of data type selected.
* **Examples**:
  + Provide multiple options to adjust the time granularity for a chart from Quarterly, Monthly, or Weekly.
  + Toggle between different customer groups: new, prospective, existing, all.
  + Show only results for the selected product quarter.

![Segmented control showing preset weekday list options](https://files.readme.io/992fbbeabcf675946c2646b3fc1ffe5109b9f168e921493500ef9a9c396c5018-ctrl-segmented.png)

For more details, see [Create and configure a segmented control](/docs/segmented-control).

### Number input

Enter a single number to filter a data element, or use as a parameter in custom SQL or a formula.

* **Input type**: Numeric input box.
* **[Supported data types](/docs/data-types-and-formats)**: Number
* **Parameter output type**: Single value number. Filter operator is not available in the output.
* **Examples**:
  + Perform aggregate calculations using the number inputted as a constant. For example, test different weights for a linear regression by using different number input controls as parameters in the formula.
  + Show only rows for a matching ID number.

![Number input control](https://files.readme.io/f43daf4e3da73ab9968728964b8e03e0507f6ad7874118c28e1dfce41f7a4a4e-ctrl-number-input.png)

#### Configure number input

You can configure filters for a text input control to control the matching conditions for the inputted number. Choose from `<=` (less than or equal to), `=` (equal to), or `>=` (greater than or equal to). Defaults to `=`.

### Number range

Enter a minimum number and/or a maximum number for a range to filter the results in targeted data elements. The range is inclusive of the entered numbers.

* **Input type**: Minimum and maximum input boxes.
* **[Supported data types](/docs/data-types-and-formats)**: Number
* **Parameter output type**: One minimum number, one maximum number.
* **Examples**:
  + Exclude survey results with fewer than 5 responses by setting a minimum of 5.
  + Include demographic data for ages between 45 and 55, inclusive.
  + Exclude user sessions with more than 100 clicks from website analytics data by setting a maximum of 100.

![Number range control with placeholder text for a minimum value (min) and a maximum value (max) of the range](https://files.readme.io/8fa3b6b2d207bce17aff2b177c67365f5b8a85d1d1b4b3331a877544fd2c8c71-ctrl-number-range.png)

### Slider

Select a number from a specific range using a slider. Similar to the number input control, the slider option lets you restrict the available input options.

* **Input type**: Move a slider.
* **[Supported data types](/docs/data-types-and-formats)**: Number
* **Parameter output type**: Single value number.
* **Examples**:
  + Show only demographic data with ages greater than or equal to the selected value. (filter is >=)
  + Show only deals less than or equal to the selected profit margin value. (filter is <=)
  + Show only transactions with the selected number of items purchased. (filter is =)

![Slider control with a specific value (32) chosen on the slider.](https://files.readme.io/34c92748f9a809b4792cb842a20760545325a0ee73396fe8eb20fb74cc9595d7-ctrl-slider.png)

### Range slider

Specify a number range within a designated range using a slider. Similar to the number range control, the range slider lets you restrict the available input options.

* **Input type**: Slider with two points.
* **[Supported data types](/docs/data-types-and-formats)**: Number
* **Parameter output type**: One minimum number, one maximum number.
* **Examples**:
  + Include demographic data for different age ranges, in 5 year steps. For example, ages 50–60, inclusive.

![Range slider with a minimum value of 10 and a maximum value of 75 selected, with the space in between the min and max highlighted.](https://files.readme.io/938d370f92cab211dfb4383e419332a050391526580aa404832a129e35abbd42-ctrl-range-slider.png)

### Date

Choose a single date to use to filter a column or use as a parameter. Both fixed (2024-12-12) and relative (Now minus 7 days) dates are supported.

* **Input type**: Calendar date picker.
* **[Supported data types](/docs/data-types-and-formats)**: Date
* **Parameter output type**: Single value date.
* **Examples**:
  + View data for a specific date.
  + Specify a project due date in a form.
  + View projects due in the next 7 days.

![Date control showing the option "On" with the date January 22, 2025 selected.](https://files.readme.io/6635d6e0fbb836cc9098dac8404189f2fa7b57a373bd721d025b681eee2cac0b-ctrl-date.png)

### Date range

Select a date range to use to filter a targeted data element, or use the selected date range as a parameter, for example to filter a custom SQL statement. The selected range is inclusive of the endpoints. Fixed and relative date ranges are supported.

* **Input type**: Calendar date picker for minimum and maximum values.
* **[Supported data types](/docs/data-types-and-formats)**: Date
* **Parameter output type**: One minimum date, one maximum date.
* **Examples**:
  + View data from the last 30 days to assess a monthlong campaign.
  + View telemetry data from the last 15 minutes to troubleshoot a problem.
  + View financial data for the current quarter-to-date.
  + View data from the first Monday of the month, for example, November 4, 2024.

![Date range control with the default option Between and the date January 22, 2025 selected for both the start and end dates.](https://files.readme.io/3232e99b5a5c90e6bc92fd55fc16b653428465e3911e501af874e3880317c64e-ctrl-date-range.png)

### Top N

Limit the available data according to a ranking, such as top 15 or bottom 10%.

Ranks and limits data in the column based on your specifications.

* **Input type**:
  + Rank order and direction
  + Numeric input
* **[Supported data types](/docs/data-types-and-formats)**: Text, Number, Date
* **Parameter output type**: Single value of data type inputted. Operator (Top, Bottom) is not included in the output.
* **Examples**:
  + View the last 20 employees by name, alphabetically.
  + View the top 10 most-viewed pages in website analytics data.
  + View the first 5 survey responses by date.

![Top N filter control showing the operator rank function Top N and a text box.](https://files.readme.io/7d2e19931839e7d113f7dfe89beedc7bd61e763307de5d4d9709bfaed643d080-ctrl-top-N.png)

For more details, see [Top N Filter](/docs/top-n-filter).

### Drill down

Let a user drill into a pre-defined layer of data, such as one level higher or lower in data granularity. A drill down control enables double click to drill.

* **Input type**: Clickable text.
* **[Supported data types](/docs/data-types-and-formats)**: Text, Number, Date, Logical
* **Parameter output type**: Single value, Text. Matches the column name for the selected drill category.
* **Examples**:
  + For a chart showing product sales by product type, provide a drill down control for a viewer to drill into sales by product family.

![Drill down control with two preset drill options selected, one for event name and one for traffic source, based on the EVENTS table from the sample database.](https://files.readme.io/6caa666abf3b03d0678a87a27c30ba9018499170eda60982e792c56f8614d036-ctrl-drill-down.png)

For more details, see [Drill Down Control](/docs/drill-down-control).

### Switch

Turn on or turn off a toggle switch to let users choose between True (turned on) or False (turned off) values.

* **Input type**: Toggle switch
* **[Supported data types](/docs/data-types-and-formats)**: Logical
* **Parameter output type**: Logical (Boolean)
* **Examples**:
  + Choose whether to display referrer data that includes internal sources.

![Switch option with True and False values](https://files.readme.io/b4cc692ee8a074329e58050cd88d889cd07dadd7824b089f02ff7be8bdf261e5-ctrl-switch.png)

### Checkbox

Select or deselect a checkbox to represent True (selected) or False (deselected) values.

* **Input type**: Checkbox
* **[Supported data types](/docs/data-types-and-formats)**: Logical
* **Parameter output type**: Logical (Boolean)
* **Examples**:
  + Choose whether to display survey responses from incomplete surveys.

![Checkbox shown deselected.](https://files.readme.io/e154e24e2e2b3678920a36d92364874c5a0731e281b3076f42c98b02b3ad6500-ctrl-checkbox.png)

### Legend

Add a legend to use for one or more charts.

* **Input type**: Select legend items.
* [**Supported data types**](/docs/data-types-and-formats): Text, Number, Date, Logical
* **Parameter output type**: Array of data type selected.
* **Examples**:
  + Apply the same chart colors across multiple charts.
  + Group values other than the top 5 into an "others" category in one or more charts.
  + Filter multiple charts at once.

For more details, see [Create and configure a legend control](/docs/create-and-configure-a-legend-control).

Updated 3 days ago

---

Related resources

* [Intro to data elements](/docs/intro-to-data-elements)
* [Filter data in data elements](/docs/data-element-filters)
* [Reference control values as parameters](/docs/parameters-in-workbooks)
* [Set control values in a URL using query string parameters](/docs/workbook-control-values-in-the-url)
* [Reference workbook control values in SQL statements](/docs/reference-workbook-control-values-in-sql-statements)

* [Table of Contents](#)
* + [Filters and controls](#filters-and-controls)
  + [About control IDs](#about-control-ids)
  + [Types of controls](#types-of-controls)
  + - [List values](#list-values)
    - [Text input](#text-input)
    - [Text area](#text-area)
    - [Segmented control](#segmented-control)
    - [Number input](#number-input)
    - [Number range](#number-range)
    - [Slider](#slider)
    - [Range slider](#range-slider)
    - [Date](#date)
    - [Date range](#date-range)
    - [Top N](#top-n)
    - [Drill down](#drill-down)
    - [Switch](#switch)
    - [Checkbox](#checkbox)
    - [Legend](#legend)