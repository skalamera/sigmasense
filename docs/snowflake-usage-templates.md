# Snowflake usage templates

# Snowflake usage templates

Sigma's Snowflake usage templates provide an accurate, in-depth, and prebuilt analysis that helps you understand your company's Snowflake consumption and performance. These templates combine descriptive and prescriptive analytics to provide a foundation for starting an unrestricted analysis into Snowflake usage data. Sigma offers the following templates:

* [Cost monitoring](/docs/snowflake-usage-templates#types-of-snowflake-usage-templates)
* [Performance monitoring](/docs/snowflake-usage-templates#types-of-snowflake-usage-templates)
* [User activity](/docs/snowflake-usage-templates#types-of-snowflake-usage-templates)
* [Reader cost](/docs/snowflake-usage-templates#types-of-snowflake-usage-templates)

## User requirements

The ability to view Snowflake usage templates on your company's Snowflake usage data requires the following:

* You must be an organization **Admin** or be assigned an [account type](/docs/user-account-types) with the **View usage dashboard** permission enabled.
* Your connection must have access to the proper Snowflake usage data schema for each template (see [Grant privileges to a role in Snowflake](/docs/snowflake-usage-templates#grant-privileges-to-a-role-in-snowflake)).

You can see the templates on sample Snowflake usage data by launching the template, regardless of your connection's Snowflake access.

## Types of Snowflake usage templates

These are the descriptions, the data, and the privileges for each template:

Cost Monitoring
:   Covers compute and storage cost across all accounts in the organization. Tracks contract consumption, compute cost and storage cost across your entire Snowflake organization.
:   `SELECT` access on the `ORGANIZATION_USAGE` schema.
:   This schema exists only in your primary Snowflake account.

Performance Monitoring
:   Monitors queries in an individual Snowflake account. Tracks query performance, warehouse activity, and other performance metrics.
:   `SELECT` access on the `ACCOUNT_USAGE` schema.

User Activity
:   Monitors users in an individual Snowflake account. Tracks how Snowflake users use warehouses and databases.
:   `SELECT` access on the `ACCOUNT_USAGE` schema.

Reader Cost
:   Monitors compute cost for reader accounts of an individual Snowflake account.
:   `SELECT` access on the `READER_ACCOUNT_USAGE` schema.

## Change the role of a connection

The value may be set by user attributes; depending on your access, you may not be able to make the change.

1. Open your Sigma [Admin Portal](/docs/sigma-administration).
2. Select the **Connections** page from the left hand panel.
3. Select your connection from the connection list.
4. In **Connection Details**, click **Edit**.
5. In the **Edit connection** page, scroll to the **Connection Credentials** section.
6. Change the **Role** definition.
7. Click **Save**.

## Grant privileges to a role in Snowflake

To use the Snowflake Usage Templates, you must grant access for the proper schema to the role of your Sigma [connection to Snowflake](/docs/connect-to-snowflake). For example, the following SQL statement grants access to the Snowflake database to the SigmaServiceRole role.

```
grant imported privileges on database snowflake to role SigmaServiceRole;
```

Note that all templates don't run on the same schema. To understand roles, permissions, and grants for a *specific* schema, see Snowflake's [Account Usage](https://docs.snowflake.com/en/sql-reference/account-usage#enabling-account-usage-for-other-roles) documentation.

## Create a new workbook from a Snowflake Usage Template

To display your company's Snowflake usage data, follow these steps to create a workbook from a Snowflake Usage Template.

1. Go to your Home page.
2. In the left navigation pane, select **Templates** gallery page. You can access it from:
3. On the left panel, click **Templates**.
4. Click the **Snowflake Usage Template** you want to use.

   ![Select a template from a list of templates](https://files.readme.io/bb24a71-1.png)
5. This page initially shows sample Snowflake usage data.
6. Click **Swap Now** to replace this sample data with your own Snowflake usage data.

   ![Swamp data in the template](https://files.readme.io/e6077b2-2.png)

   To view the workbook with sample data, click **Dismiss**.

   ![The Snowflake Performance Monitoring template](https://files.readme.io/1421f97-3.png)
7. When you click **Swap Now**, it opens the **Swap Data Sources** page. Sigma searches your connections for tables that match the structure of the current sources.

   Because Snowflake usage tables are consistent in structure, there should be a fully compatible match. If no match is found, you can manually locate the correct table.

   ![Compare the template table to your own table](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/edit.svg)
8. In the **Replace With** section, locate the matched source you want to replace, then click **Edit**.

   ![Replace the template table with your own table](https://files.readme.io/c71c26e-5.png)
9. Select a new table from the modal.
10. When you locate the correct tables to swap, click **Swap**. The page refreshes, and displays your data.
11. Check the workbook to confirm that you have correct data.
12. To create an editable and publishable workbook from the template, click **Save As** in the header, and save your new workbook.

## Known issues and Snowflake concepts

### Slow upload or timeout

If your Snowflake Usage workbooks upload slowly or time out, you can improve their performance.

Slow load times and query timeouts are common when the warehouse struggles to respond to a request because of the complexity of queries that run on large tables of busy warehouses. In response to slow load times, Sigma will time out a request if the query is still running after 2 minutes.

To check on your query run times and view timeouts, visit your workbook's [query display modal](/docs/examine-sql-queries-workbooks).

To improve your workbook's load time, filter the date to a smaller date range. Snowflake Organization and Account Usage tables are partitioned by time, so filtering by the date improves performance.

### Errors when source swapping

You may experience errors or NULL data when swapping tables in templates. To avoid errors, ensure that the tables you swap are:

* From the same connection
* From the correct schema
* Not empty

To verify these, open the **Swap Data Sources** modal, and check the connection for each table.

![](https://files.readme.io/8770456-6.png)

Snowflake sometimes provides an `ORGANIZATION_USAGE` schema for secondary Snowflake accounts, but leaves it empty. The [Cost monitoring](/docs/snowflake-usage-templates#types-of-snowflake-usage-templates) template may refer to this empty scheme, resulting in errors. You can fix this by changing the source instructions to use the `ORGANIZATION_USAGE` schema of the primary account.

### Snowflake organization vs. account

An organization is the main Snowflake object; it is effectively a collection of Snowflake accounts. It may contain one or many accounts, and only one of them is the primary account. This primary account has the `ORGANIZATION_USAGE` schema provided to it in the SNOWFLAKE database. The other (secondary) accounts, do not have access to this schema by default.

An account is a collection of warehouses, databases, users, roles, and so on. Each account is a child of an organization, and has its own `ACCOUNT_USAGE` and `READER_ACCOUNT_USAGE` schema. These schemas contain data for this account *only*, and no information about other accounts in the same organization.

### Current data

After you launch a copy of the template that you attached to your own data, the Snowflake Usage Template always shows up-to-date data. The templates rely on the Snowflake-provided views that are managed by Snowflake, and deliver current data (up to few hours latency).

### Updating templates

When Sigma updates the templates, and publishes a change to a shared template like the SUTs, all Sigma organizations with access to that template can see those changes for all new workbooks launched from that template. Workbooks created from the previous version of the template will not see the update.

Updated 3 days ago

---

Related resources

* [Get started with workbook templates](/docs/get-started-with-workbook-templates)
* [Create and edit workbook templates](/docs/create-and-edit-workbook-templates)
* [Connect to Snowflake](/docs/connect-to-snowflake)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Types of Snowflake usage templates](#types-of-snowflake-usage-templates)
  + [Change the role of a connection](#change-the-role-of-a-connection)
  + [Grant privileges to a role in Snowflake](#grant-privileges-to-a-role-in-snowflake)
  + [Create a new workbook from a Snowflake Usage Template](#create-a-new-workbook-from-a-snowflake-usage-template)
  + [Known issues and Snowflake concepts](#known-issues-and-snowflake-concepts)
  + - [Slow upload or timeout](#slow-upload-or-timeout)
    - [Errors when source swapping](#errors-when-source-swapping)
    - [Snowflake organization vs. account](#snowflake-organization-vs-account)
    - [Current data](#current-data)
    - [Updating templates](#updating-templates)