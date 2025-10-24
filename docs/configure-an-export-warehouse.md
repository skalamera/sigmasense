# Configure an export warehouse

# Configure an export warehouse

An export warehouse is a virtual warehouse in Snowflake created specifically for running Sigma exports.

By default, Sigma sends export queries to your connection’s primary warehouse, but you can configure it to run all scheduled, direct, and on-demand exports through a separate export warehouse. This practice isolates export operations to optimize performance and reduce computing costs.

This document explains how to configure an export warehouse in Sigma.

## System and user requirements

The ability to configure an export warehouse in Sigma requires the following:

* Your Sigma organization must have an existing [Snowflake connection](/docs/connect-to-snowflake).
* You must be assigned the **Admin** [account type](/docs/user-account-types).

## Prerequisites

Before you configure an export warehouse in Sigma, you (or another user with appropriate Snowflake permissions) must create a separate virtual warehouse dedicated to running export queries in Snowflake. For more information about this process, see [CREATE WAREHOUSE](https://docs.snowflake.com/en/sql-reference/sql/create-warehouse) in Snowflake’s documentation.

## Configure an export warehouse

Enable Sigma to use the dedicated export warehouse by configuring your Snowflake connection accordingly.

1. Go to **Administration** > **Connections**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Connections**.
2. In the **Connections** page, select the Snowflake connection to which you want to add an export warehouse.
3. In the connection overview, go to the **Connection Details** section and click **Edit**.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/configure-export-warehouse/connection-details_edit.png)
4. In the **Connection Features** section, locate the **Export Warehouse** field and enter the name of the virtual warehouse created for export queries.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/configure-export-warehouse/connection-features_add-export-warehouse.png)
5. Click **Save** to run all scheduled, direct, and on-demand exports through the specified warehouse.

   > 📘
   >
   > ### The export warehouse inherits the primary warehouse’s connection queue size. To set a different queue size for the export warehouse, contact [Support](/docs/sigma-support).

Updated 3 days ago

---

[Connect to Snowflake](/docs/connect-to-snowflake)[Restore input table access for a Snowflake connection or user](/docs/restore-input-table-access-for-a-snowflake-connection-or-user)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Prerequisites](#prerequisites)
  + [Configure an export warehouse](#configure-an-export-warehouse)