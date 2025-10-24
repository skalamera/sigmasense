# Format a Microsoft Teams message

# Format a Microsoft Teams message

If a Microsoft integration is enabled for your organization, you can send notifications to Teams channels from a Teams export. See [Export to Microsoft Teams](/docs/export-to-microsoft-teams).

This document describes specific syntax you can use to format text and create hyperlinks when sending Teams messages from Sigma.

## System and user requirements

The ability to send Teams messages requires the following:

* The [Microsoft integration](/docs/manage-microsoft-integration) must be enabled for your organization.
* To send notifications to a channel, you must also add Sigma to the channel. See [Add the Sigma Notifications app to Teams](/docs/manage-microsoft-integration#add-the-sigma-notifications-app-to-teams).
* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Export to Microsoft Teams and SharePoint** permission enabled.

## Supported syntax

Microsoft supports specific markup formatting for Teams messages.

When adding text to a message body, you can use the following syntax to format text and create hyperlinks:

| Formatting | Syntax | Details |
| --- | --- | --- |
| Hyperlink text | `[text](URL)` | For example, to hyperlink the Sigma documentation, type `[Sigma Documentation](<https://help.sigmacomputing.com>)` |
| Bold text | `**text**` | Bold the enclosed text (**text**) in your message. |
| Italicize text | `~text~` | Italicize the enclosed text (*text*) in your message. |

Updated 3 days ago

---

[Export to Microsoft Teams](/docs/export-to-microsoft-teams)[Export to Microsoft SharePoint](/docs/export-to-microsoft-sharepoint)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Supported syntax](#supported-syntax)