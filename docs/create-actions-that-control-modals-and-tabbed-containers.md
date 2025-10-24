# Create actions that control modals and tabbed containers

# Create actions that control modals and tabbed containers

Workbooks support actions that change the state of modals and tabbed containers, enabling seamless transitions between related content views.

This document explains how to create actions that open modals, close modals, or select a specific tab in a tabbed container. For more information about actions in Sigma, see [Intro to actions](/docs/intro-to-actions).

## User requirements

> 📘
>
> The following requirements apply to users who configure actions. Users who access and interact with a workbook can typically trigger all existing actions within it. Any restrictions are noted in this document.

The ability to configure actions requires the following:

* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Full explore** or **Create, edit, and publish workbooks** permission enabled.
* You must be the workbook owner or be granted **Can explore**1 or **Can edit** [access to the workbook](/docs/folder-and-document-permissions).

1If you’re granted **Can explore** access to the workbook, you can configure actions in custom, saved, and shared views. Actions saved to views do not apply to the workbook’s published version.

## Open or close a modal

Create an action that opens or closes a modal in the current workbook. For more details about modals, see [Add a modal to a workbook](/docs/add-a-modal-to-a-workbook).

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

* |  |  |
  | --- | --- |
  | **Action** | Select **Open modal** or **Close modal**. |
  | **Select modal** | If configuring an **Open modal** action, select the modal to open, or choose **New modal**.  The **Close modal** action doesn't require modal selection because it must be configured on an element within the modal it closes. |

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

## Select tab

Create an action to display a specific tab in a [tabbed container](/docs/create-and-configure-tabbed-containers-beta) element.

1. Open the draft, custom view, or saved view of a workbook.
2. Select the trigger element (the element users must interact with to initiate the action).
3. In the editor panel, open the **Actions** tab.
4. [Create a new sequence](/docs/create-and-manage-action-sequences), or locate an existing sequence that you want to modify.
5. Select the default action (if creating a new sequence), or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** to add a new action to the sequence.
6. In the modal, configure the required fields to define the response:

* |  |  |
  | --- | --- |
  | **Action** | Select **Select tab**. |
  | **Tabbed container** | Select a tabbed container in this workbook. |
  | **Tab** | Select the tab to display. |

7. If the trigger element is a plugin, select the name of the plugin configuration object under **Custom plugin**. In your code editor, refresh your plugin, then test the action in the workbook. For more information, see [Configure plugins to use as trigger elements](/docs/configure-plugins-to-work-with-actions#configure-plugins-to-use-as-trigger-elements).

Updated 3 days ago

---

[Create actions that modify or refresh elements](/docs/create-actions-that-modify-or-refresh-elements)[Create actions that modify input table data](/docs/create-actions-that-modify-input-table-data)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Open or close a modal](#open-or-close-a-modal)
  + [Select tab](#select-tab)