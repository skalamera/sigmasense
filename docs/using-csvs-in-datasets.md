# Using CSVs in Datasets

# Using CSVs in Datasets

You can upload CSV data to a dataset in Sigma. When you upload a CSV, Sigma stores a copy of the CSV directly in your data warehouse. As such, this functionality must be enabled on both your organization and individual warehouse connection by an organization admin.

## System and user requirements

The ability to upload CSV data to a dataset requires the following:

* The [**CSV upload** feature](/docs/enable-csv-upload) must be enabled for your organization.
* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Upload CSV** permission enabled.
* You must be the dataset owner or be granted **Can edit** [dataset permission](/docs/folder-and-document-permissions).

## CSV data storage

When a CSV file is uploaded to Sigma, its data is **automatically written back to your data warehouse** as a new table. If your organization has multiple warehouses with write access enabled, you will be given the option to select a single destination.

CSV data stored in your warehouse is **only accessible through the dataset created during file upload**. You will not see it listed as a Table in the connection. The CSV dataset can however, be [joined to other data](/docs/join-types) stored in the same warehouse.

> 💡
>
> ### You cannot append additional data to an existing CSV upload. To update the dataset, [replace the CSV data source](#replace-an-existing-csv).

## CSV deletion

If the dataset referencing the uploaded CSV is deleted from Sigma, the associated table created in your warehouse will automatically be removed within 24 hours.

## Create Dataset from a CSV

The following instructions will guide you through uploading a CSV file to create a new dataset.

1. Click **+ Create New** in the left hand navigation panel.
2. Select **Dataset** in the dropdown menu.  
   ![](https://files.readme.io/3a17db6-1.png)

   The data source selection page opens.
3. Select **CSV** as your data source to navigate to the upload page.  
   ![](https://files.readme.io/ebb9e06-2.png)
4. Select a **Connection** from the list provided. The connection you select is the warehouse that your file is uploaded to. If only one data warehouse has write access enabled, it is selected by default.  
   ![](https://files.readme.io/a3c07db-3.png)
5. In the **File Upload** section, upload your CSV file by dragging and dropping it onto the page, or click **Browse**.
6. After adding a CSV, a preview of your data appears. From the preview, you can include or exclude columns, adjust the parsing options, and address any errors if necessary.  
   ![](https://files.readme.io/2261f3c-4.png)
7. Click **Explore** to complete the upload.

## Replace an existing CSV

To replace the underlying CSV in an existing Dataset, do the following:

1. Open the dataset containing the CSV you want to replace.
2. Select the **Worksheet** tab from the dataset header, then click **Edit**.
3. Navigate to the **Data Sources** tab in the right hand panel.
4. Open the ••• menu on the CSV source you would like to replace and click **Replace CSV**.
5. You are prompted to select a file from your computer.
6. After selecting a new CSV, the **Edit Source** page opens. Preview your data and specify parsing options for the file.
7. When you are satisfied with your new CSV data source, click **Done**.

Updated 3 days ago

---

Related resources

* [Enable CSV Upload](/docs/enable-csv-upload)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [CSV data storage](#csv-data-storage)
  + [CSV deletion](#csv-deletion)
  + [Create Dataset from a CSV](#create-dataset-from-a-csv)
  + [Replace an existing CSV](#replace-an-existing-csv)