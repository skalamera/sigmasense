# Manage Microsoft integration

# Manage Microsoft integration

To allow users in your organization to [export to Microsoft Teams](/docs/export-to-microsoft-teams) and [Microsoft SharePoint](/docs/export-to-microsoft-sharepoint), set up the integration with Microsoft.

> 💡
>
> ### When you export a file to a team in Microsoft Teams, the file is stored in the SharePoint site associated with the team.

## Requirements

* You must be assigned the Admin account type.
* In your Microsoft organization, you must have at least the [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference) role assigned to your user to add the Microsoft integration.

## Integrate with Microsoft

To export to Microsoft Teams and SharePoint, add the integration with your Microsoft organization. Your Sigma organization can only be connected to one Microsoft organization.

1. Open the Admin portal and go to **Accounts**.
2. On the **General settings** tab, locate the **Integrations** section.
3. Next to **Microsoft**, click **Add**.
4. A new browser tab opens, prompting you to sign in to Microsoft.
5. Sign in, then review the requested permissions.
6. Click **Accept**.

   After the integration is set up, the **Add** button for the Microsoft integration changes to **Remove**.

After you integrate with Microsoft, you can export to Microsoft SharePoint. To export to Microsoft Teams, add the Sigma Notifications app to your team.

## Add the Sigma Notifications app to Teams

Before exporting to a Teams channel, add the [Sigma Notifications](https://appsource.microsoft.com/en-us/product/office/wa200008489?tab=overview) Teams app to the first named channel of the team.

> 📘
>
> The first named channel is the first channel named when creating a team. It might also be called the "General" channel or the home channel, and can be renamed. See [Edit a channel in Microsoft Teams](https://support.microsoft.com/en-us/office/edit-a-channel-in-microsoft-teams-3497a0d0-5cae-44be-8a57-0d75b48da859).
>
> To identify the first named channel for a team, navigate to your team in the Teams sidebar, then choose **More Options** > **Manage Team**. The channel with a house icon next to it is the first named channel.

To add the Sigma Notifications app to the first named channel:

1. From the left sidebar of Microsoft Teams, click **Apps**, then search for **Sigma Notifications**.
2. For the **Sigma Notifications** Teams app, click **Add**.
3. When prompted to add the app to a channel, search for and choose the first named channel for your team, then click **Go**.

   The app is added to the channel. If the app is new to the channel, it posts a welcome message.

You are now ready to export to all public (standard or shared) channels in the same team as the first-named channel.

> 🚩
>
> ### If you add the **Sigma Notifications** app to a channel that was not the first named channel, exports to any channels in the team fail to send. Remove the app from the team, then add the app to the first named channel.

Updated 3 days ago

---

[Manage Slack integration](/docs/manage-slack-integration)[Organization settings](/docs/organization-settings)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Integrate with Microsoft](#integrate-with-microsoft)
  + [Add the Sigma Notifications app to Teams](#add-the-sigma-notifications-app-to-teams)