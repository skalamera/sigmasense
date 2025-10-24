# Connect to Redshift

# Connect to Redshift

Sigma supports secure connections to Amazon Redshift.

This document explains how to connect your organization to an Amazon Redshift warehouse.

> 📘
>
> For information about Sigma feature compatibility with Amazon Redshift connections, see [Region, warehouse, and feature support](/docs/region-warehouse-and-feature-support).

## Requirements

In your Sigma organization:

* You must be assigned the **Admin** [account type](/docs/user-account-types).

In AWS:

* You must have access to an Amazon Redshift data warehouse with a configured cluster. A node size of `ra3.4xlarge` or larger is recommended if you are using input tables on this connection.

## Configure Amazon Redshift

Complete the following steps in the AWS Management Console before you add an Amazon Redshift connection in your Sigma organization.

1. Modify your Amazon Redshift cluster to be publicly accessible and assign an Elastic IP address to connect to it.
2. Create a security group, then add Sigma’s IP addresses to the inbound and outbound rules of the security group. Obtain the IP addresses from the connection configuration page in the Sigma UI. See [Add Sigma IPs to the allowlist](/docs/connect-to-data-sources#add-sigma-ips-to-the-allowlist).
3. Attach the security group to your Amazon Redshift cluster.
4. Create an Amazon Redshift user to act as the service account for connection to your Sigma organization.

   Grant this user `USAGE` privileges on all relevant schemas in the Redshift cluster and `SELECT` grants on all relevant tables within those schemas. Configure this user to have the same privileges on any additional tables that might be added to the schema.

   For documentation on granting privileges, see [GRANT](https://docs.aws.amazon.com/redshift/latest/dg/r_GRANT.html) in the Amazon Redshift Database Developer Guide.

   Example SQL statement:

   SQL

   ```
   CREATE USER your_sigma_service_account_name password 'a_secure_password'; 
   GRANT USAGE ON SCHEMA your_schema_name TO your_sigma_service_account_name;
   GRANT SELECT ON ALL TABLES IN SCHEMA your_schema_name TO your_sigma_service_account_name;
   ALTER DEFAULT PRIVILEGES IN SCHEMA your_schema_name
   GRANT SELECT ON TABLES TO your_sigma_service_account_name;
   ```
5. [optional] If you want to run [stored procedure actions](/docs/create-actions-that-call-stored-procedures), grant the service account user `USAGE` on any schema that contains stored procedures that you want to run from Sigma, and grant `EXECUTE` privileges on all or specific stored procedures.

   Example SQL statement:

   SQL

   ```
   GRANT USAGE ON SCHEMA your_sproc_schema_name TO your_sigma_service_account_name;
   GRANT EXECUTE ON ALL PROCEDURES IN SCHEMA your_sproc_schema_name TO your_sigma_service_account_name;
   ```
6. [optional] If you want to leverage write access features such as CSV upload, materialization, input tables, and warehouse views, create a dedicated schema that Sigma write-back features can use to write data to.

   Grant `CREATE` privileges on that schema to your user, and grant `SELECT, INSERT, UPDATE, DELETE` on all tables in that schema. Configure your user to have the same privileges on any additional tables that may be added to the schema.

   SQL

   ```
   GRANT USAGE, CREATE ON SCHEMA your_write_schema_name TO your_sigma_service_account_name;
   GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA your_write_schema_name TO your_sigma_service_account_name;
   ALTER DEFAULT PRIVILEGES IN SCHEMA your_write_schema_name
   GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO your_sigma_service_account_name;
   ```

## Create an Amazon Redshift connection in Sigma

To create an Amazon Redshift connection, perform the following steps in the Sigma UI:

* [Add a connection and specify connection details](#add-a-connection-and-specify-connection-details)
* [Specify your connection credentials](#specify-your-connection-credentials)
* [Configure write access](#configure-write-access)
* [Configure connection features](#configure-connection-features)

### Add a connection and specify connection details

1. Click the user icon at the top right of your screen.
   The user icon is usually composed of your initials.
2. In the drop-down menu, select **Add connection**. The **Add new connection** page appears.
3. In the **Connection Details** section, specify the following:

   |  |  |
   | --- | --- |
   | **Name** | Enter a **Name** for the new connection. |
   | **Type** | Select **Redshift**. |

### Specify your connection credentials

In the **Connection Credentials** section, fill out the required fields:

1. In the **Host** field, enter the value of the **Endpoint** field in the **General Information** screen of your Redshift cluster.
   Example: `cluster.abcd.us-west-1.redshift.amazonaws.com`
2. In the **Port** field, enter your cluster's port number. You can find your port number in the properties of your Amazon Redshift cluster under **Database configurations**.
   Example: `5439`
3. In the **User** and **Password** fields, enter the username and password of the Amazon Redshift user you created to connect to your Sigma organization. See Step 4 in [Configure Amazon Redshift](#configure-amazon-redshift).
4. In the **Database** field, enter your cluster's database name.
5. [optional] Turn on the **Enable TLS** toggle to enable TLS encryption on your connection.
6. [optional] Turn on the **SSH Tunnel** toggle to connect through SSH, then enter the **Tunnel host** and **Tunnel port**. See [Connect through SSH](/docs/connect-through-ssh).

Next, see [Configure write access](/docs/connect-to-databricks#configure-write-access) and [Configure connection features](/docs/connect-to-databricks#configure-connection-features) for additional options. Or, if you are finished configuring your connection, click **Create** at the top right to create your connection.

### Configure write access

Write access is necessary for the following features:

* [CSV upload](/docs/upload-csv-data)
* [Materialization](/docs/materialization)
* [Input tables](/docs/intro-to-input-tables)
* [Warehouse views](/docs/create-and-manage-workbook-warehouse-views)

Configuring write access requires you to set up a dedicated schema in Amazon Redshift that Sigma can use to write data and grant the necessary privileges on that schema to the service account. See Step 5 in [Configure Amazon Redshift](#configure-amazon-redshift).

1. To allow write access on this connection, turn on the toggle next to **Enable write access**.
2. In the **Write schema** field, enter the name of the dedicated schema you created for Sigma to store write-back data.

Next, see [Configure connection features](/docs/connect-to-databricks#configure-connection-features) for additional options. Or, if you are finished configuring your connection, click **Create** at the top right to create your connection.

### Configure connection features

In the **Connection Features** section, specify the following:

1. In the **Connection timeout** field, specify the amount of time, in seconds, that Sigma should wait for the query to return results before timing out. The default in 120 seconds. The maximum is 600 seconds (10 minutes).
2. [optional] If you do not want Sigma to automatically make column names from the data source more readable, turn off the **Use friendly names** toggle. For example, with **Use friendly names** turned on, a database column ORDER\_NUMBER or OrderNumber appears as Order Number.

### Finish creating your connection

After you specify all the parameters of the connection, click **Create.**

1. Click **Create** at the top right of the screen to create your connection. Sigma displays a connection summary on the screen.
2. Click **Browse Connection**, then click **Add permission** to grant connection access for users in your organization. See [Data permissions](/docs/data-permissions-overview).
   ![](https://files.readme.io/641ba71f977c5cce33b88891c248aa71586a969ad54446c8619b176863dc76cb-redshift-new-connection.png)
3. Use the navigation in the left panel to explore the schemas and tables in your connection.
   ![](https://files.readme.io/c740f832f805473e7f35bebecd259c33c6c024c3485d4c340d11b9ff16c6c0cb-redshift-browse-connection.png)

Updated 3 days ago

---

Related resources

* [Connect through SSH](/docs/connect-through-ssh)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Configure Amazon Redshift](#configure-amazon-redshift)
  + [Create an Amazon Redshift connection in Sigma](#create-an-amazon-redshift-connection-in-sigma)
  + - [Add a connection and specify connection details](#add-a-connection-and-specify-connection-details)
    - [Specify your connection credentials](#specify-your-connection-credentials)
    - [Configure write access](#configure-write-access)
    - [Configure connection features](#configure-connection-features)
    - [Finish creating your connection](#finish-creating-your-connection)