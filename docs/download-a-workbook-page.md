# Download workbook data

# Download workbook data

You can download an entire workbook, a specific workbook page, or a specific workbook element from Sigma at any time. You can also schedule an export or send a scheduled export on-demand. See [About exporting workbooks](/docs/send-or-schedule-workbook-exports).

If you attempt to export a workbook while editing it, you only have the option to download the draft version. If you want to download the published version or export to other destinations, open the published version of the workbook.

> 🚧
>
> When executing a scheduled export or direct download to PDF or PNG formats, Sigma may store applicable control values as URL parameters in trace logs used for debugging and troubleshooting purposes. Exercise caution when exporting or downloading workbook content that uses controls to filter sensitive data.

## Export types and limitations

There are size limits for exports based on file type and export location. For more information, see [Download, export, and upload limitations](/docs/download-export-and-upload-limitations).

## User requirements

To download data from a workbook, you must be assigned an account type with the **Download** permission enabled. See [License and account type overview](/docs/license-and-account-type-overview).

## Download an entire workbook

To download an entire workbook:

1. From the workbook menu (![caret icon](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)), select **Share and export> Export...**.
2. On the **Export** dialog, keep the default selection of **Direct download**.
3. For **Attachments**, keep the default selection of **Entire workbook** and select the format of the file to download.
4. Click **Export**.

   Sigma downloads a file to your device.

## Download a workbook page

You can download a workbook page from the workbook page menu or from the workbook menu.

1. Locate the workbook page that you want to download and open the page menu (![caret icon](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) and select **Export...**.  
   ![Workbook page menu selected and open to display options to export or copy page](https://files.readme.io/ba1d0e0b261accef8557b4dd31c0be2e40ffc5448a9d03d859d842bf12938eae-page-menu.png)
2. On the **Export** dialog, keep the default selection of **Direct download**.
3. For **Attachments**, keep the default page selected or choose another workbook page.
4. Select the format of the file to download.
5. Click **Export**.

   Sigma downloads a file to your device.

## Download a data element

1. In a published or draft workbook, select the element.
2. From the element's menu, select **More** ![more menu](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg).
3. Select **Export** and choose the file format that you want to download.  
   The available options depend on the type of element.  
   ![Export menu selected and showing download options of CSV, Excel, JSON, Google Sheets, and PDF options for immediate download, and two additional options to Export or Schedule exports.](https://files.readme.io/f4977cd-export-menu.png)

   Sigma downloads a file to your device.

Updated 3 days ago

---

[Schedule a conditional export or alert](/docs/schedule-a-conditional-export-or-alert)[Export to email](/docs/export-to-email)

* [Table of Contents](#)
* + [Export types and limitations](#export-types-and-limitations)
  + [User requirements](#user-requirements)
  + [Download an entire workbook](#download-an-entire-workbook)
  + [Download a workbook page](#download-a-workbook-page)
  + [Download a data element](#download-a-data-element)