# Export to Slack

# Export to Slack

If Slack notifications are enabled for your organization, workbooks, their pages, and individual elements can be sent to any channel in your Slack account on a set schedule or as-needed basis.

For example, you might want to provide a weekly uptime report to your management team, but your team communicates primarily in Slack. You can set up an export to a Slack channel or a specific user to make sure your management sees the report.

You can set multiple export schedules for a workbook. Slack exports capture data accessible to the user who initiated the export.

Sigma generates exports from the workbook's latest published version. Changes you make to a workbook draft, custom view, or exploration cannot be exported unless you save or publish the changes. Depending on your export destination, you can also choose to export a saved view or tagged version of the workbook. If you are exporting elements that are only on a saved view, you must open the export modal from the saved view.

For a matrix of supported file formats and saved view/version tag export support, see [Available export destinations and formats](/docs/send-or-schedule-workbook-exports#available-export-destinations-and-formats).

This documentation describes how to send and schedule exports to Slack.

## User requirements

The ability to export to Slack requires the following:

* The [Slack integration](/docs/manage-slack-integration) must be enabled for your organization. If you want to send notifications to a private channel, you must also add Sigma to the private channel. See [Adding Sigma to a private Slack channel](/docs/manage-slack-integration#adding-sigma-to-a-private-slack-channel). One Sigma organization can only connect to one Slack workspace.
* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Export to Slack** permission enabled.

## Export size limit

The size limit for exports to Slack is 1GB per file. See [Download, export, and upload limitations](/docs/download-export-and-upload-limitations).

## Send an ad hoc notification

To export information from a workbook to Slack:

1. From the workbook menu (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)), select **Share and export> Export...**.

   > 📘
   >
   > ### If the Slack option is not available, the workbook is in **Edit** mode. Either publish your draft or return to the latest published or tagged version of the workbook before attempting to export.
2. Select **Slack**.
3. In the **To** field, enter the name of the Slack channel, for example, `#team-channel`. Alternatively, type the channel ID, for example, `A123BC4DE5F`.

   If you want to send the notification to a private channel, you must first add the Sigma notifications bot to the channel. Enter `@Sigma` in your private channel to enable it. See [Adding Sigma to a private Slack channel](/docs/manage-slack-integration#adding-sigma-to-a-private-slack-channel).
4. (Optional) Enter a message in the **Message** field. Slack supports specific formatting markup, that can be used to style text and tag users and channels. See [Format a Slack message](/docs/format-a-slack-message).
5. If the workbook has versions or bookmarks, select which one you want to send.
6. In the **Attachments** section, choose what you want to export as an attachment. You can export:

   * An **Entire workbook** and export all workbook pages.
   * A specific workbook page, by navigating to the workbook page and choosing **Entire page**.
   * An element on a specific workbook page, by navigating to the workbook page and choosing the name of the element.

   Select **+ Add** to add more attachments.
7. For each attachment, select a supported file format. For a matrix of supported file formats, see [Available export destinations and formats](/docs/send-or-schedule-workbook-exports#available-export-destinations-and-formats).

   Each attachment arrives in Slack as a separate message, except for combined attachments.
8. (Optional) To include a link to the workbook in the message body, select the checkbox for **Include link to workbook**.  
   Exports to Slack capture data accessible to the member who initiated the export. If a user clicks the workbook link, Sigma only displays what that individual user has permission to view.
9. (Optional) Depending on the attachment formats that you select, you can configure more options like combining attachments, sending attachments in a zip file, and more, See [Configure additional options for exports](/docs/configure-additional-options-for-exports).
10. Click **Export**.

## Schedule a Slack notification

Sigma generates exports from the workbook's latest published version. Draft changes are not sent unless they are published.

To schedule an export to Slack notification:

1. From the workbook menu (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)), select **Share and export> Schedule exports…**..
2. If this is the first schedule for the workbook, click **Add schedule**, otherwise click **+ New schedule**.
3. Select **Slack**.  
   ![](https://files.readme.io/5edc5dedb3e6b87f5915476839fea49deab90ed4d441175c41b3b11176719756-export-slack.png)
4. In the **To** field, enter the name of the Slack channel, for example, `#team-channel`. Alternatively, type the channel ID, for example, `A123BC4DE5F`.

   If you want to send the notification to a private channel, you must first add the Sigma notifications bot to the channel. Enter `@Sigma` in your private channel to enable it. See [Adding Sigma to a private Slack channel](/docs/manage-slack-integration#adding-sigma-to-a-private-slack-channel).
5. (Optional) Enter a message in the **Message** field. Slack supports specific formatting markup, that can be used to style text and tag users and channels. See [Format a Slack message](/docs/format-a-slack-message).
6. In the **Attachments** section, choose what you want to export as an attachment. You can export:

   * An **Entire workbook** and export all workbook pages.
   * A specific workbook page, by navigating to the workbook page and choosing **Entire page**.
   * An element on a specific workbook page, by navigating to the workbook page and choosing the name of the element.

   Select **+ Add** to add more attachments.
7. For each attachment, select a supported file format. For a matrix of supported file formats, see [Available export destinations and formats](/docs/send-or-schedule-workbook-exports#available-export-destinations-and-formats).

   Each attachment arrives in Slack as a separate message, except for combined attachments.

   > 🚧
   >
   > When executing a scheduled export or direct download to PDF or PNG formats, Sigma may store applicable control values as URL parameters in trace logs used for debugging and troubleshooting purposes. Exercise caution when exporting or downloading workbook content that uses controls to filter sensitive data.
8. In the **Frequency** section, set the delivery schedule:

   * (Optional) Select the dropdown for **Daily** and select **Weekly**, **Monthly**, or **Custom**.

     + For **Daily**, select **Once a day** or **Multiple times**.
     + For **Weekly**, select which days of the week to send an email, and choose between **Once a day** or **Multiple times**.
     + For **Monthly**, select which day of the month to send an email, and the time of day.
     + For **Custom**, specify a schedule using cron syntax. See [Set up a custom delivery schedule](/docs/configure-additional-options-for-exports#set-up-a-custom-delivery-schedule).

       If you select **Multiple times**, specify the frequency. For example, every 2 hours on the :15 of the hour between 9 AM and 6 PM.

       > 📘
       >
       > If you don't have the option to set a specific frequency, export frequency might be restricted for your organization. For more details, see [Restrict export recipients and frequency](/docs/restrict-export-recipients).
   * (Optional) Adjust the default schedule time zone using the dropdown menu.
   * (Optional) Choose how often to send the export: **Always** or only **If a condition is met**. See [Schedule a conditional export or alert](/docs/schedule-a-conditional-export-or-alert).

     + (Optional) If you choose to send an export only **If a condition is met**, you can turn on the switch to stop notifying after a set number of occurrences per day, week, or in total. (This feature is in beta and subject to the [Beta features notice](/docs/sigma-product-releases#beta-features)).
9. (Optional) To include a link to the workbook in the message body, select the checkbox for **Include link to workbook**.  
   Exports to Slack capture data accessible to the member who initiated the export. However, if a user clicks the workbook link, Sigma only displays what that individual user has permission to view.
10. (Optional) Select the checkbox for **Customize control values** to filter the exported data according to the value of one or more workbook controls. See [Configure additional options for exports](/docs/configure-additional-options-for-exports).
11. (Optional) Depending on the attachment formats that you select, you can configure more options like combining attachments, sending attachments in a zip file, and more, See [Configure additional options for exports](/docs/configure-additional-options-for-exports).
12. Click **Create**.

Updated 3 days ago

---

Related resources

* [Integration for Slack](/docs/integration-for-slack)
* [Send and schedule exports from workbooks](/docs/send-and-schedule-exports-from-workbooks)
* [Schedule exports using conditions](/docs/schedule-exports-using-conditions)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Export size limit](#export-size-limit)
  + [Send an ad hoc notification](#send-an-ad-hoc-notification)
  + [Schedule a Slack notification](#schedule-a-slack-notification)