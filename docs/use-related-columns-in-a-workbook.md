# Use related columns in a workbook or data model

# Use related columns in a workbook or data model

If the data source of your data element in a workbook or data model is a [data model table with one or more relationships](/docs/define-relationships-in-data-models), you can add columns from the related tables to your data element. Any child elements that you create can also access the related columns.

> 💡
>
> ### You can use relationships created in a data model in the same data model if you first create a child table from the primary source element.

## Requirements

* The data source must be a table element in a data model with one or more relationships defined.
* You must be the workbook or data model owner or be granted **Can explore** or **Can edit** [access](/docs/folder-and-document-permissions) to the document.

## Add a related column to a data element

If the data source of your data element in a workbook or data model has one or more relationships defined, you can add the related column to your data element:

1. Customize the workbook or open the workbook or data model for editing.
2. Select the data element.
3. In the editor panel, for columns, select **+** (**Add columns...**).
4. In the menu, choose **Add source columns...** to open the **Source columns** list.

   ![Related columns available in a workbook from the Stations table, after the Trip table from the data model is added as a data source.](https://files.readme.io/910f668d28a67aa902675f0aa4737b87b63ffedcd92163fad0d59e67033d1bce-dm-rel-src-column.png)
5. Review the **Source columns** list for available columns from tables linked through data model relationships. You can see directly related table columns, as well as columns from inherited relationships.
6. Select the checkbox for a column to add it to your data element.

   The related column appears in your data element, titled *Column Name (Relationship Name)*.

## Use a related column in a formula

If the data source of your data element in a workbook has one or more relationships defined, you can also use the related column in the formula of a calculated column in the data element.

> 📘
>
> ### You do not need to add the related column to the data element before using it in a formula.

1. Explore the workbook or open the workbook for editing.
2. Select the data element. For example, a table of bike trips taken from one rental bike docking station to another, called **TRIP**.
3. In the element, or in the editor panel, select **+** (**Add column...**).
4. In the formula bar, enter a formula that references the related column. As you type, the related columns appear in the list of autocomplete suggestion:

   ![Formula bar with an If function, using autocomplete to identify the related columns, shown with a link icon and the title of the relationship, in this case, Start Station Details](https://files.readme.io/1d44a0ada1842a8cc8e9dec051b29abdf5ba111b054e0f8af7f41704a9eed352-dm-formula-auto.png)

   For example, to evaluate the availability of docking stations at the start station, you might write the following formula:

   ```
   If([TRIP/Start Station Details/Dock Count] > 15, "high availability", [TRIP/Start Station Details/Dock Count] = 15, "medium availability", [TRIP/Start Station Details/Dock Count] < 15, "low availability")
   ```

   The resulting table includes the calculated column, named *Start Station Dock Availability*:  
   ![Table with an Id, Duration, Start Date, Start Station Dock Availability, Start Station Name, Start Station Id, with several rows of trips. Most stations have high or medium dock availability. The Trip table in a data model is the source, and also the name of the workbook table element](https://files.readme.io/77a045d38b587c5fc1cbe87d3091c90854da8a75273a77a3bd02aee757d629a0-Screenshot_2025-03-26_at_5.45.43_PM.png)

Updated 3 days ago

---

[Create a data element](/docs/create-a-data-element)[Use linked columns in workbooks](/docs/use-linked-columns-in-workbooks)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Add a related column to a data element](#add-a-related-column-to-a-data-element)
  + [Use a related column in a formula](#use-a-related-column-in-a-formula)