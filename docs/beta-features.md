# Sigma product releases

# Sigma product releases

This document explains how Sigma Computing releases changes to the product, how those changes are announced in [What’s new in Sigma](/changelog), and what to expect for different release phases.

## How Sigma Computing releases changes to the product

Sigma Computing is continuously evolving the Sigma service, adding new features and capabilities and improving what our customers can do with the product. Releases happen continuously, both for bug fixes and for new functionality. We strive to maximize the value delivered to our customers, and do not use fixed release cadences that slow down software delivery.

Because we release major changes in staged rollouts using feature flags, certain features or functionality might be available in your organization that are not yet available to all customers. Documentation for incrementally-released updates typically appears once a majority of customers have access to the change.

## Release notes

Sigma Computing announces recent feature releases, functionality changes, and bug fixes weekly on Fridays, excepting holidays. See [What’s new in Sigma](/changelog) to review this changelog. Customers can subscribe to the changelog using [RSS](https://help.sigmacomputing.com/changelog.rss).

## Beta features

Sigma Computing makes some features available in private or public beta releases. These features are identified in the product with a beta icon (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/badge_beta.svg)) and in the documentation with a beta notice. Some features do not have a component in the user interface of the product to which a beta icon can be appended; in those cases, the beta notice appears in the documentation only.

**Private beta** features are not available by default and are not publicly announced. Private beta features are subject to frequent changes and might or might not have documentation available. If you are interested in joining a limited test group and enabling a private beta feature in your Sigma organization, contact Support or reach out to your Account Executive.

**Public beta** features are made available in the product to all customers in staged rollouts. Customers do not need to request access to public beta features. Public beta features might or might not have documentation available.

All beta features, whether private or public, and their documentation are subject to the following notice:

> 🚩
>
> "Sigma may make certain functionality or features related to the Service which are designated as beta, pilot, non-production, or a similar description (each, a "Beta Feature") available to Customer. Beta Features may be used by Customer in Customer’s sole discretion and at Customer’s own risk. Beta Features are intended for evaluation purposes only. Sigma may discontinue Beta Features at any time in Sigma’s sole discretion and may choose to never make them generally available. Beta Features are considered part of the Service, however, Beta Features are provided “AS-IS”."

## Generally available features

Unless otherwise indicated in the documentation, features and functionality are generally available (GA) in the product. When first released, GA features are made available in the product to all customers in staged rollouts. See [How Sigma Computing releases changes to the product](/docs/sigma-product-releases#how-sigma-computing-releases-changes-to-the-product). If a feature was previously released in a beta release, the release notes indicate the transition to GA by including "(GA)" in the release announcement.

## Deprecated features

Sigma Computing may deprecate features and functionality from the product. Deprecated features are features for which Sigma Computing has declared an intention to stop further enhancement. Deprecated features continue to work in the product for existing customers but might not be available to newly created organizations.

Sigma Computing continues to support deprecated features and provide critical bug fixes until they are removed from the product for all customers. When a feature is deprecated, Sigma customers must plan for the future removal of support. Support for such features will end after a notice period. The notice period differs based on the availability of the feature, as follows:

* For Generally Available features, Sigma provides six months' prior notice before the end of support date.
* For Public Beta features, Sigma provides three months' prior notice before the end of support date.

Sigma Computing will make diligent efforts to provide support for customers to migrate from a deprecated feature to an alternative feature. Deprecated features are marked in the Sigma documentation as "deprecated".

The following features are deprecated:

* [Get workbook schema](/reference/getworkbookschema)`GET /v2/workbooks/{workbookId}/schema`
* [Update a connection](/reference/updateconnectiondeprecated) `PATCH /v2/connections/{connectionId}`
* Workbook modes without Live Edit (documentation available only to selected customers)
* Warehouse data editing (documentation available only to selected customers)
* Application embedding (documentation available only to selected customers)
* [Secure embedding with signed URLs](/docs/secure-embedding-with-signed-urls)

## Removed features

Sigma Computing may remove features and functionality from the product after a deprecation period.

Removed features are no longer supported and cannot be used. Customers must find an alternative to using the removed feature or functionality. Documentation for removed features is unavailable to all customers.

Updated 3 days ago

---

[Escalate critical issues](/docs/escalate-critical-issues)[Supported regions, data platforms, and features](/docs/region-warehouse-and-feature-support)

* [Table of Contents](#)
* + [How Sigma Computing releases changes to the product](#how-sigma-computing-releases-changes-to-the-product)
  + [Release notes](#release-notes)
  + [Beta features](#beta-features)
  + [Generally available features](#generally-available-features)
  + [Deprecated features](#deprecated-features)
  + [Removed features](#removed-features)