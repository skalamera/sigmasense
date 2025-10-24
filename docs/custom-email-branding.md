# Customize email branding

# Customize email branding

Custom email branding lets you apply your organization's brand logo, configure email signatures and footers, configure global BCC recipients, and more to all [export emails](/docs/send-a-workbook-export-to-email-recipients) sent from your Sigma organization.

By default, all emails include Sigma branding. However, applying any subset of custom branding options automatically removes all Sigma branding.

This document covers how to configure your email branding settings, considerations if you want to configure global BCC recipients, and how to test your email branding configurations.

## Requirements

* You must be an organization admin to use this feature. See [User account types](/docs/user-account-types).

## Customize your organization's email branding

To configure custom email branding:

Warning callout: Configuring any of the custom branding options below disables unsubscribe options for scheduled emails. All recipients (including BCC recipients) will not be able to unsubscribe from the email series.

1. Go to **Administration** > **Exports** > **Settings**.
2. In the **Customize your email** section, next to **Edit your email branding**, select **Edit**.

> 📘
>
> ### All of the fields below are optional to configure, and any combination of available fields can be used. Applying any subset of custom branding options automatically removes all Sigma branding.

3. Select **Upload Logo** and follow the prompts to add an image. Recommended logo dimensions are at least 135px wide with an aspect ratio between 3:1 to 1:2.

> 🚧
>
> ### Any changes made to the **Sender name**, **Global BCC email addresses**, and **Reply-to email** fields will also affect your custom SMTP server settings if you have an SMTP server configured. See Custom SMTP server in [Customize welcome and invite emails](/docs/customize-welcome-and-invite-emails#custom-smtp-server).

4. In the **Sender name** field, enter your desired “from” name to be displayed in the recipient’s inbox. This will appear as *[Sender name] via Sigma Computing*.
5. In the **Global BCC email addresses** field, enter emails to be included as default BCC recipients on all emails sent from your Sigma organization. If entering multiple emails, these should be comma separated.

> 📘
>
> ### Emails added as global BCC recipients will receive a copy of every email sent from your Sigma organization, including failure and success emails. For example, if an email is addressed to 100 recipients, each BCC recipient will receive 100 copies of the same email, one for each unique recipient. Your email provider may filter these emails for you by default to only show one of these emails.

6. In the **Reply-to email** address field, enter the email address that replies from your email recipients should be sent to.
7. In the **Signature name** field, add your desired signature name. This does not have to match the **Sender name**. This will appear at the of the email as *Yours sincerely, [Signature name]*.
8. In the **Email footer** field, enter your desired email footer.
9. (Optional) Send a preview email to your email address. Locate your email address below the **Edit your email branding** field, then click **Send email preview**. Open your email to review the preview. The subject line for an email preview is: *[Preview] Custom Branding Test Email.*
10. Select **Save**.

## Test your email branding

1. Open your Admin Portal.
2. Select the **Exports** tab.
3. On the **Exports** page, click the **Settings** tab.
4. Locate the **Customize your email** section and review the custom branding in the **Edit your email branding** section.
5. Next to your email address, click **Send email preview**.

   > 📘
   >
   > ### If you don't see an option to send a preview email, no custom email branding is configured.

   Open your email to review the preview. The subject line for an email preview is: *[Preview] Custom Branding Test Email.*

Updated 3 days ago

---

Related resources

* [Customize welcome and invite emails](/docs/customize-welcome-and-invite-emails)
* [Export to email](/docs/export-to-email)
* [Send or schedule workbook exports](/docs/send-or-schedule-workbook-exports)
* [Manage scheduled exports](/docs/manage-scheduled-exports)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Customize your organization's email branding](#customize-your-organizations-email-branding)
  + [Test your email branding](#test-your-email-branding)