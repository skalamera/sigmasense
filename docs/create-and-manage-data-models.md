# Create and manage data models

# Create and manage data models

Build a data model to create a collection of table and input table elements that you can reference as data sources in workbooks and other data models across your organization. The familiar workbook-style format allows you to easily transform and analyze your data while streamlining data model permissions.

This document explains how to create and manage data models. For information about data model concepts, see [Get started with data modeling](/docs/get-started-with-data-modeling).

After you create your data model, you can customize it and extend the functionality further to enable analysts and business users:

* [Pass values from a workbook to a data model using a parameter](/docs/create-and-manage-a-control-element#pass-a-value-from-a-workbook-control-to-a-data-model-control)
* [Define relationships in data models](/docs/define-relationships-in-data-models)
* [Create and manage metrics](/docs/create-and-manage-metrics)
* [Configure column-level security](/docs/column-level-security)

> 📘
>
> ### Sigma will continue to support the previous datasets version (legacy datasets) until data models are fully developed and can facilitate a seamless transition. For information about legacy datasets, see [Create and manage datasets](/docs/create-and-manage-datasets).

## User requirements

The ability to create or manage a data model requires the following:

* You must be assigned an [account type](/docs/user-account-types) with the **Create, edit, and publish datasets** permissions enabled.
* You must be the data model owner or be granted **Can edit** [access](/docs/folder-and-document-permissions) to the data model.

## Create a data model with reusable elements

To create a data model, do the following:

1. Go to your **Home** page.
2. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Create New** and select **Data Model** from the menu.

   ![Create new dropdown showing Data Model in the list of options](https://files.readme.io/7136646-image.png)
3. A new data model opens to the [workbook page](/docs/navigate-data-models#data-model-workbook-page). Use one of the following methods to add data:

   * In the **Add element** bar, select a **Data > Table** or **Input**, then choose an input table element.

     If you select a table or a linked input table, choose the element’s data source. The data source can be data from your data platform, a CSV upload, custom SQL, or an existing element from any data model.

     > 📘
     >
     > ### Future data-level changes applied to the source can be reflected in the data model. Some changes, like filters, are automatically inherited. For other changes, like added or removed columns, Sigma displays a prompt when you reopen the data model workbook page. For those other changes, you can follow the prompt to either ignore the changes or update the reusable element. Display-level changes, like hidden columns or column groupings, are not inherited.
   * Copy and paste a table or input table element from an existing workbook or data model. For more information, see [Copy and paste elements](/docs/copy-and-paste-elements).

     > 📘
     >
     > ### Reusable elements created from copy/paste are not synced with the original copied element and do not reflect future changes applied to the original element.
4. [optional] Create additional reusable elements and transform the data as needed. You can group columns, aggregate values, create child elements, add control elements, and more, just like in a workbook.
5. To save the new reusable elements, click **Publish**.

   When the data model saves successfully, the [overview page](/docs/navigate-data-models#data-model-overview-page) opens. You can then preview each reusable element and [continue managing the data model](#manage-an-existing-data-model).

### Create a data model from a workbook table

You can also create a data model from a table in a workbook. For example, if you uploaded a CSV-formatted file to a workbook directly and now want to reuse the data from the file in another workbook, you can create a data model from the table element with the CSV-formatted file as a data source.

1. Open the workbook that has the table element you want to convert to a data model.
2. Right-click on the element, or hover over the element and click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**.
3. Select **Advanced options > Create data model...**.
4. In the **Create data model** modal that appears, click **Next**.
5. In the **Add to a new data model** modal, type a name for the data model and choose a destination location to organize the data model.
6. Click **Create**. The data model opens in a new tab.

## Map changed columns in a data model

When you make some changes to columns in a data model element, downstream elements such as workbooks and other data models, might display errors like the following: `Unknown column [columnID]`, `Column [ColumnID] does not exist`, or `Reference to errored column: [columnID]`. Some example changes include:

* Deleting a column from a table.
* Deleting a column from a table, then adding it back from the list of source columns.
* Change the source of an element, such as from a joined table to a new table.

To prevent these errors from appearing in data models or workbooks that use a data model element as a source, Sigma detects these changes and prompts you to map changed columns when you publish the data model.

To map changed columns, do the following:

1. While editing a data model, make a change to a table that could cause errors in downstream elements.
2. Publish the data model.

   The **Map columns** modal appears.
3. Review the changed columns for the affected table and optionally map the changed column in the published version of the data model to a replacement column in the to-be-published draft of your data model. By default, changed columns are mapped to **No match**, which causes the column to error in downstream elements.

   For example, if you have a complex calculated column called *Normalized Price* that you want to update, add a new column called *Revised Normalized Price* with the updated calculation logic and delete the previous column. When you publish the data model, map the *Normalized Price* column to the *Revised Normalized Price* column.

   ![Map columns modal with the No matches toggle turned on and showing the Normalized Price column mapped to No match, but the drop-down menu is open and showing the column Revised Normalized Price available to map.](https://files.readme.io/a91064fd63760e4f08980e6516c4d78fe7d830422f708dea0e2a6ba224b5483e-map-successful.png)

   To remove the *Normalized Price* column from the data model without mapping it to a replacement column, leave the default selection of **No match**.
4. After you finish mapping all relevant columns for all affected tables, select **Save and publish**.

### Troubleshooting: Unable to select column

If you want to map a changed column to another column, but it is not available to select, do the following:

1. In the **Map columns** modal, turn off the **No matches** toggle.
2. Map the new column to **No match**, then map the deleted column to the new column.

   For example, map *Revised Normalized Price* to *No match*, then map the deleted column *Normalized Price* to the replacement column *Revised Normalized Price*.

![Map columns modal with the No matches toggle turned off and the Normalized Price column mapped to Revised Normalized Price column and the Revised Normalized Price column mapped to No match.](https://files.readme.io/e2f2f80ee38232b0fe4f2722e83f64b35604cef95be801681bb4fde9f21800ca-map-success.png)
> 🚩
>
> ### Any column mapped to **No match** can result in a column error in data models and workbooks that use this table as a data source.

### Troubleshooting: Column is not listed

If the changed column that you want to map is not listed in the **Map columns** modal, the data model was previously published without mapping the column.

If you want to map an already published column to a different column, you must restore the draft of your data model to an earlier version and republish, then re-map the column.

For example, if you deleted the *Normalized Price* column and published the data model. When you published the data model, you mapped the column to **No match**.

Later, you create the *Revised Normalized Price* column and want to map the *Normalized Price* column to the new column, but it isn't available to map.

![Map columns modal that does not show the Normalized Price column at all, instead showing a deleted column Sku Number mapped to No match, and other published columns Revised Normalized Price, Price, and Date mapped to themselves.](https://files.readme.io/284e9658b7ceb71daee34e48d71bde6d678509bc09f06fc3f20391c475ab5cc9-map-ohno.png)

In this example, you must restore your data model to the version of the data model before you deleted the *Normalized Price* column to draft, then add the new column and delete the previous column without publishing in between the changes. Then when you publish the draft, the **Map columns** modal appears, allowing you to map *Normalized Price* to *Revised Normalized Price*.

For more details about restoring a previous version of a data model as a draft, see [Document versions and version history](/docs/workbook-versions-and-version-history).

## Manage an existing data model

You can make changes to data model metadata, share a data model with others, or make changes to the data sources in the data model. You can also delete data models and recover deleted data models.

### Edit a data model's name

Choose a unique name to make it easy for members to search for and identify the data model.

1. Open the data model you want to edit.
2. In the data model header, select the document name and choose **File > Rename**.

   The document name becomes editable.
3. Rename the data model, then press `Enter` or click anywhere to apply the change.
4. Publish the data model to make the name change available downstream.

### Edit a data model’s description

Enter a description to add context to the data model and its elements.

1. Open the data model.
2. On the [overview page](/docs/navigate-data-models#data-model-overview-page), in the **About the data model** section of the sidebar, click the description field and update the text. Sigma immediately applies the change.

### Share the data model

Share a data model to allow members of your organization to use the elements as data sources. Users who are not granted access to use a specific data model cannot view or select its elements as data sources in workbooks and other data models.

1. Open the data model that you want to share.
2. In the data model header, select the document name to open the document menu, then select **Share**.
3. In the **Share Data Model** modal, search for and select an organization member, team, or email address.
4. In the **Permission** field, select an option:

   |  |  |
   | --- | --- |
   | **Can view** | Allows selected users to view and use the data model and its reusable elements. |
   | **Can edit** | Allows selected users to view, use, and edit the data model and its reusable elements. |
5. Click **Share** to save the permissions.

### Enable or disable an element as a data source

By default, elements in a data model are visible as data sources in workbooks and other data models. You can enable or disable an element as a data source at any time. Elements disabled as a source are available on the page of a data model but are hidden from the data model overview, and thus also hidden from viewers of the data model.

You can create a relationship between elements disabled as sources. For the related columns to be available for use in other data models or workbooks, the primary source in a relationship (or the highest level primary source in a hierarchy of relationships) must be enabled as a data source. See [Define relationships in data models](/docs/define-relationships-in-data-models).

1. Open the data model containing the element you want to edit.
2. In the data model header, click **Edit**.
3. Locate and select the element in the **ERD** or the [workbook page](/docs/navigate-data-models#data-model-workbook-page), then in the editor panel, select the **Modeling** tab.
4. In **Source visibility** section, turn on or turn off the **Visible as source** toggle. By default, the toggle is turned on to make the table available as a data source to workbooks and other data models.

### Edit an element

Edit a reusable or disabled element in a data model as you would in a Sigma workbook.

1. Open the data model containing the element you want to edit.
2. In the data model header, click **Edit** to open the [workbook page](/docs/navigate-data-models#data-model-workbook-page).
3. Locate the element you want to edit, then modify it as needed.

### Delete an element

Delete a reusable or disabled element to permanently remove it from the data model.

1. Open the data model containing the element you want to delete.
2. In the data model header, click **Edit** to open the [workbook page](/docs/navigate-data-models#data-model-workbook-page).
3. Hover over or select the element you want to delete, then click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** and select **Delete element** from the menu.

### Delete a data model

To delete a data model you must be the owner of the data model, have **Can edit** access to it, or have the **Admin** account type.

1. Select the data model name to open the document menu, then select **File > Delete...**.
2. On the **Confirm Deletion** modal, click **Delete**.

### Recover a deleted data model

To recover a data model that has been deleted, you must be the owner of the data model or have the **Admin** account type.

1. Go to your ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/home.svg) **Home** page.
2. In the navigation menu, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/trash-fill.svg) **Trash**.
3. In the **Trash** page, search the list of deleted documents and click the one you want to recover. You can sort the **Name**, **Deleted on**, or **Deleted by** columns to help identify the applicable document.
4. In the **Document has been deleted** modal, click **Recover**. Sigma immediately opens the recovered document.

Updated 3 days ago

---

Related resources

* [Intro to data models (Beta)](/docs/intro-to-data-models)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Create a data model with reusable elements](#create-a-data-model-with-reusable-elements)
  + - [Create a data model from a workbook table](#create-a-data-model-from-a-workbook-table)
  + [Map changed columns in a data model](#map-changed-columns-in-a-data-model)
  + - [Troubleshooting: Unable to select column](#troubleshooting-unable-to-select-column)
    - [Troubleshooting: Column is not listed](#troubleshooting-column-is-not-listed)
  + [Manage an existing data model](#manage-an-existing-data-model)
  + - [Edit a data model's name](#edit-a-data-models-name)
    - [Edit a data model’s description](#edit-a-data-models-description)
    - [Share the data model](#share-the-data-model)
    - [Enable or disable an element as a data source](#enable-or-disable-an-element-as-a-data-source)
    - [Edit an element](#edit-an-element)
    - [Delete an element](#delete-an-element)
    - [Delete a data model](#delete-a-data-model)
    - [Recover a deleted data model](#recover-a-deleted-data-model)