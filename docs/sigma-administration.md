# Administer Sigma

# Administer Sigma

If you are a Sigma admin, you can configure and customize your Sigma organization in the Administration portal.

To access the Administration portal:

1. Go to **Home** and select the user icon with your initials.
2. Select **Administration**.

## Admin abilities

Users assigned the **Admin** [account type](/docs/user-account-types) can:

* Access and edit all configurations in the Administration portal
* Access and edit all documents in the Sigma organization
* Manage users, teams, and permissions
* Enable optional features such as audit logs and AI features
* Decide whether or not to enable private beta features for their organization or individual users

Other users might have access to specific sections of the Administration portal, depending on the permissions enabled on their assigned account type:

* Permissions in the **Usage dashboard** section grant access to usage dashboards in the **Usage** page.
* **Manage all branding settings** grants access to manage all branding settings, including setting up a custom SMTP server.
* **Manage all workbook themes and fonts** grants access to specific branding functionality, such as setting up workbook themes.
* **Manage plugins** grants access to manage plugins.

## Common administration tasks

Onboard users and configure role-based access management and authentication methods:

* **Manage users and teams**: Onboard new users by [inviting new users](/docs/invite-new-organization-members) and [creating teams](/docs/manage-teams). Simplify management by setting up [team admins](/docs/manage-team-admins).
* **Configure permissions and access**: Customize [account types](/docs/create-and-manage-account-types) and assign them to users. Configure the [permissions enabled for each account type](/docs/license-and-account-type-overview), and understand how account type permissions interact with [document access](/docs/folder-and-document-permissions) and [data permissions](/docs/data-permissions-overview).
* **Set up authentication methods**: Set up [SAML](/docs/single-sign-on-with-saml) or [OAuth](/docs/configure-oauth) authentication methods, or centralize team and user management by configuring [SCIM](/docs/manage-users-and-teams-with-scim).

Set up third-party integrations with Sigma, and manage additional organization settings:

* **Integrate Sigma with third-party tools**: Set up and manage integrations with [external AI providers](/docs/manage-external-ai-integrations) to use AI features, exports using [Slack](/docs/manage-slack-integration), and [dbt](/docs/manage-dbt-integration) to use dbt jobs, metadata, and Semantic Layer.
* **Configure Sigma functionality**: Organization admins can exercise fine-grained control over some of the functionality that users can access. Disable or restrict functionality like [public embeds](/docs/enable-or-disable-public-embeds), [workbook comments](/docs/disable-commenting), [account upgrade requests](/docs/license-upgrade-requests), [CSV uploads](/docs/enable-csv-upload), and others.

Customize your Sigma organization to fit your branding and locale:

* **Customize and configure branding**: Ensure your charts and workbooks align with your company branding. You can [customize fonts](/docs/custom-fonts) and set up [workbook themes](/docs/create-and-manage-workbook-themes) with standardized color palettes. Customize the Sigma experience by adding a [custom homepage](/docs/enable-a-custom-homepage) and configuring [email branding](/docs/custom-email-branding).
* **Localize organization settings**: Provide users in your Sigma organization with content in their preferred language and locale, including timezone, currency, and date format. Set up a [time zone for your account](/docs/account-time-zone) and [set up a locale](/docs/manage-organization-locale) or [translation files](/docs/manage-organization-translation-files) for your organization.

Monitor and audit user activity in Sigma:

* **Monitor Sigma usage**: Understand how users in your organization use different Sigma features by reviewing different [usage dashboards](/docs/usage-overview), such as [scheduled exports](/docs/scheduled-exports-dashboard), [materialization](/docs/manage-materializations), or [document activity](/docs/document-activity-dashboard).
* **Audit activities in Sigma**: If audit logging is [enabled](/docs/enable-audit-logging), review the [audit logs](/docs/access-and-explore-audit-logs) for your organization.

Extend Sigma functionality:

* **Develop and test plugins**: Enable developers in your organization to [register plugins](/docs/register-a-plugin-with-your-sigma-organization).
* **Create custom functions**: Abstract complex calculations into [custom functions](/docs/custom-functions) that you can share with your organization.

Updated 3 days ago

---

[Configure plugins to work with actions](/docs/configure-plugins-to-work-with-actions)[Users and teams](/docs/people)

* [Table of Contents](#)
* + [Admin abilities](#admin-abilities)
  + [Common administration tasks](#common-administration-tasks)