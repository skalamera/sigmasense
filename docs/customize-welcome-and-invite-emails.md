# Customize welcome and invite emails

# Customize welcome and invite emails

When you invite a user to join Sigma, they receive an email with a sign up link. Each user receives a welcome email after they create a Sigma account.

With email customization, organization admins can add their own content to two types of emails:

* **Invite emails**: When a user is invited to Sigma through Sigma’s invite modal, the default invite message appears and the user sending the invite has the opportunity to change the invite message from the default.
* **Welcome emails**: Every user who joins Sigma receives a Welcome email with the default message.

Some information that you might add to your default messages includes:

* How your organization is using Sigma
* What data is available in your cloud data warehouse
* Links to internal resources like a data dictionary or getting started guide
* Links to dashboards you think all users should know about
* Information on who to reach out to with questions about Sigma

## Customize default invite emails

1. Open your Admin Portal by selecting **Administration** in the user menu at the top right of your screen.
2. Go to **People** in the left hand panel.
3. Select the **Invitation Customization** tab.
4. For **Invite Email**, click **Customize**.
5. Enter your message.
6. To preview what your message will look like to users, click **Send Preview**. An email is sent to the address associated with your Sigma user.
7. Click **Save** to save your message.

## Customize welcome emails

1. In the Admin Portal, click the **Administration** tab.
2. Go to **People** in the left hand panel.
3. Select the **Invitation Customization** tab.
4. Next to **Welcome Email**, click **Customize**.
5. Enter your message.
6. To preview what your message will look like to users, click **Send Preview**. An email is sent to the address associated with your Sigma user.
7. Click **Save** to save your message.

## Custom SMTP server

Configure a custom SMTP server to send Sigma-generated emails from an email address and SMTP server within your domain. Emails sent from Sigma include scheduled and ad hoc exports, welcome emails, and invitation emails.

Use a custom SMTP server for cases when you want to customize the email sender, remove warnings about emails originating from an external sender, and/or remove the "via Sigma Computing" note on email messages sent from Sigma. You can also customize other branding options, such as the reply-to address and sender name, helping you create a consistent user experience.

> 📘
>
> ### If you configure your own SMTP server, Sigma can't monitor email deliverability, such as send failures or blocked recipients.

Custom SMTP also offers the following benefits:

* **Email deliverability**: The ability to configure your email server settings, which are optimized for your organization's email infrastructure, can improve email deliverability.
* **Improved security:** You control the security of all email data and communications, and consistent branding combined with a trusted sender increases security because end users can more easily identify phishing emails compared to authentic emails.
* **Flexibility:** Increase your flexibility & control over your email infrastructure. You can easily modify your email settings and troubleshoot issues as needed.

### Configure a Custom SMTP Server

Follow the steps below to set up Sigma to use your own SMTP server:

> 📘
>
> ### You must add Sigma's egress IP addresses to your SMTP server and/or firewall allowlist. To view those IP addresses, see [Adding Sigma IPs to the allowlist](/docs/connect-to-data-sources).

1. In the Admin Portal, click the **Exports** tab.
2. On the **Exports** page, click the **Settings** tab.
3. Locate the **Customize your email** section. For **Set your own SMTP server**, click **Edit**.
4. In the **Host** field, enter the hostname or IP address of your SMTP server.
5. [optional] In the **Port** field, change the default port of 587. Do not change this port to 25, because port 25 is not supported by Sigma.
6. In the **Username** field, enter your SMTP username.
7. In the **Password** field, enter the password for your SMTP server.
8. In the **Sender Email** field, specify an email address to use as the sender of the email.

> 🚧
>
> ### Any changes made to the **Sender name**, **Global BCC email addresses**, and **Reply-to email** fields will also affect your custom email branding settings. See [Customize email branding](/docs/custom-email-branding).

9. In the **Sender Name** field, specify a name to display as the sender of the email.
10. In the **Global BCC email addresses** field, enter emails to be included as default BCC recipients on all emails sent from your Sigma organization. If entering multiple emails, these should be comma separated.

> 📘
>
> ### Emails added as global BCC recipients will receive a copy of every email sent from your Sigma organization, including failure and success emails. For example, if an email is addressed to 100 recipients, each BCC recipient will receive 100 copies of the same email, one for each unique recipient. Your email provider may filter these emails for you by default to only show one of these emails.

11. [optional] In the **Reply-to email address** field, specify an email address to receive replies to the email.
12. Click **Send email preview** to send an email to yourself and test your custom SMTP server configuration.

Updated 3 days ago

---

Related resources

* [Customize email branding](/docs/custom-email-branding)

* [Table of Contents](#)
* + [Customize default invite emails](#customize-default-invite-emails)
  + [Customize welcome emails](#customize-welcome-emails)
  + [Custom SMTP server](#custom-smtp-server)
  + - [Configure a Custom SMTP Server](#configure-a-custom-smtp-server)