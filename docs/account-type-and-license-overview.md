# Account type and license overview

# Account type and license overview

> 🚩
>
> If your organization utilizes the Lite/Essential/Pro license model, refer to [this account type and license overview](/docs/license-and-account-type-overview-2024).

Account types and licenses are foundational components of Sigma’s user management and pricing structure. Account types enable the selection of granular permissions that determine how users access and interact with data and documents in Sigma. The selected permissions determine the account type’s license tier used for billing purposes.

This document outlines Sigma's license tiers and explains the relationship between account types and licenses. It also provides a comprehensive comparison of permissions that determine which license is assigned to each account type.

For information about using account types, see [Create and manage account types](/docs/create-and-manage-account-types).

> 📘
>
> For information about license pricing, contact your Account Executive or Customer Success Manager.

## License tiers

Sigma offers four license tiers that support different service levels to accommodate your organization’s diverse user requirements and access control policies. The following table describes model users and key capabilities of each license tier.

> 📘
>
> For information about license pricing, contact your Account Executive or Customer Success Manager.

| View | Act | Analyze | Build1 |
| --- | --- | --- | --- |
| Suitable for report consumers who need access to prepared data and insights with baseline interactions.   ---   Highlights   * View workbooks * Use predefined controls and drill paths * View aggregated underlying data * Export workbook pages to PDF and charts to PNG * Add and view comments * Designate workbooks as favorites * Use Ask Sigma to ask natural language queries | Ideal for collaborative data contributors who actively input and update data.   ---   *View* license capabilities, plus:   * Submit forms and edit input tables * Trigger actions * Annotate comments * View and filter underlying data * Explain charts with AI | Optimized for decision-making data consumers who require more deep-dive capabilities without building workbooks themselves.   ---   *Act* license capabilities, plus:   * Perform ad hoc analysis * Schedule reports * Export to CSV, Excel, and Google Sheets * Create alerts * Use AI-powered formula assistant | Designed for data architects, BI analysts, and report builders who model, transform, and analyze data.   ---   *Analyze* license capabilities, plus:   * Create, edit, and share workbooks * Build data apps and workflows with actions * Model share, and materialize data * Export data to cloud services * Manage users, user attributes, and teams * Manage integrations and connections * Write SQL and Python * View Custom SQL logic |

1The Build license also supports system administrators who can manage organization settings and users.

## Account type and license relationship

Account types enable admin users to select granular permissions that determine which features and capabilities organization users can access. Sigma automatically assigns a license to each account type based on the highest license tier of the enabled permissions. This relationship allows for more flexible and scalable access control that adapts to ongoing changes in your user base and user requirements.

## Account type permission availability matrix

> 🚩
>
> ### If your organization utilizes the Lite/Essential/Pro license model, refer to [this account type permission availability matrix](/docs/license-and-account-type-overview-2024#account-type-permission-availability-matrix).

The following table compares the account type permissions associated with each license tier. When configuring an account type, admins can enable or disable any combination of permissions within and across license tiers.

