# Manage access to data and connections

# Manage access to data and connections

In Sigma, you can manage user, team, and organization access to data at multiple levels:

* An entire connection
* Specific databases and catalogs
* Schemas
* Specific objects, such as tables and stored procedures

Access granted to data is additive. For more details about the access model and specific access levels that can be granted, see [Data access overview](/docs/data-permissions-overview).

> 🚩
>
> Data access applies to users with the **View connections** or **Manage connections** permissions enabled on their [account type](/docs/account-type-and-license-overview).

## User requirements

To manage access to data and connections, you must be assigned the **Admin** [account type](/docs/create-and-manage-account-types) or be granted **Can admin** access to the connection.

## Review access granted to a connection or database object

Review the access granted to an entire connection, a database or catalog, a schema, or an object:

1. From Sigma Home, select the relevant connection:

   * If your organization has between one and three connections, select the connection name in the navigation menu.
   * If your organization has more than three connections, Sigma consolidates them in a **Connections** page. In the navigation menu, click **Connections** to open the page, then select the connection.
   > 💡
   >
   > ### If you are assigned the Admin account type, you can also access a connection from the **Administration** portal. Go to **Administration** > **Connections**, select a connection, then click **Browse connection**.
2. On the **Access** tab of the connection overview, view the following information for all access granted across the connection:

   |  |  |
   | --- | --- |
   | **Access granted to** | Name of the user or team granted the access |
   | **Grant location** | Name of the database object to which the access was granted |
   | **Access level** | Access granted |
   | **Last updated** | Date the access was last updated |
3. To view access inherited by or granted to a specific user or team, search for a username, email address, or team name. To view access inherited by or granted to the entire organization, search for "all members". You can also filter the list by access level and scope level.
4. To view access inherited from or granted to a specific database or catalog, schema, or object, browse to and select the object in the side panel or click the linked name in the **Grant location** field.

   If you select a database table, open the **Access** tab to view the relevant access granted on the object.

## Grant access to a connection or database object

Grant a user, team, or the entire organization access to an entire connection, a database or catalog, a schema, or an object:

1. From Sigma Home, select the relevant connection:

   * If your organization has between one and three connections, select the connection name in the navigation menu.
   * If your organization has more than three connections, Sigma consolidates them in a **Connections** page. In the navigation menu, click **Connections** to open the page, then select the connection.
   > 💡
   >
   > ### If you are assigned the Admin account type, you can also access a connection from the **Administration** portal. Go to **Administration** > **Connections**, select a connection, then click **Browse connection**.
2. In the data catalog, select the object to which you want to grant access.
3. On the **Access** tab, click **Grant access**.
4. In the **Grant access to** modal, grant the appropriate access:

   1. Search for and select the user or team to which you want to grant access. You can grant access to multiple users or teams at the same time. To grant access to your entire organization, search for "all members" and select "All members of your organization".
   2. In the **Access** column, select the dropdown menu and choose an access level.

      The level of access that a user can be granted depends on the permissions enabled on their account type. For details, see [Data access overview](/docs/data-permissions-overview).

      * For users, the dropdown only displays access levels that can be granted to the user.
      * For teams, the dropdown displays all levels of access, even if some team members cannot be granted all levels of access. A team member only inherits the access level granted to the team if they are assigned the required account type permissions.
   3. To notify the user or team members of the granted access, select the **Send an email notification** checkbox. To grant the access without notifying them, clear the checkbox.
   4. [optional] If you choose to send an email notification, enter a message in the **Add a Message** field to provide additional context.
   5. Click **Save** to grant the access.
5. Review the granted access in the list for the object.

## Modify existing access to a connection or database object

Change the access granted to an existing user, team, or all members of your organization:

1. From Sigma Home, select the relevant connection:

   * If your organization has between one and three connections, select the connection name in the navigation menu.
   * If your organization has more than three connections, Sigma consolidates them in a **Connections** page. In the navigation menu, click **Connections** to open the page, then select the connection.
   > 💡
   >
   > ### If you are assigned the Admin account type, you can also access a connection from the **Administration** portal. Go to **Administration** > **Connections**, select a connection, then click **Browse connection**.
2. In the **Access** column, locate the user or team for which you want to update access, then click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Edit access**.

   If the access applies to a downstream object, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Go to access**, then perform this step.
3. In the **Grant access to** modal, edit the level of access granted:

   1. In the **Access** drop-down menu, select a different level of access.
   2. [optional] To notify the user or team members of the update, select the **Send an email notification** checkbox. To modify access without notifying them, clear the checkbox.
   3. [optional] If sending an email notification, enter a message in the **Add a message** field to provide additional context.
   4. Click **Save**.
4. Review the change in the **Access** list.

## Revoke access to a connection or database object

To revoke access to a connection or database object from a user or group, do the following:

1. From Sigma Home, select the relevant connection:

   * If your organization has between one and three connections, select the connection name in the navigation menu.
   * If your organization has more than three connections, Sigma consolidates them in a **Connections** page. In the navigation menu, click **Connections** to open the page, then select the connection.
   > 💡
   >
   > ### If you are assigned the Admin account type, you can also access a connection from the **Administration** portal. Go to **Administration** > **Connections**, select a connection, then click **Browse connection**.
2. In the **Access** column, locate the user or team for which you want to update access, then click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Revoke access**.

   If the access applies to a downstream object, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Go to access**, then perform this step.
3. Review the confirmation modal and click **Revoke** to proceed.
4. Confirm that the access granted to the user or team is no longer listed in the **Access** list.

Updated 3 days ago

---

Related resources

* [Data permissions overview](/docs/data-permissions-overview)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Review access granted to a connection or database object](#review-access-granted-to-a-connection-or-database-object)
  + [Grant access to a connection or database object](#grant-access-to-a-connection-or-database-object)
  + [Modify existing access to a connection or database object](#modify-existing-access-to-a-connection-or-database-object)
  + [Revoke access to a connection or database object](#revoke-access-to-a-connection-or-database-object)