# Explain charts with AI

# Explain charts with AI

The **Explain this chart** feature uses AI to instantly generate a description of any chart. Details can include key insights, observations, data distribution summaries, and other context that can enhance your understanding of visualized data and help drive informed decisions.

This document introduces AI-generated explanations for charts and explains how to access and utilize the feature.

> 🚩
>
> The use of AI features is subject to the following [disclaimer](/docs/notice-for-enabling-ai-enabled-features-in-sigma).

## System and user requirements

The ability to explain a chart with AI requires the following:

* The [OpenAI integration](/docs/manage-external-ai-integrations#add-the-openai-integration) must be configured for your organization.
* If using Azure OpenAI, the [GPT-4.1 model](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?pivots=azure-openai&tabs=global-standard-aoai%2Cstandard-chat-completions%2Cglobal-standard#gpt-41-series) (`gpt-4.1-2025-04-14`) or later must be configured in the OpenAI integration.
* You must be assigned an account type with the **Explain charts with AI** permission enabled.

## About AI-generated explanations

When you use the **Explain this chart** feature, Sigma captures a snapshot of the chart and passes this image, along with the chart’s underlying data, to your OpenAI model. The model then processes the information and analyzes the context to generate an explanation of the data visualized by the chart. Sigma presents this explanation and allows you to provide feedback about the results, which can be used to improve future responses.

For information about how your data is secured and stored when using AI features, see [Frequently asked questions](/docs/manage-external-ai-integration#frequently-asked-questions) in [Manage external AI integrations](/docs/manage-external-ai-integration).

## Explain a chart

1. Open a workbook.
2. Hover over or select the chart that you want to explain.
3. In the element toolbar, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** to open the element menu, then select **Explain this chart**.

   ![Scatter plot titled scatter plot, with the element menu open and the Explain this chart... option visible at the end of the menu.](https://files.readme.io/0c1cd3925edb54aaf3ea6239d49ddd9650897a056094c836511392c598fcf294-explain-chart.png)
4. The **Explain** modal displays the explanation in real time, as it's generated. Use or interact with the results as needed:

   * Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/copy.svg) **Copy text**, then save or share the results (for example, paste it into a text element to supplement the chart).
   * Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/thumb-up.svg) **Helpful** or ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/thumb-down.svg) **Not helpful** and submit additional details to help improve future responses.![Explain modal with a detailed description of the data visualized in the chart, highlighting key insights like high total revenue in the chart as well.](https://files.readme.io/caa8a847c5569d8ce0fef482973947d326681f7ecdd1ed8c6f1555a1b53e4096-explain-chart-modal.png)

Updated 3 days ago

---

[View underlying data](/docs/view-underlying-data)[Highlight chart values](/docs/highlight-chart-values)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [About AI-generated explanations](#about-ai-generated-explanations)
  + [Explain a chart](#explain-a-chart)