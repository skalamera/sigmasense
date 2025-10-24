# Create actions that modify plugins

# Create actions that modify plugins

You can create actions that enable workbook elements to trigger effects within a plugin. For example, an action like selecting a table cell can trigger a specific plugin effect. This document explains how to create actions that trigger plugin effects.

To configure your plugin code to support actions, see [Configure plugins to work with actions](/docs/configure-plugins-to-work-with-actions). For more information about actions in Sigma, see [Intro to actions](/docs/intro-to-actions).

## User requirements

> 📘
>
> The following requirements apply to users who configure actions. Users who access and interact with a workbook can typically trigger all existing actions within it. Any restrictions are noted in this document.

The ability to configure actions requires the following:

* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Full explore** or **Create, edit, and publish workbooks** permission enabled.
* You must be the workbook owner or be granted **Can explore**1 or **Can edit** [access to the workbook](/docs/folder-and-document-permissions).

1If you’re granted **Can explore** access to the workbook, you can configure actions in custom, saved, and shared views. Actions saved to views do not apply to the workbook’s published version.

## Prerequisites

* You must configure your plugin to be compatible with actions. See [Configure plugins to use as target elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-target-elements).

## Modify a plugin

Create an action that modifies a plugin.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).

   > 🚧
   >
   > ### To avoid causing an infinite loop, do not configure an action sequence containing the same plugin as both the trigger and target element.
3. In the editor panel, open the **Actions** tab.
4. Create a new sequence, or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click Add action to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

   |  |  |
   | --- | --- |
   | **Action** | Select **Trigger plugin**. |
   | **Target plugin** | Select the name of the plugin element you want to modify. |
   | **Select effect** | Select the name of the configuration object that was created from the steps in [Configure plugins to use as target elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-target-elements). |
7. If the trigger element is a table, pivot table, or input table, configure additional settings that determine when and how user interaction triggers the action sequence:

* To trigger the action sequence only when a user selects a cell in a specific column, click the **When selecting cells in column** field and select the column. To trigger the action sequence when a user selects a cell in any column, select **Any column**.
* [optional] To control whether keyboard navigation within the element can trigger action sequences on the element, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** in the **Actions** panel, then select **Allow keyboard to trigger actions**. When the option displays a checkmark, keyboard navigation and pointer events (e.g., mouse clicks) can trigger the action sequences. When the option doesn't display a checkmark (default), only pointer events can trigger them.

  > 💡
  >
  > Keyboard navigation as a trigger interaction can disrupt the user experience. For example, if the element's action sequences include actions that open links or other workbooks, a user can be unintentionally navigated away from their current task. This can be particularly disruptive if the action sequence can be triggered by selecting a cell in any column.
  >
  > Consider allowing keyboard navigation to trigger actions only when it facilitates the configured action sequences and is unlikely to interfere with usability.

8. [optional] To execute the action sequence only when a specific condition met, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** in the action sequence, then select **Add condition** and configure the criteria. For more information about conditions, see [Define an action condition](/docs/make-an-action-conditional).

Updated 3 days ago

---

[Create actions that generate embed iframe events](/docs/create-actions-that-trigger-embed-iframe-events)[Create actions that call stored procedures](/docs/create-actions-that-call-stored-procedures)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Prerequisites](#prerequisites)
  + [Modify a plugin](#modify-a-plugin)