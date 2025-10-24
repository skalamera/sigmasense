# Schedule materialization for a dataset

# Schedule materialization for a dataset

Materialize a dataset by scheduling materialization. The materialization schedule that you configure affects the data freshness for elements downstream. For more details, including limitations and best practices, see [About materialization](/docs/materialization).

## Requirements

* [Write access](/docs/set-up-write-access) must be enabled on your connection.
* To schedule materialization in a dataset, you must be assigned an account type with the **Schedule materializations** and **Create, edit, and publish datasets** permissions enabled.
* You must have **Can Edit** access to the dataset.

## Create a materialization schedule for a dataset

To materialize a dataset:

1. Open the dataset you want to materialize.
2. Select the **Materialization** tab and click **Create Schedule**.
3. In the **Add Materialization Schedule** modal, define a schedule to use to refresh the materialized data.
4. Click **Save**.

   The first materialization of the data begins immediately.

## Review the status of a dataset materialization

If a dataset is materialized, you can see the materialization status in the dataset header:

1. In the dataset header, click **Info** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/info.svg)) to open the dataset information.
2. In the **Materialization** section, review the status. To view more details, such as the last and next refresh date, hover over the status.

A user assigned the Admin account type can view the status and history of materializations from the **Materialization** tab at any time. See [Manage materializations](/docs/manage-materializations).

## Run a materialization job for a dataset

To manually run a scheduled materialization, do the following:

1. Open the dataset and select the **Materialization** tab.
2. In the **Schedule** section, click **Run Now**.

## Modify a dataset materialization schedule

To make changes to a dataset materialization schedule:

1. Open the dataset and select the **Materialization** tab.
2. In the **Schedule** section, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Edit Schedule**.
3. Define a new schedule.
4. Click **Save**.  
   The materialization schedule changes immediately. The next materialization occurs at the next scheduled time.

### Delete a dataset materialization schedule

To remove a materialization schedule for a dataset and delete the materialized data from the connected data platform:

1. Open the dataset and select the **Materialization** tab.
2. In the **Schedule** section, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Remove Schedule**.
3. In the confirmation that appears, select **Remove**.

   Sigma automatically removes the materialized table from your warehouse. It can take up to 24 hours for the table to be deleted.

Updated 3 days ago

---

[Schedule materialization for a data model or workbook (Beta)](/docs/schedule-materialization-for-a-data-model-or-workbook)[Schedule materialization for a version-tagged data model](/docs/schedule-materialization-for-a-version-tagged-data-model)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Create a materialization schedule for a dataset](#create-a-materialization-schedule-for-a-dataset)
  + [Review the status of a dataset materialization](#review-the-status-of-a-dataset-materialization)
  + [Run a materialization job for a dataset](#run-a-materialization-job-for-a-dataset)
  + [Modify a dataset materialization schedule](#modify-a-dataset-materialization-schedule)
  + - [Delete a dataset materialization schedule](#delete-a-dataset-materialization-schedule)