# Manage organization schedules

# Manage organization schedules

As a Sigma admin, you can view and manage an organization-wide list of scheduled reports in the Administration portal.

You can also manage exports for a specific workbook, or those that you own. See [Manage scheduled exports](/docs/manage-scheduled-exports).

## Requirements

* The complete list of organization schedules is only available for users assigned the [Admin](/docs/user-account-types) account type.

## View and manage organization schedules

To view your organization's schedules:

1. Open the Administration portal.
2. Go to **Exports** and select the **Scheduled exports** tab to see a list of all scheduled exports for your organization.

   You can search for a specific schedule by workbook name, filter by attachment, destination, and export conditions, or sort columns to locate the scheduled export you want to manage.

## Delete a schedule

1. Open the Administration portal.
2. Go to **Exports** and select the **Scheduled exports** tab.
3. Locate the schedule that you want to delete.
4. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**, then click **Delete**.

   The schedule is deleted.

### Delete scheduled exports in bulk

You can select multiple schedules to delete at the same time.

1. In the Administration portal, go to **Exports** and select the **Scheduled exports** tab.
2. Select the checkbox for each schedule that you want to delete, or select the checkbox in the column header row to select all visible scheduled exports.
   ![](https://files.readme.io/61f67a8-bulkdeleteexports.png)
3. Click **Delete** ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/trash.svg) to delete the selected scheduled exports.
4. Click **Confirm**.

## Edit or view a schedule

To edit or view a specific scheduled export for a workbook, select the workbook name to open the workbook.
See [Manage schedules for a workbook](/docs/manage-scheduled-exports#manage-schedules-for-a-workbook).

## Use AI export schedule names

For all organizations that have an [AI provider assigned](/docs/getting-started-with-ai), Sigma uses AI to generate export schedule names based on your export attachment name, export destination type and format, and set conditions. These names are visible when viewing all your or your organization's scheduled exports in Sigma, and do not affect the contents of the export itself.

Organizations without an AI provider assigned will use default names, based on export destination, attachment name, and format type.

Updated 3 days ago

---

Related resources

* [Manage Your Schedules](/docs/manage-your-schedules)
* [Send and schedule exports from workbooks](/docs/send-and-schedule-exports-from-workbooks)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [View and manage organization schedules](#view-and-manage-organization-schedules)
  + [Delete a schedule](#delete-a-schedule)
  + - [Delete scheduled exports in bulk](#delete-scheduled-exports-in-bulk)
  + [Edit or view a schedule](#edit-or-view-a-schedule)
  + [Use AI export schedule names](#use-ai-export-schedule-names)