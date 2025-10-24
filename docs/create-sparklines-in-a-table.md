# Create sparklines in a table (Beta)

# Create sparklines in a table (Beta)

> 🚩
>
> This documentation describes one or more public beta features that are in development. Beta features are subject to quick, iterative changes; therefore the current user experience in the Sigma service can differ from the information provided in this page.
>
> This page should not be considered official published documentation until Sigma removes this notice and the beta flag on the corresponding feature(s) in the Sigma service. For the full beta feature disclaimer, see [Beta features](/docs/sigma-product-releases#beta-features).

Sigma supports creating sparklines, which are small charts within a single cell. These charts can help show data trends at a glance, and can be valuable for creating overviews of data. They may remove the need for many individual charts and can help save visual space in a workbook. For example, you may want to generate sparklines to show trends in sales performance or website traffic over time. The following table shows trends in departing flights from various airports:

![Chart with sparklines of flight departure patterns for different time intervals](https://files.readme.io/dc2652fe68d5871cc8aea21792f216db616f68a618820f2797e988d242c6a18c-coverimage_sparklines.png)

This document covers how to [add](/docs/create-sparklines-in-a-table#add-sparklines), [format](/docs/create-sparklines-in-a-table#format-sparklines), [investigate the data in](/docs/create-sparklines-in-a-table#investigate-sparkline-data), and [export sparklines](/docs/create-sparklines-in-a-table#export-tables-with-sparklines). It also covers an [example use case for creating sparklines](/docs/create-sparklines-in-a-table#example-showcasing-popular-us-baby-name-trends-and-distributions-over-time).

## User requirements

* To create sparklines, you must have **Can Edit** or **Can Explore** [access](/docs/folder-and-document-permissions) to an individual workbook.
* The workbook must be in either **Edit** mode or **Explore** mode. See [Workbook modes overview](/docs/workbook-modes-overview).

## Add sparklines

> 📘
>
> ### Currently, Sigma only supports creating sparklines in tables and pivot tables. To create a sparkline for an input table, create a child table from your input table element.

How to add sparklines depends on how your data is formatted:

* If your data is JSON data in an `x`, `y` format (e.g. `{"x":"2025", "y":"123456"}`), add a new column in your desired table and use the Sparkline function. See [Sparkline](/docs/sparkline) for more information.

> 👍
>
> ### The key-value pairs must be labelled as `x` and `y`. Other labels are not compatible with the Sparkline function.

* If your data is not JSON or not in an `x`, `y` format, there are two methods you can use to add sparklines:
  + Create a new column in your desired table and use the SparklineAgg function. See [SparklineAgg](/docs/sparklineagg) for more information.
  + Add sparklines from a table in a workbook.

To add sparklines from a table:

1. Add a grouping to your table. Under **Groupings**, select **+ Add grouping...**, then select the column you want to group by.  
   Groupings are necessary for sparklines as multiple values are needed to create a meaningful sparkline. For more information on groupings, see [Group columns in a table](/docs/create-and-manage-tables#group-columns-in-a-table).
2. From the column you wish you create a sparkline for, select the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)). Hover over **Add column via**, then select **Sparkline**.
3. Configure your sparkline in the modal that appears:
   1. Select an **X-Axis** column from the dropdown. This is usually a time-based column, but can also be another numeric or text column.
   2. Select a **Y-Axis** column from the dropdown.
   3. Select an aggregation method from the **Aggregate** dropdown. The available options vary based on the data types you select for your axes.
   4. Select **Done**.

> 📘
>
> ### For sparklines in pivot tables, all cells within a pivot table column will share the same axes for easier comparison.

## Format sparklines

You can change sparkline chart type, color, interpolation method, stroke and point style/width, and more. To format sparklines:

1. Select the table with the sparklines you want to format.
2. In the editor panel, select Format, then select Sparkline.
3. From the dropdown, select which sparklines you want to apply formatting changes to:

   * Select **Apply to all sparklines** to apply your formatting changes to every sparkline in that table.
   * Select the name of a specific column to apply formatting changes to only that column.
4. Select your desired sparkline chart type (**Auto**, **Line** or **Bar**):

   * **Auto**: (Available if you selected **Apply to all sparklines**) This automatically assigns chart type based on the x-axis of your chart (line charts are used for time-based and numeric axes and bar charts for categorical x-axes).
   * **Line**: Formats sparklines as line charts.
   * **Bar**: Formats sparklines as bar charts.
5. For line charts, configure your desired formatting options:

   * **Color**: Select a color for your sparklines using the color picker, color wheel, or from the provided color palette.
   * **Interpolation**: Select how you want the lines between your data to be interpolated.
   * **Stroke style**: Select a **Solid**, **Dashed**, or **Dotted** stroke style.
   * **Stroke width**: Select your desired stroke pixel width.
   * **Null data**: Select if you want null data to be interpolated, hidden, or represented by zeroes.
   * Turn the **Show points** toggle on or off. If you choose to show points, configure the available options:
     + **Point shape**: Select **Circle**, **Square**, **Cross**, **Diamond** or **Triangle**.
     + **Point size**: Select your desired point pixel width.

   To clear previously selected options, select **Revert to default**.

## Investigate sparkline data

You can see a more detailed view of the data in each sparkline:

1. Double-click the cell with the sparkline, or right-click the cell and select **Show value**.
2. Select your preferred view:
   * **Tree view**: Select the caret by a specific index to view its `x`, `y` values.
   * **Raw text**: See an expanded list of all `x`, `y` values for that sparkline.

## Example: Showcasing popular US baby name trends and distributions over time

A table, **US\_Name\_Trends**, contains information about historical U.S. baby name trends, including columns such as:

* *State ID*: The abbreviated name of a U.S. state
* *Year*
* *Name*: A specific baby name
* *Namecount*: The number of babies born in a specific state, in a specific year, with that specific baby name
* *Gender*: Baby names classified into either F or M

To get a table with sparklines showcasing the top three most popular baby names for each gender and how they changed from year to year:

1. Group the table by *Gender*. Select **+ Add grouping**, then search for and select **Gender**.
2. Group the table by *Name*. Select **+ Add grouping**, then search for and select **Name**.
3. From the *Name* column, select the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) in the column header, then hover over **Add column via**, then select **Sparkline**
4. In the sparkline modal, configure the following:
   * **X-axis**: **Year**
   * **Y-axis**: **Namecount**
   * **Aggregate**: **Sum**  
     Select **Done**.
5. Double-click on the name of the sparkline column and rename it as **Trend over time**.
6. From the *Name* column, select the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)), then select **Add new column.** In the formula bar, enter: `Sum([Namecount])`.
7. From the *Sum of Namecount* column, select the caret, then select **Filter**.
8. Select **More ⋮**, then **Change filter type**, then **Top N**.
9. Next to **Top N**, enter `3`.
10. Select **-** in the *Name* column to collapse the rows. Your table should look something like:

