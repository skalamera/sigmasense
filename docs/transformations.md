# Define custom datetime formats

# Define custom datetime formats

Sigma enables you to define custom datetime formats to control how [date data](/docs/data-types-and-formats) displays in workbooks.

This document provides an overview of custom format strings and explains how to use them to display custom date formats.

> 📘
>
> ### This document specifically refers to custom datetime formatting in the Sigma UI. For information about datetime formats supported by functions, see [DateFormat](/docs/dateformat) and [DateParse](/docs/dateparse).

## User requirements

To define a custom datetime format, you must be the workbook owner or be granted **Can explore** [workbook permission](/docs/folder-and-document-permissions).

## Custom format strings

Custom format strings support individual [format specifiers](#common-format-specifiers) and combinations of multiple specifiers and characters, including letters, numbers, and symbols.

For example, the following table demonstrates the output of three different custom format strings applied to the value *2018-07-08 00:34:59*:

| Custom format string | Output |
| --- | --- |
| %a, %b %d, %Y | Sun, Jul 08, 2018 |
| %Y-Q%q | 2018-Q3 |
| %I:%M:%S %p | 12:34:59 AM |

### Common format specifiers

The following table defines commonly used format specifiers. For a complete set of supported specifiers, reference the [d3-time-format](https://d3js.org/d3-time-format) module.

| Format | Description | Example output  *(for 2018-07-08 00:34:59)* |
| --- | --- | --- |
| %Y | Four-digit year | 2018 |
| %y | Two-digit year | 18 |
| %q | Quarter of the year (1–4) | 3 |
| %m | Two-digit month | 07 |
| %B | Full month name | July |
| %b | Abbreviated month name | Jul |
| %A | Full day of week | Sunday |
| %a | Abbreviated day of week | Sun |
| %d | Two-digit day of month (01-31) | 08 |
| %H | Two-digit hour based on 24-hour clock (00–23) | 00 |
| %I | Two-digit hour based on 12-hour clock (01–12) | 12 |
| %M | Two-digit minutes (00–59) | 34 |
| %S | Two-digit seconds (00–59) | 59 |
| %p | AM or PM | AM |
| %L | Three-digit milliseconds (000–999) | 000 |
| %f | Six-digit microseconds (000000–999999) | 000000 |
| %Z | Time zone offset | -07:00 |
| %% | Percent sign | % |

## Define a custom datetime format

1. Use one of the following methods to access the **Custom Format** modal:

   * Column menu: In the header of the column you want to format, click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu, then select **Format** > **Custom**.

     ![](https://files.readme.io/aad14f9-image.png)
   * Toolbar: Select the column you want to format, then click the **Format** option in the workbook toolbar and select **Custom date**.

     ![](https://files.readme.io/5420bd8-image.png)
2. In the **Custom Format** modal, enter the format string and confirm that the **Example** field reflects the datetime format you want to display.

   ![](https://files.readme.io/a11b922-image.png)
3. Adjust the format string, if needed, then click **Apply**. The column immediately reflects the custom datetime format.

   ![](https://files.readme.io/6f0d36f-image.png)

Updated 3 days ago

---

Related resources

* [Data types and formats](/docs/data-types-and-formats)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Custom format strings](#custom-format-strings)
  + - [Common format specifiers](#common-format-specifiers)
  + [Define a custom datetime format](#define-a-custom-datetime-format)