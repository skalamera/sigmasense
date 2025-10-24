# Account type and license overview (Lite/Essential/Pro)

# Account type and license overview (Lite/Essential/Pro)

> 🚩
>
> ### If your organization utilizes the View/Act/Analyze/Build license model, refer to [this account type and license overview](/docs/license-and-account-type-overview).

Account types and licenses are foundational components of Sigma’s user management and pricing structure. Account types enable the selection of granular permissions that determine how users access and interact with data and documents in Sigma. The selected permissions determine the account type’s license tier used for billing purposes.

This document outlines Sigma's license tiers and explains the relationship between account types and licenses. It also provides a comprehensive comparison of permissions that determine which license is assigned to each account type.

For information about using account types, see [Create and manage account types](/docs/create-and-manage-account-types-2024). For information about license pricing, contact your Account Executive or Customer Success Manager.

## License tiers

Sigma offers three license tiers that support different service levels to accommodate your organization’s diverse user requirements and access control policies. The following table describes model users and key capabilities of each license tier.

## License tiers

The three license tiers provide different levels of service to accommodate your organization’s diverse user requirements and access control policies.

### Lite license

The Lite license is suitable for report consumers who require access to prepared data and insights. This license tier allows members to view shared datasets, explorations, and workbooks. Lite-licensed members also have access to baseline interactions in explorations and workbooks, including the ability to update control values, sort column data, view aggregated underlying data, create saved views, and ask natural language queries with Ask Sigma.

### Essential license

The Essential license is ideal for decision-making data consumers who require more deep-dive capabilities in published workbooks but don’t need to build workbooks themselves. This license tier includes all Lite license capabilities while also allowing members to drill into unaggregated underlying data, contribute to input tables, download workbook content, and schedule exports and alerts.

### Pro license

The Pro license is designed for data architects, BI analysts, and report builders who model, transform, and analyze data. This license tier offers the full range of Sigma features and capabilities, including the ability to create and manage datasets, data models, and workbooks. The Pro license also supports system administrators who manage organization settings and members.

## Account type and license relationship

Account types enable admin users to select granular permissions that determine which features and capabilities organization users can access. Sigma automatically assigns a license to each account type based on the highest license tier of the enabled permissions. This relationship allows for more flexible and scalable access control that adapts to ongoing changes in your user base and user requirements.

## Account type permission availability matrix

> 🚩
>
> ### If your organization utilizes the View/Act/Analyze/Build license model, refer to [this account type permission availability matrix](/docs/account-type-and-license-overview#account-type-permission-availability-matrix).

The following table compares the account type permissions associated with each license tier. When configuring an account type, admins can enable or disable any combination of permissions within and across license tiers.

