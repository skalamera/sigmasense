# Export to cloud storage

# Export to cloud storage

If your workbook has elements from a Snowflake or Redshift connection, you can export the data for those elements to cloud storage associated with those connections. Cloud storage is particularly useful for large, multi-GB data exports.

* With a Snowflake connection, you can export to Amazon Simple Storage Service (Amazon S3), Google Cloud Storage (GCS), or Microsoft Azure Blob Storage (Azure).
* With a Redshift connection, you can export to Amazon S3.

Sigma generates exports from the workbook's latest published version. Changes you make to a workbook draft, custom view, or exploration cannot be exported unless you save or publish the changes. Depending on your export destination, you can also choose to export a saved view or tagged version of the workbook. If you are exporting elements that are only on a saved view, you must open the export modal from the saved view.

For a matrix of supported file formats and saved view/version tag export support, see [Available export destinations and formats](/docs/send-or-schedule-workbook-exports#available-export-destinations-and-formats).

## User requirements

The requirements to export workbooks to cloud storage depend on your connection:

### Snowflake connections

* The workbook's data source must originate from a Snowflake connection.
* You must be assigned an [account type](/docs/create-and-manage-account-types) with the **Export to cloud** permission enabled.

### Redshift connections

* Redshift must be configured for your organization. See [Connect to Redshift](/docs/connect-to-redshift).
* The workbook's data source must originate from a Redshift connection.
* You must be assigned an [account type](/docs/create-and-manage-account-types) with the **Export to cloud** permission enabled.
* You must have a Redshift cluster with the data you want to unload.

## Supported file types and export limits

* CSV-formatted files (.csv)
* GZIP compression is supported (.csv.gz)
* File size limit of 5GB. See [Download and export limitations](/docs/download-export-and-upload-limitations).

Exporting version tags and saved views is not supported. Sigma exports from the workbook's published version.

> 🚩
>
> ### Data exported from Sigma is directly unloaded from Snowflake or Redshift to your cloud storage destination as a single file. As a result, the data does not have the same formatting visible in Sigma.
>
> For more information on data unloading in Snowflake, see [Overview of data unloading](https://docs.snowflake.com/en/user-guide/data-unload-overview) in the Snowflake documentation.

## Configure exports to cloud storage

This is a multi-step process. The required steps depend on your connection:

**Snowflake connections**

1. [Configure cloud storage for Snowflake](/docs/export-to-cloud-storage#configure-cloud-storage-for-snowflake)
2. [Format a destination URI](/docs/export-to-cloud-storage#format-a-destination-uri)
3. Export your data as desired:
   * [Send an ad hoc export to cloud storage](/docs/export-to-cloud-storage#send-an-ad-hoc-export-to-cloud-storage)
   * [Schedule a cloud storage export](/docs/export-to-cloud-storage#schedule-a-cloud-storage-export)

**Redshift connections**

1. [Configure cloud storage for Redshift](/docs/export-to-cloud-storage#configure-cloud-storage-for-redshift)
2. [Format a destination URI](/docs/export-to-cloud-storage#format-a-destination-uri)
3. Export your data as desired:
   * [Send an ad hoc export to cloud storage](/docs/export-to-cloud-storage#send-an-ad-hoc-export-to-cloud-storage)
   * [Schedule a cloud storage export](/docs/export-to-cloud-storage#schedule-a-cloud-storage-export)

## Configure cloud storage

### Configure cloud storage for Snowflake

Before you can export to cloud storage from Sigma, you must set up a Snowflake storage integration.

Follow Snowflake’s instructions to create your storage integration. See [CREATE STORAGE INTEGRATION](https://docs.snowflake.com/en/sql-reference/sql/create-storage-integration.html) in the Snowflake documentation, or follow the guide for your cloud storage provider:

* **Amazon S3**: See [Option 1: Configuring a Snowflake storage integration to access Amazon S3](https://docs.snowflake.com/en/user-guide/data-load-s3-config-storage-integration) in the Snowflake documentation.
* **Google Cloud Storage**: See [Configuring an integration for Google Cloud Storage](https://docs.snowflake.com/en/user-guide/data-load-gcs-config) in the Snowflake documentation.
* **Azure**: See [Configuring an Azure container for loading data](https://docs.snowflake.com/en/user-guide/data-load-azure-config) in the Snowflake documentation. Follow the steps for Option 1: Configuring a Snowflake storage integration.

After you set up the storage integration, grant the `USAGE` privilege on the storage integration to the Snowflake role used by your Sigma Snowflake Connection. A Sigma admin can check the role used by the connection in the connection settings. See [Connect to Snowflake](/docs/connect-to-snowflake).

> 📘
>
> ### If no role is specified in your Sigma Snowflake Connection, Snowflake uses a default role.

### Configure cloud storage for Redshift

1. Before you can export to cloud storage from Sigma, you must set up an Amazon S3 bucket to export to. See the AWS documentation on [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html).
2. Grant the appropriate write access permissions for your AWS Identity and Access Management (IAM) role. You need to grant `s3:PutObject` permissions. For more information, see the AWS documentation on [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) and [Adding a bucket policy by using the Amazon S3 console](https://docs.aws.amazon.com/AmazonS3/latest/userguide/add-bucket-policy.html).
3. Verify that you are able to unload data from Redshift to S3 by setting up a test export from Redshift. The export should look something like:

   ```
   unload ('select * from venue')   
   to 's3://amzn-s3-demo-bucket/tickit/unload/venue_' 
   iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole';
   ```

   For more information on this command, see the AWS documentation on [Unloading data from Amazon S3](https://docs.aws.amazon.com/redshift/latest/dg/t_Unloading_tables.html).

## Format a destination URI

For both Snowflake and Redshift connections, the destination URI represents the target file path for your export in your cloud storage service.

Use the following template to format your URI:

`<schema>://<bucket>/<filepath>/<filename><filetype><compression>`

Where:

* **Schema**: The export destination. Specify “s3” if exporting to AWS S3, “gcs” if exporting to GCS, and "azure" if exporting to Azure.
* **Bucket**: The highest level storage object supported by the cloud storage provider. Your S3 bucket, GCS bucket, or Azure container.
* **File path** (optional): Target subdirectories in the bucket or container. If you do not specify a file path, exported files are added directly to the root.
* **File name**: A file name to use for the exported file.
* **File type**: The file format for the exported file. Must be `.csv`.
* **Compression** (optional): A compression option for the exported file. Can only be `.gz`.

### Example URI

`s3://my-sigma-bucket/cloud-exports/sales.csv.gz`

If your URI is identical to an existing file in the bucket, the existing file is overwritten.

## Send an ad hoc export to cloud storage

1. From the workbook menu (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)), select **Share and export> Export...**.

   > 📘
   >
   > ### If the **Cloud Storage** option is not available, the workbook is in **Edit** mode. Either publish your draft or return to the latest published or tagged version of the workbook before attempting to export.
2. Select **Cloud storage**.
3. From the **Element** menu, select the workbook element to export.
4. Enter your cloud storage information:

   * For Snowflake:
     + For **Storage integration**, enter the name of your Snowflake Storage Integration. See [Configure cloud storage](#configure-cloud-storage) on this page.
     + For **Cloud storage URI**, enter the destination URI. For guidance formatting the URI, see [Format a destination URI](#format-a-destination-uri).
   * For Redshift:
     + For **IAM role**, enter your AWS Identity and Access Management role.
     + For **Cloud storage URI**, enter the destination URI. For guidance formatting the URI, see [Format a destination URI](#format-a-destination-uri).
5. For the specified element, select a file format. You can choose from CSV or CSV, gzipped.
6. Click **Export**.  
   Sigma sends an export confirmation message to your email address.

## Schedule a cloud storage export

1. From the workbook menu (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)), select **Share and export> Schedule exports...**.
2. If this is the first schedule for the workbook, click **Add schedule**, otherwise click **+ New schedule**.
3. Select **Cloud storage**.
4. From the **Element** menu, select the workbook element to export.
5. Enter your cloud storage information:

   * For Snowflake:
     + For **Storage integration**, enter the name of your Snowflake Storage Integration. See [Configure cloud storage](#configure-cloud-storage) on this page.
     + For **Cloud storage URI**, enter the destination URI. For guidance formatting the URI, see [Format a destination URI](#format-a-destination-uri).
   * For Redshift:
     + For **IAM role**, enter your AWS Identity and Access Management role.
     + For **Cloud storage URI**, enter the destination URI. For guidance formatting the URI, see [Format a destination URI](#format-a-destination-uri).
6. For the specified element, select a file format. You can choose from CSV or CSV, gzipped.
7. (Optional) Select the checkbox for **Prefix file name with the current date and time**.

   > 🚩
   >
   > ### If you do not select this option, the same file name is used for each scheduled export and the file is overwritten every time the export runs.
8. In the **Frequency** section, set the delivery schedule:

   * (Optional) Select the dropdown for **Daily** and select **Weekly**, **Monthly**, or **Custom**.

     + For **Daily**, select **Once a day** or **Multiple times**.
     + For **Weekly**, select which days of the week to send an email, and choose between **Once a day** or **Multiple times**.
     + For **Monthly**, select which day of the month to send an email, and the time of day.
     + For **Custom**, specify a schedule using cron syntax. See [Set up a custom delivery schedule](/docs/configure-additional-options-for-exports#set-up-a-custom-delivery-schedule).

       If you select **Multiple times**, specify the frequency. For example, every 2 hours on the :15 of the hour between 9 AM and 6 PM.

       > 📘
       >
       > If you don't have the option to set a specific frequency, export frequency might be restricted for your organization. For more details, see [Restrict export recipients and frequency](/docs/restrict-export-recipients).
   * (Optional) Adjust the default schedule time zone using the dropdown menu.
   * (Optional) Choose how often to send the export: **Always** or only **If a condition is met**. See [Schedule a conditional export or alert](/docs/schedule-a-conditional-export-or-alert).

     + (Optional) If you choose to send an export only **If a condition is met**, you can turn on the switch to stop notifying after a set number of occurrences per day, week, or in total. (This feature is in beta and subject to the [Beta features notice](/docs/sigma-product-releases#beta-features)).
9. (Optional) Select the checkbox for **Customize control values** to filter the exported data according to the value of one or more workbook controls. See [Configure additional options for exports](/docs/configure-additional-options-for-exports).
10. Click **Create**.

Updated 3 days ago

---

Related resources

* [Schedule exports using conditions](/docs/schedule-exports-using-conditions)
* [Send and schedule exports from workbooks](/docs/send-and-schedule-exports-from-workbooks)
* [Connect to Snowflake](/docs/connect-to-snowflake)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + - [Snowflake connections](#snowflake-connections)
    - [Redshift connections](#redshift-connections)
  + [Supported file types and export limits](#supported-file-types-and-export-limits)
  + [Configure exports to cloud storage](#configure-exports-to-cloud-storage)
  + [Configure cloud storage](#configure-cloud-storage)
  + - [Configure cloud storage for Snowflake](#configure-cloud-storage-for-snowflake)
    - [Configure cloud storage for Redshift](#configure-cloud-storage-for-redshift)
  + [Format a destination URI](#format-a-destination-uri)
  + - [Example URI](#example-uri)
  + [Send an ad hoc export to cloud storage](#send-an-ad-hoc-export-to-cloud-storage)
  + [Schedule a cloud storage export](#schedule-a-cloud-storage-export)