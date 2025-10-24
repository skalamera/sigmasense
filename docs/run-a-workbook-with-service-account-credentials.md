# Run a workbook with service account credentials

# Run a workbook with service account credentials

On workbooks created with data from an OAuth connection with a service account, an admin can configure the workbook to run queries using the service account instead of each user’s OAuth credentials.

OAuth tokens can expire if the owner goes a significant amount of time without logging in to Sigma. If this happens, scheduled exports and materialization schedules configured by that user fail. This limitation can be avoided by running the workbook with service account credentials.

This setting changes how Sigma queries data and evaluates permissions for the workbook. Refer to the following table to compare the behavior:

| Workbook connections | Is **Run as service account** configured? | How Sigma queries data and evaluates permissions |
| --- | --- | --- |
| Workbook using a non-OAuth connection. | N/A | Sigma evaluates the workbook owner's  [permission to the source data](/docs/data-permissions-overview)  and then runs queries using the user account credentials set in the connection settings. |
| Workbook using an OAuth connection. | Yes | Sigma queries the published version of the workbook using the data connection’s service account credentials whenever it is viewed from within Sigma or run as part of a scheduled report. This ensures that any user with  [permissions](/docs/data-permissions-overview)  on a workbook can view it, regardless of their permissions in the cloud data warehouse. |
| Workbook using an OAuth connection. | No | Sigma always runs queries with the organization member's OAuth credentials. This includes when users are viewing workbooks owned by others. |
| Workbook using some data from an OAuth connection and other data from a non-OAuth connection. | Yes | For the data from the OAuth connection, Sigma queries the published version of the workbook using the data connection’s service account credentials whenever it is viewed from within Sigma or run as part of a scheduled report. This ensures that any user with permissions on a workbook can view it, regardless of their permissions in the cloud data warehouse.  For the data from the non-OAuth connection, Sigma evaluates the workbook owner's permission to the source data and then runs queries using the user account credentials set in the connection settings. |
| Workbook using some data from an OAuth connection and other data from a non-OAuth connection | No | For data from the OAuth connection, Sigma always runs queries with the user's OAuth credentials using the permissions configured in the IdP. This includes when users are viewing workbooks owned by others.  For the data from the non-OAuth connection, Sigma evaluates the workbook owner's permission to the source data and then runs queries using the user account credentials set in the connection settings. |
| Workbook using data from two different OAuth connections with different OAuth configurations. | Yes | Sigma queries the published version of the workbook using each data connection’s service account credentials whenever it is viewed from within Sigma or run as part of a scheduled report. This ensures that any user with permissions on a workbook can view it, regardless of their permissions in the cloud data warehouse. |
| Workbook using data from two different OAuth connections with different OAuth configurations. | No | Sigma always runs queries with the user's OAuth credentials as they are configured for each connection, using the permissions configured in the IdP. This includes when users are viewing workbooks owned by others. |

## Requirements

* To configure this setting on a workbook, you must be assigned the **Admin** [account type](/docs/user-account-types).
* The **Run as service account** option is only available on workbooks that use an OAuth connection that meets the following criteria:
  + A service account has been configured for the OAuth connection.
  + OAuth is configured at the organization level. (This feature is not available for connections with independent OAuth.)
    For information on how to configure a connection with a service account, see the documentation for your connection type:
  + [Connect to Snowflake](/docs/connect-to-snowflake#connect-to-snowflake-with-oauth)
  + [Connect to Databricks](/docs/connect-to-databricks#configure-oauth-features)

## Run an individual workbook as a service account

1. Open the workbook in Published mode.
2. Click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the workbook menu.
3. Select **Share…**.
4. Turn on the toggle next to **Run as service account**.

Updated 3 days ago

---

[Configure OAuth with write access](/docs/configure-oauth-with-write-access)[Dynamically assign roles used by a connection](/docs/dynamically-assign-roles-used-by-a-connection)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Run an individual workbook as a service account](#run-an-individual-workbook-as-a-service-account)