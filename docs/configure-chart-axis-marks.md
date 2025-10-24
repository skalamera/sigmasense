# Configure chart axis marks

# Configure chart axis marks

Sigma supports configuring custom chart axis marks, like ticks and grid lines. You can change the appearance, spacing and step size of both major (labeled) and minor (unlabeled) chart ticks. Utilizing axis marks can increase the readability of your chart and allow you to customize the reference points in your visualizations.

This document covers how to configure axis marks in Sigma.

## **User requirements**

* You must have **Can Edit** or **Can Explore** [access](/docs/folder-and-document-permissions) to an individual workbook.

## **Configure chart axis marks**

> 📘
>
> ### Configuring chart axis marks is only supported for charts with **Linear** or **Time** selected as the **Scale type**.

By default, the axis mark options shown will differ slightly based on the scale type of your chart. To configure axis marks:

1. Select your desired chart, then select the **Format** tab in the editor panel.
2. Open the **X-axis** or **Y-axis** dropdown.
3. From the **Axis marks** menu, select your desired axis mark option:

   * **Tick**: Adds axis marks along the axis of your chart where the axis labels are located.
   * **Grid line**: Adds vertical lines to the background of your chart, aligned with the axis labels.
   * **Both**: Adds both ticks and grid lines to your chart.
   * **None**: Removes both ticks and grid lines from your chart.

> 📘
>
> ### Labels for axis marks may be hidden if they overlap.

4. Configure your desired **Axis mark spacing** option. You can select **Auto**, **Count**, or **Step**. If you select **Auto**, the axis mark spacing is automatically configured based on your chart type and data. If you chose **Count** or **Step**, configure your desired settings.
5. For charts with **Count** axis mark spacing, enter your desired number of axis marks. To produce values that are regularly spaced (e.g. every 1, 5, 10 or every day, week, or month), the exact number of axis marks displayed may change based on your data. For full control over spacing, use **Step**.
6. For charts with **Step** axis mark spacing, configure your desired settings:

|  |  |
| --- | --- |
| **Unit** | *(For time axes)* Select your desired unit (e.g. **Year**, **Week**, or **Minute**). |
| **Step size** | Enter your desired step size. This refers to the number of units between each axis mark. For example, for a time axis with a unit of **Minute** and step size of `15`, there will be 15 minutes between each axis mark. For a numeric axis with a step size of `200`, there will be 200 units between each axis mark. |
| **Anchor** | *(Optional)* Once you have entered a step size, you can specify an **Anchor**. Anchors can be useful if you want axis marks to align with a specific value.  By default, axis marks "step" from the beginning of the first whole unit at or after your data's starting point. For example, if your step unit is **Month** and your data begins on June 15th, the first axis mark will be on July 1st (the start of the next whole unit). If you instead wanted your axis marks to be on every 15th of the month, you could set an anchor of `6/15/2025`.  Anchors can also be used for time in units smaller than a day - for example, changing the anchor `6/15/2025, 12PM` will cause axis marks to appear at midday, instead of at midnight.  Anchors operate similarly with numeric data. For example, an anchor of `100` with a step size of `1,000` will result in the chart being labeled with `100`, `1,100`, `2,100`, `3,100` and so forth. |

> 💡
>
> ### Setting an anchor applies to both major and minor axis marks, and can be used to align major and minor axis marks so they overlap. To do so, set the anchor to the date or number you want them to overlap at.

5. To enable minor axis marks (unlabeled marks between the labeled major marks), turn the **Show minor axis marks** toggle on. Configure your minor axis marks:
   * (For time scale charts only) Select your desired **Minor unit** from the menu.
   * Enter a **Minor step size**.
   * Select your desired **Minor axis mark** (**Tick**, **Grid line**, **Both**) from the menu.

By default, for time axes, if the major step size is larger than one, the minor axis mark size will be set to 1 of the major unit. If the major step size is smaller than one, the minor axis mark unit will be set to one unit smaller than the major axis mark unit (e.g. a major axis unit of **Year** will result in a default minor unit of **Month**).

For linear axes, there will be approximately 4 minor axis marks per major axis mark by default.

6. To revert back to default axis mark settings, select **Reset to default**. This will remove all axis marks.

Updated about 11 hours ago

---

[Format chart axis position](/docs/format-chart-axis-position)[Display chart reference marks](/docs/display-chart-reference-marks)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Configure chart axis marks](#configure-chart-axis-marks)