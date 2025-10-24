# Use the navigation element to guide user exploration (Beta)

# Use the navigation element to guide user exploration (Beta)

> 🚩
>
> This documentation describes one or more public beta features that are in development. Beta features are subject to quick, iterative changes; therefore the current user experience in the Sigma service can differ from the information provided in this page.
>
> This page should not be considered official published documentation until Sigma removes this notice and the beta flag on the corresponding feature(s) in the Sigma service. For the full beta feature disclaimer, see [Beta features](/docs/sigma-product-releases#beta-features).

Add a navigation element to your workbook to display a list of destinations users can visit. The navigation element shows each destination as an individual button, which you can configure to send users to a workbook page, workbook element, or external link when clicked. Submenus allow you to nest additional navigation options under a top-level option.

The navigation element is a [layout element](/docs/intro-to-layout-elements), allowing you to guide users and create focused interfaces as you build [data apps](/docs/data-apps) in Sigma.

![Image of a navigation bar in a page header. A user clicks several options to navigate the workbook](https://files.readme.io/cf7668332677ff45cf7711b7c381f489e21f7db93e94bd2df6c8c76e7c053fd4-Nav_demonstration.gif)

Use a navigation element when you want to:

* Provide a list of destinations for users to explore.
* Hide the native workbook page navigation.
* Link to workbook pages and external links in the same list of options.

To create a container with several tabs of content on a single workbook page, [Use tabbed containers to organize workbook content](/docs/use-tabbed-containers-to-organize-workbook-content).

To create a static page header that is shared by multiple pages, see [Add custom page headers to a workbook](/docs/add-custom-page-headers-to-a-workbook).

## User requirements

The ability to create and customize a navigation element requires the following:

* You must be assigned an account type with the **Create, edit, and publish workbooks** permission enabled.
* You must be the workbook owner or be granted **Can edit** access to the workbook.

## Create a navigation element

Add a navigation element to your workbook:

1. Open a workbook draft.
2. In the **Add element** bar, select **Layout**, then select **Navigation**.

![The Add elements bar with the Layout > Navigation option highlighted for selection](https://files.readme.io/ff9f21f80eddd3fb359a50e4e02afc2f8bfee711c3f756a7e8e525543ea97b81-Add_Navigation.png)

By default, the navigation element populates in **Auto** mode, listing the current workbook pages as the destination options. For example, if your workbook has pages titled Sales - East, Sales - West, and Raw Data, those three pages appear as options when you create a navigation element. For more information on customizing destination options, see [Set manual navigation options](#set-manual-navigation-options).

## Customize a navigation element

To customize the content or style of a navigation element, see the following sections:

* [Set automatic navigation options](#set-automatic-navigation-options)
* [Set manual navigation options](#set-manual-navigation-options)
* [Style a navigation element](#style-a-navigation-element)
* [Create a nested submenu of navigation options](#create-a-nested-submenu-of-navigation-options)

### Set automatic navigation options

You can set navigation options to automatically match the current workbook pages:

1. Select the navigation element.
2. In the editor panel, select **Properties**.
3. Select **Auto**.

In **Auto** mode, the navigation element lists all current workbook pages as navigation options. Changes to the workbook pages (new pages, renamed pages, deleted pages) automatically appear in the navigation element. Hidden pages do not appear as navigation options.

> 💡
>
> Any customization requires you to convert the navigation element to manual mode. See [Set manual navigation options](#set-manual-navigation-options).

### Set manual navigation options

You can manually set a list of navigation options including custom destinations, names, and nesting.

Set a navigation element to manual:

1. Select the navigation element.
2. In the editor panel, select **Properties**.
3. Select **Manual**.

> 📘
>
> Setting a navigation element to **Manual** stops automatic updates from changes to workbook pages. This allows you to set the navigation options independent of the current workbook pages.

To add a new navigation option:

1. Select the navigation element.
2. In the editor panel, select **Properties**.
3. Select **Manual**.
4. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg) **Add an option** and select an option from the menu:

|  |  |
| --- | --- |
| **Submenu title** | Add a title with nested navigation options in a submenu. The submenu title itself is not a navigation option. |
| **Main page** | Add an option that navigates to a selected workbook page. |
| **Page anchor** | Add an option with a navigation action and no specified destination. Configure the destination to navigate to any workbook page or element. |
| **Link** | Add an option that navigates to an external link. Configure a static or dynamic link URL, and select whether the link opens in a new window, the current window, or the parent window. |

Edit a navigation option:

1. Select the navigation element.
2. In the editor panel, select **Properties**.
3. Select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **Options** for the navigation option you want to edit and select an option from the menu:

|  |  |
| --- | --- |
| **Edit destination** | Change the destination for the navigation option. |
| **Rename** | Change the name of the navigation option. |
| **Duplicate** | Duplicate the navigation option. |
| **Delete** | Delete the navigation option. |
| **Move to** | Move the option to another location in the navigation element. Selecting an existing option transforms that options into a submenu title. The option you moved appears under that submenu title. |

### Style a navigation element

You can configure the padding, background color, and corner style for a navigation element:

1. Select the navigation element.
2. In the editor panel, select **Format**.
3. Expand the **Element style** section to view the style settings.
4. Configure the style settings:

|  |  |
| --- | --- |
| **Padding** | On by default. Enable or disable the space between the border of the navigation element and its contents. |
| **Background color** | Select the color displayed behind the contents of the navigation element. |
| **Corner** | Select whether to have square, round, or pill-shaped corners for the navigation element. |

You can configure the corner style, orientation, alignment, and size of the options in a navigation element:

1. Select the navigation element.
2. In the editor panel, select **Format**.
3. Expand the **Option style** section to view the style settings.
4. Configure the style settings:

|  |  |
| --- | --- |
| **Corner** | Select whether to have square or pill-shaped corners for the navigation element. |
| **Orientation** | Select whether to display the navigation options horizontally or vertically. |
| **Alignment** | Select whether to left align, center align, right align, or stretch the navigation options. |
| **Size** | Select whether the navigation options are small, medium, or large. |

### Create a nested submenu of navigation options

In a manual navigation element, you can configure a nested submenu of navigation options.

![An open navigation submenu titled Teams shows options for Marketing, Engineering, and People](https://files.readme.io/a7867e561794ed401b8749f96ef30795d71f62338af03aefa109ae3340cd7ae4-Open_nested_submenu.png)

1. Select the navigation element.
2. In the editor panel, select **Properties**.
3. Select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **Options** for the navigation option you want to add to the submenu.
4. Select **Move to**.
5. Select an existing submenu or create a new one by selecting another navigation option.
6. Repeat steps 3-5 for each navigation option you want to add to the submenu.

Alternatively, you can drag and drop a navigation option under another navigation option in the editor panel to create a submenu.

![A navigation option is dragged and dropped under another navigation option to create a submenu.](https://files.readme.io/346c274abcc23d43242af63be694f2992acf84a6803aa05d1092dc91b1eb0f1e-Submenu_drag_and_drop_example.gif)
> 📘
>
> The title of a submenu is not a navigation option. Sigma recommends creating an empty navigation option to move other options into.

## Delete a navigation element

You can delete a navigation element directly from the workbook page:

1. Select the navigation element.
2. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**.
3. Select **Delete element**.

## Hide page tabs in view mode

You can hide the workbook page tabs from users in view mode, allowing you to set a navigation element as the primary navigation for your workbook.

To hide the workbook page tabs in view mode:

1. Select the workbook page.
2. In the editor panel, under **Settings**, select **Workbook settings**.
3. Open the **Layout settings**.
4. In the **Layout settings** section, check the box next to **Hide page tabs in view mode**.
5. In the confirmation modal, click **Confirm**.

> 🚩
>
> After hiding the page tabs, users won’t be able to change pages without a navigation element or navigate action. Consider this user experience before hiding the page tabs.

Updated 3 days ago

---

[Use popovers to simplify a workbook interface](/docs/use-popovers-to-simplify-a-workbook-interface)[Add logic and interactivity](/docs/add-logic-and-interactivity)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Create a navigation element](#create-a-navigation-element)
  + [Customize a navigation element](#customize-a-navigation-element)
  + - [Set automatic navigation options](#set-automatic-navigation-options)
    - [Set manual navigation options](#set-manual-navigation-options)
    - [Style a navigation element](#style-a-navigation-element)
    - [Create a nested submenu of navigation options](#create-a-nested-submenu-of-navigation-options)
  + [Delete a navigation element](#delete-a-navigation-element)
  + [Hide page tabs in view mode](#hide-page-tabs-in-view-mode)