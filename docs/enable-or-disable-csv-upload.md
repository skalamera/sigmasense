# Enable or disable CSV upload

# Enable or disable CSV upload

Enable or disable CSV uploads to allow or restrict users from writing CSV data to connected data platforms. If your organization is connected to Snowflake and you enable CSV upload, you can also choose to use internal or external stages to temporarily store CSV files.

This document explains how to set the organization-wide settings for CSV uploads. For information about how to upload CSV files, see [Upload CSV data](/docs/upload-csv-data).

## User requirements

To enable or disable CSV upload for your organization, you must be assigned the **Admin** [account type](/docs/user-account-types).

For information about user requirements to upload CSV files, see [Upload CSV data](/docs/upload-csv-data).

> 📘
>
> ### CSV upload is only supported by connections with [write access](/docs/set-up-write-access) enabled. If the **CSV Upload** setting for your organization is turned on, but the connection a user wants to upload CSV data to does not have write access, the user will not be able to upload the CSV file.

## Where is uploaded CSV data stored?

When a user uploads a CSV file to Sigma, the data in the file is automatically written to the data platform as a new table in the schema used for write-back. If your organization uses multiple connections with write access enabled, users with access to more than one are required to choose the connection to write the CSV data to.

If a user uploads a CSV file to a workbook, the data is only accessible from that specific Sigma workbook using the CSV file. Users cannot see the table created from the CSV upload when browsing the connection's data catalog. If a user deletes the workbook, the data from the CSV file is no longer accessible.

## Enable or disable CSV upload

Enable or disable the ability to upload CSV files. This setting only affects connections with write access enabled. Any connection that does not have write access cannot support CSV upload.

1. Open the **Administrator** portal.
2. In the side panel, select **Account**.
3. In the **Features** section, enable or disable the **CSV Upload** setting:

   * To enable CSV uploads, turn on the **CSV Upload** toggle.

     Users can immediately upload CSV files using connections with write access enabled.
   * To disable CSV uploads, turn off the **CSV Upload** toggle.

     Users are immediately prevented from uploading CSV files using any connection.

## Enable internal or external stages for CSV uploads (Snowflake)

If your organization is connected to Snowflake, you can elect to import CSV files to Snowflake via internal or external stages after the files are processed in Sigma's infrastructure. This accommodates Snowflake accounts with `REQUIRE_STORAGE_INTEGRATION_FOR_STAGE_CREATION` set to `true`.

1. Open the **Administrator** portal.
2. In the side panel, select **Account**.
3. In the **Features** section, set the **Internal stages** setting (displayed only when the **CSV Upload** toggle is turned on):

   * To use internal stages to temporarily store CSV files, turn on the **Internal stages** toggle.
   * To use external stages to temporarily store CSV files, turn off the **Internal stages** toggle.
4. Refer to the following Snowflake documentation for information about Snowflake's implementation of the temporary storage of CSV files in internal and external stages.

   * [Bulk loading from a local file system](https://docs.snowflake.com/en/user-guide/data-load-local-file-system) (internal)
   * [Bulk loading from Amazon S3](https://docs.snowflake.com/en/user-guide/data-load-s3) (external)
   * [Bulk loading from Google Cloud Storage](https://docs.snowflake.com/en/user-guide/data-load-gcs) (external)
   * [Bulk loading from Microsoft Azure](https://docs.snowflake.com/en/user-guide/data-load-azure) (external)

Updated 3 days ago

---

Related resources

* [Upload CSVs](/docs/upload-csvs)
* [Set up write access](/docs/set-up-write-access)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Where is uploaded CSV data stored?](#where-is-uploaded-csv-data-stored)
  + [Enable or disable CSV upload](#enable-or-disable-csv-upload)
  + [Enable internal or external stages for CSV uploads (Snowflake)](#enable-internal-or-external-stages-for-csv-uploads-snowflake)