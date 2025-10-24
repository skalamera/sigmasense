# View workbook and data model data lineage

# View workbook and data model data lineage

Data lineage refers to the ancestry and relationships between data elements in a workbook or data model. All workbooks and data models contain a *lineage graph*, allowing you to review and navigate the relationships and dependencies in the document.

Some use cases for data lineage include:

* Determining how changes to a data element might affect any child elements
* Determining the source of unexpected data
* Cleaning up existing workbooks to remove unused or redundant elements
* Diagnosing the source of data and/or permission errors
* Identifying dependencies for materialization schedules

This document describes how to view and navigate the data lineage for a workbook or data model.

## Requirements

* To view data lineage, you must have **Can Edit** [access](/docs/folder-and-document-permissions) to the workbook or data model.

## View data lineage for a workbook or data model

1. Open the document for editing by clicking **Edit** in the document header.
2. Select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/document-lineage.svg) (**Lineage**) to open the data lineage for the workbook or data model.

> 💡
>
> ### You can also open lineage from the element toolbar of a specific element.
>
> 1. In the element toolbar, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**.
> 2. In the menu, select **View lineage**.
>
> The data lineage for the document opens with the element highlighted.

![Data lineage graph showing an EVENTS data model from the warehouse and specific data elements in the workbook across several pages. All pages show in one lineage graph, with several parent and child elements depending on the one data model table.](https://files.readme.io/4e6263a321dba70c1a28becc8f5b4a38a4cdb5e7d7c386e6584834e9ffaa8a57-lineage-base.png)

On the data lineage graph, you can do any of the following:

* Zoom in and out using the **+** and **-** options.
* Fit the lineage graph to your browser window view.
* Select the **Show controls** checkbox to show or hide control elements.
* Move around the graph using your cursor to grab and drag.
* Reorganize elements in the graph by clicking and dragging. Any changes you make to element position are reset when you close the data lineage.
* [Focus your lineage view on a specific element or page](#focus-your-lineage-view-on-a-specific-element-or-page) .
* [Open an element from data lineage](#open-an-element-from-data-lineage) .

## Focus your lineage view on a specific element or page

**Before you start:** This action is only available in edit mode. To start editing, click **Edit** in the document header.

1. Select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/document-lineage.svg) (**Lineage**) to open the data lineage for the workbook or data model.
2. At the top of the graph, search for elements or open the dropdown menu to choose a specific page in the workbook or data model.
3. Select a page from the menu to show elements only from that page.

![The same data lineage graph filtered to show elements only from page three, including upstream dependencies on other pages.](https://files.readme.io/173c83678fda2017a278658b0555c59c004a510f28adc83f9481e5a7f98d2c10-lineage-page.png)

## Open an element from data lineage

**Before you start:** This action is only available in edit mode. To start editing, click **Edit** in the document header.

1. Select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/document-lineage.svg) (**Lineage**) to open the data lineage for the workbook or data model.
2. Select an element in the lineage graph.
3. In the element details, select **View element**.

![Data lineage graph with one element, Organic Traffic by Country selected and highlighted on the graph. A detail pane shows the title, connection, data refresh details, a link to open query details, and the option to focus the element on the graph and view the element in the workbook.](https://files.readme.io/57133d1b958dfcfca63a0bb416a0c98d4148aae092bbd8b98c6bade42fe6709e-lineage-highlight.png)

Updated 3 days ago

---

Related resources

* [Intro to data elements](/docs/intro-to-data-elements)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [View data lineage for a workbook or data model](#view-data-lineage-for-a-workbook-or-data-model)
  + [Focus your lineage view on a specific element or page](#focus-your-lineage-view-on-a-specific-element-or-page)
  + [Open an element from data lineage](#open-an-element-from-data-lineage)