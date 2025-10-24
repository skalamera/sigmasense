# Caching and data freshness

# Caching and data freshness

When you open a workbook or data model, Sigma generates and runs optimized SQL queries to retrieve data from your connected data platform. Sigma does not store your data, and uses browser caching and warehouse-level caching to ensure fresh data while also reducing warehouse overhead.

## How Sigma reduces warehouse overhead

When data elements are updated, Sigma tries to reduce the overhead on your warehouse. The steps Sigma follows are:

1. [Check browser cache](#check-browser-cache)
2. [Try alpha query](#try-alpha-query)
3. [Try CDW result ID cache](#try-query-id-cache) (only available for some CDWs)
4. Re-query the warehouse

> 🚩
>
> ### Manual refresh or scheduled refresh bypasses all caching options. See [Manage workbook refresh options](/docs/workbook-refresh-options).

For more details about what queries are running and where, review the query history for a workbook, data model, or dataset. See [Examine workbook and data model queries](/docs/examine-workbook-queries) and [Examine dataset queries](/docs/examine-dataset-queries).

### Check browser cache

The browser cache accounts for the data immediately accessible in the browser. The browser cache is not available when you first open a workbook or data model because the cache is empty, but as you make changes, Sigma automatically uses the browser cache to display results when possible.

If you make changes to a data element, Sigma first checks if existing data already in the browser can still work for the updated element.

This might happen when:

* A column is renamed or moved

### Try alpha query

If the data in the browser can't be used directly, Sigma checks if it can recalculate new values using the existing data in the browser.

This may happen when:

* A new aggregate column is added.

### Try query ID cache

The query cache is only used if your data warehouse supports result caching, such as with Snowflake and BigQuery.

This might happen when:

* Regrouping data

Sigma does not store query results, only the query ID returned by the warehouse, and uses that ID to retrieve results from the cache in the data warehouse.

## Set a query ID cache duration

Some data platforms support returning results of past queries from a cache using a query ID, such as Snowflake and BigQuery.

A workbook's cache duration, or time-to-live (TTL), refers to the duration within which Sigma attempts to retrieve results from the CDW's result cache using the query ID.

* If Sigma determines that the query ID cache can be used for a query and the last time the query was run against the CDW is within the query ID cache duration, Sigma does not attempt to re-run the query against the warehouse.
* If the last time the query was run against the warehouse is outside the query ID cache duration, Sigma retrieves the results from the CDW results cache using the query ID and renders the workbook, and in parallel Sigma executes the query against the warehouse. When the latest results are returned from the warehouse, Sigma updates the workbook elements.

For information about changing the TTL, see [Set a query ID cache duration](/docs/set-a-query-id-cache-duration).

## Manual refresh and refresh schedules

Use a refresh schedule, if necessary. For more information see [workbook refresh options](/docs/workbook-refresh-options).

> 🚩
>
> ### Sigma does not store query results, only the query ID returned by the warehouse. **Every data refresh re-queries the data in the warehouse.** Setting an auto-refresh might burden the connection and result in significant warehouse costs.

Updated 3 days ago

---

Related resources

* [Set a query ID cache duration](/docs/set-a-query-id-cache-duration)
* [Workbook Refresh Options](/docs/workbook-refresh-options)

* [Table of Contents](#)
* + [How Sigma reduces warehouse overhead](#how-sigma-reduces-warehouse-overhead)
  + - [Check browser cache](#check-browser-cache)
    - [Try alpha query](#try-alpha-query)
    - [Try query ID cache](#try-query-id-cache)
  + [Set a query ID cache duration](#set-a-query-id-cache-duration)
  + [Manual refresh and refresh schedules](#manual-refresh-and-refresh-schedules)