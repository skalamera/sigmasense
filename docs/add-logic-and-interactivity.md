# Intro to actions

# Intro to actions

Actions are user-defined interactivity that you can configure within and across workbook elements. By automating responses to specific user interactions, you can create efficient workbook workflows that produce quick and relevant data insights.

This document introduces action conditions, triggers, and effects. For information about using actions, see the **Related resources** section at the end of this page.

## Understanding actions

An individual action consists of a condition (optional), a trigger, and an effect.

|  |  |
| --- | --- |
| Trigger | A user interaction with a specific element (the trigger element) that initiates the response of one or more actions or sequences of actions. |
| Condition (optional) | A rule that determines when an action or sequence of actions1 executes. |
| Effect | The defined response to the user interaction. |

1You can configure a single action on a workbook element or a [sequence of multiple actions](/docs/configure-actions-in-sequences) that execute in a specified order.

### Action conditions

You can define an optional condition for any action sequence. The condition can be a custom formula or, if you are configuring an action for a control, the condition can be the value of the control.

For more information, see [Make an action conditional](/docs/make-an-action-conditional).

### Action triggers

Action triggers can be configured on most element types. The following table describes the supported trigger types.

> 📘
>
> ### Actions are not initiated when a trigger element is maximized. This behavior prevents users from triggering action effects that are not visible while the maximized element spans the full browser window.

| Element type | Trigger type (user interaction) |
| --- | --- |
| Table, pivot table, or input table | **On select**: User selects a cell in a specific column.  **Cell context menu**: User selects a [custom context menu](/docs/create-custom-context-menu-actions) item on a cell. |
| Visualization | **On select**: User selects a data point or category on the chart.  **Cell context menu**: User selects a [custom context menu](/docs/create-custom-context-menu-actions) item on a data point. |
| UI element\ *(button or image only)* | **On click**: User clicks the element. |
| Control element | **On change**: User changes the control value. |
| Modal | **On click - primary**: User clicks the primary button.  **On click - secondary**: User clicks the secondary button.  **On close**: user clicks the X or clicks outside the modal. |
| Plugin | User-configured interaction. See [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements). |

### Action effects

The following table lists the actions you can configure on a trigger element and describes the corresponding effect.

| Category | Action | Effect |
| --- | --- | --- |
| Navigation | [Open link](/docs/create-actions-that-navigate-to-destinations#configure-an-action-to-open-a-link) | Navigates to an external link or destination within Sigma. |
| [Open Sigma doc](/docs/create-actions-that-navigate-to-destinations#configure-an-action-to-open-a-workbook) | Navigates to a different Sigma workbook. |
| [Navigate in this workbook](/docs/create-actions-that-navigate-to-destinations#configure-an-action-to-navigate-the-workbook) | Shifts the focus to the top of a specific page or an individual element in the current workbook. |
| [Download and export](/docs/create-actions-that-download-and-export-data) | Initiates a direct download or an export to email, Slack, webhook, or cloud storage. |
| Controls | [Set control value](/docs/create-actions-that-manage-control-values#configure-an-action-to-set-a-control-value) | Sets the value of a specific control element in the current workbook. |
| [Clear control](/docs/create-actions-that-manage-control-values#configure-an-action-to-clear-a-control-value) | Clears the values of a specific control element in the current workbook. |
| Elements | [Modify element](/docs/create-actions-that-modify-or-refresh-elements) | Modifies an element's columns, groupings, properties, or axis scale. |
| [Refresh element](/docs/create-actions-that-modify-or-refresh-elements#configure-an-action-to-refresh-an-element) | Refreshes the data of a specific element in the current workbook.  *This action doesn’t apply to materialized elements.* |
| Modals and tabbed containers | [Open modal](/docs/create-actions-that-navigate-to-destinations#open-or-close-a-modal) | Opens a modal in the current workbook. |
| [Close modal](/docs/create-actions-that-navigate-to-destinations#open-or-close-a-modal) | Closes an open modal. |
| [Select tab](/docs/create-actions-that-control-modals-and-tabbed-containers#select-tab-beta) | Displays a tabbed container opened to a specific tab. |
| Input tables | [Insert row](/docs/create-actions-that-modify-input-table-data#insert-row) | Adds a new row to an existing input table. |
| [Update row](/docs/create-actions-that-modify-input-table-data#update-row) | Updates row values in an existing input table. |
| [Delete row](/docs/create-actions-that-modify-input-table-data#delete-row) | Deletes a row in an existing input table. |
| Advanced | [Call stored procedure](/docs/create-actions-that-call-stored-procedures) | Calls a stored procedure. |
| [Generate iframe event (for embedding)](/docs/create-actions-that-trigger-embed-iframe-events) | Generates an outbound iframe event. |
| [Trigger plugin](/docs/create-actions-that-modify-plugins) | Triggers effects within a plugin. |

## Action configurations

Actions feature versatile configurations to support responses that are highly relevant to your specific needs and preferences.

Examples:

* Configure the **Open URL** action to open a static link, or utilize dynamic text to generate URLs that adjust to control or column values in the current workbook.
* Configure the **Set control value** action to filter the trigger element itself, or create a cross-element action that filters a child element.
* Configure the **Open Sigma doc** action to open another workbook in its published state, or pass values to control elements in the destination workbook to open a custom, drilled-down view.

For detailed information about configuring the different types of actions, see the **Related resources** section at the end of this page.

Updated 3 days ago

---

Related resources

* [Create actions that navigate to destinations](/docs/create-actions-that-navigate-to-destinations)
* [Create actions that manage control values](/docs/create-actions-that-manage-control-values)
* [Create actions that modify or refresh elements](/docs/create-actions-that-modify-or-refresh-elements)
* [Create actions that download and export data](/docs/create-actions-that-download-and-export-data)
* [View and manage existing actions](/docs/view-and-manage-existing-actions)
* [Make an action conditional](/docs/make-an-action-conditional)
* [Use variables in actions](/docs/use-variables-in-actions)

* [Table of Contents](#)
* + [Understanding actions](#understanding-actions)
  + - [Action conditions](#action-conditions)
    - [Action triggers](#action-triggers)
    - [Action effects](#action-effects)
  + [Action configurations](#action-configurations)