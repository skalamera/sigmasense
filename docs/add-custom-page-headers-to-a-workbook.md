# Add custom page headers to a workbook (Beta)

# Add custom page headers to a workbook (Beta)

> 🚩
>
> This documentation describes one or more public beta features that are in development. Beta features are subject to quick, iterative changes; therefore the current user experience in the Sigma service can differ from the information provided in this page.
>
> This page should not be considered official published documentation until Sigma removes this notice and the beta flag on the corresponding feature(s) in the Sigma service. For the full beta feature disclaimer, see [Beta features](/docs/sigma-product-releases#beta-features).

You can create custom page headers that appear on one or more workbook pages. Page headers can be configured to stick to the top of the page as users scroll, allowing you to make content visible regardless of where the user navigates in the workbook.

This document explains how to enable, customize, and manage page headers.

## User requirements

* To configure a page header in a saved or custom view, you must be assigned an account type with the **Full explore** permission.
* To configure a page header in the published version of a workbook, you must be assigned an account type with the **Create, edit, and publish workbooks** permission.

## Enable page header

Add a page header for your workbook in workbook settings:

1. Click on the background of your workbook. In the side panel, select **Workbook settings**.
2. Open the **Layout settings**.
3. Check the box next to **Page header**

A blank header appears on all workbook pages. To create additional page headers and manage their visibility, see [Manage multiple page headers](#manage-multiple-page-headers).

## Customize a header

You can customize the size, scroll style, background color, and contents of a header.

### Header settings

You can customize the following for a page header:

* **Size:** Select the header. Use the bottom drag handle to resize.
* **Scroll style:** Select the header. In the editor panel, navigate to **Properties**. Under **Scroll style**, select **Sticky** to keep the header fixed as users scroll, or **Scroll** to allow users to scroll past the header.
* **Background color:** Select the header. In the editor panel, navigate to **Format**. Select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/fill-color.svg) **Background color** and choose a color for the header.

You can rename, duplicate, or delete a header in the **Manage header** menu:

1. Click on the background of your workbook. In the side panel, select **Workbook settings**.
2. Open the **Layout settings**.
3. Under **Manage headers**, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More options** for the header you want to

### Header contents

You can add any element to a page header. Since one header can be used on multiple pages, this allows you to quickly add the same element to multiple pages.

There are multiple ways to add an element to a header:

* With the header selected, select an element in the **Add element** bar. If the default element size is smaller than the current header size, it appears inside the header automatically.
* Select an element from the workbook page. Drag and drop the element inside the header. The element must be smaller than the current header size to drag and drop successfully.

## Manage multiple page headers

You can create multiple page headers in the same workbook and choose which pages they appear on.

### View pages by header

To view which pages a header is assigned to:

1. Click on the background of your workbook.
2. In the side panel, select **Workbook settings**.
3. Open the **Layout settings**.
4. Under **Manage headers**, open the menu option for the number of pages with that header.
5. In the **Go to** menu, you can see the list of pages that header is assigned to.

![The manage header menu shows three pages assigned to the header.](https://files.readme.io/30d15be45bcff9fc30c54467f17b7ab711943fc7747f9e8d2a2fe81556d8f603-page_header_screenshot_2.png)

### Add a new header

To add additional headers to your workbook:

1. Click on the background of your workbook. In the side panel, select **Workbook settings**.
2. Open the **Layout settings**.
3. Under **Manage headers**, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg) **Add new header.**

![A user hovers over the add new header option.](https://files.readme.io/05e43d77bb203812a83cedc14890b961fd3ab63e95c8a0af92f7792cb39af699-add_new_header_screenshot.png)

### Set the header for a page

To set the header for a page:

1. Navigate to the page you want to set the header for.
2. Click on the background of the workbook.
3. In the side panel, open the **Page header** dropdown.
4. Select the header you want to apply to the page.

![The header options for a workbook page showing three options: Header 1, Header 2, and Header 3.](https://files.readme.io/8780194fdda70b2164b823046bdb4260fc584aebb3d12629a65f16eb59451485-Set_header_for_a_page.png)

## Example: Use a page header and navigation element to create a custom navigation bar

You can use a page header and navigation element to create a custom navigation bar for your workbook. The navigation element provides a list of destinations for users to explore, and the page header keeps the navigation bar visible as users switch pages and scroll.

### Setup

To follow along with this example step-by-step, create a new workbook with the following pages:

* Sales - East
* Sales - West
* Raw Data

![The workbook page tabs show three options: Sales - East, Sales - West, and Raw Data.](https://files.readme.io/ce54c32de20ef32653f72a517edf1e0b17abfae1e7b41a283990f3b7fa1b176e-page_header_screenshot_one.png)

### Add a page header

To start, enable a page header for the workbook:

1. Click on the background of your workbook. In the side panel, select **Workbook settings**.
2. Open the **Layout settings**.
3. Check the box next to **Page header**.

A page header appears on all workbook pages. You can confirm this by going to **Workbook settings** > **Layout settings** > **Manage headers** and opening the **On 3 pages** dropdown for the header. Though we can make multiple headers, this example uses one shared header for all workbook pages.

![The manage page headers dropdown shows the three pages listed for the header.](https://files.readme.io/30d15be45bcff9fc30c54467f17b7ab711943fc7747f9e8d2a2fe81556d8f603-page_header_screenshot_2.png)

### Add a navigation element to the header

Now, add a navigation element to the page header to make it available across all workbook pages:

1. Select the header.
2. In the **Add element** bar, select **Layout** > **Navigation**.

The navigation element appears in the header. By default, it populates with the current workbook pages as the navigation options.

![A navigation element with the three workbook pages as options in the page header.](https://files.readme.io/4bb23fc6b98f51d6320dff63882008c95aadae1e499e41bbe75b791f058fbeaa-page_header_screenshot_3.png)

### Hide the workbook page tabs

Since the page header and navigation element appear across all workbook pages, a user can navigate the without the workbook page tabs. You can hide the workbook page tabs to create a cleaner interface for users.

1. Select the workbook page.
2. In the editor panel, under **Settings**, select **Workbook settings**.
3. Open the **Layout settings**.
4. In the **Layout settings** section, check the box next to **Hide page tabs in view mode**.
5. In the confirmation modal, click **Confirm**.

![The workbook page tabs are hidden, and the navigation element is the only way to navigate the workbook.](https://files.readme.io/9c166d11011d89a8a07de49edc460195c9f2f65cc6ee37133ae0d5be00881589-Page_header_screenshot_4.gif)

From here, you can customize the navigation options, adding external links, submenus, and more as you need. Since the workbook page tabs are hidden, you don't have to worry about potential user confusion that might arise from the navigation element and page tabs differing.

> 🚩
>
> Hiding page tabs does not prevent users from navigating to the page from a direct link, and is not a security feature. To restrict access to data, use a data model with row-level security or column-level security. For more information, see [Set up row-level security](/docs/set-up-row-level-security) and [Configure column-level security](/docs/configure-column-level-security).

Updated 3 days ago

---

[Add shortcuts to documents](/docs/add-shortcuts-to-documents)[Workbook templates](/docs/templates)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Enable page header](#enable-page-header)
  + [Customize a header](#customize-a-header)
  + - [Header settings](#header-settings)
    - [Header contents](#header-contents)
  + [Manage multiple page headers](#manage-multiple-page-headers)
  + - [View pages by header](#view-pages-by-header)
    - [Add a new header](#add-a-new-header)
    - [Set the header for a page](#set-the-header-for-a-page)
  + [Example: Use a page header and navigation element to create a custom navigation bar](#example-use-a-page-header-and-navigation-element-to-create-a-custom-navigation-bar)
  + - [Setup](#setup)
    - [Add a page header](#add-a-page-header)
    - [Add a navigation element to the header](#add-a-navigation-element-to-the-header)
    - [Hide the workbook page tabs](#hide-the-workbook-page-tabs)