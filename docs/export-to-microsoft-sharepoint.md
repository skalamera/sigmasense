# Export to Microsoft SharePoint

# Export to Microsoft SharePoint

To send documents, reports, and data to a Microsoft SharePoint site, schedule or set up an export. When you [export to Microsoft Teams](/docs/export-to-microsoft-teams) , the exported file is also stored in the SharePoint site associated with the Team. You can also send files directly to a SharePoint folder.

Export an element, a workbook page, or an entire workbook to Microsoft SharePoint.

Sigma generates exports from the workbook's latest published version. Changes you make to a workbook draft, custom view, or exploration cannot be exported unless you save or publish the changes. Depending on your export destination, you can also choose to export a saved view or tagged version of the workbook. If you are exporting elements that are only on a saved view, you must open the export modal from the saved view.

For a matrix of supported file formats and saved view/version tag export support, see [Available export destinations and formats](/docs/send-or-schedule-workbook-exports#available-export-destinations-and-formats).

This documentation describes how to send and schedule exports to Microsoft SharePoint.

## User requirements

The ability to export to Microsoft SharePoint requires the following:

* The [Microsoft integration](/docs/manage-microsoft-integration) must be added for your organization.
* One Sigma organization can only connect to one Microsoft organization, but you can share to any SharePoint site within the Microsoft organization.
* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Export to Microsoft Teams and SharePoint** permission enabled.

Any files added from Sigma appear as modified by the SharePoint App.

## Prerequisites

You must know the URL of the SharePoint folder that you want to export to. To copy a link to a SharePoint folder, click **Copy Link** or navigate to **Share> Copy Link**.

You cannot export directly to a document or page library in a Site, but you can export to a folder within a document library.

> 🚩
>
> ### You cannot export to a personal SharePoint folder. Personal SharePoint folder URLs are formatted like: `-my.sharepoint.com`.

## Send to Microsoft SharePoint

To send an ad hoc export to Microsoft SharePoint:

1. From the workbook menu , select **Share and export> Export...**.
2. Select **Microsoft SharePoint**.
3. For **Folder URL**, enter the URL to the SharePoint folder to which to send your exported file(s).
4. In the **Attachments** section, choose what you want to export as an attachment. You can export:

   * An **Entire workbook** and export all workbook pages.
   * A specific workbook page, by navigating to the workbook page and choosing **Entire page**.
   * An element on a specific workbook page, by navigating to the workbook page and choosing the name of the element.

   Select **+Add** to add more attachments.
5. For each attachment, select a supported file format. For a matrix of supported file formats, see [Available export destinations and formats](/docs/send-or-schedule-workbook-exports#available-export-destinations-and-formats).
6. Click **Create**.

## Schedule an export to Microsoft SharePoint

To schedule an export to a Microsoft SharePoint folder:

1. From the workbook menu , select **Share and export> Schedule exports…**.
2. If this is the first schedule for the workbook, click **Add Schedule**, otherwise click **+New schedule** .
3. Select **Microsoft SharePoint**.
4. For **Folder URL**, enter the URL to the SharePoint folder to which to send your exported file(s).
5. In the **Attachments** section, choose what you want to export as an attachment. You can export:

   * An **Entire workbook** and export all workbook pages.
   * A specific workbook page, by navigating to the workbook page and choosing **Entire page**.
   * An element on a specific workbook page, by navigating to the workbook page and choosing the name of the element.

   Select **+Add** to add more attachments.
6. For each attachment, select a supported file format. For a matrix of supported file formats, see [Available export destinations and formats](/docs/send-or-schedule-workbook-exports#available-export-destinations-and-formats).
7. In the **Frequency** section, set the delivery schedule:

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
8. (Optional) Select the checkbox for **Customize control values** to filter the exported data according to the value of one or more workbook controls. See [Configure additional options for exports](/docs/configure-additional-options-for-exports).
9. Click **Create**.

Updated 3 days ago

---

[Format a Microsoft Teams message](/docs/format-a-microsoft-teams-message)[Manage scheduled exports](/docs/manage-exports)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Prerequisites](#prerequisites)
  + [Send to Microsoft SharePoint](#send-to-microsoft-sharepoint)
  + [Schedule an export to Microsoft SharePoint](#schedule-an-export-to-microsoft-sharepoint)