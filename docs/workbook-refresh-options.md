# Manage workbook refresh options

# Manage workbook refresh options

Sigma refreshes workbook data every time an individual opens or refreshes the workbook. If you want to refresh workbook data on a set schedule, such as for a workbook displayed on a screen without user interaction, you can set a custom refresh schedule.

Data elements can also be refreshed individually, but not on an automated schedule.

> 🚩
>
> ### Sigma does not store data. Every refresh re-queries the data in the warehouse. Setting an auto-refresh can burden the connection and result in significant warehouse costs.

## Requirements

* To set up a refresh schedule, you must have **Can Edit** [access](/docs/folder-and-document-permissions#document-permissions) to the individual workbook and you must be assigned an account type with the **Set workbook data refresh** permission enabled.
* If your workbook is embedded in a host application, the secure embed must be authenticated with JSON Web Tokens (JWTs) for a custom refresh schedule to apply to the embedded content. See [Create an embed API with JSON Web Tokens](/docs/create-an-embed-api-with-json-web-tokens).

## Set up a refresh schedule

To set up a refresh schedule for a workbook, do the following:

1. Click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) **More options** to the right of the refresh button in the workbook header.
2. Select **Data refresh**.  
   The **Data refresh settings** modal opens.
3. For **Refresh schedule**, turn on the **Enable** toggle.
4. Adjust the **Query data every** field to specify how often to refresh the workbook. For example, every 10 minutes.
5. [optional] To limit the refresh schedule to a specific time window, enter times in the **Between** fields. Sigma uses the browser timezone to evaluate whether the refresh schedule should be in effect.
6. Click **Save**.

## Refresh individual data elements

You can manually refresh the data in an individual data element.

1. Select the data element.
2. In the element toolbar, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**.
3. Click **Refresh data**.

   The data in the element refreshes.

Updated 3 days ago

---

Related resources

* [Set a query ID cache duration](/docs/set-a-query-id-cache-duration)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Set up a refresh schedule](#set-up-a-refresh-schedule)
  + [Refresh individual data elements](#refresh-individual-data-elements)