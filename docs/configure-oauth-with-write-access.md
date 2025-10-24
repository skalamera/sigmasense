# Configure OAuth with write access

# Configure OAuth with write access

Sigma allows you to leverage the benefits of OAuth permission management with write-access features like [input tables](/docs/intro-to-input-tables), [warehouse views](/docs/create-and-manage-workbook-warehouse-views), [workbook and data model materializations](/docs/materialization#create-materializations-in-workbooks), and [CSV uploads](/docs/upload-csvs).

This document explains how to configure an OAuth connection to enable secure and efficient write-back workflows for Sigma objects (created or edited using write access features). For more information about OAuth and general usage, see [Configure OAuth](/docs/configure-oauth).

> 📘
>
> ### By design, the destination that you configure for write access is not visible in the Sigma connection explorer pane. The data that Sigma writes to this destination is not formatted in a way that can be browsed and used. Configure a separate database or a database and schema combination for write-access purposes.

## System and user requirements

The ability to configure an OAuth connection with write access requires the following:

* You must be assigned the **Admin** [account type](/docs/user-account-types).
* You must be able to provide the schema paths of all write destinations to be used by Sigma’s write-access features (including the schema path for the input table edit log destination).
* You must also be able to provide credentials for a service account with permission to write to the input table edit log destination.

  + For Snowflake, the service account requires `CREATE` privileges on the edit log destination schema in Snowflake.
  + For Databricks, the service account requires `DATA EDITOR` privileges.

## About OAuth with write access features

To use an OAuth connection with write access features, Sigma requires you to designate one or more schemas as write destinations for Sigma object data. OAuth uses the data permissions granted to each individual user in the data warehouse, so those users must be authorized to write to the configured write-back destination.

To determine whether or not a user is authorized to write to a particular destination, Sigma utilizes the user's corresponding user account in the CDW (not a service account) to attempt to create a table in each write destination schema. If a table is successfully created, write access is confirmed for the schema and the validation table is deleted. Sigma initiates the validation process when the user logs in, and the authorized write destinations are cached for the duration of the session to reduce the frequency of queries.

> 🚧
>
> ### Tables created by the write access validation process can be easily identified by object names prepended with `SIGDS_`. To ensure proper functionality of write-access features, avoid modifying any table with the `SIGDS_` prefix.

When a user is only authorized to write to one schema designated as a write destination for the OAuth connection, the Sigma objects they create are written to that destination by default. Otherwise, Sigma allows the user to select from multiple destinations when creating the object.

> 💡
>
> ### In Snowflake, write permissions can be granted to users through their primary or secondary roles in Snowflake. However, the ability to create objects must be granted through the primary role.

### Write-back architecture for warehouse views, materializations, and CSV uploads

The following steps explain how an OAuth connection enables Sigma to write workbook warehouse views, workbook and data model materializations, and CSV uploads to the CDW. (For information about writing input tables, see [About OAuth with input tables](#about-oauth-with-input-tables) in this document.)

> 📘
>
> ### Dataset materializations are not supported when using an OAuth connection.

1. In the Sigma UI, a user creates or edits a Sigma object with a specified write destination.
2. The Sigma UI sends the object data to Sigma’s web service.
3. Sigma’s web service retrieves the user’s OAuth credentials from the Sigma database.
4. Sigma’s web service applies the user’s OAuth credentials to authorize access to your CDW and write the object data to the specified write destination schema.

![Diagram of OAuth flow for write access features other than input tables, matching the steps in the preceding text.](https://files.readme.io/fef8d78e33e588b5c30bb60baa76566d312d9d9676ae928c01c8adedcfaed0bf-Screenshot_2024-08-27_at_3.12.39_PM.png)

## About OAuth with input tables

When your organization utilizes input tables, enabling OAuth with write access requires you to designate a schema as the input table edit log destination.

The edit log (also known as a write-ahead log or WAL) is a sequential record of input table changes that stores information related to user activity and resulting system operations (including input table data stored as edit records). As an internal database mechanism, the edit log ensures data durability, consistency, and recovery.

Sigma also requires you to provide credentials for a service account granted the necessary privileges to write to the edit log destination schema in your CDW. *For data governance purposes, ensure the service account is the only account with permission to write to the edit log destination.*

> 🚧
>
> ### The edit log's corresponding table and all input tables can be easily identified by object names prepended with `SIGDS_`. To ensure proper input table functionality, avoid modifying any table with the `SIGDS_` prefix.

For more information about enabling and using a service account with an OAuth connection, see the documentation corresponding to your connection type:

* See [Connect to Snowflake with OAuth](/docs/connect-to-snowflake#connect-to-snowflake-with-oauth)
* See "Configure OAuth features" in [Connect to Databricks](/docs/connect-to-databricks#configure-oauth-features)

### Write-back architecture for input tables

The following steps explain how an OAuth connection enables Sigma to write input tables to your CDW:

1. In the Sigma UI, a user creates or edits an input table with a specified write destination.
2. The Sigma UI sends the object data to Sigma’s web service.
3. Sigma’s web service retrieves the connection’s service account credentials from the Sigma database.
4. Sigma’s web service applies the service account credentials to authorize CDW access and write input table change information to the edit log destination schema.
5. Sigma’s web service retrieves the *user* OAuth credentials from the Sigma database.
6. Sigma’s web service applies the *user* OAuth credentials to authorize CDW access and write the object data to the specified write destination schema.

![Diagram of OAuth flow for input tables, matching the steps in the preceding text.](https://files.readme.io/062ff4a5d9669ebb6b6c9edaa61856a240ea4e28c77bf485c2ac4d226fddae2f-Screenshot_2024-08-27_at_3.15.09_PM.png)

### Best practices when upgrading to OAuth with input tables

If your organization uses input tables, it's important to note the following information and best practices when you upgrade a non-OAuth connection to use OAuth.

* Input tables written to the connection before the upgrade can still be viewed in Sigma, regardless of whether the previous destination schema is configured as a new write destination. However, users can only continue writing to existing input tables if they're granted write permission to the previous destination schema in your CDW.
* For a seamless transition using OAuth, the edit log destination must be the same schema path that was configured as the connection's write-back destination before the upgrade. If you need to configure a different schema path as the edit log destination, you must also move the edit log's corresponding table to the new destination.

  + For example, in Snowflake, use the following SQL statement to move the edit log table to a new destination:

    SnowSQL

    ```
    ALTER TABLE {original_db}.{original_schema}.{original_table} RENAME TO {new_db}.{new_schema}.{new_table};
    ```
  + Each connection has a single edit log table, named as follows: `SIGDS_WAL_{connection_id}`. If multiple connections use the same edit log destination, that destination schema can contain multiple tables with the `SIGDS_WAL` prefix. Ensure you move the correct edit log table for the specific connection.

Updated 3 days ago

---

Related resources

* [Run a workbook with service account credentials](/docs/run-a-workbook-with-service-account-credentials)
* [Configure OAuth](/docs/configure-oauth)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [About OAuth with write access features](#about-oauth-with-write-access-features)
  + - [Write-back architecture for warehouse views, materializations, and CSV uploads](#write-back-architecture-for-warehouse-views-materializations-and-csv-uploads)
  + [About OAuth with input tables](#about-oauth-with-input-tables)
  + - [Write-back architecture for input tables](#write-back-architecture-for-input-tables)
    - [Best practices when upgrading to OAuth with input tables](#best-practices-when-upgrading-to-oauth-with-input-tables)