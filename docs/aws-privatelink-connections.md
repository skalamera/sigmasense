# AWS PrivateLink Connections

# AWS PrivateLink Connections

If your Sigma organization runs on Amazon Web Services (AWS), you can securely connect to your data using AWS PrivateLink. AWS PrivateLink is a security feature that allows users to create connections between your AWS [Virtual Private Cloud](https://aws.amazon.com/vpc/) (VPC) without sending traffic over the public internet. Sigma can connect to cloud data platforms via AWS PrivateLink in all Amazon regions with PrivateLink support.

For more information on the security advantages and internals of PrivateLink, see the AWS documentation on [AWS PrivateLink](https://aws.amazon.com/privatelink/).

This document explains how to set up AWS PrivateLink connections from Sigma to your data platform.

## System and user requirements

The following are required for all AWS PrivateLink connections:

* A Sigma organization running on AWS.

> 🚧
>
> ### Note: Your Sigma organization must be on the same cloud as your data platform to use private link. If your organization uses Azure, see [Azure Private Link connections](/docs/azure-private-link-connections).

* You must be assigned the Admin account type in Sigma. See [User account types](/docs/user-account-types).
* An AWS VPC-deployed Snowflake (self-managed or VPS), Redshift, MySQL, SQL Server 2022, Starburst, Postgres data warehouse, or custom proxy server in any AWS region.

> 📘
>
> ### This feature does not support BigQuery warehouses or self-managed warehouses running on Azure, GCP, or VMWare clouds.

Additional requirements may also apply depending on the data platform and specific PrivateLink configuration method, and will be listed in the corresponding section below.

## Connecting to your data with PrivateLink

The steps below cover both updating existing public connections to use PrivateLink, and creating a new connection to use PrivateLink. The process to set up PrivateLink depends on the data platform your organization uses:

* [Snowflake](/docs/aws-privatelink-connections#snowflake)
* [Redshift](/docs/aws-privatelink-connections#redshift)
* [Databricks](/docs/aws-privatelink-connections#databricks)
* [MySQL, SQL Server 2022, PostgreSQL, Starburst, and custom proxy servers (e.g. secuPi)](/docs/aws-privatelink-connections#mysql-sql-server-2022-postgresql-starburst-or-custom-proxy-servers)

## Snowflake

Connecting to Snowflake via PrivateLink depends on your Snowflake configurations:

* If you are a Snowflake customer with the [Business Critical](https://docs.snowflake.com/en/user-guide/intro-editions#business-critical-edition) (or higher) edition, and do not use a Virtual Private Server (VPS) or proxy server, you might be able to connect via [Snowflake’s PrivateLink integration](https://docs.snowflake.com/en/user-guide/admin-security-privatelink). See [Connect with Snowflake’s PrivateLink integration](/docs/aws-privatelink-connections#connect-with-snowflakes-privatelink-integration).
* If you are a Snowflake customer and use a Virtual Private Server (VPS) or proxy server, see [Connect to Snowflake via your own VPC](/docs/aws-privatelink-connections#connect-to-snowflake-via-your-own-vpc).

### Connect with Snowflake’s PrivateLink Integration

Snowflake’s PrivateLink Integration allows Sigma to create a secure connection over PrivateLink directly to the Snowflake VPC that is housing your data. Traffic between Sigma and your Snowflake warehouse will travel exclusively on the AWS Backbone. You do not need an Amazon account or VPC of your own - only the warehouse managed by Snowflake must reside in an AWS VPC.

#### Additional requirements

* Snowflake requires [Business Critical](https://docs.snowflake.com/en/user-guide/intro-editions#business-critical-edition) edition (or higher) for PrivateLink support.
* Confirm your Sigma organization’s eligibility with your Sigma Account Executive.
* If your Snowflake account uses VPS or you connect Sigma to Snowflake with a proxy server, you cannot use Snowflake’s PrivateLink integration. See [Connect to Snowflake via your own VPC](/docs/aws-privatelink-connections#connect-to-snowflake-via-your-own-vpc).
* You must be a Snowflake account administrator (your system role should be `ACCOUNTADMIN`).

#### Connect using Snowflake's PrivateLink integration

To connect with Snowflake’s PrivateLink integration:

1. In Snowflake, call `SYSTEM$GET_PRIVATELINK_CONFIG`. Record the following values:

   * `privatelink-vpce-id`: This is your VPC Endpoint service name, formatted similarly to `com.amazonaws.vpce.<region>.vpce-svc-xxxxxxxxxx`
   * `privatelink-account-url`: This is your Snowflake PrivateLink account URL, formatted similarly to `<privatelink-account-name>.<aws-region>.privatelink.snowflakecomputing.com`
2. Contact your Sigma Account Executive or Customer Account Manager to install your PrivateLink connection with Sigma and provide them with the service name and URL. Sigma will contact you once installation is complete.
3. Update your connection to use PrivateLink:

   * For existing connections to Snowflake:
     1. Go to **Home** > **Administration** > **Connections**.
     2. Select your existing connection, then select **Edit**.
     3. In the **Account** field, enter the PrivateLink account URL you recorded in Step 1, following the format `<privatelink-account-name>.<aws-region>.privatelink`.
     4. Select **Save**.
   > 📘
   >
   > ### Existing connections will continue to work, but will not use PrivateLink until this step has been completed.

   * For new connections to Snowflake: Create a new connection using the steps in [Connect to Snowflake](/docs/connect-to-snowflake). When filling out the **Account** field, enter the PrivateLink account URL you recorded in Step 1, following the format `<privatelink-account-name>.<aws-region>.privatelink`.

   ![](https://files.readme.io/74e4420e5fde0485e6293a59b1293a8d9486ecc49dee93c1c50b11e474f69cd2-accountfieldprivatelink.png)

### Connect to Snowflake via your own VPC

To connect to PrivateLink for Snowflake:

1. Create a VPC endpoint service. To create an endpoint service, see the AWS documentation on [Create a service powered by AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/create-endpoint-service.html).
2. Make the newly created VPC endpoint service discoverable to Sigma. To make your endpoint discoverable, see [Manage permissions](https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.html#add-remove-permissions) in the the AWS documentation.

   You need Sigma’s Amazon Resource Name (ARN) to configure your endpoint service. Enter the following ARN in the **Allow principals** configuration of your VPC endpoint service: `arn:aws:iam::185497759670:role/cdktf-operator`.

   > 📘
   >
   > ### While existing configurations with `arn:aws:iam::185497759670:role/root configurations` will continue to work for all users, using `role/cdktf-operator` is recommended.
3. Contact your Sigma Account Executive or Customer Account Manager to install your PrivateLink connection. They will need the following:

   * Your endpoint’s VPC endpoint service name (formatted similarly to `com.amazonaws.vpce.<region>.vpce-svc-xxxx`).
   * Availability zone IDs of your load balancer (formatted similarly to `use1-az1`) .
   * Account URL (formatted similarly to `<account-name>.<region>.privatelink.snowflakecomputing.com`).
4. Installation may take up to a few days. Sigma will contact you once installation is complete, and will provide an account URL name for your connection (required for later configuration).
5. After installation, if your VPC Endpoint Service requires you to manually accept new connections, you will need to accept Sigma’s new endpoint connection. See the AWS documentation on [Accept or reject connection requests](https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.html#accept-reject-connection-requests).
6. Update your connection to use PrivateLink:

   * For existing connections to a data platform:

     1. Go to **Home** > **Administration** > **Connections**.
     2. Select your desired connection, then select **Edit**.
     3. In the **Account** field, enter the account URL name provided to you by Sigma.
     4. Select **Save**.
     > 📘
     >
     > ### Existing connections to data platforms will continue to work, but will not use PrivateLink until this step has been completed.
   * For new data platform connections: Connect to your data platform using the steps in [Connect to data sources](/docs/connect-to-data-sources). When filling out the **Account** field, use the new account URL provided to you by Sigma.

## Redshift

Connecting to Redshift via PrivateLink depends on your Redshift configurations:

* If your Redshift cluster is the RA3-instance type and has cluster relocation turned on, Sigma recommends connecting via Redshift managed VPC endpoints. See [Connect with Redshift managed VPC endpoints](/docs/aws-privatelink-connections#connect-with-redshift-managed-vpc-endpoints).
* If your Redshift cluster is not of RA3-instance type, has cluster relocation turned off, or if you prefer not to use Redshift managed endpoints, see [Connect to Redshift via your own VPC](/docs/aws-privatelink-connections#connect-to-redshift-via-your-own-vpc).

### Connect with Redshift managed VPC endpoints

Redshift-managed VPC endpoints allow you to add additional security to your clusters without creating additional infrastructure. For more information, see the AWS documentation on [Redshift managed VPC endpoints](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-cross-vpc.html).

#### Additional requirements

* Have an existing Redshift instance.
* The cluster to access must be the RA3-instance type.
* The cluster to access must have cluster relocation turned on. See the AWS documentation on [Relocating a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-recovery.html#using-recovery).

#### Set up PrivateLink on Redshift managed VPC endpoints

To set up Redshift managed VPC endpoints:

1. Authorize Sigma access to your Redshift instance. See the AWS documentation on [Granting access to a VPC](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-cross-vpc-console-grantor.html). The AWS account ID to grant access to is `185497759670`. Depending on the location of your Redshift cluster, grant access to the following VPC IDs:

   | Location | VPC ID |
   | --- | --- |
   | us-east-1 | `vpc-03e998398a2b8d7d4` |
   | us-east-2 | `vpc-0eb5c451f6d93b9b0` |
   | us-west-1 | `vpc-0b98df9ea218bbae3` |
   | us-west-2 | `vpc-0ebc060057f91792c` |
   | ap-southeast-2 | `vpc-0173a781cad403b87` |
   | ap-northeast-1 | `vpc-01d69d4176bf329d4` |
   | eu-central-1 | `vpc-03967ee832f14c234` |
   | eu-west-1 | `vpc-0ef690315d8c934e9` |
   | eu-west-2 | `vpc-0d89ee0ccf9f3eeb7` |

   If your Redshift cluster's region is not listed above, contact Sigma Support for assistance.
2. Provide the following information to Sigma:

   * Redshift cluster identifier
   * AWS region of your Redshift cluster
   * AWS account number
   * Availability Zone ID(s): Formatted similarly to `use1-az1`. See the AWS documentation on [Availability Zone IDs for your AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/working-with-az-ids.html).
   * [optional] Desired DNS name: Your desired subdomain name for the private link account URL. The name should be descriptive and identifying. For example, you might want to format it similarly to `<name>-<env>-<region>-<index_number>`.
3. Sigma will reach out once the private link has been created.

### Connect to Redshift via your own VPC

1. Create a VPC endpoint service. To create an endpoint service, see the AWS documentation on [Create a service powered by AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/create-endpoint-service.html).
2. Make the newly created VPC endpoint service discoverable to Sigma. To make your endpoint discoverable, see the AWS documentation on how to [Manage permissions](https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.html#add-remove-permissions).\   
   You will need Sigma’s Amazon Resource Name (ARN) to configure your endpoint service. Enter the following ARN in the **Allow principals** configuration of your VPC endpoint service: `arn:aws:iam::185497759670:role/cdktf-operator`.

> 📘
>
> While existing configurations with `arn:aws:iam::185497759670:role/root configurations` will continue to work for all users, using `role/cdktf-operator` is recommended.

3. Contact your Sigma Account Executive, Customer Account Manager, or Sigma Support to install your PrivateLink connection. They will need the following:
   * Your endpoint’s VPC endpoint service name (formatted similarly to `com.amazonaws.vpce.<region>.vpce-svc-xxxx`).
   * Availability zone IDs of your load balancer (formatted similarly to `use1-az1`) .
   * [optional] Desired DNS name: Your desired subdomain name for the private link account URL. The name should be descriptive and identifying. For example, you might want to format it similarly to `<cdw_name>-<env>-<region>-<index_number>`. If you do not provide this value, Sigma Support will choose it and provide it to you.
4. Installation may take up to a few days. Sigma will contact you once installation is complete, and will provide an account URL name for your connection (required for later configuration).
5. After installation, if your VPC Endpoint Service requires you to manually accept new connections, you will need to accept Sigma’s new endpoint connection. See the AWS documentation on [Accept or reject connection requests](https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.html#accept-reject-connection-requests).
6. Update your connection to use PrivateLink:

* For existing connections to a data platform:
  1. Go to **Home** > **Administration** > **Connections**.
  2. Select your desired connection, then select **Edit**.
  3. In the **Host** field, enter the DNS name from step 3 followed by `.privatelink.sigma.internal`. For example, `<cdw_name>-<env>-<region>-<index_number>.privatelink.sigma.internal`.
  4. Select **Save**.

> 📘
>
> Existing connections to data platforms will continue to work, but will not use PrivateLink until this step has been completed.

* For new data platform connections: Connect to your data platform using the steps in [Connect to data sources](/docs/connect-to-data-sources). When filling out the **Host** field, enter the DNS name from step 3 followed by `.privatelink.sigma.internal`. For example, `<cdw_name>-<env>-<region>-<index_number>.privatelink.sigma.internal`.

## Databricks

### Additional requirements

* Your Databricks platform must be [Enterprise tier](https://www.databricks.com/product/pricing/platform-addons).
* Your Databricks workspace **cannot** be in the `us-west-1` region.
* Your Databricks workspace must be customer-managed, not Databricks-managed:
  + If you do not see a **Network** thumbnail when accessing your Databricks workspace, your workspace is Databricks-managed.
  + If you see a **Network** thumbnail when accessing your Databricks workspace, it is customer-managed.

### Connect to Databricks with PrivateLink

To connect to Databricks with PrivateLink:

1. Create two VPC endpoints in your AWS account. See [Create a VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) in the AWS documentation. For the endpoint service names needed to create VPC endpoints in your region, see the Databricks documentation on [PrivateLink VPC endpoint services](https://docs.databricks.com/aws/en/resources/ip-domain-region#privatelink-vpc-endpoint-services). You need to create:

   * One **Workspace (including REST API)** VPC endpoint
   * One **Secure cluster connectivity relay** VPC endpoint
2. In Databricks, you will need to register the 2 VPC endpoints you just created, so you can use them in your network configurations. See the Databricks documentation on how to [Manage VPC endpoint registrations](https://docs.databricks.com/aws/en/security/network/classic/vpc-endpoints).
3. In Databricks, you will need to register the Sigma VPC endpoint for your region. See the Databricks documentation on how to [Manage VPC endpoint registrations](https://docs.databricks.com/aws/en/security/network/classic/vpc-endpoints).

   Sigma's VPC endpoints are listed in the table below. If your region is not listed, contact your Sigma Account Executive or Customer Account Manager:

   | Region | WORKSPACE\_ACCESS Endpoint |
   | --- | --- |
   | us-east-2 | `vpce-01e5bcfb542cc064b` |
   | us-east-1 | `vpce-01e5ee810ad38e87a` |
   | us-west-2 | `vpce-0f7f1c9eb781e5ee0` |
   | ap-southeast-2 | `vpce-0ea8cc8aaac99003c` |
   | eu-central-1 | `vpce-042d25a7829e28994` |
   | eu-west-1 | `vpce-089a8efa3ea799d03` |
   | eu-west-2 | `vpce-0e2cc626d12fd41a5` |
   | ap-northeast-1 | `vpce-05a3ec6e4605fdd94` |
4. In Databricks, create a private access settings object to allow PrivateLink connectivity. See the Databricks documentation on [Create a private access settings object](https://docs.databricks.com/aws/en/security/network/classic/private-access-settings#create-a-private-access-settings-object). Ensure the following configurations are set:

   * **Public access enabled**: False
   * **Private access level**: Account
5. In Databricks, create a new network configuration. See the Databricks documentation on [Create a network configuration](https://docs.databricks.com/aws/en/admin/account-settings-e2/networks#create-a-network-configuration). Ensure the following configurations are used:

   * Use the **VPC**, **Subnet IDs**, and **Security Group IDs** of your desired Databricks workspace.
   * For the **VPC endpoint for secure cluster connectivity relay** and **VPC endpoint for REST APIs fields**, use the AWS endpoints you created in your AWS account.
6. Update your Databricks workspace to include the new network configuration and private access settings. See the Databricks documentation on [Advanced configurations](https://docs.databricks.com/aws/en/admin/workspace/create-uc-workspace#advanced).
7. Contact your Sigma Account Executive or Customer Account Manager to install your PrivateLink connection. They will need the following information about your Databricks workspace:

   * **Deployment name** (example: dbc-05a998877-123d)
   * **Workspace region** (example: us-east-1)

   Installation may take up to a few days. Sigma will contact you once installation is complete, and will provide an host URL for your connection. If you have multiple workspaces, you will need to provide the **Deployment name** for each workspace you want to connect to. If you add additional workspaces in the future, and want to connect to them through Sigma, you will need to request an update to your Sigma PrivateLink setup.
8. Update your connection to use PrivateLink:

   * For existing connections to a data platform:

     1. Go to **Home** > **Administration** > **Connections**.
     2. Select your desired connection, then select **Edit**.
     3. In the **Host** field, enter the host URL provided to you by Sigma in step 7. The URL should end with `privatelink.databricks.com`.
     4. Select **Save**.
   > 📘
   >
   > ### Existing connections to data platforms will continue to work, but will not use PrivateLink until this step has been completed.

   * For new data platform connections: Connect to your data platform using the steps in [Connect to data sources](/docs/connect-to-data-sources). When filling out the **Host** field, use the host URL provided to you by Sigma in step 7.

## MySQL, SQL Server 2022, PostgreSQL, Starburst, or custom proxy servers

For organizations using MySQL, SQL Server 2022, Starburst, PostgreSQL, or a custom proxy server (e.g. secuPi), use the following steps to connect with AWS PrivateLink:

1. Create a VPC endpoint service. To create an endpoint service, see the AWS documentation on [Create a service powered by AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/create-endpoint-service.html).
2. Make the newly created VPC endpoint service discoverable to Sigma. To make your endpoint discoverable, see the AWS documentation on how to [Manage permissions](https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.html#add-remove-permissions).\   
   You will need Sigma’s Amazon Resource Name (ARN) to configure your endpoint service. Enter the following ARN in the **Allow principals** configuration of your VPC endpoint service: `arn:aws:iam::185497759670:role/cdktf-operator`.

> 📘
>
> While existing configurations with `arn:aws:iam::185497759670:role/root configurations` will continue to work for all users, using `role/cdktf-operator` is recommended.

3. Contact your Sigma Account Executive, Customer Account Manager, or Sigma Support to install your PrivateLink connection. They will need the following:
   * Your endpoint’s VPC endpoint service name (formatted similarly to `com.amazonaws.vpce.<region>.vpce-svc-xxxx`).
   * Availability zone IDs of your load balancer (formatted similarly to `use1-az1`) .
   * [optional] Desired DNS name: Your desired subdomain name for the private link account URL. The name should be descriptive and identifying. For example, you might want to format it similarly to `<cdw_name>-<env>-<region>-<index_number>`. If you do not provide this value, Sigma Support will choose it and provide it to you.
4. Installation may take up to a few days. Sigma will contact you once installation is complete, and will provide an account URL name for your connection (required for later configuration).
5. After installation, if your VPC Endpoint Service requires you to manually accept new connections, you will need to accept Sigma’s new endpoint connection. See the AWS documentation on [Accept or reject connection requests](https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.html#accept-reject-connection-requests).
6. Update your connection to use PrivateLink:

* For existing connections to a data platform:
  1. Go to **Home** > **Administration** > **Connections**.
  2. Select your desired connection, then select **Edit**.
  3. In the **Host** field, enter the DNS name from step 3 followed by `.privatelink.sigma.internal`. For example, `<cdw_name>-<env>-<region>-<index_number>.privatelink.sigma.internal`.
  4. Select **Save**.

> 📘
>
> Existing connections to data platforms will continue to work, but will not use PrivateLink until this step has been completed.

* For new data platform connections: Connect to your data platform using the steps in [Connect to data sources](/docs/connect-to-data-sources). When filling out the **Host** field, enter the DNS name from step 3 followed by `.privatelink.sigma.internal`. For example, `<cdw_name>-<env>-<region>-<index_number>.privatelink.sigma.internal`.

Updated 3 days ago

---

Related resources

* [Connect to data sources](/docs/connect-to-data-sources)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Connecting to your data with PrivateLink](#connecting-to-your-data-with-privatelink)
  + [Snowflake](#snowflake)
  + - [Connect with Snowflake’s PrivateLink Integration](#connect-with-snowflakes-privatelink-integration)
    - [Connect to Snowflake via your own VPC](#connect-to-snowflake-via-your-own-vpc)
  + [Redshift](#redshift)
  + - [Connect with Redshift managed VPC endpoints](#connect-with-redshift-managed-vpc-endpoints)
    - [Connect to Redshift via your own VPC](#connect-to-redshift-via-your-own-vpc)
  + [Databricks](#databricks)
  + - [Additional requirements](#additional-requirements-2)
    - [Connect to Databricks with PrivateLink](#connect-to-databricks-with-privatelink)
  + [MySQL, SQL Server 2022, PostgreSQL, Starburst, or custom proxy servers](#mysql-sql-server-2022-postgresql-starburst-or-custom-proxy-servers)