# Create actions that navigate to destinations

# Create actions that navigate to destinations

Workbooks support actions that navigate users to predefined URLs, other Sigma documents, or different locations within the current workbook.

This document explains how to create actions that navigate users to specific destinations. For more information about actions in Sigma, see [Intro to actions](/docs/intro-to-actions).

## User requirements

> 📘
>
> The following requirements apply to users who configure actions. Users who access and interact with a workbook can typically trigger all existing actions within it. Any restrictions are noted in this document.

The ability to configure actions requires the following:

* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Full explore** or **Create, edit, and publish workbooks** permission enabled.
* You must be the workbook owner or be granted **Can explore**1 or **Can edit** [access to the workbook](/docs/folder-and-document-permissions).

1If you’re granted **Can explore** access to the workbook, you can configure actions in custom, saved, and shared views. Actions saved to views do not apply to the workbook’s published version.

## Open a link

Create an action that navigates to an external link or destination within Sigma. Open a static link or generate a [dynamic URL](#open-a-link-with-a-dynamic-url) that adjusts to control or column values in the current workbook.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

|  |  |
| --- | --- |
| **Action** | Select **Open link**. |
| **Link URL** | Enter the URL of an external webpage or destination within Sigma.   *For information about using dynamic text in the URL, see [Create a dynamic URL](#open-a-link-with-a-dynamic-url) in this document.* |
| **Open in** | Select an option to determine how the link opens in the browser.   * **New window**: Opens the link in a new browser window. * **Same window**: Opens the link in the current browser window when the user interacts with the trigger element directly in Sigma. * **Parent window**: Opens the link in the current browser window when the user interacts with the trigger element in an embed.   *The interacting user's browser settings may change the selected **Open in** behavior. For example, **New window** may instead open the URL in a new tab (same window), and **Same window** may instead open the URL in the same tab.* |

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

### Open a link with a dynamic URL

To generate a dynamic URL that adjusts to control or column values in the current workbook, utilize Sigma’s dynamic text functionality when configuring the Link URL field in step 4 of the [previous section](#configure-an-action-to-open-a-link).

1. In the **Link URL** field, enter the base URL (unless this must also be dynamically generated), then enter `=` anywhere you want to add a dynamic value.
2. When you enter `=` , Sigma immediately displays an overlay containing a formula bar.

   * To pass the value of a control, enter a control ID in square brackets: `[<control-ID>]`. For example, `[search-control]`.
   * To pass the selection that was made in a column, add a variable that references the selection: `[Selection/<Column Name>]`. For example, `[Selection/Name]`. See [Use variables in actions](/docs/use-variables-in-actions).
   * To pass all values in a column, enter the column name of an element enclosed in square brackets: `[<Element name>/<Column name>]`. For example: `[Vendors/Portal]`

   You can also apply functions to generate dynamic values or to transform control and column values as needed.

## Open a workbook or template

Create an action that navigates to another Sigma workbook or template. Open the destination document in its published state, or [pass specific values to existing control elements](#pass-values-to-controls-in-the-destination-workbook) to instantly open a drilled-down view.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

* |  |  |
  | --- | --- |
  | **Action** | Select **Open Sigma doc**. |
  | **Destination** | Select a workbook or template to open.  *Interacting users can only view the destination document if granted permission to access it.* |
  | **Pass control values** | *See [Pass values to controls in the destination workbook](#pass-values-to-controls-in-the-destination-workbook) in this document.* |
  | **Open in** | Select an option to determine how the workbook or template opens in the browser.  + **New window**: Opens the document in a new browser window. + **Same window**: Opens the the document in the current browser window when the user interacts with the trigger element directly in Sigma. + **Parent window**: Opens the document in the current browser window when the user interacts with the trigger element in an embed. *The interacting user’s browser settings may change the selected **Open in** behavior. For example, **New window** may instead open the workbook or template in a new tab (same window), and **Same window** may instead open it in the same tab.* |

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

### Pass values to controls in the destination workbook

To open a drilled-down view of the destination workbook, add control targets and rules to the **Pass control values** field in step 4 of the [previous section](#configure-an-action-to-open-a-workbook).

1. In the **Pass control values** section, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add a control target**.
2. Configure the required fields to identify the control target and define the rule:

|  |  |
| --- | --- |
| **Update control** | Select a control element to update in the destination workbook. |
| **Set value as** | Select an option to determine the type of value Sigma passes to the control, then define the value.   * **Specific values**: Passes the specified (fixed) value. * **Values from a column**: Passes values from the specified column in the trigger element's underlying data (if applicable).  *Only available when the trigger element is a table, pivot table, input table, or visualization.* * **Custom formula**: Passes a value based on the defined formula. |

3. [optional] Repeat steps 1 and 2 to configure additional control targets and rules.

## Navigate the current workbook

Create an action that navigates to a specific location within the current workbook. Shift the focus to the top of a page or to an individual element.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

* |  |  |
  | --- | --- |
  | **Action** | Select **Navigate in this workbook**. |
  | **Destination** | Select the page or element to focus on in the workbook view |

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

Updated 3 days ago

---

Related resources

* [Intro to actions](/docs/intro-to-actions)
* [View and manage existing actions](/docs/view-and-manage-existing-actions)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Open a link](#open-a-link)
  + - [Open a link with a dynamic URL](#open-a-link-with-a-dynamic-url)
  + [Open a workbook or template](#open-a-workbook-or-template)
  + - [Pass values to controls in the destination workbook](#pass-values-to-controls-in-the-destination-workbook)
  + [Navigate the current workbook](#navigate-the-current-workbook)