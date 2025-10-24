# Perform AI queries

# Perform AI queries

If your data warehouse includes one or more SQL functions that you can use to work with generative AI models, you can run those SQL functions from Sigma and perform an AI query.

When you run an AI query, you can call an AI model from your cloud data warehouse and run it on columns in your data, returning the output to Sigma.

## Requirements

* You must have a connection set up to a cloud data warehouse that supports AI functions:
  + Snowflake
  + Databricks
  + Google BigQuery\*
  + Amazon Redshift\*
* The account used to authenticate to the data warehouse must have permission to use the AI functions that you want to use.
* The Sigma user must have at least Can use access to the connection.

\*Might require additional model configuration steps. Refer to the documentation for your data warehouse.

## Run an AI query

You can run an AI query in one of two ways:

* Use the [CallVariant](/docs/callvariant) function in a calculated column to query the cloud data warehouse, then work with the output in a table column.
* Use a custom SQL element to directly query the cloud data warehouse using an AI query, then work with the output in a table.

If you want to streamline AI queries for users in your Sigma organization, consider creating a [custom function](/docs/custom-functions) with the syntax for a specific AI query. For more details, see [Boosting Productivity: Leveraging Cloud Data Warehouse AI Functions in Sigma for Enhanced Insights](https://www.sigmacomputing.com/blog/leveraging-cloud-data-warehouse-ai-functions-in-sigma-for-enhanced-insights) on the Sigma Blog.

Follow the steps for your cloud data warehouse:

* [Run an AI query in Snowflake](#run-an-ai-query-in-snowflake)
* [Run an AI query in Databricks](#run-an-ai-query-in-databricks)
* [Run an AI query in BigQuery](#run-an-ai-query-in-bigquery)
* [Run an AI query in Amazon Redshift](#run-an-ai-query-in-amazon-redshift)

For examples of using AI queries as part of a larger workflow, see the YouTube playlist [Build with AI](https://www.youtube.com/playlist?list=PLEPuTCV_4dNyLs9c_Qm4BruMMHOg6d_PT) on the Sigma YouTube channel.

### Run an AI query in Snowflake

Snowflake supports several Large Language Model (LLM) functions that you can use to perform an AI query from Sigma.

For example, if you have a table with call transcripts in a column *Call Transcript* and you want to evaluate the sentiment of the call, you can add a column to your table with the following formula:

```
CallNumber("SNOWFLAKE.CORTEX.SENTIMENT", [CALL_TRANSCRIPT])
```

The Snowflake Cortex function returns -1, 0, or 1 depending on the sentiment of the transcript.

As another example, using the same table with call transcripts in a column *Call Transcript*, you can add a column to your table with the following formula, which prompts the AI model to return the top three topics discussed:

```
CallVariant("SNOWFLAKE.CORTEX.COMPLETE", "llama2-70b-chat", "return a short, comma-separated list of the top three topics discussed in the call, ignoring any small talk" & [CALL TRANSCRIPT])
```

For more details about the available LLM functions, see [Large Language Model (LLM) Functions (Snowflake Cortex)](https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions) in the Snowflake documentation.

### Run an AI query in Databricks

Databricks supports several LLM functions that you can use to perform an AI query from Sigma, such as to classify data.

For example, if you have a table with website analytics data and want to classify the type of content based on the page title column *Page Title*, you can add a column to your table with the following formula, supplying the possible content types in the ARRAY section:

```
CallVariant("ai_classify", ([Page Title], CallVariant("ARRAY", ("marketing", "documentation", "API reference")))
```

Alternatively, you can provide the labels in another table column *Content Types*:

```
CallVariant("ai_classify([Page Title], ARRAY([Content Types])))
```

See [AI Functions on Databricks](https://docs.databricks.com/en/large-language-models/ai-functions.html) in the Databricks documentation.

### Run an AI query in BigQuery

BigQuery provides generative AI functions such as ML.GENERATE\_TEXT.

Using AI functions in BigQuery requires you to configure a remote model. See [The CREATE MODEL statement for remote models over LLMs](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model) in the Google Cloud BigQuery documentation. To make the functions available in Sigma, create a user-defined function for each AI function that you want to use. See [User-defined functions](https://cloud.google.com/bigquery/docs/user-defined-functions) in the Google Cloud BigQuery documentation.

After setting up a model and a UDF, you can call that UDF in Sigma. For example, if you set up a UDF called *my\_dataset.generate* to generate text in response to a prompt using the ML.GENERATE\_TEXT function in BigQuery, and you have a table with a *Call Organization* column, you can prompt the model to generate text based on the transcript:

```
CallText("my_dataset.generate", "Is this organization in the Fortune 500?", [Call Organization])
```

As another example, if you have a UDF called *my\_dataset.understand* using the ML.UNDERSTAND\_TEXT function in BigQuery, and you have a table with a *Call Transcript* column, you can prompt an AI model to answer a question about the contents of the transcript:

```
CallVariant("my_dataset.understand", "model_name", "Does this transcript mention Sigma's writeback capabilities?" & [CALL TRANSCRIPT])
```

For more details on the available generative AI functions, see [The ML.GENERATE\_TEXT function](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-generate-text).

Other AI functions are also available for processing data. See [The ML.UNDERSTAND\_TEXT function](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-understand-text) in the Google Cloud BigQuery documentation.

### Run an AI query in Amazon Redshift

Using AI functions in Amazon Redshift requires you to create and configure a model and SQL endpoint using Amazon Sagemaker and Redshift user-defined functions (UDFs). See [Use cases](https://docs.aws.amazon.com/redshift/latest/dg/r_create_model_use_cases.html) for the CREATE MODEL syntax in the Amazon Redshift documentation.

After setting up a model, you can call that model in Sigma. For example, if you set up a generative AI model called *LLM\_extract* to extract information from a provided text sample, and you have a table with a *Call Transcript* column, you can prompt the model to extract information from the column:

```
CallVariant("your_redshift_db.sagemaker.LLM_extract", "extract logistical details related to in-person meetings" & [Call Transcript])
```

For more details, see [Getting started with Amazon Redshift ML](https://docs.aws.amazon.com/redshift/latest/dg/getting-started-machine-learning.html) in the Amazon Redshift documentation.

Updated 3 days ago

---

[Use AI with formulas (Beta)](/docs/use-ai-with-formulas)[Metrics](/docs/metrics)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Run an AI query](#run-an-ai-query)
  + - [Run an AI query in Snowflake](#run-an-ai-query-in-snowflake)
    - [Run an AI query in Databricks](#run-an-ai-query-in-databricks)
    - [Run an AI query in BigQuery](#run-an-ai-query-in-bigquery)
    - [Run an AI query in Amazon Redshift](#run-an-ai-query-in-amazon-redshift)