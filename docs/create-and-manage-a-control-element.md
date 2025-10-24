# Create and manage a control element

# Create and manage a control element

Add a control element to a workbook to provide predefined interactions to users viewing or customizing a workbook, such as inputs that modify data, selections to filter data or change displayed data, drilldown paths, or other ways of manipulating data. Add a control element to a data model to function as a parameter and filter tables in the data model, according to a selected value in a workbook control.

After adding a control element, you can add targets to filter elements or data sources, or pass values to a dataset parameter or a control element in a data model.

You can also duplicate an existing control. For more details about the available types of controls, see [Intro to control elements](/docs/intro-to-control-elements).

## Requirements

* You must have **Can edit** [access](/docs/folder-and-document-permissions) to the workbook or data model, or **Can explore** access to the workbook.

## Add a control element

You can add one or more control elements to a workbook or data model. You cannot add a control to a dataset worksheet, but you can reference a workbook control value in a dataset with a parameter. For details about the available control types, see [Intro to control elements](/docs/intro-to-control-elements).

To add a control element:

1. Open the workbook or data model for editing.
2. On the **Add element** bar, select **Controls**, then select the [control type](/docs/intro-to-control-elements) that you want to add.

   The new control appears on the canvas.
3. Select the control element, then in the **Properties** tab of the editor panel, configure the control. Configuration options available in the **Settings** tab depend on the type of control.
4. (Optional) Select **Targets** to specify which elements to filter or modify when the user interacts with the control. See [Specify the target of the control](#specify-the-target-of-the-control).

   > 💡
   >
   > ### Before you publish a workbook, check the values specified for each control. You might want each control to have a specific value to provide a specific experience for users interacting with the workbook.

After you create a control, you can customize the design.

### Change the control type for a control

Some control types, such as a date control, cannot be added directly. Instead, you can change the control type after adding a control element to a workbook or data model:

1. Open the workbook or data model for editing or customizing.
2. Select the control element.
3. In the **Properties** tab of the editor panel, for **Control type**, select a different control type.

   The control type changes.

   You can configure the settings for the new control. Depending on the configuration and control types, previous configurations might be reset. The control ID and formatting remain the same.

## Convert an existing element filter into a control

You can convert an existing [data element filter](/docs/data-element-filters) to a control, which can simplify the process of configuring and targeting a control.

When you convert a data element filter to a control element, the original filtered data element is automatically added as a target of the new control. You can customize and add additional targets to the control using the editor panel.

To create a control from an existing data element filter:

1. Open a workbook or data model for editing.
2. Hover over the element that you want to filter. In the element bar that appears, select **Filters** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/filter.svg)).
3. For a specific filter on the data element, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**, then select **Convert to page control**.  
   A control of the same type as the filter appears directly above the selected data element.
4. Use the editor panel to customize and configure the control.

After you create a control, you can customize the design.

## Specify the target of the control

Add targets to a control to specify which data elements and data sources to filter based on the input or selection in the control element.

* To modify a data element or data source, add a target to the control.
* To modify a data model, add a target to the control.
* To modify a dataset, add a dataset as a target.

A control does not require targets. For example, you can use a control without targets as a parameter, passing a selected or inputted value to a formula for a calculated column or a custom SQL statement. See [Reference control values as parameters](/docs/parameters-in-workbooks).

