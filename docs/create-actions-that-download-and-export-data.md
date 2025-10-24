# Create actions that send notifications and export data

# Create actions that send notifications and export data

You can create workbook actions that initiate direct downloads as well as exports to email, Slack channels, Microsoft Teams Channels, Microsoft SharePoint, webhooks, and cloud storage.

For email and Slack, you can create actions that send notifications to users and channels. These notifications can be configured independently of an export, and support both static and dynamic lists of users.

> 🚩
>
> This documentation describes one or more public beta features that are in development. Beta features are subject to quick, iterative changes; therefore the current user experience in the Sigma service can differ from the information provided in this page.
>
> This page should not be considered official published documentation until Sigma removes this notice and the beta flag on the corresponding feature(s) in the Sigma service. For the full beta feature disclaimer, see [Beta features](/docs/sigma-product-releases#beta-features).

This document explains how to create actions that export workbook content to specific destinations or notify users by Slack and email. For more information about configuring these actions in Sigma, see [Intro to actions](/docs/intro-to-actions). For more information on exporting data, see [Export data.](/docs/schedule-a-conditional-export-or-alert)

## User requirements

> 📘
>
> The following requirements apply to users who configure actions. Users who access and interact with a workbook can typically trigger all existing actions within it. Any restrictions are noted in this document.

The ability to configure actions requires the following:

* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Full explore** or **Create, edit, and publish workbooks** permission enabled.
* You must be the workbook owner or be granted **Can explore**1 or **Can edit** [access to the workbook](/docs/folder-and-document-permissions).

1If you’re granted **Can explore** access to the workbook, you can configure actions in custom, saved, and shared views. Actions saved to views do not apply to the workbook’s published version.

## Send notifications by email (Beta)

Create an action that emails selected recipients, without sending an attachment or export.

> 📘
>
> ### This action can only be configured and triggered by users assigned an account type with the **Export to email** permission enabled.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

|  |  |
| --- | --- |
| **Action** | Select **Notify and export**. |
| **Destination** | Select **Email**. |
| **Recipient** | For **Specific users / teams**, enter one or more comma-separated email addresses for the recipients.  For **Dynamic recipients**, provide a list of users based on dynamic information from a control or formula. If your action is configured on a table, pivot table, or input table, you can also create a list of dynamic recipients from a column. |
| **Subject** | Enter a subject line for the email notification. For dynamic text, press **=** on your keyboard to open the formula bar and [configure dynamic text.](/docs/text-elements#add-dynamic-text-based-on-your-data) |
| **Message** | [optional] Enter a message to include in the email body. For dynamic text, press **=** on your keyboard to open the formula bar and [configure dynamic text](/docs/text-elements#add-dynamic-text-based-on-your-data). Sigma includes basic information about the sender and workbook in the email body. |
| **Link to workbook** | [optional] On by default. Turn the **Link to workbook** toggle on to include a link to the workbook in the email. When the toggle is turned on, you can select whether to link to the entire workbook (top of page 1), a specific page (top of specified page), or a specific element. |
| **Attachment** | Confirm that the **Attachment** toggle is turned off. |
| **More options** | [optional] Select the **Run queries as recipient** checkbox to run workbook queries as the recipient of the email. If deselected (default), queries run as the user who performs the action. When **Run queries as recipient** is enabled, each query runs separately per recipient. Larger list of recipients result in more queries and longer processing times. Each recipient must be a Sigma user, and the user who performs the action must have an account type with the **Run exports as recipient permission** enabled. |

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

## Send notifications by Slack (Beta)

Create an action that sends a Slack message to selected recipients, without sending an attachment or export.

To create a Slack notification action, the [Slack integration](/docs/manage-slack-integration) must be enabled for your organization. If you want to send notifications to a private channel, you must also add Sigma to the private channel. See [Adding Sigma to a private Slack channel.](/docs/manage-slack-integration#adding-sigma-to-a-private-slack-channel)

> 📘
>
> ### This action can only be configured and triggered by users assigned an account type with the **Export to Slack** permission enabled.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

|  |  |
| --- | --- |
| **Action** | Select **Notify and export**. |
| **Destination** | Select **Slack**. |
| **To** | For **Specific users / teams**, enter a comma-separated list of Slack #channel-names, channel-ids, or member-ids.  For **Dynamic recipients**, provide a list of channel names, channel ids, or member ids based on dynamic information from a control or formula. If your action is configured on a table, pivot table, or input table, you can also provide a column that contains a list of channel names, channel ids, or member ids. |
| **Message** | [optional] Enter a message to include in the Slack notification. For dynamic text, press **=** on your keyboard to open the formula bar and [configure dynamic text](/docs/text-elements#add-dynamic-text-based-on-your-data). Sigma includes basic information about the sender and workbook in the message body by default. For more information on formatting a message, such as tagging users, see [Format a slack message.](/docs/format-a-slack-message) |
| **Link to workbook** | [optional] On by default. Turn the **Link to workbook** toggle on to include a link to the workbook in the message. When the toggle is turned on, you can select whether to link to the entire workbook (top of page 1), a specific page (top of specified page), or a specific element. |
| **Attachment** | Confirm that the **Attachment** toggle is turned off. |

> 💡
>
> ### When sending to Slack channels, Sigma recommends using channel ids rather than channel names. For more information, see [Format a slack message](/docs/format-a-slack-message).

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

## Download a file

Create an action that downloads an entire workbook, a specific page, or an individual element directly to the interacting user’s device.

> 📘
>
> ### This action can only be configured and triggered by users assigned an account type with the **Download** permission enabled.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

* |  |  |
  | --- | --- |
  | **Action** | Select **Notify and export**. |
  | **Destination** | Select **Download**. |
  | **Attachment** | Select the workbook content to download, then choose a file format. |

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

## Export to email

Create an action that emails an entire workbook, a specific page, or an individual element to selected recipients.

To configure a standard export to email that is not managed by a workbook action, see [Export to email](/docs/export-to-email).

> 📘
>
> ### This action can only be configured and triggered by users assigned an account type with the **Export to email** permission enabled.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

|  |  |
| --- | --- |
| **Action** | Select **Notify and export**. |
| **Destination** | Select **Email**. |
| **Recipient** | For **Specific users / teams**, enter one or more comma-separated email addresses for the recipients.  For **Dynamic recipients**, provide a list of users based on dynamic information from a control or formula. If your action is configured on a table, pivot table, or input table, you can also create a list of dynamic recipients from a column. |
| **Subject** | Enter text to include in the email subject line. For dynamic text, press **=** on your keyboard to open the formula bar and configure dynamic text. |
| **Message** | [optional] Enter a message to include in the email body. For dynamic text, press **=** on your keyboard to open the formula bar and configure dynamic text. |
| **Attachment** | Confirm that the **Attachment** toggle switch is on. Select the workbook content to export, then choose a file type. |
| **More options** | [optional] Select the **Include link to workbook** checkbox to allow the export recipient to open the workbook directly from the email.  [optional] Select the **Run queries as recipient** checkbox to run workbook queries as the recipient of the email. If deselected (default), queries run as the user who performs the action. When **Run queries as recipient** is enabled, each query runs separately per recipient. Larger list of recipients result in more queries and longer processing times. Each recipient must be a Sigma user, and the user who performs the action must have an account type with the **Run exports as recipient permission** enabled.  [optional] Select the **Send as .zip file** checkbox to send attachments as a compressed zip file. |

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

## Export to Slack

Create an action that exports an entire workbook, a specific page, or an individual element to Slack.

To create a Slack export action, the [Slack integration](/docs/manage-slack-integration) must be enabled for your organization. If you want to send notifications to a private channel, you must also add Sigma to the private channel. See [Adding Sigma to a private Slack channel.](/docs/manage-slack-integration#adding-sigma-to-a-private-slack-channel)

> 📘
>
> ### This action can only be configured and triggered by users assigned an account type with the **Export to Slack** permission enabled.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

|  |  |
| --- | --- |
| **Action** | Select **Notify and export**. |
| **Destination** | Select **Slack**. |
| **To** | For **Specific users / teams**, enter a comma-separated list of Slack #channel-names, channel-ids, or member-ids.  For **Dynamic recipients**, provide a list of channel names, channel ids, or member ids based on dynamic information from a control or formula. If your action is configured on a table, pivot table, or input table, you can also provide a column that contains a list of channel names, channel ids, or member ids. |
| **Message** | [optional] Enter a message to include in the Slack notification. For dynamic text, press **=** on your keyboard to open the formula bar and [configure dynamic text](/v0.0/docs/text-elements). Sigma includes basic information about the sender and workbook in the message body by default. For more information on formatting a message, such as tagging users, see [Format a slack message.](/docs/format-a-slack-message) |
| **Attachment** | Confirm that the **Attachment** toggle is turned on. Select the workbook content to export, then choose a file type. |
| **More options** | [optional] Select the **Include link to workbook** checkbox to allow Slack channel members to open the workbook directly from the Slack message. |

> 💡
>
> ### When sending to Slack channels, Sigma recommends using channel ids rather than channel names. For more information, see [Format a slack message](/docs/format-a-slack-message).

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

## Export to Microsoft Teams (Beta)

Create an action that exports an entire workbook, a specific page, or an individual element to Microsoft Teams.

To create a Teams export action, the [Microsoft integration](/docs/manage-microsoft-integration) must be enabled for your organization. To send notifications to a channel, you must also add Sigma to the channel. See [Add the Sigma Notifications app to Teams](/docs/manage-microsoft-integration#add-the-sigma-notifications-app-to-teams).

> 📘
>
> ### This action can only be configured and triggered by users assigned an account type with the **Export to Microsoft Teams and SharePoint** permission enabled.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

|  |  |
| --- | --- |
| **Action** | Select **Notify and export**. |
| **Destination** | Select **Microsoft Teams**. |
| **Channel URL** | Enter the URL for the Microsoft Teams channel. For example:  `https://teams.microsoft.com/l/channel/><channel-ID-and-name>?groupId=<group-ID>&tenantId=\<tenant-ID>` |
| **Message** | [optional] Enter a message to include in the notification. Sigma includes basic information about the sender and workbook in the message body by default. For more information on formatting a Teams message, such as supported markdown syntax, see [Format a Microsoft Teams message](/docs/format-a-microsoft-teams-message). |
| **Attachment** | Select the workbook content to export, then choose a file type and layout. |
| **More options** | [Optional] Select the **Include link to workbook** checkbox to allow Teams channel members to open the workbook directly from the Teams message. |

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

## Export to SharePoint (Beta)

Create an action that exports an entire workbook, a specific page, or an individual element to Microsoft SharePoint.

To create a SharePoint export action, the [Microsoft integration](/docs/manage-microsoft-integration) must be enabled for your organization.

> 📘
>
> ### This action can only be configured and triggered by users assigned an account type with the **Export to Microsoft Teams and SharePoint** permission enabled.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

|  |  |
| --- | --- |
| **Action** | Select **Notify and export**. |
| **Destination** | Select **SharePoint**. |
| **Folder URL** | Enter the URL for the SharePoint folder. For example:  `https://<organization>.sharepoint.com/:f:/s/<site-name>/<folder-id>` |
| **Attachment** | Select the workbook content to export, then choose a file type and layout. |

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

## Export to a webhook

Create an action that exports an individual element’s data to another application with a webhook.

> 📘
>
> ### This action can only be configured and triggered by users assigned an account type with the **Export to webhook** permission enabled.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

* |  |  |
  | --- | --- |
  | **Action** | Select **Notify and export**. |
  | **Destination** | Select **Webhook**. |
  | **Endpoint** | Enter the receiving application’s endpoint. |
  | **Attachment** | Select an element to export, then choose a data format. |

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

## Export to cloud storage

Create an action that exports an individual element’s data to cloud storage.

> 📘
>
> ### This action can only be configured and triggered by users assigned an account type with the **Export to cloud** permission enabled.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

* |  |  |
  | --- | --- |
  | **Action** | Select **Notify and export**. |
  | **Destination** | Select **Cloud Storage**. |
  | **Storage integration** | Enter an integration name. |
  | **Cloud Storage URI** | Enter a file path for the export destination. |
  | **Element** | Select an element to export, then choose a file format. |
  | **More options** | [optional] Select the **Prefix file name with current date and time** checkbox to include the export date and time (in ISO format) in the file name. |

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

## Example: Slack notification workflow for new project tasks

You can configure workbook actions that send notifications to users about changes to a workbook, such as new data entry or changes to existing data.

In this example, imagine you're interacting with a project tracker data app. Users can add new projects, tasks, and statuses.

![A gif shows a user demonstrating a project tracker application, adding a task to a project.](https://files.readme.io/0c3888e79db402e74697fdbf6bcfbc309dea0ff2661fe55f21fe5be16c4d33ce-Schedule_Weekly_Recap_Clip.gif)

You decide to configure a workbook action to send a notification whenever a user assigns a new task. Currently, users add tasks by selecting Add Task, entering information into the provided modal, and clicking the Create Task button to add the task to an input table.

Using the **Notify and export** action, you can send a notification by Slack whenever someone clicks the Create Task button, so that users are always up to date when a task is assigned to them.

1. Navigate to the Create Task modal, and open the **Actions** panel.
2. Add an action to the **On click - primary** action sequence.
3. In the **Action** modal, configure the action:

|  |  |
| --- | --- |
| **Action** | Select **Notify and export**. |
| **Destination** | Select **Slack**. |
| **To** | Select **Dynamic recipients** and **Formula**  In the formula bar, enter the following formula: `Lookup([Employees/Slack ID], [ct-Task-Owner], [Employees/Name])`  In the context of this workbook, this formula uses a Lookup to return a Slack ID based on the name of the user currently selected in the Task Owner control. |
| **Message** | Enter a message to be sent to the user with the assigned task.  To tag them, press **=** on your keyboard to open the formula bar. In the formula bar, enter the following formula: `"<@" & Lookup([Employees/Slack ID], [ct-Task-Owner], [Employees/Name]) & ">"`  In the context of this workbook, this concatenates the user's Slack ID with the characters required to tag them in Slack. For more information on this, see [Format a slack message](/docs/format-a-slack-message). |
| **Attachment** | Turn the **Attachment** toggle off. |
| **More options** | Select the **Include link to workbook** checkbox. |

4. [optional] Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** to add a condition to the **Action sequence**. In the example below, the condition `IsNotNull([ct-Task-Name])` prevents tasks from being published with a blank name.

![A screenshot of the Sigma UI shows a notification action configured according to this tutorial](https://files.readme.io/201744d9b9dcba14a6df6e368bb291e2e0b0a7ee601902a9c41a5bec59b8e486-Notification_Action_Configuration.png)

Updated 3 days ago

---

[Create actions that modify input table data](/docs/create-actions-that-modify-input-table-data)[Create actions that generate embed iframe events](/docs/create-actions-that-trigger-embed-iframe-events)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Send notifications by email (Beta)](#send-notifications-by-email-beta)
  + [Send notifications by Slack (Beta)](#send-notifications-by-slack-beta)
  + [Download a file](#download-a-file)
  + [Export to email](#export-to-email)
  + [Export to Slack](#export-to-slack)
  + [Export to Microsoft Teams (Beta)](#export-to-microsoft-teams-beta)
  + [Export to SharePoint (Beta)](#export-to-sharepoint-beta)
  + [Export to a webhook](#export-to-a-webhook)
  + [Export to cloud storage](#export-to-cloud-storage)
  + [Example: Slack notification workflow for new project tasks](#example-slack-notification-workflow-for-new-project-tasks)