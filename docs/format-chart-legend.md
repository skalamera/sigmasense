# Format chart legend

# Format chart legend

Chart legends associate chart mark colors, shapes, sizes, types, and other attributes with specific groups or values. This helps users interpret data when the chart metric is distributed into categories (like regions or product types) or when a metric defines size or color scale. Most chart types in Sigma support legends that you can format to improve chart usability and readability. If you want to configure a legend that updates more than one chart, see [Create and configure a legend control](/docs/create-and-configure-a-legend-control).

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Format+chart+legend/chart-legend_intro.png)

This document explains how to change a legend’s visibility and customize its position, font size, and text color.

## User requirements

The ability to format chart legends requires the following:

* You must be assigned an [account type](/docs/user-account-types) with the **Full explore** and/or **Create, edit, and publish workbooks** permission enabled.
* You must be the workbook owner or be granted **Can explore** or **Can edit** [workbook permission](/docs/folder-and-document-permissions).

## Show or hide the legend and header

You can change the visibility of the chart legend and choose to display it with or without a header when applicable. The header specifies the variable categorized into groups or the metric that defines the chart’s size or color scale.

1. Select the chart element you want to modify on the workbook page.
2. In the editor panel, select **Format**, then click **Legend** to expand the section.
3. To change the visibility of the chart legend (including the header and labels), configure the **Show legend** field:

   * To show the legend, turn on the **Show legend** toggle.
   * To hide the legend, turn off the **Show legend** toggle.
4. To change the visibility of the legend header (when the legend is displayed), configure the **Show legend header** field:

   * To show the header, turn on the **Show legend header** toggle.
   * To hide the header and display labels only, turn off the **Show legend header** toggle.
   > 📘
   >
   > ### When you configure the **Size** property in a scatter plot, the chart element supports two separate legends for color and size. You can change the visibility of the individual legends by configuring the **Show color legend** and **Show size legend** fields.

## Change the legend position

To change the position of the legend relative to the chart:

1. Select the chart element you want to modify on the workbook page.
2. In the editor panel, select **Format**, then click **Legend** to expand the section.
3. Click **Position** and select an option from the dropdown. The available positions are shown in the matrix below:

     

   | Top | Bottom | Left | Right |
   | --- | --- | --- | --- |
   |  |  |  |  |

     

   | Top left | Top right | Bottom left | Bottom right |
   | --- | --- | --- | --- |
   |  |  |  |  |

## Customize the labels

You can customize the font size and color of the legend labels. Legend headers aren’t affected by label formatting.

1. Select the chart element you want to modify on the workbook page.
2. In the editor panel, select **Format**, then click **Legend** to expand the section.
3. To change the size of the labels, click the **Label font size** dropdown and select an option. You can choose font size values between 10 and 48.
4. To change the font color of the labels, click **Label text color**, then enter a hex value or select an option from the color palette or picker.

Updated 3 days ago

---

Related resources

* [Customize element background](/docs/customize-element-background)
* [Customize element title](/docs/customize-element-title)
* [Customize chart mark tooltip fields](/docs/customize-chart-mark-tooltip-fields)
* [Create and format trellis charts](/docs/create-and-format-trellis-charts)
* [Display chart data labels](/docs/display-chart-data-labels)
* [Display chart reference marks](/docs/display-chart-reference-marks)
* [Add trend lines](/docs/add-trend-lines)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Show or hide the legend and header](#show-or-hide-the-legend-and-header)
  + [Change the legend position](#change-the-legend-position)
  + [Customize the labels](#customize-the-labels)