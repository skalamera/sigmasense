# Data access overview

# Data access overview

To support granular data security and flexible access control at any level of your data architecture and organizational structure, Sigma supports granting access to data at different levels. Data access is additive, so access granted on a database or catalog also applies to its schemas and objects (database tables and stored procedures).

This document describes the additive data access model and provides details about the available access levels. For information about viewing, adding, editing, and revoking access, see [Manage access to data and connections](/docs/manage-data-permissions).

> 🚩
>
> Data access applies to users with the **View connections** or **Manage connections** permissions enabled on their [account type](/docs/account-type-and-license-overview).

## Data access model

Access to data is additive, meaning that Sigma provides access and capabilities based on a cumulative set of access and permissions inherited or granted at different levels of the data architecture (connection, database/catalog, schema, database table, stored procedure) and organizational structure (organization, team, user).

For example, access might be inherited based on where it is granted or to whom it is granted:

* Access granted on an entire connection is inherited by the databases or catalogs in that connection.
* Access granted on a database or catalog is inherited by the schemas in that database or catalog.
* Access granted to teams is inherited by the users that are members of those teams.

When an admin grants access directly to a lower-level object, Sigma uses the access level (inherited or directly granted) with the *most* access.

In the following two examples, the additive access model applies the cumulative set of access inherited or granted at any given level. Access inherited by higher-level grants cannot be revoked or restricted by lower-level grants.

### Example 1

If John is a user in an organization that connects to a single database containing multiple schemas and database tables. An admin grants John **Can use** access to the connection, which allows him to use all databases, schemas, and database tables within the connection.

The admin later grants John **Can use & annotate** access to a specific schema, which allows him to use and annotate any database table within that particular schema. The schema-level access overrides the inherited connection-level access because the **Can use & annotate** access is greater. For any other schema or database table in the schema, John maintains the inherited **Can use** access.

### Example 2

As another example, for an entire connection, an admin grants **Can use & annotate** access to the Sales team and **Can use** access to Radhika as an individual user. Radhika is not part of the Sales team.

If the admin later adds Radhika to the Sales team, she inherits the team-level **Can use & annotate** access, which overrides the **Can use** access granted directly to her. She can then use and annotate any database, schema, and database objects in the connection.

## Data access levels

Sigma supports four levels of access that grant various capabilities to connections, databases or catalogs, schemas, and database tables: **Can write only**, **Can use**, **Can use & annotate**, and **Can admin**.

The following sections summarize each access level. For a detailed access breakdown, see [Data access matrix](#data-access-matrix) in this document.

> 📘
>
> ### Admins can grant access to teams. However, individual users in a team only inherit team-level access if they are assigned the required account type permissions listed in the following sections.

### Can write only

**Can write only** access restricts access to data while enabling users to perform tasks, like creating input tables and uploading CSV files, that write data to the connection’s write-back destination. This access is ideal for enabling input tables and CSV uploads in embedded workbooks with restricted data access.

* Access granularity: Granted at the connection level only
* Minimum required [account type](/docs/user-account-types) permission: **Create input tables**, **Upload CSV**, **Schedule materializations**, **Create warehouse views**.

### Can use

**Can use** access allows users to view connection details, explore the data, and use it to build datasets, data models, and workbooks.

* Access granularity: Granted at the connection, database or catalog, schema, database table or stored procedure level
* Minimum required [account type](/docs/user-account-types) permissions:
  + **View connections** to browse the connection
  + **Create, edit, and publish datasets** to use the connection as a data source for datasets or data models
  + **Create, edit, and publish workbooks** to explore the connection data and use it as a data source for workbook elements

> 📘
>
> ### Any user can be granted **Can use** data access. However, the extent of access and capabilities depends on each individual user’s account type permissions.

### Can use & annotate

**Can use & annotate** access enables all **Can use** access and allows users to annotate database table details. Table annotations include changes that apply only in Sigma and are not written to the database.

* Access granularity: Granted at the connection, database or catalog, schema, database table or stored procedure level
* Minimum required [account type](/docs/user-account-types) permission: **Manage connections** or **Annotate tables**

### Can admin

**Can admin** access grants full access to the connection data, including the ability to grant data access to other users or teams.

* Access granularity: Granted at the connection level only
* Minimum required [account type](/docs/user-account-types) permission: **Manage connections**

## Data access matrix

The following table indicates user capabilities based on data access granted.

|  | Can write  only | Can use | Can use &  annotate | Can  admin |
| --- | --- | --- | --- | --- |
| Write data to the connection’s write-back destination1 |  |  |  |  |
| Browse connection2 |  |  |  |  |
| Explore data |  |  |  |  |
| Use as data sources for datasets and workbook elements |  |  |  |  |
| Edit column details in Sigma3 |  |  |  |  |
| Manage metrics |  |  |  |  |
| Manage links to other sources |  |  |  |  |
| Grant data access |  |  |  |  |
| View and manage connection in the **Administration** portal |  |  |  |  |

1Create input tables and CSV uploads that write data to the connection’s write-back destination.

2View underlying database table overviews, column details, metrics, links, and lineage (Sigma datasets, data models, and workbooks referencing the database table).

3Edit the column name in Sigma (“friendly name”), change column visibility, set column format, and add column description.

Updated 3 days ago

---

Related resources

* [Manage data permissions](/docs/manage-data-permissions)
* [User account types](/docs/user-account-types)

* [Table of Contents](#)
* + [Data access model](#data-access-model)
  + - [Example 1](#example-1)
    - [Example 2](#example-2)
  + [Data access levels](#data-access-levels)
  + - [Can write only](#can-write-only)
    - [Can use](#can-use)
    - [Can use & annotate](#can-use--annotate)
    - [Can admin](#can-admin)
  + [Data access matrix](#data-access-matrix)