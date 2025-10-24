# Create and manage warehouse views

# Create and manage warehouse views

Warehouse views are virtual tables saved to your data platform. You can create warehouse views from tables, pivot tables, input tables, and charts, then query them using Sigma or any other application in your data ecosystem. Warehouse views can simplify queries and allow you to retrieve relevant and up-to-date subsets of data directly from your data platform.

This document explains how to create and manage warehouse views in workbooks and data models. For information about the **Warehouse Views** page in the **Administration** portal, see [Review warehouse view details](/docs/review-warehouse-view-details).

> 📘
>
> This feature isn't supported by all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## System and user requirements

The ability to create and manage a warehouse view requires the following:

* The element’s data source must retrieve data from a connection with **Write access** enabled.
* You must be assigned an [account type](/docs/user-account-types) with the **Create warehouse views** permission enabled.
* You must be the workbook or data model owner or be granted **Can edit** [access](/docs/folder-and-document-permissions) to the workbook or data model.

## About warehouse views

Instead of storing data in a database table, a warehouse view saves a SQL statement that expresses specific query logic defined by an individual data element or input table in Sigma.

When you create a warehouse view, you establish a live link between your data platform and Sigma. The view references the data element or input table as the source of truth and automatically updates to reflect the most recent version of the element’s underlying data.

Because warehouse views query the data platform directly, they work differently from materializations. However, you can create a warehouse view from a materialized element, in which case the view queries the element’s materialized underlying data table.

### Warehouse view considerations

When you create a warehouse view, consider the following limitations and restrictions:

* Warehouse views are created from the published version of a document. You cannot create a warehouse view from a tagged version of a data model or workbook. Custom views and saved views on a workbook are also not supported. If a warehouse view is created in a draft, one of the following outcomes occur:

  + If the element only exists in the draft, Sigma creates the view when the workbook or data model is published and the element exists in the published version.
  + If the element exists in the published version but contains unsaved changes in the draft, Sigma creates the view based on the published version of the element, which might not match the data in the draft.
  + If the element exists in the published version and contains no unsaved changes in the draft, Sigma creates a view based on the published version of the element, which matches the data in the draft.
* The following dynamic conditions are not supported:

  + [Control values referenced as parameters](/docs/parameters-in-workbooks) in the element: Control values are not explicitly defined in an element's SQL statement because the query depends on user input. When control values are referenced as parameters in the element, Sigma dynamically generates the SQL at the time it executes the query and there is no predefined SQL statement to save as a warehouse view.
  + Relative date filters: Relative date filters (like **Last**, **Next**, and **Current**) depend on current date criteria that cannot be explicitly defined in an element's SQL statement. Therefore, they are not saved to warehouse views.
