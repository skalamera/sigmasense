# Format a Slack message

# Format a Slack message

If a [Slack integration](/docs/manage-slack-integration) is enabled for your organization, you can send notifications to Slack users from a Slack export or Slack notification action. See [Send notifications by Slack](/docs/create-actions-that-download-and-export-data#send-notifications-by-slack) and [Export to Slack](/docs/export-to-slack).

This document describes specific syntax you can use to format text, create hyperlinks, and tag users when sending Slack notifications from Sigma.

## System and user requirements

The ability to send Slack notifications requires the following:

* The [Slack integration](/docs/manage-slack-integration) must be enabled for your organization. If you want to send notifications to a private channel, you must also add Sigma to the private channel. See [Adding Sigma to a private Slack channel](/docs/manage-slack-integration#adding-sigma-to-a-private-slack-channel) . Only one Sigma organization can connect to one Slack workspace.
* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Export to Slack** permission enabled.

## Supported syntax

Slack supports specific markup formatting for Slack notifications.

When adding text to a message body, you can use the following syntax to format text, create hyperlinks, and tag users and groups:

| Formatting | Syntax | Details |
| --- | --- | --- |
| Notify a user | `<@user_id>` | Get the Slack member ID for the user from their Slack user profile. See [Find Slack User ID](#find-slack-user-id). |
| Notify a channel | `@here` or `@channel` | See [Notify a channel or workspace](https://slack.com/help/articles/202009646-Notify-a-channel-or-workspace) in the Slack Help Center. |
| Hyperlink text | `<URL|text>` | For example, to hyperlink the Sigma documentation, type `<https://help.sigmacomputing.com|Sigma Documentation>` |
| Bold text | `*text*` | Bold the enclosed text (**text**) in your message. |
| Strike through text | `~text~` | Strike through the enclosed text (~~text~~) in your message. |
| Format text as code | ``text`` | Format the enclosed text (`text`) as code in your message. |
| Reference a group | `<!subteam^groupID>` | See the Slack documentation on [Browse people and user groups in Slack](https://slack.com/help/articles/360003534892-Browse-people-and-user-groups-in-Slack). |

See [Format your messages](https://slack.com/help/articles/202288908-Format-your-messages) in the Slack Help Center for additional reference. Sigma does not support all Slack markup.

## Find Slack user and channel ID

When sending Slack notifications, you can identify Slack users and channels in the **To** field by ID. To find the ID values for a user or channel, see the sections below.

### Find Slack user ID

1. In Slack, navigate to your conversation with the user.
2. From the top right, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More actions**
3. Select **View full profile**.

   ![A user in Slack hovers their mouse over an option that reads 'View full profile' inside a dropdown menu.](https://files.readme.io/417109527f579a61064faa005728527f98c1ce13c4aab299fbf6f0ce259a3314-View_full_profile.png)
4. Select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) and then **Copy member ID**.

   ![The more actions menu open with the Copy member ID option highlighted.](https://files.readme.io/afb13675310ad1c7c4961d1309e217a2b1a27a782eda09d6a2003eddbbd575eb-Copy_Member_ID_Slack_Actions.png)

### Find Slack channel ID

To send Slack messages to a private channel, you must first add Sigma to the channel. See [Adding Sigma to a private Slack channel](/docs/manage-slack-integration#adding-sigma-to-a-private-slack-channel) .

1. In Slack, navigate to the channel.
2. From the top right, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More actions**.
3. Select **Open channel details**.

   ![The more actions menu open with Open channel details highlighted in the list of menu options.](https://files.readme.io/49885cabaea3966e17b22f7cef3265d6786266a1551a1442c876e68f7da605bc-Open_Channel_Details_Slack_Action.png)
4. At the bottom of the modal, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/copy.svg) to copy the channel ID.

   ![At the bottom of the modal, below Leave channel, select the copy button next to the channel ID.](https://files.readme.io/6eb5f4f633fd6eaea6938e0793d759a0259b5c7829453b25394bb039845c3b4f-Copy_Channel_ID_Slack_Actio.png)

Updated 3 days ago

---

[Export to Slack](/docs/export-to-slack)[Export to Google Sheets](/docs/export-to-google-sheets)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Supported syntax](#supported-syntax)
  + [Find Slack user and channel ID](#find-slack-user-and-channel-id)
  + - [Find Slack user ID](#find-slack-user-id)
    - [Find Slack channel ID](#find-slack-channel-id)