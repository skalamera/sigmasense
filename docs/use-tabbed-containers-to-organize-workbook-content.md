# Use tabbed containers to organize workbook content

# Use tabbed containers to organize workbook content

Add a tabbed container to your workbook pages when you want to offer multiple sets of content in the same section of your workbook canvas. A tabbed container works just like a regular [container](/docs/organize-workbook-layouts-with-containers) when it comes to organizing, grouping, and managing workbook elements. In addition, a tabbed container has multiple tabs, which can either be visible at the top of the container or hidden for end users. By placing content on different tabs and configuring logic about which tab should display, you can allow users to experience different views in the same space without scrolling or navigating elsewhere.

Tabbed containers are a [layout element](/docs/intro-to-layout-elements), allowing you to guide users and create focused interfaces as you build [data apps](/docs/data-apps) in Sigma.

![Gif of a container with three tabs along the top, showing the mouse clicking between two of the tabs to change which one is displayed.](https://files.readme.io/6442096812dbd8759d6c58522c3091a2f26ab9ddf91e16d05f9a6c34146521ee-tab.gif)

Use tabbed containers when you want to:

* Show a chart and its underlying data in the same dashboard space.
* Show different charts based on the number of selected items in a control.
* Show a custom “No data” message for an empty element.
* Create a drill down that changes from one chart type to another.

To create several navigation options between different workbook pages, [Use the navigation element to guide user exploration](/docs/use-the-navigation-element-to-guide-user-exploration).

## Limitations

* Hiding individual tabs is not supported. You can show or hide the entire tab bar, but not individual tabs. If you hide the tab bar, the only way to display tabs other than the default tab is through the **Select tab** action. See [Create actions that modify or refresh elements](/docs/create-actions-that-modify-or-refresh-elements#select-tab-beta).
* When exporting from a workbook with a tabbed container, the export always renders the first tab, which is labeled as the default tab in the properties tab of the editor panel.
* When you nest containers or tabbed containers, you can only nest four levels deep. If you attempt to place a tabbed container or container inside another layout element that is already nested within three surrounding container or tabbed container elements, Sigma shows a "Cannot nest more than 4 levels of layouts" error.

## Prerequisites

* You must be the owner or have **Can edit** or **Can explore** permissions on the workbook.

## Add a tabbed container to a workbook

In edit or explore mode, follow these steps to add a tabbed container:

1. In the **Add element** bar, select **Layout** then select **Tabbed container**.

   An empty tabbed container appears. If you selected a container or tabbed container before adding the element, the new tabbed container is nested within that element. Otherwise, the tabbed container appears on the canvas.

> 💡
>
> ### To quickly size the container to match the width of other elements already on your canvas, select the element or element you want to match before adding the tabbed container.
>
> The tabbed container appears on your canvas near the elements you selected and matches their width.

## Customize a tabbed container

To customize the tab controls, container layout, and style, see the following sections:

* [Configure a tabbed container](#configure-a-tabbed-container)
* [Resize a tabbed container](#resize-a-tabbed-container)
* [Change the grid column density of a tabbed container](#change-the-grid-column-density-of-a-tabbed-container)
* [Style a tabbed container](#style-a-tabbed-container)

### Configure a tabbed container

When you first add a tabbed container to a workbook, it contains three empty tabs named Tab 1, Tab 2, and Tab 3.

To customize the configuration of your tabbed container, use the **Properties** tab of the editor panel:

* To rename your tabs, in the **Properties** tab, double-click on the default tab names. Or, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**, then click **Rename**.
* To reorder your tabs, click the drag handle to the left of the tab name in the **Properties** tab, then drag it to your preferred location in the list.

> 📘
>
> ### The first tab in your container is the default tab. The default tab is what displays when a user accesses your workbook in view or explore mode, unless you have configured logic to override this default. To configure specific tabs to open based on conditions or user actions, see [Create actions that modify or refresh elements](/docs/create-actions-that-modify-or-refresh-elements#select-tab).
>
> When exporting from a workbook with a tabbed container, the export always renders the default tab.

* To duplicate a tab and all of its contents, click![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**, then click **Duplicate**.
* To configure different tabs to display based on user actions, configure the **Select tab** action. See [Create actions that modify or refresh elements](/docs/create-actions-that-modify-or-refresh-elements#select-tab).

### Resize a tabbed container

By default, a tabbed container has a grid width of 12, which you can resize as needed. Drag the edges of a container to resize it.

* You cannot resize a container smaller than the elements inside of it.
* When you resize a container horizontally, the width of the grid spaces inside the container change and the elements inside the container are resized horizontally to fit.
* When you resize a container vertically, the number of vertical grid spaces inside the container changes but elements do not resize automatically.
* All tabs in a tabbed container share the same width and height. This means that if you add an element in one tab that takes up more vertical space than the elements on other tabs, the height of all tabs is affected.

### Change the grid column density of a tabbed container

A container has its own grid, similar to the grid on the canvas. By default, a container's grid has 12 horizontal grid spaces, or 12 "columns", which expand and contract to fit the container size. You can change this density in the **Properties** tab of the editor panel using the **Column density** setting.

> 💡
>
> ### High density means more (and narrower) columns, which allows more elements to fit side by side with finer control over their widths. Low density means fewer (and wider) columns, which prevents overcrowding and ensures visibility of element content when the browser window width is reduced.

* A container with **Low** column density has 6 grid columns.
* A container with **Medium** column density has 12 grid columns. This is the default density.
* A container with **High** column density has 24 grid columns. When dragged to the full width of the canvas, the grid within a container with high column density aligns with the full canvas grid.

### Style a tabbed container

In the editor panel, select the **Format** tab to style your container:

| Style | Details |
| --- | --- |
| **Spacing** | Specify the amount of space to include between elements in the container. If the tab bar is visible, the spacing setting also changes the amount of space between the top of the tabbed container and the tab bar. If padding is turned on, the spacing setting also determines the amount of padding. |
| **Padding** | Adds padding to the tabbed container. Selected by default. Deselect the checkbox to remove padding between the outside edges of elements and the container. |
| **Background color** | Select a background color for the tabbed container. |
| **Border** | Specify a border for the tabbed container. Defaults to none, but can be set to 1, 2, or 3 pixels. You can also choose a color for the border. |
| **Corner** | Choose a corner shape for the tabbed container. Choose between square, round, and pill. Defaults to round. |
| **Element gap** | Adds padding between elements in the tabbed container. Selected by default. Deselect the checkbox to remove padding between elements. |

Open the **Tab bar style** section to style the tab bar:

| Style | Details |
| --- | --- |
| **Show tab bar** | Turn off the toggle to hide the tab bar from end users in view mode and explore mode. By default, the tab bar is visible. If you hide the tab bar, the only way to display tabs other than the default tab is using the **Select tab** action. See [Create actions that modify or refresh elements](/docs/create-actions-that-modify-or-refresh-elements#select-tab) . |
| **Tab style** | Select **Open**, **Box**, or **Button**. The default style is **Open**. |
| **Alignment** | Select  **Left**, **Center**,  **End**, or **Justify** to specify how the tabs should be aligned in the tab bar. The default alignment is **Left**. |
| **Size** | Select a size for the tabs, **Small**, **Medium**, or **Large**. The default size is **Medium**. |

## Remove or delete a tabbed container

When you delete a tabbed container, you also delete all elements inside every tab of the tabbed container. To do so, select the tabbed container, then select **More** > **Delete element**. The tabbed container and all elements inside are deleted.

Updated 3 days ago

---

Related resources

* [Organize workbook layouts with containers](/docs/organize-workbook-layouts-with-containers)
* [Create actions that modify or refresh elements](/docs/create-actions-that-modify-or-refresh-elements)

* [Table of Contents](#)
* + [Limitations](#limitations)
  + [Prerequisites](#prerequisites)
  + [Add a tabbed container to a workbook](#add-a-tabbed-container-to-a-workbook)
  + [Customize a tabbed container](#customize-a-tabbed-container)
  + - [Configure a tabbed container](#configure-a-tabbed-container)
    - [Resize a tabbed container](#resize-a-tabbed-container)
    - [Change the grid column density of a tabbed container](#change-the-grid-column-density-of-a-tabbed-container)
    - [Style a tabbed container](#style-a-tabbed-container)
  + [Remove or delete a tabbed container](#remove-or-delete-a-tabbed-container)