|  | | Lite | Essential | Pro |
| --- | --- | --- | --- | --- |
| Data warehouse | | | | |
| Connections | View connections  *Browse connections, schemas, and database tables* | yes | yes | yes |
| Manage connections1  *Create new connections and manage existing ones*  *(Automatically enables the* ***View connections*** *permission)* | no | no | yes |
| Tables | Annotate tables1  *Annotate database tables (edit column details, metrics, and links)* | no | no | yes |
| Stored procedures | Create stored procedure actions  *Allow users to create stored procedure actions*  *(Automatically enables the* ***Call stored procedure actions*** *permission)* | no | no | yes |
| Call stored procedure actions  *Allow users to call stored procedure actions* | no | yes | yes |
| Write-back | | | | |
| Input tables | Create input tables2  *Create and edit input tables in workbooks* | no | no | yes |
| Materialization | Schedule materializations2  *Create and edit materialization schedules* | no | no | yes |
| CSV | Upload CSV  *Upload and analyze CSV data* | no | no | yes |
| Warehouse views | Create warehouse views2  *Create warehouse views based on datasets and workbook elements* | no | no | yes |
| Data modeling | | | | |
| Datasets | View datasets2  *View existing datasets and data models* | yes | yes | yes |
| Create, edit, and publish datasets2  *Create and manage datasets and data models*  *(Automatically enables the **View datasets** permission)* | no | no | yes |
| Features | Write Python  *Write Python code to run in your data platform* | no | no | yes |
| Write SQL  *Query a connected data platform directly with SQL* | no | no | yes |
| Documents | | | | |
| Workbooks | View workbooks2  *View and interact with explorations and published workbooks* | yes | yes | yes |
| Can comment on workbooks4  *View and add comments on workbooks* | yes | yes | yes |
| Basic explore2,3  *View and interact with explorations and published workbooks with added ability to drill into data, filter columns, enter input table data, and more*  *(Automatically enables the* ***View workbooks*** *permission)* | no | yes | yes |
| Full explore2,3  *Modify workbook elements to create custom views of published workbooks, configure actions, and more*  *(Automatically enables the* ***Basic explore*** *and* ***View workbooks*** *permissions)* | no | no | yes |
| Create, edit, and publish workbooks2  *Create new workbooks and manage existing ones*  *(Automatically enables the* ***Full explore****,* ***Basic explore****, and* ***View workbooks*** *permissions)* | no | no | yes |
| Set workbook data refresh2  *Set an automatic data refresh schedule for a workbook*  *(Automatically enables the* ***Create, edit, and publish workbooks*** *permission)* | no | no | yes |
| Version tags | Apply tag2  *Apply version tags to workbooks or data models* | no | no | yes |
| Org management | | | | |
| Usage dashboard | View usage dashboard  *View the organization dashboard* | no | no | yes |
| View SQL in usage dashboard  *View raw SQL in the organization usage dashboard*  *(Automatically enables the* *View usage dashboard* *permission)* | no | no | yes |
| Customization | Manage all workbook themes and fonts  *Create, edit, and delete workbook themes and custom fonts* | no | no | yes |
| Admin | Manage branding settings  *Manage organization branding settings, including workbook themes, custom fonts, and system emails* | no | no | yes |
| Plugins | Manage plugins  *Access plugin development features and manage custom plugins* | no | no | yes |
| Badges | Manage all badges  *Add, change, and remove workbook badges (Endorsed, Warning, or Deprecated)* | no | no | yes |
| Sharing / folders | | | | |
| Sharing and exports | Download2  *Immediately download entire workbooks, specific pages, and individual elements* | no | yes | yes |
| Export to email2  *Export entire workbooks, specific pages, and individual elements by email*  *(Automatically enables the **Download** permission)* | no | yes | yes |
| Run exports as recipient2  *Choose to run exports as the recipients.*  *(Automatically enables the **Download** and **Export to Email** permissions)* | no | yes | yes |
| Export to Google Sheet2  *Export data to Google Sheets spreadsheets*  *(Automatically enables the **Download** permission)* | no | yes | yes |
| Export to Google Drive2  *Export data to Google Drive folders*  *(Automatically enables the **Download** permission)* | no | yes | yes |
| Export to Slack2  *Export data to Slack channels*  *(Automatically enables the **Download** permission)* | no | yes | yes |
| Export to Microsoft Teams and SharePoint2  *Export data to Microsoft Teams channels or Microsoft SharePoint folders.*  *(Automatically enables the **Download** permission)* | no | yes | yes |
| Schedule export2  *Create, edit, and delete scheduled exports and alerts to send entire workbooks, specific pages, and individual elements*  *(Automatically enables the **Download** and **Export to Email** permissions)* | no | yes | yes |
| Share documents2  *Share folders and documents with organization members* | no | no | yes |
| Export to cloud2  *Export data to Google Cloud Storage (GCS) or Amazon S3*  *(Automatically enables the **Download** permission)* | no | no | yes |
| Export to webhook2  *Export data to webhook endpoints*  *(Automatically enables the **Download** permission)* | no | no | yes |
| Export as email burst2  *Export data as email bursts to send different reports for each email recipient.*  *(Automatically enables the **Download** and **Export to Email** permissions)* | no | no | yes |
| Folders | Create new folders2  *Create new personal, workspace, and shared folders* | no | yes | yes |
| Contribute to shared folders2  *Create new documents in workspaces and shared folders* | no | no | yes |
| Create new workspace  *Create new organization workspaces*  *(Automatically enables the* ***Contribute to shared folders*** *and* ***Share documents*** *permissions)* | no | no | yes |
| AI | | | | |
| AI features | Explain charts with AI5  *Use AI to instantly generate a description of any chart* | no | yes | yes |
| Use AI with formulas5  *Use the formula assistant to write new formulas, correct formula errors, and explain existing formulas* | no | no | yes |
| Use Ask Sigma5  *Access and use Ask Sigma to ask natural language queries* | yes | yes | yes |

1Access to individual connections are determined by [data permissions](/docs/data-permissions-overview).

2Access to individual datasets, data models, and workbooks are determined by [folder and document permissions](/docs/folder-and-document-permissions).

3For a comprehensive comparison of user capabilities, see [Basic explore vs. Full explore](/docs/basic-explore-vs-full-explore).

4Enables the ability to add and view comments for all license tiers. Also enables screenshot capture and annotation in comments for Essential and Pro licenses only.

5AI features such as Ask Sigma, explain charts with AI, and the AI-powered formula assistant require an AI provider to be configured for the organization. See [Configure an AI provider](/docs/configure-ai-features-for-your-organization#configure-an-ai-provider).

Updated 3 days ago

---

Related resources

* [Create and manage account types](/docs/create-and-manage-account-types)
* [View license utilization](/docs/view-license-utilization)
* [Basic explore vs. Full explore](/docs/basic-explore-vs-full-explore)

* [Table of Contents](#)
* + [License tiers](#license-tiers)
  + [License tiers](#license-tiers-1)
  + - [Lite license](#lite-license)
    - [Essential license](#essential-license)
    - [Pro license](#pro-license)
  + [Account type and license relationship](#account-type-and-license-relationship)
  + [Account type permission availability matrix](#account-type-permission-availability-matrix)