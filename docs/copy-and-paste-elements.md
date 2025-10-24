# Copy and paste workbook elements

# Copy and paste workbook elements

Sigma's copy-and-paste functionality allows you to replicate elements in various locations. You can copy and paste an element within its originating workbook, or you can copy an element from one workbook and paste it in another. Sigma supports copying and pasting multiple elements at once.

## User requirements

The ability to copy and paste elements requires the following:

* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Explore workbooks** or **Create, edit, and publish workbooks** permission enabled.
* You must be the workbook owner or be granted **Can explore** or **Can edit** [workbook permission](/docs/folder-and-document-permissions).

## Copy and paste an element

You can copy and paste an element using [keyboard shortcuts](#copy-and-paste-with-keyboard-shortcuts), or by [using the element menu](#copy-and-paste-via-the-element-menu). If you want to copy and paste multiple elements at once, you must do so via keyboard shortcuts.

> 🚩
>
> ### Linked input tables don't currently support copy-and-paste functionality. However, you can copy empty input tables and all data, UI, and control elements.

### Copy and paste with keyboard shortcuts

1. Select your desired element. If you want to select multiple elements, you can do so by clicking the workbook canvas and dragging your cursor until your desired elements are selected.
2. Press the `⌘` + `C` keys on your keyboard to copy the element(s).
3. Navigate to where you want to paste the element(s), then press `⌘` + `V` on your keyboard.

### Copy and paste via the element menu

1. Open a workbook in [any mode](/docs/workbook-modes-overview-view-explore-edit), then select or hover over the element(s) you want to copy.
2. In the element toolbar, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** to open the element menu, then select **Copy element**. The original element and all applicable parent elements in its lineage are copied.
3. If you want to paste the element in an empty space:

   * Open the destination workbook in [**Explore** or **Edit** mode](/docs/workbook-modes-overview-view-explore-edit), then find an empty space in the canvas. Right-click the empty space to open the action menu, then select **Paste element**. A replica of the original element is added to the empty space.
4. If you want to paste the element below an existing element:

   * Open the destination workbook in [**Explore** or **Edit** mode](/docs/workbook-modes-overview-view-explore-edit), then select or hover over an existing element.
   * In the element toolbar, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** to open the element menu, then select **Paste element below**.

## Frequently asked questions

How do the Copy/Paste element actions differ from the Duplicate action? When should I use each?

|  | Duplicate | Copy/Paste element |
| --- | --- | --- |
| Action type | Single workbook action | Cross-workbook action |
| Content copied | Original element only | Original element + lineage |
| Destination | Current workbook/page | Any workbook/page |
| Lineage association | Original and duplicate reference the same lineage | Original and replica reference separate lineages |

When you select **Duplicate** in the element menu, Sigma immediately adds a duplicate directly below the original element in the same workbook and page. If the original is a child element, the duplicate shares its lineage. In other words, the original and its duplicate reference the same parent elements in the workbook. Changes applied to a parent element are reflected in the original and its duplicate. This feature is recommended when you need to create a duplicate in the same workbook containing the original element.

When you select **Copy element** in the element menu, Sigma copies the element to the browser. You can then select **Paste element** to add a replica of the copied element to any workbook and page across your organization. If the original element is a child element, its lineage is also copied and pasted to the destination workbook page. In this case, the original and its replica are disassociated and don't share the same lineage (they reference separate parent elements). This feature is recommended when you need to replicate the original element in a different workbook.

If I copy a child element, but its parent element exists in a different page of the workbook, does Sigma still replicate the parent element in the destination?

Yes. The element's entire lineage is copied, regardless of a parent element's location in the originating workbook. In the destination workbook, however, child and parent elements are pasted to the same page.

Can I copy an element and paste it to a workbook in a different organization?

No. An element can only be copied and pasted between workbooks created in the same Sigma organization.

Are control elements copied and pasted with an element?

Yes, most control elements that affect the original element and its lineage are copied and pasted to the destination workbook page. An exception occurs when a parameter control affects an element with a custom SQL source. For more information, refer to the following question about copying and pasting custom SQL elements.

Can I copy and paste a custom SQL element?

Yes. An element with a custom SQL source can be copied and pasted whether it's the original element or part of its lineage. Related parameter controls aren't replicated with the custom SQL element, but they can be copied and pasted separately. In the destination workbook, the custom SQL element automatically remaps to the copied control element or an existing parameter control with the same control ID.

How are permissions applied when I copy and paste an element between different workbooks? Who can view the element's data?

The ability to view an element's data depends on a user's access to the data source. When you share a workbook with a user who doesn’t have access to a particular element’s data source (the source dataset or connection table), the user can view that element’s data in the shared workbook only. If the user copies the element and pastes it to another workbook, the replica doesn’t load any data in the destination workbook page, and Sigma notifies the user that they don't have access.

Are an element's filters carried over when it's copied and pasted?

Yes. If filters are already applied to the original element at the time it's copied, those filters are applied to the replica in the destination workbook page. This also applies to parent elements that are copied and pasted as part of the original element's lineage.

Can I copy and paste an entire workbook page?

Yes. See [Copy and paste workbook pages](/docs/copy-a-page-within-and-between-workbooks) for more information.

Updated 3 days ago

---

Related resources

* [Copy and paste workbook pages (Beta)](/docs/copy-and-paste-workbook-pages)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Copy and paste an element](#copy-and-paste-an-element)
  + - [Copy and paste with keyboard shortcuts](#copy-and-paste-with-keyboard-shortcuts)
    - [Copy and paste via the element menu](#copy-and-paste-via-the-element-menu)
  + [Frequently asked questions](#frequently-asked-questions)