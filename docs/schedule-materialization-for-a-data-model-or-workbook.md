# Schedule materialization for a data model or workbook (Beta)

# Schedule materialization for a data model or workbook (Beta)

> 🚩
>
> ### Materialization of data elements in data models is generally available.
>
> Materialization of data elements in workbooks is in public beta.
>
> This documentation describes a public beta feature and is under construction. This documentation should not be considered part of our published documentation until this notice, and the corresponding Beta flag on the feature in Sigma, are removed. As with any beta feature, the feature discussed below is subject to quick, iterative changes. The latest experience in the Sigma service may differ from the contents of this document.  
> Beta features are subject to the disclaimer on [Beta features](/docs/beta-features).

Materialize a data element in a workbook or data model by scheduling materialization. The materialization schedule that you configure affects the data freshness for elements downstream. For more details, including limitations and best practices, see [About materialization](/docs/materialization). If your data model uses version tags, see [Schedule materialization for a version-tagged data model](/docs/schedule-materialization-for-a-version-tagged-data-model).

## Requirements

* [Write access](/docs/set-up-write-access) must be enabled on your connection.
* To schedule materialization in a data model, you must be assigned an account type with the **Schedule materializations** and **Create, edit, and publish datasets** permissions enabled.
* To schedule materialization in a workbook, you must be assigned an account type with the **Schedule materializations** and **Create, edit, and publish workbooks** permissions enabled.
* You must have **Can Edit** access to the workbook or data model.

## Create a data element materialization schedule

You can materialize specific data elements in a workbook or data model:

> 📘
>
> ### A data element can only have one materialization schedule, but you can create one schedule to materialize multiple elements.

