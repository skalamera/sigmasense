# Manage scheduled exports

# Manage scheduled exports

You can view and manage scheduled exports, such as to stagger the schedules of exports, remove no longer needed scheduled exports, or to update the configuration of a scheduled export.

* [Manage schedules for a workbook](#manage-schedules-for-a-workbook).
* [Manage scheduled exports that you own or subscribe to](#view-and-manage-schedules-in-your-profile).
* As an admin, [manage all scheduled exports for your organization](/docs/manage-organization-schedules).

> 💡
>
> ### If you have multiple scheduled exports, it's a best practice to stagger the schedules. Staggering schedules helps to reduce the load on Sigma and on the data warehouse.

## User requirements

The ability to send and schedule workbook exports requires the following:

* To export to a specific destination, you must be assigned an [account type](/docs/create-and-manage-account-types) with the export permission for that destination enabled.
* To schedule a workbook export, you must be assigned an [account type](/docs/create-and-manage-account-types) with the **Schedule export** permission enabled.
* You must be the workbook owner or be granted **Can explore** or **Can edit** [workbook permission](/docs/folder-and-document-permissions).

> 📘
>
> ### Additional requirements and permissions might apply depending on the export destination.

## Manage schedules for a workbook

1. From the workbook menu (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)), select **Schedule exports**.  
   The **Schedule Exports** dialog opens.
2. You can review the list of scheduled exports for the workbook, reviewing the times and types of exports to identify overlapping schedules or recipients.
3. For a specific scheduled export, you can click the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** menu to rename the schedule, edit the schedule, send the configured scheduled export immediately, pause the scheduled export, or delete it.

   ![Schedule exports page with the drop-down menu for the schedule displayed, listing Rename Schedule, Edit, Send Now, Pause, and Delete options.](https://files.readme.io/c454fc3-export-more-menu-open.png)

### Edit or delete a schedule

1. From the workbook menu (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)), select **Schedule exports**.  
   The **Schedule Exports** dialog opens.
2. Locate the schedule you want to send and click the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** menu.
3. Click **Delete** to delete the schedule or **Edit** to make changes to the schedule.  
   ![](https://files.readme.io/c454fc3-export-more-menu-open.png)

### Send a scheduled export on demand

If you want to send a scheduled export without waiting for the next scheduled run of the export, you can send it on demand.

1. From the workbook menu (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)), select **Schedule exports**.
2. Locate the schedule that you want to send and click the **More** menu (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg)), then select **Send now**.

### Pause or resume a scheduled export

You can manually pause and resume scheduled exports.

1. From the workbook menu (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)), select **Schedule exports**.

   The **Schedule Exports** dialog opens.
2. Click the **More** menu of the **Actions** column and select **Pause**.

   ![Schedule exports page with the drop-down menu for the schedule displayed, listing Rename Schedule, Edit, Send Now, Pause, and Delete options.](https://files.readme.io/c454fc3-export-more-menu-open.png)
3. In the **Status** column, the status changes to **Paused**.
4. To resume an export, repeat the above steps but choose **Resume** from the **More** menu.

   ![Schedule exports page with the drop-down menu for the schedule displayed, listing Rename Schedule, Edit, Send Now, Resume, and Delete options](https://files.readme.io/532d663-export-more-resume-paused.png)

#### Auto-paused scheduled exports

If a scheduled export fails more than 10 times consecutively, Sigma pauses the export schedule and the owner of the schedule receives an email notification.

The email notification contains the following message:

`Document export failed. Sigma has paused one of your scheduled exports. Please use the below link to the workbook to check details.`

You can manually resume the export. The **Status** column shows **Paused** with an exclamation point. To resume the paused export, choose **Resume** from the **More** menu in the **Actions** column.

![Schedule Exports page with a paused (!) export. Hovering over the (!) exclamation mark in a triangle icon shows information that "This schedule has been paused by Sigma on 07/13/2022 - 06:05 PM due to repeated failures. Error: Target Google Spreadsheet is not found." and provides an incident ID.](https://files.readme.io/d0a53ac-5.png)

## Manage your scheduled exports and subscriptions

From your user profile, you can view and manage scheduled exports that you own or receive.

If you are a Sigma admin, you can view or manage all scheduled exports for your organization. See [Manage organization schedules](/docs/manage-organization-schedules).

### View and manage schedules in your profile

To view and manage scheduled exports from your profile, do the following:

1. Click the **user menu** in the top menu bar.
2. From the dropdown menu, select **Profile**.
3. From your user profile, select **Scheduled Exports**.
4. Choose which scheduled exports you want to view and manage:

   * Select **Owned by you** to view and manage scheduled exports created by you. If you're a Sigma admin, you also see schedules inherited from organization members that you deactivated.
   * Select **Your subscriptions** to view and manage exports sent to your email address, whether owned by you or others.

   You can search, filter, and sort the listed schedules to more easily locate the schedule you want to find.

   To make changes to a specific schedule, select the name of the workbook to open the workbook and manage the schedule. See [Manage schedules for a workbook](#manage-schedules-for-a-workbook).

### Delete a schedule

To delete a schedule that you own:

1. Click the **user menu**, then from the dropdown menu, select **Profile**.
2. Select **Scheduled Exports**.
3. Locate the scheduled export that you want to delete, then click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More > Delete**.

### Unsubscribe from a subscription

To unsubscribe from a subscription to a scheduled export:

1. Click the **user menu**, then from the dropdown menu, select **Profile**.
2. Select **Scheduled Exports**.
3. Select **Your subscriptions** and locate the subscription that you want to unsubscribe from.
4. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More > Unsubscribe**.

Updated 3 days ago

---

Related resources

* [Send and schedule exports from workbooks](/docs/send-and-schedule-exports-from-workbooks)
* [Manage Organization Schedules](/docs/manage-organization-schedules)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Manage schedules for a workbook](#manage-schedules-for-a-workbook)
  + - [Edit or delete a schedule](#edit-or-delete-a-schedule)
    - [Send a scheduled export on demand](#send-a-scheduled-export-on-demand)
    - [Pause or resume a scheduled export](#pause-or-resume-a-scheduled-export)
  + [Manage your scheduled exports and subscriptions](#manage-your-scheduled-exports-and-subscriptions)
  + - [View and manage schedules in your profile](#view-and-manage-schedules-in-your-profile)
    - [Delete a schedule](#delete-a-schedule)
    - [Unsubscribe from a subscription](#unsubscribe-from-a-subscription)