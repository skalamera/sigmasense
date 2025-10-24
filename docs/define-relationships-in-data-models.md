# Define relationships in data models

# Define relationships in data models

You can add relationships between tables in a data model to enable business users to work with related data without performing ad hoc joins.

A relationship defines the join logic for Sigma to use to join the tables. After you define a relationship between two tables, the columns from both tables are available to the source table for analysis and exploration as needed. When a user analyzes the source table in a workbook and adds a related column, Sigma performs the join.

Relationships can help reduce unnecessary joins, which can improve performance and reduce cost. With a relationship, a join is only performed when a related column is added to a workbook element. If you use a join instead, the join is performed in the underlying SQL every time.

Sigma does not automatically create relationships between tables from a connected data source. Even if the tables have primary and foreign keys defined, you must create relationships between the tables in a data model to make the related columns available to downstream elements.

> 💡
>
> Relationships between elements are directional. Consider how your data is related when defining a relationship.

## Guidance for modeling relationships

Relationships between data model tables only support many-to-one or one-to-one joins. When you define a relationship between tables in a data model, use the most-granular data table as the source element and add a relationship to one or more less-granular tables as target elements. Each row in the source table must have only one possible result in the target table, otherwise unintentional fanouts or wrong results can be introduced to workbooks that use the related column.

For example, if you use a [star schema](https://en.wikipedia.org/wiki/Star_schema), use your fact table (for example, EVENTS) as the source element, and add a relationship with each dimension table (for example, USER, or EVENT\_TYPE) as the target element.

For more details, see [Relationships: what they are and how to use them](https://community.sigmacomputing.com/t/relationships-what-they-are-and-how-to-use-them/4332) in Sigma Community.

## Add a relationship between two data model tables

Define a relationship to make additional columns available from a data model element.

> 📘
>
> ### You can only define relationships between elements on the same connection. All related elements must be in the same data model.

1. Open the data model for editing.
2. [Add elements to the data model](/docs/create-and-manage-data-models).
3. Select **Data model ERD** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/data-model.svg)) to open the entity relationship diagram (ERD) view.
4. In the **Data model ERD** view, select the source element for the relationship on the canvas.
5. In the editor panel, select the **Modeling** tab. In the **Relationships** section, select **+** (**Add relationship**).

   ![Entity relationship diagram with one Trip element and one Stations element. A modeling overview provides options to add relationships, metrics, and column security to the element, and a details pane includes information about the connection, materialization status, and downstream elements.](https://files.readme.io/d9a1ec580897e1c8f8f0518c2ed7eebd0b765bf6d58b683db1fe5f7d625d9aa3-data-model-erd.png)

   The **Add a relationship** modal opens.

   ![Relationship modal, showing target element with join keys of Start station Id from the Trip table and Id from the Stations table, a name of Start Station details, and an empty description.](https://files.readme.io/931951e7fb7aea1c01e837b794b21e1af3f738c54a15c831221a78ea7a8d6529-dm-rel-add.png)
6. (Optional) Name the relationship. By default, the relationship name uses the target element title.
7. (Optional) Add a description for the relationship.
8. For **Target source**, select an element in the data model to add as a target of the relationship. Adding an element as a target makes its columns available from the source element.

   > 💡
   >
   > The target source can be an element disabled as a source. When the target source is disabled, the only way for downstream users to work with columns in that element is through this relationship.
9. For **Join keys**, select the columns from the source element and the target element to use as the join keys in the relationship.
10. (Optional) Click **+ Add another mapping** to add more column mappings.
11. (Optional) Review the key matching details for the source and target elements to validate that your relationship is set up on the correct keys. Select **Result preview** to confirm the output of the relationship looks as expected.
12. Click **Save**.
13. To make the relationship available to downstream users, publish the data model.

For details about using related columns in a workbook, see [Use related columns in a workbook](/docs/use-related-columns-in-a-workbook).

### Example relationship

For example, if you want to make the BIKES data in the Sigma Sample Database easier to analyze in a workbook, you can model and define a relationship as follows:

1. In your data model, using the Sigma Sample Database EXAMPLES.BIKES schema as a data source, add the TRIP table and the STATIONS table as two data elements.

   The TRIP table provides details about bike trips taken on rental bikes. There is one row for every bike trip, so there are many total rows for each station.

   The STATIONS table provides details about the location of each bike docking station. There is one row for each station.

   ![Data model entity relationship diagram, showing a TRIP table and a STATIONS table from the Sigma Sample Database](https://files.readme.io/d9a1ec580897e1c8f8f0518c2ed7eebd0b765bf6d58b683db1fe5f7d625d9aa3-data-model-erd.png)
2. To create a relationship between the two tables, start from the TRIP table, using the STATIONS table as the target element. Creating a relationship in this direction defines the logic for a many-to-one join:

   ![Data model relationship modal, showing a relationship definition that uses the stations table as the target element, with a column mapping of Start Station Id in the trip table to the Id column in the stations table.](https://files.readme.io/931951e7fb7aea1c01e837b794b21e1af3f738c54a15c831221a78ea7a8d6529-dm-rel-add.png)
3. Then, after publishing the data model, business analysts can work with the TRIP table from the data model, easily adding related columns from the STATIONS table. Sigma performs a join based on the logic defined in the relationship, and the join is only executed when the related columns are added to the workbook:

   ![Related columns available in a workbook from the Stations table, after the Trip table from the data model is added as a data source.](https://files.readme.io/f49529347bdc20fb584a935075ddf64c86fc4b3c62e586a36e59a97986a4c95d-use-related-columns.png)

## Review existing relationships for data model elements

You can use the entity relationship diagram (ERD) for your data model to review the relationships between data model elements.

* Identify directional relationships with the arrows connecting elements. Each relationship has a distinct arrow.
* Select an arrow to highlight the relationship and the relevant keys in the source and target elements.
* Identify which relationships are set up for which columns of the reusable elements.

  ![Data model entity relationship diagram for trip and stations elements, with two arrows from trips to stations to indicate two separate relationships, one for the start station ID and another for the end station ID, and the modeling panel open to provide configuration options for the selected element.](https://files.readme.io/363a358c6e585bc9605527404691685fbe330276589441087c35fe6c81c302f7-dm-erd-multiple.png)

![](https://files.readme.io/363a358c6e585bc9605527404691685fbe330276589441087c35fe6c81c302f7-dm-erd-multiple.png)

Updated 3 days ago

---

[Navigate data models](/docs/navigate-data-models)[Tutorial: Intro to data models](/docs/data-modeling-tutorial)

* [Table of Contents](#)
* + [Guidance for modeling relationships](#guidance-for-modeling-relationships)
  + [Add a relationship between two data model tables](#add-a-relationship-between-two-data-model-tables)
  + - [Example relationship](#example-relationship)
  + [Review existing relationships for data model elements](#review-existing-relationships-for-data-model-elements)