# Dynamically assign roles used by a connection

# Dynamically assign roles used by a connection

You can dynamically assign a role for a specific user or team of users to use in a new or existing connection that supports it based on the value of an assigned user attribute.

> 📘
>
> This feature isn't supported by all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

Use a dynamically assigned role to manage user access for a variety of use cases, such as assigning the role that a team of embed users should use to access securely embedded content. By using more than one role on your connection, you can take advantage of the row-level security defined in your data platform rather than manually recreating row-level security and security policies in Sigma.

> 📘
>
> ### You can only use this option with key pair authentication. If you connect Sigma to your data platform using OAuth, you cannot use this option.

After you configure attributes on the connection, you can also assign the attribute to external embed users in a secure embed URL. For more details, see [Restrict access to data in embedded content](/docs/restrict-access-to-data-in-embedded-content).

> 💡
>
> ### For Snowflake connections, you can also dynamically assign a virtual warehouse with a `Warehouse` user attribute. Dynamically assigning a warehouse lets you manage compute costs separately for each customer, for example, if you securely embed Sigma.

## Requirements

You must be assigned the Admin [account type](/docs/user-account-types).

You also must ensure that your data platform is set up to support this configuration:

* Each role must be granted to the user or user account associated with the connection.
* Each role must be granted privileges or permissions to use the relevant database objects.
* If you dynamically assign a warehouse for Snowflake, the Snowflake role to be used with a specific warehouse must be granted at least the USAGE privilege on the warehouse.

## Configure user attributes

To set user attributes on a connection, you must first create and assign a `Role` user attribute to the relevant users and teams of users.

1. Create a `Role` user attribute. Set a default value equivalent to a suitable default role in your data platform configuration.
2. Assign the `Role` user attribute to users and teams. Set the value of the user attribute to the role name that you want each team or user to use when accessing data.

> 💡
>
> ### The same steps apply for the `Warehouse` attribute.

For instructions, see [Configure user attributes](/docs/user-attributes).

## Set user attributes on a connection

After you create and assign a user attribute to users and teams, configure a new or existing connection to use the user attributes:

1. Follow the steps to create a connection for your data platform:

   * [Snowflake](/docs/connect-to-snowflake#create-a-snowflake-connection-in-sigma)
   * [PostgreSQL](/docs/connect-to-postgresql)
2. (Snowflake only) In the **Connection Credentials** section, for the **Warehouse** field, select **Set by user attribute** to browse and select the `Warehouse` attribute that you previously configured.
3. In the **Connection Credentials** section, for the **Role** field, select **Set by user attribute** to browse and select the `Role` attribute that you previously configured.
4. Finish setting up your connection. When you create or save your connection, the changes take effect.

## Use with secure embeds

See [Restrict access to data in embedded content](/docs/restrict-access-to-data-in-embedded-content).

Updated 3 days ago

---

[Run a workbook with service account credentials](/docs/run-a-workbook-with-service-account-credentials)[Connect through SSH](/docs/connect-through-ssh)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Configure user attributes](#configure-user-attributes)
  + [Set user attributes on a connection](#set-user-attributes-on-a-connection)
  + [Use with secure embeds](#use-with-secure-embeds)