# Set up a Databricks connection for Python (Beta)

# Set up a Databricks connection for Python (Beta)

> 🚩
>
> This documentation describes one or more public beta features that are in development. Beta features are subject to quick, iterative changes; therefore the current user experience in the Sigma service can differ from the information provided in this page.
>
> This page should not be considered official published documentation until Sigma removes this notice and the beta flag on the corresponding feature(s) in the Sigma service. For the full beta feature disclaimer, see [Beta features](/docs/sigma-product-releases#beta-features).

If you set up Python with your Databricks connection, you can write and run Python code in Sigma as a notebook-style experience, elevating the level of complex analysis that you can perform on your data and reducing friction between business analytics and data science.

After setting up your connection for Python, you can [write and run Python code in a Sigma workbook](/docs/write-and-run-python-code).

## Requirements

To set up your Databricks connection for Python, the following requirements must be met.

In your Sigma organization:

* You must be assigned the **Admin** [account type](/docs/user-account-types).

In Databricks:

* You must have access to an all-purpose compute resource, or create one. To create one, you must either be an Admin or have the `Allow unrestricted cluster creation` user entitlement. See [Connect to all-purpose and jobs compute](https://docs.databricks.com/aws/en/compute/use-compute) in the Databricks documentation.

  > 💡
  >
  > If you create an all-purpose compute resource to run Python from Sigma, start by creating a small cluster. Monitor usage and set up auto-scaling or change the size of the cluster based on usage.
* If you run Databricks on Azure, you must be running Databricks Runtime LTS 11.3 or higher. See [Databricks Runtime release notes versions and compatibility](https://learn.microsoft.com/en-us/azure/databricks/release-notes/runtime/) in the Databricks documentation.

Additional requirements apply to set up a new Databricks connection. See [Connect to Databricks](/docs/connect-to-databricks).

## Limitations

* You must have a write-back destination set up to use Python, but your write-back destination cannot use default storage.
* Set a reasonable automatic termination policy for the all-purpose compute. Sigma recommends a policy of at least 3 hours, based on your expected usage. If the all-purpose compute cluster is terminated, users assigned an account type with the **Write Python** permission enabled can restart the cluster.

## Set up a Databricks connection to work with Python

To create or modify a Databricks connection in Sigma to work with Python, complete the steps to [connect to Databricks](/docs/connect-to-databricks) and complete additional configuration steps in both Databricks and Sigma.

### Configure Databricks

After you complete the steps to [Configure Databricks](/docs/connect-to-databricks#configure-databricks), perform additional steps specific to configure Databricks for use with Sigma and Python:

1. Identify the cluster ID of the all-purpose compute cluster. See [Get identifiers for workspace objects](https://docs.databricks.com/aws/en/workspace/workspace-details#cluster-url-and-id) in the Databricks documentation.
2. Confirm that the access token or service principal you plan to use to connect to this compute has `CAN RESTART` permissions for the compute resource. See [Compute ACLs](https://docs.databricks.com/aws/en/security/auth/access-control/#compute-acls) in the Access control lists topic in the Databricks documentation.

   > 💡
   >
   > Sigma requires `CAN RESTART` to allow users to restart a terminated compute cluster from a workbook. If you do not want to grant this level of permission to the access token or service principal, use `CAN ATTACH TO` instead and manage the cluster in the Databricks workspace interface.
3. Install libraries on your Databricks cluster for use in Python. See [Cluster libraries](https://docs.databricks.com/aws/en/libraries/cluster-libraries) in the Databricks documentation. Several libraries, such as DBUtils and pyspark, are included by default.

   Sigma recommends installing the latest version of the libraries. Other libraries such as pandas, pyflakes, numpy, scipy, requests, and others might be useful.
4. To allow API calls made from Python code in Sigma, ensure the network configuration for the cluster allows egress to the relevant API endpoints.

### Create or update a Databricks connection in Sigma

After you complete the steps to [Create a Databricks connection in Sigma](/docs/connect-to-databricks#create-a-databricks-connection-in-sigma), but before you finish creating your connection, complete the steps to set up Python:

1. In the **Python** section, turn on the toggle for **Enable Python queries**.
2. For **Compute cluster**, specify the **Cluster ID** of your all-purpose compute cluster.
3. Follow the steps to [Finish creating your connection](/docs/connect-to-databricks#finish-creating-your-connection).

After you set up Python for Databricks, users can [write and run Python code in a Sigma workbook](/docs/write-and-run-python-code).

Updated 3 days ago

---

[Connect to Databricks](/docs/connect-to-databricks)[Redshift](/docs/redshift)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Limitations](#limitations)
  + [Set up a Databricks connection to work with Python](#set-up-a-databricks-connection-to-work-with-python)
  + - [Configure Databricks](#configure-databricks)
    - [Create or update a Databricks connection in Sigma](#create-or-update-a-databricks-connection-in-sigma)