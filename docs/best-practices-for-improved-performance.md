# Best practices for improved performance

# Best practices for improved performance

This document gathers some best practices related to performance for you to consider.

## Use datasets to reduce query loads

Sigma uses datasets to centralize data definitions and provide source data for workbooks. For more information about using datasets see [Data modeling In Sigma](/docs/data-modeling-with-datasets) and [Data modeling tutorial](/docs/data-modeling-tutorial).

Reduce the amount of unneeded data returned in a workbook query by using filters at the dataset level. Filters cut out irrelevant data without being restrictive. Surfacing only the most relevant data makes the process of discovering insights much quicker. When combined with materialization, it also means queries run faster.

### Dataset time range filters

Use relative date filters to ensure that Sigma queries return only a specific time range of data. For more information see [Add relative date filters](/docs/data-modeling-tutorial#filter-your-data) and [Dataset filters](/docs/dataset-filters).

### Dataset parameters

Create dataset parameters and use them in worksheets to ensure that the data filters to only the necessary data.  For more information see [Dataset parameters](/docs/dataset-parameters).

## Materialize datasets and workbook elements to reduce compute costs

Materializations allows you to write datasets and workbook elements back to your warehouse as tables which can reduce compute costs. Materialization enhances query performance by allowing your data warehouse to avoid recomputing the dataset when it's used by an element or a in descendant Sigma analysis. For more information see [Materialization](/docs/materialization).

## Use a query cache in the CDW

Some cloud data warehouses (CDW) have a query results cache that Sigma can use to retrieve query results without incurring additional compute costs. This leads to better performance. For more information see [Set a cache duration](/docs/set-a-query-id-cache-duration).

## More tips for improving workbook performance

Excessive joins, repeated logic, unused data, and filter overload can slow down your workbook. For performance tips, see [How to improve workbook performance](https://community.sigmacomputing.com/t/how-to-improve-workbook-performance/2456) in the Sigma Community.

Updated 3 days ago

---

Related resources

* [Data modeling with datasets](/docs/data-modeling-with-datasets)
* [Materialization with Sigma (QuickStart)](https://quickstarts.sigmacomputing.com/guide/administration_materialization/index.html?_gl=1*1h3b3ew*_ga*ODkzMjkyNDY1LjE3MDAwMDU1NzM.*_ga_PMMQG4DCHC*MTcwMTcxMjQ3OC4zNy4xLjE3MDE3MjE2NjQuOC4wLjA.)
* [Benefits of Materializing Datasets (Community)](https://community.sigmacomputing.com/t/benefits-of-materializing-datasets/383?_gl=1*1h3b3ew*_ga*ODkzMjkyNDY1LjE3MDAwMDU1NzM.*_ga_PMMQG4DCHC*MTcwMTcxMjQ3OC4zNy4xLjE3MDE3MjE2NjQuOC4wLjA.)
* [What can slow your Sigma workbook down! (Community)](https://community.sigmacomputing.com/t/warning-what-can-slow-your-sigma-workbook-down/2456?_gl=1*1h3b3ew*_ga*ODkzMjkyNDY1LjE3MDAwMDU1NzM.*_ga_PMMQG4DCHC*MTcwMTcxMjQ3OC4zNy4xLjE3MDE3MjE2NjQuOC4wLjA.)

* [Table of Contents](#)
* + [Use datasets to reduce query loads](#use-datasets-to-reduce-query-loads)
  + - [Dataset time range filters](#dataset-time-range-filters)
    - [Dataset parameters](#dataset-parameters)
  + [Materialize datasets and workbook elements to reduce compute costs](#materialize-datasets-and-workbook-elements-to-reduce-compute-costs)
  + [Use a query cache in the CDW](#use-a-query-cache-in-the-cdw)
  + [More tips for improving workbook performance](#more-tips-for-improving-workbook-performance)