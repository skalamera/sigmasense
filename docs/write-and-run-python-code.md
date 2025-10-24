# Write and run Python code in Sigma (Beta)

# Write and run Python code in Sigma (Beta)

> 🚩
>
> This documentation describes one or more public beta features that are in development. Beta features are subject to quick, iterative changes; therefore the current user experience in the Sigma service can differ from the information provided in this page.
>
> This page should not be considered official published documentation until Sigma removes this notice and the beta flag on the corresponding feature(s) in the Sigma service. For the full beta feature disclaimer, see [Beta features](/docs/sigma-product-releases#beta-features).

You can write and run Python code in Sigma to perform data science, data engineering, and data analysis tasks. For example, define and run a churn prediction or price optimization model, clean and classify data sources, or enrich data from your data platform on the fly with information from an API.

> 📘
>
> This feature isn't supported by all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

If you want, you can perform complex data aggregation tasks in Sigma, then perform additional analysis in Python using DataFrames.

When you write Python code in Sigma, you can do any of the following:

* Reference data elements like tables, pivot tables, and input tables.
* Use the values from many control elements in your code.
* Build tables and charts with the output from your Python code.
* Call API endpoints and work with the response.
* Run Databricks notebooks and work with the output.
* Import libraries, including custom libraries, available in your Databricks instance.
* Use autocomplete to reference data sources available in your connection.

For examples, see [Examples](#examples) on this page.

To write and run Python code in Sigma, you must first set up Python for your Databricks connection. See [Set up a Databricks connection for Python](/docs/set-up-a-databricks-connection-for-python).

## User requirements

* You must be assigned an account type granted the **Write Python** permission. See [License and account type overview](/docs/license-and-account-type-overview).
* You must be granted **Can Use** access to the connection. To perform some actions in your Python code, you might need higher level access. See [Data access overview](/docs/data-permissions-overview).

## Limitations

If you use a JWT-signed secure embed, you can embed an element, page, or workbook that contains a Python element. Public embeds and secure embeds that are not signed by a JWT are not supported.

The following is unsupported:

* Exporting the output from Python code. Scheduled exports use the last run Python output instead of re-running the Python code at the time of the export.
* Materialization of Python elements, including child elements.
* Referencing columns from drill down control elements.
* Adding Python elements to data models.
* Modifying Python code in a custom view.

## Add a Python element to a workbook

All Python code in Sigma is run in a Python element that you add to a workbook.

1. Create a workbook or open an existing one and start editing.
2. In the **Add element** bar, select **Data**, then choose **Python** to add the element to your workbook canvas. You can also drag the element to your canvas.

   The element automatically defaults to the available connection associated with running Python code, or you can choose a connection.
3. Start to [write Python code](#write-python-code).

> 💡
>
> By default, all Python elements are named **Code**. You can rename a Python element by double-clicking the element name in the editor panel or the workbook page overview. Renaming the element can make reviewing the [query history for a workbook](/docs/examine-workbook-queries) and data lineage clearer.

## Write Python code

You must be editing your workbook to write Python code in Python elements.

Sigma provides several available Python methods for working with other Sigma elements:

* [Reference data elements with `sigma.get_element()`](/docs/python-method-reference#sigmagetelement).
* [Make code output available to other elements with `sigma_output()`](/docs/python-method-reference#sigmaoutput).
* [Reference control values with `sigma.get_control_value()`](/docs/python-method-reference#sigmaget_control_value).

When writing code for a Python element sourced by a Databricks connection, you can work with your data as [PySpark DataFrames](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.html), or convert data into other formats.

For detailed code examples, see [Examples](#examples).

> 📘
>
> ### For datasets of millions of rows, some data manipulation operations like `toPandas`, `collect`, `groupBy`, `orderBy`, `sort`, and `distinct` can cause an out of memory (OOM) error in the underlying Spark cluster.

### Work with packages in your Python code

Sigma includes various Python libraries and packages by default, and additional packages can be set up when you [set up your Databricks connection for Python](/docs/set-up-a-databricks-connection-for-python).

When you select a Python element, the editor panel lists the included libraries in the **Installed packages** section. To use any of those libraries in your Python code, import them first.

For example, to use the `pandas` library:

Python

```
import pandas as pd
```

Or to use the `requests` library to make API calls:

Python

```
import requests
```

To use the [Databricks Utilities (dbutils)](https://docs.databricks.com/aws/en/dev-tools/databricks-utils) package, you do not need to import it because it is initialized in every Python session:

Python

```
dbutils.notebook.run('/Workspace/Users/[email protected]/Example Notebook', 60)
```

## Run Python code

After writing your code in a Python element, click **Run** to run the code.

In Databricks, Python code runs using the service account credentials of your connection.

While the code runs, the **Run** button is unavailable and shows that the code is running. Dependent elements start to refresh.

After the code runs, any output from your script is shown, including any error messages. Dependent elements update.

To review details about the Python code run, use the query history. For example, retrieve a request ID for troubleshooting purposes, or identify long-running code. See [Examine queries in a workbook or data model](/docs/examine-workbook-queries).

### Run Python code from an action

You can run the code in a Python element using an [action](/docs/intro-to-actions). You can trigger an action from a UI element like a button, a change to a control element, or a selection in a data element.

For example, if your Python code uses the input from a control element, add an action to the control to run the dependent Python element when the control value is changed:

1. Select the trigger element for the action. In this example, a slider control element.
2. In the editor panel, select **Actions**.
3. In the **Actions** panel, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action** in an existing sequence, or click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add action sequence** to create a new one.
4. In the Action modal, configure the required fields to define the response:

   * For **Action**, select **Run Python element**.
   * For **Element**, select the Python element that you want to run. When you hover over different element names, the relevant element is highlighted on the workbook canvas.

After setting up the action, test it out. For example, change the value of the slider control and confirm that the associated Python element runs.

## Use Python output in child elements

When you use the `sigma.output()` method to make the contents of a variable in your code available to other elements in your workbook, you can then create child elements with the variable.

1. Update your code to use `sigma.output()`. See the method reference for [`sigma_output()`](/docs/python-method-reference#sigmaoutput).
2. Run your code. See [Run Python code](#run-python-code).
3. In the **Variables:** section, select the name of the variable, then choose the type of data element that you want to create: **Chart**, **Table**, or **Pivot table**.

   ![Selected variable showing available options described in text.](https://files.readme.io/c6b2cfe8e2247b949e9acbd8af9afe20aee3dc199375a391049c5218b7a40589-py-output-child.png)

   A data element of the selected type is created and appears below the Python element on the canvas.

Whenever the parent Python code is run, child elements update.

## Examples

You can write Python code to run models for data science tasks, enrich your data analysis with third-party data sources, and more in Sigma. Review the following examples for sample code and scenarios that you can adapt for your own use cases:

* [Run a Databricks notebook](#run-a-databricks-notebook)
* [Collect data from an API](#collect-data-from-an-api)
* [Display text output from Python code](#display-text-output-from-python-code)
* [Process and enrich data from an API](#process-and-enrich-data-from-an-api)

Basic examples are also available in the [Python method reference](/docs/python-method-reference).

> 📘
>
> ### To work with API endpoints in your Python code, your Databricks cluster must allow egress to the public Internet or the relevant API endpoints.

### Run a Databricks notebook

If you have a Databricks notebook, you can start a job to run the notebook from a Sigma Python element. Depending on what the notebook does, you can [work with the output in Sigma](#work-with-the-output).

> 📘
>
> ### You must have at least **CAN RUN** permissions on the notebook and access to the folder or workspace in which the notebook is stored.

To run a Databricks notebook from Sigma, use the `run` command of the [Notebook utility (dbutils.notebook) of Databricks Utilities (dbutils)](https://docs.databricks.com/aws/en/dev-tools/databricks-utils#notebook-utility-dbutilsnotebook). For specific syntax, see [Orchestrate notebooks and modularize code in notebooks](https://docs.databricks.com/aws/en/notebooks/notebook-workflows) in the Databricks documentation.

For example, to run a notebook called *Example Notebook* with a timeout limit of 60 seconds:

Python

```
dbutils.notebook.run('/Workspace/Users/[email protected]/Example Notebook', 60)
```

If your notebook uses [widgets](https://docs.databricks.com/aws/en/notebooks/widgets) to add parameters, you can pass values from Sigma control elements to the notebook when you run the notebook.

For example, to pass the value of a text input control with a control ID of `message` to a notebook parameter called `sigma_message`, make sure your Databricks notebook includes the following syntax:

Python

```
# Create widget that can listen for the inputs from the Sigma workbook
dbutils.widgets. text("sigma_message" , "test")

# Create widget reference
sigma_message = dbutils.widgets.get ("sigma_message")
```

Then use the following syntax in a Sigma Python element:

Python

```
dbutils.notebook.run(
    "/Workspace/Users/[email protected]/Example Notebook",
    60,
    {"sigma_message": sigma.get_control_value("message")},
)
```

#### Work with the output

After you run the notebook, how you work with the results depends on what your notebook does:

* If your notebook updates a table in Databricks in a catalog and schema that is available in Sigma, you can add a data element to your workbook and use the updated table as the data source.
* If your notebook returns data as the output in the `dbutils.notebook.exit(<output>)` command, you can work with it in your Python element. For details using the `exit` command of the [Notebook utility (dbutils.notebook)](https://docs.databricks.com/aws/en/dev-tools/databricks-utils#notebook-utility-dbutilsnotebook) of Databricks Utilities (dbutils), see the Databricks documentation.

For example, if you have a Databricks notebook to run a performance model based on a `cluster_size` widget and output the results with the `exit` command of `dbutils.notebook`, you can call the notebook from Sigma with the parameter value specified by a control element.

Given a workbook with a number input control with a control ID of `total-nodes` and a notebook called *Performance Modeling*, write and run the following Python code to run the notebook and display the results:

Python

```
model_output = dbutils.notebook.run(
    "/Workspace/[email protected]/Performance Modeling",
    120,
    {"cluster_size": sigma.get_control_element("total_nodes")},
)

display(model_output)
```

If your notebook outputs a data structure that you can work with in Sigma functions, such as JSON or a PySpark DataFrame, as part of the `exit` command of `dbutils.notebook`, you can work with the output in a child element. To do so, use the [`sigma_output`](#make-output-from-your-code-available-to-other-elements) method:

Python

```
model_output = dbutils.notebook.run(
    "/Workspace/[email protected]/Performance Modeling",
    120,
    {"cluster_size": sigma.get_control_element("total_nodes")},
)

display(model_output)

sigma.output("performance_results", model_output)
```

### Collect data from an API

You can write Python code to call an API from Sigma, letting you enrich data from your data platform with information available through APIs on the web.

With this example code, you can retrieve metadata about specific Pokémon from the open source [PokéAPI](https://pokeapi.co/), store the response in a pandas DataFrame, then make the DataFrame available to downstream elements in your Sigma workbook.

You can optionally make the code interactive, where users can choose one or more Pokémon from a multi-select list control to provide the list of Pokémon to retrieve details about.

Refer to the following example code:

Python

```
import requests
import pandas as pd

def get_pokemon_data(pokemon_list):
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    pokemon_data = []

    for pokemon in pokemon_list:
        response = requests.get(f"{base_url}{pokemon}")
        if response.status_code == 200:
            data = response.json()
            pokemon_info = {
                "name": data["name"],
                "id": data["id"],
                "height": data["height"],
                "weight": data["weight"],
                "types": ", ".join([t["type"]["name"] for t in data["types"]])
            }
            pokemon_data.append(pokemon_info)
        else:
            print(f"Failed to retrieve data for {pokemon}")

    return pd.DataFrame(pokemon_data)

# Example usage
# You can also input the pokemon_list with a control
# pokemon_list= sigma.get_control_value(‘pokemon’)
pokemon_list = ["pikachu", "charizard", "bulbasaur", "squirtle"] 
df = get_pokemon_data(pokemon_list)

sigma.output("Pokemon",df)
```

### Display text output from Python code

If your Python code outputs a variable whose value is a string, you can display the string output in a dynamic text formula in a text element, button label, element title, and more.

For example, write code to forecast a cost trend, and use a conditional statement to output a string with information about the trend.

Reference this pseudocode:

Python

```
# get the cost data

df = sigma.get_element("plugs")

# forecast a trend

forecast = # your forecasting code goes here and outputs an integer for the trend

    # the forecast can include other data in the forecast variable which you
    # can chart on a scatter plot
    trend = # integer output of the forecast

# evaluate the trend forecast

trend_eval = "More expensive" if trend > 1000 else "Same or less expensive"

# make the trend and trend_eval available to other Sigma elements

sigma.output("cost_forecast", forecast)
sigma.output("evaluation", trend_eval)
```

With code like this, you can do the following to display a scatter plot with dynamic text that references the evaluation:

1. For each variable, create a child element. Create a **Chart** from the `cost_forecast` output, and a **Table** from the `evaluation` output.
2. Rename the table element "Trend evaluation".
3. Change the chart element to a scatter plot, then rename it to the following: `This forecast is =[Trend evaluation/evaluation]`, where the formula after the = is a dynamic text formula that references the *evaluation* column of the "Trend evaluation" table element that contains the string output of the code.

### Process and enrich data from an API

In this example, you can process data from your data platform and enrich it with an API call. For a given table of sales data, retrieve the current relevant exchange rate and calculate the effect of the exchange rate on your total revenue.

> 🚩
>
> Running this example requires an API key from fixer.io. Ensure that your planned usage meets the restrictions for the free tier.

To perform this example, do the following:

1. Open an existing workbook or create one.
2. Add a text input control to your workbook to use to provide the API key to your code and update the control ID to `Fixer-API-Key`.

   > 🚩
   >
   > This is not a secure method of storing or providing API keys.
3. Add a table with the plugs electronics sample data from the Sigma Sample Database: `sigma_sample_data.examples__plugs_electronics.plugs_electronics_hands_on_lab_data`.
4. In the `plugs` table, create three new columns with the following formulas and names:

   * A *Sales* column with a formula of `[Price] * [Quantity]`
   * A *COGs* column with a formula of `[Cost] * [Quantity]`
   * A *Profit* column with a formula of `[Sales] - [COGs]`
5. In the `plugs` table, format the *Profit* column to use Euros as the currency.
6. Add a Python element to your workbook, and use the sample code provided below.
7. Run the Python code, then create a child table with the `current_exchange_rates` variable. Two columns exist in the output: *rate* and *currency*.
8. In the `plugs` table, add a new column called *Adjusted Profit* to calculate the exchange rate for your *Profit*, with the following formula:

   `[Profit] * MaxIf([Code: current_exchange_rates/rate], [Code: current_exchange_rates/currency] = "USD")`

#### Example code

Python

```
import requests
import pandas as pd
from datetime import datetime

def fetch_exchange_rates(url):

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        if data.get('success'):

            rates = data.get('rates', {})
            
            df = pd.DataFrame([
                {'currency': currency, 'rate': rate} 
                for currency, rate in rates.items()
            ])
            
            df['base'] = data.get('base')
            df['date'] = data.get('date')
            df['timestamp'] = data.get('timestamp')

            if 'timestamp' in df.columns:
                df['datetime'] = pd.to_datetime(df['timestamp'], unit='s')
            
            return df
        else:
            print(f"API Error: {data.get('error', {}).get('info', 'Unknown error')}")
            return None
    else:
        print(f"HTTP Error: {response.status_code}")
        return None

# Example usage
if __name__ == "__main__":
    api_key = sigma.get_control_value('Fixer-API-Key')
    url = "http://data.fixer.io/api/latest?access_key=" + api_key
    exchange_rates_df = fetch_exchange_rates(url)
    
    if exchange_rates_df is not None:
        print(exchange_rates_df)

sigma.output('current_exchange_rates', exchange_rates_df)
```

## Manage the Python compute cluster

Python code runs on an all purpose compute cluster in Databricks, configured when you set up your connection to Databricks.

While customizing or editing a workbook, if you select a Python element, you can review the status of the cluster:

* Whether the cluster is ready, pending (restarting), or terminated.
* After how many minutes of inactivity the cluster will terminate.

If the cluster is terminated, you can start it in one of the following ways:

* Select the Python element, then in the editor panel, select **Start cluster**.
* Run the code in the Python element by clicking **Run** or triggering an action that runs the code in the Python element.

> 📘
>
> ### Restarting the cluster can take up to 5 minutes, during which time the cluster status updates to **Pending**.

If you encounter any issues managing the status of your all purpose compute cluster in Sigma, work with your Databricks admin to update the cluster in the Databricks console.

Updated 3 days ago

---

[Transpose a table](/docs/transpose-a-table)[Python method reference (Beta)](/docs/python-method-reference)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Limitations](#limitations)
  + [Add a Python element to a workbook](#add-a-python-element-to-a-workbook)
  + [Write Python code](#write-python-code)
  + - [Work with packages in your Python code](#work-with-packages-in-your-python-code)
  + [Run Python code](#run-python-code)
  + - [Run Python code from an action](#run-python-code-from-an-action)
  + [Use Python output in child elements](#use-python-output-in-child-elements)
  + [Examples](#examples)
  + - [Run a Databricks notebook](#run-a-databricks-notebook)
    - [Collect data from an API](#collect-data-from-an-api)
    - [Display text output from Python code](#display-text-output-from-python-code)
    - [Process and enrich data from an API](#process-and-enrich-data-from-an-api)
  + [Manage the Python compute cluster](#manage-the-python-compute-cluster)