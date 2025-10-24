# Export audit log data to cloud storage

# Export audit log data to cloud storage

Sigma enables you to export your audit log data to cloud storage to comply with security, regulatory, and operational requirements.

This document explains how to configure a recurring export to cloud storage using an existing audit log storage integration. For more information about audit logging with Sigma, see the following:

* [Enable or disable audit logging](/docs/enable-audit-logging)
* [Access and explore audit logs](/docs/access-and-explore-audit-logs)
* [Audit log events and metadata](/docs/audit-log-events-and-metadata)
* [Create an audit logs storage integration](/docs/create-an-audit-logs-storage-integration)

## System and user requirements

The ability to schedule an audit log export to cloud storage requires the following:

* Your organization must have an existing [audit log storage integration](/docs/create-an-audit-logs-storage-integration).
* You must be assigned the **Admin** account type or be granted access to the *Sigma Audit Logs* connection.

## Export audit log data to cloud storage

To configure an audit log export to cloud storage, you must complete the following procedures:

* [Retrieve the storage integration name](#retrieve-the-storage-integration-name)
* [Save the audit log data in a workbook](#save-the-audit-log-data-in-a-workbook)
* [Create and test a scheduled export](#create-and-test-a-scheduled-export)

> 📘
>
> ### If you update or delete your audit log storage integration destination, new exports will be paused by default.

### Retrieve the storage integration name

The name of the audit logs storage integration is required when you [create a scheduled export](#create-and-test-a-scheduled-export). The following steps explain how to retrieve this detail in the **Administration** portal.

If you don’t have access to the **Administration** portal, request the integration name from a user assigned the **Admin** account type.

1. Go to **Administration** > **Account** > **General Settings**.

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Account**, then open the **General Settings** tab.
2. In the **Audit Logging** section, go to the **Create an Audit Logs Storage Integration** setting, then locate the applicable integration and click **View credentials**.

   ![](https://files.readme.io/0269d8efab6f2c0ffbe1129a5afe83649f91a24d5c05e4f25910322d860b3441-browseconnection.png)
3. Reference the **Cloud storage credentials** section and record the **Integration name** value.

### Save the audit log data in a workbook

Scheduled exports can only be configured for saved workbooks. The following steps explain how to access your audit log data and save it in a workbook.

1. Go to your **Home** page.
2. In the navigation menu, select the *Sigma Audit Logs* connection.

   If your organization has more than three connections, Sigma consolidates them in a **Connections** page. In the navigation menu, first click **Connections** to open the page, then select the *Sigma Audit Logs* connection.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/Export+audit+log+data+to+cloud+storage/export-audit-log_select-connection.png)
3. In the connection browser, select the *AUDIT\_LOGS* table, then click **Explore** to open the audit log data as a table element in an exploration.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/Export+audit+log+data+to+cloud+storage/export-audit-log_explore-data.png)
4. In the exploration header, click **Save As** to save the exploration as a workbook.
5. In the **Save as** modal, enter a name and destination for the workbook, then click **Save**.

### Create and test a scheduled export

With the storage integration name available and the audit log data saved in a workbook, you can now create a scheduled export. The following steps explain how to configure and test a recurring export using the [audit log storage integration](/docs/create-an-audit-logs-storage-integration).

1. Open the workbook containing the audit log data.
2. In the header, click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) next to the workbook title to open the workbook menu, then click **Schedule exports**.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/Export+audit+log+data+to+cloud+storage/export-audit-log_wb-menu_schedule-exports.png)
3. In the **Schedule Exports** modal, click **Add Schedule**, then configure the recurring cloud storage export.

   1. In the **Destination** section, select the **Cloud Storage** option.
   2. In the **Storage Integration** field, enter the **Integration name** value [retrieved from the integration credentials](#retrieve-the-storage-integration-name).
   3. In the **Destination Cloud Storage URI** field, enter the destination file path. This value should include the bucket or container name, the folder path prefix (if applicable), and the file name.
   4. In the **Element** dropdown, select the table element referencing the audit log data you want to export (named *AUDIT\_LOGS* by default).
   5. Select the option to **Prefix file name with the current date and time**.
   6. Customize the remaining fields in the **Schedule Exports** modal as needed, then click **Create**.
4. When the new schedule is successfully created, the **Schedule Exports** modal displays the schedule summary. To test the scheduled export, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **Actions** and select **Send now**.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/Export+audit+log+data+to+cloud+storage/export-audit-log_schedule_send-now.png)

   If the export succeeds, the data is uploaded to and viewable in your cloud storage console. If the export fails, Sigma sends an email notification containing the error message received from the cloud storage platform. Modify the scheduled export configurations or the storage integration as needed, then run the export test again.

Updated 3 days ago

---

Related resources

* [Enable or disable audit logging](/docs/enable-audit-logging)
* [Access and explore audit logs](/docs/access-and-explore-audit-logs)
* [Audit log events and metadata](/docs/audit-log-events-and-metadata)
* [Create an audit logs storage integration](/docs/create-an-audit-logs-storage-integration)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Export audit log data to cloud storage](#export-audit-log-data-to-cloud-storage)
  + - [Retrieve the storage integration name](#retrieve-the-storage-integration-name)
    - [Save the audit log data in a workbook](#save-the-audit-log-data-in-a-workbook)
    - [Create and test a scheduled export](#create-and-test-a-scheduled-export)