# Manage external AI integrations

# Manage external AI integrations

The external AI integration allows users of the Sigma Service to access and use AI language models (including GPT-4 and embedding models) for features like [Ask Sigma](/docs/ask-natural-language-queries-with-ask-sigma), [chart explanations](/docs/explain-visualizations-with-ai) and the [formula assistant](/docs/use-ai-with-formulas).1 You can integrate with OpenAI directly, Azure OpenAI Foundry, or with Gemini through Google.

1Sigma Computing is continuously working to improve and expand on existing functionality. This document will be updated as new AI features become available.

> 🚩
>
> The use of AI features is subject to the following [disclaimer](/docs/notice-for-enabling-ai-enabled-features-in-sigma).

## User requirements

The ability to configure the OpenAI integration in Sigma requires the following:

* You must be assigned the **Admin** [account type](/docs/user-account-types).
* You must be able to provide the required [authentication credentials](/docs/manage-external-ai-integrations#prerequisites).

## Prerequisites

Before configuring the OpenAI integration, retrieve the authentication credentials from OpenAI, Azure, or Gemini depending on your chosen integration method (direct, through Azure OpenAI Foundry, or Google API Studio).

You can enable or disable the relevant permissions for specific account types. See [Configure permissions for AI features](/docs/configure-ai-features-for-your-organization#configure-permissions-for-ai-features).

### OpenAI credentials (direct)

To integrate with OpenAI directly, your company must obtain, manage, and secure an OpenAI API key. You can retrieve the API key in the API keys section of the OpenAI developer platform.

For more information, see [Where do I find my secret API key?](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key) in the OpenAI documentation.

For more information about your API key security, see [Best Practices for API Key Safety](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety) in the OpenAI documentation.

### Azure OpenAI credentials

To integrate with OpenAI through Azure OpenAI Service, your company must have an Azure subscription with access to Azure OpenAI. For each model, you must also provide the deployment ID, endpoint URL, and API key, which you can retrieve from your Azure OpenAI Foundry. To obtain these credentials:

1. Log in to your Azure AI Foundry portal.
2. Select your project.
3. Go to the **Models + endpoints** page to retrieve your credentials.

| Sigma credential | Azure location |
| --- | --- |
| **Deployment ID** *(model deployment name)* | Copy the value of the model name on your project's **Model deployments** page. *This must be gpt-4.1 or later (for a GPT-4 model) or text-embedding-3-small (for an Embeddings model).* |
| **Endpoint URL** | On your project's **Model deployments** page, click on **Get endpoint**, then copy the value in the **Endpoint** field. |
| **API Key** | On your project's **Model deployments** page, click on **Get endpoint**, then copy the value in the **Key** field. |

For more details of how to find these values in your Azure AI Foundry portal, see [Manage models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/how-to/create-model-deployments?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&pivots=ai-foundry-portal#manage-models) in the Azure AI Foundry documentation.

### Google Gemini credentials (Beta)

> 🚩
>
> ### The Gemini external AI integration is a public beta feature and is under construction. This information should not be considered part of our published documentation until this notice, and the corresponding Beta flag on the feature in the Sigma, are removed. As with any beta feature, the feature discussed below is subject to quick, iterative changes.
>
> Beta features are subject to the [Beta features](/docs/sigma-product-releases#beta-features) disclaimer.

You must obtain, manage, and secure an Gemini API key. You can retrieve the API key in the [API keys](https://aistudio.google.com/apikey) section of the Google AI Studio. Sigma will use `Gemini 2.0 Flash` by default. You can find current Google API rate limits [here](https://ai.google.dev/gemini-api/docs/rate-limits#current-rate-limits).

## Add the OpenAI integration

If you’ve retrieved the required credentials, you can authenticate the OpenAI integration to enable AI functionality in Sigma. Refer to one of the following sections based on your chosen integration method.

* [Open AI integration (direct)](#openai-integration-direct)
* [Azure OpenAI integration](#azure-openai-integration)

> 📘
>
> ### Sigma defaults to the `GPT-4.1` model for OpenAI integrations.

### OpenAI integration (direct)

1. Go to **Administration** > **AI Settings**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **AI Settings**.
2. In the **AI provider** modal, select the **External models** option.
3. Configure the integration:

   1. In the **AI Provider** field, select **OpenAI**.
   2. In the **API Key** field, enter the OpenAI API key.
   3. Click **Save** to authenticate.

   When the integration is successfully authenticated, the AI provider settings display **Remove** and **Edit** buttons, and AI functionality is enabled for your organization.

For more information about Sigma’s AI features, see the related resources at the end of this page.

### Azure OpenAI integration

When you integrate with Azure OpenAI, you specify two different model endpoints. The Sigma service supports the following models:

* GPT 4.1 or later for a language model.
* The text-embedding-3-small embedding model.

> 📘
>
> ### Both models are required to use AI features in Sigma.

To integrate Azure OpenAI models with the Sigma service, do the following:

1. Go to **Administration** > **AI Settings**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **AI Settings**.
2. Locate the **AI provider** modal and select the **External models** option.
3. Configure the integration:

   1. For **AI Provider**, select **Azure OpenAI**.
   2. For each model, provide the [required credentials](#azure-openai-credentials):

      * In the **Deployment ID** field, enter the model deployment name.
      * In the **Endpoint URL** field, enter the endpoint URL.
      * In the **API Key** field, enter the Azure API key.
      > 📘
      >
      > ### If your language model and your embeddings model are in the same project, your endpoint URL and key will be the same for both.
   3. Click **Save** to authenticate. After you save, Sigma does not display the values of your credentials.

> 🚧
>
> ### If you have restricted access to your Azure instance using IP allowlisting, Sigma displays a "Failed to validate" error. In this case, you need to add Sigma's IP addresses to your allowlist in Azure. See [Add Sigma IPs to the allowlist](/docs/connect-to-data-sources#add-sigma-ips-to-the-allowlist).
>
> For instructions on how to add the allowlist in the Azure portal, see [Grant access from an internet IP range](https://learn.microsoft.com/en-us/azure/ai-services/cognitive-services-virtual-networks?tabs=portal#grant-access-from-an-internet-ip-range) in the the Microsoft Azure documentation.

When the integration is successfully authenticated, the AI provider settings display **Remove** and **Edit** buttons, and AI functionality is enabled for your organization.

For more information about AI features in Sigma, see the related resources at the end of this page.

## Add a Gemini AI integration (Beta)

1. Go to **Administration** > **AI Settings**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **AI Settings**.
2. In the **AI provider** modal, select the **External models** option.
3. Configure the integration:

   1. In the **AI Provider** field, select **Gemini**.
   2. In the **API Key** field, enter the Gemini API key.
   3. Click **Save** to authenticate.

   When the integration is successfully authenticated, the AI provider settings display **Remove** and **Edit** buttons, and AI functionality is enabled for your organization.

For more information about Sigma’s AI features, see the related resources at the end of this page.

## Edit an external AI integration

You can edit the OpenAI integration at any time to update the credentials.

1. Go to **Administration** > **AI Settings**.

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **AI Settings**.
2. Locate the **AI provider** settings and click **Edit**.
3. In the **Edit external AI Integration** modal, edit the credentials as needed, then click **Save**.

## Remove an AI integration

You can remove an AI integration at any time to disable AI functionality within Sigma.

1. Go to **Administration** > **AI Settings**.

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **AI Settings**.
2. Locate the **AI Provider** settings and click **Remove**.
3. In the **Confirm removing external AI provider** modal, click **Remove** to confirm.

   After the integration is successfully removed, the **AI provider** setting displays the **Add** button, and AI functionality is disabled for your organization.

## Frequently asked questions

How does Sigma secure the external AI integration?

Sigma encrypts API key data exchanged through external AI API interactions.

It’s important to note that Sigma doesn’t retain data exchanged through the API (like data provided through user prompt completions) or control how OpenAI uses it. Your company owns this data and can implement proper measures to safeguard data privacy and security according to its unique requirements.

Is my workbook data used for generative AI features in the Sigma service?

If you initiate an action that uses an AI feature, such as asking AI to write a new formula, a limited amount of data from your workbook may be used as part of a prompt to generate a response. Prompts are provided to the third-party generative AI provider integrated with the Sigma service. The Sigma service does not contain any generative AI owned or controlled by Sigma Computing.

Does an external AI provider store my data or use it to train the AI language model?

OpenAI stores your API data for 30 days unless you explicitly opt out of sharing your data, or delete data manually. OpenAI doesn’t use it to train the language models for 30 days—unless you explicitly opt in to training. Your API data isn’t incorporated into the language model ecosystem, and it will never be exposed in AI interactions outside your Sigma organization.

*This statement was verified at the time Sigma began supporting the OpenAI integration. Sigma cannot control OpenAI’s policies, which may change in the future. For the most up-to-date information about how OpenAI stores and uses your data, see[Enterprise privacy at OpenAI](https://openai.com/policies/api-data-usage-policies) on the OpenAI website.*

*For the most up-to-date information about how Google stores and uses your data, see the Generative AI (GenAI) and Privacy section of the[Privacy Resource Center](https://cloud.google.com/privacy?hl=en) on the Google Cloud website.*

Can Sigma’s AI capabilities handle large-scale datasets from my warehouse?

Sigma does not use external AI integrations to send API requests to your data platform.

Updated 3 days ago

---

Related resources

* [Explain charts with AI](/docs/explain-visualizations-with-ai)
* [Use AI with formulas](/docs/use-ai-with-formulas)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Prerequisites](#prerequisites)
  + - [OpenAI credentials (direct)](#openai-credentials-direct)
    - [Azure OpenAI credentials](#azure-openai-credentials)
    - [Google Gemini credentials (Beta)](#google-gemini-credentials-beta)
  + [Add the OpenAI integration](#add-the-openai-integration)
  + - [OpenAI integration (direct)](#openai-integration-direct)
    - [Azure OpenAI integration](#azure-openai-integration)
  + [Add a Gemini AI integration (Beta)](#add-a-gemini-ai-integration-beta)
  + [Edit an external AI integration](#edit-an-external-ai-integration)
  + [Remove an AI integration](#remove-an-ai-integration)
  + [Frequently asked questions](#frequently-asked-questions)