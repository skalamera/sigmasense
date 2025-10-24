# Schedule materialization for a version-tagged data model

# Schedule materialization for a version-tagged data model

If you have a data model with one or more tagged versions, you can set up [materialization](/docs/materialization) schedules for each version of the data model. For example, if you have “testing” and “production” tagged versions of a data model, you can schedule materialization for the data elements in each tag, which can improve the performance of downstream elements that rely on that tagged version of the data model.

When scheduling materialization of elements in version-tagged data models, the [best practices for materialization](/docs/materialization) still apply. For more details about scheduling materialization, see [Schedule materialization for a data model or workbook](/docs/schedule-materialization-for-a-data-model-or-workbook).

# Requirements

* To use this feature, you must be assigned an account type with the [permission to materialize data](/docs/account-type-and-license-overview).
* To materialize a data element, the connection for the data source must have write-back enabled.

# Schedule materialization for a tagged data model

For a data model with at least one tagged version, schedule materialization for one or more data elements in the tagged version. If you want to schedule materialization for the same data element across different tagged versions of the data model, create a schedule for each tagged version.

1. Open the data model.
2. In the document header, next to the refresh data button, click **More options** > **Materialization schedule...**.
3. In the **Materialization** modal, click **+ New schedule**. If you do not have any materialization schedules, click **Add schedule**.

   > 💡
   >
   > ### To duplicate an existing schedule instead, locate the schedule that you want to duplicate and select **More** > **Duplicate schedule**.
4. For **Version**, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/edit.svg) to modify the version, then in the dropdown, select the version tag to which the schedule applies.
5. For **Elements**, add data elements to the schedule. To materialize the same elements in the tagged version that are materialized in the published version or another tagged version of the data model, select **+ Add element**, then choose **Copy elements from schedule of other versions**.
6. Set the frequency of the schedule:

   * (Optional) Select the dropdown for **Daily** and select **Weekly**, **Monthly**, or **Custom**.

     + For **Daily**, select **Once a day** or **Multiple times**.
     + For **Weekly**, select which days of the week to run a materialization job, and choose between **Once a day** or **Multiple times**.
     + For **Monthly**, select which day of the month to run a materialization job, and the time of day.
     + For **Custom**, specify a schedule using cron syntax. See [Set up a custom delivery schedule](/docs/configure-additional-options-for-exports#set-up-a-custom-delivery-schedule).

       If you select **Multiple times**, specify the frequency. For example, every 2 hours on the :15 of the hour between 9 AM and 6 PM.
   * (Optional) Adjust the default schedule time zone using the dropdown menu.
7. Save the schedule.

> 📘
>
> ### When you promote a tag to a new version of the data model, such as moving a tag from an older version of the data model to the latest published version, a new materialization run is started. While the materialization runs for the newly tagged version, the materialized data for the previously tagged version of the data model is used.

Updated 3 days ago

---

[Schedule materialization for a dataset](/docs/schedule-materialization-for-a-dataset)[Best practices for improved performance](/docs/best-practices-for-improved-performance)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Schedule materialization for a tagged data model](#schedule-materialization-for-a-tagged-data-model)