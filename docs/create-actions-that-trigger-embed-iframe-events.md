# Create actions that generate embed iframe events

# Create actions that generate embed iframe events

Workbook actions configured in an embedded workbook support interaction with host applications. You can configure an action to send an iframe event from your embedded content to your host application, which can then react to this event with some outcome. For example, you can use these events to add custom tracking, change the UI of your application, or trigger your own application APIs.

This document explains how to configure the **Generate iframe event** action in an embedded workbook. For more information about actions in Sigma, see [Intro to actions](/docs/intro-to-actions). For more information about embedding, see [Intro to embedded analytics](/docs/intro-to-embedded-analytics).

## System and user requirements

> 📘
>
> The following requirements apply to users who configure actions. Users who access and interact with a workbook can typically trigger all existing actions within it. Any restrictions are noted in this document.

The ability to configure actions requires the following:

* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Full explore** or **Create, edit, and publish workbooks** permission enabled.
* You must be the workbook owner or be granted **Can explore**1 or **Can edit** [access to the workbook](/docs/folder-and-document-permissions).

1If you’re granted **Can explore** access to the workbook, you can configure actions in custom, saved, and shared views. Actions saved to views do not apply to the workbook’s published version.

This workbook action is only relevant for embedded workbooks. See [Intro to embedded analytics](/docs/intro-to-embedded-analytics) for specific requirements for public and secure embedding.

## Prerequisites

Configure an event listener and an `action:outbound` event in your application to receive messages about the user interactions in the embedded workbook. You can then develop custom logic in your host application to respond to these events.

* See [Implement inbound and outbound events in embeds](/docs/inbound-and-outbound-events-in-embeds) for information about about how to send and receive events between a parent application and Sigma.
* See the configuration instructions for the [`action:outbound`](/docs/inbound-and-outbound-events-in-embeds#actionoutbound) event to configure the outbound event required for this workbook action to take effect.

## Generate an outbound iframe event

Create an action that generates an outbound iframe event.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

* |  |  |
  | --- | --- |
  | **Action** | Select **Generate iframe event**. |
  | **Event name** | Enter the name of the event configured in the `name` property in the `action:outbound` event in your host application. |
  | **Event key** and **Key value** | Enter the key names and values configured in the `values` property in the `action:outbound` event in your host application. |

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

Updated 3 days ago

---

[Create actions that send notifications and export data](/docs/create-actions-that-send-notifications-and-export-data)[Create actions that modify plugins](/docs/create-actions-that-modify-plugins)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Prerequisites](#prerequisites)
  + [Generate an outbound iframe event](#generate-an-outbound-iframe-event)