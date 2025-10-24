# Workbook modes overview

# Workbook modes overview

Sigma features three workbook modes (**View**, **Explore**, and **Edit**) that provide different levels of interactions, customizations, and analysis within a workbook. Each mode is designed to help you perform specific tasks depending on your objectives and permissions.

## Workbook mode objectives

|  | View mode | Explore mode | Edit mode |
| --- | --- | --- | --- |
| Purpose | Allows you to view a published version of a workbook (the version labeled “Published” and all tagged versions). | Provides an isolated environment in which you can customize published workbook content and perform ad hoc analysis in your own custom view *without affecting saved or shared versions of a workbook*. | Provides a draft environment with full-scope analytic functionality that allows you to edit and save an individual or collaborative analysis. |
| Use case | Recommended when you need to view prepared data and insights without performing additional analysis. | Recommended when you need quick answers to specific business questions, but you don’t want your changes to affect the published version. | Recommended when you need to build reports and publish them for future use or sharing. |
| Required account type permission | **View workbooks** or **Basic explore** | **Full explore** | **Create, edit, and publish workbooks** |
| Required workbook access | **Can view**, **Can explore**, **Can edit**, or **Owner** | **Can explore**, **Can edit**, or **Owner** | **Can edit** or **Owner** |

## Workbook accessibility comparison

The following table compares what you can do in each mode based on the workbook access that is granted to you or inherited from workspace or folder access.

|  | View mode (Can view) | View mode (Can explore / Can edit) | Explore mode (Can explore / Can edit) | Edit mode (Can edit) |
| --- | --- | --- | --- | --- |
| Update control values |  |  |  |  |
| Modify existing filters |  |  |  |  |
| Sort column data |  |  |  |  |
| View column details |  |  |  |  |
| Expand/collapse grouped rows |  |  |  |  |
| View *aggregated* underlying data |  |  |  |  |
| Refresh data |  |  |  |  |
| Create saved views |  |  |  |  |
| View and add comments1 |  |  |  |  |
| Create new filters |  |  |  |  |
| View and drill into *unaggregated* underlying data |  |  |  |  |
| Use drill paths ("Drill anywhere") |  |  |  |  |
| Format, reorder, rename, hide, freeze, and delete columns |  |  |  |  |
| Enter input table values2 |  |  |  |  |
| Download individual elements to PNG |  |  |  |  |
| Download individual elements to CSV, Excel, JSON, Google Sheets, or PDF3 |  |  |  |  |
| Send or schedule exports4 |  |  |  |  |
| Copy data point values |  |  |  |  |
| Create, edit, and delete pages |  |  |  |  |
| Create, edit, and delete elements *(editing encompasses properties, format, actions, columns, etc.)* |  |  |  |  |
| Duplicate and move existing elements |  |  |  |  |
| Copy/paste elements |  |  |  |  |
| View and change element data sources |  |  |  |  |
| Add and modify columns |  |  |  |  |
| View custom SQL logic |  |  |  |  |
| Edit layouts and workbook settings |  |  |  |  |
| View lineage |  |  |  |  |
| View hidden pages |  |  |  |  |
| Publish workbook edits |  |  |  |  |

1Requires an [account type](/docs/license-and-account-type-overview) with the **Can comment on workbooks** permission enabled.

2Requires the input table element's [data entry permission](/docs/create-and-manage-input-tables#set-data-entry-permission) to be set to the workbook's published version.

3The ability to download to CSV, Excel, JSON, and PDF requires an [account type](/docs/license-and-account-type-overview) with the **Download or Send Now** permission enabled. The ability to download to Google Sheets also requires the **Export to Google Sheet** permission.

4The ability to send exports (using the **Send now** feature) requires an [account type](/docs/license-and-account-type-overview) with the **Download or Send Now** permission enabled. The ability to schedule exports requires the **Schedule export** permission.

Updated 3 days ago

---

Related resources

* [Use a workbook in Explore mode](/docs/use-a-workbook-in-explore-mode)
* [Workbook collaboration with Live Edit](/docs/workbook-collaboration-with-live-edit)

* [Table of Contents](#)
* + [Workbook mode objectives](#workbook-mode-objectives)
  + [Workbook accessibility comparison](#workbook-accessibility-comparison)