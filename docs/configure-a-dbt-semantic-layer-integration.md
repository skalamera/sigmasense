# Configure a dbt Semantic Layer integration

# Configure a dbt Semantic Layer integration

Sigma supports [dbt Semantic Layer](https://www.getdbt.com/product/semantic-layer) integrations, allowing you to leverage your predefined dbt metrics in Sigma workbooks. This document explains how to configure a dbt Semantic Layer in Sigma. To query an existing integration, see [Query a dbt Semantic Layer integration](/docs/query-a-dbt-semantic-layer-integration).

## System and user requirements

* You must be assigned the Admin [account type](/docs/create-and-manage-account-types).
* You must have a dbt integration configured in Sigma. See [Manage dbt integration](/docs/manage-dbt-integration).
* You must use the same dbt service account token that you use for the dbt integration, and that token must be configured with the following permissions: Semantic Layer Only, Metadata Only, and Read-Only. See the dbt documentation on [Service account tokens](https://docs.getdbt.com/docs/dbt-cloud-apis/service-tokens).
* You need a dbt environment ID. See the dbt documentation on the [dbt environment command](https://docs.getdbt.com/reference/commands/dbt-environment).

## Configure a dbt Semantic Layer integration

1. Go to **Administration** > **Account**.
2. In the **Integrations** section, select **Edit** next to your dbt integration.
3. In the **dbt Integration section**, fill out the required fields:

   |  |  |
   | --- | --- |
   | **Service Token** | Your dbt service account token. |
   | **Access URL** | The URL of your existing Sigma dbt integration. This is likely `cloud.getdbt.com` (not `semantic-layer.cloud.getdbt.com`). |
   | **Environment ID** | Your dbt environment ID. |
4. Select **Save**.

Updated 3 days ago

---

[Manage dbt Integration](/docs/manage-dbt-integration)[Manage Slack integration](/docs/manage-slack-integration)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Configure a dbt Semantic Layer integration](#configure-a-dbt-semantic-layer-integration)