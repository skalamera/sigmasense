# Workbooks overview

# Workbooks overview

Whether you're a spreadsheet-savvy analyst or more familiar with Business Intelligence (BI) tools, Sigma combines the best of spreadsheets and BI tools in one place — a workbook:

* Like a spreadsheet, workbooks have pages and can display data in tables and pivot tables.
* Like a BI tool, workbooks provide dashboard-like layouts that can include charts, graphs, interactive filters and controls, tables, text, and images.

In a workbook, you can perform data exploration and analysis, build complex visualizations, prepare detailed reports for export, and more. Workbooks also provide the interface for [building a data app](/docs/data-apps) or [designing embedded analytics](/docs/intro-to-embedded-analytics) for your product or organization.

This document provides a conceptual overview of workbooks and links to more resources.

## About workbooks

Start an exploratory analysis, build enterprise-grade analytics, or develop a data app by creating a workbook. Almost everything in Sigma happens in a workbook:

* Analyze data in [tables and pivot tables](/docs/create-and-manage-tables).
* Visualize data with [charts and maps](/docs/intro-to-visualizations).
* Format and [export reports to various destinations](/docs/send-or-schedule-workbook-exports).
* [Collaborate with colleagues](/docs/collaborate-with-live-edit-in-workbooks) on analysis and development.
* [Build interactivity with actions](/docs/intro-to-actions).
* [Customize layouts](/docs/design-workbook-layouts) and designs with [themes](/docs/create-and-manage-workbook-themes), [containers](/docs/organize-workbook-layouts-with-containers), [modals](/docs/add-a-modal-to-a-workbook), and other elements.
* and more...

## What's in a workbook

A workbook contains one or more pages. Modals and other app-like functionality also appear like pages of the workbook.

Each workbook page or modal has a canvas on which you can place elements. You can arrange elements on the page canvas. Element types include:

* Data elements, like tables, charts, and pivot tables. See [Create a data element](/docs/create-a-data-element).
* Input elements, like empty or linked input tables. See [Intro to input tables](/docs/intro-to-input-tables).
* Control elements, like filters and inputs. See [Intro to control elements](/docs/intro-to-control-elements).
* UI elements, like text, images, buttons, embeds, and dividers. See [Intro to UI elements](/docs/intro-to-ui-elements).
* Layout elements, like containers, tabbed containers, and modals. See [Design workbook layouts](/docs/design-workbook-layouts).

For more details about using and navigating a workbook, see [Navigate a workbook](/docs/navigating-a-workbook).

## The lifecycle of a workbook

When you first create a workbook, you open an exploration. An exploration is an unsaved workbook that supports ad hoc data exploration and exploratory data analysis (EDA) workflows that you might not need beyond the current moment. Working with an exploration helps you avoid cluttering folders and workspaces with one-off documents. You can access explorations on the **Explorations** tab of the the **Recents** page. For more details about explorations, see [Ad hoc data explorations](/docs/ad-hoc-data-explorations).

To continue your analysis or experimentation, save your exploration as a workbook. When you save a workbook, you can edit and make changes in the draft, or view a published version of the workbook like a dashboard or report. For more details, see [Create a workbook](/docs/create-a-workbook) and [Workbook lifecycle: explore, draft, and publish](/docs/workbook-lifecycle-explore-draft-and-publish).

After saving, only you have access to the workbook unless you save it in a folder or workspace that others have access to. For more details about sharing workbooks, see [Share a workbook](/docs/share-a-workbook).

After a workbook is created, different users can interact with it in different ways.

* You might want to give users of your embedded analytics solution access to a tagged and stable version of the workbook, rather than relying on the latest published version for your embedding. See [Add version tags to workbooks and data models](/docs/add-version-tags-to-workbooks-and-data-models).
* Users without permissions to create workbooks might be able to customize existing workbooks by creating views. See [Create and interact with custom views](/docs/create-and-interact-with-custom-views). To save a specific configuration of a workbook, you can save a view and share it with others. See [Create and share saved views](/docs/create-and-share-saved-views).
* Users with less access might only be able to view or filter the dashboards or reports that you build, or input data into forms for [data apps](/docs/data-apps).

