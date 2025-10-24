# Introduction to the Dataset Worksheet

# Introduction to the Dataset Worksheet

Dataset worksheets allow you to structure and manipulate its data. You can create calculations, group data, apply filters and formats, add parameters, etc. A dataset’s worksheet must contain at least one data source. Examples of data sources include tables from your organization's data warehouse, uploaded CSVs, and even other datasets.

## Worksheet Tab Anatomy

![dataset-worksheet.png](https://files.readme.io/65ea8e1-dataset-worksheet.png)

### The Formula Bar

Each worksheet has a formula bar positioned near the top of the page.  
![20-dataset-worksheet-formula-bar.png](https://files.readme.io/fbb79de-20-dataset-worksheet-formula-bar.png)

Formulas are applied to columns, not cells. When a formula is applied to a column, it is applied to all rows in that column.

Every column has a formula, including those that directly reference data from your data source. To view a column’s formula, select the column and its formula will automatically appear in the formula bar.

To create a new calculation in your worksheet, you should first add a new column then add a formula to that column. Get started with some of Sigma's most [popular functions](/docs/popular-functions).

### The Right Side Panel

The panel on the right side of any worksheet has two components: the column view and the data source list.

#### The Column View Panel

The column view panel contains the full list of columns in the worksheet. Unless they are marked as hidden, these columns are all visible in the worksheet’s spreadsheet.   
![21-dataset-worksheet-right-bar.png](https://files.readme.io/9c74941-21-dataset-worksheet-right-bar.png)

From here, you can organize and group your worksheet’s columns into levels. As was mentioned in the spreadsheet section above, creating leveled groups allows you to bundle rows of data based on common characteristics in select columns. When you group your data from the column view panel, those groups will automatically be reflected in the worksheet spreadsheet.

This column view panel also contains a section for worksheet totals. Totals are single value column aggregates that live at the top most level or a worksheet.

#### The Data Source Panel

Click on the second tab in your worksheet’s right side panel to open the data sources panel. This panel displays the worksheet’s data source(s). From here you can edit and join data sources.

Each data source contains a list of its columns, so you may also add any missing data source columns to your worksheet from the sources dropdown column list.  
![22-dataset-right-datasource-tab.png](https://files.readme.io/9bc5ad9-22-dataset-right-datasource-tab.png)

#### The Control Panel

Worksheets have an expandable control panel on the left side of the screen. This contains worksheet filters and parameters. It also contains total values if any exist. ![23_-_dataset-worksheet-left-bar.png](https://files.readme.io/bef05d1-23_-_dataset-worksheet-left-bar.png)

Updated 3 days ago

---

Related resources

* [Dataset Worksheet Columns](/docs/dataset-worksheet-columns)
* [Dataset worksheet controls](/docs/dataset-worksheet-controls)

* [Table of Contents](#)
* + [Worksheet Tab Anatomy](#worksheet-tab-anatomy)
  + - [The Formula Bar](#the-formula-bar)
    - [The Right Side Panel](#the-right-side-panel)