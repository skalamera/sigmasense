# Send or schedule workbook exports

# Send or schedule workbook exports

Export or download workbook contents to use outside of Sigma, enabling automated reporting and workflows. You can choose from a variety of methods, formats, and destinations:

* Download workbook data on demand.
* Schedule an export to one or more destinations.
* Send a scheduled export on demand.

You can export any of the following:

* An entire workbook
* A single page of a workbook
* A specific element of a workbook

When you export to destinations such as email, Slack, or others, the latest published version of the workbook is exported. Depending on the destination and file format you choose, you can also export a saved view or a tagged version. While editing a workbook, you can download the current draft workbook, page, or element.

If you export data that uses [materialization](/docs/materialization), the materialized data is not used and a new query is run.

## Available export destinations and formats

Depending on what you want to export and where you want to send it, different data formats are available:

| Export destination | Entire workbook | Workbook page | Workbook page element |
| --- | --- | --- | --- |
| [Download](/docs/download-workbook-data) | Excel, PDF | Excel, PDF, PNG | CSV, Excel, JSON, PDF, PNG |
| [Email](/docs/export-to-email), including [email bursts](/docs/export-as-email-burst) | Excel, PDF | Excel, PDF, PNG | CSV, Excel, JSON, PDF, PNG |
| [Microsoft Teams](/docs/export-to-microsoft-teams) and [Microsoft SharePoint](/docs/export-to-microsoft-sharepoint) | Excel, PDF | Excel, PDF, PNG | CSV, Excel, JSON, PDF, PNG |
| [Slack](/docs/export-to-slack) | Excel, PDF | Excel, PDF, PNG | CSV, Excel, PDF, PNG |
| [Google Sheets](/docs/export-to-google-sheets) | Unsupported | Unsupported | Google Sheet |
| [Google Drive](/docs/export-to-google-drive) | Excel, PDF | Excel, PDF, PNG | CSV, Excel, Google Sheet, JSON, PDF, PNG |
| [Webhook](/docs/export-to-webhook) | Unsupported | Unsupported | CSV, JSON, PDF, PNG |
| [Cloud storage](/docs/export-to-cloud-storage) | Unsupported | Unsupported | CSV, gzipped CSV |

> 🚧
>
> When executing a scheduled export or direct download to PDF or PNG formats, Sigma may store applicable control values as URL parameters in trace logs used for debugging and troubleshooting purposes. Exercise caution when exporting or downloading workbook content that uses controls to filter sensitive data.

File size limits apply to the various exports. See [Download and export limitations](/docs/download-export-and-upload-limitations).

Certain export destinations are not compatible with exporting elements from [saved views](/docs/create-and-share-saved-views) and [version tags](/docs/create-and-manage-version-tags):

| Export destination | Exporting elements on a saved view | Exporting elements on a version tag |
| --- | --- | --- |
| [Download](/docs/download-workbook-data) | Supported | Supported |
| [Email](/docs/export-to-email) | Supported | Supported |
| [Email bursts](/docs/export-as-email-burst) | Unsupported | Supported |
| [Microsoft Teams](/docs/export-to-microsoft-teams) and [Microsoft SharePoint](/docs/export-to-microsoft-sharepoint) | Supported | Supported |
| [Slack](/docs/export-to-slack) | Supported | Supported |
| [Google Sheets](/docs/export-to-google-sheets) | Unsupported | Unsupported |
| [Google Drive](/docs/export-to-google-drive) | Supported | Supported |
| [Webhook](/docs/export-to-webhook) | Supported | Supported |
| [Cloud storage](/docs/export-to-cloud-storage) | Unsupported | Unsupported |

> 👍
>
> ### When exporting elements that are only on a saved view, and not in the published version of a workbook, you must open the export modal (**Share and export** > **Export…** or **Share and export** > **Schedule exports…**) from the saved view.

## Manage scheduled exports

You can manage scheduled exports in different ways:

* Manage scheduled exports that you own or that you receive. See [Manage scheduled exports](/docs/manage-exports).
* Manage exports scheduled for a workbook. See [Manage scheduled exports](/docs/manage-exports).
* As an admin, manage all scheduled exports for your organization. See [Manage organization schedules](/docs/manage-organization-schedules).

## Table and pivot table PDF export formatting

When you export a table or pivot table to PDF, the formatting is handled differently based on the layout used by the workbook.

* For grid layouts, the formatting matches the workbook layout. See [Format PDF export page layout](/docs/configure-additional-options-for-exports#format-pdf-export-page-layout).
* For legacy layouts, see [Table and pivot table PDF export formatting (legacy layouts)](/docs/table-and-pivot-table-pdf-export-formatting-legacy-layouts#table-and-pifor-pdf-export-formatting).

Updated 3 days ago

---

Related resources

* [Schedule a conditional export or alert](/docs/schedule-a-conditional-export-or-alert)
* [Apply control values to scheduled exports](/docs/apply-control-values-to-scheduled-exports)
* [Export to email](/docs/export-to-email)
* [Export to Slack](/docs/export-to-slack)
* [Export to webhook (Beta)](/docs/export-to-webhook)
* [Export to cloud storage (Beta)](/docs/export-to-cloud-storage)
* [Export to Google Sheets or Drive](/docs/export-to-google-sheets-or-drive)
* [Download workbook data](/docs/download-workbook-data)

* [Table of Contents](#)
* + [Available export destinations and formats](#available-export-destinations-and-formats)
  + [Manage scheduled exports](#manage-scheduled-exports)
  + [Table and pivot table PDF export formatting](#table-and-pivot-table-pdf-export-formatting)