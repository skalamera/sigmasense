# Create actions that call stored procedures

# Create actions that call stored procedures

Workbooks support actions that can **call a stored procedure** and allow you to use the output of the stored procedure as a [**variable**](/docs/use-variables-in-actions).

For example, if you have an existing stored procedure in your data platform that you use to perform a complex calculation, rather than recreating the logic in a Sigma custom function or formula, you can call the stored procedure and use the output in Sigma.

This document explains how to create actions to **call a stored procedure**. For more information about actions in Sigma, see [Intro to actions](/docs/intro-to-actions).

For specific end-to-end examples, see:

* [Example: Run a stored procedure with column data](#example-run-a-stored-procedure-with-column-data).
* [Example: Run a stored procedure based on user input](#example-run-a-stored-procedure-based-on-user-input).

## Limitations

* Only BigQuery, PostgreSQL, Redshift, and Snowflake are supported.
* The stored procedure must be contained in a schema that is indexed by Sigma (available through the connection in the data catalog). Do not place any stored procedures in the same schema used for write back.
* Variant argument types are not supported.
* Arguments with default values are not supported.
* To work with the return value or output of a stored procedure, the stored procedure must return a scalar value.

  + If a stored procedure returns tabular data, you cannot work with the output as a variable and instead must locate the created table in the data catalog for the connection to work with it in Sigma.
  + If the stored procedure returns an array, modify the stored procedure to convert the array to text (serialize) and then deserialize the data in the stored procedure.

## User and system requirements

The ability to configure stored procedure actions requires the following:

* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Full explore** or **Create, edit, and publish workbooks** permission enabled, and the **Create stored procedure actions** permission enabled.
* You must be the workbook owner or be granted **Can explore**1 or **Can edit** [workbook access](/docs/folder-and-document-permissions).

1If you’re granted **Can explore** workbook access, you can configure actions in custom, saved, and shared views. Actions saved to views do not apply to the workbook’s published version.

You cannot define stored procedures in Sigma. Before you can create an action to call a stored procedure in Sigma, you must create the stored procedure in your data warehouse or data platform.

### Requirements to call a stored procedure from an action

To call a stored procedure from an action, the following applies:

* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Call stored procedure action** permission enabled.
* You must have **Can use** access or greater granted on the connection, or **Can use** access granted on the stored procedure in Sigma. See [Manage access to data and connections](/docs/manage-data-permissions).
* The user and role associated with the connected data platform must have permission to use and run the stored procedure in the data platform.

  + For a BigQuery connection, if the service account is granted the BigQuery Data Viewer role, no additional permissions are required. See [Connect to BigQuery](/docs/connect-to-bigquery).
  + For a PostgreSQL connection, the service account must be granted `EXECUTE` privileges on the stored procedure.
  + For a Redshift connection, the service account must be granted `USAGE` on the schema that contains the stored procedure and `EXECUTE` on the stored procedure. See [Connect to Redshift](/docs/connect-to-redshift#configure-amazon-redshift).
  + For a Snowflake connection, the user's default role or the service account role must be granted the following privileges:

    - `USAGE` on the schema that contains the stored procedure.
    - `USAGE` or `OWNERSHIP` on the stored procedure.

    See [Connect to Snowflake](/docs/connect-to-snowflake).

> 📘
>
> ### If a user with **Can Explore** or **Can Edit** access to the workbook does not have **Can use** access granted on the stored procedure or relevant connection and also does not have access to run stored procedures in the data platform, they cannot see or modify the stored procedure. The stored procedure does not appear when browsing available connections in the data catalog, and an already configured action appears blank.
>
> Users with **Can use** access to the stored procedure granted in Sigma, but without permissions to run the stored procedure in the data platform, can see the stored procedure, but attempts to call the stored procedure with the action fail.

## Call a stored procedure from an action

Create an action that calls a stored procedure in your data platform.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

* |  |  |
  | --- | --- |
  | **When selecting cells in** | Select a column from the trigger element to initiate the action when clicked. *This field only applies when the trigger element is a table, pivot table, or input table.* |
  | **Condition** | [optional] Turn on the switch to configure a condition that should be met for the action to take effect. |
  | **Action** | In **Advanced**, select **Call stored procedure**. |
  | **Select a stored procedure** | Search or browse to the stored procedure that you want to call, then select the stored procedure. |

* Configure the stored procedure setup. These steps might be different depending on the arguments and signatures expected by the stored procedure:

* |  |  |
  | --- | --- |
  | **Select signature** | If the stored procedure has multiple signatures, in the list of signatures, select the desired signature for the stored procedure. |
  | **Set value for: <argument>** | Assign values to the stored procedure argument using one of the following options:  + **Static values**: Enter a value for the argument. + **Column**: If the action is triggered from a data element, choose a column in the data element to which the action applies to provide the argument value. + **Control**: Choose a control element in the workbook to provide the argument value. + **Formula**: Enter a formula to use to provide the argument value. The provided argument value must match the data type expected by the stored procedure. |
  | **Outputs** | If the stored procedure provides an output, review the variable name and data type with which the output is available. For example, for a stored procedure named "echo\_args", the action variable is `echo_args`. |

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

> 📘
>
> ### When using a stored procedure action in an action sequence, Sigma waits for the stored procedure to finish running before triggering the next action in the sequence. If the stored procedure fails with an error, the action sequence stops running and any following actions in the sequence do not run.

For more details about calling a stored procedure with an action, see the following examples.

### Who the stored procedure runs as

When a stored procedure is run from Sigma as an action, the user that the stored procedure runs as depends on your connection settings and the configuration of your stored procedure. In some data platforms, you can configure the stored procedure to run either as the caller or as the owner.

If your stored procedure is set up to run as the caller:

* For an OAuth connection, the stored procedure runs in your data platform as the user who triggered the action.
* For a non-OAuth connection, the stored procedure runs in your data platform as the user and using the role specified in the connection, sometimes referred to as the service account.

## Example: Run a stored procedure with column data

As an end-to-end example, run a stored procedure based on user selection in a data element.

For example, if you have a stored procedure in BigQuery called GET\_CAMPAIGN\_STATUS that compiles and calculates the latest clickthrough data for an email campaign performed in a third-party tool. The stored procedure takes one argument, the name of the email campaign, and outputs text with the plain text body of the email.

1. Open your workbook for editing.
2. Add relevant workbook elements:

   1. Add a data element, for example a table with a row for each email campaign sent by your marketing department, with columns like **Campaign Name** and **Date Sent**.
   2. Add a text area control next to the data element and rename the control **Campaign details**.
3. On the data element, define an action sequence that runs **On select** from the *Campaign Name* column:

   1. Add the **Call stored procedure** action and configure it:
      1. Navigate to the BigQuery connection and search for the GET\_CAMPAIGN\_STATUS stored procedure.
      2. For **Set value for arg1: name**, choose **Column**, then choose the *Campaign Name* column in the data element that contains the name of the email campaign.
      3. Note the action variable used for the response, **get\_campaign\_status**.
   2. Add the **Set control value** action and set the value to the **Action variable**: `get_campaign_status`.![Input table with an action sequence configured On select of the Campaign Name column to open a modal, call a stored procedure, and set the Campaign Details control element.](https://files.readme.io/6e839abbeb5e238e1e921c399ec697b92ccc82b3129b12d75db0da03334fbed5-example2-config.png)
4. Test the workflow. In this example, a modal appears with the text of the email campaign:

   ![A modal titled Campaign Details with details about the eggscuse me email campaign, promising hats and books with eggtastic info.](https://files.readme.io/b888e7dea8b4775c4c2fddae4d810b5d7c625dac2346c02599a1cbba33a258e0-egg-campaign-output.png)
5. Publish your workbook.

> 💡
>
> Add the output control to a modal to add interactivity and reduce visual clutter. Set the action sequence for the primary button for the modal to clear the control and close the modal.

## Example: Run a stored procedure based on user input

As another end-to-end example, run a stored procedure based on user input.

For example, recalculate the project budget requirements based on several inputted values. In this example, assume that you have access to a stored procedure in Redshift called ESTIMATE\_BUDGET that calculates the estimated budget for a project. The stored procedure takes 3 number arguments, one for estimated materials cost, one for estimated number of employees, and one for number of weeks, and outputs a string with a budget estimate.

1. Open your workbook for editing.
2. Add relevant workbook elements:

   1. Add three number input control elements to use as the input for the calculation, named:

      * Materials cost
      * Headcount
      * Weeks
      > 💡
      >
      > Use a slider control instead of a static value to set a number, which allows you to constrain the input values.
   2. Add a text input control element to display the output of the stored procedure, named **Estimated budget**.
   3. Add a button element. Update the button title to **Estimate the budget!**.![Three number input controls labeled as documented, with a pink button labeled Estimate the budget! followed by a text input to store the budget estimate.](https://files.readme.io/08b7d837db955c27d2aef658b9ab23f7a99df4eb2620d6c67502f559f5d39bc8-spactions-example3-basic.png)
3. On the button element, define an action sequence with the following actions:

   1. Add the **Set control value** action and target the **Estimated budget** control element. Set the value to "Calculating…"
   2. Add the **Call stored procedure** action.
      1. Navigate to the Redshift connection and search for the ESTIMATE\_BUDGET stored procedure.
      2. For **Set value for arg1: cost**, choose **Control**, then choose the **Materials cost** control.
      3. For **Set value for arg2: headcount**, choose **Control**, then choose the **Headcount** control.
      4. For **Set value for arg3: weeks**, choose **Control**, then choose the **Weeks** control.
      5. Note the action variable used for the response, **estimate\_budget**.
   3. Add the **Set control value** action and target the **Estimated budget** control. Set the value to an **Action variable**, then choose the `estimate_budget` variable to display the output of the stored procedure.![Estimate the budget button selected and showing the action sequences configured, one to call the stored procedure and another to set the estimated budget control.](https://files.readme.io/38a00f0e698b036d6498b33f251ce149d2d0bbe3af35a2b7d09b0a8e65b8087b-spactions-example3-config.png)
4. Test the workflow:

   1. Add numbers to each input control, then click the button.
   2. Review the output control, **Estimated budget**.![Gif entering number values into the three inputs, clicking estimate the budget, then waiting for a budget estimate to appear.](https://files.readme.io/0aedba6d80f11755b63d223fce50a85b2ce5ffb879fa14cd6b5ea97b381adae3-Screen_Recording_2025-03-03_at_12.30.14_PM_2.gif)
5. Publish the workbook.

> 💡
>
> Add another button with an action sequence that inserts a row to an input table with the values of all 4 control elements to keep a historic record of the various budget estimates, then clears all the controls on the page to reset the configuration.

![Gif with the same configuration of 2 number input controls but the headcount control is now a number slider control between 0 and 10. Clicking estimate the budget produces filler text for \"Calculating...\", then \"Save budget options\" inserts a row into a Possible budgets input table and clears the controls.](https://files.readme.io/22e0a1bdeffb47a1f7c371622874fc46d81c0cb86803346e1c6b6b3f97fc693a-Screen_Recording_2025-03-03_at_12.37.22_PM_1.gif)

Updated 3 days ago

---

[Create actions that modify plugins](/docs/create-actions-that-modify-plugins)[Configure actions](/docs/configure-workbook-actions)

* [Table of Contents](#)
* + [Limitations](#limitations)
  + [User and system requirements](#user-and-system-requirements)
  + - [Requirements to call a stored procedure from an action](#requirements-to-call-a-stored-procedure-from-an-action)
  + [Call a stored procedure from an action](#call-a-stored-procedure-from-an-action)
  + - [Who the stored procedure runs as](#who-the-stored-procedure-runs-as)
  + [Example: Run a stored procedure with column data](#example-run-a-stored-procedure-with-column-data)
  + [Example: Run a stored procedure based on user input](#example-run-a-stored-procedure-based-on-user-input)