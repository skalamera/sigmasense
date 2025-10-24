# Customize element title

# Customize element title

Titles allow you to identify individual data elements (visualizations, tables, and pivot tables) and input tables in workbooks. You can customize element titles to provide context, communicate insights, and improve accessibility.

This document explains how to change title visibility and create custom titles using dynamic values, formatting tools, and descriptions.

## User requirements

The ability to customize workbook element titles requires the following:

* You must be assigned an [account type](/docs/user-account-types) with the **Create, edit, and publish workbooks** and/or **Full Explore** permission enabled.
* You must be the workbook owner or be granted **Can explore** or **Can edit** [workbook permission](/docs/folder-and-document-permissions).

## Default element titles

Sigma creates default element titles that depend on the element type.

* **Visualizations**: Titles are auto-generated based on the metric value and other data attributes applied to the chart properties. Until a user customizes a visualization element title, Sigma auto-updates it whenever chart properties are modified. Once the title is customized, auto-updates no longer apply.
* **Tables**: Titles reflect the data source (database table name, CSV filename, or parent element) or type of data integration (custom SQL, join, or union).
* **Pivot table**: Titles default to `New Pivot Table`.
* **Input table**: Titles default to `New Input Table` or `New Linked Input Table`.

## Show or hide the title

Change the visibility of an element’s title.

1. Start customizing a workbook or open it for editing, then select the element you want to modify.
2. In the side panel, select **Format**, then click the **Title** header to expand the section.
3. To change the visibility of the element title, turn on or turn off the **Show title** toggle:

   * To display the title, turn on the toggle.
   * To hide the title, turn off the toggle.

## Edit the title text

You can edit an element’s title text in two ways: in the **Title** section of the **Format** tab of the side panel or directly in the element using inline editing.

When you update the title in the side panel, you can edit the text and format the title. Editing the title directly on the element lets you quickly update the text without navigating away from the element.

### Element format panel

1. Start customizing a workbook or open it for editing, then select the element you want to modify.
2. In the side panel, select **Format**, then click the **Title** header to expand the section.
3. In the text field below **Show title**, enter your preferred title, then press `Enter` or click anywhere outside the text field to apply the change.

### Inline edit

1. Start customizing a workbook or open it for editing.
2. Locate the element you want to modify, then click the title to enable text editing.
3. Enter your preferred title, then press `Enter` or click anywhere outside the text field to apply the change.

## Create a dynamic title

Use dynamic values to create a more relevant and detailed element title that adapts to selected control values. For more details about referencing control values in formulas, see [Reference control values as parameters](/docs/parameters-in-workbooks).

1. Start customizing a workbook or open it for editing, then select the element you want to modify.
2. Start editing the title using either method described in the [Edit the title text](#edit-the-title-text) section.
3. In the title text, enter `=` where you want to add a dynamic value. Sigma immediately displays an overlay containing a formula bar and **Reference label** field.
4. Configure the dynamic value:

   1. In the formula bar, enter a control ID or an element title/column enclosed in square brackets. For example, `[date-range]` or `[Plugs_Electronics/Store Region]`.
      You can also use functions to generate custom calculations or transform control and column values as needed.

      > 💡
      >
      > When referencing a date or date range control, use [date functions](/docs/date-functions) to customize the value display.
      >
      > For example, if 01/01/2024 is the end date of the selected date range, enter `DateFormat([date-range].end, “%Y-%m”)` to display the dynamic title value as `2024-01`.
      >
      > Alternatively, enter `DateFormat([date-range].end, “%b %Y”)` to display the dynamic title value as `Jan 2024`.
   2. [optional] In the **Reference label** field, enter a label that identifies the dynamic value. This label is used in place of the dynamic value when the element title is referenced elsewhere in the product, including in formulas, the workbook lineage, and the list of available element sources.

![Title editing in the sidebar with the dynamic text popover shown featuring the described formula of DateFormat([date-range].start, “%b %Y”) and a reference label of date-range-start-sold ](https://files.readme.io/db8c2e90822fe5b99340c49dfb0fb31f6510a013ba3d32df6cd160ce4b83307d-element-dynamic-title.png)

## Customize the title format

Customize the title font weight, size, and color, and determine the title text alignment.

1. Start customizing a workbook or open it for editing, then select the element you want to modify.
2. In the side panel, select **Format**, then click the **Title** header to expand the section.
3. Use the formatting tools to customize the title as needed:

   |  |  |  |
   | --- | --- | --- |
   |  | **Bold** | Change the font weight. When bold font is applied, the icon displays a gray background. |
   |  | **Font color** | Enter a hex value or select an option from the color palette or picker. |
   |  | **Font size** | Select a font size (10-48px). |
   |  | **Alignment** | Select the text alignment within the element (left, center, or right). |

## Add a description

Provide extra context about an element and display it as a subtitle or tooltip.

> 💡
>
> Give your elements concise titles and use descriptions to convey additional details about the element contents.

1. Start customizing a workbook or open it for editing, then select the element you want to modify.
2. In the side panel, select **Format**, then click the **Title** header to expand the section.
3. Turn on the **Show description** toggle.
4. Enter a description (up to 200 characters), and use the formatting tools to customize the text color, size, and weight as needed.
5. In the **Description display** section, select an option to determine how the description displays within the element:

   |  |  |
   | --- | --- |
   | **Auto** | Displays as a subtitle or tooltip depending on the height of the element.  When the height is 13 grid rows or more, the description is shown as a subtitle.  When the height is 12 grid rows or fewer, the description is shown as a tooltip. |
   | **Subtitle** | Displays beneath the element title.  Subtitles wrap text in up to two lines. When the text extends beyond the second line, it is truncated with an ellipsis (...). A user can view the full description by hovering over the truncated subtitle. |
   | **Tooltip** | Displays as an information icon () tooltip next to the element title. |

![A chart with a tooltip description](https://files.readme.io/e4722fda6918c5a39daa5bfebb93973a618809fad91cf9c988f2720373fb9e54-description-tooltip.png)

## Customize no data text

To customize the text that appears when an element has no data to display, such as when a user inputs an invalid value into a control targeting the data element, do the following:

1. Start customizing a workbook or open it for editing, then select the element you want to modify.
2. In the side panel, select **Format**, then click the **Title** header to expand the section.
3. For **Display label for no data**, enter text to use instead. For example "Enter a valid store name" to reference a text control that targets a chart.

![Products sold by quarter chart with a Store name text input control targeting it. The text input control has 'My Store' as the input and the chart is blank and displays text 'Enter a valid store name'](https://files.readme.io/e5fd4846f120963a6e2c68394876642bd1c849f9ad1e17817544f212eef69ded-custom-no-data.png)

Updated 3 days ago

---

[Workbook settings overview](/docs/workbook-settings-overview)[Customize element background and styles](/docs/customize-element-background-and-styles)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Default element titles](#default-element-titles)
  + [Show or hide the title](#show-or-hide-the-title)
  + [Edit the title text](#edit-the-title-text)
  + - [Element format panel](#element-format-panel)
    - [Inline edit](#inline-edit)
  + [Create a dynamic title](#create-a-dynamic-title)
  + [Customize the title format](#customize-the-title-format)
  + [Add a description](#add-a-description)
  + [Customize no data text](#customize-no-data-text)