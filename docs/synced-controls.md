# Synced controls

# Synced controls

Synced controls are workbook control elements that have identical, synchronized copies. Both filter controls and parameters support synced copies. Here we explain how synced controls work, how to create and identify synced controls, and how to unsync controls.

Synced copies can help maintain context when a control affects elements across several workbook pages. For example, you may want to track your organization's high-level sales data on one page and drill into region-specific data on another. If the same filter control targets elements on both pages, we recommend that you display the control on both pages; this enables you and your workbook's viewers to edit the control value from either page, instead of switching back and forth. See [Example #2: Maintain context across pages](/docs/synced-controls#example-2-maintain-context-across-pages).

You can also use synced controls to encourage pre-selection of control values before the data loads on other pages. Place copies of the controls on the landing page that the viewer sees before the data display pages. Queries run against your CDW after a page opens, so preselecting filter values  increases performance and reduce CDW compute costs. See [Example #3: Preselect control values](/docs/synced-controls#example-3-preselect-control-values).

## Requirements

* You must have **Can Edit** [access](/docs/folder-and-document-permissions#document-permissions) to the individual workbook, and be in Edit mode.
* Create synced copies directly from existing controls. You must have a working control before making a copy.
* It is not possible to sync two pre-existing controls.

## Synced copies vs. duplicates

Synced copies are not the same as duplicates.

**Duplicates**

Independently operating controls.

Edits to a control's settings or values do not transfer to duplicate copies. The first of the duplicate filter controls that gets edited has precedence, and behaves as the primary control. The other copies of the control only display values that are not filtered out by the first control.

Duplicate controls have different control IDs.

**Synced copies**

Fully identical and synchronized controls.

A synced copy is automatically synchronized with all other synced copies. Edits to one of the settings or values updates the state of all synced copies.

There is no precedence among synced copies. Deleting or unsyncing any of the copies or the original control does not affect other copies.

Synced controls share the same control ID.

## Create a synced copy of a control

Synced controls are created directly from existing controls. You must have a control before you can create a synced copy of it. When a synced copy is made, the copy is automatically synced to all other synced copies.

It is not possible to sync two pre-existing controls. Duplicating a control or a page with controls does not result in synced copies.

To create a synced control, change to Edit mode, and then complete the following steps:

1. Hover over the element and open its more (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg)) menu.
2. Click **Create a synced copy**.

   ![](https://files.readme.io/53b82c1-1.png)  
   A synced copy appears on the page.

   To move the control to a new page, open its More (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg)) menu and select a page from the **Move to** menu.

## Identify synced controls

To identify a control's synced copies, enter Edit mode, then:

1. Select the control.
2. In the editor panel, open the **SYNCED COPIES** tab.

   ![Screenshot of synced copies tab](https://files.readme.io/c4274f4-2.png)
3. The tab lists all synced copies, including the version you selected.
4. Click on a copy to navigate to it.

## Unsync controls

When you unsync control is unsynced, it remains on the page as an independently operating duplicate.

To unsync a control, perform these steps in Edit mode:

1. Hover over the element and open its more (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg)) menu.
2. Click **Unsync control**.

   ![Screenshot of open More menu with Unsync control highlighted](https://files.readme.io/94291cd-3.png)

## Synced control examples

### Example #1: Two controls, one target

These two control elements are synced: they are identical copies of the same control.

When you select new values in one of these control elements, Sigma updates both controls.

Observe this in both the synced controls and in the target table.

### Example #2: Maintain context across pages

Synced copies maintain context when a control affects elements in several pages of the workbook.

### Example #3: Preselect control values

Use synced controls to pre-select control values before loading data, reducing the volume of data that needs to be retrieved from your data warehouse.

For example, place copies of controls on a landing page so that a viewer can select the relevant data, then navigate to relevant pages that display the data.

After the viewer opens the page with data on it, the queries are run to retrieve data from your data warehouse.

Updated 3 days ago

---

Related resources

* [Intro to control elements](/docs/intro-to-control-elements)
* [Create and manage a control element](/docs/create-and-manage-a-control-element)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Synced copies vs. duplicates](#synced-copies-vs-duplicates)
  + [Create a synced copy of a control](#create-a-synced-copy-of-a-control)
  + [Identify synced controls](#identify-synced-controls)
  + [Unsync controls](#unsync-controls)
  + [Synced control examples](#synced-control-examples)
  + - [Example #1: Two controls, one target](#example-1-two-controls-one-target)
    - [Example #2: Maintain context across pages](#example-2-maintain-context-across-pages)
    - [Example #3: Preselect control values](#example-3-preselect-control-values)