* If you create a warehouse view from a grouped table, you cannot define which grouping levels to use for the warehouse view. The warehouse view represents the data displayed in the published version of the element, which might or might not include grouped data. If groupings and grouping levels are edited in the element, those changes are applied to the view when the workbook is published.
* If a data element contains [column-level security](/docs/column-level-security) , you cannot create a warehouse view.
* If the data element is [transposed](/docs/transpose-a-table) , you cannot create a warehouse view.
* If your Sigma organization and data platform have different account time zones, date columns in the warehouse view might display unexpected values. For more information, see [Warehouse views time zone support](/docs/account-time-zone#warehouse-views-time-zone-support).

## Create a view

To create a warehouse view, do the following:

1. Open a published workbook or data model and locate the element for which you want to create a warehouse view.
2. In the element toolbar, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** to open the element menu, then select **Advanced options** > **Create warehouse view**.

   ![Element menu open to show the option for creating a warehouse view on a table element.](https://files.readme.io/50c1b470d6e85a19c76faff5273ad6e26a0eee094ccfd6e82bf189b1bb163c9d-whv-create-element.png)
3. In the **Create Warehouse View** modal, Sigma auto-generates a name for the view. If needed, edit the name, then click **Create**.

   This name is also used when saving your view in the data platform.

   ![Create warehouse view modal, with an autogenerated name FY_23_TARGET_V_FORECAST, and a reminder of the path to the view in the data warehouse, in this case, DOCUMENTATION_TEAM.SIGMA_WRITABLE.FY_23_TARGET_V_FORECAST. A callout reminds you that the warehouse view is created with your data permissions and only includes published changes.](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/create-and-manage-warehouse-views/create-warehouse-view-modal.png)
4. Sigma notifies you when it successfully creates the view (see [Warehouse view statuses](#warehouse-view-statuses)). You can also preview the status in the element toolbar or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/info.svg) **View warehouse view info** to see details about the view.

   ![Hovering over the view warehouse view info option in the element toolbar to view the location, view name, and status of the view. This one is pending.](https://files.readme.io/629786f6c4527e6a375ff9ed5854d9224aeb3e251696ac44b17ddc8549871773-whv-status.png)

   > 📘
   >
   > ### After Sigma creates the view, filters and any other changes applied to the element are only saved to the view when the workbook is republished.

You can only create one warehouse view per element. If you need to create multiple views of the same data, you can duplicate the element, adjust the data as needed, and create a separate warehouse view.

## Rename a view

To rename a warehouse view, do the following:

1. Open a workbook or data model and locate the element associated with the warehouse view that you want to rename.
2. In the element toolbar, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** to open the element menu, then select **Advanced options** > **Manage warehouse view**.
3. In the **Manage Warehouse View** modal, enter a new name in the **Name** field, then click **Update**.

   The warehouse view name and path update.

   ![Modal showing the new name, FY23_Forecast, with the updated location and path visible.](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/create-and-manage-warehouse-views/manage-warehouse-view-modal_update.png)

   You can preview the status of the warehouse view update in the element toolbar or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/info.svg) **View warehouse view info** to see details about the view. See [Warehouse view statuses](#warehouse-view-statuses).

   ![Hovering over the view warehouse view info option in the element toolbar to view the location, view name, and status of the view. This one is successful.](https://files.readme.io/8bc3cc8568874a692fb3bc324ece951e141767318fbb3b943899f18c4e2430cd-whv-info.png)

## Delete a view

To delete a warehouse view, do the following:

1. Open a workbook or data model and locate the element associated with the warehouse view you want to delete.
2. In the element toolbar, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** to open the element menu, then select **Advanced options** > **Manage warehouse view**.
3. In the **Manage Warehouse View** modal, click **Delete**.
4. In the **Confirm Delete** modal, click **Delete**.

## Warehouse view statuses

The following statuses apply to warehouse views:

|  |  |
| --- | --- |
| Pending | Sigma will create or update the view when the workbook is published. |
| Successful | Sigma successfully created or updated the view. |
| In Progress | Sigma is currently creating or updating the view. |
| Failed | The view couldn’t be created or updated. To view the cause of a failed status, hover over the **Failed** status indicator in the warehouse view details. |

## Troubleshooting

If you cannot create a warehouse view for a particular element, determine if any of the following are true:

* You’re currently working in an exploration. You must save an exploration as a workbook before creating a warehouse view.
* You’re attempting to create a warehouse view for a data element or input table sourced from another warehouse view. Views cannot query other views.
* The element data [references control values as parameters](/docs/parameters-in-workbooks).
* The element type doesn’t currently support warehouse views.

Updated 3 days ago

---

Related resources

* [Review warehouse view details](/docs/review-warehouse-view-details)
* [Dataset Warehouse Views](/docs/dataset-warehouse-views)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [About warehouse views](#about-warehouse-views)
  + - [Warehouse view considerations](#warehouse-view-considerations)
  + [Create a view](#create-a-view)
  + [Rename a view](#rename-a-view)
  + [Delete a view](#delete-a-view)
  + [Warehouse view statuses](#warehouse-view-statuses)
  + [Troubleshooting](#troubleshooting)