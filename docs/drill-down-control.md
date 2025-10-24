# Drill down control

# Drill down control

## Requirements

* To create a drill control, your account must have **Can Edit** access to the workbook.
* The activities described on this page are only available in Edit mode. To begin editing, click **Edit** in the top right corner of the page. For more information see [Workbook Lifecycle](/docs/workbook-lifecycle-explore-draft-and-publish).

## Create a drill control

1. In the editor panel, click **+ADD NEW** .
   The **ADD NEW** panel opens.
2. In the **CONTROL** **ELEMENTS** section, select **Drill Down**.

   ![Screen_Shot_2022-02-09_at_12.16.49_PM.png](https://files.readme.io/b70a089-1.png)

   The new drill down element appears on the page.
3. In the editor panel **SETTINGS** > **Value source** section, use the dropdown list to select a data element containing the columns that you intend to use in the drill path.

   ![Screen_Shot_2022-02-09_at_12.18.39_PM.png](https://files.readme.io/89ba253-2.png)

   If the selected data element supports drill downs, Sigma adds a column under **DRILL CATEGORIES**. You can keep this, change it, or add more.
4. Next to the **DRILL CATEGORIES section,** click **+Add drill category** .
5. Select a column from the list.

   ![Screen_Shot_2022-02-09_at_12.19.32_PM.png](https://files.readme.io/8bc861d-3.png)
6. (Optional) Repeat the step above to add any additional columns to your drill path. The element displays the path.

   ![Screen_Shot_2022-02-09_at_12.20.24_PM.png](https://files.readme.io/14a992e-4.png)
7. Add one or more targets to your control. Targets are the data elements that a control manipulates. In the editor panel, click the **TARGETS** tab.
8. Click **+Add Target** .
9. Select a target data element from the list.

   ![Screen_Shot_2022-02-09_at_12.22.47_PM.png](https://files.readme.io/3e030de-5.png)
10. The **Map with columns in target** section appears. Use the dropdown menu to map the drill path column to the corresponding column in the target data element.
11. The **SETTINGS** tab shows all the drill categories. You can change the ID and/or the label of the control.

    ![Screen_Shot_2022-02-09_at_12.29.55_PM.png](https://files.readme.io/8686725-6.png)
12. Repeat steps 8-10 to add additional targets.
13. To test it, click a category name in the drill control element’s drill path and drill into that category. The target data element updates accordingly.

## Create a drill control from an existing drill path

1. Right click a value in the data element visualization to open its menu.
2. Select **Drill up** > **Create drill control**.

   ![Screen_Shot_2022-02-09_at_2.39.10_PM.png](https://files.readme.io/bccf652-7.png)

   Sigma adds the control and you can edit it further, if needed.

## Add categories to an existing drill control

1. Select the existing drill down control.
2. In the editor panel **SETTINGS** section, click **DRILL CATEGORIES** > **+Add drill category**.
     
    ***Note***: The **+Add drill category** button will only be enabled if a **Value source** is selected above.
3. Select a column from the list.

   ![Screen_Shot_2021-09-23_at_2.57.59_PM.png](https://files.readme.io/19f636d-8.png)
4. Repeat the step above to add any additional columns to your drill path. Sigma displays each drill category in the drill control's drill path.

   ![Screen_Shot_2021-09-23_at_3.02.50_PM.png](https://files.readme.io/44bf0d7-9.png)

## Add targets to an existing drill control

1. Select the existing drill down control.
2. In the editor panel, click the **TARGETS** tab.

   ![Screen_Shot_2021-09-23_at_3.08.31_PM.png](https://files.readme.io/4195f76-10.png)
3. Click **+Add Target** .
4. Select a target element from the list.

   ![Screen_Shot_2021-09-23_at_3.11.56_PM.png](https://files.readme.io/91ecc71-11.png)

   A box representing your target element appear.
5. Use the drop down menus to map your drill path drill categories to the corresponding columns in the target element.

   ![Screen_Shot_2021-09-23_at_3.14.17_PM.png](https://files.readme.io/c07da23-12.png)
6. Repeat steps 3-5 to add additional targets.
7. To test it, click a category name in the control element’s drill path to drill into that category. Your new target element updates accordingly.

   ![Screen_Shot_2021-09-23_at_3.20.05_PM.png](https://files.readme.io/67e4ab3-13.png)

Updated 3 days ago

---

Related resources

* [Visualization drill paths (Drill Anywhere)](/docs/visualization-drill-paths-drill-anywhere)
* [Intro to control elements](/docs/intro-to-control-elements)
* [Drill Downs in Sigma (Community)](https://community.sigmacomputing.com/t/drill-downs-in-sigma/2048?_gl=1*h8fxxp*_ga*ODkzMjkyNDY1LjE3MDAwMDU1NzM.*_ga_PMMQG4DCHC*MTcwMTIwOTMxNS4yNC4xLjE3MDEyMTY1MjIuNTguMC4w)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Create a drill control](#create-a-drill-control)
  + [Create a drill control from an existing drill path](#create-a-drill-control-from-an-existing-drill-path)
  + [Add categories to an existing drill control](#add-categories-to-an-existing-drill-control)
  + [Add targets to an existing drill control](#add-targets-to-an-existing-drill-control)