# Format and customize a table

# Format and customize a table

You can efficiently and effectively design and format the display of your tabular data in Sigma. Sigma provides preset display styles for out-of-the-box aesthetics and readability, or you can customize style components independently for more personalized table designs.

You can format and customize tables, pivot tables, and input tables, and apply the formatting at different levels of workbook development:

* Admins can define a default table style in an organization-wide workbook theme. See [Create and manage workbook themes](/docs/create-and-manage-workbook-themes).
* Specify table styles for all tables, including pivot tables and input tables, in a workbook. See [Table style settings in Workbook settings overview](/docs/workbook-settings-overview#table-style-settings).
* Apply table styles to one table element. See [Customize the table style for an individual element](#customize-the-table-style-for-an-individual-element) on this page.
* Format data in a given column or totals row or column. See [Format column and totals data](#format-column-and-totals-data) on this page.
* Format data in columns based on a condition. See [Apply conditional formatting](#apply-conditional-formatting-to-table-columns-and-cells) on this page.

## User requirements

**Before you start:** This action uses the editor panel. If you have not done so already, open the editor panel from either **Explore** or **Edit** mode; see [Workbook modes](/docs/workbook-modes-overview).

* You must be assigned an [account type](/docs/user-account-types) with the **Full explore** or **Create, edit, and publish workbooks** permission enabled.
* You must be the workbook owner or be granted **Can explore** or **Can edit** [workbook permission](/docs/folder-and-document-permissions).

## Customize the table style for an individual element

Apply a custom table style to an individual table, pivot table, or input table element. Any custom table styles override styles [set on the workbook level](/docs/workbook-settings-overview#table-style-settings).

1. Start customizing a workbook or open it for editing.
2. Select the table, pivot table, or input table element that you want to modify.
3. In the side panel, select **Format**, then click the **Table style** header to expand the section.
4. Select a table style preset, or customize the table style components as needed.

See [Customizable table style options](#customizable-table-style-options) for more.

## Available table style presets

Sigma includes two presets that automatically configure all table style options for a workbook. You can use a preset as a one-click solution or as the starting point for a custom table design.

### Spreadsheet

The **Spreadsheet** preset (default) is designed for ongoing analysis and collaboration. It’s ideal for ensuring readability and including additional context, like tooltips and images.

![Spreadsheet table styling, with a light gray header and white cells with black text, and light gray vertical and horizontal grid lines. Cell spacing is small to allow for dense data presentation.](https://files.readme.io/eb2ccc5-image.png)

### Presentation

The **Presentation** preset is designed for table viewing. It’s ideal for aligning with company branding and adding visual appeal to your workbook.

![Presentation table styling, with white header row and white cells, light gray horizontal grid lines, and large cell spacing. 4 cells of data and 1 header row show in the same amount of space as 9 rows and 1 header row in the spreadsheet style.](https://files.readme.io/7db37b0-image.png)

## Customizable table style options

You can customize any of the following table style components to meet branding and aesthetic requirements with table, pivot table, and input table elements:

* [Cell spacing](#cell-spacing)
* [Grid lines](#grid-lines)
* [Banding](#banding)
* [Header format](#header-format)
* [Subheader format](#subheader-format-pivot-tables-only)
* [Cell format](#cell-format)

### Cell spacing

The **Cell spacing** setting allows you to adjust the padding around text within table cells. You can select one of four options: **Extra small**, **Small**, **Medium**, and **Large**.

| Extra small | Small |
| --- | --- |
|  |  |
| Medium | Large |
|  |  |

### Grid lines

The **Grid lines** setting lets you manage the display of cell borders. You can select one of four options: **No grid**, **Vertical grid**, **Horizontal grid**, and **All grid**.

| No grid | Vertical grid |
| --- | --- |
|  |  |
| Horizontal grid | All grid |
|  |  |

### Banding

You can alternate the background color of the data rows. For **Banding color**, select a color. Choose **None** to remove banding from your table.

| Banding color set to None | Banding color set to #EBEBEB |
| --- | --- |
|  |  |

### Header format

The **Header** tab contains settings and tools that let you format table headers. You can customize the font type, size, weight, and color, as well as text wrap, text alignment, background color, and divider color settings.

![Pivot table with a bright blue header with white text, default gray subheaders, and black dividers.](https://files.readme.io/bc13511-image.png)

### Subheader format *(pivot tables only)*

The **Subheader** tab contains settings and tools that let you format subheader rows and columns. You can customize the font type, size, weight, and color, as well as text wrap, text alignment, and background color settings for both row or column headers.

![The same pivot table from the header format section with light blue subheaders.](https://files.readme.io/9231f92-image.png)

### Cell format

The **Cell** tab contains settings and tools that let you format data cells. You can customize the font type, size, weight, and color, as well as text wrap, text alignment, and background color settings.

> 📘
>
> ### For pivot tables, cell styles apply to both value and total cells by default. To apply different styles to pivot table total cells, see [Format column and totals data](#format-column-and-totals-data) and [Format pivot table totals](/docs/format-pivot-table-totals).

![Same pivot table from header and subheader sections with the cells having a light gray background ](https://files.readme.io/2eee376-image.png)

## Format column location in a table

To manage visibility and interactions with the columns in a table, you can format the location of columns in a table or pivot table.

Right-click a column, or select the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to customize a column:

* Choose **Freeze up to column** to freeze the position of that column and all columns to the left of the selected column. When scrolling to the right, the frozen columns remain visible. To remove a column from the frozen position, choose **Unfreeze columns**.
* Choose **Hide column** to hide the column when the table is viewed. You can reference hidden columns in formulas. Child elements created from a table with hidden columns do not include the hidden columns, but the columns can be added.

Pivot tables support freezing values columns, including totals columns, but not pivot row columns or columns set as pivot columns.

> 📘
>
> ### You cannot change the location of the totals row in a grouped table.

## Hide and show table components

To manage whether various table components are shown in a table, you can format the table components:

1. Start customizing a workbook or open it for editing.
2. Select the table or input table element you want to modify.
3. In the side panel, select **Format**.
4. Click the **Table components** header to expand the section and adjust the settings:

   | Option | Details |
   | --- | --- |
   | Show table | Whether to show the table columns and rows in the element. Turn on to show only the summary bar and title, if shown. |
   | Show collapsed columns | For a table, whether to show ungrouped columns when a grouping is collapsed. Tables without groupings are unaffected by this option. For tables with multiple groupings, See [Manage groups in a table](/docs/create-and-manage-tables#manage-groups-in-a-table). |
   | Show summary bar | Whether to show the summary bar in a table or input table. |

## Format column and totals data

Columns are formatted automatically according to the [data type](/docs/data-types-and-formats) of the column. You can change the formatting to display the column data in a different way.

If your grouped table or pivot table includes totals, you can use the toolbar to format the totals row or totals column separately from the table columns. If you apply formatting to both a totals row and a totals column, the row formatting takes precedence. For more options formatting totals in a pivot table, see [Format pivot table totals](/docs/format-pivot-table-totals).

### Change number formatting

Select a column or totals cell, then choose an option in the toolbar to change the number formatting:

* Format as currency
* Format as percent
* Decrease or increase decimal places.
* Display numeric data in a different format. See [Supported data types and formats](/docs/data-types-and-formats) for more details.

## Change column data appearance

You can change the appearance of data in a specific column using the formatting toolbar. To change the appearance of all data in a table, set the [Cell format](#cell-format). These formatting options do not affect the column headers.

After selecting a column or totals cell, choose an option in the toolbar to change the appearance of the data:

* Choose the alignment of data.
* Choose the text color.
* Choose the background color. Select the column or totals cell, then in the toolbar, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/fill-color.svg) **Background color**.
* (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/text-wrap.svg)) **Wrap text** in the column.

> 📘
>
> ### [Conditional formatting](#apply-conditional-formatting-to-table-columns-and-cells) takes precedence over formatting applied from the toolbar.

## Apply conditional formatting to table columns and cells

To format table columns and cells based on a rule, or condition, apply conditional formatting.

> 📘
>
> ### Conditional formatting takes precedence over [toolbar column formatting options](#format-columns-and-totals-data).

With conditional formatting, you can apply a specific format to one or more columns based on a formatting rule. Choose from a default formatting rule, or specify a custom formula to use, such as with a [logical function](/docs/logical-functions) or [text function](/docs/text-functions).

* Apply text formatting, such as italics, bold, underline, and text color.
* Set a background color.
* Format number or date values.
* Apply a color scale to the background color or the text color.
* Display data bars over data values, or hide the data values to show data bars only.

To apply formatting to the entire table, see [Customizable table style options](#customizable-table-style-options).

1. Click to select the table.
2. In the column menu for a column, or from the **Format** section of the side panel, select **Conditional formatting**.
3. If you open conditional formatting from the column menu, the **Conditional formatting** panel contains a default rule for the column. Otherwise, click **+ Add rule**.
4. (Optional) For **Apply to**, choose the columns to apply the conditional formatting to. You can also choose **All columns**.
5. Choose between **Single color**, **Color scale**, and **Data bars** options for the formatting.
6. For **Formatting rule**, define the conditional formatting rule. Choose a prebuilt rule, or define a custom formula.  
   As you create the rule and define the formatting, the formatting is applied to the relevant columns and cells.
7. (Optional) Add more conditional formatting rules by clicking **+ Add rule**.

> 💡
>
> ### If your table contains totals, you can apply conditional formatting only to subtotal rows and columns or grand total rows and columns.

Updated 3 days ago

---

[Create and manage tables](/docs/create-and-manage-tables)[Add hyperlinks and images to columns](/docs/add-hyperlinks-to-columns)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Customize the table style for an individual element](#customize-the-table-style-for-an-individual-element)
  + [Available table style presets](#available-table-style-presets)
  + - [Spreadsheet](#spreadsheet)
    - [Presentation](#presentation)
  + [Customizable table style options](#customizable-table-style-options)
  + - [Cell spacing](#cell-spacing)
    - [Grid lines](#grid-lines)
    - [Banding](#banding)
    - [Header format](#header-format)
    - [Subheader format (pivot tables only)](#subheader-format-pivot-tables-only)
    - [Cell format](#cell-format)
  + [Format column location in a table](#format-column-location-in-a-table)
  + [Hide and show table components](#hide-and-show-table-components)
  + [Format column and totals data](#format-column-and-totals-data)
  + - [Change number formatting](#change-number-formatting)
  + [Change column data appearance](#change-column-data-appearance)
  + [Apply conditional formatting to table columns and cells](#apply-conditional-formatting-to-table-columns-and-cells)