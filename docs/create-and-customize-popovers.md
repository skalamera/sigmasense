# Use popovers to simplify a workbook interface

# Use popovers to simplify a workbook interface

Use popovers to display contextual information (tables, charts, filters, text, etc.) in floating containers anchored to specific trigger buttons. Popovers open on demand without obscuring the rest of the workbook page, which can help create a more efficient and simplified workbook interface.

Popovers are a [layout element](/docs/intro-to-layout-elements), allowing you to guide users and create focused interfaces as you build [data apps](/docs/data-apps) in Sigma.

![A popover trigger button with an open popover containing three control filters](https://files.readme.io/9a3c7662b146c6df9721b32f73513f25841cf3d128f0813051bfa177dea371d9-image.png)

Use a popover when you want to:

* Display multiple filters for one table with a single button.
* Reduce visual clutter by grouping filters, controls, and buttons.
* Provide additional functionality to a user without navigating them away from the current page.

To create a floating container that obscures the workbook page, and that isn't anchored to workbook elements, see [Create and customize modals](/docs/add-a-modal-to-a-workbook).

## User requirements

The ability to create and customize a popover requires the following:

* You must be assigned an account type with the **Create, edit, and publish workbooks** permission enabled.
* You must be the workbook owner or be granted **Can edit** access to the workbook.

## Limitations

Sigma does not currently support nesting popovers inside other popovers. Popovers can, however, be nested inside [modals](/docs/use-modals-to-create-focused-content-views).

## Create a popover

To create a popover, first add a **Popover** element to your workbook.

1. Open a workbook draft.
2. In the **Add element** bar, select **Layout**, then select **Popover**.

   ![Image of the Add elements bar with the Layout > Popover option highlighted for selection](https://files.readme.io/3b88c2800ee064a52bb320acd37c4764ccf0f202c3c8221c80b2baf00c818e39-image.png)

   Sigma adds the two popover components described below and identified in the following screenshot:

   1. Trigger button: Opens the popover.
   2. Popover configuration page: Allows you to customize the content, properties, and style of the popover. *The configuration page and corresponding tab are visible in the workbook draft only.*

      ![Image of a workbook with annotations pointing to the popover button in the workbook page and the popover configuration page tab in the workbook footer](https://files.readme.io/3a6493f8a029a1e7e83e071cb9510d63ad24eb45ccbf832c38ae7ebb457ab51e-image.png)

## Customize a popover

To customize the content, width, or style of a popover, see the following sections:

* [Add or edit the popover content](#add-or-edit-the-popover-content)
* [Change the popover width](#change-the-popover-width)
* [Customize the popover style](#customize-the-popover-style)
* [Customize a popover trigger button](#customize-a-popover-trigger-button)

### Add or edit the popover content

Add or edit contextual information to display in the popover.

1. Select the tab for the popover configuration page.
2. Use the **Add element** bar to add elements in the same way you would add them to a workbook page. You can include any data, input, chart, control, UI, or layout element with the exception of popovers. *Sigma does not support nested popovers.*

   ![Image of the popover configuration page displaying the popover container, editor panel, and the Add element bar with the Controls option highlighted for selection](https://files.readme.io/aee767ef0d34ff8814402d5cb5f6dae16a91898ebf7773631a55e454d2b4318a-image.png)

### Change the popover width

Adjust the width of the popover to accommodate its contents and placement in the workbook.

1. Select the tab for the popover configuration page.
2. In the editor panel, select the **Properties** tab.
3. In the **Width** dropdown, select an option to adjust the width of the popover.

   ![Image of the editor panel open to the Properties tab with the Width dropdown field selected and open](https://files.readme.io/0cda9263ea53ad0e1c0677221dba3111abd2e82cdff39bc59eee2c767e50fad9-image.png)

### Customize the popover style

Configure the popover spacing, padding, background color, and element gap.

1. Select the tab for the popover configuration page.
2. In the editor panel, select the **Format** tab.
3. Expand the **Popover style** section to view the style settings.
4. Configure the style settings:

   * **Spacing**: Select the size of the padding and element gap.
   * **Padding**: Enable or disable the space between the border of the popover and its content.
   * **Background color:** Select the color displayed behind the elements in the popover.
   * **Element gap**: Enable or disable the space between elements in the popover.

   ![Image of the editor panel open to the Format tab with the Popover style section expanded to display all popover style settings](https://files.readme.io/f421e9135f1ec566733e1fd303c8e2190b1da6b9cc62516289c52e3b500f25de-image.png)

### Customize a popover trigger button

Customize the trigger button that the popover is anchored to. You can configure properties that define the button's appearance, including the label, style, alignment, shape, and size.

1. To navigate directly to the trigger button:

   1. Select the tab for the popover configuration page.
   2. In the editor panel, select the **Properties** tab.
   3. In the **Trigger button** section, click **Edit**.

   ![Image of the editor panel open to the Properties tab with the trigger button Edit option highlighted for selection](https://files.readme.io/c056a3f7a64f80321681ef0cb751373da9445fb034001499a87a526ad89d8b39-image.png)

   Sigma opens the workbook page containing the trigger button and automatically opens the button properties in the editor panel.
2. In the editor panel, configure the button properties:

   * **Appearance**: Select a button variant.
   * **Text**: Add a label or call to action (CTA) to display in the button. Enter `=` to include a dynamic value defined by a formula expression.
   * **Style**: Customize the font weight, text color, and button color.
   * **Horizontal**: Align or stretch the button relative to the total element width. The popover mirrors the alignment setting of the button. I.e. a left-aligned button opens a left-aligned popover.
   * **Vertical**: Align the button relative to the total element height. The popover mirrors the alignment setting of the button. I.e. a top-aligned button opens a popover above the button as long as there is enough space onscreen.
   * **Shape**: Select a button shape.
   * **Size**: Select a button size.
   * **Show filter count**: Select the checkbox to display the number of active filters originating from the popover. *An active filter is any control element in the popover that has been modified from its default value.*

   ![Image of a workbook page containing the popover trigger button, with the popover button properties displayed in the editor panel](https://files.readme.io/d627ac93fd21d1d90085bca09742c5ade3f8ba20c1c53da3689a7e15b74199cf-image.png)

## Delete a popover

Use one of the following methods to delete a popover, including its trigger button, configuration page, and all elements within the popover.

* [Delete a popover from the trigger button](#delete-a-popover-from-the-trigger-button)
* [Delete a popover from the configuration page tab](#delete-a-popover-from-the-configuration-page-tab)

### Delete a popover from the trigger button

1. Open the workbook page containing the trigger button.
2. Hover over the trigger button, then click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**.
3. In the element menu, select **Delete element**.

### Delete a popover from the configuration page tab

1. In the popover configuration page tab, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)).
2. In the page menu, select **Delete**.j

Updated 3 days ago

---

[Use modals to create focused content views](/docs/use-modals-to-create-focused-content-views)[Use the navigation element to guide user exploration (Beta)](/docs/use-the-navigation-element-to-guide-user-exploration)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Limitations](#limitations)
  + [Create a popover](#create-a-popover)
  + [Customize a popover](#customize-a-popover)
  + - [Add or edit the popover content](#add-or-edit-the-popover-content)
    - [Change the popover width](#change-the-popover-width)
    - [Customize the popover style](#customize-the-popover-style)
    - [Customize a popover trigger button](#customize-a-popover-trigger-button)
  + [Delete a popover](#delete-a-popover)
  + - [Delete a popover from the trigger button](#delete-a-popover-from-the-trigger-button)
    - [Delete a popover from the configuration page tab](#delete-a-popover-from-the-configuration-page-tab)