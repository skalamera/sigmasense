# Troubleshoot input table connection issues

# Troubleshoot input table connection issues

When you encounter an input table error (as a general user) or receive a system email notifying you of failed input table edits (as an admin), it can be the result of a configuration or availability issue in your connection or data platform. This type of issue must be resolved by an admin within Sigma or directly in the data platform.

This document explains how Sigma handles input table errors resulting from configuration and availability issues and provides guidance on troubleshooting and resolving these errors.

## User requirements

The ability to resolve an input table issue identified in this document requires the following:

* You must be assigned the **Admin** [account type](/docs/create-and-manage-account-types).
* You must have the necessary privileges in the data platform to perform the resolution tasks identified in this document.

If you don't meet these requirements, contact your Sigma or data platform administrator to resolve the issue.

## Input table error handling

To improve data integrity and prevent unexpected data loss, Sigma handles input table errors as follows:

* When an input table edit is unsuccessful due to configuration or availability issues in the connection or data platform, Sigma treats it as a fatal error and does not retry the operation. The underlying issue is not recoverable by Sigma, therefore, retrying the operation would continue to fail.
* An input table error resulting from a configuration or availability issue in the connection or data platform can apply to specific users or the entire organization. When Sigma detects this type of issue, it temporarily restricts the ability for affected users to create and edit input tables that are subject to the same error. Following the initial input table error, all relevant existing input table elements display an “Editing restricted” message.
* Sigma sends admins an email alert that identifies the misconfigured or unavailable connection, displays the error message, and links to this document.

## Troubleshooting steps

Complete the following steps to troubleshoot the error.

