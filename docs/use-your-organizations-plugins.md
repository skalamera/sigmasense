# Use your organization's plugins

# Use your organization's plugins

With Sigma, you can add plugin elements to workbooks, to support custom functionality that isn't standard with Sigma's deployment. You only have access to plugins registered with your organization. Plugins are third-party applications built to add additional functionality into an existing product. For example, a software developer in your organization may create a plugin that lets you display your data in a chart type not otherwise supported in Sigma.

## Requirements

To add or edit a workbook element through a plugin:

* You must be a [Creator or Admin](/docs/user-account-types), or have a [custom account type](/docs/user-account-types#custom-account-types) with appropriate permissions.
* You must have **Can Edit** [access](/docs/folder-and-document-permissions#document-permissions) to the relevant workbook.

## Add an element to a workbook through a plugin

Plugin-based elements only accept [data elements](/docs/intro-to-data-elements) as data sources. The source data element must be in the same workbook as the plugin.

This action is only available in edit mode. To begin editing, click **Edit** in the top right corner of the page; see [Workbook lifecycle](/docs/workbook-lifecycle-explore-draft-and-publish).

1. Open the workbook's **ADD NEW** panel.
2. Select **PLUGINS**.  
   ![Screen_Shot_2022-02-03_at_8.31.47_AM.png](https://files.readme.io/f9e0a7f-1.png)
3. Select a plugin type from the list.  
   ![Screen_Shot_2022-02-03_at_8.33.25_AM.png](https://files.readme.io/d3f4274-2.png)  
   Your new blank plugin-based element will appear on the page.  
   ![Screen_Shot_2022-02-03_at_8.35.13_AM.png](https://files.readme.io/bbd4ee0-3.png)
4. Configure your element’s values using the editor panel.

   Individual plugins define each element’s configuration options.

   Plugins only have access to the first 25,000 rows in a data source. Therefore, [group and aggregate](/docs/create-and-manage-tables#groups-and-groupings) data to reduce the total number of rows. If your data source already contains groupings, the editor panel prompts you to select an aggregate level.

   ![Screen_Shot_2022-02-03_at_8.36.28_AM.png](https://files.readme.io/da70c96-4.png)

Updated 3 days ago

---

Related resources

* [Register a Plugin with your Sigma Organization](/docs/register-a-plugin-with-your-sigma-organization)
* [Get Started with Custom Plugins](/docs/get-started-with-custom-plugins)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Add an element to a workbook through a plugin](#add-an-element-to-a-workbook-through-a-plugin)