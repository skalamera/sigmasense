# Dynamically filter and modify data in Sigma

# Dynamically filter and modify data in Sigma

When building workbooks and modeling data in Sigma, you can filter data and modify data based on user inputs.

For example, you might want to do any of the following:

* [Limit the data available to workbooks](#filter-data) that use a data model as a source, or to child elements of a workbook table.
* [Perform calculations or filter SQL queries](#filter-sql-queries-or-perform-calculations-based-on-inputs) based on user inputs.
* [Design interactions for viewers of your workbook](#design-interactions-for-workbook-viewers), such as a drilldown or changing the data being displayed, letting you simplify workbooks and provide self-serve analytics.
* [Modify the contents of an exported report](#modify-contents-and-recipients-of-an-exported-report), including how the report is sent and to whom.

## Filter data

You can limit available data on an individual element, in an entire workbook, or in a dataset or data model.

* [Add a **filter**](/docs/data-element-filters) to a table, pivot table, or visualization. A data element filter limits the data in that element and any downstream dependencies using the element as a data source.
* [Add a **control**](/docs/intro-to-control-elements) to a workbook or data model page and target one or more elements to limit the data available to those elements and any child elements. For example:
  + Add a list control for multi-select filters.
  + Add a segmented control for single-select filters.
  + Add a slider or range slider control to filter values within a specific numeric range.
  + Add a date range or date control for date filters.

## Filter SQL queries or perform calculations based on inputs

Build calculated columns or filter custom SQL queries based on user input by referencing controls in formulas or SQL statements:

* [Add a **control**](/docs/intro-to-control-elements) to a workbook or data model, then [reference the control](/docs/parameters-in-workbooks) to use the value of the control in a Custom SQL element or in a formula, such as for a calculated column. For example:
  + [Reference a date range control in a “where” filter in a SQL query](/docs/reference-workbook-control-values-in-sql-statements) to filter the results.
  + Reference a list control with date values in a column with a `DateTrunc()` function, then use that calculated column as the X-axis in a chart to dynamically display different date ranges.
  + Reference a segmented control in a column with the `Switch`, `Choose`, or `If` function to change the output of a column based on user input.
  + Reference a control value in the title of a data element using dynamic text to display the filtering applied.
* [Add a **parameter** to a dataset](/docs/create-and-manage-dataset-parameters) to perform calculations in the dataset based on user input.

## Design interactions for workbook viewers

[Add one or more **controls**](/docs/intro-to-control-elements) to a workbook to let users viewing or exploring the workbook interact with the data in a specific way. For example:

* Add a switch control to let viewers switch from one granularity of data to another, or perform other Boolean operations.
* Add a text or text area control to let viewers search for information in a column.
* Add a list control, [segmented control](/docs/segmented-control), slider or range slider control, or date or date range control to let viewers filter data.
* Add a [drill down control](/docs/drill-down-control) to support one-click drill down or drill up behavior.

To design more complex interactions, such as [filtering one element based on interaction with another](/docs/create-cross-element-filters), or changing which columns are visualized in a pivot table or a chart, configure workbook actions. For more details, see [Intro to actions](/docs/intro-to-actions). You can also [combine controls with workbook actions](/docs/create-actions-that-manage-control-values) to design interactions like a form that can write-back data to your data platform.

## Modify contents and recipients of an exported report

Add a **control** to a workbook to modify the content of an exported report according to the [values of the control](/docs/configure-additional-options-for-exports#filter-by-control-values), or manage which reports are sent to which recipient as an [email burst](/docs/export-as-email-burst). You can then reference the control when performing or scheduling an export using the UI or the API.

## Best practices for using filters, controls, and parameters

When adding filters, controls, or parameters to your workbook, data model, or dataset, consider the following best practices:

* Add a filter to parent or source elements to keep data filtering consistent and lineage clear. For example, filter a website analytics data model by host name rather than filtering individual data elements by the same value.
* Target controls to child elements of materialized data to avoid invalidating a materialization.
* Use dynamic text in element titles and workbook page titles to communicate the current state of a filtered element when the element is targeted by a control.
* Consider applying filters or targeting controls that perform filtering to the source tables for complex visualizations to ensure that the filter is applied to the correct grouping level and works as intended.
* If you configure a control to use a column as the source of control values, do not target the source element with the same control. Instead, duplicate the table and use one table as the source for the control values and another as the target, which can then be used as a data source by any downstream or child elements.

Updated 3 days ago

---

[Add a custom color scale](/docs/add-a-custom-color-scale)[Filter data in data elements](/docs/data-element-filters)

* [Table of Contents](#)
* + [Filter data](#filter-data)
  + [Filter SQL queries or perform calculations based on inputs](#filter-sql-queries-or-perform-calculations-based-on-inputs)
  + [Design interactions for workbook viewers](#design-interactions-for-workbook-viewers)
  + [Modify contents and recipients of an exported report](#modify-contents-and-recipients-of-an-exported-report)
  + [Best practices for using filters, controls, and parameters](#best-practices-for-using-filters-controls-and-parameters)