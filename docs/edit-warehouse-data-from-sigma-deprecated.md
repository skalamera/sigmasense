# Edit Warehouse Data from Sigma (Deprecated)

# Edit Warehouse Data from Sigma (Deprecated)

> 🚧
>
> ### **Important**: This feature is **deprecated** as of February 2022. Access is limited to a small set of grandfathered organizations.

Sigma’s warehouse data editing feature allows you to update data in your warehouse directly from Sigma’s spreadsheet interface. Warehouse data editing is only accessible from warehouse tables and requires Admin configuration and granted update permissions.

## Requirements

* Data Warehouse Editing must be enabled on the warehouse table you wish to edit.  
  Admins can use the following instructions to enable this feature for your organization and warehouse tables: [Configure Warehouse Data Editing.](/docs/configure-warehouse-data-editing-deprecated)
* You must have permission in Sigma to update your target data warehouse table. Permissions are granted per warehouse table.

## Edit Table Data

1. Open the warehouse table you would like to edit.  
   This can be done from the **Connection** section of Sigma’s left hand navigation panel.
2. On the table’s **Overview** tab, click the **Edit Cell Values** button on the right hand side of the page. This will open the warehouse table’s Warehouse Data Editing page.  
   ***Note**: The **Edit Cell Values** button will only be enabled if Data Editing has been configured for the warehouse table and you have been granted permission to edit. Please contact your Admin if you need assistance.*
3. On the table’s Warehouse Data Editing page, double click a cell to begin editing. You may edit as many cells as you wish before submitting your changes. Use the keyboard to navigate between cells. You can also [copy and paste cell values](/docs/edit-warehouse-data-from-sigma-deprecated).  
   ***Note**:*
   * *Greyed columns are READ ONLY. Contact your Admin to enable editing on these cells.*
   * *Yellow cells indicate your pending edits.*
4. A dropdown value list may appear when you begin editing certain cells. This Admin-defined list indicates acceptable cell values for the associated column. If no list appears, you may enter any value matching the column's [value type](/docs/oops).
5. [optional] You can choose to add filters to narrow your focus to select rows. These filters only live for the duration of your edit session. [Learn more](/docs/edit-warehouse-data-from-sigma-deprecated).
6. Once you are satisfied with your edits, click **Save to Warehouse.**
7. Once your changes are saved, you refresh the table data by clicking the refresh icon button above the top right corner of the editable table. Or click ‘X’ in the top right corner of the page to navigate back to the main table page.

### Copy and Paste Cell Values

Copy and paste is available for all editable cells. Use the standard keyboard shortcuts ( ⌘⇧C and ⌘⇧V ) to copy and paste cell data.

### Revert Edits

Pending table edits can be reverted to their original state as a whole or per cell.

To revert all pending edits, click the ‘Revert All’ button in the top right corner of the page.

To revert an edit on a single cell, right click on the cell to open the cell menu, and select ‘Revert edit’.

## Filter Rows While Editing

In the Data Editor, you can choose to add filters to narrow your focus to select rows. These filters only live for the duration of your edit session.

Filters work similarly to worksheet filters.

Updated 3 days ago

---

Related resources

* [Configure Warehouse Data Editing (Deprecated)](/docs/configure-warehouse-data-editing-deprecated)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Edit Table Data](#edit-table-data)
  + - [Copy and Paste Cell Values](#copy-and-paste-cell-values)
    - [Revert Edits](#revert-edits)
  + [Filter Rows While Editing](#filter-rows-while-editing)