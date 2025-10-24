# Share and accept cross-org workbook templates

# Share and accept cross-org workbook templates

Cross-org sharing allows you to share and accept workbook templates across different Sigma organizations. When the receiving organization accepts a shared template, they must choose their own data source to populate the template, ensuring no data from the sharing organization is disclosed.

This document explains how to share and accept a workbook template across organizations.

## User requirements

To share or accept a workbook template through cross-org sharing, you must be assigned the **Admin** [account type](/docs/license-and-account-type-overview).

## Share a template with another organization

1. Go to your **Home** page.
2. In the navigation menu, select **Templates**.
3. In the **Templates** page, locate the template you want to share, then click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** and select **Share** from the menu.

   > 📘
   >
   > ### To add new template, first click **Create Template**, then create a template from a saved workbook.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/Share+and+accept+cross-org+workbook+templates/cross-org-wb-template_share.png)
4. In the **Share Template** modal, click **Share across Sigma Orgs**.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/Share+and+accept+cross-org+workbook+templates/cross-org-wb-template_share-across-sigma-orgs.png)
5. In the **Cross Org Share Template** modal, provide the required information:

   1. In the **Company Login URL Slug** field, enter the slug associated with the receiving organization. This is a unique identifier that typically follows `app.sigmacomputing.com/` in the Sigma URL.
   2. [optional] In the **Add a message** field, enter a message to include in the invitation email Sigma sends to the receiving organization's admins.
   3. Click **Share Template**.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/Share+and+accept+cross-org+workbook+templates/cross-org-wb-template_share-template.png)

## Accept a template shared with your organization

When your organization receives an invitation to use a shared template, you or another admin must swap the data source (to populate the template with your organization's data) before accepting it. The template will not be available to your organization members until this is completed.

1. In the invitation email, click **Open in Sigma**.
2. In the **Swap Data Sources Overview** modal, Sigma identifies connections and data sources that closely match the data used in the original template. Choose from these matches to automatically swap the data, or manually select and match individual data source columns.

   * Use a matching connection and data source:

     1. In the **Matching Connection** and **Matching Data Sources** fields, select the relevant options.
     2. Click **Choose** to preview the template with the swapped data.

        ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/Share+and+accept+cross-org+workbook+templates/cross-org-wb-template_swap-data-sources-overview.png)
   * Manually select and map the data:

     1. Click **Match Manually**.
     2. In the **Swap Data Sources** screen, preview the column names from the template's original data source, then click **Select Source**.

        ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/Share+and+accept+cross-org+workbook+templates/cross-org-wb-template_review-current-source.png)
     3. In the **Select source to replace** modal, select the preferred data source to populate the template. To view and select a data source from a different connection, click **Back** in the source selector.
     4. Review the selected data, then click **Select** to proceed.

        ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/Share+and+accept+cross-org+workbook+templates/cross-org-wb-template_select-data-source.png)
     5. In the **Swap Data Sources** screen, map the template's original data source columns to the swapped data source columns.
     6. Click **Choose** to preview the template with the swapped data.

        ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/Share+and+accept+cross-org+workbook+templates/cross-org-wb-template_manually-match-columns.png)
3. To save the template with the swapped data, click **Accept** in the workbook header. Otherwise, click **Swap sources** and repeat step 2 to select different data.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Admin/Share+and+accept+cross-org+workbook+templates/cross-org-wb-template_accept.png)

Updated 3 days ago

---

Related resources

* [Create and edit workbook templates](/docs/create-and-edit-workbook-templates)
* [Share workbook templates](/docs/share-workbook-templates)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Share a template with another organization](#share-a-template-with-another-organization)
  + [Accept a template shared with your organization](#accept-a-template-shared-with-your-organization)