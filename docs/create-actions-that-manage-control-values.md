# Create actions that manage control values

# Create actions that manage control values

Workbooks support actions that set or clear values of specific control elements, enabling interacting users to quickly filter and unfilter data for different focused views.

This document explains how to create actions that manage control values. For more information about actions in Sigma, see [Intro to actions](/docs/intro-to-actions).

## User requirements

> 📘
>
> The following requirements apply to users who configure actions. Users who access and interact with a workbook can typically trigger all existing actions within it. Any restrictions are noted in this document.

The ability to configure actions requires the following:

* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Full explore** or **Create, edit, and publish workbooks** permission enabled.
* You must be the workbook owner or be granted **Can explore**1 or **Can edit** [access to the workbook](/docs/folder-and-document-permissions).

1If you’re granted **Can explore** access to the workbook, you can configure actions in custom, saved, and shared views. Actions saved to views do not apply to the workbook’s published version.

## Set a control value

Create an action that sets the value of a specific control element in the current workbook.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

* |  |  |
  | --- | --- |
  | **Action** | Select **Set control value**. |
  | **Update control** | Select a target control element to update in the current workbook. |
  | **Set value as** | Select an option to determine the type of value Sigma passes to the target control, then define the value.  + **Static values**: Passes the specified (fixed) value. + **Column**: Passes values from the specified column in the trigger element’s underlying data (if applicable).  *Only available when the trigger element is a table, pivot table, input table, or visualization.* + **Control**: Passes the value selected on the specified source control. + **Formula**: Passes a value based on the defined formula. |
  | **Set control selection to** | Select an option to determine how the interaction affects the target control value.  + **Replace previous selection**: The value passed to the control replaces all selected values. Any value previously selected is removed from the control selection. + **Add to existing selection**: The value passed to the control is added to currently selected values. + **Remove from existing selection**: The value passed to the control is removed from the selected values. |

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

## Clear one or more control values

Create an action that clears the values of one or more control elements in the current workbook.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

* |  |  |
  | --- | --- |
  | **Action** | Select **Clear control**. |
  | **Apply to** | Select the scope of the action to clear controls at one of the following levels of granularity: **Specific control**, **Container**, **Tabbed container**, **Page / modal**, or **Entire workbook**. |
  | **Control**, **Container**, **Tabbed container**, or **Page / modal** | Depending on your selection in the **Apply to** field, specify the target control, container, tabbed container, page, or modal from the dropdown. If you selected **Entire workbook** in the **Apply to** field, this field does not apply. |
  | **Tab** | If you selected **Tabbed container** in the **Apply to** field, select one or all tabs containing the controls you want to clear. |
  | **Reset to published value** | [optional] Select the checkbox to reset the control values to the last published values. On a tagged version of a workbook, this setting resets to the tagged version's values. |

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

Updated 3 days ago

---

Related resources

* [Intro to actions](/docs/intro-to-actions)
* [View and manage existing actions](/docs/view-and-manage-existing-actions)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Set a control value](#set-a-control-value)
  + [Clear one or more control values](#clear-one-or-more-control-values)