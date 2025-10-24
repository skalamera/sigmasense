# Add system-generated columns to input tables

# Add system-generated columns to input tables

Add system-generated columns to input tables to expose metadata for auditing and other data management processes.

* **Row edit history**: Records the timestamp and user email address associated with each row's creation or most recent update.
* **Row ID**: Populates unique row identifiers that support data management and referential integrity.

This document explains how to add system-generated row edit history and row ID columns to input tables. For information about other input table data governance options, see [Configure data governance options for input tables](/docs/configure-data-governance-options-for-input-tables).

## Add row edit history

Add columns containing row edit history to provide data transparency and promote accountability. Row edit history columns track the timestamp and user email associated with row edits that occur through [direct input](/docs/edit-existing-input-table-columns) and [actions](/docs/intro-to-actions).

* Click the plus (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg)) icon at the end of the column header, then hover over **Row edit history** and select an option:

  |  |  |
  | --- | --- |
  | **Last updated at** | Date and time the most recent edit was applied to the row. |
  | **Last updated by** | Email address of the user who applied the most recent edit to the row. |
  | **Created at** | Date and time the row was added to the input table. |
  | **Created by** | Email address of the user who initially added the row to the input table. |

  ![](https://files.readme.io/5321c8243ee5ecfca7a71e928700c564ead0c8115c10b3a5c1e4197e40ca0053-image.png)

  The column populates the edit history for all existing rows in the input table.

  > 📘
  >
  > ### When a user duplicates an input table, all row edit history (**Created at/by** and **Last updated at/by**) in the copy initially reflects the time of the duplication and the user who initiated it.

  ![](https://files.readme.io/e06a7942e17ea89f096139f2a60b724ea5d714fd16fadc6924880619a4b7ece2-image.png)

## Add row ID

Add a column containing row IDs to establish a primary key that uniquely identifies each row in the input table.

> 📘
>
> ### System-generated row IDs are irrelevant to linked input tables and only available for empty and CSV input tables.

* Click the plus (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg)) icon at the end of the column header, then select **Row ID**.

  ![](https://files.readme.io/48c296d852e4bff7adeb81372cdb79ac00dd772c25fdcbe87c34cb237b31e7d7-image.png)

  The column populates a unique ID for all existing rows in the input table, including empty rows.

  > 📘
  >
  > ### When a user duplicates an input table, Sigma preserves the row IDs for existing rows, resulting in identical IDs in the original and copy. For new rows added after duplication, however, Sigma generates unique IDs.

  ![](https://files.readme.io/82f0deb2159c1bb7a33cac0b1619a576c728dd49d70fe598d79e79caa91b3d02-image.png)

Updated 3 days ago

---

[Customize data entry permission on input tables](/docs/customize-data-entry-permission-on-input-tables)[Design layouts](/docs/design-layouts)

* [Table of Contents](#)
* + [Add row edit history](#add-row-edit-history)
  + [Add row ID](#add-row-id)