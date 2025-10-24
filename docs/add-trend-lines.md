# Add trend lines

# Add trend lines

Trend lines are lines added to charts to highlight and predict patterns across multiple values in a set of data. For example, you may want to track your company's overall pace of revenue growth over the past 5 years.

This article describes how to add, edit, and delete trend lines in charts.

## User requirements

* To edit a chart, you must have **Can edit** or **Can explore** [access](/docs/folder-and-document-permissions#document-permissions) to the individual workbook.
* You must be in **Edit** or **Explore** mode for the workbook. See [workbook modes overview](/docs/workbook-modes-overview).

## Prerequisites

* The chart must have values plotted on both its **X-axis** and **Y-axis.** Both axes must also have a [compatible scale type](/docs/add-trend-lines#axis-scale-types) applied. The following scale types are compatible with trend lines: **Linear**, **Time**, **Log**, **Pow**, **Sqrt**.
* The chart must support trend lines. Trellised charts, stacked charts, and charts with values plotted on the **Color** field do not support trend lines.
* The column you want to use to calculate a trend should be plotted on the **Y-axis**.

## Trend line model types

The following model types are available: [**Linear**](/docs/add-trend-lines#h_01GGAQX1WPWZNF4JAFC0BQY1YZ), [**Logarithmic**](/docs/add-trend-lines#h_01GGAQX8E9WNZ0Q50ZC0ACRASY), [**Exponential**](/docs/add-trend-lines#h_01GGAQXE0969HKHYGXYDN2ZY8J), [**Power**](/docs/add-trend-lines#h_01GGAQXT9DDPR5TVSRDNN2N609), [**Quadratic**](/docs/add-trend-lines#h_01GGAQY80CBX9KY7NHRSRE2TZQ), and [**Polynomial**](/docs/add-trend-lines#h_01GGAQYKD8F2SKPXRHJBEM3TE0).

If you’re unsure which model type to choose, we recommend trying a few and picking the one that looks best with your data. A line’s [R² value](/docs/add-trend-lines#determine-best-fit-from-r²-values) can also help you determine best fit.

Each model type is based on an underlying linear regression formula. These formulas are included below. However, understanding the math behind the line is not necessary for using trend lines in Sigma.

|  |  |
| --- | --- |
| Linear Linear trend lines are used for data that follows a simple, steady, straight line. Data points may increase or decrease, but the trend remains steady.   **Formula**: Y = a + b \* X |  |
| Logarithmic Logarithmic trend lines are used for data sets in which the rate of change increases or decreases quickly before leveling out.   **Formula**: Y = a + b \* log(X) |  |
| Exponential Exponential trend lines are used for data sets in which the values rise or fall at constantly increasing rates.   Exponential trend lines don't recognize zeros or negative numbers.  **Formula**: Y = a \* e^(b \* X) |  |
| Power Power trend lines are used for data sets in which the values increase at a specific rate.   Power trend lines don't recognize zeros or negative numbers.  **Formula**: Y = a \* X^b |  |
| Polynomial Polynomial trend lines are used when data fluctuates. They're helpful when analyzing gains and losses over a large period of time.  Sigma's polynomial trend lines default to a polynomial order of 3 and support orders 3 - 7. **Polynomial order** refers to the number of coefficients applied. This effects how many hills or valleys are present in the line. The higher the number, the more hills or valleys to expect. Order 3 trends typically have one or two hills or valleys. Whereas order 2 trends would have only one hill or valley.   **Formula**: Y = a + b \* X + … + k \* X^3 |  |
| Quadratic Quadratic trend lines are 2nd-order polynomial trend lines. Much like Polynomial trend lines, they're used to smooth out fluctuations in a data set.   **Formula**: Y = a + b \* X + c \* X^2 |  |

## Determine best fit from R² values

R-squared (R²) represents how well the trend line fits the data. This is based on variance between data points.

R² values are always between 0 and 1. Values closer to 0 signal that the line fit is worse, while values closer to 1 signify a better fit.

To include the R² value on a chart's trend line, select the trend line's **Show value** option in the editor panel. The value will appear wherever the trend line label is positioned in relation to the line.

![](https://files.readme.io/3cc9d39707af415e384d7446c95cbbf5519f6b2ab728e5b1830df112cbc0fc54-trendline_8.png)

## **Add a trend line**

To add a trend line to a chart:

1. Select the chart.
2. In the editor panel, click **Format**.
3. Click **Trend lines** to expand the section.
4. Click **+Add new** .
5. Select **Trend line** to expand the section and begin configuring the trend line.
6. Under **Select column**, select a column to use for the trend line.

   The available list contains only columns plotted on the chart's **Y-axis**.

   ![Screenshot of the Trend lines select column section in the Format panel](https://files.readme.io/6b5feb70e4f667ff5e59025ddee37ca6b3720e809413bcc5349f8753ece748ec-trendline_5.png)
7. For **Model**, select a trend line [model type](/docs/add-trend-lines#trend-line-model-types):

   * **Linear**: display as a best-fit straight line
   * **Logarithmic**: used for data sets in which the rate of change increases or decreases quickly before leveling out
   * **Exponential**: used for data sets in which the values rise or fall at constantly increasing rates
   * **Power**: used for data sets in which the values increase at a specific rate.
   * **Polynomial**: used when data fluctuates. They're helpful when analyzing gains and losses over a large period of time. Sigma's polynomial trend lines default to a [polynomial order](/docs/add-trend-lines#polynomial) of 3. This value is configurable below.
   * **Quadratic**: 2nd-order polynomial trend lines used to smooth out fluctuations in a data set
8. (Optional) For Polynomial trend lines only, for **Degree**, select a polynomial order between 3 and 7.  
   Polynomial order changes how many hills or valleys are present in the line. The higher the number, the more hills or valleys to expect.
9. (Optional) Select the line style: **Solid**, **Dashed** or **Dotted**. Then select its size and color.
10. (Optional) To add a label to the trend line, select the checkbox for **Label text** and enter a label into the text box.
11. (Optional) Select where you want to position the label in relation to the line: **Top right**, **Top left**, **Top center**, **Bottom right**, **Bottom left**, **Bottom center**.
12. (Optional) To show the line's R² value, select **Show value**.  
    R² represents how well the trend line fits the data based on variance between data points.  
    ![Screenshot of the trend line's R-Squared value label](https://files.readme.io/e3bf9f65ab4021d148299837b486b752c5306d80a3cb432fc6593840e3ac02a8-trendline_8.png)

## Edit a trend line

To edit an existing trend line:

1. Select the desired chart and click **Format** in the editor panel.
2. Click **Trend lines** to expand the section.
3. Select the trend line you wish to edit.
4. Make any of the following edits:

   * To select a new column to use for the trend, pick a column under **Select column**.  
     The available list contains only columns plotted on the chart's **Y-axis**.
   * To change the line's [model type](/docs/add-trend-lines#trend-line-model-types), select a model type under **Model**.
   * (Optional) For Polynomial trend lines only, for **Degree**, select a polynomial order between 3 and 7.
   * Select the line style: **Solid**, **Dashed** or **Dotted**.
   * Select a new line size or color.
   * To add a text label, select the **Label text** checkbox and enter a label into the text box.  
     For no label, leave the text box blank or deselect **Label text**.
   * To position or reposition the label in relation to the line, select a position from the dropdown menu: **Top right**, **Top left**, **Top center**, **Bottom right**, **Bottom left**, **Bottom center**.
   * To show or hide the line's R² value, select or deselect **Show value**.  
     R² represents how well the trend line fits the data based on variance between data points.

## Delete a trend line

To delete a trend line:

1. Select the chart and click **Format** in the side panel.
2. Click **Trend lines** to expand the section.
3. Select the trend line you wish to edit.
4. In the bottom right corner of the trend line editor, click **Delete**.

## Axis scale types

A chart only supports trend lines if its columns are plotted on both its axes and if a trend line compatible scale type is applied. The following scale types are compatible with trend lines: **Linear**, **Time**, **Log**, **Pow**, **Sqrt**.

Charts that use an incompatible scale type display a warning message in the **Trend lines** section of the format panel. To clear this warning and add a trend line, check your axes’ scale types and update as appropriate.

To change an axis' scale type:

1. Select the chart and click **Format** in the side panel.
2. Click either **X-axis** or **Y-axis** to expand the appropriate section.
3. Select an option from the **Scale type** dropdown menu.  
   Not all charts support all scale types. The following scale types are compatible with trend lines:

   * **Linear**: Plots data along the axis using a linear numeric scale
   * **Time**: Plots data along the axis as time values
   * **Log**: Plots data along the axis using a logarithmic scale
   * **Pow**: Plots data along the axis using a power scale
   * **Sqrt**: Plots data along the axis using a square-root scale

Updated 3 days ago

---

Related resources

* [Intro to visualizations](/docs/intro-to-visualizations)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Prerequisites](#prerequisites)
  + [Trend line model types](#trend-line-model-types)
  + [Determine best fit from R² values](#determine-best-fit-from-r-values)
  + [Add a trend line](#add-a-trend-line)
  + [Edit a trend line](#edit-a-trend-line)
  + [Delete a trend line](#delete-a-trend-line)
  + [Axis scale types](#axis-scale-types)