For more details, see [Workbook modes: view, explore, and edit](/docs/workbook-modes-overview).

## Data used in workbooks

Workbooks can use data from multiple sources, such as tables in a [supported data platform](/docs/region-warehouse-and-feature-support) connected to Sigma, tables in a data model created in Sigma, or data added to Sigma and stored in your data platform, like [CSV-formatted files](/docs/upload-csv-data) or information added to an [input table](/docs/intro-to-input-tables). For more information about connecting to data platforms, see [Connect to data sources](/docs/connect-to-data-sources).

Your data is always live, accessible at scale, and cannot be deleted or corrupted.

After Sigma is connected to your data platform, you can create workbooks directly from tables in your database or data catalog, or model the data in Sigma. Using a data model or dataset as the source for your workbooks helps ensure consistency. For more details, see [Get started with data modeling](/docs/get-started-with-data-modeling) and the [Data modeling tutorial](/docs/data-modeling-tutorial).

When users access a dataset, data model, or workbook that has been shared with them, the document owner's [access to the source data](/docs/data-permissions-overview) is evaluated within Sigma and the queries to the data platform are run using the credentials specified in the connection settings.

For connections that support OAuth, queries might instead run differently:

* If the connection is configured to use OAuth *without* a service account, queries from the document run with the user's personal OAuth credentials configured for the data platform.
* If the connection is configured to use OAuth *with* a service account, an admin can configure individual workbooks to use the service account credentials instead. See [Run a workbook with service account credentials](/docs/run-a-workbook-with-service-account-credentials).

For details about what queries are being run in a workbook or data model, see [Examine workbook and data model queries](/docs/examine-workbook-queries). For a dataset, see [Examine dataset queries](/docs/examine-dataset-queries).

### Information for legacy worksheet users

If you previously used Sigma worksheets or dashboards, you may be familiar with the process of creating multiple worksheets to source visualizations for a single dashboard. Workbooks alleviate this workflow by allowing you to build your analysis exactly where it is displayed to your report consumers.

Updated 3 days ago

---

Related resources

* [Edit, draft, and publish a workbook](/docs/edit-draft-and-publish-a-workbook)
* [Workbook modes overview: View, Explore, Edit](/docs/workbook-modes-overview-view-explore-edit)
* [Workbook lifecycle: explore, draft, and publish](/docs/workbook-lifecycle-explore-draft-and-publish)
* [Create a workbook](/docs/create-a-workbook)
* [Intro to Element Types](/docs/intro-to-element-types)
* [Workbook example templates](/docs/workbook-example-templates)
* [What's Possible with Sigma Workbooks (Webinar)](https://www.sigmacomputing.com/webinars-and-events/whats-possible-with-sigma-workbooks?_gl=1*yg4d0d*_ga*ODkzMjkyNDY1LjE3MDAwMDU1NzM.*_ga_PMMQG4DCHC*MTcwMTEyOTA5OS4yMS4xLjE3MDExMjkxMjUuMzQuMC4w)
* [Questions and Answers on Workbooks and Visualizations (Community)](https://community.sigmacomputing.com/t/questions-and-answers-on-workbooks-and-visualizations/13?_gl=1*yg4d0d*_ga*ODkzMjkyNDY1LjE3MDAwMDU1NzM.*_ga_PMMQG4DCHC*MTcwMTEyOTA5OS4yMS4xLjE3MDExMjkxMjUuMzQuMC4w)

* [Table of Contents](#)
* + [About workbooks](#about-workbooks)
  + [What's in a workbook](#whats-in-a-workbook)
  + [The lifecycle of a workbook](#the-lifecycle-of-a-workbook)
  + [Data used in workbooks](#data-used-in-workbooks)
  + - [Information for legacy worksheet users](#information-for-legacy-worksheet-users)