# Format PDF exports (legacy layouts)

# Format PDF exports (legacy layouts)

You can configure the appearance of PDF exports from your workbook, configuring where PDF pages break and how many rows to export for a given table element.

How you configure PDF export formatting depends on the layout used by your workbook:

* Grid layouts (most workbooks). See [Configure additional options for exports](/docs/configure-additional-options-for-exports#format-pdf-export-page-layout).
* Legacy layouts. This page describes PDF export formatting for legacy layouts.

## User requirements

The ability to format PDF exports requires the following:

* You must be assigned an account type with the **Full explore** permission enabled.
* You must be the workbook owner or be granted **Can explore** or **Can edit** [workbook permission](/docs/folder-and-document-permissions).

## About page sections

Page sections let you lay out elements on workbook pages for workbooks that use legacy layouts.

If a workbook page has elements on it, it has one or more sections with one or more elements.

For example, the workbook in the following screenshot contains 3 sections:

![A workbook in edit mode with the page overview tab selected, showing one section with a chart and a page title, another section with two charts, and a third section with one table.](https://files.readme.io/20513e9-1.png)

## Show first 1k rows

By default, table and pivot tables in exported PDFs only display the number of rows that appear on the dashboard. If you want to display more rows in your export, you can configure the option to show up to 1,000 rows per table. You cannot export more than 1,000 rows per table in a PDF.

When you configure this option, the table headers appear on every PDF page containing the table data, and up to 1000 rows of data for the table are exported.

For legacy layouts, you must configure this option for a [page section](#about-page-sections) instead of an individual element. The section must only contain a single table or pivot table element.

**Before you start:** This action is only available in Edit mode. To begin editing, click **Edit** in the top right corner of the page.

1. Open the workbook page **PAGE ELEMENTS** editor panel by selecting the caret.
2. Hover over the section containing your target table or pivot table, and click ![more menu](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**.  
   ![Workbook with the page overview open and the page section with a table in it highlighted.](https://files.readme.io/4e15d30-2.png)
3. Select **Export formatting** > **Expand to first 1k rows**.

   A check displays beside **Expand to first 1k rows** if the option is already configured.  
   ![More menu selected showing the export formatting option in the menu.](https://files.readme.io/28e60cb-3.png)

To see how the table looks on your export, [download the page as a PDF](/docs/download-workbook-data) or use [Send Now](/docs/manage-scheduled-exports#send-a-scheduled-export-on-demand) to test an existing schedule.

## Add page breaks

You can customize the look of your exported PDFs by adding page breaks after any section in your dashboard.

1. Open the workbook page **PAGE ELEMENTS** editor panel by selecting the caret.
2. In the editor panel, hover over the section containing your target table or pivot table, and click ![more menu](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**.
3. Select **Export formatting** > **Page Break After Section**.

   A check displays beside **Page Break After Section** if the option is already configured.  
   ![More menu selected showing the export formatting option in the menu.](https://files.readme.io/28e60cb-3.png)

   Page breaks apply to your next export.

To see how the table looks on your export, you can do one of the following:

* [Download the page as a PDF](/docs/download-workbook-data)
* [Send a scheduled export on demand](/docs/manage-scheduled-exports#send-a-scheduled-export-on-demand) to test an existing schedule.

Updated 3 days ago

---

Related resources

* [Download and export limitations](/docs/download-export-and-upload-limitations)
* [Intro to data elements](/docs/intro-to-data-elements)
* [Send or schedule workbook exports](/docs/send-or-schedule-workbook-exports)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [About page sections](#about-page-sections)
  + [Show first 1k rows](#show-first-1k-rows)
  + [Add page breaks](#add-page-breaks)