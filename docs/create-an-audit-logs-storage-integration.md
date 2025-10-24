# Manage an audit logs storage integration

# Manage an audit logs storage integration

The *Sigma Audit Logs* connection stores entries for 30 days by default, but you can retain audit log data for extended periods by [exporting it to cloud storage](/docs/export-audit-log-data-to-cloud-storage). To ensure secure, scalable, and compliant exports, set up an audit log storage integration using role-based access control (RBAC) with appropriate permissions.

This document explains how to create, update or delete a storage integration for exporting audit log data to an Amazon S3 bucket, Azure container, or Google Cloud Storage (GCS) bucket. For more information about audit logging with Sigma, see the following:

* [Enable or disable audit logging](/docs/enable-audit-logging)
* [Access and explore audit logs](/docs/access-and-explore-audit-logs)
* [Audit log events and metadata](/docs/audit-log-events-and-metadata)
* [Export audit log data to cloud storage](/docs/export-audit-log-data-to-cloud-storage)

## User requirements

The ability to create and edit audit log storage integrations requires the following:

* You must be assigned the **Admin** account type in Sigma.
* You must be granted administrative permissions in Amazon Web Services (AWS), Microsoft Azure, or Google Cloud (GCP).

## Storage integration requirements

Sigma’s audit log data is provided by a Sigma-managed Snowflake connection. Therefore, the audit log storage integration creates an interface between Snowflake and your cloud storage platform. The integration, however, does not require your organization to maintain its own Snowflake account, and no part of the following procedures requires configuration within Snowflake.

Much of the storage integration configuration involves completing steps within your cloud storage platform. As these workflows are maintained and updated by a third party, the steps detailed in this document may differ from the cloud storage platform’s current UI and terminology.