> 🚩
>
> ### When a control targets a data element, the control can also be modified from the data element filter menu:
>
> ![](https://files.readme.io/997be65da672ec473476a433f647138d6593a26c1982a180418ba9e6f3eae0cf-ctrl-filters-element.png)

1. Open a workbook or data model for editing.
2. Select the control.
3. In the editor panel, in **Properties**, select the **Targets** tab.  
   ![](https://files.readme.io/748ed843cc4454e54de5ba60fe532e00bc569fea2a484ee137eca3aa43d24683-control-add-target-start.png)
4. Click **+ Add filter target**.
5. Select one or more workbook elements or data sources used in the workbook that you want to be changed by the control.  
   In this example, the data element table `VIOLATION_TYPES` is selected. The table is on the same page of the workbook as the control.  
   ![](https://files.readme.io/0d8bcfbf53750c1f9aa99f21d42b8dd0e4b0620ef54c435f952c3d9fe8240bb3-control-add-target.png)  
   The table appears under **Targets**, and the count of targets for the control increases to 1.  
   As you add other targets to this control, the count increases.  
   ![](https://files.readme.io/d7b51984e35462eee97d8b848bdf5622b91996495d0e8330ced253dfdc6ca435-control-added-target.png)
6. Update the column targeted by the control. By default, the control targets the first column of the table. To change the target column, click the current column and choose the new target column. In this example, the target column **Risk Category** is correct for the control.

   As you change the target column, the default name of the control updates to match the selected column. In this example, the name of the filter control was **New Control**, then it changed to **Risk Category** when the table was added as a target.

After adding targets, customize and configure the control. See [Types of controls](/docs/intro-to-control-elements#types-of-controls).

### Pass a value from a workbook control to a data model control

To filter a data model based on user input in a workbook, you can pass a value from a workbook control element to a data model control element by targeting the data model control ID as a parameter from the workbook control element. This functionality mimics targeting a dataset parameter, but with a data model.

To pass a value to a data model from a workbook as a parameter, the following must be true:

* The data model must be a data source for the workbook.
* The data model must have a control element that targets one or more elements in the data model. To add a control element to a data model, see [Add a control element](#add-a-control-element) on this page.
* The control element in the data model must be the same data type as the output of the workbook control element. For example, the output of a number input control element is a single value number, which can be passed to a single value list control, a slider control, or a number input control in a data model.

To pass a value from a workbook to a data model as a parameter:

1. Open a workbook for editing or customizing.
2. Select a control element.
3. In the **Properties** tab of the editor panel, select the **Targets** tab.
4. Select **Add source parameter**, then choose the data model with the control that you want to target.

   ![Target tab of a text control with add source parameter selected and the Events data model chosen. The available control IDs are listed in a dropdown menu.](https://files.readme.io/a0a02630e4159069e038508de8da2971312d4c40bc0d1623f165239990eeeb84-control-add-a-param.png)
5. In the dropdown list, select the control ID(s) in the data model that you want to populate with the values from the workbook control element. Only control elements with supported data types are available to select.  
   ![](https://files.readme.io/6f918f0746a0044e25197ab1b44fb6ede23c1e1c07f4f650ffa4d7793e94af28-control-add-param.png)

After adding targets, customize and configure the control. See [Types of controls](/docs/intro-to-control-elements#types-of-controls).

### Pass a value from a workbook control to a dataset parameter

To filter a dataset based on user input in a workbook, you can pass a value from a control to a dataset parameter by targeting the parameter from the control element.

To target the dataset parameter, the output type of the control must be the same as the data type of the parameter. For example, a single value number and a number.

1. Open a workbook for editing.
2. Select a control element.
3. In the **Properties** tab of the editor panel, select the **Targets** tab.
4. Select **Add source parameter**, then choose the dataset with the parameter that you want to target.
5. In the dropdown list, select the dataset parameter(s) that you want to populate with the value of the workbook control element. Only parameters with supported data types are available to select.

To create a dataset parameter, see [Create and manage dataset parameters](/docs/create-and-manage-dataset-parameters).

After adding targets, customize and configure the control. See [Types of controls](/docs/intro-to-control-elements#types-of-controls).

## Duplicate a control

After creating a control element, you can duplicate it. Duplicating a control preserves the formatting, targets, and other settings while allowing you to modify the duplicate control separately from the original control.

> 💡
>
> ### If you want to keep the control configuration exactly the same, create a synced copy. See [Synced controls](/docs/synced-controls).

To duplicate a control without creating a synced copy:

1. Open the workbook or data model for editing.
2. Select the control element that you want to duplicate, then select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**.
3. In the element menu, select **Duplicate**. You can also use a keyboard shortcut. The duplicate control appears below the original control, and you can make configuration changes or customizations.

## Set a control as required

If you make a control element required, all data elements on the same page as the control display no data until a value is selected in the control, even if the elements do not reference and are not targeted by the control. After a user makes a selection in a required control, the data elements on the page load and display data.

You can make a control required in a data model, but data model behavior is unchanged.

To make a control required, do the following:

1. Open the workbook for editing.
2. Select the control.
3. On the **Settings** tab, select the checkbox for **Required**.

   The changes save immediately. To make the changes visible to those without edit access, publish the workbook.

> 📘
>
> ### A drill down control cannot be required.

Updated 3 days ago

---

Related resources

* [Intro to control elements](/docs/intro-to-control-elements)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Add a control element](#add-a-control-element)
  + - [Change the control type for a control](#change-the-control-type-for-a-control)
  + [Convert an existing element filter into a control](#convert-an-existing-element-filter-into-a-control)
  + [Specify the target of the control](#specify-the-target-of-the-control)
  + - [Pass a value from a workbook control to a data model control](#pass-a-value-from-a-workbook-control-to-a-data-model-control)
    - [Pass a value from a workbook control to a dataset parameter](#pass-a-value-from-a-workbook-control-to-a-dataset-parameter)
  + [Duplicate a control](#duplicate-a-control)
  + [Set a control as required](#set-a-control-as-required)