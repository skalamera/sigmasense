# Create workbooks from templates

# Create workbooks from templates

Templates are reusable workbook structures that let you build new workbooks with speed and consistency.

This document explains how to access existing templates and use them to create new workbooks. For more information about templates, see [Create and edit templates](/docs/create-and-edit-workbook-templates) and [Share templates](/docs/share-workbook-templates).

## Requirements

The ability to access an existing template and use it to create a workbook requires the following:

* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Can create, edit, and publish workbooks** permission enabled.
* To access templates created by users of your organization, you must be the template owner or be granted **Can use** or **Can edit** access to the template.
* To access Sigma templates and other templates shared with your organization, you must be an internal user. Guest users cannot access external templates.

## Create a workbook from a template

1. From Sigma **Home**, select **Templates** from the navigation panel.
2. Click the template you want to explore.

   The templated workbook opens.
3. Explore the template by clicking any of its interactive elements. These include tables, charts, and controls. None of your changes affect the template itself.
4. (Optional) Save the template as a workbook to create an editable and publishable workbook from the template. Click **Save as** in the document header, then choose a name and location for the workbook.

## Use your data in a workbook template (swap sources)

To use your data in a workbook template, change the data source of the template. The data you want to use must be available in Sigma.

To swap the source of a workbook template:

1. From Sigma **Home**, select **Templates** from the navigation panel.
2. Click the template you want to use.

   The templated workbook opens.
3. If the workbook is built on [sample data](/docs/sigmas-sample-connection), you are prompted to swap the data source to a different connection. When prompted, click **Swap now**.

   The **Swap data sources** page opens.
4. Sigma attempts to automatically match your data with the data expected by the template.

   You can override the automatic match to choose a different data source. If no data source is automatically matched, you must manually select a source.

   To replace a matched source, click **Edit** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/edit.svg)) next to the source, then select a new source from the modal.
5. If the template requires additional sources, review each source match from **All sources in use** panel.
6. When all data sources are ready to be swapped, click **Swap**.
7. Explore the changes to confirm that your data looks correct.
8. To create an editable and publishable workbook from the template, click **Save as** in the document header.

Workbooks also support source swapping. See [Change the data source for a workbook or element](/docs/change-the-data-source-for-a-workbook-or-element).

Updated 3 days ago

---

Related resources

* [Get started with workbook templates](/docs/get-started-with-workbook-templates)
* [Create and edit workbook templates](/docs/create-and-edit-workbook-templates)
* [Share templates with different orgs](/docs/share-templates-with-different-orgs)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Create a workbook from a template](#create-a-workbook-from-a-template)
  + [Use your data in a workbook template (swap sources)](#use-your-data-in-a-workbook-template-swap-sources)