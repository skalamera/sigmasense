# Basic explore vs. Full explore

# Basic explore vs. Full explore

[Account types](/docs/user-account-types) support two permissions (**Basic explore** and **Full explore**) that enable users to be granted **Can explore** [access to individual workbooks](/docs/folder-and-document-permissions). These account type permissions determine how users interact with workbooks, specifically in **View** and **Explore** mode.

* **Basic explore** enables users to access **View** mode with additional interactions and lightweight customization *when granted **Can explore** access to the workbook*.
* **Full explore** enables **Basic explore** capabilities in **View** mode and the full scope of interactions and customizations in **Explore** mode.

This document provides comprehensive comparisons of granular user capabilities based on account type permission (**View workbooks**, **Basic explore**, or **Full explore**) and workbook access (**Can view** or **Can explore**). For a complete comparison of capabilities in all workbook modes, including **Edit** mode, see [Workbook modes overview](/docs/workbook-modes-overview).

> 📘
>
> ### The comparisons include the **View workbook** permission to demonstrate the workbook interactions supported when a user is assigned an account type with neither **Basic explore** nor **Full explore** permission. For more information about these account type permissions, see [License and account type overview](/docs/license-and-account-type-overview).

## **View** mode + **Can view**

The following table lists the baseline interactions enabled in **View** mode *when a user is granted **Can view** workbook access*.

User capabilities are the same whether a user is assigned an account type with **View workbooks**, **Basic explore**, or **Full explore** permission.

|  | View workbooks | Basic explore | Full explore |
| --- | --- | --- | --- |
| Update control values |  |  |  |
| Modify existing filters |  |  |  |
| Sort column data |  |  |  |
| View column details |  |  |  |
| Expand/collapse grouped rows |  |  |  |
| View *aggregated* underlying data |  |  |  |
| Refresh data |  |  |  |
| Create bookmarks |  |  |  |

## **View** mode + **Can explore**

The following table lists additional interactions and lightweight customization enabled in **View** mode *when a user is granted **Can explore** workbook access*. All capabilities detailed in the previous section ([View mode + Can view](#view-mode--can-view)) are also supported.

Only users assigned account types with **Basic explore** or **Full explore** permission can be granted **Can explore** workbook permission. Therefore, users assigned account types limited to **View workbooks** permission cannot be granted **Can explore** workbook permission and cannot perform the following interactions.

|  | View workbooks | Basic explore | Full explore |
| --- | --- | --- | --- |
| Create new filters |  |  |  |
| View and drill into *unaggregated* underlying data |  |  |  |
| Use drill paths ("Drill anywhere") |  |  |  |
| Format, reorder, rename, hide, freeze, and delete columns |  |  |  |
| Enter input table values1 |  |  |  |
| Export to PNG |  |  |  |
| Copy data point values |  |  |  |
| Copy/paste elements |  |  |  |

1Requires the input table element's [data entry permission](/docs/create-and-manage-input-tables#set-data-entry-permission) to be set to the workbook's published version.

## **Explore** mode + **Can explore**

The following table lists the remaining interactions and customizations enabled in **Explore** mode *when a user is granted **Can explore** workbook access*. All capabilities detailed in the previous sections ([View mode + Can view](#view-mode--can-view) and [View mode + Can explore](#view-mode--can-explore)) are also supported.

Only users assigned account types with **Full explore** permission can access **Explore** mode. Therefore, users assigned account types limited to **View workbooks** or **Basic explore** permission cannot access **Explore** mode to perform the following capabilities.

|  | View workbooks | Basic explore | Full explore |
| --- | --- | --- | --- |
| Create, edit, and delete pages |  |  |  |
| Create, edit, and delete elements  *editing encompasses properties, format, actions, columns, etc.* |  |  |  |
| Duplicate and move existing elements |  |  |  |
| View and change element data sources |  |  |  |
| Add and modify columns |  |  |  |
| View custom SQL logic |  |  |  |
| Edit layouts and workbook settings |  |  |  |
| View lineage |  |  |  |

Updated 3 days ago

---

[Create and manage account types](/docs/create-and-manage-account-types)[View license utilization](/docs/view-license-utilization)

* [Table of Contents](#)
* + [View mode + Can view](#view-mode--can-view)
  + [View mode + Can explore](#view-mode--can-explore)
  + [Explore mode + Can explore](#explore-mode--can-explore)