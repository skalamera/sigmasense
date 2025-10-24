# Manage export frequency and authentication settings

# Manage export frequency and authentication settings

As an admin of a Sigma organization, you can configure export settings for users in your organization.

You can manage the following settings:

* Restrict the frequency of scheduled exports.
* Define authorized domains that can receive emails, Google Sheets, and Google Drive exports.
* Restrict email recipients so that users can only email exports to other members of their Sigma teams.
* Require all email exports to run queries as recipient.

If no domains are authorized, or the teams restriction is disabled, users can export reports to any recipients.

## Requirements

* Only users assigned the [Admin](/docs/user-account-types) account type can configure export settings.

## Restrict scheduled export frequency

To restrict the frequency options available to users when scheduling exports, do the following:

1. Open the Administration portal.
2. Go to **Exports**, then select the **Settings** tab.
3. For **Export frequency**, click **Edit**.
4. Turn on the **Restrict export frequency** switch, then configure the frequencies to restrict. For example:

   * Choose to restrict daily exports to multiple times per day, every 30 minutes. This option prevents users from scheduling an export that runs more than once every 30 minutes per day.
   * Choose to restrict daily exports to multiple times per day, every 8 hours. This option prevents users from scheduling an export that runs more than once every 8 hours per day.
   * Choose to restrict daily exports to once per day. This option prevents users from scheduling an export that runs more than once per day.
   > 📘
   >
   > ### When this option is enabled, users cannot configure custom cron schedules.
5. Click **Save**.

> 📘
>
> ### Existing export schedules are unaffected by this restriction. Select the **Scheduled exports** tab to review existing export schedules in your organization that might be occurring more frequently than wanted. See [Manage organization schedules](/docs/manage-organization-schedules).

## Restrict export domains

To restrict the recipients of exports to only users and email addresses from authorized domains:

1. Open the Administration portal.
2. Go to **Exports**, then select the **Settings** tab.
3. Review the **Export authentication** section for the current state:

   * **Authorized Domains: None** means that users in your organization can export reports to any email address.
   * If any domains are listed for **Authorized domains**, users in your organization are limited to emailing only addresses for the listed domains.
4. To add new or modify existing domains, click **Edit**.
5. Enter one or more authorized domains, separating values with a comma.
6. Click **Save**.

## Restrict recipients to team members

To restrict the recipients of exports to only users on the same team as the user sending or scheduling the export:

1. Open the Administration portal.
2. Go to **Exports**, then select the **Settings** tab.
3. In the **Export authentication** section, click **Edit**.
4. To restrict recipients, turn on the **Restrict recipient list to members on same team** switch.
5. Click **Save**.

## Require run as recipient for all email exports

To increase data security for your email exports, you can require all email exports to run queries as recipient. When an export is run as recipient, each query runs separately per recipient. Larger recipient lists result in more queries sent to the database and longer processing times.

After you turn on this setting, all email schedules created or edited require queries to run as recipient. Scheduled exports created before this setting was turned on are **not affected** and do not force running queries as recipient.

> 🚩
>
> ### This setting requires that any affected schedule is sent to 300 or fewer recipients, and all of the recipients are Sigma users. If not all recipients are Sigma users, the email fails to send and the sender of the export receives a failure notification email with the error message: "No users found in organization for the provided email recipients".

To require all email exports to run queries as the email recipient:

1. Open the Administration portal.
2. Go to **Exports**, then select the **Settings** tab.
3. In the **Export authentication** section, click **Edit**.
4. Turn on the **Require run as recipient for all email exports** switch.
5. Click **Save**.

Updated 3 days ago

---

Related resources

* [Send and schedule exports from workbooks](/docs/send-and-schedule-exports-from-workbooks)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Restrict scheduled export frequency](#restrict-scheduled-export-frequency)
  + [Restrict export domains](#restrict-export-domains)
  + [Restrict recipients to team members](#restrict-recipients-to-team-members)
  + [Require run as recipient for all email exports](#require-run-as-recipient-for-all-email-exports)