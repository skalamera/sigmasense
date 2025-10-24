# Configure Warehouse Data Editing (Deprecated)

# Configure Warehouse Data Editing (Deprecated)

> 🚩
>
> ### As of February 2022, this feature is deprecated and available to a limited group of organizations with legacy access.

Sigma's warehouse data editing feature allows you and your team to update your warehouse data directly from Sigma’s spreadsheet interface. As an Admin, you can choose which connections and individual Tables support data editing. Sigma level access permissions also allow you to control which organization members and/or teams can edit your data.

## Requirements

* You must be a Sigma Admin to configure this feature. [Learn about user account types](/docs/user-account-types).
* You may need to make configuration updates in your warehouse (see [Step 1: Configure Data Editing on your Connection](/docs/configure-warehouse-data-editing-deprecated#step-1-configure-data-editing-on-your-connection)). If so, you will need the appropriate warehouse privileges.

## Configure Data Warehouse Editing

### Step 1: Configure Data Editing on your Connection

The following steps outline how you can enable Data Editing for your warehouse connection. Depending on your current connection configuration, you may need to make updates in Sigma and/or in your warehouse.

1. Confirm that the **User/Role associated with the connection** has permission to **UPDATE** the intended Tables in the warehouse. Warehouse permission should be granted at the Table level.  
   For guidance, please reference your warehouse’s documentation:  
   • [Snowflake](https://docs.snowflake.com/en/user-guide/security-access-control-privileges.html#all-privileges-alphabetical) (If you use a [Snowflake with OAuth](/docs/oauth-with-snowflake) connection, permissions are granted to individuals on your OAuth provider.)  
   • [Redshift](https://docs.aws.amazon.com/redshift/latest/dg/r_GRANT.html)  
   • [BigQuery](https://cloud.google.com/bigquery/docs/table-access-controls-intro)
2. If your warehouse supports table **primary keys,** and if you do not already have one selected, please set one now.  
   **Note**: If a primary key is not defined in your warehouse, we will prompt you to select one directly in Sigma. However, we do recommend that you define this key in your warehouse if possible.
3. [optional] To track who updated a row and when it was updated, add empty date and string columns to your warehouse table. From within Sigma, you’ll configure these columns to be automatically updated when changes are made.  
   For more information, see the [Track UPDATED\_AT and UPDATED\_BY](/docs/configure-warehouse-data-editing-deprecated#track-updated_at-and-updated_by) section below.

### Step 2: Set up Data Editing on a Table

1. Open the Table you would like to make editable from Sigma.  
   This can be done from the Connection section of Sigma’s left navigation panel.
2. Click the **Edit** button in the Table header to enter Edit mode.
3. Open the Table page’s **Columns** tab.  
   ![Screen_Shot_2020-10-28_at_6.39.57_PM.png](https://files.readme.io/f28a8f3-1.png)
4. If a table primary key is not yet set in your warehouse, or if your warehouse does not support primary keys, click the **Configure Primary Key** button under **Table Configurations**. Then select a key from the available columns and save.  
   ***Note**: We highly recommend setting a primary key in your warehouse if supported.*
5. In the column list, switch on **Is Editable** for any columns you would like to permit edits on.  
   ![Screen_Shot_2020-10-22_at_4.59.04_PM.png](https://files.readme.io/64cf80f-2.png)
6. [optional] Define a list of optional input values for individual editable columns by clicking the gear icon and populating the Column Configuration value list. [Learn more](/docs/configure-warehouse-data-editing-deprecated#select-which-column-are-editable).
7. [optional] Click the **Configure Data Editing** button under **Table Configurations**, to define columns for tracking who updated a row (`UPDATED_AT`) and when it was updated (`UDPATED_BY`).  
   See [Track UPDATED\_AT and UPDATED\_BY](/docs/configure-warehouse-data-editing-deprecated#track-updated_at-and-updated_by).
8. Click the **Publish** button in the top right corner of your table’s header.
9. To confirm that editing has been enabled for your table, open the Table’s **Overview** tab, and look for the **Edit Cell Values** button on the right hand side of the page. Clicking this button will bring you and other editors to the table’s Warehouse Data Editing page.

#### Select which Column are Editable

Data editors can only edit the Table columns you, as an Admin, declare editable. By default, all Table columns are NOT editable. To select which columns are editable:

1. Open the Table page’s **Columns** tab. And, if you have not already, click the ‘Edit’ button to put the Table in edit mode.
2. In the column list, click the **Is Editable** toggle next to the column to enable or disable editing.  
   ![Screen_Shot_2020-10-22_at_5.05.01_PM.png](https://files.readme.io/1d1cc4c-3.png)

#### Define Limited Input Options for Columns

Selectable value lists can be created on a per-column basis. Create a list of possible cell values for the column, and the list will be displayed whenever someone begins editing a cell. Editors will be limited to using only these values when updating the table.

If a value options list is not provided, editors will be permitted to enter any value matching the column’s type.

1. Open the Table page’s **Columns** tab. And, if you have not already, click the ‘Edit’ button to put the Table in edit mode.
2. If a column is editable, you will see a gear icon under the column table’s **Is Editable** column. Click this gear icon to open the **Column Configuration** model.
3. Add one or more value options to the list.  
   ![Screen_Shot_2020-10-22_at_5.04.00_PM.png](https://files.readme.io/aede5be-4.png)
4. Click **Save**.

#### Track UPDATED\_AT and UPDATED\_BY

You can optionally choose to track `UPDATED_AT` and `UPDATED_BY` data by adding these columns to your table from the warehouse

1. Add columns for `UPDATED_AT` and `UPDATED_BY` data to the table in your warehouse.
2. Open the table in Sigma.
3. Click the **Edit** button in the table header to enter Edit mode.
4. Select the **Columns** tab.
5. Under **Table Configurations**, click the **Configure Data Editing** button to open the associated modal.
6. In the modal, select your target `UPDATED_AT` and `UPDATED_BY` columns under the corresponding header.  
   ![](https://files.readme.io/993ebff-5.png)
7. Click **Save**.

### Step 3: Grant Table “Can Update” Permissions to Users in Sigma

Sigma 'Can Update' permission can only be granted at the Table level. Table update permission is also required in the warehouse (see [Step 1: Configure Data Editing on your Connection](/docs/configure-warehouse-data-editing-deprecated#step-1-configure-data-editing-on-your-connection)).

1. Open the table in Sigma.  
   This can be done from the Connection section of Sigma’s left hand navigation panel.
2. Navigate to the table's **Permissions** tab.  
   ![Screen_Shot_2020-10-28_at_6.46.11_PM.png](https://files.readme.io/1260c00-6.png)
3. Click the **Add Permission** button to open the permissions modal.
4. Enter the organization member or team.
5. Under **Permission**, select ‘Can Update’. [Learn more about permission options](/docs/data-permissions-overview).  
   ![Screen_Shot_2020-10-22_at_5.26.35_PM.png](https://files.readme.io/527dddd-7.png)
6. [optional] Enter an email message to notify the grant recipient(s) of their new permission. You may also choose to opt out of sending an email.
7. Click **Save**.

## Disable Warehouse Data Editing for your Organization

Warehouse Data Editing is enabled by default for all organizations. This simply means that organization Admins have the option to configure the feature on a per-connection basis. Organization members will not be able to use this feature without this Admin configuration.

If you do not plan to configure Warehouse Data Editing, you may choose to disable it at the organization level. To do so:

1. Open your Admin Portal.
2. On the **Account** page, find the section titled **Features**.
3. Click the toggle switch next to **Warehouse Data Editing.  
   ![Screen_Shot_2021-11-19_at_3.25.41_PM_copy.png](https://files.readme.io/10e9971-8.png)**

Updated 3 days ago

---

Related resources

* [Edit Warehouse Data from Sigma (Deprecated)](/docs/edit-warehouse-data-from-sigma-deprecated)
* [Permissions](/docs/permissions-1)
* [Connect to data sources](/docs/connect-to-data-sources)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Configure Data Warehouse Editing](#configure-data-warehouse-editing)
  + - [Step 1: Configure Data Editing on your Connection](#step-1-configure-data-editing-on-your-connection)
    - [Step 2: Set up Data Editing on a Table](#step-2-set-up-data-editing-on-a-table)
    - [Step 3: Grant Table “Can Update” Permissions to Users in Sigma](#step-3-grant-table-can-update-permissions-to-users-in-sigma)
  + [Disable Warehouse Data Editing for your Organization](#disable-warehouse-data-editing-for-your-organization)