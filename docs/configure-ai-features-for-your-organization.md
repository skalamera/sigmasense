# Configure AI features for your organization

# Configure AI features for your organization

Sigma offers several AI-powered features1 to accelerate user insights:

* **Ask Sigma** is a natural language query (NLQ) interface that allows you to ask questions about your data and interact with AI-generated responses. See [Ask natural language queries with Ask Sigma](/docs/ask-natural-language-queries-with-ask-sigma).
* The **formula assistant** uses AI to write new formulas, correct formula errors, and explain existing formulas. See [Use AI with formulas](/docs/use-ai-with-formulas).
* **Explain this chart** uses AI to instantly generate a description of any chart. See [Explain charts with AI](/docs/explain-visualizations-with-ai).

1Sigma Computing is continuously working to improve and expand on existing functionality. This document will be updated as new AI features become available.

> 🚩
>
> The use of AI features is subject to the following [disclaimer](/docs/notice-for-enabling-ai-enabled-features-in-sigma).

The AI connection is only used by Sigma as an AI provider, and is separate from where data is stored.

As an admin, you can configure an AI provider, configure permissions for AI feature usage, and select the data sources that are highlighted in Ask Sigma:

* [Configure an AI provider](#configure-an-ai-provider)
* [Configure permissions for AI features](#configure-permissions-for-ai-features)
* [Configure Ask discovery features](/docs/configure-ai-features-for-your-organization#configure-ask-discovery-features)
* [Select data sources to highlight in Ask Sigma](/docs/configure-ai-features-for-your-organization#select-data-sources-to-highlight-in-ask-sigma)

## User requirements

You must be assigned the **Admin** [account type](/docs/create-and-manage-account-types).

## Configure an AI provider

Sigma currently supports warehouse AI models and external models (OpenAI and Azure OpenAI Foundry) as AI providers.

* For information about configuring AI models hosted by your data platform, see [Configure warehouse AI model integration](/docs/configure-warehouse-ai-model-integration).
* For information about configuring OpenAI or Azure OpenAI Foundry, see [Manage external AI integrations](/docs/manage-external-ai-integrations).

## Configure Ask discovery features

You can access the following settings for Ask Sigma discovery:

* **Show Ask discovery** is enabled by default. Ask discovery produces data collections when you access the **Ask Sigma** page.
* **Show Ask discovery assets** is enabled by default. When you disable this option, discovery displays only text, with no links to sources or workbooks.

## Configure permissions for AI features

To control which Sigma users have access to AI features, enable or disable the relevant permissions for specific account types.

| AI feature | Account type permission that enables use |
| --- | --- |
| Ask Sigma | Use Ask Sigma and discovery |
| Formula assistant | Use AI with formulas |
| Explain this chart | Explain charts with AI |

For more details, including details on which license tiers have access to these permissions, see [License and account type overview](/docs/license-and-account-type-overview).

## Select data sources to highlight in Ask Sigma

Choose the data sources to highlight in Ask Sigma. Select popular data sources to improve the relevance of results for your users.

> 📘
>
> ### Non-highlighted data sources aren't excluded from Ask Sigma, just used for answers after highlighted sources. Ask Sigma respects access granted to users for data sources. Each user can see and query only the data sources that they have access to. If you want to restrict what Ask Sigma uses as a data source for answers for a specific user or team, Sigma recommends restricting that user or team at the data source, schema, or table level.

1. Go to **Administration > AI Settings**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the Administration portal.
   3. In the side panel, select **AI Settings**.
2. In the **Ask Sigma data sources** section, enter terms in the search bar to find the tables, data model elements, and datasets that you want to highlight for use in responses to user questions in Ask Sigma. The data sources in the table are listed in order of usage.

   If a data model element is not listed, make sure that you are granted or inherit access to the data model.

   > 🚧
   >
   > ### Tagged versions of data models aren't highlighted in Ask Sigma.
   >
   > When you select a data model to include in the data sources highlighted in Ask Sigma, only the Published version of that data model is highlighted, and only users who have access to the Published version can receive answers from Ask Sigma that reference that data model.
   >
   > For more about version tagging, see [Add version tags to workbooks and data models](/docs/add-version-tags-to-workbooks-and-data-models).
3. Select the checkboxes next to the sources that you want to highlight in Ask Sigma.
4. To see a list of all data sources that are either already available or that you have selected to highlight, clear any text from the search bar. The **Pending** column indicates the action to be taken when you proceed.

   ![Image showing the Ask Sigma data source selection panel with one source selected to be added and highlight, and another to be excluded from questions.](https://files.readme.io/b88ede7fa0db8134b91c154a1aeb6d81771bdcb87b26d4014ac0b622162f967a-ask_sigma_admin_highlighted_data_sources.png)
5. After selecting all relevant data sources, click **Sync**.

> 📘
>
> ### If you change any data sources or metadata in your data platform after your initial sync, return to this screen and manually re-sync your data sources to ensure Ask Sigma has access to those changes.

## How Ask Sigma selects data sources when answering user questions

Ask Sigma determines which data source to use to answer a user's question based on these factors, in this order:

* The user's permission to the data source. Ask Sigma will respect the permissions of the user asking the question and will not expose data they are not authorized to use.
* The relevancy of the data to the question. Ask Sigma uses any metadata that exists to describe data sources and data columns, and can infer relevancy from column names if no other metadata has been defined.
* The known validity of the data. If, for example, a data model has an "endorsed" badge, Ask Sigma is more likely to suggest it. Similarly, if someone in your organization has created and shared a metric definition, data model, or dataset, Ask Sigma will leverage those in relevant answers rather than using a raw table.
* The frequency of usage of the data source. Ask Sigma is more likely to reference frequently used data sources in its answers.

> 📘
>
> ### You do not need to add any metadata to your data sources in order for Ask Sigma to determine which ones to use. Ask Sigma will use any existing available metadata, such as certification badges, source descriptions, and column descriptions, to determine relevancy to a user's question, but can also determine relevancy using column names alone. If no metadata is defined, Ask Sigma automatically generates AI summaries for each data source that it uses. If you want to add badges and other metadata, see [Annotate tables with metadata](/docs/manage-data-catalog#annotate-tables-with-metadata).

Updated 3 days ago

---

Related resources

* [Ask natural language queries with Ask Sigma](/docs/ask-natural-language-queries-with-ask-sigma)
* [Use AI with formulas](/docs/use-ai-with-formulas)
* [Explain charts with AI](/docs/explain-visualizations-with-ai)
* [Manage external AI integrations](/docs/manage-external-ai-integrations)
* [Notice for enabling AI-enabled features in Sigma](/docs/notice-for-enabling-ai-enabled-features-in-sigma)
* [Configure warehouse AI model integration](/docs/configure-warehouse-ai-model-integration)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Configure an AI provider](#configure-an-ai-provider)
  + [Configure Ask discovery features](#configure-ask-discovery-features)
  + [Configure permissions for AI features](#configure-permissions-for-ai-features)
  + [Select data sources to highlight in Ask Sigma](#select-data-sources-to-highlight-in-ask-sigma)
  + [How Ask Sigma selects data sources when answering user questions](#how-ask-sigma-selects-data-sources-when-answering-user-questions)