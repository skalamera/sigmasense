# Set a query ID cache duration

# Set a query ID cache duration

Some cloud data warehouses or data platforms have a query results cache that Sigma can use to retrieve query results without incurring additional compute costs. When available from the CDW, Sigma uses a query ID to access the cached data, which leads to better performance when compared to performing a new query to retrieve the data.

Each workbook has a query ID cache duration setting, or time-to-live (TTL). The default query ID cache duration is 10 minutes.

If the source data changes during the cache duration, the cached results reflect irrelevant or inaccurate data. If a query ID exceeds the cache duration setting, a new query is performed to retrieve the most accurate results. For more detailed information, see [Caching and data freshness](/docs/caching-and-data-freshness).

The actual query results are cached in the data platform, not in Sigma. Typically, the cache is in the form of a copy of results and is stored for 24 hours.

If you attempt to return the result of a query, you can use the **Cache duration** setting to specify that the results cache is a certain number of minutes old.

## Requirements

* This feature is only available for data platforms that support query result caches that Sigma can access using an ID, such as Snowflake and BigQuery.
* To set a the query ID cache duration for a workbook, you must be assigned the [Admin](/docs/user-account-types) account type.

## Set a query cache ID duration

To change the default cache duration for retrieving cached results from the data platform, do the following:

1. In a workbook, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) next to the refresh button (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/refresh.svg)) .
2. In the menu, select **Data refresh**.

   The **Data Refresh Settings** modal opens.
3. For **Cache duration**, set a duration in either minutes or hours.
4. Click **Save**.

Updated 3 days ago

---

Related resources

* [Manage workbook refresh options](/docs/workbook-refresh-options)
* [Caching and data freshness](/docs/caching-and-data-freshness)
* [Examine workbook and data model queries](/docs/examine-workbook-queries)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Set a query cache ID duration](#set-a-query-cache-id-duration)