If you allowlist IP addresses in your cloud storage platform, make sure to allow ingress from the IP addresses used by Snowflake. See [FAQ: What IP address range does Snowflake use?](https://community.snowflake.com/s/article/faq-what-ip-address-range-does-snowflake-use) in the Snowflake Community.

## Configure a storage integration to access AWS

To configure a storage integration that allows Sigma to write audit log data to AWS, you must complete the following procedures:

* [Create an IAM policy in AWS](#create-an-identity-and-access-management-iam-policy-in-aws) to configure access to the S3 bucket.
* [Create a custom IAM role in AWS](#create-a-custom-iam-role-in-aws) to grant permissions to the S3 bucket.
* [Add an AWS integration in Sigma](#add-an-aws-integration-in-sigma) to enable scheduled audit log exports to cloud storage.
* [Update the custom IAM role in AWS](#update-the-custom-iam-role-in-aws) to grant the IAM user access to the S3 bucket.

### Create an Identity and Access Management (IAM) policy in AWS

Refer to the AWS documentation on [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html#access_policies_create-start). The following is an example JSON policy (with bucket name and folder path prefix placeholders) that meets the Snowflake requirements.

JSON

```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Action": [
                   "s3:ListBucket",
                   "s3:GetBucketLocation"
               ],
               "Effect": "Allow",
               "Resource": "arn:aws:s3:::{{bucket}}",
               "Condition": {
                   "StringLike": {
                       "s3:prefix": [
                           "{{prefix}}/*"
                       ]
                   }
               }
           },
           {
               "Action": [
                   "s3:PutObject",
                   "s3:DeleteObject"
               ],
               "Effect": "Allow",
               "Resource": "arn:aws:s3:::{{bucket}}/{{prefix}}/*"
           }
       ]
   }
```

> 📘
>
> ### You're not required to specify a folder path prefix if the role can upload files to any destination in the S3 bucket.

### Create a custom IAM role in AWS

This IAM role must be created before adding an AWS integration in Sigma as certain AWS credentials are needed to add the integration. Refer to the AWS documentation on how to [Create an IAM role](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/create-iam-role.html). When creating the IAM role, ensure that your configurations match these requirements for the integration with Sigma:

* When prompted for an **Account ID**, you should use your AWS account ID as a temporary value. After you add an [AWS integration in Sigma](#add-an-aws-integration-in-sigma), you must [update the IAM role](#update-the-custom-iam-role-in-aws) to modify the trusted relationship and grant access to Snowflake.
* When creating the role, ensure you select **Require external ID**.
* When prompted for an external ID, enter a placeholder value (for example, `0000`). Sigma generates an external ID when you [add an AWS integration](#add-an-aws-integration-in-sigma), after which you must [update the IAM role](#update-the-custom-iam-role-in-aws).
* When selecting permissions, use the IAM policy you just created.

### Add an AWS integration in Sigma

1. Go to **Administration** > **Account** > **General Settings**.
2. In the **Audit Logging** section, locate the **Create an Audit Logs Storage Integration** setting and click **Add**.

   > 📘
   >
   > ### If the **General Settings** tab doesn’t include an **Audit Logging** section, [contact Support](/docs/sigma-support) or your Sigma Account Executive to enable it for your organization.
3. In the **Create a storage integration for audit logs** modal, provide the AWS credentials:

   1. In the **Cloud Storage** section, select the **AWS** option.
   2. In the **Destination** field, enter the S3 destination folder path that includes the bucket and folder path prefix specified in the [IAM policy](#create-an-iam-policy-in-aws).
   3. In the **Role ARN** field, enter the **Role ARN** value recorded for the [IAM role](#create-a-custom-iam-role-in-aws).
   4. Click **Create storage integration**.
4. Sigma sends a confirmation email when the storage integration is successfully created and an **Amazon Resource Name (ARN)** is available for the IAM user. When this occurs, return to the **Administration** portal to record the credentials for an upcoming step in the integration configuration process:

   1. Go to the **Account** > **General Settings** tab.
   2. In the **Audit Logging** section, locate the **Create an Audit Logs Storage Integration** setting and click **View credentials**.
   3. Reference the **Sigma credentials** section and record the **External ID** and **IAM User ARN** values.

### Update the custom IAM role in AWS

Refer to the AWS documentation on [Editing the trust relationship for an existing role](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/edit_trust.html). When editing the trust policy document, use the **External ID** and **IAM User ARN** values recorded in Sigma. Your JSON configuration may look like:

JSON

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "<iam_user_arn>"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "sts:ExternalId": "<external_id>"
                }
            }
        }
    ]
}
```

To schedule a recurring audit log export, see [Export audit log data to cloud storage](/docs/export-audit-log-data-to-cloud-storage).

## Configure a storage integration to access Azure

To configure a storage integration that allows Sigma to write audit log data to Azure, you must complete the following procedures:

* [Add an Azure integration in Sigma](#add-an-azure-integration-in-sigma) to enable scheduled audit log exports to cloud storage.
* [Accept requested permissions](#accept-requested-permissions) to allow Snowflake to access Azure.
* [Add role assignment in Azure](#add-role-assignment-in-azure) to grant Snowflake access to storage locations.

### Add an Azure integration in Sigma

1. Go to **Administration** > **Account** > **General Settings**.
2. In the **Audit Logging** section, locate the **Create an Audit Logs Storage Integration** setting and click **Add**.

   > 📘
   >
   > ### If the **General Settings** tab doesn’t include an **Audit Logging** section, [contact Support](/docs/sigma-support) or your Sigma Account Executive to enable it for your organization.
3. In the **Create a storage integration for audit logs** modal, provide the Azure credentials:

   1. In the **Cloud Storage** section, select the **Azure** option.
   2. In the **Destination** field, enter a path containing the names of the account, container, and optionally one or more folders. Use the following syntax: `azure://accountname.blob.core.windows.net/containername/folder`. The path should begin with `azure://`, not `https://`.
   3. In the **Tenant ID** field, enter your organization’s Azure account tenant ID.

      > 📘
      >
      > ### For guidance on finding your tenant ID, refer to [How to find your Microsoft Entra tenant ID](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant) in Microsoft’s documentation.
   4. Click **Create storage integration**.
4. Sigma sends a confirmation email when the storage integration is successfully created and the Azure consent URL and multi-tenant app name are available. When this occurs, return to the **Administration** portal to record the credentials for an upcoming step in the integration configuration process:

   1. Go to the **Account** > **General Settings** tab.
   2. In the **Audit Logging** section, locate the **Create an Audit Logs Storage Integration** setting and click **View credentials**.
   3. Record the **Azure Consent URL** and **Azure Multi Tenant App Name** values.

### Accept requested permissions

1. Go to the URL specified by the **Azure Consent URL** value recorded in Sigma.
2. In the Microsoft permissions request page, click **Accept** to grant the Snowflake service principal an access token on specified resources inside your tenant. The page redirects to the Snowflake website.

Continue to [Add role assignment in Azure](#add-role-assigment-in-azure) .

### Add role assignment in Azure

Refer to the Azure documentation on [how to assign Azure roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal).

When assigning roles, ensure that your configurations match these requirements for the integration with Sigma:

* Sigma requires that you select the **Storage Blob Data Contributor** role option.
* When selecting members, enter the **Azure Multi Tenant App Name** value (only the characters preceding the underscore) recorded in Sigma to search for the member.

> 📘
>
> ### As it may take up to 45 minutes for Azure to process the role assignment, exports may not work immediately.

To schedule a recurring audit log export, see [Export audit log data to cloud storage](/docs/export-audit-log-data-to-cloud-storage).

## Configure a storage integration to access GCP

To configure a storage integration that allows Sigma to write audit log data to GCP, you must complete the following procedures:

* [Add a GCP integration in Sigma](#add-a-gcp-integration-in-sigma) to enable scheduled audit log exports to cloud storage.
* [Create a custom IAM role in GCP](#create-a-custom-iam-role-in-gcp) to grant permissions to the GCS bucket.
* [Assign the custom IAM role in GCP](#assign-the-custom-iam-role-in-gcp) to grant the service account access to the GCS bucket.

### Add a GCP integration in Sigma

1. Go to **Administration** > **Account** > **General Settings**.
2. In the **Audit Logging** section, locate the **Create an Audit Logs Storage Integration** setting and click **Add**.

   > 📘
   >
   > ### If the **General Settings** tab doesn’t include an **Audit Logging** section, [contact Support](/docs/sigma-support) or your Sigma Account Executive to enable it for your organization.
3. In the **Create a storage integration for audit logs** modal, provide the GCP credentials:

   1. In the **Cloud Storage** section, select the **GCP** option.
   2. In the **Destination** field, enter the GCS destination folder path. Do not include a filename.
   3. Click **Create storage integration**.
4. Sigma sends a confirmation email when the storage integration is successfully created and the service account credential is available. When this occurs, return to the **Administration** portal to record the credentials for an upcoming step in the integration configuration process:

   1. Go to the **Account** > **General Settings** tab.
   2. In the **Audit Logging** section, locate the **Create an Audit Logs Storage Integration** setting and click **View credentials**.
   3. Reference the **Sigma credentials** section and record the **Service account** value.
   > 📘
   >
   > ### Sigma doesn’t currently support the ability to delete audit logs storage integrations through the **Administration** portal. If you need to delete an existing integration, please [contact Support](/docs/sigma-support).

### Create a custom IAM role in GCP

Refer to the Google Cloud documentation on [creating and managing custom roles](https://cloud.google.com/iam/docs/creating-custom-roles). When creating the role, the following permissions need to be selected:

* storage.objects.create
* storage.objects.delete
* storage.objects.list
* storage.buckets.get

### Assign the custom IAM role in GCP

Refer to the Google Cloud documentation on [authorizing access with IAM](https://cloud.google.com/functions/docs/securing/managing-access-iam#:~:text=In%20the%20New%20principals%20field,a%20role%20drop%2Ddown%20menu/).

* When prompted to fill the **New principals** field, search for and select the **Service account value** from Sigma.
* When selecting a role, select the custom [IAM role](#create-a-custom-iam-role-in-gcp) created for the audit log storage integration.

To schedule a recurring audit log export, see [Export audit log data to cloud storage](/docs/export-audit-log-data-to-cloud-storage).

## Update an audit log storage integration destination

If you're updating the audit log storage integration to a destination within your current cloud provider, follow the steps in this section. If you want to update existing audit log storage integration destination to a different cloud provider, you must first [delete your storage integration](#delete-an-audit-log-storage-integration) and then configure a new storage integration.

1. Select **Administration**, then **Account**.
2. Under **Audit Logging** , select **View credentials**.
3. Select **Edit Destination**.
4. Under **Destination**, enter the your desired storage integration destination. Select **Save**.
5. If you have scheduled exports linked to this storage integration, you can view them by selecting **Linked scheduled exports**. All scheduled exports will be paused by default. To update the export destination to your new storage integration location, select the **Update export destination for all linked scheduled exports instead of pausing** checkbox.
6. Once your integration destination has been successfully updated, you will see a **Cloud destination updated** pop-up. You will also receive a confirmation email.

## Delete an audit log storage integration

To delete your audit log storage integration:

1. Select **Administration**, then **Account**.
2. Under **Audit Logging** , select **View credentials**.
3. Select **Delete integration**.

   > 🚧
   >
   > ### Deleting a storage integration cannot be undone. Once a storage integration is deleted, all scheduled exports linked to the integration will be paused by default.
4. If you have scheduled exports linked to this storage integration, you can view them by selecting **Linked scheduled exports**. To delete all scheduled exports, select the **Delete all linked scheduled exports** checkbox.
5. Select **Delete integration**.
6. Once your integration has been successfully deleted, you will see an **Integration deleted** pop-up. You will also receive a confirmation email.

Updated 3 days ago

---

Related resources

* [Enable or disable audit logging](/docs/enable-audit-logging)
* [Access and explore audit logs](/docs/access-and-explore-audit-logs)
* [Audit log events and metadata](/docs/audit-log-events-and-metadata)
* [Export audit log data to cloud storage](/docs/export-audit-log-data-to-cloud-storage)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Storage integration requirements](#storage-integration-requirements)
  + [Configure a storage integration to access AWS](#configure-a-storage-integration-to-access-aws)
  + - [Create an Identity and Access Management (IAM) policy in AWS](#create-an-identity-and-access-management-iam-policy-in-aws)
    - [Create a custom IAM role in AWS](#create-a-custom-iam-role-in-aws)
    - [Add an AWS integration in Sigma](#add-an-aws-integration-in-sigma)
    - [Update the custom IAM role in AWS](#update-the-custom-iam-role-in-aws)
  + [Configure a storage integration to access Azure](#configure-a-storage-integration-to-access-azure)
  + - [Add an Azure integration in Sigma](#add-an-azure-integration-in-sigma)
    - [Accept requested permissions](#accept-requested-permissions)
    - [Add role assignment in Azure](#add-role-assignment-in-azure)
  + [Configure a storage integration to access GCP](#configure-a-storage-integration-to-access-gcp)
  + - [Add a GCP integration in Sigma](#add-a-gcp-integration-in-sigma)
    - [Create a custom IAM role in GCP](#create-a-custom-iam-role-in-gcp)
    - [Assign the custom IAM role in GCP](#assign-the-custom-iam-role-in-gcp)
  + [Update an audit log storage integration destination](#update-an-audit-log-storage-integration-destination)
  + [Delete an audit log storage integration](#delete-an-audit-log-storage-integration)