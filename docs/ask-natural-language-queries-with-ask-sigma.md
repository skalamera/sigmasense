# Ask natural language queries with Ask Sigma

# Ask natural language queries with Ask Sigma

Ask Sigma is a natural language query (NLQ) interface that allows you to ask questions about your data and interact with AI-generated responses. You can extract factual information from your data, or ask questions that generate charts that you can then further explore in a workbook.

> 🚩
>
> The use of AI features is subject to the following [disclaimer](/docs/notice-for-enabling-ai-enabled-features-in-sigma).

## System and user requirements

The ability to use Ask Sigma requires the following:

* An AI provider must be configured for your organization. See [Configure an AI provider](/docs/configure-ai-features-for-your-organization#configure-an-ai-provider).
* You must be assigned an account type with the **Use Ask Sigma** permission enabled. See [Account type and license overview](/docs/account-type-and-license-overview) for details.
* To move analysis from Ask Sigma into a workbook, you must be assigned an account type with the **Create, edit, and publish workbooks** permission enabled. See [Account type and license overview](/docs/account-type-and-license-overview) for details.

## Limitations

* Ask Sigma can't perform joins. Ask Sigma selects a single data source with which to answer a data question and cannot combine data from multiple tables, data models, or metrics.
* Ask Sigma can only answer data questions based on data sources in your data platform that your admin has made available to the AI model. See [Select data sources to highlight in Ask Sigma](/docs/configure-ai-features-for-your-organization#select-data-sources-to-highlight-in-ask-sigma).
* Ask Sigma won't generate Observations about your data if the data set is too large. If you receive this error, consider narrowing your question parameters.
* Tagged versions of data models aren't highlighted in Ask Sigma. When you select a data model to include in the data sources highlighted in Ask Sigma, only the Published version of that data model is highlighted, and only users who have access to the Published version can receive answers from Ask Sigma that reference that data model.
* If you want to embed Ask Sigma in your own portal or site, you must sign your secure embed URLs with JWTs. See [Embed Ask Sigma](/docs/embed-ask-sigma).

## Search data sources

Ask Sigma only has access to the data sources that your admins have selected to make available to Ask Sigma. You can search the data sources that you have access to and see which ones are available in the data catalog. These are labeled as highlighted data sources.

To search available data sources:

1. From Sigma Home, click **Ask Sigma** in the left navigation. If you don't see this option, refer to [System and user requirements](#system-and-user-requirements) above.
2. Click **All data sources**, then enter all or part of the name of a table, data model element, or dataset to check if it is highlighted in Ask Sigma.

   Sigma returns all matching tables, data model elements, and datasets that you have permission to use, each with an indicator of whether it is highlighted or not highlighted for Ask Sigma.

   > 📘
   >
   > ### Your admin configures which sources are highlighted to be queried by Ask Sigma.
   >
   > All data permissions that apply elsewhere in Sigma also apply in Ask Sigma. For example, if your admin has configured row-level security or column-level security on a data source, Ask Sigma respects those restrictions. In the case of a data model, you must have access to the published version for its elements to appear as highlighted sources.

   ![Image of the \"All data sources\" menu open and a search term \"census\" entered. The menu shows all matching data sources and shows that only one is highlighted to Ask Sigma. All others are grayed out and marked \"Not Highlighted\".](https://files.readme.io/04ef9e20359ae68209f680bfcf0d129fa92a47d7dbb7bea2c7224d16a3b28fa9-ask_sigma_highlighted_datasource.png)

If a source that you want to be highlighted in Ask Sigma is currently not highlighted, notify your Sigma admin. Sigma admins choose which data sources to highlight in Ask Sigma. See [Select data sources to make available to ask Sigma (Beta)](/docs/configure-ai-features-for-your-organization#select-data-sources-to-make-available-to-ask-sigma-beta).

## Ask natural language queries with Ask Sigma

To use Ask Sigma to ask questions about your data:

1. From Sigma Home, click **Ask Sigma** in the left navigation.
2. Type your question in the box in the upper left of your screen.
3. Ask Sigma interprets your question and searches the data sources you have access to and selects what it determines to be the best source to answer your question. Ask Sigma uses semantic relevance, data validity metadata, and data source usage to select the best data source from among the data sources you have permission to view.
4. Ask Sigma provides an answer and displays the step-by-step decision logic it used to determine the answer.

   ![A screenshot of an Ask Sigma response to the question \"What are our ten most profitable stores in the East region?\" with several steps showing what Ask Sigma did to determine the answer, and then a summary of the answer in the form of a bar chart in the center of the screen.](https://files.readme.io/bb9a8365374dd9439e3a18d44020c4a1bccfd010cb45cc3a65f64440d3d0e2aa-answer-view.png)
5. [optional] Scroll through the steps or select a specific step in the side panel to examine the decision logic, and modify the choices that Ask Sigma made, if necessary.

   ![A gif showing what happens when you scroll up to review each step in the Ask Sigma response.](https://files.readme.io/15cc5b9bbf09d013dea95e85eee6d2fa751c2619a3dfc90330f5780d021cab61-scroll-back-through-steps.gif)
6. [optional] In any step, click **Open in workbook** to start an [exploration](/docs/ad-hoc-data-explorations) from that point in the analysis.

## Share questions in a custom URL

Once you enter a question into Ask Sigma, Sigma automatically adds that question into a custom URL that you can then share with other users in your organization. When other users access the URL, Ask Sigma automatically populates the query and produces a response. Also, if you or other users modify the original query, Ask Sigma automatically updates the custom URL to share.

You can use this feature to:

* Preconfigure an Ask Sigma experience to get new users started with the correct question.
* Save questions you want to reuse to consistently access new data insights for recurring analysis.
* Generate URLs to access Ask Sigma and embed them anywhere in your organization, like:
  + Workbooks
  + Embed environments
  + Internal documentation

> 📘
>
> ### Results from these shared questions are determined by the data sources a user has access to.

## Continue exploring with related charts

From your initial answer, you can continue exploring the provided analysis. Ask Sigma offers related charts underneath its primary answer to offer avenues to analyze related data.

You can:

* Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/table.svg) **View underlying data** for the answer chart or for any related chart.
* Click on a related chart to see a detailed view and get more related charts.
* Check the box for any step, answer, or related chart and click **Open in workbook** to further analyze your data in an [exploration](/docs/ad-hoc-data-explorations).

![](https://files.readme.io/5fe428f47a8e2725047e543272cd175e2684c893e7ce7fd6c26efe29ccd64aa7-keep-exploring.gif)
  

## Ask a question on a data source table

When you view a data source table, you can ask a question of that data source from the Ask Sigma option on the **Overview** tab. You can ask a question of any data source visible to you, not just sources highlighted for Ask Sigma.

1. From **Sigma Home**, select **Connections** to open the list of connected data sources.
2. Select the data connection with the data catalog that you want to view.
3. In the left navigation panel, search or browse the data catalog to locate the table.
4. Select the table name to open the table.
5. Enter a question in the Ask Sigma question bar.

   ![Asking a question about a data source table in the data catalog using the Ask Sigma question bar.](https://files.readme.io/109223e65a00bf63fa7e6d621ce4ae6ece56bc023a3d7fe8c688ef7531c5be84-ask_sigma_dataset_table.png)
6. Sigma opens Ask Sigma in a new browser tab, populated with the question that you asked.

   ![Ask Sigma opening a new tab with the question that was asked, and the response output.](https://files.readme.io/f2bdac9cdfc9a6a4a6644aa52eadd10ec25f5829ff26a6ad3e2cee34b9608a30-ask_sigma_data_set_question_new.png)

## Troubleshoot Ask Sigma

If you need to consult with technical support about a failing Ask Sigma query, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/download.svg) **Download debug** in the bottom left corner of Ask Sigma so that you can provide it to our support team. The debug file contains the text of your questions and metadata about your data sources to help troubleshoot the steps that Ask Sigma took to resolve the query.

Updated 1 day ago

---

Related resources

* [Configure AI features for your organization](/docs/configure-ai-features-for-your-organization)
* [Embed Ask Sigma](/docs/embed-ask-sigma)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Limitations](#limitations)
  + [Search data sources](#search-data-sources)
  + [Ask natural language queries with Ask Sigma](#ask-natural-language-queries-with-ask-sigma)
  + [Share questions in a custom URL](#share-questions-in-a-custom-url)
  + [Continue exploring with related charts](#continue-exploring-with-related-charts)
  + [Ask a question on a data source table](#ask-a-question-on-a-data-source-table)
  + [Troubleshoot Ask Sigma](#troubleshoot-ask-sigma)