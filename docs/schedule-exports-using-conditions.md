# Schedule a conditional export or alert

# Schedule a conditional export or alert

You can schedule an export to send only if specific conditions are met, functioning as a conditional alert. Trigger an export based on whether data is available, or on the specific value of a control or column. This flexibility lets you fine tune recurring exports and ensure efficiency and relevance of the exported reports.

For example, configure a conditional alert to support outlier and anomaly detection workflows, sending a Slack notification when data in a specific column is above a specific value, or matches a specific anomalous condition. See [Alert on detected outliers and anomalies](#alert-on-detected-outliers-and-anomalies).

This document explains how to schedule a recurring export with a predefined condition.

## User requirements

The ability to add conditions to scheduled exports requires the following:

* You must be assigned an [account type](/docs/user-account-types) with the **Schedule exports** permission enabled.
* You must be the workbook owner or be granted **Can explore** or **Can edit** [workbook permission](/docs/folder-and-document-permissions).

> 📘
>
> ### Additional requirements might apply depending on the export destination. See the **Sharing and exports** section in [Account type permission availability matrix](/docs/account-type-and-license-overview#account-type-permission-availability-matrix) for details.

## About conditional exports and alerts

A predefined data condition acts as a filter to determine whether Sigma initiates a scheduled export. When an export is due, Sigma checks the data and only proceeds if the condition is met. The recurring schedule ensures that an export is timely, while the condition ensures it is relevant.

When you [filter your export by control values](/docs/configure-additional-options-for-exports#filter-by-control-values), Sigma performs the filter before checking if the condition is met.

> 🚧
>
> When executing a scheduled export or direct download to PDF or PNG formats, Sigma may store applicable control values as URL parameters in trace logs used for debugging and troubleshooting purposes. Exercise caution when exporting or downloading workbook content that uses controls to filter sensitive data.

## Schedule an export based on data availability

Schedule a recurring export that only initiates when a specific data element or input table meets a predefined data condition.

1. In a workbook header, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) associated with the workbook's name and select **Share and export> Schedule exports...**.
2. If this is the first schedule for the workbook, click **Add schedule**, otherwise click **+ New schedule**.
3. In the **Frequency** section, for **Send**, select **If a condition is met**.
4. (Optional) If you choose to send an export only If a condition is met, you can turn on the switch to stop notifying after a set number of occurrences per day, week, or in total. (This feature is in beta and subject to the [Beta features notice](/docs/sigma-product-releases#beta-features)).
5. In the **Condition** section, specify the condition settings:

   1. For **Send**, specify the condition under which to send the export:

      * **If there's no data**: Export as scheduled if there is no data available in the target element.
      * **If there's data**: Export as scheduled if data is available in the target element.
   2. For **In data element**, select the target element to which the data availability applies.

      > 📘
      >
      > ### Although the condition applies to a single target element, you can configure the schedule to export the entire workbook, specific pages, and individual elements.
   3. Click **Test condition** to check if the target element currently meets the condition. If the results don’t align with your expectations, confirm that you selected the correct condition and target element.

   ![Screenshot of described settings in the Schedule exports dialog](https://files.readme.io/7d188d072d379cce41c82d2d55cd122c097843d371e8f09d45606279ffbc4b09-scheduleexportconditional2_1.png)
6. Complete the remaining sections in the **Schedule exports** modal. For more information, see the following documentation based on the preferred export destination.

   > 📘
   >
   > ### Destination availability depends on [account type permissions](/docs/create-and-manage-account-types).

   * [Export to email](/docs/send-a-workbook-export-to-email-recipients)
   * [Export to Slack](/docs/send-slack-notifications)
   * [Export to Google Sheets](/docs/export-to-google-sheets)
   * [Export to Google Drive](/docs/export-to-google-drive)
   * [Export to webhook](/docs/export-to-webhook)
   * [Export to cloud storage](/docs/export-to-cloud-storage)
   * [Export as email burst](/docs/export-as-email-burst)
7. Click **Create** to save the configured schedule.

## Schedule an export based on a conditional statement

Schedule a recurring export that only initiates when a specific data element or input table satisfies a predefined conditional statement.

1. In the workbook header, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) associated with the workbook's name and select **Share and export> Schedule exports...**.
2. If this is the first schedule for the workbook, click **Add schedule**, otherwise click **+ New schedule**.
3. In the **Frequency** section, for **Send**, select **If a condition is met**.
4. (Optional) If you choose to send an export only If a condition is met, you can turn on the switch to stop notifying after a set number of occurrences per day, week, or in total. (This feature is in beta and subject to the [Beta features notice](/docs/sigma-product-releases#beta-features)).
5. In the **Condition** section, specify the condition settings:

   1. For **Send**, select **If a condition is met** to export as scheduled if a specific data condition in the target element is met.
   2. For **In data element**, select the target element to which the condition applies.

      > 📘
      >
      > ### Although the condition applies to a single target element, you can configure the schedule to export the entire workbook, specific pages, and individual elements.
   3. Define the conditional statement. For **Check if**, select which element values to apply the condition to:

      * **Any value**: The condition must match for one or more values in the column.
      * **All values**: The condition must match for all values in the column.

      If the selected element is a KPI, you can check additional conditions:

      * **{Element title}**: One or more values in the element's **Value** property column must meet the criteria.
      * **Comparison value (%)**: One or more values in the element's **Comparison** property column must meet the criteria.
   4. If you selected **Any value** or **All values**, for **In column**, specify the column to be used.
   5. For **Is**, select a comparison operator.
   6. For **Value**, select a comparison value.
   7. Click **Test condition** to check if the target element currently meets the condition. If the results don’t align with your expectations, confirm that you selected the correct condition and target element.
      ![](https://files.readme.io/4fd6a5af4bdf657f7ce8457b66b048700f62925bc3ee5af342ccbb724dcb11ad-scheduleexportconditional_4.png)
6. Complete the remaining sections in the **Schedule exports** modal. For more information, see the following documentation based on the preferred export destination:

   > 📘
   >
   > ### Destination availability depends on your [account type permissions](/docs/create-and-manage-account-types).

   * [Export to email](/docs/send-a-workbook-export-to-email-recipients)
   * [Export to Slack](/docs/send-slack-notifications)
   * [Export to Google Sheets](/docs/export-to-google-sheets)
   * [Export to Google Drive](/docs/export-to-google-drive)
   * [Export to webhook](/docs/export-to-webhook)
   * [Export to cloud storage](/docs/export-to-cloud-storage)
   * [Export as email burst](/docs/export-as-email-burst)
7. Click **Create** to save the configured schedule.

## Schedule a conditional alert for an element

To monitor a specific data element or input table, schedule a recurring export as a conditional alert, such as an email or Slack message.

> 💡
>
> ### You can create a conditional alert using the steps in the previous sections of this document, this method auto-populates specific fields to make it easier to quickly configure a conditional alert.

1. In the element toolbar, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** to open the element menu, then select **Alert when**.

   > 📘
   >
   > ### You can only create alerts for published content. If the target element hasn’t been published or contains unpublished changes, Sigma prompts you to publish the workbook.
2. In the **Schedule exports** modal, configure the alert. Sigma configures a default conditional statement in the **Condition** section (based on the type of target element), auto-populates the target element’s title as an email **Subject** or Slack **Message**, and selects the target element in the **Attachments** field.

   1. Customize fields as desired, then complete the remaining sections. For more information, see [Schedule an export based on data availability](#schedule-an-export-based-on-data-availability) and [Schedule an export based on a conditional statement](#schedule-an-export-based-on-a-conditional-statement) in this document.
   2. Click **Create** to save the schedule configurations.

## Alert on detected outliers and anomalies

You can set up an alert based on detected outliers and anomalies in your data, either a threshold-defined anomaly, or write a formula to detect outliers and anomalies and alert based on the output of the formula.

For example, you might do one of the following:

* [Configure a static threshold alert](#configure-a-static-threshold-alert)
* [Configure a formula-based threshold alert](#configure-a-formula-based-threshold-alert)

### Configure a static threshold alert

For example, if you want to monitor anomalous page visits to your website, you might configure an alert that sends a Slack message when page views exceed a known threshold, such as 25,000 views for a specific day. You can recreate this example with the Sigma Sample Database Google Analytics Events data.

1. For a website analytics data source, use a [table grouping](/docs/create-and-manage-tables#group-columns-in-a-table) to calculate total page views per day:
   ![](https://files.readme.io/df56b7024c87e393ed8d0b9e35453694a90ca890abe843ab165a6658fc020f2e-outlier-base.png)
2. Use a [date control element](/docs/intro-to-control-elements#date) to filter the table to now minus 1 day, to see data for the previous day:
   ![](https://files.readme.io/b703db189a944375cc124de602a0a82529ea49a48da32c9553afa2818298c0f4-outlier-pv-grouped.png)
3. On the table, configure an alert when page views exceed a specific threshold:

   1. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** to open the element menu, then select **Alert when**.
   2. Set up the email or Slack recipient and message as desired.
   3. In the **Condition** section, set **Check if** to **Any value**.
   4. For **In column**, select the *Total Page Views* column.
   5. For **Is**, choose the operator to evaluate the threshold. In this case, **Greater Than**.
   6. For **Value**, set the threshold. In this case, set a threshold of **25000**.

      ![Conditional alert for an element configured to send if the total page views column has any value that is greater than 100000](https://files.readme.io/2b83caf92c95076d8aa59a11a8376f34eb1a6bb21980573e05c6c6e26b3951d1-b8099457b50c378cda44b68f49d8062d164d92ac541caed90cc55e9e15b861d9-send-if-over-threshold.png)
   7. In the **More options** section, select the checkbox for **Customize control values**.
   8. For **Controls**, select the date control and validate that the selection is correct.

      ![Customize control values set to previous-day, showing a relative date selected of 1 day ago and the date 2/19/2025.](https://files.readme.io/7301b698c390350c5e17057e49fe7519a65fec6dddf553d9cfa30ecae3aeabca-outlier-control-config.png)
4. Click **Create** to save the alert.

### Configure a formula-based threshold alert

For example, if you want to monitor anomalous page visits to your website, you might write a formula to identify anomalous traffic, then configure an alert that sends a Slack message when the formula output indicates anomalous traffic.

Following the guidance in [How to Detect Outliers in Sigma](https://community.sigmacomputing.com/t/how-to-detect-outliers-in-sigma/2124) in the Sigma Community, set up a data table and alert as follows. You can recreate this example with the Sigma Sample Database Google Analytics Events data.

1. For a website analytics data source, use a table grouping to calculate total page views per day.
2. Add a summary column to calculate the standard deviation of the *Total Page Views* column: `Stddev([Total Page Views])`. Rename the summary column *Standard Deviation*.
3. Add a summary column to calculate the average value of the *Total Page Views* column: `Avg([Total Page Views])`. Rename the summary column *Average*.

   ![Grouped table with summaries showing Standard Deviation of 8370.78 and Average of 21,736.89.](https://files.readme.io/35c00a38e0d7f16c130a06ebbfa1d8e4baaab7b49990b270e318f8a3941eff68-outlier-summaries.png)
4. Based on your data, determine what an upper and lower bound would be considered for your data. Add two new summary columns:

   * One summary column named *Upper Bound*: `[Average] + (1.5 * [Standard Deviation])`
   * One summary column named *Lower Bound*: `[Average] - (1.5 * [Standard Deviation])`![Grouped table with four summaries showing Standard Deviation of 8370.78 and Average of 21,736.89 and Upper Bound of 34,293.06 and Lower Bound of 9,180.73.](https://files.readme.io/d5c22cb975622cb1346e1239040dab6a303a7af2005432c80cc4c8991ca2a8c4-outliers-all-summaries.png)
5. Add a new calculated column *isOutlier* to the table grouping to evaluate whether each *Total Page Views* value falls within the acceptable bounds, or is an outlier: `If(Between([Total Page Views], [Lower Bound], [Upper Bound]), False, True)`

   Each column with a value **True** for the *isOutlier* column is considered an outlier according to the formula that you defined.

   ![Table with summary columns collapsed showing only Day of Event Date, Total Page Views, and isOutlier column. On 2025-02-11 there are total page views of 36182, which is above the Upper Bound, so the isOutlier column is True for that row.](https://files.readme.io/ba3f06d951fef787d552523ead39cdb1c1e121af92327dc4b1575208fc34933d-outlier-web-traffic-isoutlier.png)
6. On the table, configure an alert when page views are anomalous and the *isOutlier* column is true:

   1. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** to open the element menu, then select **Alert when**.
   2. Set up the email or Slack recipient and message as desired.
   3. In the **Condition** section, set **Check if** to **Any value**.
   4. For **In column**, select the *isOutlier* column.
   5. For **Is**, leave the default operator of **Equal to**.
   6. For **Value**, choose **True** to send an alert when the *isOutlier* column is **True**.

      ![Conditional alert for an element configured to send if the isOutlier column is set to true as described in the surrounding text.](https://files.readme.io/5808e8b7a9ace634d79b9af1b0c1a8f90e0f1f70df386a181acf1557369239d6-outlier-condition.png)
7. Click **Create** to save the alert.

Updated 3 days ago

---

[Send or schedule workbook exports](/docs/send-or-schedule-workbook-exports)[Download workbook data](/docs/download-workbook-data)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [About conditional exports and alerts](#about-conditional-exports-and-alerts)
  + [Schedule an export based on data availability](#schedule-an-export-based-on-data-availability)
  + [Schedule an export based on a conditional statement](#schedule-an-export-based-on-a-conditional-statement)
  + [Schedule a conditional alert for an element](#schedule-a-conditional-alert-for-an-element)
  + [Alert on detected outliers and anomalies](#alert-on-detected-outliers-and-anomalies)
  + - [Configure a static threshold alert](#configure-a-static-threshold-alert)
    - [Configure a formula-based threshold alert](#configure-a-formula-based-threshold-alert)