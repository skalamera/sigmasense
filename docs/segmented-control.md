# Create and configure a segmented control

# Create and configure a segmented control

A segmented control has between one and seven sections that a user can select to filter data in target elements. The segments in the control are single-select, so each segment acts like a radio button, selecting the matches and excluding other data.

You might choose to use a segmented control as an alternative to a list control to present a small set of relevant values to choose from. You can also use a segmented control like a toggle switch, to change between different views of related content. For example, if you segment your webinar registrations by customer type, you can build one workbook with all relevant data and use a segmented control to switch between relevant customer groups: new, prospect, existing, all.

## Create a segmented control

To create a segmented control, do the following:

1. In your workbook, in edit mode, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add element**.
2. On the left navigation panel, scroll to **Control elements** and select **Segmented control**.  
   The new segmented control appears on the canvas.
3. In the **Element properties** panel, choose whether to use column-based or manual values for the control. See [Configure the control](#configure-the-control).
4. Specify what changes happen when the user interacts with the control. See [Specify the target of the control](#specify-the-target-of-the-control).

> 📘
>
> ### Before a control can filter relevant data elements, you must [specify the target](#specify-the-target-of-the-control), and [select the source of segments](#configure-the-control).

## Configure the control

To configure the control behavior, click **Settings**, and choose the attributes of the segmented control.

You can populate the values used by a segmented control in different ways:

* Create a [manual list](#use-a-custom-list). For your control to work, the list must correspond in some way with the data in the target data elements.
* Create a [list from a preset](#use-a-list-from-a-preset) defined by Sigma.
* Use a [column in your data](#use-a-column-from-a-data-element-or-data-source). The first 7 values in the column are used for the control. You can change the sort order to modify which column values are used.

After the control values are populated, you can perform additional configuration steps:

1. (Optional) To allow users of the control reset the control so nothing is selected, select the checkbox to **Show clear option**. By default, the label for this option is **None**, but you can change it.
2. (Optional) To make sure that targeted data elements only load after a user makes a selection on the control, select the checkbox for **Required**.
3. (Optional) Decide whether to update the default **Control ID**. See [About control IDs](/docs/intro-to-control-elements#about-control-ids).

### Use a manual list

You can create a manual list to select custom values. You still reference a data table or a data element, but you can directly name the data segments you want to use, regardless of their relative frequency in the data.

1. In the **Properties** tab for the control, select the **Settings** tab.
2. For **Value source**, select **Create manual list**.
3. For **Value type**, specify the data type of the values that you add manually. The data type must match the data type of the columns targeted by the control. Choose between [Text](/docs/data-types-and-formats#text) (default), [Number](/docs/data-types-and-formats#number), [Date](/docs/data-types-and-formats#date), and [Boolean](/docs/data-types-and-formats#logical).
4. For **Values**, enter a custom list of values to use for the control. Press enter or return to add new values. You can optionally specify a display value to show in the control instead of the raw data value.

For example, you can create a manual list of text values that correspond to the states in the New England region of the United States: Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, and Vermont.

You can specify the display values as the full state names, but use the state abbreviations as the data values to correspond with a column in the targeted data element.

![Custom list of New England states, set up as described](https://files.readme.io/167941f28a0bc1d33720466ad57feefecb298f7081d57e0e058838250ac2dc90-control-manual-list.png)

### Use a list from a preset

This option lets you choose from a common set of presets: Month names, Weekday names, and Date parts. After you select one of these options, your control is a manual list. You can change it, remove values, and add new values.

1. In the **Properties** tab for the control, select the **Settings** tab.
2. For **Value source**, select **Create list from preset** and choose one of the preset options:

   * Month names
   * Weekday names
   * Date parts
3. After selecting a preset list, the **Value type** and **Values** automatically update. The **Value source** changes to **Create manual list** to reflect that a preset list is a pre-populated manual list.
4. Modify the preset list as desired, removing unneeded values and changing display values. To delete a value, hover over the value and select **x**.

### Use a column from a data element or data source

1. In the **Element properties** panel for the control, select the **Settings** tab.
2. For **Value source**, select a data source or data element in use on the workbook.
3. For **Source column**, the first column of the data source is shown. Select the column to open a drop-down menu and choose the column that you want to use to populate the control.

   By default, the top 7 most frequent values in that column are used for the control. Select **Sort** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/sort_desc.svg)) to change the sort order from the default of **Descending by count** to **Ascending by count**, **Ascending by alphanumeric**, or **Descending by alphanumeric**. Custom sort orders are not supported.
4. (Optional) To use a different, related column, as the display values for the data, turn on the toggle switch to **Set display column** and choose a display column from the same data source. For example, you might use an ID column as the data source, but a name column as the display value.
5. (Optional) To allow users of the control reset the control so nothing is selected, select the checkbox to **Show clear option**. By default, the label for this option is **None**, but you can change it.
6. (Optional) To make sure that targeted data elements only load after a user makes a selection on the control, select the checkbox for **Required**.
7. (Optional) Decide whether to update the default **Control ID**. See [About control IDs](/docs/intro-to-control-elements#about-control-ids).

## Specify the target of the control

Add targets to a control to specify which data elements and data sources to filter:

1. Select the control, then in **Element properties**, click **Targets**.  
   ![Element properties panel with the control selected, hovering over the Targets tab between Settings and Synced.](https://files.readme.io/b66c7287052e7fc3167b8c33dfe1799a4d0271a1d94db87bda2ee5b5d32e69c9-control-targets.png)
2. Click **+ Add filter target**.
3. Select one or more elements in your workbook that you want to be changed by the control.  
   In this example, the data element table `VIOLATION_TYPES` is selected. The table is on the same page of the workbook as the control.  
   ![Navigate the dropdown menu to select one or more data sources or data elements to target with the control.](https://files.readme.io/fd1205b9d88d7f6ef1df61ccefe9cd9587968d62a3d02b3c34229043080cae30-control-choose-target.png)  
   The table appears under **Targets**, and the count of targets for the control increases to 1.  
   As you add other targets to this control, the count increases.  
   ![Targets tab showing a value of 1 and showing the table as an affected data element.](https://files.readme.io/649b5c3d1e374e00c7cb6437fd48d70b0242fc3733a44789788efcbe7047057e-control-target-column.png)
4. Update the column targeted by the control. By default, the control targets the first column of the table. To change the target column, click the current column and choose the new target column. In this example, the target column **Risk Category** is correct for the control.

   As you change the target column, the default name of the control updates to match the selected column. In this example, the name of the filter control was **New Control**, then it changed to **Risk Category** when the table was added as a target.

## Format and design a segmented control

You can format and design the segmented control to match the styling of your workbook. To review and update the formatting options, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/element-format.svg) **Element format**.

### Update the element style

You can customize the style of the element, such as the background. See [Customize element background](/docs/customize-element-background),

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

### Update the alignment of the control

You can align a segmented control within the element boundaries on the workbook canvas.

Choose from the following horizontal alignment options:

| Alignment setting | Example |
| --- | --- |
| **Left align** () (default) | Segmented control aligned to the left of an element showing top 7 traffic sources above a bar chart showing top 10 traffic sources |
| **Right align** () | Segmented control aligned to the right of an element showing top 7 traffic sources above a bar chart showing top 10 traffic sources |
| **Stretch** () | Segmented control stretched to the entire width of an element showing top 7 traffic sources above a bar chart showing top 10 traffic sources |

Updated 3 days ago

---

[Create and manage a control element](/docs/create-and-manage-a-control-element)[Drill down control](/docs/drill-down-control)

* [Table of Contents](#)
* + [Create a segmented control](#create-a-segmented-control)
  + [Configure the control](#configure-the-control)
  + - [Use a manual list](#use-a-manual-list)
    - [Use a list from a preset](#use-a-list-from-a-preset)
    - [Use a column from a data element or data source](#use-a-column-from-a-data-element-or-data-source)
  + [Specify the target of the control](#specify-the-target-of-the-control)
  + [Format and design a segmented control](#format-and-design-a-segmented-control)
  + - [Update the element style](#update-the-element-style)
    - [Update the control label](#update-the-control-label)
    - [Update the alignment of the control](#update-the-alignment-of-the-control)