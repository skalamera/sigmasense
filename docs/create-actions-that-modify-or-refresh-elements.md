# Create actions that modify or refresh elements

# Create actions that modify or refresh elements

Workbooks support actions that determine column visibility, update element groupings and properties, change axis scales, refresh data, and select tabs in tabbed containers. These actions enable interacting users to quickly view and drill into different underlying data segments, tailor chart presentations, and ensure elements display the most up-to-date data.

This document explains how to configure the **Modify element**, **Refresh element**, and **Select tab** actions. For more information about actions in Sigma, see [Intro to actions](/docs/intro-to-actions).

## User requirements

> 📘
>
> The following requirements apply to users who configure actions. Users who access and interact with a workbook can typically trigger all existing actions within it. Any restrictions are noted in this document.

The ability to configure actions requires the following:

* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Full explore** or **Create, edit, and publish workbooks** permission enabled.
* You must be the workbook owner or be granted **Can explore**1 or **Can edit** [access to the workbook](/docs/folder-and-document-permissions).

1If you’re granted **Can explore** access to the workbook, you can configure actions in custom, saved, and shared views. Actions saved to views do not apply to the workbook’s published version.

## Modify elements

The **Modify elements** action supports the following effects:

* [Show columns](#show-columns)
* [Hide columns](#hide-columns)
* [Move columns](#move-columns)
* [Swap columns](#swap-columns)
* [Set axis scale](#set-axis-scale)

### Show columns

Create an action that shows columns (ungrouped only) in the target element. Columns can be shown based on a static selection or when column names match selected control values in the trigger element.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

|  |  |
| --- | --- |
| **Action** | Select **Modify element**. |
| **Target element** | Select an element to modify. |
| **What to modify** | Select **Show columns**, then choose one or more columns to show in the target element.  If the trigger element is a **List values** or **Segmented** control, choose an option in the secondary field:   * **From a static selection**: Allows you to select specific columns to show in the target element.  *When you choose **All columns**, user interaction triggers the target element to show all columns that existed at the time you configured the action. To show columns added post-configuration, you must [update the action](/docs/view-and-manage-existing-actions).*  * **With names matching control values**: Dynamically shows columns in the target element when the column names match selected control values in the trigger element.  *When a user interacts with the control, the target element shows all columns with names that match selected control values (selected checkboxes in a **List values** control, or the selected segment in a **Segmented** control) and hides all columns with names that match unselected control values (cleared checkboxes in a **List values** control, or unselected segments in a **Segmented** control). Columns with names that don't match any control values are unaffected by the action and may be shown or hidden based on other configurations and actions.* |
| **Hide unselected columns** | Select the checkbox to hide the remaining columns (not selected in the **What to modify** field), or keep the checkbox clear to continue showing all columns already displayed in the target element. |

> 💡
>
> ### To set column names as the control values, use one of the following methods:
>
> * Enter column names in an input table column, then select that column as the control element's value source.
> * Create a manual list of column names as the control element's values source.

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

### Hide columns

Create an action that hides columns (ungrouped only) in the target element. Columns can be hidden based on a static selection or when column names match selected control values in the trigger element.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

|  |  |
| --- | --- |
| **Action** | Select **Modify element**. |
| **Target element** | Select an element to modify. |
| **What to modify** | Select **Hide columns**, then choose one or more columns to hide in the target element.  If the trigger element is a **List values** or **Segmented** control, choose an option in the secondary field:   * **From a static selection**: Allows you to select specific columns to hide in the target element.  *When you choose **All columns**, user interaction triggers the target element to hide all columns that existed at the time you configured the action. To hide columns added post-configuration, you must [update the action](/docs/view-and-manage-existing-actions).* * **With names matching control values**: Dynamically hides columns in the target element when the column names match selected control values in the trigger element.  *When a user interacts with the control, the target element hides all columns with names that match selected control values (selected checkboxes in a **List values** control, or the selected segment in a **Segmented** control) and shows all columns with names that match unselected control values (cleared checkboxes in a **List values** control, or unselected segments in a **Segmented** control). Columns with names that don't match any control values are unaffected by the action and may be shown or hidden based on other configurations and actions.* |
| **Show unselected columns** | Select the checkbox to show the remaining columns (not selected in the **What to modify** field), or keep the checkbox clear to continue hiding all columns already hidden in the target element. |

> 💡
>
> ### To set column names as the control values, use one of the following methods:
>
> * Enter column names in an input table column, then select that column as the control element's value source.
> * Create a manual list of column names as the control element's values source.

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

### Move columns

Create an action that moves columns into or out of a table grouping, pivot table property (row, column, or value), or chart property (axis, color, tooltip, etc.) in the target element. Columns can be moved based on a static selection or when column names match selected control values in the trigger element.

> 📘
>
> ### If the target element is a table, the **Move columns** option is only available when the table contains existing groupings.
>
> If the target element is a pivot table or chart, the action doesn't remove an existing column from the target property unless the property only supports one column.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

|  |  |
| --- | --- |
| **Action** | Select **Modify element**. |
| **Target element** | Select an element to modify. |
| **What to modify** | Select **Move columns**, then select a grouping or property from the target element.  *The **to base** option moves a column out of a grouping or property and into the base underlying data. Other available groupings and properties depend on the type of target element selected* |
| **Which column** | Most elements only support the **From a static selection** option, which allows you to choose a specific column to move into or out of the target grouping or property. In these cases, use the secondary field to select the column to move.  If the trigger element is a **List values** or **Segmented** control, you can choose the **Column names matching control values** option to dynamically move columns when their names match selected control values in the trigger element. When you choose this option, all columns (in any grouping or property) with names that match unselected control values automatically move to the base underlying data. Columns with names that don't match any control values are unaffected by the action. |

> 💡
>
> ### To set column names as the control values, use one of the following methods:
>
> * Enter column names in an input table column, then select that column as the control element's value source.
> * Create a manual list of column names as the control element's values source.

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

### Swap columns

Create an action that swaps all columns of a table grouping, chart property (axis, color, tooltip, etc.), or pivot table property (row, column, or value). This action removes all existing columns in the target grouping or property and replaces them with the selected column.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

|  |  |
| --- | --- |
| **Action** | Select **Modify element**. |
| **Target element** | Select an element to modify. |
| **What to modify** | Select **Swap columns**, then select a grouping or property from the target element. |
| **Swap with** | Select a column to replace the existing columns in the target grouping or property. |

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

### Set axis scale

Create an action to set the scale of the dependent variable (or value) axis in the target element.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

|  |  |
| --- | --- |
| **Action** | Select **Modify element**. |
| **Target element** | Select an element to modify. |
| **What to modify** | Select **Set axis scale**. |
| **Scale type** | Select an option to determine the scale type applied to the target element's dependent variable (or value) axis. |

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

## Refresh an element

Create an action to refresh the data of a target element in the current workbook. Refreshing a parent element also refreshes all child elements in the workbook.

> 🚧
>
> ### This action doesn’t refresh the data if the element is materialized.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

* |  |  |
  | --- | --- |
  | **Action** | Select **Refresh element**. |
  | **Element** | Select an element to refresh. |

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

## Select tab

Create an action to display a specific tab in a [tabbed container](/docs/create-and-configure-tabbed-containers-beta) element.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

* |  |  |
  | --- | --- |
  | **Action** | Select **Select tab**. |
  | **Tabbed container** | Select a tabbed container in this workbook. |
  | **Tab** | Select the tab to display. |

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

Updated 3 days ago

---

Related resources

* [Intro to actions](/docs/intro-to-actions)
* [View and manage existing actions](/docs/view-and-manage-existing-actions)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Modify elements](#modify-elements)
  + - [Show columns](#show-columns)
    - [Hide columns](#hide-columns)
    - [Move columns](#move-columns)
    - [Swap columns](#swap-columns)
    - [Set axis scale](#set-axis-scale)
  + [Refresh an element](#refresh-an-element)
  + [Select tab](#select-tab)