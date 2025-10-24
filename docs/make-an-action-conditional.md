# Define an action condition

# Define an action condition

You can define an optional condition for any action sequence to control the circumstances in which the actions in that sequence should take effect. The condition can be a custom formula or, if you are configuring an action sequence for selected controls, the condition can be the value of the control. Conditions based on custom formulas can reference [action variables](/docs/use-variables-in-actions) to reference the values the user selected in a table or visualization. For more information about actions in Sigma, see [Intro to actions](/docs/intro-to-actions).

To make an action sequence conditional, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**, then click **Add condition** when creating or editing the action.

You can configure multiple action sequences, each with an optional condition. If a user interacts with an element that has multiple action sequences configured, each action sequence triggers if its condition, if there is one, evaluates to true.

## Example: Modify a chart display based on a segmented control

You can configure an action on a segmented control that modifies the display of a visualization based on the value the user selects in the control. For more about using segmented controls, see [Create and configure a segmented control](/docs/segmented-control).

For example, if you have a chart showing the total sales, broken down by region, you can add a segmented control to allow users to change the display of the chart to their preferred view.

To achieve this, follow these steps:

1. Add a segmented control targeting your visualization, giving it two values: `Individual trend` and `Comparison`.
2. Add an action sequence on the control with the following configuration:

   |  |  |
   | --- | --- |
   | **Condition** | Set to **Control value is equal to**. For this example, select **Individual trend**. |
   | **Action** | Select **Modify element**. |
   | **Target element** | Select the visualization targeted by the control. In this example, the visualization is `Total sales by country over time`. |
   | **What to modify** | Select a modification to display the chart in a way that matches the user selection in the control. In this example, the modification is **Move columns** and **to trellis column**. |
   | **Column to move** | In this example, the column is `Country`. |
3. Add a second action sequence on the control with the following configuration:

   |  |  |
   | --- | --- |
   | **Condition** | Set to **Control value is equal to**. For this example, select **Comparison**. |
   | **Action** | Select **Modify element**. |
   | **Target element** | Select the visualization targeted by the control. In this example, the visualization is `Total sales by country over time`. |
   | **What to modify** | Select a modification to display the chart in a way that matches the user selection in the control. In this example, the modification is **Move columns** and **to color - category**. |
   | **Column to move** | In this example, the column is `Country`. |
4. You now have two action sequences configured on your segmented control, each one modifying your visualization element based on the value of the segmented control.
5. Publish your changes to the workbook.

When viewers interact with the control, they can now swap back and forth between the individual trend and comparison view of the data in your visualization.

![GIF showing a visualization of Total sales by country over time and a control with two values, Individual trend and Comparison. In the animation, a user clicks each of the two values, demonstrating that the chart visualization switches between a trellis view of each country and a combined view in a stacked bar chart.](https://files.readme.io/5b8012d6cc5fa189ddafaae7e310d2aefb88cbbe1d487c068d6e939f7b76e320-conditional_action_segmented.gif)

## Example: Limit form submissions with a deadline

You can configure a condition on an action sequence to prevent it from occurring if a deadline has passed.

For example, if you are creating a form, you can configure the action on the submission button to insert a row in an input table only if the deadline has not yet passed. For more information about actions that insert rows in input tables, see [Create actions that modify input table data](/docs/create-actions-that-modify-input-table-data).

To achieve this, follow these steps:

1. Create a workbook with an empty input table, one or more text controls, and a button element.
2. Configure the input table data entry permissions to allow edits in the published version. See [Configure data governance options in input tables](/docs/configure-data-governance-options-in-input-tables#set-data-entry-permission) for details on how to modify data entry permissions.
3. Add another control of any type to the workbook, then open the editor panel and set the **Control type** to `Date`. In this example, the date control has a control ID of `Deadline-Control`.
4. Set a date in your date control to a future date. This date is used as the deadline when you set the condition.
5. Select the button element.
6. In the editor panel, open the **Actions** tab.
7. Add an action sequence with the following configuration:

   |  |  |
   | --- | --- |
   | **Condition** | Set to **Custom formula**. For this example, enter `DateDiff("day", Today(), [Deadline-Control]) > 0` . This formula evaluates to True if the number of days between the current date and the date set in the date control with the ID "Deadline-Control" is greater than zero. |
   | **Action** | Select **Insert row**. |
   | **Into** | Select the name of your input table. In this example, the name is `Form Submissions`. |
   | **With values** | Select the control elements that make up your form. |
8. Publish your workbook, then view the published version.
9. Test your action by entering text in the text controls, then clicking the button.

   1. If the date in your date control is set to a date later than today's date, the values of your text controls should appear as new rows in your input table.
   2. If you update the date in your date control to today's date or any past date, clicking the button does not insert a row, because the deadline has passed.

Updated 3 days ago

---

Related resources

* [Intro to actions](/docs/intro-to-actions)
* [View and manage existing actions](/docs/view-and-manage-existing-actions)
* [Use variables in actions](/docs/use-variables-in-actions)

* [Table of Contents](#)
* + [Example: Modify a chart display based on a segmented control](#example-modify-a-chart-display-based-on-a-segmented-control)
  + [Example: Limit form submissions with a deadline](#example-limit-form-submissions-with-a-deadline)