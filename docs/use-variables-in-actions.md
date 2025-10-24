# Use variables in actions

# Use variables in actions

Action variables allow formulas written within an action to reference values the user selected within a table or visualization, or the results from a previously run action like a [stored procedure action](/docs/create-actions-that-call-stored-procedures). You can use action variables in any custom formula for an action, including conditions.

When actions are triggered from a table or visualization, Sigma generates a piece of data called `Selection` which represents the values of the rows that the user selected in a table or the data points the user selected in a visualization.

Reference the `Selection` variable to work with the selected data point, such as to run an action condition on a specific row selected by a user, display the specific value selected by a user in a dynamic text formula, or pass a selected value to another formula. When referencing the `Selection` action variables, you can perform all of the usual functions that tables support, such as aggregations, conditions, and lookups.

> 📘
>
> ### Action variables persist only during the execution of the action sequence and can only be referenced inside formulas for actions or conditions for action sequences. If you want to reference a user-selected value or stored procedure result outside of an action sequence, set a control to the action variable, then reference the value of that control instead.

## User requirements

> 📘
>
> The following requirements apply to users who configure actions. Users who access and interact with a workbook can typically trigger all existing actions within it. Any restrictions are noted in this document.

The ability to configure actions requires the following:

* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Full explore** or **Create, edit, and publish workbooks** permission enabled.
* You must be the workbook owner or be granted **Can explore**1 or **Can edit** [access to the workbook](/docs/folder-and-document-permissions).

1If you’re granted **Can explore** access to the workbook, you can configure actions in custom, saved, and shared views. Actions saved to views do not apply to the workbook’s published version.

## Reference a variable in a custom formula for an action

To reference a variable in an action, do the following:

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. In the panel, add an action or edit an existing one using one of these methods:
   * Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** within a sequence group to add an action within an existing sequence. If there were no previously configured actions on this element, add the action inside the empty sequence.
   * Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action sequence** at the top of the actions panel to add the action outside of an existing sequence.
   * Hover over the name of an existing action, then click **Edit** ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/edit.svg) to open the **Action** modal.
5. In the **Action** modal, choose an action type that supports using custom formulas to set a value, such as **Insert row** or **Set control value**.
6. In the **Set value as** or **With values** field, select **Formula**.
7. In the formula bar, use the syntax `[Selection/<Column Name>]` to reference the the values the user selected in the element. Depending on the element type, the user may be selecting values in table cells or data points in a chart.
8. [optional] If the element is a table, set the **When selecting cells in** field for the sequence to a specific column in the table. Setting this value restricts the actions you configure in the sequence to trigger only when the user clicks on that column.

## Reference a variable in a condition for an action

Action variables also work in conditions. For more about configuring conditions for actions, see [Make an action conditional](/docs/make-an-action-conditional).

To reference a variable in an action condition, do the following:

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. If there is not already a condition defined in the sequence, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**, then click **Add condition**.
5. Click on the gray condition bar to open the **Condition** modal.
6. Choose **Custom formula**.
7. In the formula bar, use the syntax `[Selection/<Column Name>]` to reference the values the user selected in the element. Depending on the element type, the user may be selecting values in table cells or data points in a chart.

## Examples

| Formula with action variables | Usage |
| --- | --- |
| `[Selection/Region] = "South" or [Selection/Region] = "East"` | This formula identifies a user's selection of a table cell or corresponding data point in a visualization that corresponds to either the value "North" or the value "East" in the `Region` column.  Use this formula in a condition to limit the action execution depending on the user's selection in the data. To configure unique actions depending on the values the user selects, configure multiple action sequences, each with a condition based on an action variable. |
| `Lookup([Selection/Company Name], Max([Selection/Revenue]), [Selection/Revenue])` | This formula returns the value of the `Company Name` column that has the largest value in the `Revenue` column.  Use this formula to set a control value when the user clicks in a grouped column to single out a particular value from within the grouping. |

For examples using a stored procedure result as an action variable, see the examples in [Create actions that call stored procedures](/docs/create-actions-that-call-stored-procedures).

Updated 3 days ago

---

[Define an action condition](/docs/make-an-action-conditional)[Create cross-element filters](/docs/create-cross-element-filters)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Reference a variable in a custom formula for an action](#reference-a-variable-in-a-custom-formula-for-an-action)
  + [Reference a variable in a condition for an action](#reference-a-variable-in-a-condition-for-an-action)
  + [Examples](#examples)