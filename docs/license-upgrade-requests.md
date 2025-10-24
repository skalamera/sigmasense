# Enable or disable account upgrade requests

# Enable or disable account upgrade requests

Sigma lets users request an account upgrade to gain access to features and capabilities that their current user account type doesn't permit. For example, users can request to be reassigned to an account type that allows them to create or explore workbooks.

If you don't want users to be able to request account upgrades, an admin can disable this functionality.

## User requirements

To disable the ability for users in your organization to request an account upgrade, you must be assigned the **Admin** account type.

## About upgrade requests

Users can submit upgrade requests when trying to perform specific actions in Sigma. After submitting an upgrade request, a user cannot submit a new request unless the previous request has been denied.

### Users without permission to create workbooks

When a user without permission to create workbooks clicks **Create New** on the **Home** page, they see a message that the ability to create workbooks requires an account upgrade.

The user can send an upgrade request to organization admins, who can then reassign the user to an account type with **Create, edit, and publish workbooks** permission.

![Upgrade request prompted from the create new option, with a prompt to tell admins why you are requesting an account upgrade and a button to send request.](https://files.readme.io/ed1a63b9bbb59277ff1a255404b4ccab66d289f654171261805cef30b394d01a-create-upgrade-request.png)

### Users without permission to explore workbooks

When a user doesn't have permission to explore workbooks, Sigma displays a **Request explore access** button in workbook header. The user can click this button to learn about **Explore** access and send a upgrade request to organization admins, who can reassign the user to an account type with **Basic Explore** or **Full Explore** permissions.

![Workbook header displaying "Request explore access" in place of the usual "Edit" option.](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/Account/Enable+or+disable+account+upgrade+request/account-upgrade-request_explore-access.png)

## Enable or disable upgrade requests

To enable or disable the ability for users to request account upgrades, do the following:

1. Go to **Administration > Account > General Settings**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Account**, then open the **General Settings** tab
2. In the **Features** section, locate the **License upgrade request** setting.
3. Toggle the switch to the "on" position to enable the feature (default), or toggle the switch to the "off" position to disable it.

![Admin portal general settings, with the toggle switch for license upgrade request selected to the on position.](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/Account/Enable+or+disable+account+upgrade+request/admin_license-upgrade-request.png)

If upgrade requests are enabled, as an admin, you receive an email and can respond to upgrade requests in Sigma. See [Respond to account upgrade requests](/docs/respond-to-account-upgrade-requests).

Updated 3 days ago

---

Related resources

* [Use a workbook in Explore mode](/docs/use-a-workbook-in-explore-mode)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [About upgrade requests](#about-upgrade-requests)
  + - [Users without permission to create workbooks](#users-without-permission-to-create-workbooks)
    - [Users without permission to explore workbooks](#users-without-permission-to-explore-workbooks)
  + [Enable or disable upgrade requests](#enable-or-disable-upgrade-requests)