|  | | View | Act | Analyze | Build |
| --- | --- | --- | --- | --- | --- |
| Data warehouse | | | | | |
| Connections | View connections  *Browse connections, schemas, and database tables* | yes | yes | yes | yes |
| Manage connections1  *Create new connections and manage existing ones*  *(Automatically enables the* ***View connections*** *permission)* | no | no | no | yes |
| Tables | Annotate tables1  *Annotate database tables (edit column details, metrics, and links)* | no | no | no | yes |
| Stored procedures | Create stored procedure actions  *Allow users to create stored procedure actions*  *(Automatically enables the* ***Call stored procedure actions*** *permission)* | no | no | no | yes |
| Call stored procedure actions  *Allow users to call stored procedure actions* | no | yes | yes | yes |
| Write-back | | | | | |
| Input tables | Create input tables2  *Create and edit input tables in workbooks* | no | no | no | yes |
| Materialization | Schedule materializations2  *Create and edit materialization schedules* | no | no | no | yes |
| CSV | Upload CSV  *Upload and analyze CSV data* | no | no | no | yes |
| Warehouse views | Create warehouse views2  *Create warehouse views based on datasets and workbook elements* | no | no | no | yes |
| Data modeling | | | | | |
| Datasets | View datasets2  *View existing datasets and data models* | yes | yes | yes | yes |
| Create, edit, and publish datasets2  *Create and manage datasets and data models*  *(Automatically enables the **View datasets** permission)* | no | no | no | yes |
| Features | Write Python  *Write Python code to run in your data platform* | no | no | no | yes |
| Write SQL  *Query a connected data platform directly with SQL* | no | no | no | yes |
| Documents | | | | | |
| Workbooks | View workbooks2  *View and interact with explorations and published workbooks* | yes | yes | yes | yes |
| Can comment on workbooks4  *View and add comments on workbooks* | yes | yes | yes | yes |
| Basic explore2,3  *View and interact with explorations and published workbooks with added ability to drill into data, filter columns, enter input table data, and more*  *(Automatically enables the* ***View workbooks*** *permission)* | no | yes | yes | yes |
| Full explore2,3  *Modify workbook elements to create custom views of published workbooks, configure actions, and more*  *(Automatically enables the* ***Basic explore*** *and* ***View workbooks*** *permissions)* | no | no | yes | yes |
| Create, edit, and publish workbooks2  *Create new workbooks, manage existing workbooks, and share custom views of published workbooks*  *(Automatically enables the* ***Full explore****,* ***Basic explore****, and* ***View workbooks*** *permissions)* | no | no | no | yes |
| Set workbook data refresh2  *Set an automatic data refresh schedule for a workbook*  *(Automatically enables the* ***Create, edit, and publish workbooks*** permission) | no | no | no | yes |
| Version tags | Apply tag2  *Apply version tags to workbooks or data models* | no | no | no | yes |
| Org management | | | | | |
| Users and teams | Manage users  *Invite new users, delete users, and assign account types*  *Cannot assign or reassign admins, or any account type with Manage users, Manage teams, Manage user attributes, Manage export integrations, or Manage connections* | no | no | no | yes |
| Manage user attributes  *Create, edit, and assign user attributes* | no | no | no | yes |
| Manage teams  *Create, edit, and delete teams. Assign users to teams* | no | no | no | yes |
| Usage dashboard | View usage dashboard  *View the organization dashboard* | no | no | no | yes |
| View SQL in usage dashboard  *View raw SQL in the organization usage dashboard*  *(Automatically enables the* *View usage dashboard* *permission)* | no | no | no | yes |
| Branding settings | Manage email branding  *Manage organization branding settings for system emails* | no | no | no | yes |
| Manage all workbook themes and fonts  *Create, edit, and delete workbook themes and custom fonts* | no | no | no | yes |
| Plugins | Manage plugins  *Access plugin development features and manage custom plugins* | no | no | no | yes |
| Badges | Manage all badges  *Add, change, and remove workbook badges (Endorsed, Warning, or Deprecated)* | no | no | no | yes |
| Export integrations | Manage export integrations  *Can configure export integrations to Slack channels, Microsoft Teams channels and SharePoint folders* | no | no | no | yes |
| Sharing / folders | | | | | |
| Sharing and exports | Download2  *Immediately download entire workbooks, specific pages, and individual elements* | no | no | yes | yes |
| Export to email2  *Export entire workbooks, specific pages, and individual elements by email*  *(Automatically enables the **Download** permission)* | no | no | yes | yes |
| Run exports as recipient2  *Choose to run exports as the recipients.*  *(Automatically enables the **Download** and **Export to Email** permissions)* | no | no | yes | yes |
| Export to Google Sheet2  *Export data to Google Sheets spreadsheets*  *(Automatically enables the **Download** permission)* | no | no | yes | yes |
| Export to Google Drive2  *Export data to Google Drive folders*  *(Automatically enables the **Download** permission)* | no | no | yes | yes |
| Export to Slack2  *Export data to Slack channels.*  *(Automatically enables the **Download** permission)* | no | no | yes | yes |
| Export to Microsoft Teams and SharePoint2  *Export data to Microsoft Teams channels and SharePoint folders.*  *(Automatically enables the **Download** permission)* | no | no | yes | yes |
| Schedule export2  *Create, edit, and delete scheduled exports and alerts to send entire workbooks, specific pages, and individual elements*  *(Automatically enables the **Download** and **Export to Email** permissions)* | no | no | yes | yes |
| Share documents2  *Share folders and documents with organization members* | no | no | no | yes |
| Export to cloud2  *Export data to Google Cloud Storage (GCS) or Amazon S3*  *(Automatically enables the **Download** permission)* | no | no | no | yes |
| Export to webhook2  *Export data to webhook endpoints*  *(Automatically enables the **Download** permission)* | no | no | no | yes |
| Export as email burst  *Export data as email bursts to send different reports for each email recipient.*  *(Automatically enables the **Download** and **Export to Email** permissions)* | no | no | no | yes |
| Folders | Create new folders2  *Create new personal, workspace, and shared folders* | no | no | no | yes |
| Contribute to shared folders2  *Create new documents in workspaces and shared folders* | no | no | no | yes |
| Create new workspace  *Create new organization workspaces*  *(Automatically enables the* ***Contribute to shared folders*** *and* ***Share documents*** *permissions)* | no | no | no | yes |
| AI | | | | | |
| AI features |
| Explain charts with AI5  *Use AI to instantly generate a description of any chart.* | no | yes | yes | yes |
| Use AI with formulas5  *Use the formula assistant to write new formulas, correct formula errors, and explain existing formulas.* | no | no | yes | yes |
| Use Ask Sigma5  *Access and use Ask Sigma to ask natural language queries* | yes | yes | yes | yes |

1Access to individual connections is determined by [data access](/docs/data-permissions-overview).

2Access to individual datasets, data models, and workbooks is determined by [folder and document permissions](/docs/folder-and-document-permissions).

3For a comprehensive comparison of user capabilities, see [Basic explore vs. Full explore](/docs/basic-explore-vs-full-explore).

4Enables the ability to add and view comments for all license tiers. Also enables screenshot capture and annotation in comments for Analyze and Build licenses only.

5AI features such as Ask Sigma, explain charts with AI, and the AI-powered formula assistant require an AI provider to be configured for the organization. See [Configure an AI provider](/docs/configure-ai-features-for-your-organization#configure-an-ai-provider).

Updated 3 days ago

---

[Manage workspaces](/docs/manage-workspaces)[Create and manage account types](/docs/create-and-manage-account-types)

* [Table of Contents](#)
* + [License tiers](#license-tiers)
  + [Account type and license relationship](#account-type-and-license-relationship)
  + [Account type permission availability matrix](#account-type-permission-availability-matrix)