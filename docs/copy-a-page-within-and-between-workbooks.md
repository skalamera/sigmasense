# Copy workbook pages

# Copy workbook pages

You can copy a page from one workbook to another, or copy one workbook page to another page in the same workbook.

## Requirements

* When copy and pasting between workbooks, both workbooks must belong to the same organization.
* When copy and pasting between workbooks, both workbooks must use the same layout style. You cannot copy a page from an old layout to the new grid layout. For more information about the new grid layout see [Create and manage workbook layouts](/docs/create-and-manage-workbook-layouts).
* For one or multiple workbooks, your account type must be Pro or Admin, or be a custom [account type](/docs/user-account-types) with the Edit Workbook or Explore Workbook permission enabled.
* You must be the workbook owner or be granted Can edit or Can explore [workbook permission](/docs/folder-and-document-permissions) on one or multiple workbooks.

## Tips for copy and pasting workbook pages

* Sigma copies the whole page, plus dependent sources for elements on the page, even if the sources are not on the page. For sources that are not on the page, Sigma creates a second page with the naming convention “Page Name - Dependencies”.
  + If the user performing the copy operation does not have access permissions to the source data of an element on the page, Sigma will copy and paste it, but the user will not see the data and pasted elements might show a permissions error message.
* Linked input tables are not supported when copy and pasting workbook pages. Sigma can copy empty input tables and all data, UI, and control elements.
* If you only need to copy elements on the page, consider doing that. See [Copy and paste elements.](/docs/copy-and-paste-elements)

## Copy and paste a page

1. From the page menu, select **Copy page**. Sigma copies the page.
2. (Optional) Click out of the copy confirmation message, or wait a few seconds for it to disappear.
3. Paste the copied page.
   * If copying to the same workbook, press cmd/ctrl-v or right-click and select **Paste**.  
     ![page-paste-menu.png](https://files.readme.io/be30309-2.png)  
     Sigma pastes the new page into the workbook and appends "Copy" to the page name.  
     ![copied-new-page.png](https://files.readme.io/7b0048a-3.png)
   * If copying to another workbook, go to the workbook and enter Edit mode. Press cmd/ctrl-v or right-click and select **Paste**.  
     Sigma pastes the new page into the workbook and appends "Copy" to the page name.  
     If there are dependencies, Sigma pastes them into another page and appends "Dependencies" to the page name.
4. Edit the new, copied page as you like.

Updated 3 days ago

---

Related resources

* [Design your workbook layout](/docs/create-and-manage-workbook-layouts)
* [Copy and paste workbook elements](/docs/copy-and-paste-elements)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Tips for copy and pasting workbook pages](#tips-for-copy-and-pasting-workbook-pages)
  + [Copy and paste a page](#copy-and-paste-a-page)