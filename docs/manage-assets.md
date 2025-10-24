# Review warehouse view details

# Review warehouse view details

The **Warehouse Views** page in the **Administration** portal provides a centralized location to review details of all warehouse views created by users in your organization. The page allows you to search for and check the status of specific warehouse views, verify or copy view paths, and reference audit history, including who created a view and when it was created and last updated. You can also determine the location of a view’s source element and navigate directly to that workbook.

This document explains how to utilize the **Warehouse Views** page in the **Administration** portal. For information about creating, renaming, and deleting views, see [Create and manage workbook warehouse views](/docs/create-and-manage-workbook-warehouse-views).

## User requirements

To access the **Warehouse Views** page in the **Administration** portal, you must be assigned the **Admin** [account type](/docs/user-account-types).

## Utilize the **Warehouse Views** page

1. Go to **Administration** > **Warehouse Views**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Warehouse Views**.
2. In the **Warehouse Views** page, use the search bar, status filter (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/filter.svg)), and column sorting to view a focused list.

   The search feature looks for matches in the **Document** and **View name** fields.

   ![Example of searching for a specific view, matching steps above](https://files.readme.io/9c30464-1.png)
3. Review details about your organization's warehouse views, including source element name, view name, [status](/docs/review-warehouse-view-details#warehouse-view-statuses), and last update date.

   To rename or delete a specific warehouse view, click the workbook name in the **Document** column. Sigma opens the workbook where you can locate the source element and [manage the view](/docs/create-and-manage-workbook-warehouse-views).

   ![Warehouse view page with a specific view highlighted](https://files.readme.io/b16c5f9-2.png)

## Warehouse view statuses

The following statuses apply to warehouse views:

|  |  |
| --- | --- |
| Pending | Sigma will create or update the view when the workbook is published. |
| Successful | Sigma successfully created or updated the view. |
| In Progress | Sigma is currently creating or updating the view. |
| Failed | The view couldn’t be created or updated.1 |

1To view the cause of a failed status, hover over the **Failed** status indicator.

Updated 3 days ago

---

Related resources

* [Create and manage workbook warehouse views](/docs/create-and-manage-workbook-warehouse-views)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Utilize the Warehouse Views page](#utilize-the-warehouse-views-page)
  + [Warehouse view statuses](#warehouse-view-statuses)