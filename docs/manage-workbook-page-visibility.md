# Manage workbook page visibility

# Manage workbook page visibility

By default, workbook pages are visible to all users with permission to view, explore, or edit the workbook. You can change the visibility of individual pages to restrict viewing specific workbook content.

This document describes Sigma’s page visibility options and explains how to customize the visibility of a particular page.

## User requirements

The ability to manage workbook page visibility requires the following:

* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Create, edit, and publish workbooks** permission enabled.
* You must be the workbook owner or be granted **Can edit** [workbook permission](/docs/folder-and-document-permissions).

## Understanding page visibility

Page visibility is not a security feature. If you need to restrict access to data, use row-level security or column-level security. See [Set up row-level security](/docs/set-up-row-level-security) and [Configure column-level security](/docs/configure-column-level-security).

> 📘
>
> ### At least one page in a workbook must not have any page visibility restrictions applied.

> 🚧
>
> ### Page visibility settings apply in **View** and **Explore** mode only. The workbook owner and any user granted **Can edit** permission for the particular workbook can access all pages in **Edit** mode, regardless of page visibility settings.

> 🚧
>
> ### When a user with **Save as** permissions saves a copy of a workbook, all pages are visible in the copy, regardless of page visibility settings in the original workbook.

### Page visibility icons

Page tabs display icons to indicate the current page visibility setting:

|  |  |
| --- | --- |
| **no icon** | Indicates the page is visible to all users. |
|  | Indicates the page is visible to select users or teams. |
|  | Indicates the page is hidden from all users. |

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/manage-workbook-page-visibility/page-tab-icon.png)

### Page visibility in workbook versions and secure embeds

#### Tagged versions

Tagged workbook versions inherit the page visibility settings saved to the workbook when the tag is applied. Therefore, a page can be accessible to a user in one version and hidden from the same user in another.

#### Secure embeds

Page visibility in secure embeds is determined by team settings. A page is only visible to an embed user when shown to the user’s assigned team (via **Show page to all users** or **Only show to select users or teams**).

> 🚧
>
> ### When a secure embed user saves a copy of an embedded workbook, all pages are visible in the copy, regardless of page visibility settings in the original workbook.

## Hide or unhide a page

Use the **Hide page** and **Unhide page** options to quickly update the page visibility for all users.

1. Open a workbook in **Edit** mode.
2. Locate the tab for the page you want to customize.
3. Click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) in the tab to open the page menu, then select the available option:

   |  |  |
   | --- | --- |
   | **Hide page** | Hides page from all users accessing the workbook in **View** or **Explore** mode. *Available when the page is currently visible to all users.* |
   | **Unhide page** | Shows page to all users accessing the workbook in any mode.  *Available when the page is currently hidden from all or select users and teams.* |

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/manage-workbook-page-visibility/page-menu_hide-page.png)

## Customize page visibility

Use the **Customize page visibility** option to update the page visibility for all users or specific users and teams.

1. Open a workbook in **Edit** mode.
2. Locate the tab for the page you want to customize.
3. Click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) in the tab to open the page menu, then select **Customize page visibility**.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/manage-workbook-page-visibility/page-menu_customize-page-visibility.png)
4. In the **Customize Page Visibility** modal, configure the page visibility:

   1. Click the **Page visibility setting** field and select an option from the dropdown:

      |  |  |
      | --- | --- |
      | **Hide page from all users** | Hides page from all users accessing the workbook in **View** or **Explore** mode. |
      | **Show page to all users** *(default)* | Shows page to all users accessing the workbook in any mode. |
      | **Only show to select users or teams** | Only shows page to selected users and teams. Hides page from remaining users accessing the workbook in **View** or Explore **mode**. |
   2. If you selected **Only show to select users or teams** in step 4a, use the **Select users** field to search for and select applicable users and teams.
   3. Click **Save** to apply the page visibility change.

Updated 3 days ago

---

[Manage workbook localization](/docs/manage-workbook-localization)[Add shortcuts to documents](/docs/add-shortcuts-to-documents)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Understanding page visibility](#understanding-page-visibility)
  + - [Page visibility icons](#page-visibility-icons)
    - [Page visibility in workbook versions and secure embeds](#page-visibility-in-workbook-versions-and-secure-embeds)
  + [Hide or unhide a page](#hide-or-unhide-a-page)
  + [Customize page visibility](#customize-page-visibility)