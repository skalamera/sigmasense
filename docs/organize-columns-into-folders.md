# Organize columns into folders

# Organize columns into folders

When working with data elements in data models and workbooks you can organize columns into folders, letting you nest columns into relevant groups.

When you organize columns into folders, you can do the following:

* Create as many folders for columns as you want.
* Nest folders inside other folders.
* Add folders of columns to table groupings or chart axes.
* Delete or duplicate a folder and its columns.

You cannot create folders for columns in datasets or warehouse tables.

Folders are available to child elements and downstream elements. If you make a folder for columns in a data model table, data elements that use that table as a data source display the folders.

> 📘
>
> ### Folders created in a source element after the child element was created do not automatically appear. For example, folders added to a data model table do not automatically appear in tables in a workbook that use that data model table as a source. You can add these folders manually by selecting **+** (**Add columns...**), then choosing **Add source columns…** to open the source columns list.

## Requirements

You must have **Can edit** or **Can explore** access to the workbook or data model

## Add columns to a new folder

You can add columns to a new folder from the column menu, or from the list of columns.

1. Open the document for editing, or start customizing the workbook.
2. Select the data element.
3. Select one or more columns, then select the down arrow ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg) to open the column menu and choose **Move to new folder**.

   A new folder appears. If you selected columns in different parts of the column list, the folder and its columns appear in the same spot as the column that you selected first.

> 💡
>
> You can also click **+** > **Add folder** to add an empty folder, then click and drag columns into the folder.

## Add columns or folders to an existing folder

You can select columns or folders to add to an existing folder.

1. Open the document for editing, or start customizing the workbook.
2. Select the data element, then locate the columns list in the editor panel.
3. Select the columns or folders that you want to add to the existing folder, then click and drag the selected columns or folders into the folder.

## Remove columns from a folder

To remove columns from a folder:

1. Open the folder and drag and drop each column outside of the folder
2. Select the down arrow ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg) to open the folder menu, then select **Delete folder**.

> 🚧
>
> ### Deleting the folder without moving the columns also deletes the columns from the data element. Add deleted columns back by selecting **+** (**Add columns...**), then choose **Add source columns...** to open the **Source columns** list.

## Manage a column folder

Right-click a folder in the list of columns to perform the following tasks:

* Rename the folder

  > 💡
  >
  > You can also double-click the name of a folder to rename it.
* Delete the folder and all columns and folders contained in it. Add deleted columns back to your data element by selecting **+** (**Add columns...**), then choose **Add source columns...** to open the **Source columns** list.
* Duplicate the folder and all columns and folders contained in it. Folder names remain the same.

Updated 3 days ago

---

[Create and edit period-over-period analysis](/docs/create-and-edit-period-over-period-analysis)[Tables](/docs/tables)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Add columns to a new folder](#add-columns-to-a-new-folder)
  + [Add columns or folders to an existing folder](#add-columns-or-folders-to-an-existing-folder)
  + [Remove columns from a folder](#remove-columns-from-a-folder)
  + [Manage a column folder](#manage-a-column-folder)