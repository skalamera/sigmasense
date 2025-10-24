# Export as email burst

# Export as email burst

You can send a custom-filtered report to a dynamic list of recipients as a scheduled email burst. For example, you might send individual sales representatives their individual quarterly performance numbers for all categories of product that they sell. Because each sales rep is only responsible for one region, customize the report to provide relevant region-specific data, and filter the elements on the page with a page control for the store region.

![Workbook page with a header with dynamic text titled Quarterly Sales Performance for null, with empty store region and quarter controls, 2 KPIs for sales volume and total cost, and a bar chart showing sales volume by quarter and product type](https://files.readme.io/3cfe80dab4d5dcb4cf1c3bae65aaaf5daefe7f21a912dcfaee20f6209bdf5a94-export-burst-empty.png)

In this example, the sales rep assigned to the West Store Region would receive this report as an email attachment in her email inbox:

![Workbook page with a header with dynamic text titled Quarterly Sales Performance for Priya Shankar, with store region control with West selected and quarter control, 2 KPIs for sales volume and total cost filtered to show just the West region, and a bar chart showing sales volume by quarter and product type for the West region](https://files.readme.io/95ec44a113cc94f9f8185bb2493197df5872ded827809eb4b7803e5ecef2f381-export-burst-received.png)

Sigma generates exports from the workbook's latest published version. Changes you make to a workbook draft, custom view, or exploration cannot be exported unless you save or publish the changes. Depending on your export destination, you can also choose to export a saved view or tagged version of the workbook. If you are exporting elements that are only on a saved view, you must open the export modal from the saved view.

For a matrix of supported file formats and saved view/version tag export support, see [Available export destinations and formats](/docs/send-or-schedule-workbook-exports#available-export-destinations-and-formats).

## Limitations

When exporting as an email burst, certain limitations apply:

* The control that you split by must be a list control with values sourced from a column. You can split by a maximum of 500 values.
* The split by column must be a number or text data type.
* The source of the dynamic recipients must be a column in the same data source that the list control is sourced from. You can send to a maximum of 500 dynamic recipients.
* The size limit for emailed exports is 30MB. This is the total limit for all attachments when combined. If an export exceeds this limit, the entire export fails and the owner of the scheduled export is notified. Scheduled exports that repeatedly exceed this limit are automatically paused and their owner notified. See [Download, export, and upload limitations](/docs/download-export-and-upload-limitations).
* Email bursts do not support exporting elements that are only in a [saved view](/docs/create-and-share-saved-views).
* Unsubscribing to email bursts with dynamic recipients is not supported.

> 🚧
>
> When executing a scheduled export or direct download to PDF or PNG formats, Sigma may store applicable control values as URL parameters in trace logs used for debugging and troubleshooting purposes. Exercise caution when exporting or downloading workbook content that uses controls to filter sensitive data.

## User requirements

* You must be assigned an account type with the [Export as email burst](/docs/license-and-account-type-overview) permission enabled.

> 📘
>
> If your organization restricts email traffic sent from specific IP addresses, add `198.37.153.185` and `134.128.103.81` to the allowlist. Alternatively, you can configure a custom SMTP server to use instead. See [Custom SMTP server](/docs/customize-welcome-and-invite-emails#custom-smtp-server).

## Schedule an email burst

1. From the workbook menu (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)), select **Share and export> Schedule export...**.
2. If this is the first schedule for the workbook, click **Add schedule**, otherwise click **+ New schedule**.
3. Select **Export as email burst**.
4. For **Split by...**, select a control to use as the split-by value.
5. Choose recipients for the email burst. You can include both dynamic and standard recipients:

   * For **Dynamic recipients**, select a column from the data source used to populate the list control used as split-by values. Dynamic recipients receive only the attachments relevant to the associated split by control value. Leave empty to send all attachments to a static list of recipients. Multiple recipients can be listed per record in the data source column, but they must be comma-separated.
   * For **Standard recipients**, enter one or more comma-separated Sigma teams, Sigma users, or email addresses. Combined with **Dynamic recipients**, you can email up to 1,000 total recipients. Standard recipients receive all attachments.
   > 📘
   >
   > ### If export authentication is configured for your organization by an admin, you can only send the export to email addresses associated with an authorized domain. For **Standard recipients** When you attempt to create the schedule, Sigma notifies you if an email address contains a domain that's not allowed. For **Dynamic recipients**, emails to restricted addresses are not sent. See [Restrict export recipients](/docs/restrict-export-recipients).

   ![Schedule exports modal with email burst selected and the described options visible](https://files.readme.io/56e6d9ab1b095e113cafa19647a477350e0e80db5767ed12cd3ed1e5ba2ffc15-export-burst.png)
6. (Optional) In the **Subject** field, enter a subject line.
7. (Optional) In the **Message** field, enter a message.
8. If the workbook has tagged versions, select a version to send. By default, the published version is sent.
9. In the **Attachments** section, choose what you want to export as an attachment. You can export:

   * An **Entire workbook** and export all workbook pages.
   * A specific workbook page, by navigating to the workbook page and choosing **Entire page**.
   * An element on a specific workbook page, by selecting the workbook page and choosing the name of the element.
10. In the **Frequency** section, set the delivery schedule:

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

    > 📘
    >
    > ### Conditions are evaluated separately for each split by control value, but the number of occurrences is evaluated for the condition overall. For example, if you send an email burst to a dynamic list of recipients once per day if a table has data in it, the email burst is sent once per day to whichever recipients have data in that table. If, later that day, the table has data in it for other recipients, no email burst is sent.
11. (Optional) By default, Sigma includes a link to the workbook in the email body. If you don't want to include a link, deselect the checkbox for **Include link to workbook**.
12. (Optional) Depending on the attachment formats that you select, you can configure more options like combining attachments, sending attachments in a zip file, and more. See [Configure additional options for exports](/docs/configure-additional-options-for-exports).
13. (Optional) Select the checkbox for **Customize control values** to filter the exported data according to the value of one or more workbook controls. See [Configure additional options for exports](/docs/configure-additional-options-for-exports).
14. Click **Create**.

Updated 3 days ago

---

[Export to webhook](/docs/export-to-webhook)[Export to Microsoft Teams](/docs/export-to-microsoft-teams)

* [Table of Contents](#)
* + [Limitations](#limitations)
  + [User requirements](#user-requirements)
  + [Schedule an email burst](#schedule-an-email-burst)