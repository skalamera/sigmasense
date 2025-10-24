# Use linked columns in workbooks

# Use linked columns in workbooks

If a [dataset has links](/docs/dataset-links), you can use the linked columns when analyzing and exploring data in a workbook.

## User requirements

To use linked columns in workbooks, you must be the workbook owner or be granted **Can explore** or **Can edit** [workbook permission](/docs/folder-and-document-permissions).

# Use linked columns in workbooks

*Links* are column-based relationships created between two data sources in Sigma. They allow you to access data from one data source based on a column it shares with another data source.

Cloud Data Warehouse (CDW) tables can be linked to other CDW tables. Sigma [datasets](/docs/data-modeling-with-datasets) can be linked to other datasets. And CDW tables can be linked to datasets. A data source can have links to multiple other data sources.

![](https://files.readme.io/20a1aa7-1.png)

## Link accessibility in workbooks

Links can only be accessed in workbooks through [data elements](/docs/intro-to-data-elements) created directly from a data source containing a linked column. Child elements of a data element that inherited links from its CDW or dataset parent will not continue to inherit those links.

This means that if you want to access linked columns from a data element, you should either (1) create that element from the original data source containing the link OR (2) [add the columns you want](/docs/use-linked-columns-in-workbooks) to the parent element so they can be directly inherited by the child.

## Add columns from a link in a table element

Linked columns in [tables](/docs/create-and-manage-tables) can be identified by the light blue background on their cell values.

1. Click on a cell in the linked column to open the link popup.
2. Check the box beside any column(s) you wish to display in your table.  
   ![Screen_Shot_2022-02-02_at_5.43.25_PM.png](https://files.readme.io/4f8e124-2.png)

## Add columns from a link in a visualization or pivot table

Linked columns in [visualizations](/docs/intro-to-visualizations) and [pivot tables](/docs/working-with-pivot-tables) are only accessible when an element is [maximized](/docs/intro-to-data-elements). From there, you can access links through the underlying data table. Like in table elements, linked columns can be identified by the blue background on their cells' values.

1. [Maximize the element.](/docs/maximize-or-minimize-a-data-element)
2. In the underlying data table, click any cell in the linked column.  
   This will open the link popup.
3. Check the box beside any column(s) you want to display in your table.  
   ![Screen_Shot_2022-02-02_at_5.48.55_PM.png](https://files.readme.io/6a93b12-3.png)

Updated 3 days ago

---

Related resources

* [Intro to data elements](/docs/intro-to-data-elements)
* [Create a data element](/docs/create-a-data-element)

* [Table of Contents](#)
* + - [User requirements](#user-requirements)
  + [Use linked columns in workbooks](#use-linked-columns-in-workbooks)
  + - [Link accessibility in workbooks](#link-accessibility-in-workbooks)
    - [Add columns from a link in a table element](#add-columns-from-a-link-in-a-table-element)
    - [Add columns from a link in a visualization or pivot table](#add-columns-from-a-link-in-a-visualization-or-pivot-table)