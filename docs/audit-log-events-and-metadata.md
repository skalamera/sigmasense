# Audit log events and metadata

# Audit log events and metadata

The **Sigma Audit Log** is a connection that provides metadata related to user-initiated events that occur within your Sigma organization.

This document details audit log event categories, event types, and entry metadata. For more information about audit logging with Sigma, see the following:

* [Enable or disable audit logging](/docs/enable-audit-logging)
* [Access and explore audit logs](/docs/access-and-explore-audit-logs)
* [Create an audit logs storage integration](/docs/create-an-audit-logs-storage-integration)
* [Export audit log data to cloud storage](/docs/export-audit-log-data-to-cloud-storage)

## Documentation memo

This document references the audit log with its default column settings and connection configurations. If settings and configurations were customized by an **Admin** user, column visibility and naming in your audit log may differ.

To confirm column visibility and identify the default columns defined in this document, refer to the **Column** tab in your audit log. If necessary, you can cross-reference your audit log's custom “friendly names” with cloud data warehouse (CDW) or database management system (DBMS) column IDs provided in the event metadata tables throughout this document.

## Event categories

The audit log records user events in the following categories:

## Event types and metadata

### Base entry metadata (all entries)

All audit entries—regardless of event category or type—include the following base metadata:

## Audit events reference

Select an event category to browse the available audit log events in that category.

## Sigma Shared metadata reference

Select a table name to view the columns available in the `SIGMA_SHARED` audit tables.

Updated 3 days ago

---

Related resources

* [Access and explore audit logs](/docs/access-and-explore-audit-logs)

* [Table of Contents](#)
* + [Documentation memo](#documentation-memo)
  + [Event categories](#event-categories)
  + [Event types and metadata](#event-types-and-metadata)
  + - [Base entry metadata (all entries)](#base-entry-metadata-all-entries)
  + [Audit events reference](#audit-events-reference)
  + [Sigma Shared metadata reference](#sigma-shared-metadata-reference)