# Access and explore audit logs

# Access and explore audit logs

Sigma's audit log feature is facilitated by a Sigma-managed connection that provides data related to user-initiated events that occur within your Sigma organization. Access the audit log to troubleshoot issues or monitor user activity for security and compliance purposes. You can also explore the audit log in a workbook to analyze how users across your organization utilize Sigma.

This document explains how to access the *Sigma Audit Logs* connection and open the data in a workbook. For more information about audit logging with Sigma, see the following:

* [Enable or disable audit logging](/docs/enable-audit-logging)
* [Audit log events and metadata](/docs/audit-log-events-and-metadata)
* [Create an audit logs storage integration](/docs/create-an-audit-logs-storage-integration)
* [Export audit log data to cloud storage](/docs/export-audit-log-data-to-cloud-storage)

## User requirements

By default, the *Sigma Audit Logs* connection is accessible to **Admin** users only. If you're assigned a different account type, you or your team must be granted access to the **Sigma Audit Logs** connection. See [Manage access to data and connections](/docs/manage-data-permissions) for instructions.

## Access and explore the audit log

1. Go to your **Home** page.
2. In the navigation menu, select the *Sigma Audit Logs* connection.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/Audit+Log/audit-log_side-nav_select-connection.png)

   If your organization has more than three connections, Sigma consolidates them in a **Connections** page. In the navigation menu, first click **Connections** to open the page, then select the *Sigma Audit Logs* connection.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/Audit+Log/audit-log_connections-page_select-connection.png)
3. In the connection browser, select the *AUDIT\_LOGS* table to view all audit log entries.

   > 🚧
   >
   > ### Real-time user events may take several minutes (up to 1 hour) to appear in the audit log.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/Audit+Log/audit-log_view-entries.png)
4. To open the audit log data in a workbook, click **Explore** in the connection header.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/Audit+Log/audit-log_explore.png)

   A new workbook opens with an *AUDIT\_LOGS* table containing all entries and metadata. You can now explore, analyze, and share audit log data as needed.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/Audit+Log/audit-log_new-exploration.png)

  

## Service Level Indicators

* **Freshness**: Fresh event data is available within an hour 99.9% of the time.
* **Delivery**: New audit log events are available at least once 99.9% of the time.

## Frequently Asked Questions

How much historical data is stored in the audit log?

The audit log begins logging event entries when the **Sigma Audit Log** connection is enabled for your organization. Entries are then stored for 30 days.

My organization just enabled the audit log, but we want data from the past several months. Can the audit log retroactively record events that predate enablement?

No, the audit log can only reflect events that occur after the **Sigma Audit Log** connection is enabled.

My business requires more than 30 days of audit log data. Can it be customized to store entries for a longer period of time?

No, the audit log can currently store entries for 30 days only. If you need to retain entries for an extended period of time, Sigma recommends saving the **AUDIT\_LOGS** table as a workbook and scheduling exports to a cloud-based storage service. When you do, select the checkbox to **Prefix file name with the current date and time** to ensure each point-in-time record is saved as a new file. For more details about exporting your audit log data, see [Export to cloud storage](/docs/export-a-workbook-to-cloud-storage).

Updated 3 days ago

---

Related resources

* [Audit log events and metadata](/docs/audit-log-events-and-metadata)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Access and explore the audit log](#access-and-explore-the-audit-log)
  + [Service Level Indicators](#service-level-indicators)
  + [Frequently Asked Questions](#frequently-asked-questions)