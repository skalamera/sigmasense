# Manage Slack integration

# Manage Slack integration

# Integration for Slack

Sigma's Integration for Slack enables the members of your organization to send and schedule Sigma notifications for any channel in your connected Slack account. It also enables workbooks actions that notify users and export data to Slack.

## System and user requirements

To add the Slack integration in Sigma, you must be assigned the **Admin** [account type](/docs/create-and-manage-account-types).

To add a Slack integration, your Sigma organization cannot already be integrated with a Slack workspace. One Sigma organization can only connect to one Slack workspace.

## Enable Slack notifications

1. Open your Admin Portal by selecting **Administration** in the user menu at the top right of your screen.
2. On the **Account** page, navigate to General Settings and find the **Integrations** section.
3. At the right of the Integration for Slack entry, click **Add**.

   ![The Sigma admin panel. A box and mouse cursor indicate the user selecting the Add button to add a Slack integration.](https://files.readme.io/40b8f93e2ca3390ee3f6c138ea7bbd79c95e994180a0e7a2afecb678e2187c87-slack_Integration_update_copy.png)
4. The process redirects you to Slack, to authorize the integration.
5. Click **Allow** to complete the integration.
6. To test the integration, try [sending or scheduling a notification](/docs/export-to-slack).

## Access and permissions

When you send or schedules a notification in Sigma, you can choose to include a link to the worksheet or dashboard in Sigma. Anyone who sees the notification in Slack must have a Sigma account with [access granted](/docs/data-permissions) to view it with full details inside Sigma.

## Activating Slack for users

After you enable an integration with Sigma, you can open a new channel from Slack.

Follow these steps.

1. Navigate to the [Sigma](https://sigmacomputing.slack.com/apps/AD36UV1PG) option in the Slack app directory.
2. Click **Open in Slack**.

   ![](https://files.readme.io/981e523-2.png)
3. The process redirects you to Sigma.

   You may have to authorize access, and choose the version of Slack you plan to use.
4. The direct Sigma channel now appears in your organization's Slack interface.

   ![](https://files.readme.io/601095a-3.png)

### Adding Sigma to a private Slack channel

To add Sigma notifications to a private Slack channel, follow these steps:

1. In the channel where you plan to add Sigma, start typing *@sigma*.

   The system finds the match, Sigma app. Note that it is not in channel at this time.

   ![](https://files.readme.io/33a36aa-4.png)
2. Select the Sigma app.
3. The Slackbot dialog prompts you to add Sigma to the channel.

   Click **Invite Them**.

   ![](https://files.readme.io/21c74eb-5.png)
4. The system confirms that the Sigma app is now in the private channel.

   ![](https://files.readme.io/76e4f0a-6.png)

Updated 3 days ago

---

Related resources

* [Send and schedule exports from workbooks](/docs/send-and-schedule-exports-from-workbooks)
* [Sigma's privacy policy](https://www.sigmacomputing.com/privacy-policy?_gl=1*c6wulf*_ga*ODkzMjkyNDY1LjE3MDAwMDU1NzM.*_ga_PMMQG4DCHC*MTcwMTI4Njk4NC4yNi4xLjE3MDEyODg0OTQuNDUuMC4w)
* [Understand app permissions](https://slack.com/help/articles/115003461503-Understand-app-permissions-)

* [Table of Contents](#)
* + [Integration for Slack](#integration-for-slack)
  + - [System and user requirements](#system-and-user-requirements)
    - [Enable Slack notifications](#enable-slack-notifications)
    - [Access and permissions](#access-and-permissions)
    - [Activating Slack for users](#activating-slack-for-users)