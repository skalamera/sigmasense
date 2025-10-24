# Add a custom color scale

# Add a custom color scale

When you format a chart, or conditionally format a table column, you can apply a single color or a color scale, among other options. Sigma includes several predefined color palettes, but you can also create your own:

* [Choose a predefined color scale palette](#choose-a-predefined-color-scale-palette)
* [Set a custom color scale palette](#set-a-custom-color-scale-palette)

You can add a color scale palette at the [organization level as part of a theme](/docs/create-and-manage-workbook-themes), at the [workbook level in the workbook settings](/docs/workbook-settings-overview), or at the element level for a specific data element. The following elements support color scales:

* [Bar chart](/docs/build-a-bar-chart#configure-mark-colors)
* [Funnel chart](/docs/build-a-funnel-chart#configure-mark-colors)
* [Gauge chart](/docs/build-a-gauge-chart#configure-chart-colors)
* [Geography map](/docs/build-a-geography-map#configure-mark-colors)
* [Scatter plot](/docs/build-a-scatter-plot#configure-mark-colors)
* Tables, pivot tables, and input tables with [conditional formatting](/docs/format-and-customize-a-table#apply-conditional-formatting-to-table-columns-and-cells).

![Bar chart next to a table, showing votes for a lunch option, both with the same custom sequential color scale informed by a custom color scale.](https://files.readme.io/c3b5f8ff22745f29a4a119e41293df1a095cc54ec2ae1fde1d3988405ec716e1-custom-scale-viz-conditional.png)

## User requirements

* To edit a chart, you must have **Can edit** or **Can explore** [access](/docs/folder-and-document-permissions#document-permissions) to the individual workbook.
* You must be in **Edit** or **Explore** mode for the workbook. See [workbook modes overview](/docs/workbook-modes-overview).

## Choose a predefined color scale palette

1. Open the color options for the chart in the editor panel, or open conditional formatting options for a table and select **Color scale**.
2. Select the dropdown menu for the color palette to review other color choices.
3. Use the dropdown menu to choose between **Sequential** (default) or **Diverging** palettes.
4. Select a palette.
5. (Optional) To reverse the default colors, turn on the switch to **Reverse color scale**.
6. (Optional) To customize the color at specific data values, turn on **Customize domain**, then specify a **Minimum value**, **Middle value**, and **Maximum value** in the data.
7. (Optional) To use distinct colors instead of a gradient color scale, set **Steps** to a value between **1** and **5**, depending on your data values. You can use this option with the color domain settings to more granularly define the color settings for specific data values. Set **Steps** to **None** to return to a gradient color scale.
8. (Optional) For conditional formatting only, you can enable **Format null values as zero** to apply formatting to null values. The data value does not update but cells with null values reflect conditional formatting.

To create a custom color palette to use for sequential or diverging scales, see [Set a custom color scale palette](#set-a-custom-color-scale-palette).

## Set a custom color scale palette

To set a custom color scale palette for a data element or conditional formatting of table cells:

1. Open the color options for the chart in the editor panel, or open conditional formatting options for a table and select **Color scale**.  
   ![Conditional formatting color scale options, showing a selected column to apply the formatting to (Votes) and the selected palette to apply as a background scale.](https://files.readme.io/9952a76b694549105700456099be108939e7ce7511f48f50ae953bd783654e6a-custom-scale-conditional.png)
2. Select the dropdown menu for the color palette to review other color choices.
3. (Optional) Select a default palette.
4. Select **Custom** to configure a custom color palette. The default colors match the default palette selected when you opened the custom option, or the default palette set in the selected workbook theme.  
   ![Custom palette options described in surrounding steps](https://files.readme.io/a970e7fcb310481a22b65ec93dc17241edd433ace706425ea6a0ae020e1e7b2c-custom-color-scale.png)
5. For each color that you want to customize, select the color block, then choose a new color by doing one of the following:

   * Select one of the provided standard colors.
   * Enter a hex code for the color.
   * Use the eyedropper.
   * Choose a color with the color picker.
6. (Optional) To reverse the colors, turn on **Reverse color scale**.
7. (Optional) To customize the color at specific data values, turn on the switch for **Customize domain**, then specify a **Minimum value**, **Middle value**, and **Maximum value** in the data.
8. (Optional) To use distinct colors instead of a gradient color scale, set **Steps** to a value between **1** and **5**, depending on your data values. You can use this option with the color domain settings to more granularly define the color settings for specific data values. Set **Steps** to **None** to return to a gradient color scale.
9. (Optional) For conditional formatting only, you can enable **Format null values as zero** to apply formatting to null values. The data value does not update but cells with null values reflect conditional formatting.

To make a custom color scale available to other elements in the workbook, set a custom scale of sequential colors or diverging colors in the [workbook settings](/docs/workbook-settings-overview). This sets a default custom color scale. You can override it on a specific element. After overriding a workbook-level or theme-level custom color scale, you can choose **Revert to default** to use the workbook-level or theme-level custom color scale again.

Updated 3 days ago

---

[Add trend lines](/docs/add-trend-lines)[Filter data](/docs/filter-data)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Choose a predefined color scale palette](#choose-a-predefined-color-scale-palette)
  + [Set a custom color scale palette](#set-a-custom-color-scale-palette)