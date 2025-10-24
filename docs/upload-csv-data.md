# Upload CSV data

# Upload CSV data

Upload CSV data to analyze data that isn't stored in a connected data platform.

## System and user requirements

The ability to upload CSV data requires the following:

* [Write access](/docs/set-up-write-access) must be enabled for the connection you want to use to upload CSV data.
* The [**CSV upload**](/docs/enable-csv-upload) feature must be enabled for your organization.
* You must be assigned an [account type](/docs/create-and-manage-account-types) with the **Upload CSV** permission enabled.

## Limitations

The maximum file size for uploading a CSV-formatted file is 200MB.

## Where's my data stored?

When a CSV file is uploaded to Sigma, the data in the file is automatically written to your data platform as a new table in the schema used for write-back, prepended by `sigma_df_csv`. If your organization has multiple connections with write access enabled, you can choose which connection to write the data to.

If you upload a CSV file to a workbook, the data in your file is **only accessible from the Sigma workbook** that uses the CSV file. You cannot see the table created from the CSV upload when browsing the tables in the connection's data catalog. If you delete the workbook, the data from the CSV file is no longer accessible.

> 💡
>
> ### To reuse a CSV file in other workbooks, [create a data model](/docs/create-and-manage-data-models) instead. You can also [create a data model from a workbook table element](/docs/create-and-manage-data-models#create-a-data-model-from-a-workbook-table) if you already uploaded the file to a workbook.

## Create a workbook from a CSV file

1. Click ![Add element](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Create New** in the left navigation panel, then select **Upload CSV**.

   The **Upload CSV** page opens.
2. Select a **Connection** from the drop-down menu to specify the cloud data warehouse to upload your file to.  
   If only one data warehouse has write access enabled, it is selected by default.  
   ![Upload CSV page shown with the Sigma Docs Database connection selected in the Connections drop-down menu.](https://files.readme.io/3a33d42-upload-csv.png)
3. Upload your CSV file by dragging and dropping it into the **Upload CSV** section, or click **Browse**.

   A preview of your data appears.
4. While previewing your data, you can address any warnings or errors and make other adjustments:

   * [optional] On the left side of the page, deselect the checkboxes for any columns you want to exclude from the upload.
   * [optional] Customize the parsing options under **Parsing Options**.

   ![CSV file preview page, with a list of columns showing in the File Upload section with checkboxes that you can select or deselect, a Parsing Options section where you can specify whether the file contains headers, the delimiter used, whether the file uses single or double quotes, and the escape character to use. Your data as it will upload displays in the Results tab, and Warnings and Raw tabs are also visible.](https://files.readme.io/cd185e9-3.png)
5. Click **Explore** in the top right corner of the page to open the data in a workbook.

## Add a CSV file to an existing workbook

If you have an existing workbook, you can add a CSV file as a data element to the workbook.

**Before you start:** This action is only available in edit mode. To begin editing, click **Edit** in the top right corner of the page; see [Workbook lifecycle](/docs/workbook-lifecycle-explore-draft-and-publish).

1. From within a workbook, select ![Add element](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) to open the workbook's **Add new element** panel.
2. Under **Data elements**, select the type of element you want to add: **Table**, **Visualization**, or **Pivot table**.
3. As your data source for the element, select **CSV** to upload a CSV-formatted file.
4. Select a **Connection** from the drop-down menu to specify the cloud data warehouse to upload your file to.  
   If only one data warehouse has write access enabled, it is selected by default.  
   ![Upload CSV page shown with the Sigma Docs Database connection selected in the Connections drop-down menu.](https://files.readme.io/3a33d42-upload-csv.png)
5. Upload your CSV file by dragging and dropping it into the **File Upload** section, or click **Browse**.

   A preview of your data appears.
6. While previewing your data, you can address any warnings or errors and optionally customize the parsing options in the **Parsing Options** section.

   ![CSV file preview page, with a list of columns showing in the File Upload section with checkboxes that you can select or deselect, a Parsing Options section where you can specify whether the file contains headers, the delimiter used, whether the file uses single or double quotes, and the escape character to use. Your data as it will upload displays in the Results tab, and Warnings and Raw tabs are also visible.](https://files.readme.io/cd185e9-3.png)
7. Click **Done**.

   Your new element appears on the page, and the editor panel opens to the specific element’s configuration view.

Updated 3 days ago

---

Related resources

* [Enable CSV Upload](/docs/enable-csv-upload)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Limitations](#limitations)
  + [Where's my data stored?](#wheres-my-data-stored)
  + [Create a workbook from a CSV file](#create-a-workbook-from-a-csv-file)
  + [Add a CSV file to an existing workbook](#add-a-csv-file-to-an-existing-workbook)