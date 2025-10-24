# Azure Private Link Connections

# Azure Private Link Connections

This document explains how to connect Sigma to your data warehouse that's hosted on Azure using Azure's Private Link.

> 📘
>
> ### See Sigma's [Azure Private Link](https://quickstarts.sigmacomputing.com/guide/administration_azure_private_link/index.html?index=..%2F..index#0) lab for more information on how to establish a secure connection between Sigma and an Azure data warehouse.

## Requirements

* A Sigma organization running on Azure.
* You must be assigned the Admin [account type](/docs/create-and-manage-account-types) in your Sigma organization.
* Snowflake, Databricks, PostgreSQL or MySQL Admin, depending on the data warehouse.
* Be an Admin in Azure.

## Introduction

Sigma organizations running on Azure can securely connect to their data using Azure's Private Link, which allows Sigma to access the data warehouse hosted on Azure via a private endpoint in the virtual network. This not only enhances security during data transit but also improves performance by reducing network latency. With Private Link, Sigma connects to the data warehouse using private IP addresses, ensuring traffic never leaves the Microsoft network and data remains secure without exposure to the internet.

To utilize Private Link, create a private endpoint in your virtual network that maps to the data warehouse, assign it a private IP address, and connect to the warehouse using this address.

Sigma supports connections to the following data warehouses on Azure:

* [Snowflake](#snowflake)
* [Databricks](#databricks)
* [PostgreSQL](#postgresql)
* [MySQL](#mysql)
* [Azure SQL Database, Azure SQL Managed Instance, or SQL Server 2022](#azure-sql-database-azure-sql-managed-instance-or-sql-server-2022)

## Create Private Link connection for your data warehouse

Follow the steps below to create a Private Link connection to your data warehouse hosted in Azure.

> 📘
>
> ### To initiate this process, the first step for all data warehouses is to retrieve the required information and send to your account manager.

## Snowflake

> 📘
>
> ### As of September 16, 2025, new Private Links to Snowflake will require a private link to a [Snowflake internal stage](https://docs.snowflake.com/en/user-guide/private-internal-stages-azure). Existing Azure Private Links created before September 16, 2025 will not require an additional internal stage Private Link. If you want to add a private link to a Snowflake internal stage and already have an Azure Snowflake private link set up with Sigma, see [Add a Private Link to a Snowflake internal stage](#add-a-private-link-to-a-snowflake-internal-stage).

Creating an Azure Private Link to Snowflake is a multi-step process:

1. [Configure your Snowflake internal stage](#step-1-configure-your-snowflake-internal-stage)
2. [Provide Snowflake information to Sigma](#step-2-provide-snowflake-information-to-sigma)
3. [Configure your Snowflake connection in Sigma](#step-3-configure-snowflake-connection-in-sigma)

### Step 1: Configure your Snowflake internal stage

Sigma requires all Azure Private Links created after September 16, 2025 to also include a link to a [Snowflake internal stage](https://docs.snowflake.com/en/user-guide/private-internal-stages-azure).

Configure your internal stage in Snowflake by running the following commands in your Snowflake console:

```
USE ROLE ACCOUNTADMIN;  
ALTER ACCOUNT SET ENABLE\_INTERNAL\_STAGES\_PRIVATELINK \= true;
```

See the Snowflake documentation on [Configuring private endpoints to access internal stages](https://docs.snowflake.com/en/user-guide/private-internal-stages-azure#configuring-private-endpoints-to-access-snowflake-internal-stages) for more information.

### Step 2: Provide Snowflake information to Sigma

> 📘
>
> ### Your Snowflake account must be Business Critical Edition to use Private Link.

Follow the steps below to provide Sigma with the requisite information to create a Private Link for your organization.

1. In your Snowflake console, run the following command:

```
select key, value from table(flatten(input=>parse_json(system$get_privatelink_config())));
```

2. In the output field, copy the values for `privatelink-pls-id`, `private-account-url`, `privatelink-internal-stage` and `ResourceID`:

   * The `private-pls-id` may be formatted similarly to: `Sf-pvlinksvc-<region>.<id>.<region>.azure.privatelinkservice`
   * The `private-account-url` may be formatted similarly to `<account_id>.<region>.privatelink.snowflakecomputing.com`
   * The `privatelink-internal-stage` may be formatted similarly to `/subscriptions/<subscription_id>/resourceGroups/sfc-prod-storage/providers/Microsoft.Storage/storageAccounts/<internal_stage_id>`
   * The ResourceID of the internal stage storage account is defined by the `privatelink-internal-stage` key.
3. Contact your Sigma account manager and provide:

   * The `privatelink-pls-id` value
   * The `private-account-url` value
   * The `ResourceID` defined by the `privatelink-internal-stage` key
4. Sigma will create a Private Link and notify you when the link is active.
5. After the Private Link to internal stage has been created, you will need to approve the endpoint request in Snowflake. Call the `SYSTEM$AUTHORIZE_STAGE_PRIVATELINK_ACCESS` function by running the following in your Snowflake console:

```
select system$authorize_stage_privatelink_access('<Sigma_Private_Endpoint_ID>');
```

Use the `Sigma_Private_Endpoint_ID` provided to you by your Sigma account manager.

See the Snowflake documentation on [SYSTEM$AUTHORIZE\_STAGE\_PRIVATELINK\_ACCESS](https://docs.snowflake.com/en/sql-reference/functions/system_authorize_stage_privatelink_access) for more information.

Once your Private Link is active and you have approved the internal stage endpoint request, follow the steps to configure your Snowflake connection in Sigma.

### Step 3: Configure Snowflake connection in Sigma

Follow the steps below to configure your Sigma Snowflake connection to use Private Link. You can only complete these steps once your Private Link is active.

1. After the private link is active, in Sigma, go to **Admin > Connections > Snowflake**.
2. Click **Create** to create a Snowflake connection.
3. In the **Account** field, enter the three parts of the account URL in this format: `<account>.<region_id>.privatelink`

   For example, if the account URL is:

   `test123.west-us-2.privatelink.snowflakecomputing.com`

   The **Account** field is `test123.west-us-2.privatelink`
4. Under **Warehouse,** enter your warehouse’s name as listed in Snowflake.
5. If you have OAuth enabled on your organization, and you would like to use it on the connection, switch on OAuth access; see [Connect to Snowflake with OAuth](/docs/connect-to-snowflake#connect-to-snowflake-with-oauth).
   *Please note: Steps 9 - 11 are not applicable if you choose to use OAuth without a service account.*
6. Under **User,** enter your Snowflake username.
7. Under **Password**, enter your Snowflake password.
8. [optional] For **Role**, you can specify a Snowflake role to be used on this connection.

   ![company apps](https://files.readme.io/fd91793-2.png)
9. [optional] For **Connection Features**, you can set a connection timeout and/or [enable write access](/docs/set-up-write-access).
10. After completing the form, click **Create**.

### Add a Private Link to a Snowflake internal stage

If you have an existing Azure Snowflake Private Link and want to create a private link to a [Snowflake internal stage](https://docs.snowflake.com/en/user-guide/private-internal-stages-azure), follow the steps below:

1. Enable the internal stage in Snowflake by running the following command in your Snowflake console:

   ```
   USE ROLE ACCOUNTADMIN;
   ALTER ACCOUNT SET ENABLE_INTERNAL_STAGES_PRIVATELINK = true;
   ```
2. Obtain the `ResourceID` of the internal stage storage account defined by the `privatelink-internal-stage` key from your Snowflake console, by running the following command:

   ```
   select key, value from table(flatten(input=>parse_json(system$get_privatelink_config())));
   ```

The `ResourceID` may be formatted similarly to `/subscriptions/XXX-XXX-XXX-XXX/resourceGroups/sfc-prod-storage/providers/Microsoft.Storage/storageAccounts/XXXX`.

3. Contact your Sigma account manager and provide them with the `ResourceID`.
4. Sigma will contact you once the new Private Link has been created, and provide you with a `Sigma_Private_Endpoint_ID` (which is the `ResourceID` of a Sigma-owned private endpoint).
5. After the Private Link has been created, you will need to approve the endpoint request in Snowflake. Call the `SYSTEM$AUTHORIZE_STAGE_PRIVATELINK_ACCESS` function by running the following in your Snowflake console:

   ```
   select system$authorize_stage_privatelink_access('<Sigma_Private_Endpoint_ID>');
   ```

Use the `Sigma_Private_Endpoint_ID` provided to you by your Sigma account manager.

See the Snowflake documentation on [SYSTEM$AUTHORIZE\_STAGE\_PRIVATELINK\_ACCESS](https://docs.snowflake.com/en/sql-reference/functions/system_authorize_stage_privatelink_access) for more information.

## Databricks

**Prerequisites**

* You must create an Azure Databricks workspace.
* Your Databricks workspace must be Premium tier.
* A customized networking configuration is required to support Private Link.

### Provide Databricks Resource ID to Sigma

Follow the steps below to provide Sigma with the Resource ID to create a private link for your organization.

1. In Azure Services, hover over **Azure Databricks** and click **Create**.

   ![company apps](https://files.readme.io/cd565f2-4.png)
2. Click **JSON View** in the top-right corner of the databricks workspace page in Azure.
3. On the **Networking** tab, you must check **Yes for Deploy Azure Databricks workspace in your own Virtual Network** and enter pre-configured virtual network and two subnets within the virtual network CIDR range for public and private subnet fields.
4. Copy the following values and send them to your Account Executive:

   * **Resource ID**
   * **Region Name** for the Databricks warehouse (under **Location**)
   * **URL** for the Databricks service, formatted as `adb-<workspace-id>.<random-number>.azuredatabricks.net`.

   ![company apps](https://files.readme.io/26fdb87-5.png)

### Private Link approval

Follow the steps below to approve the Private Link after Sigma notifies you.

1. In the Azure portal, go to **Azure Databricks**.
2. Click the selected Azure Databricks workspace.
3. Click **Networking** on the left panel.
4. Click on **Private endpoint connections.**
5. Select the newly created private endpoint. The status will be **Pending**. Check **Approve** to approve the endpoint. Copy the name of the private endpoint, it's required when you configure Sigma.

   ![company apps](https://files.readme.io/bb7b579-6.png)

### Configure Databricks Connection

1. In the Databricks section of Azure, click on the warehouse instance > **Databricks Workspace**.
2. Click **Launch Workspace**.

   ![company apps](https://files.readme.io/870df05-7.png)
3. In Databricks, select **SQL** in the **Data Science & Engineering** dropdown.

   ![company apps](https://files.readme.io/200f8d7-8.png)
4. Click **Review SQL Warehouses**.

   ![company apps](https://files.readme.io/0138e83-9.png)
5. Select the warehouse.
6. Click the **Connection details** tab.
7. Copy the **HTTP path** value in Databricks as it's required in the Sigma UI.

   ![company apps](https://files.readme.io/7d4fc7c-10.png)
8. Go to **User Settings** in Databricks by clicking on your username.

   ![company apps](https://files.readme.io/c69849a-11.png)
9. Click **Personal access tokens** tab.
10. Click **Generate new token**.
11. In the **Lifetime** field, set the duration of the private link. The link will expire based on the value.
12. Enter a value in the **Comment** field.

    ![company apps](https://files.readme.io/6cf7600-12.png)
13. Click **Generate**. Copy this token as it's required in the Sigma UI.

    ![company apps](https://files.readme.io/95702e6-13.png)
14. In Sigma, go to **Admin > Connections > Databricks**.
15. In the **Host** field, enter the private endpoint you copied when you approved the endpoint, in the following format.

    `<private_endpoint_name>.privatelink.azuredatabricks.net`

    For example, if the private endpoint name is databricks-endpoint, then you would enter the following in the **Host** field.
    `databrick-endpoint.privatelink.azuredatabricks.net`

    > 📘
    >
    > ### To locate the private endpoint's name, go to your Azure portal > **Azure Databricks Workspace > Networking** on the left panel. The private endpoint name is displayed in the **Private Endpoint** column in Private endpoint connections.
16. Paste the **HTTP path** value from Azure into the **HTTP path** field in Sigma.
17. Paste the token you created in Azure and enter into **Access token** field in Sigma.

    ![company apps](https://files.readme.io/e8b6e0c-14.png)
18. [optional] Under **Connection Features,** you can set a connection timeout and/or [enable write access](/docs/set-up-write-access).
19. [optional] In the **Connection queue size** field, define the number of interactive queries Sigma can run on this connection concurrently.
20. Click **Create** in Sigma.

    ![company apps](https://files.readme.io/a8d5ed4-15.png)

---

## PostgreSQL

Private Link can be enabled for Azure Database for PostgreSQL flexible server instances that are created with public access, or single server instances.

**Prerequisites**

To add a Private Link connection, you must complete the following procedures:

* [Provide your PostgreSQL Resource ID to Sigma](#provide-your-postgresql-resource-id-to-sigma)
* [Approve the Private Link in Azure](#approve-the-private-link-in-azure)
* [Configure the PostgreSQL connection in Sigma](#configure-the-postgresql-connection-in-sigma)

### Provide your PostgreSQL Resource ID to Sigma

Sigma requires your **Resource ID** to create a Private Link for your organization. View the Azure documentation on [How to get your Azure Resource ID](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/voice-video-calling/get-resource-id). Copy the **Resource ID** from the **JSON View** of your server page, as well as the **Region Name** for the PostgreSQL warehouse. Send these to your Sigma Account Executive.

### Approve the Private Link in Azure

After Sigma has finished configuring the Private Link, view the Azure documentation on how to [Approve private endpoint connections](https://learn.microsoft.com/en-us/azure/private-link/how-to-approve-private-link-cross-subscription#approve-private-endpoint-connection). Ensure the status of the private endpoint is changed from **Pending** to **Accepted**.

### Configure the PostgreSQL connection in Sigma

Configure a new Private Link PostgreSQL connection in Sigma:

1. Go to **Administration** > **Connections**.
2. Select **Create** **Connection**, then select **PostgreSQL**. Enter a **Name** for your connection.
3. Fill out the fields under **Connection Credentials**:

   |  |  |
   | --- | --- |
   | **Host** | Enter the DNS name provided by your Sigma Account Executive. |
   | **User** | Enter the **Admin Username** found in your Azure PostgreSQL server page. |
   | **Port** | Enter the PostgreSQL port number. |
   | **Password** | Enter the password created to access your data warehouse. |
   | **Database** | Enter the name of your database. |
4. Turn on the **Enable TLS** toggle on to enable TLS encryption for your connection.

## MySQL

**Prerequisites**

* Private Link can only be enabled for Azure Database for MySQL flexible server instances that are created with public access.

To add a Private Link connection, you must complete the following procedures:

* [Provide your MySQL Resource ID to Sigma](#provide-your-mysql-resource-id-to-sigma)
* [Approve the Private Link in Azure](#approve-the-private-link-in-azure-1)
* [Configure the MySQL connection in Sigma](#configure-the-mysql-connection-in-sigma)

### Provide your MySQL Resource ID to Sigma

Sigma requires your **Resource ID** to create a Private Link for your organization. View the Azure documentation on [How to get your Azure Resource ID](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/voice-video-calling/get-resource-id). Copy the **Resource ID** from the **JSON View** of your server page, as well as the **Region Name** for the MySQL warehouse. Send these to your Sigma Account Executive.

### Approve the Private Link in Azure

Once Sigma has finished configuring the Private Link, View the Azure documentation on how to [Approve private endpoint connections](https://learn.microsoft.com/en-us/azure/private-link/how-to-approve-private-link-cross-subscription#approve-private-endpoint-connection). Ensure the status of the private endpoint is changed from **Pending** to **Accepted**.

### Configure the MySQL connection in Sigma

Configure a new Private Link MySQL connection in Sigma:

1. Go to **Administration** > **Connections**.
2. Select **Create** **Connection**, then select **MySQL**. Enter a **Name** for your connection.
3. Fill out the fields under **Connection Credentials**:

   |  |  |
   | --- | --- |
   | **Host** | Enter the DNS name provided by your Sigma Account Executive. |
   | **User** | Enter the **Admin Username** found in your MySQL server page. |
   | **Port** | Enter the MySQL port number. |
   | **Password** | Enter the password created to access your data warehouse. |
   | **Database** | Enter the name of your database. |
4. Turn on the **Enable TLS** toggle on to enable TLS encryption for your connection.

## Azure SQL Database, Azure SQL Managed Instance, or SQL Server 2022

Reach to out to your Sigma Account Executive for more information on setting up Private Link for Azure SQL Database, Azure SQL Managed Instance or SQL Server 2022 connections.

Updated 3 days ago

---

[AWS PrivateLink Connections](/docs/aws-privatelink-connections)[Troubleshoot your connection](/docs/troubleshoot-your-connection)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Introduction](#introduction)
  + [Create Private Link connection for your data warehouse](#create-private-link-connection-for-your-data-warehouse)
  + [Snowflake](#snowflake)
  + - [Step 1: Configure your Snowflake internal stage](#step-1-configure-your-snowflake-internal-stage)
    - [Step 2: Provide Snowflake information to Sigma](#step-2-provide-snowflake-information-to-sigma)
    - [Step 3: Configure Snowflake connection in Sigma](#step-3-configure-snowflake-connection-in-sigma)
    - [Add a Private Link to a Snowflake internal stage](#add-a-private-link-to-a-snowflake-internal-stage)
  + [Databricks](#databricks)
  + - [Provide Databricks Resource ID to Sigma](#provide-databricks-resource-id-to-sigma)
    - [Private Link approval](#private-link-approval)
    - [Configure Databricks Connection](#configure-databricks-connection)
  + [PostgreSQL](#postgresql)
  + - [Provide your PostgreSQL Resource ID to Sigma](#provide-your-postgresql-resource-id-to-sigma)
    - [Approve the Private Link in Azure](#approve-the-private-link-in-azure)
    - [Configure the PostgreSQL connection in Sigma](#configure-the-postgresql-connection-in-sigma)
  + [MySQL](#mysql)
  + - [Provide your MySQL Resource ID to Sigma](#provide-your-mysql-resource-id-to-sigma)
    - [Approve the Private Link in Azure](#approve-the-private-link-in-azure-1)
    - [Configure the MySQL connection in Sigma](#configure-the-mysql-connection-in-sigma)
  + [Azure SQL Database, Azure SQL Managed Instance, or SQL Server 2022](#azure-sql-database-azure-sql-managed-instance-or-sql-server-2022)