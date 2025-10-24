# Configure a usage dashboard for Ask Sigma

# Configure a usage dashboard for Ask Sigma

Admins can configure a usage dashboard to view data about how Ask Sigma is used in their Sigma organization.

## Data security

Ask Sigma usage is not visible in usage dashboards or audit logs, and requires separate configuration to ensure data security.

Because this data includes names of users and the full text of the questions they ask, Sigma recommends configuring a unique schema to store this data in your warehouse and granting view privileges to that schema to only the admins who should be able to see this data.

## Requirements

* You must be assigned the Admin [account type](/docs/create-and-manage-account-types).
* You must have a Sigma connection to [Snowflake](/docs/connect-to-snowflake), [Databricks](/docs/connect-to-databricks), or [BigQuery](/docs/connect-to-bigquery) with write access enabled.
* You must have permissions in Snowflake, Databricks, or BigQuery to create the writable destination and configure appropriate access.

## Configure a destination in your warehouse to store Ask Sigma usage data

The following sections contain example instructions for how to create a location in your data platform to store usage data and set up the permissions so that all users can write data to that location, but only your admins can view the data.

This schema can't be the same as the write-back schema you configured during your connection set up. The connection write-back schema is hidden by Sigma, so you can’t build a new dashboard with a table from the schema. Sigma writes the data to the connection write-back schema, but you need another schema which is visible to Sigma to create the dashboard template in your data platform.

> 📘
>
> ### Sigma Computing, Inc. does not store this data or have the ability to access it.

Follow the instructions that match the data platform connection you are using to store and secure your Ask Sigma usage data.

* [Create a schema in Snowflake](#create-a-schema-in-snowflake)
* [Create a schema in Databricks](#create-a-schema-in-databricks)
* [Create a dataset in BigQuery](#create-a-dataset-in-bigquery)

### Create a schema in Snowflake

These are example instructions. Sigma recommends replacing these placeholder values with those more specific to your organization.

```
-- STEP 1: Setup for Ask Sigma dashboard 
-- Create database and schema for Ask Sigma history
CREATE DATABASE IF NOT EXISTS ASK;
CREATE SCHEMA IF NOT EXISTS ASK.HISTORY;

-- STEP 2: Grant privileges to access Ask Sigma logs
GRANT USAGE ON DATABASE ASK TO ROLE ASK_ADMIN_ROLE;
GRANT USAGE ON SCHEMA ASK.HISTORY TO ROLE ASK_ADMIN_ROLE;
GRANT CREATE TABLE, CREATE VIEW ON SCHEMA ASK.HISTORY TO ROLE ASK_ADMIN_ROLE;
```

### Create a schema in Databricks

These are example instructions. Sigma recommends replacing these placeholder values with those more specific to your organization.

```
-- Step 1: Setup for Sigma Dashboard Logging
-- Create schema for logs
CREATE SCHEMA IF NOT EXISTS ask.history;

-- STEP 2: Grant access to the group
GRANT USAGE ON SCHEMA ask.history TO 'ask_admin_group';
GRANT CREATE TABLE, CREATE VIEW ON SCHEMA ask.history TO 'ask_admin_group';
```

### Create a dataset in BigQuery

These are example instructions. Sigma recommends replacing these placeholder values with those more specific to your organization.

```
# Grant roles/bigquery.dataViewer to allow usage of the dataset

bq update --dataset --add_iam_member  
  "dataset_id=your-project-id:ask_ask_admin"  
  "member=role:ask_admin_role"  
  "role=roles/bigquery.dataViewer"

# Grant roles/bigquery.dataEditor to allow creating tables

bq update --dataset --add_iam_member  
  "dataset_id=your-project-id:ask_ask_admin"  
  "member=role:ask_admin_role"  
  "role=roles/bigquery.dataEditor"
```

## Configure your Ask Sigma usage view

After you have prepared your write destination in your data platform, configure your Ask Sigma usage view in the **Administration** portal.

1. Go to **Administration** > **AI Settings**:
   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **AI Settings**.
2. In the **Connection** field, select a connection that has write access to input tables.
3. Depending on the connection type, additional fields appear to prompt you to enter the details of the writable destination you configured in your data platform.
4. Click **Create.**

If you see the error "Cannot manage views on given scope with the following error: SQL access control error: Insufficient privileges to operate on schema 'your\_schema\_name' ", it means that the schema (Snowflake or Databricks) or dataset (BigQuery) you entered is not configured correctly to allow write access. See [Configure a destination in your warehouse to store Ask Sigma usage data](#configure-a-destination-in-your-warehouse-to-store-ask-sigma-usage-data) and ensure your writable destination in your data platform is configured correctly.

Updated 3 days ago

---

[Manage external AI integrations](/docs/manage-external-ai-integrations)[Notice for enabling AI-enabled features in Sigma](/docs/notice-for-enabling-ai-enabled-features-in-sigma)

* [Table of Contents](#)
* + [Data security](#data-security)
  + [Requirements](#requirements)
  + [Configure a destination in your warehouse to store Ask Sigma usage data](#configure-a-destination-in-your-warehouse-to-store-ask-sigma-usage-data)
  + - [Create a schema in Snowflake](#create-a-schema-in-snowflake)
    - [Create a schema in Databricks](#create-a-schema-in-databricks)
    - [Create a dataset in BigQuery](#create-a-dataset-in-bigquery)
  + [Configure your Ask Sigma usage view](#configure-your-ask-sigma-usage-view)