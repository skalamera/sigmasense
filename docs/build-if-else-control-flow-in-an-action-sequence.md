# Build if/else control flow in an action sequence (Beta)

# Build if/else control flow in an action sequence (Beta)

> 🚩
>
> This documentation describes one or more public beta features that are in development. Beta features are subject to quick, iterative changes; therefore the current user experience in the Sigma service can differ from the information provided in this page.
>
> This page should not be considered official published documentation until Sigma removes this notice and the beta flag on the corresponding feature(s) in the Sigma service. For the full beta feature disclaimer, see [Beta features](/docs/sigma-product-releases#beta-features).

Use an if/else statement to create a dynamic workflow within an action sequence. If/else control flow adds flexibility to a sequence by allowing it to check one or more conditions and execute actions for the first condition that evaluates to true.

This document introduces the if/else framework, provides tips and best practices, and explains how to configure an if/else statement in an action sequence. You can also try an interactive demo in the [Examples](#example-1-with-and-without-ifelse) section of this document.

## User requirements

> 📘
>
> The following requirements apply to users who configure actions. Users who access and interact with a workbook can typically trigger all existing actions within it. Any restrictions are noted in this document.

The ability to configure actions requires the following:

* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Full explore** or **Create, edit, and publish workbooks** permission enabled.
* You must be the workbook owner or be granted **Can explore**1 or **Can edit** [access to the workbook](/docs/folder-and-document-permissions).

1If you’re granted **Can explore** access to the workbook, you can configure actions in custom, saved, and shared views. Actions saved to views do not apply to the workbook’s published version.

## About if/else control flow

If/else is a type of conditional statement that allows you to add logical control flow within an action sequence. You can insert an if/else statement anywhere in the sequence to add a decision point where an action or group of actions only executes if a specific condition is true.

### Action paths

*Without if/else control flow*, a sequence executes actions on a linear path: every action runs, and they run in the same order each time.

When you add if/else logic, a sequence can diverge from the linear path and execute different actions depending on whether a condition is true or false. You can configure one or more conditions in an if/else statement (see [Components of an if/else statement](#components-of-an-ifelse-statement)), and the sequence checks them sequentially until one evaluates to true or the statement ends. When a condition is true, the sequence executes the corresponding actions, then returns to the linear path of the sequence.

### Components of an if/else statement

In an action sequence, an if/else statement can include the following components that determine which action path executes:

|  |  |
| --- | --- |
| **if** | The primary path that executes if its condition is true. An if/else statement always includes the *if* component. |
| **else if** | [Optional] One or more alternative paths that are only checked when the *if* condition and previous *else if* conditions (if any) are false. *Else if* conditions are checked sequentially, and when a condition evaluates to true, the sequence executes that path and ends the if/else control flow. |
| **else** | [Optional] The default path that executes when the *if* condition and all *else if* conditions are false. |

> 📘
>
> If the if/else statement doesn't include an else component, no action path executes when the *if* condition and all *else if* conditions are false.

![A flowchart demonstrating how a sequence evaluates and executes an if/else statement](https://files.readme.io/426d705abd9500069151d023f2138f487c118ccbeb51976072db89a7bbc157a3-if_else_control_flow.png)

## Tips and best practices

The following information can help you build a robust and reliable if/else control flow.

* Use if/else statements to simplify action workflows by consolidating multiple conditions into a single sequence. This also ensures consistent order of execution, which is not guaranteed when creating conditional workflows in separate sequences. For a comparison of a use case with and without if/else, see [Example 1](#example-1-with-and-without-ifelse) in this document.
* A sequence checks the conditions of an if/else statement sequentially and stops when one evaluates to true or the statement ends. Therefore, it's important to consider the following:

  + The order of the conditions matters. Multiple conditions may be true, but only the first one evaluated is executed.
  + If there are conditions that the sequence must continue to check, configure them in a separate if/else statement within the sequence.
* Including the *else* component to define default output can prevent workflow errors and incomplete logic.
* If/else conditions can reference the results of previous actions in the sequence. You can use this functionality to check for specific action variable values, including the output of a called stored procedure (see [Example 2](#example-2-check-called-stored-procedure-output) in this document).
* Drag and drop *if* and *else if* components to quickly reorder them within an if/else statement. You can also drag and drop individual actions to reorder them within a component, move them between components, or move them into or out of the if/else statement.

## Build an if/else control flow

The following sections explain how to build an if/else control flow with a sequence.

* [Add an if/else statement](#add-an-ifelse-statement)
* [Configure the *if* component](#configure-the-if-component)
* [Configure *else if* components](#configure-else-if-components)
* [Configure the *else* component](#configure-the-else-component)

### Add an if/else statement

Add an if/else statement to an action sequence.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the if/else control flow).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing one that you want to modify.
5. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg) **Add action** to add a new action to the sequence.
6. The action configuration modal opens automatically (if it closes, select the action name to reopen it). Click the **Action** field and select **If/else**.

   ![The action configuration modal showing the Action field dropdown menu expanded and cursor hovering over the if/else option.](https://files.readme.io/e66fd8783923770de0f3f4e998e9a54b4fdbf510a84779478b333f03db79b163-image.png)
7. In the sequence, Sigma converts the action to an *if* component and opens the **Condition** modal. To continue building the if/else control flow, see [Configure the *if* component](#configure-the-if-component) in this document.

   ![An action sequence containing the "if" component of an if/else statement.](https://files.readme.io/f459937959650f73f5f293a29e756886cd96a0a4d5f10799c6ce966a22bf8994-image.png)

### Configure the *if* component

Define the *if* condition and configure one or more actions that execute when the condition is true. The sequence always checks the if condition and only proceeds to check *else if* and *else* conditions when the *if* condition is false.

1. Define the *if* condition:

   1. Select the *if* component to open the **Condition** popover.

      ![An action sequence containing only the "if" component of an if/else statement, and a cursor hovering over the "if" condition.](https://files.readme.io/b556dfea0d68ba029f3aff50400432f8aac0f7a90db709a7e6e023012be7415f-image.png)
   2. In the **Condition** popover, select one of the following condition options from the dropdown (available options depend on the element type), then define the criteria that must be met for the corresponding action to run.
   3. * **Custom formula**: Enter a formula that must return `true`.
      * **Selection matches criteria**: Select a column and specify the required column value.
      * **Selected values contain**: (available with multi-select **List values** controls only) Specify a single value that must be one of the selected control values.
      * **Control value is equal to**: Specify the required control value.

      ![The condition modal showing the "Control value is equal to" option selected and a cursor hovering over the "Week" option in the segmented control.](https://files.readme.io/d0128506e8e0bdf1e2b0e492cac5efaf87ba253860fc12aed698d2532cfe58c1-image.png)
2. Configure the primary path to execute when the *if* condition is true:

   1. Select the default action in the *if* component, or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** next to the condition and select **Add action within** to add a new one.
   2. In the action configuration popover, select an action type and configure the effect. For a list of action types and detailed information about how to configure them, see [Action effects](/docs/intro-to-actions#action-effects).

      ![The action configuration modal showing the Action field set to "Set control value," the Update control field set to "Period (Sales by period)," and the Set value as field set to "Static values" with the static value set to a date range for the last week.](https://files.readme.io/f3efe325d1f2c3e31dcb9d317c3b95530925135bdb914ffbf5aff22c8ed98af2-image.png)
   3. [Optional] Repeat steps 2a and 2b above to add more actions to the component.

### Configure *else if* components

[Optional] Define an *else if* condition and configure one or more actions that execute when the condition is true. Repeat the steps to add multiple *else if* components.

1. To add an *else if* component, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** next to the *if* condition or any previously added *else if* condition, then select **Add else if**.

   ![An action sequence showing the More menu open on the "if" component and a cursor hovering over the "Add else if" option.](https://files.readme.io/30c45969597219309991db4edede82494321611cc6a29f607e41ac6528cd4097-image.png)
2. Define the *else if* condition:

   1. Select the *else if* component to open the **Condition** popover.

      ![An action sequence containing the "if" and "else if" components of an if/else statement, and a cursor hovering over the "else if" condition.](https://files.readme.io/9c67285c3c7a68f3ee4998d46ce0ab0a58af7a92bcf7cb67df76a9baa5e752f0-image.png)
   2. In the **Condition** popover, select one of the following condition options from the dropdown (available options depend on the element type), then define the criteria that must be met for the corresponding action to run.

      * **Custom formula**: Enter a formula that must return `true`.
      * **Selection matches criteria**: Select a column and specify the required column value.
      * **Selected values contain**: (available with multi-select **List values** controls only) Specify a single value that must be one of the selected control values.
      * **Control value is equal to**: Specify the required control value.

      ![The condition modal showing the "Control value is equal to" option selected and a cursor hovering over the "Month" option in the segmented control.](https://files.readme.io/67d77c1d0838209d1dffc23b16fef723ea2b58fb63d1acb17ae373738dfb90dc-image.png)
3. Configure an alternative path to execute when the *else if* condition is true:

   1. Select the default action in the *else if* component, or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** next to the condition and select **Add action within** to add a new one.
   2. In the action configuration popover, select an action type and configure the effect. For a list of action types and detailed information about how to configure them, see [Action effects](/docs/intro-to-actions#action-effects).

      ![The action configuration modal showing the Action field set to "Set control value," the Update control field set to "Period (Sales by period)," and the Set value as field set to "Static values" with the static value set to a date range for the last month.](https://files.readme.io/8ee644d20e93c15aba31e35bd870384c3a598580c8961185ad44791a9d26ed6b-image.png)
   3. [Optional] Repeat steps 3a and 3b above to add more actions to the component.

### Configure the *else* component

[Optional] Configure one or more actions that execute when the *if* condition and all *else if* conditions are false.

1. To add an *else* component, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** next to the *if* condition or any *else if* condition, then select **Add else**.

   ![An action sequence showing the More menu open on the "else if" component and a cursor hovering over the "Add else" option.](https://files.readme.io/93e6a5b865df3455b41085fdd016441d48a08c822f5486f94f70df1b42c3d487-image.png)
2. Configure the default path to execute when the *if* condition and all *else if* conditions are false:

   1. Select the default action in the *else* component, or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** in the *else* heading and select **Add action within** to add a new one.
   2. In the action configuration popover, select an action type and configure the effect. For a list of action types and detailed information about how to configure them, see [Action effects](/docs/intro-to-actions#action-effects).

      ![The action configuration modal showing the Action field set to "Set control value," the Update control field set to "Period (Sales by period)," and the Set value as field set to "Static values" with the static value set to a date range for the last year.](https://files.readme.io/4341fc90d52a74129ae5b2345b64df684b31419b9c9da62eec7695d65df07dd9-image.png)
   3. [Optional] Repeat steps 2a and 2b above to add more actions to the component.

## Example 1: With and without if/else

The screenshots in the [Build an if/else control flow](#build-an-ifelse-control-flow) sections of this document demonstrate a use case in which an if/else statement is used to streamline a workflow that could also be configured using three separate conditional sequences. The two methods support the same interactivity (see the [interactive demo](#interactive-demo) below), but the if/else statement represents the workflow with more clarity and can be easier to maintain and debug.

| With if/else | Without if/else (conditional sequences) |
| --- | --- |
| An action sequence showing an if/else statement containing an if, else if, and else components that check for specific values in a segmented control and set a date range control accordingly. | Three action sequences, each with a condition that checks for a specific value in a segmented control and then sets a date range control if true. |

### Interactive demo

The following embedded example demonstrates the use case configured in [Example 1](#example-1-with-and-without-ifelse). When you select a value in the *Filter by last* segmented control, the action sequence sets the *Period* data range control based on the selected value (using if/else control flow), which then filters the table data.

## Example 2: Check called stored procedure output

This example demonstrates how an action sequence can call a stored procedure and then use an if/else control flow to apply different logic using the value returned by the called stored procedure.

The following action sequence is configured on a data app that allows users to check current product stock and request a restock. When the sequence is initiated, it first calls the `PROCESS_DATA` stored procedure that returns a number. The if/else control flow then references the called stored procedure output when checking the *if* and *else if* conditions and when executing the *else* action path.

![An action sequence that shows an initial action that calls a stored procedure, followed by an if/else statement that references the results of the called stored procedure in the "if" and "else if" conditions, as well as in the "else" action path.](https://files.readme.io/a279016205fb8c8a01caad179dad8aa74d9b27e9d7787d4d74471b86a5084e6d-image.png)

Updated 3 days ago

---

[View and manage existing actions](/docs/view-and-manage-existing-actions)[Interact with workbooks](/docs/interact-with-workbooks)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [About if/else control flow](#about-ifelse-control-flow)
  + - [Action paths](#action-paths)
    - [Components of an if/else statement](#components-of-an-ifelse-statement)
  + [Tips and best practices](#tips-and-best-practices)
  + [Build an if/else control flow](#build-an-ifelse-control-flow)
  + - [Add an if/else statement](#add-an-ifelse-statement)
    - [Configure the if component](#configure-the-if-component)
    - [Configure else if components](#configure-else-if-components)
    - [Configure the else component](#configure-the-else-component)
  + [Example 1: With and without if/else](#example-1-with-and-without-ifelse)
  + - [Interactive demo](#interactive-demo)
  + [Example 2: Check called stored procedure output](#example-2-check-called-stored-procedure-output)