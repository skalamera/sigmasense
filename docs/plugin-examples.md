# Plugin examples

# Plugin examples

Sigma’s development team has created a set of example plugins, listed below.

All of our example plugins are hosted and can be added to your organization. To view or add an example plugin to your organization, follow the steps to register a plugin using its *Production URL,* listed below.

You can also visit [Sigma’s Sample Plugin repository](https://github.com/sigmacomputing/sigma-sample-plugins) directly on Github.

## Use an example in your organization

The following examples can be viewed when added to your organization.

To add an example plugin to your organization, follow the steps to [register a plugin](/docs/register-a-plugin-with-your-sigma-organization) using its **Production URL** listed below. These URLs are intended for use when registering a plugin, and might not display anything in your browser until they are configured within a workbook.

* **Recharts Bar Chart**  
  A basic bar chart built with the [Recharts](https://recharts.org/en-US/) library.  
  [Source code](https://github.com/sigmacomputing/sigma-sample-plugins/tree/main/sample-plugin-bar-chart) |     **Production URL**: <https://sigma-sample-bar-chart-54049.netlify.app/>
* **D3 Candlestick**  
  A candlestick visualization built with D3.  
  [Source code](https://github.com/sigmacomputing/sigma-sample-plugins/tree/main/sample-plugin-candlestick-chart) |     **Production URL**: <https://sigma-sample-candlestick-chart-1664e5.netlify.app/>
* **D3 Graph**  
  Demonstrates usage of multiple data sources and in-memory joins.  
  [Source code](https://github.com/sigmacomputing/sigma-sample-plugins/tree/main/d3-graph) |    **Production URL**: <https://d3-graph-3a0d0f.netlify.app/>
* **D3 Sunburst**  
  A sunburst visualization built with D3.  
  [Source code](https://github.com/sigmacomputing/sigma-sample-plugins/tree/main/d3-sunburst) |    **Production URL**: <https://d3-sunburst-b97c7c.netlify.app/>
* **Frappe Heatmap**  
  A basic Frappe visualization example.  
  [Source code](https://github.com/sigmacomputing/sigma-sample-plugins/tree/main/frappe-heatmap) |    **Production URL**: <https://frappe-heatmap-9a4163.netlify.app/>

## Run an example locally

1. Open your terminal, and navigate to the directory you want to save the example in.
2. Clone [Sigma’s Sample Plugin repository](https://github.com/sigmacomputing/sigma-sample-plugins).

   `git clone https://github.com/sigmacomputing/sigma-sample-plugins.git`
3. Navigate to the plugin you want to try.

   `cd sigma-sample-plugins/<plugin-name>`
4. Run the plugin.

   `yarn && yarn start`

> 📘
>
> ### For additional instructions, visit the README file located in the main directory of any given example plugin.

Updated 3 days ago

---

Related resources

* [Get Started with Custom Plugins](/docs/get-started-with-custom-plugins)
* [Register a Plugin with your Sigma Organization](/docs/register-a-plugin-with-your-sigma-organization)

* [Table of Contents](#)
* + [Use an example in your organization](#use-an-example-in-your-organization)
  + [Run an example locally](#run-an-example-locally)