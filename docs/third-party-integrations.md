# Manage dbt Integration

# Manage dbt Integration

This article provides instructions on how to integrate dbt jobs with Sigma. When you integrate dbt jobs with Sigma, you can access the docs and metadata generated from dbt jobs directly in Sigma.

Some of the benefits of this integration with Sigma are:

* **Data freshness**: The dbt job execution data is displayed in Sigma, letting you to verify the freshness of the data.
* **Data quality**: You can view dbt quality tests on columns and models in Sigma, providing a greater degree of transparency into data quality issues.
* **Data cataloging**: The dbt table and column descriptions are displayed in Sigma, providing users with additional insights into the data they explore.

If you want to configure a dbt Semantic Layer integration, configure a dbt integration and then configure the Semantic Layer integration. For details, see [Configure a dbt Semantic Layer integration](/docs/configure-a-dbt-semantic-layer-integration).

## dbt Data

The following dbt metadata is available in Sigma:

* **Table description**: Provides dbt source information about the table view.
* **Column descriptions**: Provides dbt source information about the column views.
* **Last run time**: You can view the **Last run** date to verify when that model ran, which is when the data was last updated, and the duration of the job.
* **Tests**: Tests are assertions made about your models and other resources in your dbt project (e.g. sources, seeds and snapshots).
* **Additional model details**: See [Review metadata and details for dbt jobs](#review-metadata-and-details-for-dbt-jobs).

> 📘
>
> ### To see column descriptions and other details persisted to the information schema in Sigma data models and workbooks, you must enable the `persist_docs` configuration option in dbt. See [persist\_docs](https://docs.getdbt.com/reference/resource-configs/persist_docs) in the dbt documentation. If you do not enable this option, the information schema metadata is only visible when browsing the connection tables.
>
> After you enable this option in dbt, sync the table in Sigma to get the column descriptions to appear. See [Sync your data](/docs/troubleshoot-your-connection#sync-your-data).

## Requirements

* To configure and manage a dbt integration, you must be assigned the **Admin** [account type](/docs/create-and-manage-account-types).
* You must have a dbt service token. See the dbt documentation on [Service account tokens](https://docs.getdbt.com/docs/dbt-cloud-apis/service-tokens). The service token must have at least read access to the dbt account. For example, `Read-only` for Team plans or `Account Viewer` for Enterprise plans.
* You must know your API host. See the dbt documentation on [API access URLs](https://docs.getdbt.com/docs/cloud/about-cloud/access-regions-ip-addresses#api-access-urls).

## Configure dbt integration

To create and configure a connection to dbt, do the following:

1. In the Sigma header, click your user avatar to open the user menu, then select **Administration** to open the **Administration** portal.
2. On the **General settings** tab, locate the **Integrations** section. To the right of **dbt**, click **Add**.
3. In the **dbt Integration** modal, enter the **Service Token** and **API Host** for your account. For details on retrieving those values, see the [Requirements](#requirements) on this page.
4. Click **Save**.

## Review metadata and details for dbt jobs

After setting up the dbt integration, you can review metadata and other details for the dbt job, columns, and tables.

> 📘
>
> ### The dbt tab is not available in the **Connections** view for your data until a job is run in dbt for Sigma to fetch data.

![Data catalog for a Snowflake connection open with a table, STG_GA__EVENTS visible. The dbt tab is selected and shows Model details and other metadata described in surrounding text.](https://files.readme.io/b1b9a792323b1e7b48f829d6d04cf5dbbf8ebdaaba08915b738e801e768dd0c1-dbt-tab.png)

1. From Sigma Home, select **Connections** to open the list of connected data sources.
2. Select the table for which you want to view details.
3. In the **Model details** section, review the name, relation, and description of the dbt model used to create the table. Select **View SQL** to review the source SQL used to create the dbt model. Choose to view either the source code or the compiled code.
4. In the section below the **Model details**, review metadata about the specific dbt job:

   * Last run date and time
   * Execution time for the job
   * Health of the job. Hover over the health icon (such as a checkmark for a healthy job) for details.
   * Job ID of the dbt job.
   * Run ID of the specific run of the job.

## Remove dbt integration

After you have successfully integrated your dbt jobs with Sigma, you have the option to remove the integration:

1. In the Sigma header, click your user avatar to open the user menu, then select **Administration** to open the **Administration** portal.
2. On the **General settings** tab, locate the **Integrations** section. To the right of **dbt**, click **Remove**.

Updated 3 days ago

---

[Set up inactivity timeouts](/docs/set-up-inactivity-timeouts)[Configure a dbt Semantic Layer integration](/docs/configure-a-dbt-semantic-layer-integration)

* [Table of Contents](#)
* + [dbt Data](#dbt-data)
  + [Requirements](#requirements)
  + [Configure dbt integration](#configure-dbt-integration)
  + [Review metadata and details for dbt jobs](#review-metadata-and-details-for-dbt-jobs)
  + [Remove dbt integration](#remove-dbt-integration)