# Create custom context menu actions

# Create custom context menu actions

Add custom context menu items in tables, pivot tables, input tables, and charts to provide clear, discoverable triggers for actions relevant to selected cells and data points. You can add standalone menu items or create nested submenus that execute any action effect, including [calling stored procedures](/docs/create-actions-that-call-stored-procedures), [generating iframe events](/docs/create-actions-that-trigger-embed-iframe-events), and [opening modals](/docs/create-actions-that-navigate-to-destinations#open-or-close-a-modal).

This document explains how to add custom context menu items and define them as action triggers.

## User requirements

The ability to add custom context menu items and define them as action triggers requires the following:

* You must be assigned an [account type](/docs/account-type-and-license-overview) with the **Full explore** or **Create, edit, and publish workbooks** permission enabled.
* You must be the workbook owner or have **Can explore** or **Can edit** [workbook access](/docs/folder-and-document-permissions). *If you have**Can explore** access, you can create and configure custom context menu items in custom views only.*

## Add custom context menu items

Add standalone menu items or create nested submenus to supplement existing cell or data point context menus.

1. Select the element you want to customize.
2. In the editor panel, open the **Format** tab.
3. Expand the **Custom context menu** section and click **+ Add an option** for each menu item you want to add.

   ![](https://files.readme.io/05b259a33bed8d6ef9b530b9a74653420d334079eb7ed4fc647433599c9d8390-image.png)
4. In each menu item card, double-click the "Option" placeholder text and enter the label to display in the menu. You can also click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** and select **Rename** to edit the text.

   ![](https://files.readme.io/692761cbcbd89734f75321f9c55a3f2d3ea29b051e68bffdbb4eb55935d07ee9-image.png)
5. [optional] To reorder the menu items, click and hold any card's drag handle (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/drag-handle-dots.svg)), then move it to the desired position.

   ![](https://files.readme.io/45deddbed1ca6fda26d72ea5c969c5fa7517dc06ce45e370f0c481a3d752087f-image.png)
6. [optional] To create a nested submenu, click and hold a card's drag handle (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/drag-handle-dots.svg)), then drag it below the parent menu item and slightly to the right. You can also click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**, then hover over **Move to** and select the name of the parent menu item.

   When a menu item is successfully nested in a submenu, it displays as an indented card below the parent menu item.

   ![](https://files.readme.io/4a6267479adaf56924cc2527a9b2d50d05a3fc20352a48d3a6a0cc9d8c610aaa-image.png)

   > 📘
   >
   > ### With nested submenus, you can only configure actions on child menu items. Parent menu items cannot trigger actions.
7. [optional] To delete a menu item, hover over the card, then click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** and select **Delete**. When you delete a parent menu item, any child menu items are also deleted.

   ![](https://files.readme.io/eeb52b95d1a139a75b03ea5f39e793ee9f1aad13852ca5bf9c00fd585d63464b-image.png)

## Define custom context menu items as action triggers

Configure action sequences with custom context menu items as the triggers.

1. Select the element containing custom context menu items.
2. In the editor panel, open the **Actions** tab.
3. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action sequence** to create a new sequence, or apply the following steps to the default empty sequence. Each menu item requires a separate sequence.

   ![](https://files.readme.io/4d9613755968927568371b1b21026df71216b35b0068ce35265ef32c3e24b093-image.png)
4. In the sequence, configure the menu item as the action trigger:

   1. Click the trigger type field (upper field) and select **Cell context menu**.
   2. Click the trigger target field (lower field) and select the name of a specific menu item.

   ![](https://files.readme.io/a870691700b803da667b56c4893d372698cebd92e54468bd951d263c20b70af3-image.png)
5. Configure the remaining logic on the menu item. See [Action effects](/docs/intro-to-actions#action-effects) for information about available effects and links to corresponding configuration steps.
6. Repeat steps 3 through 5 for all single menu items and nested child menu items.

Updated 3 days ago

---

[Create cross-element filters](/docs/create-cross-element-filters)[View and manage existing actions](/docs/view-and-manage-existing-actions)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Add custom context menu items](#add-custom-context-menu-items)
  + [Define custom context menu items as action triggers](#define-custom-context-menu-items-as-action-triggers)