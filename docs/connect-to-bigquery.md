# Connect to BigQuery

# Connect to BigQuery

Sigma supports secure connections to BigQuery.

This document explains how to connect your organization to a BigQuery warehouse.

> 📘
>
> ### For information about Sigma feature compatibility with BigQuery connections, see [Region, warehouse, and feature support](/docs/region-warehouse-and-feature-support).

## Requirements

* You must be assigned the Admin account type in your Sigma organization. See [Create and manage account types](/docs/user-account-types).
* You must have permission to create a service account on your Google Cloud Project. See [Create service accounts](https://cloud.google.com/iam/docs/service-accounts-create#permissions) in the Google Cloud documentation.

You must also determine what permissions to grant to the account that you plan to use to connect to BigQuery. Avoid granting excessive permissions. For example, the account does not require SYSADMIN-level access.

## Create a BigQuery service account

Before you connect to Sigma, you must visit your Google Cloud Platform (GCP) console to create a service account and generate a JSON private key for your BigQuery instance. See [Service accounts](https://cloud.google.com/compute/docs/access/service-accounts) and [Authenticate to Cloud Storage](https://cloud.google.com/storage/docs/authentication#apiauth) in the Google Cloud documentation.

### What is a service account, and why do I need one?

A GCP service account is a type of Google account that can securely communicate over Google APIs on your behalf. The service account functions as a middleman between Sigma and your BigQuery warehouse.

### Account permissions / roles

When creating your service account, you must grant it specific access permissions called roles.

To run BigQuery with Sigma, grant your service account the following roles:

* BigQuery Data Viewer
* BigQuery Job User
* BigQuery Data Editor (This role is only required if you intend to [enable write access](/docs/set-up-write-access) on your connection.)

For more details about roles in BigQuery, see [IAM roles and permissions index](https://cloud.google.com/iam/docs/roles-permissions) in the Google Cloud documentation.

### Create a service account

We have included instructions below to create your service account. However, please be aware that this guide may not always be up to date with the most recent GCP console changes, as GCP is not managed by Sigma.

For Google’s instructions, visit [Create a VM that uses a user-managed service account](https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances).

1. Log into your GCP console.
2. Open the Navigation menu.
3. Hover over **IAM & Admin** and select **Service Accounts** from the submenu.
4. Click **+ CREATE SERVICE ACCOUNT** in the service accounts header.
5. Under **Service account details**, add an account name, ID, and optional description.  
   Click **CREATE**.
6. Under **Service account permissions**, add the following roles:
   * BigQuery Data Viewer
   * BigQuery Job User
   * BigQuery Data Editor - This role is only required if you intend to [enable write access](/docs/set-up-write-access) on your connection.
7. Click **CONTINUE.**
8. [optional] Under **Grant users access**.... you may choose to grant other users access to your new service account.  
   *This step is not necessary for connecting to Sigma*.
9. Click **+ CREATE KEY** to create a **json private** [key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys).  
   A file will be downloaded to your computer, which you will later use when [connecting to Sigma (Step 7)](/docs/connect-to-bigquery#create-a-connection-in-sigma).

## Create a Connection in Sigma

1. In Sigma, open **Administration** > **Connections.**
2. Click **Create Connection**.
3. In the **Connection details**, specify the following:

   |  |  |
   | --- | --- |
   | **Name** | Enter a **Name** for the new connection. Sigma displays this name in the connection list. |
   | **Type** | Select **BigQuery**. |
4. Under **Billing project ID**, enter your GCP ‘Project ID’. This can be found under ‘Project Info’ on your GCP console dashboard. [Find your project id.](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)  
   **Note**: Grant the service account the “BigQuery Data Viewer“ role for the project's datasets. See BigQuery documentation on [Control access to resources with IAM: Grant access to a resource](https://cloud.google.com/bigquery/docs/control-access-to-resources-iam#grant_access_to_a_dataset).
5. Under **Service account**, paste the [JSON key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys) you created when setting up your service account. The key is located in the `.json` file that was downloaded to your computer when you created the service account.
6. [Optional] Under **Additional project IDs**, you can add additional BigQuery project IDs to the same connection. Separate multiple IDs with a comma. For example, `project-id-001, project-id-002`

   > 📘
   >
   > ### The service account must be granted the BigQuery Data Viewer role for each project's datasets. For more details, see [Control access to resources with IAM: Grant access to a resource](https://cloud.google.com/bigquery/docs/control-access-to-resources-iam#grant_access_to_a_dataset) in the Google Cloud documentation.
7. Under **Connection Features**, specify the following:

   Connection timeout
   :   The time before timeout (or cancellation), in seconds, that Sigma waits for the query to return results.
   :   Default is 120, or 2 minutes.
   :   Maximum is 600, or 10 minutes.

   Use friendly names
   :   This toggle makes column names from the data source more readable.
   :   For example, a database column ORDER\_NUMBER or OrderNumber appears as Order Number.
   :   On by default.
8. Follow the steps to [enable write access](/docs/set-up-write-access). Write access is required to use input tables, upload CSV data, materialization, and more. The service account must be granted the BigQuery Data Editor role.

   > 💡
   >
   > ### Configure a separate database or a database and schema combination for write-access purposes. By design, the destination that you configure for write access is not visible in the Sigma connection explorer pane. The data that Sigma writes to this destination is not formatted in a way that can be browsed and used.
9. After completing the form, click **Create**.

## Confirm your connection

After you have created your connection, you can confirm that your data is accessible by visiting the **Connections** section in the left hand navigation panel of Sigma Home.

1. Go to Sigma Home.
2. From the left hand navigation panel, select the new warehouse connection.
3. Explore your connection’s schemas and tables, confirming the connection was successful. See [Review and manage your data catalog](/docs/manage-data-catalog).

Updated 3 days ago

---

Related resources

* [Set up write access](/docs/set-up-write-access)
* [Data permissions](/docs/data-permissions)
* [Google Cloud - Service Accounts](https://cloud.google.com/compute/docs/access/service-accounts)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Create a BigQuery service account](#create-a-bigquery-service-account)
  + - [What is a service account, and why do I need one?](#what-is-a-service-account-and-why-do-i-need-one)
    - [Account permissions / roles](#account-permissions--roles)
    - [Create a service account](#create-a-service-account)
  + [Create a Connection in Sigma](#create-a-connection-in-sigma)
  + [Confirm your connection](#confirm-your-connection)