1. Review the organization and connection identified in the system email. This is important if you manage multiple organizations or connections.
2. Check the error message identified in the system email.
3. Locate the error message in the [Error messages and resolutions](#error-messages-and-resolutions) tables. If you cannot find the applicable error message, [contact Support](/docs/sigma-support).
4. Review the root cause, then complete the resolution provided for the authentication method configured on your connection.

## Error messages and resolutions

This section provides details about known configuration and availability errors specific to Databricks, Redshift, and Snowflake. If you encounter an error message that's not included in the following tables, [contact Support](/docs/sigma-support).

* [Databricks errors](#databricks-errors)
* [Redshift errors](#redshift-errors)
* [Snowflake errors](#snowflake-errors)

### Databricks errors

#### Insufficient privileges

|  |  |
| --- | --- |
| Error message | `execution error: failed to execute query: unexpected operation state ERROR_STATE: [INSUFFICIENT_PERMISSIONS] Insufficient privileges: User does not have <REQUIRED_PRIVILEGE> on <OBJECT_TYPE><OBJECT_NAME>. SQLSTATE: 42501` |
| Root cause | The service principal doesn't have the privilege required to perform the identified operation |
| Resolution | Refer to [Show, grant, and revoke privileges](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/?language=Catalog%C2%A0Explorer#show-grant-and-revoke-privileges) in the Databricks documentation to ensure that the service principal used for your connection is granted the required catalog and schema privileges.  For information about the required privileges, see [Configure Databricks](/docs/connect-to-databricks#configure-databricks). |

#### Invalid or expired access token

|  |  |
| --- | --- |
| Error message | `Databricks access token is invalid or expired.`  or `Invalid Databricks access token.` |
| Root cause | The access token provided in the connection configuration could not be used for authentication.  Possible causes:   * The token provided contains a typo. * An incorrect token was provided. * The token has been deleted or revoked. * The token has expired. |
| Resolution (non-OAuth) | In Sigma, go to the connection configuration page and enter a valid token in the **Connection Credentials** > **Access token** field.  If the access token has expired or been deleted or revoked, refer to [Databricks personal access tokens for workspace users](https://docs.databricks.com/aws/en/dev-tools/auth/pat#databricks-personal-access-tokens-for-workspace-users) in the Databricks documentation to generate a new one.  For more information about access token requirements, see [Specify your connection credentials](/docs/connect-to-databricks#specify-your-connection-credentials) . |
| Resolution (OAuth) | In Sigma, go to the connection configuration page and enter a valid token in the **Service Account Configuration** > **Access token** field.  If the access token has expired or been deleted or revoked, refer to [Databricks personal access tokens for service principals](https://docs.databricks.com/aws/en/dev-tools/auth/pat#databricks-personal-access-tokens-for-service-principals) in the Databricks documentation to generate a new one.  For more information about access token requirements, see [Configure OAuth features](/docs/connect-to-databricks#configure-oauth-features). |

### Redshift errors

#### Case sensitivity enabled

|  |  |
| --- | --- |
| Error message | `enable_case_sensitive_identifier must be off` |
| Root cause | The `enable_case_sensitive_identifier` configuration value in Redshift is set to `true`, causing input table edits to fail. |
| Resolution | In Redshift, set the `enable_case_sensitive_identifier` to `false`.  For more information about the configuration value, see [enable\_case\_sensitive\_identifier](https://docs.aws.amazon.com/redshift/latest/dg/r_enable_case_sensitive_identifier.html) in the Redshift documentation. |

### Snowflake errors

#### Role not found

|  |  |
| --- | --- |
| Error message | `Role does not exist` |
| Root cause | The role provided in the connection configuration cannot be found in your Snowflake environment.  Possible causes:   * The role provided contains a typo or case sensitivity issue. * The role was deleted in Snowflake. |
| Resolution (non-OAuth) | In Sigma, go to the connection configuration page and verify that the role name is entered correctly in the **Connection Credentials** > **Role** field.  If the role was deleted, refer to [Create a role](https://docs.snowflake.com/en/user-guide/security-access-control-configure#create-a-role) in the Snowflake documentation to recreate it (you cannot recover a deleted role).  For more information about setting a role in the connection configuration, see [Connect to Snowflake with key pair authentication](/docs/connect-to-snowflake#connect-to-snowflake-with-key-pair-authentication) or [Connect to Snowflake with basic authentication](/docs/connect-to-snowflake#connect-to-snowflake-with-basic-authentication). |
| Resolution (OAuth) | In Sigma, go to the connection configuration page and verify that the role name is entered correctly in the **Service Account Configuration** > **Role** field.  If the role was deleted, refer to [Create a role](https://docs.snowflake.com/en/user-guide/security-access-control-configure#create-a-role) in the Snowflake documentation to recreate it (you cannot recover a deleted role).  For more information about setting a role in the connection configuration, see [Connect to Snowflake with OAuth](/docs/connect-to-snowflake#connect-to-snowflake-with-oauth). |

#### Cannot access warehouse

|  |  |
| --- | --- |
| Error message | `000606 (57P03): No active warehouse selected in the current session. Select an active warehouse with the 'use warehouse' command.` |
| Root cause | The connection cannot access a warehouse.  Possible cause: The warehouse is set using a user attribute that's invalid or has no value assigned to the user. |
| Resolution (non-OAuth) | In Sigma, go to the connection configuration page and verify that the user attribute name used to set the warehouse is entered correctly in the **Connection Credentials** > **Warehouse** field.  If the user attribute name provided is valid, see [Configure user attributes on a Snowflake connection](/docs/configure-user-attributes-on-a-snowflake-connection) to ensure that the user is assigned a warehouse attribute. |
| Resolution (OAuth) | In Sigma, go to the connection configuration page and verify that the user attribute name used to set the warehouse is entered correctly in the **Connection Credentials** > **Warehouse** field.  If the user attribute name provided is valid, see [Configure user attributes on a Snowflake connection](/docs/configure-user-attributes-on-a-snowflake-connection) to ensure that the user is assigned a warehouse attribute. |

#### Cannot access tables

|  |  |
| --- | --- |
| Error message | `002003 (42S02): SQL compilation error: Object <OBJECT_NAME> does not exist or not authorized.` |
| Root cause | The connection cannot access tables containing input table data and the edit log.  Possible causes:   * The role provided doesn't have the Snowflake privileges required to access the identified table. * The table was deleted or moved. |
| Resolution | See [Restore input table access for a Snowflake connection or user](/docs/restore-input-table-access-for-a-snowflake-connection-or-user). |

#### Insufficient role privileges

|  |  |
| --- | --- |
| Error message | `003001 (42501): SQL access control error: Insufficient privileges to operate on schema <SCHEMA_NAME>` |
| Root cause | The role provided in the connection configuration doesn't have the Snowflake privileges required to perform the operation on the identified schema. |
| Resolution | Refer to [Grant privileges to a role](https://docs.snowflake.com/en/user-guide/security-access-control-configure#grant-privileges-to-a-role) in the Snowflake documentation to grant the required privileges to the role.  For more information about the schema privileges required to correctly configure write access, see [Configure write access](/docs/connect-to-snowflake#configure-write-access). |

#### User access disabled

|  |  |
| --- | --- |
| Error message | `390101 (08004): User access disabled. Contact your local system administrator.` |
| Root cause | The username and password provided in the connection configuration has been changed or disabled. |
| Resolution (non-OAuth) | In Sigma, go to the connection configuration page and update the **User** and **Password** fields (or **User**, **Private key**, and **Private key passphrase** if the connection uses key pair authentication) in the **Connection Credentials** section.  Alternatively, refer to [Disabling or enabling a user](https://docs.snowflake.com/en/user-guide/admin-user-management#disabling-or-enabling-a-user) in the Snowflake documentation to re-enable the user. |

Updated 3 days ago

---

[Troubleshoot your connection](/docs/troubleshoot-your-connection)[Get started with data modeling](/docs/get-started-with-data-modeling)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Input table error handling](#input-table-error-handling)
  + [Troubleshooting steps](#troubleshooting-steps)
  + [Error messages and resolutions](#error-messages-and-resolutions)
  + - [Databricks errors](#databricks-errors)
    - [Redshift errors](#redshift-errors)
    - [Snowflake errors](#snowflake-errors)