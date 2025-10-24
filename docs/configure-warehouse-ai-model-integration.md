# Configure warehouse AI model integration

# Configure warehouse AI model integration

You can elect to use AI models in your cloud data warehouse to power Sigma AI features.

## Limitations

* You can only use Snowflake, Databricks, and BigQuery connections for warehouse AI models at this time.
* Configuring a warehouse model as your AI provider is not currently supported for the [Explain charts with AI](/docs/explain-visualizations-with-ai) feature. Both [Ask Sigma](/docs/ask-natural-language-queries-with-ask-sigma) and [formula assistant](/docs/use-ai-with-formulas) are supported with warehouse models.

## System and user requirements

> 🚩
>
> ### The BigQuery warehouse AI integration through Google Vertex AI is a public beta feature and is under construction. This information should not be considered part of our published documentation until this notice, and the corresponding Beta flag on the feature in the Sigma, are removed. As with any beta feature, the feature discussed below is subject to quick, iterative changes.
>
> Beta features are subject to the [Beta features](/docs/sigma-product-releases#beta-features) disclaimer.

* You must be assigned the Admin [account type](/docs/create-and-manage-account-types).
* If using Snowflake as your AI provider:

  + You must have a Snowflake connection authenticated with either Key Pair auth or OAuth. Basic Auth connections are not supported.
  + Verify the user defined on the connection has the `snowflake.cortex_user` database role in their default role. By default, this role is inherited from PUBLIC. In case it has been revoked from PUBLIC, follow [Setting up authorization](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-llm-rest-api#setting-up-authorization) in the Snowflake documentation to grant the role.

    - If you are using a connection with Key Pair authentication, the Key Pair service account user on the connection must have `snowflake.cortex_user` in their default role.
    - If you are using a connection with OAuth authentication, all users with access to the connection must have `snowflake.cortex_user` in their default role. If you are using a service account, the service account user must have `snowflake.cortex_user` in their default role.
    - The default role must have [Snowflake REST API access authentication](https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/authentication) configured. You can use either key pair or OAuth authentication, but not basic authentication.
  + Your Snowflake account must be hosted in a region that supports the `snowflake-arctic-embed-l-v2.0` embed model. See the [embed model availability table](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-rest-api#id2) to confirm.
  > 📘
  >
  > ### You must enable Snowflake's cross-region inference parameter to access your Cortex integration through Sigma. The cross-region inference parameter doesn't apply to embedding models.

  + If you are using AWS, your Snowflake account must be hosted in a region that supports `llama4 Maverick` and `claude3.5` LLM models.
  + If you are using Azure, your Snowflake account must be hosted in a region that supports the `openai-gpt-4.1` LLM model.
  > 📘
  >
  > ### Sigma uses to the `llama4 Maverick` model for non-complex tasks, such as selecting a data source. For more complex tasks, such as building a workbook, Sigma uses `claude3.5`.

See the [LLM model availability table](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-rest-api#model-availability) to confirm your account region is supported, otherwise [cross-region inference](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cross-region-inference) must be enabled.

* If using Databricks as your AI provider:
  + Your Databricks account must be hosted in a region that supports the `databricks-bge-large-en` embedding model, and these LLM models, see [Foundational models hosted on Databricks](https://docs.databricks.com/aws/en/machine-learning/model-serving/foundation-model-overview#aws-models) for more information:
    - `databricks-meta-llama-3-3-70b-instruct`
    - `databricks-claude-3-7-sonnet`
  + You must have an active Databricks workspace within a [supported model serving region](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#region) with AI Model Serving enabled (currently in public preview).
  + You must have a running Databricks Serverless or Pro SQL warehouse (not available with Classic SQL warehouses) with access to the `ai_query` function. For detailed requirements related to the ai\_query function for foundational models, refer to [Example: Query a foundation model](https://docs.databricks.com/aws/en/sql/language-manual/functions/ai_query#foundation-model) in the Databricks documentation.
  + The Databricks connection must have read access to the data sources you intend to query. This includes: `USE`, `BROWSE`, `EXECUTE`, and `SELECT` privileges on the catalog or schema containing the data sources.
* If using BigQuery as your AI provider, [Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/start/api-keys) enables you to access Google provided models, like Gemini, to use your connection for database and AI. Currently, Sigma only supports `Gemini 2.0 Flash`. To set up a connection to use Gemini:
  + You must have a Google cloud platform with billing enabled.
  + You must have a service account with these permissions and key:
    - `Vertex AI User` to use vertex
    - `BigQuery Data Viewer` to set up with Sigma
    - `BigQuery Job User` to set up with Sigma
    - (Optional) `BigQuery Data Editor` to enable write-back abilities if you want to use this specific connection for recording Ask Sigma usage.
  + If you are moving from an OpenAI model to Gemini, you lose the AI explain visual functionalities that are not yet supported for warehouse models.
  + The [endpoint](https://cloud.google.com/vertex-ai/docs/reference/rest#service-endpoint) specifies where the model you’re querying is located and isn’t related to the location of any elements within the project. The endpoint defaults to `us-central1`. It's recommended to set your endpoint close to your Sigma instance region to improve latency.
  + Performance depends on the current traffic and is liable to higher latency when busy. More information can be found [here](https://cloud.google.com/vertex-ai/generative-ai/docs/dynamic-shared-quota).

## Configure data warehouse hosted model as your AI provider

1. Go to **Administration** > **AI Settings**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **AI Settings**.
2. If this is the first time you are configuring an AI provider integration, skip this step.

   If **External models** is selected in the **AI provider integration** section and the available buttons read **Remove** and **Update**, you have an OpenAI or Azure OpenAI key already provisioned. If you want to use a warehouse model instead, click **Remove** to clear your credentials.

   > 📘
   >
   > ### Removing your OpenAI or Azure OpenAI credentials clears out all previously indexed data sources. You will need to re-index all data sources after configuring a new AI provider integration.
3. Select **Data warehouse hosted model (recommended)**.
4. In the **Connection** dropdown menu, select the connection to use to access models in your data warehouse.
5. (Optional) In the **Region** dropdown menu, select a region for your connection (BigQuery only).
6. Click **Save**. If the connection is successful at reaching the AI models in your data warehouse, the Ask Sigma data sources section appears.
7. Next, [select the data sources that should be available to Ask Sigma](/docs/configure-ai-features-for-your-organization#select-data-sources-to-make-available-to-ask-sigma-beta).

Updated 3 days ago

---

[Configure AI features for your organization](/docs/configure-ai-features-for-your-organization)[Manage external AI integrations](/docs/manage-external-ai-integrations)

* [Table of Contents](#)
* + [Limitations](#limitations)
  + [System and user requirements](#system-and-user-requirements)
  + [Configure data warehouse hosted model as your AI provider](#configure-data-warehouse-hosted-model-as-your-ai-provider)