![](https://files.readme.io/12e137c21f8eec5c24464b56dff2d7eba0db6e820a072d48e3eb44a1a9dc2f94-name_trends_sparkline.png)

To get a view of the distribution of these 3 most popular names per gender over the states of California (CA), New York (NY) and Pennsylvania (PA):

1. Select **+** in the *Name* column to expand the rows.
2. From the *Name* column, select the caret in the column header, then hover over **Add column via**, then select **Sparkline**.
3. In the sparkline modal, configure the following:
   * **X-axis**: **State Id**
   * **Y-axis**: **Namecount**
   * **Aggregate**: **Sum**
4. Select **Done**.
5. From the *State Id* column, select **Filter**. Search for and select **CA**, **NY** and **PA**. Your table should look something like:

![](https://files.readme.io/16e94ac4fdfbd08187e8a6c0b563b87024cf4e1b85d2e47b96f680c0fba42ae4-bar_chart_sparkline.png)

## Export tables with sparklines

To export or download tables with sparklines, see [Send or schedule workbook exports](/docs/send-or-schedule-workbook-exports).

Updated 3 days ago

---

[Maps](/docs/maps)[Customize a chart](/docs/customize-a-chart)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Add sparklines](#add-sparklines)
  + [Format sparklines](#format-sparklines)
  + [Investigate sparkline data](#investigate-sparkline-data)
  + [Example: Showcasing popular US baby name trends and distributions over time](#example-showcasing-popular-us-baby-name-trends-and-distributions-over-time)
  + [Export tables with sparklines](#export-tables-with-sparklines)