# Create and configure a legend control

# Create and configure a legend control

Add a legend control to your workbook to align colors and perform interactive selection across multiple charts with shared values. With a legend control, users only need to click once to filter data across multiple charts and visualizations.

For example, you can use a legend control to create one legend for product types that you want to focus on, then target multiple charts. If the targeted charts have color split by the product type category, they can be filtered at the same time and use the same colors as defined in the legend control:

## Limitations

You can only target charts that have a color property set by category. The following chart types are not supported:

* KPI
* Box and whisker
* Waterfall
* Sankey
* Gauge

If the column used to define color categories is removed, or if the color is changed to a scale or single color, the legend control has no effect on the chart. A warning appears in the filter menu for the chart element, but the legend control still targets the chart element.

## Requirements

* You must have **Can edit** [access](/docs/folder-and-document-permissions) to the workbook.

## Add a legend control

Add a legend control to your workbook:

> 💡
>
> ### Create a legend control from an existing chart legend by right-clicking the legend and choosing **Convert to legend control**.

1. In your workbook, in edit mode, locate the **Add element bar** at the bottom of the workbook canvas.
2. In the **Add element** bar, choose **Controls** > **Legend**
3. The new control appears on the canvas.
4. In the **Properties** tab of the editor panel, choose source values for the control. See [Configure the control](#configure-the-control).
5. Specify which charts are affected when the user interacts with the control. See [Specify the target of the control](#specify-the-target-of-the-control).

> 📘
>
> ### Before the legend can be used to interact with relevant data elements, you must [select the source of the legend values](#configure-the-control) and [specify the target of the legend control](#specify-the-target-of-the-control).

## Configure the control

To configure the control behavior, click **Settings**, and choose the attributes of the legend control.

You can populate the values used by a legend control in different ways:

* Create a [manual list](#use-a-manual-list). For your control to work, the list must correspond in some way with the data in the target data elements.
* Create a [list from a preset](#use-a-list-from-a-preset) defined by Sigma.
* Use a [column in your data](#use-a-column-from-a-data-element-or-data-source).

After setting up the values used for the control, you can perform other configuration steps:

1. [Assign colors to values](#assign-colors-to-values)
2. [Group additional values as others](#group-additional-values-as-others-in-a-chart)
3. Decide whether to update the default **Control ID**. See [About control IDs](/docs/intro-to-control-elements#about-control-ids).

### Use a manual list

You can create a manual list to set custom values to manage in the legend.

1. In the **Properties** tab for the control, select the **Settings** tab.
2. For **Value source**, select **Create manual list**.
3. For **Value type**, specify the data type of the values that you add manually. The data type must match the data type of the columns targeted by the control. Choose between [Text](/docs/data-types-and-formats#text) (default), [Number](/docs/data-types-and-formats#number), [Date](/docs/data-types-and-formats#date), and [Boolean](/docs/data-types-and-formats#logical).
4. For **Values**, enter a custom list of values to use for the control. Press enter or return to add new values. You can optionally specify a display value to show in the control instead of the raw data value.

After setting up the values for the control, [assign colors to values](#assign-colors-to-values) and [group additional values as others](#group-additional-values-as-others-in-a-chart).

### Use a list from a preset

This option lets you choose from a common set of presets: Month names, Weekday names, and Date parts. After you select one of these options, your control is a manual list. You can change it, remove values, and add new values.

1. In the **Properties** tab for the control, select the **Settings** tab.
2. For **Value source**, select **Create list from preset** and choose one of the preset options:

   * Month names
   * Weekday names
   * Date parts
3. After selecting a preset list, the **Value type** and **Values** automatically update. The **Value source** changes to **Create manual list** to reflect that a preset list is a pre-populated manual list.
4. Modify the preset list as desired, removing unneeded values and changing display values. To delete a value, hover over the value and select **x**.

After setting up the values for the control, [assign colors to values](#assign-colors-to-values) and [group additional values as others](#group-additional-values-as-others-in-a-chart).

### Use a column from a data element or data source

You can also use a column from a data element or data source to provide the values for the legend control. The data source for the control element should not be any of the targeted data elements, otherwise unexpected filtering behavior could occur.

1. In the **Properties** tab for the control, select the **Settings** tab.
2. For **Value source**, select a data source or data element in use on the workbook.
3. For **Source column**, the first column of the data source is shown. Select the column to open a drop-down menu and choose the column that you want to use to populate the control.
4. [optional] To use a different, related column, as the display values for the data, turn on the toggle switch to **Set display column** and choose a display column from the same data source. For example, you might use an ID column as the data source, but a name column as the display value.

After setting up the values for the control, [assign colors to values](#assign-colors-to-values) and [group additional values as others](#group-additional-values-as-others-in-a-chart).

### Assign colors to values

Choose a color palette and optionally custom colors to apply to the legend. If you apply a workbook or organization theme, the categorical colors from the theme are used for the legend control.

1. In the **Properties** tab for the control, select the **Settings** tab.
2. For **Color assignment**, choose a color palette to use. Each legend item is assigned a color.
3. [optional] You can customize the color for each legend value by selecting the color, or customize the entire color palette. See [Add a custom color scale](/docs/add-a-custom-color-scale).

After assigning colors to values, optionally customize how other categories are handled by the legend.

### Group additional values as others in a chart

When a legend control targets a chart, values present in the targeted chart column that are not present in the legend are grouped into a separate category by default. For example, a manual list of specific values, or filtered values from a column used as the source. The category is labeled **Others**, but it can be renamed, or removed.

1. In the **Properties** tab for the control, select the **Settings** tab.
2. For **Other categories**, choose between **Use other color** (default) and **Use legend palette**.

   * **Use other color** allows you to group values in targeted charts that are not represented in the legend with a common label and color. By default, the label is **Others** and the color is gray, but you can change the label and color.
   * **Use legend palette** applies the colors used by the color palette selected in the **Color assignment** section to the values not represented in the legend.

## Specify the target of the control

Add targets to a control to specify which data elements and data sources to filter:

1. Select the control, then in **Properties**, click **Targets**.
2. Click **+Add interaction target** .
3. Select one or more charts in your workbook that you want the legend to apply to.

   Each selected chart appears under **Targets**, and the count of targets for the control increases. For each chart targeted by this control, any existing legend is hidden.

   > 💡
   >
   > ### You can show any individual chart legend after targeting a chart with a legend control.
4. Update the column targeted by the control. By default, the control targets the column used to manage the chart color. To change the target column, click the current column and choose the new target column.

   As you change the target column, the default name of the control updates to match the selected column.

## Format and design a legend control

You can format and design the legend control to match the styling of your workbook.

To review and update the formatting options, select the control, then select the **Format** tab.

### Update the element style

You can customize the style of the element, such as the background. See [Customize element background](/docs/customize-element-background).

### Update the control label

| Option | Description |
| --- | --- |
| **Show label** | Select the checkbox to show a label on the control. A label is shown by default, either "New Control" or a label that matches the column name used to populate the control. You can update the label. |
| **Bold** | Bold the label text. |
| **Text color** | Update the color of the label text. |
| **Label position** | Choose whether to position the label at the **Top** of the control, or to the **Left**. |
| **Show description** | Select the checkbox to show a description on the control. You can provide up to 200 characters of text as a description. |
| **Description formatting** | If a description is shown, you can bold the description text and update the text color. |
| **Description display** | If a description is shown, you can choose whether to display the description as a **Subtitle** or **Tooltip**, or use the **Auto** setting, which defaults to a tooltip. |

### Format legend control

You can format the appearance of the legend control:

1. After selecting the legend, select the **Format** tab.
2. Select **Legend** to review and modify the relevant options:

| Option | Description |
| --- | --- |
| **Orientation** | How to display the legend control options. Choose **Vertical** (default), **Horizontal**, or **Horizontal with wrap**. |
| **Font size** | Font size to use for the legend labels. |
| **Text color** | Text color to use for the legend labels. |
| **Mark shape** | Shape to use for the legend marks. Choose **Circle**, **Square** (default), **Cross**, **Diamond**, **Triangle**, **Solid line**, **Dashed line**, or **Dotted line**. |

Updated 3 days ago

---

[Top N filter](/docs/top-n-filter)[Work with controls](/docs/work-with-controls)

* [Table of Contents](#)
* + [Limitations](#limitations)
  + [Requirements](#requirements)
  + [Add a legend control](#add-a-legend-control)
  + [Configure the control](#configure-the-control)
  + - [Use a manual list](#use-a-manual-list)
    - [Use a list from a preset](#use-a-list-from-a-preset)
    - [Use a column from a data element or data source](#use-a-column-from-a-data-element-or-data-source)
    - [Assign colors to values](#assign-colors-to-values)
    - [Group additional values as others in a chart](#group-additional-values-as-others-in-a-chart)
  + [Specify the target of the control](#specify-the-target-of-the-control)
  + [Format and design a legend control](#format-and-design-a-legend-control)
  + - [Update the element style](#update-the-element-style)
    - [Update the control label](#update-the-control-label)
    - [Format legend control](#format-legend-control)