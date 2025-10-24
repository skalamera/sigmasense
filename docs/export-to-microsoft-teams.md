# Export to Microsoft Teams

# Export to Microsoft Teams

To send documents, reports, and data to Microsoft Teams, schedule or set up an export to Microsoft Teams from Sigma. You can export to any public channel in a team.

![Message posted by Sigma notifications bot in Microsoft Teams with the title New Export and text that contains the workbook name, Example, and the element name, Grouped MLB sales, along with a user-provided message that says "These are the top sales from various MLB stadium businesses — please take a look!". Two buttons appear, one with an option to Open File, and another to Open in Sigma.](https://files.readme.io/f1b5cf15dfd239d686f83a85f696e4f4f289dba4ffa03192a33c9092c8a73580-teams-export-border-small.png)

Export an element, a workbook page, or an entire workbook to Microsoft Teams.

Sigma generates exports from the workbook's latest published version. Changes you make to a workbook draft, custom view, or exploration cannot be exported unless you save or publish the changes. Depending on your export destination, you can also choose to export a saved view or tagged version of the workbook. If you are exporting elements that are only on a saved view, you must open the export modal from the saved view.

For a matrix of supported file formats and saved view/version tag export support, see [Available export destinations and formats](/docs/send-or-schedule-workbook-exports#available-export-destinations-and-formats).

This documentation describes how to send and schedule exports to Microsoft Teams.

## User requirements

The ability to export to Microsoft Teams requires the following:

* The [Microsoft integration](/docs/manage-microsoft-integration) must be set up for your organization.
* The Sigma Notifications app [must be added to the first named channel of your team](/docs/manage-microsoft-integration#add-the-sigma-notifications-app-to-teams).

  > 📘
  >
  > The first named channel is the first channel named when creating a team. It might also be called the "General" channel or the home channel, and can be renamed. See [Edit a channel in Microsoft Teams](https://support.microsoft.com/en-us/office/edit-a-channel-in-microsoft-teams-3497a0d0-5cae-44be-8a57-0d75b48da859).
  >
  > To identify the first named channel for a team, navigate to your team in the Teams sidebar, then choose **More Options** > **Manage Team**. The channel with a house icon next to it is the first named channel.
* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Export to Microsoft Teams and SharePoint** permission enabled.

## Export size limit

The size limit for exports to Microsoft Teams is 1GB per file. See [Download, export, and upload limitations](/docs/download-export-and-upload-limitations).

## Prerequisites

You must know the channel URL for the Microsoft Teams channel to which you want to send an export. In Microsoft Teams, open the channel menu and select **Get link to channel**.

## Send an ad hoc notification to a Microsoft Teams channel

To send an ad hoc notification to a Microsoft Teams channel, the Sigma Notifications app must be added to the first named channel of the Team. The channel that you share to must be standard or shared.

Notifications send the shared file as an attachment stored in the SharePoint folder corresponding with the Microsoft Team and channel. Multiple attachments are shared as multiple messages. Each message is from the Sigma Notifications bot and includes **New Export** and the title of the workbook and element being shared.

1. From the workbook menu , select **Share and export> Export...**.
2. Select **Microsoft Teams**.
3. In the **Channel URL** field, enter the URL of the Microsoft Teams channel. For example, `https://teams.microsoft.com/l/channel/<channel-ID-and-name>?groupId=<group-ID>&tenantId=<tenant-ID`

   > 📘
   >
   > ### You cannot send a notification to a private channel.
4. (Optional) Enter a message in the **Message** field. To format your message, see [Format a Microsoft Teams message](/docs/format-a-microsoft-teams-message).
5. If the workbook has versions or saved views, select which one you want to use to send your message.
6. In the **Attachments** section, choose what you want to export as an attachment. You can export:

   * An **Entire workbook** and export all workbook pages.
   * A specific workbook page, by navigating to the workbook page and choosing **Entire page**.
   * An element on a specific workbook page, by navigating to the workbook page and choosing the name of the element.

   Select **+Add** to add more attachments.
7. For each attachment, select a supported file format. For a matrix of supported file formats, see [Available export destinations and formats](/docs/send-or-schedule-workbook-exports#available-export-destinations-and-formats).  
   Each attachment arrives in Microsoft Teams as a separate message, except for combined attachments.
8. (Optional) To include a link to the workbook in the message body, select the checkbox for **Include link to workbook**.  
   Exports to Microsoft Teams capture data accessible to the member who initiated the export. If a user clicks the workbook link, Sigma only displays what that individual user has access to view.
9. (Optional) Depending on the attachment formats that you select, you can configure more options like combining attachments, sending attachments in a zip file, and more, See [Configure additional options for exports](/docs/configure-additional-options-for-exports).
10. Click **Export**.

## Schedule a notification to a Microsoft Teams channel

To send a scheduled notification to a Microsoft Teams channel, the Sigma Notifications app must be added to the first named channel of the Team. The channel that you share to must be standard or shared.

Notifications send the shared file as an attachment stored in the SharePoint site that corresponds to the Microsoft Team. Multiple attachments are shared as multiple messages. Each message is from the Sigma Notifications bot and includes **New Export** and the title of the workbook and element being shared.

1. From the workbook menu , select **Share and export> Schedule exports…**.

   > 📘
   >
   > ### If the Microsoft Teams option is not available, the workbook is in **Edit** mode. Either publish your draft or return to the latest published or a tagged version of the workbook before attempting to export.
2. If this is the first schedule for the workbook, click **Add Schedule**, otherwise click **+New schedule** .
3. Select **Microsoft Teams**.
4. In the **Channel URL** field, enter the URL of the Microsoft Teams channel. For example, `https://teams.microsoft.com/l/channel/<channel-ID-and-name>?groupId=<group-ID>&tenantId=<tenant-ID>`

   > 📘
   >
   > ### You cannot send a notification to a private channel.
5. (Optional) Enter a message in the **Message** field. To format your message, see [Format a Microsoft Teams message](/docs/format-a-microsoft-teams-message).
6. If the workbook has versions or saved views, select which one you want to use to send your message.
7. In the **Attachments** section, choose what you want to export as an attachment. You can export:

   * An **Entire workbook** and export all workbook pages.
   * A specific workbook page, by navigating to the workbook page and choosing **Entire page**.
   * An element on a specific workbook page, by navigating to the workbook page and choosing the name of the element.

   Select **+Add** to add more attachments.
8. For each attachment, select a supported file format. For a matrix of supported file formats, see [Available export destinations and formats](/docs/send-or-schedule-workbook-exports#available-export-destinations-and-formats).  
   Each attachment arrives in Microsoft Teams as a separate message, except for combined attachments.
9. In the **Frequency** section, set the delivery schedule:

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
10. (Optional) To include a link to the workbook in the message body, select the checkbox for **Include link to workbook**.  
    Exports to Microsoft Teams capture data accessible to the member who initiated the export. If a user clicks the workbook link, Sigma only displays what that individual user has access to view.
11. (Optional) Select the checkbox for **Customize control values** to filter the exported data according to the value of one or more workbook controls. See [Configure additional options for exports](/docs/configure-additional-options-for-exports).
12. (Optional) Depending on the attachment formats that you select, you can configure more options like combining attachments, sending attachments in a zip file, and more, See [Configure additional options for exports](/docs/configure-additional-options-for-exports).
13. Click **Create**.

Updated 3 days ago

---

[Export as email burst](/docs/export-as-email-burst)[Format a Microsoft Teams message](/docs/format-a-microsoft-teams-message)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Export size limit](#export-size-limit)
  + [Prerequisites](#prerequisites)
  + [Send an ad hoc notification to a Microsoft Teams channel](#send-an-ad-hoc-notification-to-a-microsoft-teams-channel)
  + [Schedule a notification to a Microsoft Teams channel](#schedule-a-notification-to-a-microsoft-teams-channel)