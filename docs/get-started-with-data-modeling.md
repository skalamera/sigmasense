# Get started with data modeling

# Get started with data modeling

Data models provide a semantic layer for your data, letting you organize and store data in a structured governed way without modifying raw data. Most importantly, data models are reusable. When you create a data model, you can centralize business logic and metrics, minimizing repeated work like writing joins or long formulas.

* [Build data models with reusable data source elements.](/docs/create-and-manage-data-models)
* [Define relationships between related data sources](/docs/define-relationships-in-data-models) instead of building bespoke joins at analysis-time.
* [Define metrics to improve the consistency of aggregated analysis](/docs/about-metrics).

Data models make it easier to work with data and increase user confidence in the results of their analysis. You don't need to use a data model to work with data in Sigma, but data models let you enable business users performing analysis or exploration with governed, curated, and frequently revisited data.

## About data models

A data model is a type of Sigma document that provides the framework for creating and managing a collection of reusable data source elements. You can curate focused views of data from your connected platform which users can then use as sources in workbooks or other data models.

Data models offer a comprehensive, dynamic platform to consolidate, transform, and share related data that your organization members can reuse in workbooks and other data models. A single data model serves as a container for a collection of reusable elements that can offer different subsets, perspectives, or evaluations of the data model’s broader data context. This cumulative data representation facilitates a convenient, structured foundation for building relevant, detailed workbook analyses.

Data models also provide the following benefits:

* **Centralized permissions:** Grant permissions at the data model level for consistent, streamlined access control.
* **Efficient data handling:** Enhance reusable elements with controls to easily filter and refine data segments.
* **Flexible reusability:** Quickly enable or disable elements for reuse as data sources.

With a well-designed data model, users can easily access the data they need for analysis, reducing the time and effort required to analyze data.

## Data models and datasets

Data models support the same functionality as datasets, and more:

* [Metrics](/docs/about-metrics)
* [Relationships](/docs/define-relationships-in-data-models)
* [Column-level security](/docs/column-level-security)
* [Row-level security](/docs/dataset-row-level-security)
* [Materializations](/docs/materialization)
* [Warehouse views](/docs/dataset-warehouse-views)
* [Parameters](/docs/parameters-in-workbooks)
* [URL parameters](/docs/workbook-control-values-in-the-url)
* [Version tagging](/docs/add-version-tags-to-workbooks-and-data-models) (data models only)

Data models and reusable elements are designed to replace the existing dataset functionality. Sigma will eventually deprecate datasets but will continue to support them until data models are fully developed and can facilitate a seamless transition. Prior to this deprecation, Sigma will notify all customers and implement an automated migration path to convert all datasets to data models.

## Best practices for data modeling

When building a data model, start with the most granular data and build relationships and metrics as relevant to develop the reusable data source elements.

* **Avoid circular schemas** where relationships reference upstream tables.
* **Apply filters** to data to provide only the most relevant data downstream of the data model.
* **Add descriptive titles** and include a description to help users decide if the data source fits their use case.
* **Materialize your data** to improve performance, and schedule materialization to occur after database updates to ensure the latest data is always available.

For more details, see [Data model best practices](https://community.sigmacomputing.com/t/data-model-best-practices/5011) in Sigma Community.

Updated 3 days ago

---

[Troubleshoot input table connection issues](/docs/troubleshoot-input-table-connection-issues)[Data models](/docs/data-models)

* [Table of Contents](#)
* + [About data models](#about-data-models)
  + [Data models and datasets](#data-models-and-datasets)
  + [Best practices for data modeling](#best-practices-for-data-modeling)