# Join data in workbooks

# Join data in workbooks

Joins combine data from multiple sources based on matching columns.

This article covers how to create joins in workbooks, for example, so that you can combine data from multiple sources in a single data element.

For details on joins and guidance choosing the join type you want to use to combine data, see [Join types](/docs/join-types).

## Join data sources

**Before you start:** This action is only available in edit mode. To begin editing, click **Edit** in the top right corner of the page.

1. Select ![Add element](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) to open the workbook's **ADD NEW ELEMENT** panel.
2. Under **DATA ELEMENTS**, select the type of element you want to add: **TABLE**, **VIZ**, or **PIVOT TABLE**.
3. Select **Join** or **Union** to combine data sources.
4. In the **Select source** dialog that appears, search for a data source or current workbook element, or browse to a workbook element, table, or dataset.
5. Select a data source to preview and choose the columns to select, then click **Select**.  
   The **Create Join** page opens.
6. Joins require two or more sources.  
   To add a second source, next to **SOURCES**, click **+**.  
   ![Image of the Create Join page, with the + icon highlighted.](https://files.readme.io/c0a772e-5.png)
7. Repeat steps 4 & 5.
8. Select a **Join type**.  
   ![Image of the join type drop-down menu open and highlighted, showing options of Left Outer Join, Inner JOin, Right Outer Join, and Full Outer Join.](https://files.readme.io/8b2acdd-6.png)
9. Select the **Join keys** to use. On the right side of the page, you see the match rates for your selected join keys.

   ![Image of the Create Join page with the join keys section highlighted, showing the Product Key field selected as the join keys for the two selected data sources](https://files.readme.io/2b9c70e-7.png)

   > 📘
   >
   > ### In some cases, you might want to define multiple pairs of join keys, such as with a [full outer join](/docs/full-outer-join).
10. [optional] To join an another source, repeat steps 6 – 9.
11. Select **Preview output**.
12. Review the preview of the joined data sources and make any changes to included columns.  
    ![Preview of the two combined data sources, with a flowchart depicting the flow of data from each source into a final output that is a left join, and a full table listing all data columns from both sources, using color to distinguish which columns came from which source data.](https://files.readme.io/b7462c7-9.png)
13. Select **Done**.  
    Your new element appears in the workbook.

Updated 3 days ago

---

[Join data in datasets](/docs/join-data-in-datasets)[Transform data](/docs/transformations)

* [Table of Contents](#)
* + [Join data sources](#join-data-sources)