1. Open a data model or workbook for editing.
2. Locate the element that you want to materialize and click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** to open the element menu.
3. Select **Advanced options** > **Schedule materialization...**.
4. In the **Materialization schedules** modal, set up a schedule to materialize data elements:

   * (Optional) Select the dropdown for **Daily** and select **Weekly**, **Monthly**, or **Custom**.

     + For **Daily**, select **Once a day** or **Multiple times**.
     + For **Weekly**, select which days of the week to run a materialization job, and choose between **Once a day** or **Multiple times**.
     + For **Monthly**, select which day of the month to run a materialization job, and the time of day.
     + For **Custom**, specify a schedule using cron syntax. See [Set up a custom delivery schedule](/docs/configure-additional-options-for-exports#set-up-a-custom-delivery-schedule).

       If you select **Multiple times**, specify the frequency. For example, every 2 hours on the :15 of the hour between 9 AM and 6 PM.
   * (Optional) Adjust the default schedule time zone using the dropdown menu.

   > 📘
   >
   > ### If an element contains multiple grouping levels, select a grouping level to materialize. Sigma materializes the selected grouping level and all levels above the selected grouping. It's often unnecessary and potentially costly to materialize the most granular level (**All source columns**) of a grouped element.
5. Click **Save schedules**.

   The materialization run starts immediately using the latest published version of the workbook.

   > 🚩
   >
   > ### If you use OAuth to authenticate to your data platform, the materialization job runs as the user who scheduled the materialization. To use a service account to perform materialization instead, run the workbook as a service account. See [Run a workbook with service account credentials](/docs/run-a-workbook-with-service-account-credentials).

### Set up a dependent materialization schedule

If you materialize both parent and child elements, you can set up a dependent materialization schedule for child elements. In a dependent materialization schedule, materialization for one or more child elements runs after a parent element materialization successfully completes. Dependent materialization helps ensure that the data in child elements reflects the latest data available in the parent element.

A parent element can be multiple levels upstream in the same workbook, data model, or across data models. To identify parent and child elements, review the [data lineage for a workbook](/docs/workbook-data-lineage) or data model.

To set up a dependent materialization schedule, do the following:

1. Open a data model or workbook for editing.
2. Locate the child element that you want to materialize and click **More** to open the element menu.
3. Select **Advanced options> Schedule materialization...**.  
   The **Materialization schedules** modal opens with a draft schedule for the selected element.
4. In the **Frequency** section, for **Select a run time**, choose an option:

   * To materialize the child element only after the parent element materialization finishes successfully, select **After selected parent schedule finishes** and choose the relevant parent schedule in the dropdown menu.
   * To materialize the child element on its own schedule, separate from the materialization schedule of the parent element, select **Manual Time** and specify a frequency.
5. [optional] If you want to materialize multiple elements in the same schedule, select **+Add element** and select another element. Elements that are not children of the parent element can still be materialized in a dependent schedule as long as at least one element in the schedule is a child element of a materialized parent element.
6. Select **Save schedules**.

After saving the schedule, the dependent schedule appears as part of the same schedule as the parent schedule. If the parent schedule is paused or fails, the dependent schedule is also paused or fails.

> 📘
>
> ### If the materialization schedule for the parent element is deleted, the dependent schedule updates to match the frequency set for the parent element.

## Review the status of a materialized data element

You can see the status of the materialization in several places:

* When you view a data element in a workbook or data model, the status of the materialization displays on the element menu.

  ![Element toolbar showing filter option, materialization icon with a green checkmark to indicate success, child visualization option, expand to show underlying data option, and the more menu.](https://files.readme.io/7c31688de23c0a86d2678e02ee7c7e3470c723687867427138cb6421bc5da3c4-element-mat.png)
* When you review the lineage for the data element, the materialization status is shown.

  ![Element selected in the lineage, and information about the materialization status visible with a green checkmark on the element and in the details pane, listing the materialization status, next materialization, and options to materialize now or view the schedule.](https://files.readme.io/3365082e4877578b724d316e26a6b79a07b2be240e19c09c3c06a3a0f6eb972e-mat-lineage.png)

To review the history of materialization for a data element:

1. Open a data model or workbook for editing.
2. Locate the element that you want to materialize and click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** to open the element menu.
3. Select **Advanced options** > **Schedule materialization...**.
4. In the **Materialization schedules** modal, select **History**.
5. Review the materialization history for all elements in the workbook or data model:

   * Review the status of the materialization. For a failed materialization, you can copy the error message.
   * Review the start time and runtime for a materialization.
   * Review the amount of data materialized by total rows and total bytes.
   * Select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** to materialize an element immediately, or go to the schedule that materializes the element.

## Run a scheduled materialization for a data element

To immediately materialize a data element with a scheduled materialization:

1. Select the materialized data element.
2. In the menu, select **View materialization info** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/info.svg)).

   If the option is not available, the element is not materialized. See [Create a data element materialization schedule](#create-a-data-element-materialization-schedule).
3. In the menu that appears, click **Materialize now**.

   The materialization run starts immediately using the latest published version of the workbook.

You can also run a data element materialization from the schedule, for example, if you want to immediately run a materialization for all or multiple elements in the same schedule:

1. Select the materialized data element.
2. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** to open the element menu.
3. Select **Advanced options** > **Schedule materialization...**.
4. In the **Materialization schedules** modal, review the elements in the schedule and choose which to materialize immediately:

   * To materialize all elements in the schedule, in the header row, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Materialize all now**.
   * To materialize an individual element in the schedule, locate the element row, then select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Materialize now**.

   The materialization run starts immediately using the latest published version of the workbook.

## Manage the materialization schedule for a data element

You can modify the materialization schedule to change the materialization frequency or which elements are materialized. You can also delete one or more elements from the schedule, or the entire schedule. When you delete an element or an entire schedule, the associated tables are deleted from the data platform within 24 hours.

1. Open a data model or workbook for editing.
2. Locate the element that you want to materialize and click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** to open the element menu.
3. Select **Advanced options** > **Schedule materialization...**.
4. In the **Materialization schedules** modal, make the desired changes:

   * Modify the frequency of the schedule.
   * Remove an element from the schedule. Locate the element row, then select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Remove element**.
   * Delete the schedule by selecting **Delete schedule**.

As an admin, to manage additional materialization functionality, see [Manage materializations](/docs/manage-materializations).

Updated 3 days ago

---

[About materialization](/docs/materialization)[Schedule materialization for a dataset](/docs/schedule-materialization-for-a-dataset)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Create a data element materialization schedule](#create-a-data-element-materialization-schedule)
  + - [Set up a dependent materialization schedule](#set-up-a-dependent-materialization-schedule)
  + [Review the status of a materialized data element](#review-the-status-of-a-materialized-data-element)
  + [Run a scheduled materialization for a data element](#run-a-scheduled-materialization-for-a-data-element)
  + [Manage the materialization schedule for a data element](#manage-the-materialization-schedule-for-a-data-element)