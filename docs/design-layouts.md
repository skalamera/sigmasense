# Intro to layout elements

# Intro to layout elements

Layout elements are dynamic workbook elements that separate, group, and manage the visibility of other workbook elements. They allow you to design user-friendly layouts and build intuitive workflows for a wide variety of use cases.

Use layout elements to organize existing elements on a single page, or combine them with [actions](/docs/intro-to-actions) to hide and display multiple layers of content across pages, tabs, and pop-ups.

This document introduces the fundamentals of layout elements such as functionality, types, and use cases.

## Layout element functionality

Layout elements allow you to do the following:

* Group elements together
* Separate unrelated elements on the same page
* Style elements as a group
* Direct user attention
* Manage access to workbook pages and elements
* Manage user workflows for data entry
* Reduce visual clutter from multiple filters and controls

## Types of layout elements

Sigma offers the following types of layout elements:

* [Containers](#containers)
* [Tabbed containers](#tabbed-containers)
* [Modals](#modals)
* [Popovers](#popovers)
* [Navigation](#navigation-beta)

### Containers

[Containers](/docs/organize-workbook-layouts-with-containers) are customizable elements that can group several elements on a page. You can place a container around existing elements, or you can move individual elements in and out as needed. They allow you to manage a page’s layout and to style elements as a group.

### Tabbed containers

[Tabbed containers](/docs/create-and-configure-tabbed-containers) are used to group elements like a standard container, but they also offer the ability to move between multiple tabs of content. You can navigate between the tabs using the provided controls, or you can hide the controls and use actions to move between tabs.

### Modals

[Modals](/docs/add-a-modal-to-a-workbook) are page-like elements that are displayed as an overlay on your workbook. You can configure a modal to be opened or closed by an action, overlaying the current page and directing the user to interact with the modal’s contents.

### Popovers

[Popovers](/docs/create-and-customize-popovers) are smaller layout elements that are anchored to a trigger button. You can group multiple filters or controls inside a popover, reducing visual clutter.

Popovers are similar to modals, but differ in two key ways:

* Popovers are always anchored to a trigger button
* Popovers are less disruptive to user attention, as they do not obscure the current page

### Navigation (Beta)

The [navigation](/docs/use-the-navigation-element-to-guide-user-exploration) element allows you to display a list of destinations for users to explore in the style of a navigation bar or panel. You can configure the navigation element to show each destination as an individual button, which you can configure to send users to a workbook page, workbook element, or external link when clicked.

## Example use cases

Each layout element serves a specific purpose when adding interactivity to a workbook. Containers, for example, are excellent for organizing a single page of content. But, if you were struggling to fit many elements on a page, a container wouldn't help as much as a tabbed container or modal. This is because tabbed containers and models both create new workbook space where you can place elements, and containers do not.

Consider the following use case examples as you decide which layout element suits your needs.

### Separate metrics on a dashboard with containers

Containers allow you to group elements together on a page. When using one workbook page to display two separate metrics, you can group the elements associated with each metric into their own container.

By creating a visual division between the elements and applying styles like a background color to each container, you can make it obvious to users which elements are referencing each metric at first glance.

In this example, KPIs and charts for profit and order volume are separated into their own containers.

![A screenshot of a business intelligence dashboard in Sigma. On the left, a charts and KPIs about profit are grouped in an orange container. On the right, charts and KPIs about order volume are grouped in a blue container.](https://files.readme.io/082f294262e8b127417b10513c824960a0b3472486c95dbfbbae02423c2d29eb-Containers_Example_Final.png)

### Handle multiple user inputs with a modal

Modals allow you to obscure the current page, and supply a new set of contents for users to interact with. When using a data app to capture user inputs, you can use a modal to direct their attention towards required inputs. By configuring an Open Modal action on a button click, you can further streamline user interaction with your data app.

In this example, a Project Tracker data app allows end users to enter information about new projects. The Create Project button is configured to open a modal where they can enter the required information, and then click insert a new row based on the information they entered in the modal.

![A gif of a screen recording that shows a user navigating a modal in Sigma. They open the modal with a button, make several selections in the modal, and then create a new row in a data table based on their entries before closing the modal.](https://files.readme.io/6be527ace86ea15d9ee55b8670884e1c92b73fa074ffae67a1a0a08d772cb6a7-Modals_Example_FInal.gif)

Updated 3 days ago

---

[Add system-generated columns to input tables](/docs/add-system-generated-columns-to-input-tables)[Use containers to organize workbook layouts](/docs/use-containers-to-organize-workbook-layouts)

* [Table of Contents](#)
* + [Layout element functionality](#layout-element-functionality)
  + [Types of layout elements](#types-of-layout-elements)
  + - [Containers](#containers)
    - [Tabbed containers](#tabbed-containers)
    - [Modals](#modals)
    - [Popovers](#popovers)
    - [Navigation (Beta)](#navigation-beta)
  + [Example use cases](#example-use-cases)
  + - [Separate metrics on a dashboard with containers](#separate-metrics-on-a-dashboard-with-containers)
    - [Handle multiple user inputs with a modal](#handle-multiple-user-inputs-with-a-modal)