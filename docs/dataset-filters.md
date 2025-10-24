# Dataset filters

# Dataset filters

Filters allow you to limit your data to show only rows that meet certain criteria. Sigma worksheet filters live in the dataset worksheet control panel, which is positioned directly to the left panel. This positioning allows you to modify your filter values while simultaneously watching your data respond in real time.

## User requirements

To use filters in datasets, you must be assigned an [account type](/docs/license-and-account-type-overview) with the **Create, edit, and publish datasets** permission enabled.

## Anatomy of a filter

### Control panel

Filters live in the worksheet control panel, located on the left side of the dataset worksheet tab. This panel also includes any Worksheet Totals and Parameters.
![](https://files.readme.io/15ae7b2-47_-_filters-left-inspector.png)

### Filter list

All existing filters are available in the control panel under the header FILTERS. Disabled filters are greyed out.
![](https://files.readme.io/584aef8-48_-_disabled-filter.png)

### Filter

All filter types have the same basic structure when displayed in the filter list.

The following screenshots show components of an “Include” filter and a "Range" filter.

![](https://files.readme.io/b19488d-49-filter-1234.png)
![](https://files.readme.io/4df978b-50_-_filter-56.png)

1. Column type icon
:   This icon shows the type of column being filtered.

2. Column name
:   This is the name of the column used for the filter. A worksheet may have multiple filters on the same column.

3. Filter type
:   This label specifies the [filter type](/docs/dataset-filters#filter-types).

4. Filter value input
:   This input component will display differently for different filter types. Use it to input the values you would like to filter on. The worksheet data will update to reflect your filter value selection in real time.

5. Disable/Enable filter toggle
:   Only visible on hover. Click the toggle to disable or re-enable a filter. It will be grey if the filter is disabled.

6. Filter menu
:   Only visible on hover. Open this menu to see additional actions including edit and delete.

7. Include Nulls Checkbox
:   This allows you to choose whether you would like to include nulls in your filtered column. The 'Include Nulls' checkbox is not applicable to Include/Exclude filters. Instead, null is listed as a value in the filter value input list. It is not applicable to Text Match filters.

![](https://files.readme.io/8fd531d-51_-_filter7.png)

### The Filter Modal

The filter modal allows Sigma Creators to create and edit filters. Modal field options vary depending on the column type and filter type you have selected.

![](https://files.readme.io/344c926-52_-_filter-modal.png)

Unlike when you select values directly on a filter in the control panel, your value selection in the filter modal will only be applied to your worksheet data after you click **Save**.

## Filter Types

A filter’s filter type dictates what values can be set on your filter and the format in which they can be selected. For example, an “include” filter provides a list of data values for you to choose from, while a “range” filter requests minimum and/or maximum values.

Sigma worksheets support seven filter types. The filter types you can choose from for each given filter are dependent on the [type of column](/docs/data-types-and-formats) that the filter targets. Json columns are the only column type that cannot be filtered on. To filter on json data, you will first need to [extract data from the json object](/docs/data-modeling-tutorial).

Include
:   Default filter type

    Selected values will be included in your data. All other values will be excluded.

    **Value input type:** List of selectable values

    **Supported column type:** Text, Number, Datetime

Exclude
:   Selected values will be excluded from your data.

    **Value input type:** List of selectable values

    **Supported column type:** Text, Number, Datetime

Range
:   Only values within the specified range will be included in your data.

    The range is min/max inclusive.

    **Value input type:** Min/Max numeric input boxes

    **Supported column type:** Number

Date Range
:   This filter type supports both fixed and relative date types. Only values within the specified range will be included in your data.

    The range is min/max inclusive.

    **Value input type:** A single input box with the option to select fixed and/or relative dates for both min and max values.

    **Supported column type:** Date (Fixed), Date (Relative)

Limit
:   Ranks and limits data in the column based on your specifications.

    **Value input type:** A list of rank order/direction (eg “First N”); A numeric input for the number of values to include; rank type (i.e., [Rank](/docs/rank), [RankDense](/docs/rankdense), [RowNumber](/docs/rownumber))

    **Supported column type:** Text, Number, Date

Text Match
:   The filter will search for full and partial matches between your input text and your data’s values.

    **Value input type:** A list of formulas to match on (i.e., [Contains](/docs/contains), [Starts with](/docs/startswith), [Ends with](/docs/endswith), [Like](/docs/like)) as well as their value excluding counterparts (i.e., Does not contain, Does not start with, Does not end with, and Not like); A text input box for text to search for; A checkbox for case sensitivity.

    **Supported column type:** Text

Boolean
:   True or False

    Filters on true, false, and null

    **Value input type:** A list of values

    **Supported column type:** Logical: True, False

## Create a filter

Create a filter from the control panel

1. If the **control panel** is not already open, open it by clicking either the collapsed CONTROLS bar or the **Show Controls** button in the worksheet toolbar.
   ![](https://files.readme.io/c2bbe1f-53_-_show-controls.png)
2. Click on the **+** icon on the right side of the panel’s **FILTERS** section.
   ![](https://files.readme.io/1c7d692-54_-_add_new_filter.png)
3. The Add Filter modal will now appear on your screen, prompting you to select a column to filter from your worksheet.
   Select a **Column** from the drop down list.
   **Note**: The type of column you select will determine the steps that follow. This is because `filter type` and `filter values` are dependent on column type. For this example, we will select a Text (abc) column.
   ![](https://files.readme.io/f017774-55_-_new_filter_type_popup.png)
4. Next, select a **Filter Type** from the dropdown menu.
   For this example, use the default ‘Include Values’ filter type.
   ![](https://files.readme.io/aa1f101-56_-_filter_type_select.png)
5. Under **Filter value**, select the value(s) you would filter on.
   Both Include and Exclude filter types provide a value list ranked by count. Scroll through the ordered list or use search to find and select values.
   ![](https://files.readme.io/15fb580-57_-_include_values.png)
6. Click **Save** to save your new filter.Your new filter will now appear in the worksheet control panel, where you can modify selected values alongside your worksheet’s spreadsheet interface.
   ![](https://files.readme.io/4d4aaa2-58_-_completed_filter_add.png)

### Create a filter from a column menu

1. Open the column menu on the column you would like to filter.
2. Select **Add Filter...** from the menu.
3. The **Add Filter** modal will now appear on your screen with the column selected and the default `Filter Type` set.
   **Note**: The type of column you selected will determine the steps that follow. This is because `filter type` and `filter values` depend on column type. For this example, we selected a Numeric (123) column.
   ![](https://files.readme.io/0cb4258-59_-_range-filter.png)
4. [optional] Change your **filter type**.
   For this example, use the default ‘Range’ filter type.
5. Under **Filter value**, select the range you want to filter on. You can choose to specify both min and max values or leave one end of the range open.
   ![](https://files.readme.io/390bcfa-60_-_numeric_range_filter.png)
6. After selecting your values, you can choose whether or not to include null values in your filter. Nulls are included by default.
7. Click **Save** to save your new filter.

   Your new filter appears in the worksheet control panel, where you can modify selected values alongside your worksheet’s spreadsheet interface.
   ![](https://files.readme.io/7cd9e6c-61_-_numeric_filter_complete.png)

### Filter from a cell menu

It is possible to create new include/exclude type filters and modify existing ones using the context menu on a table cell. To filter on a select cell value:

1. Right click on the cell you want to filter on. The the **cell menu** opens.
2. From the menu, select **Include`<cell value>`** or **Exclude`<cell value>`** .
   ![](https://files.readme.io/c772da8-62_-_filter_from_cell.png)
   Your selection is applied to the worksheet and reflected in the control panel **Filters** list.

## Modify a filter’s value selection

Changes made to a filter’s value selection from the control panel will automatically be applied to your worksheet’s data. The value selection input field is dependent on the filter type.
![](https://files.readme.io/e1d3ec9-63-change-filter-value.gif)

## Edit a filter

The following instructions will show you how to open the ‘Edit Filter’ modal. From here, you can edit any structural detail of the filter.

Changes will not be made until you hit **Save**.

### Edit a filter from the control panel

1. Open the **control panel**.
2. In the FILTERS list, hover over the control you would like to edit, and click the caret icon to **open the dropdown menu**.
3. Click **Edit Filter**.

   ![](https://files.readme.io/413a412-64_-_edit_filter.png)

   The '**Edit Filter**' modal opens. Make your desired changes and click **Save**.

## Delete a filter

The following instructions will permanently delete your filter. Alternatively, you can choose to [temporarily disable the filter](#temporarily-disabling-a-filter).

1. Open the [**control panel**](#control-panel).
2. In the FILTERS list, hover over the filter you would like to delete, and click the caret icon to **open the dropdown menu**.
3. Click **Delete Filter**.

## Temporarily disabling a filter

1. Open the [**control panel**](#control-panel).
2. In the **FILTERS** list, hover over the control you would like to disable.
3. Click the blue toggle switch to disable the filter.
   ![](https://files.readme.io/5a50ce4-65_-_disable_filter.png)

## Filter permissions

If you are a Sigma Creator or Admin, you can view, create, edit, and delete filters on the dataset worksheets you have access to. However, as with other worksheet changes, you must have edit permissions on the worksheet to publish your work. If you have view-only access, you may save your worksheet changes as a new worksheet; see [Data permissions](/docs/data-permissions).

Updated 3 days ago

---

[Dataset Totals](/docs/dataset-totals)[Create and manage dataset parameters](/docs/create-and-manage-dataset-parameters)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Anatomy of a filter](#anatomy-of-a-filter)
  + - [Control panel](#control-panel)
    - [Filter list](#filter-list)
    - [Filter](#filter)
    - [The Filter Modal](#the-filter-modal)
  + [Filter Types](#filter-types)
  + [Create a filter](#create-a-filter)
  + - [Create a filter from a column menu](#create-a-filter-from-a-column-menu)
    - [Filter from a cell menu](#filter-from-a-cell-menu)
  + [Modify a filter’s value selection](#modify-a-filters-value-selection)
  + [Edit a filter](#edit-a-filter)
  + - [Edit a filter from the control panel](#edit-a-filter-from-the-control-panel)
  + [Delete a filter](#delete-a-filter)
  + [Temporarily disabling a filter](#temporarily-disabling-a-filter)
  + [Filter permissions](#filter-permissions)