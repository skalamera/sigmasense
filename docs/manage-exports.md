# Configure additional options for exports

# Configure additional options for exports

When you export workbook data from Sigma, you can configure additional options to control the appearance and content that gets exported.

> 👍
>
> ### The additional options that are available depend on the export destination you select. Options that are not applicable based on your export configurations will appear greyed out.

## User requirements

To configure export options, you must be assigned an [account type](/docs/license-and-account-type-overview) with relevant export permissions.

## Set up a custom delivery schedule

When you configure a scheduled export, if the default delivery options do not work for your needs, you can set up a custom cron schedule to define the delivery time.

* On the **Schedule Exports** dialog, for the **Frequency**, choose **Custom** and enter a cron expression.

Use cron syntax to specify the minute, hour, day (month), month and day (week). For assistance writing cron expressions, see [crontab guru](https://crontab.guru/).

For example, to send a report at 1:30 AM on the first of every month, enter:

`30 1 1 * *`

This is read as, "run at 30 minutes after 1 AM on the 1st day of the month every month, regardless of the day of the week."

For example, to send a report at 1:05 AM on the first Monday of every quarter, enter:

`5 1 * 1/3 1#1`

This is read as, "run at 5 minutes after 1 AM regardless of the day of the month, every third month from January through December if it is the first Monday of the month."

> 📘
>
> ### If you don't have the option to set a custom frequency, export frequency might be restricted for your organization. For more details, see [Restrict export recipients and frequency](/docs/restrict-export-recipients).

## Filter by control values

If your workbook uses controls to filter the data on a page or for a given element, you can also choose to filter the exported data by the values of one or more controls.

You can only set this option for scheduled exports.

1. On the **Schedule Exports** dialog, in the **More Options** section, select the checkbox for **Customize control values**.
2. In the **Controls** section that appears, search for and select a control ID in the search box.
3. Select the control value for the control and set it to the value that you want to use for the export.
4. Search to add another control, or click **Create** to save the scheduled export.

## Merge PDF or Excel files

If you export multiple PDF or Excel files, you can combine the attachments into one file:

* Multiple workbook pages or data elements as PDF attachments into one PDF file.
* Multiple data elements as Excel attachments into one Excel file.

To combine attachments into one file, do the following:

* On the **Export** or **Schedule Exports** dialog, in the **More Options** section, select the checkbox for **Combine attachments**.

  If you don't see the checkbox, make sure that you selected a file type of **Excel** or **PDF** for at least 2 attachments.

## Compress attachments to a .zip file

If you export one or more attachments that result in a large file size, you can choose to compress the attachments into a ZIP file.

* On the **Export** or **Schedule Exports** dialog, in the **More Options** section, select the checkbox for **Send as .zip file**.

  Your attachments appear in one zip file named `merged-report.zip`.

## Repeat header labels

If you export a pivot table to Excel or CSV, you can repeat the header labels so that each pivot table row and column header appears in its own cell:

* On the **Export** or **Schedule Exports** dialog, in the **More Options** section, select the checkbox to **Repeat header labels**.

  If you don't see the checkbox, make sure that the file format is Excel or CSV and that you are exporting a pivot table element or a page or workbook with a pivot table element.

For example, for a pivot table like the following:

![Pivot table with product type and product family rows and store region columns with total cost and total quantity, with nothing repeated](https://files.readme.io/5087230-pivot-row-column-repeat-source.png)

When you export the pivot table element, the headers show up for each pivot table row and column:

![Pivot table exported to excel with product family values duplicated in the row, and store region header name and values repeated across column headers.](https://files.readme.io/e1fa92f-pivot-export-repeated.png)

If you don't configure this setting, the pivot table row and column headers only show up once:

![Same pivot table with product type values listed once for each category in the pivot rows, store region listed once in the export, and values for store region listed once for each set of columns.](https://files.readme.io/8bd0afb-pivot-export-no-repeat.png)

To configure this setting in the pivot table itself, see [Repeat row labels](/docs/working-with-pivot-tables#repeat-row-labels).

## Download Excel files with metadata

If you want to include additional metadata with Excel files, such as the date and time of the export and the name of the user downloading the Excel file, do the following:

1. For a workbook or workbook page, select the (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the menu, then select **Export...**. For a workbook element, select **More** ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) > **Export**, then under **Send**, select **Export**.
2. On the **Export** dialog, leave the default **Direct Download** option selected.
3. For the file type, select **Excel**.
4. In the **More Options** section, select the checkbox for **Include metadata**.
5. Select **Export**.

## Format PDF export page layout

When exporting PDF files from Sigma, you can configure several different options to improve the format of the exported report:

* Set a custom page width to match your desired PDF page width. Use 1050 pixels for letter-sized portrait PDF exports, or 1380 pixels for letter-sized landscape PDF exports. Use other pixel widths for other PDF page sizes. See [Layout style settings](/docs/workbook-settings-overview#layout-style-settings).
* Show up to 1000 rows of data in a table in your PDF. See [Show additional rows](#show-additional-rows).
* Add a page break element to control where elements are pushed to the next page of the PDF export. See [Add a page break](#add-a-page-break).

If your workbook uses legacy layouts, see [Format PDF exports (legacy layouts)](/docs/format-pdf-exports).

### Show additional rows

If you want to export up to 1,000 rows of a table or pivot table, do the following:

> 📘
>
> ### If you want to export an entire workbook or a page of the workbook, the table must be on its own row, without elements next to it, and cannot be in a container.

1. Open the workbook in **Edit** mode.
2. In your workbook, locate the element that you want to show up to 1,000 rows of data for.
3. Select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Export formatting**, then click **Expand table to first 1k rows**. If this option has already been set, a checkmark is visible.  
   ![](https://files.readme.io/282d97f4b7b538582726ce5381de9bdd7736164d87baf703acbaa390d30b8f7f-export-expand-table.png)
4. Publish the workbook.
5. Export the workbook to PDF to make sure the output looks as desired.
6. Make any necessary changes, then set up a scheduled export to your preferred destination.

### Add a page break

If you want to specify where to break a PDF export of the workbook into separate pages, or if workbook elements get cut off or don't display as expected in a PDF export, add one or more page break elements to your workbook pages:

1. Open the workbook in **Edit** mode.
2. Select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) to open the workbook's **Add New Element** panel.
3. In the **PDF export elements** section, select a **Page break** element and drag it onto the workbook canvas.
4. Publish the workbook.
5. Export the workbook to PDF to make sure the output looks as desired.
6. Make any necessary changes, then set up a scheduled export to your preferred destination.

### Example PDF layout configurations

In this example, no configuration changes have been made and a PDF export in portrait orientation exports a table with the same number as rows that are visible in the workbook:

![PDF export with the standard amount of rows.](https://files.readme.io/365e768-Screenshot_2024-05-13_at_3.44.00_PM.png)

In this example, the option to show up to 1,000 rows of data for a table has been selected, but no page break element is used on the workbook page. Choosing a PDF export in portrait orientation exports a table of up to 1000 rows, and at the end of the 1000 row table, a text element is visible on the same page. On the next page, another data element is visible:

![PDF export with up to 1000 rows displayed](https://files.readme.io/3a6b195-Screenshot_2024-05-13_at_3.52.31_PM.png)

In this example, the option to show up to 1,000 rows of data for a table has been selected and a page break element is used on the workbook page before a text element and a second data element. Choosing a PDF export in portrait orientation exports a table of up to 1000 rows, and at the end of the 1000 row table, there is a page break. On the next page, a text element is visible, followed by another data element:

![PDF export with up to 1000 rows displayed and a page break element used](https://files.readme.io/292bb9b-Screenshot_2024-05-13_at_3.52.48_PM.png)

Updated 3 days ago

---

[Export to Microsoft SharePoint](/docs/export-to-microsoft-sharepoint)[Manage scheduled exports](/docs/manage-scheduled-exports)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Set up a custom delivery schedule](#set-up-a-custom-delivery-schedule)
  + [Filter by control values](#filter-by-control-values)
  + [Merge PDF or Excel files](#merge-pdf-or-excel-files)
  + [Compress attachments to a .zip file](#compress-attachments-to-a-zip-file)
  + [Repeat header labels](#repeat-header-labels)
  + [Download Excel files with metadata](#download-excel-files-with-metadata)
  + [Format PDF export page layout](#format-pdf-export-page-layout)
  + - [Show additional rows](#show-additional-rows)
    - [Add a page break](#add-a-page-break)
    - [Example PDF layout configurations](#example-pdf-layout-configurations)