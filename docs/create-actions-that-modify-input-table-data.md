# Create actions that modify input table data

# Create actions that modify input table data

> 🚩
>
> The **Update row(s)** and **Delete row(s)** actions are public beta features that are currently in development. The sections describing the **Update row(s)** and **Delete row(s)** actions should not be considered official published documentation until Sigma removes this notice and the beta flags on the corresponding features in the Sigma service.
>
> All beta features and functionality described below are subject to quick, iterative changes. Therefore, the latest experience in the Sigma service might differ from the contents of this document. For the full beta feature disclaimer, see [Beta features](/docs/sigma-product-releases#beta-features).

Workbooks support actions that add, update, or delete rows in input tables. These actions are designed to support form functionality but can be used in other ways to accommodate different data app use cases.

This document explains how to configure the **Insert row**, **Update row(s)**, and **Delete row(s)** actions. For more information about actions in Sigma, see [Intro to actions](/docs/intro-to-actions).

## User requirements

> 📘
>
> The following requirements apply to users who configure actions. Users who access and interact with a workbook can typically trigger all existing actions within it. Any restrictions are noted in this document.

The ability to configure actions requires the following:

* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Full explore** or **Create, edit, and publish workbooks** permission enabled.
* You must be the workbook owner or be granted **Can explore**1 or **Can edit** [access to the workbook](/docs/folder-and-document-permissions).

1If you’re granted **Can explore** access to the workbook, you can configure actions in custom, saved, and shared views. Actions saved to views do not apply to the workbook’s published version.

## Insert row

Create an action that adds a new row in a target input table.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

* |  |  |
  | --- | --- |
  | **Action** | Select **Insert row**. |
  | **Into** | Select a target input table (empty only) to update with the added row. |
  | **With values** | For each column of your input table, define the value (or source of the value) that Sigma must pass to the row.  The availability of value type options (described below) depend on the elements in the workbook.  + **Static values**: Passes a specified (fixed) value + **Column**: Passes the value of the specified table column. + **Control**: Passes the value of the specified control element. + **Formula**: Passes a value based on the defined formula. *To leave a column blank, select Static values and leave the value unset.* |

7. In the document header, click **Publish** to apply the action to the published version of the workbook.
8. If the action is part of a workflow that can be triggered by any user with access to the workbook, confirm that the target input table or linked input table is editable in the published version. For more information, see [Set data entry permission](/docs/configure-data-governance-options-in-input-tables#set-data-entry-permission).

## Update row(s) (Beta)

Create an action that updates the value of one or more rows in a specific input table or linked input table.

> 📘
>
> ### The **Update row(s)** action can only modify input tables created after April 23, 2023.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

* |  |  |
  | --- | --- |
  | **Action** | Select **Update row(s)**. |
  | **In** | Select an input table or linked input table (the target element) that the action must modify. |
  | **Update row(s) by** | Choose an option and define the criteria that determines which row or rows are updated.  + **Single row**: Target an individual row based on its unique identifier (the system-generated row ID for input tables or the primary key column value for linked input tables). Depending on the trigger element type, you can define the criteria using one of the following options:   - **Static value**: Specify a fixed value. If the value matches the unique identifier of a single row in the target element, Sigma updates that row.   - **Column**: Choose a column from the trigger element (table, pivot table, input table, or chart). If the column value for the row selected in the trigger element matches the unique identifier of a single row in the target element, Sigma updates that row.   - **Control**: Choose a control element from the workbook. If the control value matches the unique identifier of a single row in the target element, Sigma updates that row.   - **Formula**: Enter a formula to evaluate. If the expression returns a value that matches the unique identifier of a single row in the target element, Sigma updates that row. If the formula returns a value that matches multiple rows, the action does not affect the table, and Sigma does not update any row. If multiple rows meet the criteria set for the Single row option, the action does not affect the table, and Sigma does not update any row. + **Formula**: Target rows based on a formula that evaluates to `True` or `False`. When the expression returns `True` for one or more rows in the target element, Sigma updates those rows. + **Column value matches criteria**: Target rows based on a comparison or logical operator evaluated against the specified column. When the operator criteria is True for one or more rows, Sigma updates those rows. |
  | **Update with values** | Define the column values that Sigma must pass to the row or rows it updates. You can configure values or value sources for any editable column in the target element. Depending on the trigger element type, you can define the value using one of the following options:  + **Static value**: Specify a fixed value to pass to the updated row or rows. + **Column**: Choose a column from the trigger element (table, pivot table, input table, or chart) containing values to pass to the updated row or rows. Sigma passes the column value for the row selected in the trigger element. + **Control**: Choose a control element from the workbook. Sigma passes the current control value to the updated row or rows. + **Formula**: Enter a formula to evaluate. Sigma passes the returned value to the updated row or rows. |

7. In the document header, click **Publish** to apply the action to the published version of the workbook.
8. If the action is part of a workflow that can be triggered by any user with access to the workbook, confirm that the target input table or linked input table is editable in the published version. For more information, see [Set data entry permission](/docs/configure-data-governance-options-in-input-tables#set-data-entry-permission).

## Delete row(s) (Beta)

Create an action that deletes one or more rows in a specific input table or linked input table.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

* |  |  |
  | --- | --- |
  | **Action** | Select **Delete row(s)**. |
  | **In** | Select an input table or linked input table (the target element) that the action must modify. |
  | **Delete row(s) by** | Choose an option and define the criteria that determines which row or rows are deleted  + **Single row**: Delete an individual row based on its unique identifier (the system-generated row ID for input tables or the primary key column value for linked input tables). Depending on the trigger element type, you can define the criteria using one of the following options:   - **Static value**: Specify a fixed value. If the value matches the unique identifier of a single row in the target element, Sigma deletes that row.   - **Column**: Choose a column from the trigger element (table, pivot table, input table, or chart). If the column value for the row selected in the trigger element matches the unique identifier of a single row in the target element, Sigma deletes that row.   - **Control**: Choose a control element from the workbook. If the control value matches the unique identifier of a single row in the target element, Sigma deletes that row.   - **Formula**: Enter a formula to evaluate. If the expression returns a value that matches the unique identifier of a single row in the target element, Sigma deletes that row. If the formula returns a value that matches multiple rows, the action does not affect the table, and Sigma does not delete any row. If multiple rows meet the criteria set for the Single row option, the action does not affect the table, and Sigma does not delete any row. + **Formula**: Delete rows based on a formula that evaluates to `True` or `False`. When the expression returns `True` for one or more rows in the target element, Sigma deletes those rows. + **Column value matches criteria**: Delete rows based on a comparison or logical operator evaluated against the specified column. When the operator criteria is True for one or more rows, Sigma deletes those rows. |

7. In the document header, click **Publish** to apply the action to the published version of the workbook.
8. If the action is part of a workflow that can be triggered by any user with access to the workbook, confirm that the target input table or linked input table is editable in the published version. For more information, see [Set data entry permission](/docs/configure-data-governance-options-in-input-tables#set-data-entry-permission).

Updated 3 days ago

---

[Create actions that control modals and tabbed containers](/docs/create-actions-that-control-modals-and-tabbed-containers)[Create actions that send notifications and export data](/docs/create-actions-that-send-notifications-and-export-data)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Insert row](#insert-row)
  + [Update row(s) (Beta)](#update-rows-beta)
  + [Delete row(s) (Beta)](#delete-rows-beta)