# Enable or disable audit logging

# Enable or disable audit logging

Sigma facilitates audit logging through the *Sigma Audit Logs* connection, which records data related to user-initiated events that occur within your Sigma organization. The connection is disabled by default, but an **Admin** user can enable it in the **Administration** portal.

This document explains how to enable or disable the *Sigma Audit Logs* connection. For more information about audit logging with Sigma, see the following:

* [Access and explore audit logs](/docs/access-and-explore-audit-logs)
* [Audit log events and metadata](/docs/audit-log-events-and-metadata)
* [Create an audit logs storage integration](/docs/create-an-audit-logs-storage-integration)
* [Export audit log data to cloud storage](/docs/export-audit-log-data-to-cloud-storage)

## User requirements

> 📘
>
> This feature isn't supported in all regions. To check if it is supported in your region, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

These regions are currently supported for audit logging:

| Provider | Region |
| --- | --- |
| AWS | * US East 1 * US West 2 * CA Central 1 * AP Southeast 2 * EU Central 1 * UK |
| Azure | * East US 2 * Canada Central |
| GCP | * US Central 1 |

To enable the *Sigma Audit Logs* connection, you must be assigned the **Admin** account type.

## Enable the Sigma Audit Log connection

1. Go to **Administration** > **Account** > **General Settings**.

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Account**, then open the **General Settings** tab.
2. In the **Audit Logging** section, locate the **Sigma Audit Logs** setting and click **Enable**. The setting displays a **Feature Pending** tag while the audit log connection activates.

   > 📘
   >
   > If the **General Settings** tab doesn’t include an **Audit Logging** section, contact Sigma Support or your Sigma Account Executive to enable it for your organization.
3. The connection typically activates within a few minutes, and Sigma sends a confirmation email when the connection is successfully enabled. Click **Open in Sigma** in the email or refresh the **Administration** portal, then click **Browse Connection** in the **Sigma Audit Logs** setting to view the connection data.

## Disable the Sigma Audit Log connection

You can disable audit logging for your Sigma organization. If you wish to re-enable your audit logs, Sigma stores your data related to user-initiated events captured before you disabled audit logging for 30 days. If you re-enable audit logging you can recover that data, but you will need to reconfigure any:

* Storage integrations
* Scheduled exports

> 📘
>
> Sigma tracks which user disabled auto logging.

1. Go to **Administration** > **Account** > **General Settings**.

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Account**, then open the **General Settings** tab.
2. In the **Audit Logging** section, locate the **Sigma Audit Logs** setting and click **Disable**.
3. (Optional) Select the **view exports** option to access the **Exports** > **Scheduled exports** page and review any scheduled exports for your storage integration.
4. (Optional) Select the **view elements** option to access the **Lineage** tab of your audit logs in the connections browser so you can review any Sigma elements that utilize your audit logs prior to disabling.
5. Select **Disable audit logging**. The setting displays a **Disabling** tag while the audit log connection deactivates.

Updated 3 days ago

---

Related resources

* [Access and explore audit logs](/docs/access-and-explore-audit-logs)
* [Audit log events and metadata](/docs/audit-log-events-and-metadata)
* [Create an audit logs storage integration](/docs/create-an-audit-logs-storage-integration)
* [Export audit log data to cloud storage](/docs/export-audit-log-data-to-cloud-storage)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Enable the Sigma Audit Log connection](#enable-the-sigma-audit-log-connection)
  + [Disable the Sigma Audit Log connection](#disable-the-sigma-audit-log-connection)