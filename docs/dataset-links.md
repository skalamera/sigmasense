# Dataset Links

# Dataset Links

Links create a pre-defined join pathway between two data sources. When you define a link, users can easily add columns from the linked data sources to workbooks, based on the dataset. Sigma pulls in data relationships that already exist in your database. If you have foreign keys set up in your warehouse, you should automatically see those relationships in the Links tab.

Data added through links always appear in a Left Join. Links only support Many-to-One or One-to-One relationships. Each row in your source object should have at most one possible result in your target object; otherwise, incorrect results can be introduced into workbooks that use the link, affecting subsequent calculations and charts.

The power of Sigma’s links is that you can do more than create links between tables. You can create a link between any two data sources in Sigma. You can create a dataset that defines Metrics, then link it to a warehouse table so that users can pull in additional customer information. You can create a link between two datasets, two warehouse tables, or any other combination. Links allow you to create pathways of exploration, without limiting your users.

Additionally, Sigma preserves the work you’ve already done to set up relationships between your database tables.

When running Sigma over multiple linked tables, you must ensure that the underlying tables with links have their relationship already defined in the primary data source. After creating links, all linked columns appear in the Worksheet tab in Datasets, and you can create the necessary calculated columns. See [Use linked columns in workbooks](/docs/use-linked-columns-in-workbooks).

## Create Links

1. Use the left-hand navigation menu to navigate to the dataset or table you would like to create a Link for.
2. Open to the **Links** tab.
3. Click the **Edit** button in the top right.
4. Click **Add Link** to other sources.
5. Use the left-hand menu to choose the data source you would like to connect to. Ensure that your source data has a one-to-one or many-to-one relationship with the target data.
6. Once you select the data source, a preview will appear.
7. Click **Next** in the page header.
8. Preview your join column and the join results on the right hand side of the screen.
9. Click **Accept** in the page header.
10. You will now see your new Link listed on the **Links** tab.
11. Click **Publish** to save and publish your new Link.

![](https://files.readme.io/281fad1-18-dataset-links.png)

For details on using links, see [Use linked columns in workbooks](/docs/use-linked-columns-in-workbooks).

Updated 3 days ago

---

[Configure Dataset Columns](/docs/configure-dataset-columns)[Create a dataset from SQL](/docs/create-a-dataset-from-sql)

* [Table of Contents](#)
* + [Create Links](#create-links)