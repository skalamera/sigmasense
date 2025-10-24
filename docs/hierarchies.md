# Hierarchies (Beta)

# Hierarchies (Beta)

> 🚩
>
> This documentation describes one or more public beta features that are in development. Beta features are subject to quick, iterative changes; therefore the current user experience in the Sigma service can differ from the information provided in this page.
>
> This page should not be considered official published documentation until Sigma removes this notice and the beta flag on the corresponding feature(s) in the Sigma service. For the full beta feature disclaimer, see [Beta features](/docs/sigma-product-releases#beta-features).

Use hierarchies to group columns categorically and define the order of data granularity.

Common hierarchy examples:

* Product: type, family, name
* Location: continent, country, region, state, city
* Time: year, month, week, day
* Taxonomy: kingdom, phylum, class, order, family, genus, species

> 📘
>
> ### Hierarchies can be defined in tables, pivot tables, and visualization elements, but they can only be applied to pivot tables.

## Create a hierarchy

The following steps explain how to create a hierarchy.

1. Open a workbook in **Edit** mode.

   ![editing option](https://files.readme.io/4eb734d-1.png)
2. Select the element for which you want to create a hierarchy. You can create a hierarchy in a table or in a pivot table, but note that you can only use hierarchies in pivot tables.
3. In the **Columns** menu, click the **+** icon, and choose **Manage hierarchies**.

   ![How to get to Manage hierarchies interface](https://files.readme.io/5b313e0-2.png)
4. In the **Manage hierarchies** modal, click **+ New hierarchy** and define hierarchy properties:

   1. In the **Hierarchy name** field, enter a name to identify the hierarchy.
   2. In the **Columns in hierarchy** section, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add column** to add a column to the hierarchy.

   ![](https://files.readme.io/80bc313-4.png)

   When you add a column to a hierarchy, this column is labeled with a ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/img/icon-hierarchy.svg) hierarchy icon in the workbook's **Columns** menu. Hover over the icon to view the hierarchy details.

   ![Columns tagged as part of a hierarchy](https://files.readme.io/ddee60f-5.png)
5. To create additional hierarchies, click **+ New hierarchy** in the **Manage hierarchies** modal, then repeat step 4.

   ![](https://files.readme.io/2fb3281-6.png)

## Manage a hierarchy

You can rename a hierarchy, reorder columns, add new columns, remove existing columns, or delete a hierarchy altogether.

1. In the **Manage hierarchies** modal, select the hierarchy you want to update.
2. To rename the hierarchy, edit the **Hierarchy name** field.
3. To reorder columns, go to the **Columns in hierarchy** section, then drag and drop column names as needed.
4. To add a new column, go to the **Columns in hierarchy** section and click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add column**.

   ![Add a column to an existing hierarchy](https://files.readme.io/e0b38f8-7.png)
5. To remove a column from the hierarchy, locate the column name in the **Columns in hierarchy** section and click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/square_close.svg) **Remove column**.

   ![Remove a column from a hierarchy](https://files.readme.io/8f144c9-8.png)
6. To delete the hierarchy, locate the hierarchy name in the left panel and click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/square_close.svg) **Delete hierarchy**.

   ![Delete a hierarchy](https://files.readme.io/90fdbbd-9.png)

## Hierarchy inheritance

Child elements inherit all hierarchies defined in a parent element. Inherited hierarchies cannot be removed or modified from child elements, but new hierarchies can be added with full editing privileges.

When a hierarchy is selected in the **Manage hierarchies** modal, Sigma indicates if it's inherited from the parent element.

![](https://files.readme.io/746220c-10.png)

## Using hierarchies

The following steps explain how to use defined hierarchies in pivot tables.

1. To create a pivot row with hierarchies, go to the **Pivot Rows** property and click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add new column**.
2. In the **Add new column** menu, select a defined hierarchy.

   ![Defining a pivot row through a hierarchy](https://files.readme.io/ac7bab6-12.png)
3. To apply a hierarchy to the pivot values, go to the Values property and click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add new column**.
4. In the **Add new column** menu, select a defined hierarchy.

   ![Defining the values of a pivot table through a hierarchy](https://files.readme.io/d6a3910-13.png)

   The resulting pivot table demonstrates the configured hierarchies.

   ![Pivot table with hierarchies](https://files.readme.io/7bc59d0-14.png)

## Limitations

* Hierarchies can only be used in pivot tables.
* Hierarchies exist in singular workbooks and cannot be not passed to datasets or other workbooks.
* When you update a hierarchy, Sigma does not apply those changes to pivot tables that currently use it.

Updated 3 days ago

---

[Format pivot table totals](/docs/format-pivot-table-totals)[Transpose a table](/docs/transpose-a-table)

* [Table of Contents](#)
* + [Create a hierarchy](#create-a-hierarchy)
  + [Manage a hierarchy](#manage-a-hierarchy)
  + [Hierarchy inheritance](#hierarchy-inheritance)
  + [Using hierarchies](#using-hierarchies)
  + [Limitations](#limitations)