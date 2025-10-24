# Lesson four: Charts and visualizations

# Lesson four: Charts and visualizations

Welcome to lesson four: Charts and visualizations.

In the last lesson, we familiarized ourselves with our data by using groupings. Then, we added the first element to our dashboard: a formatted pivot table that functions like a heatmap. Additionally, we learned the difference between duplicate elements and child elements, and began leveraging the parent-child relationship to simplify our development process.

Now, we’ll expand our dashboard with additional charts and visualizations. By the end of this lesson, we’ll have a draft dashboard with several visualizations. We’ll also learn more strategies for leveraging the parent-child relationship by discussing lineage.

This lesson covers the following Sigma features:

* Bar charts
* Line charts
* KPI elements
* Donut hole charts
* Workbook lineage
* Hiding workbook pages

## Basic chart elements

With our parent table transformed and separated onto its own page, let’s begin building charts by adding a bar chart, a line chart, and a pair of KPIs. Our manager has asked us to expand our analysis to include arrival delay as well as departure delay, so we’ll be charting both of them on this page as we go.

1. Navigate to the **Raw Data** page.
2. Select the **FLIGHTS** table, and select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add-dependent.svg) **Create child element** > **Chart**.

![A user opens the create child element menu](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_1.png)

By default, Sigma creates a bar chart element on the current page. Let's bring it to the Dashboard page.

3. Select the new bar chart and click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**. Select **Move to** > **Dashboard**.

![In the element menu, a user selects Dashboard from the Move to options](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_2.png)

Over on the **Dashboard** page, notice that the editor panel for our chart has new options. We can configure a **Data source**, **Chart type**, orientation, axes, and more.

![The editor panel for a bar chart shows options for customizing the chart under Properties](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_3.png)

Bar charts are excellent for making comparisons between categories, so let’s configure this one to show differences between departure delay and arrival delay by airline. Because we want to easily compare categories across these two columns, we’ll create a bar chart with no stacking, and set our aggregates to the average of each delay. Removing stacking will make the comparisons between airlines visually clear, and setting our aggregate to average helps us make a consistent comparison across airlines with different flight volumes.

> 💡
>
> #### When should I use one chart type instead of another?
>
> Choosing an appropriate chart type is critical for creating legible, accessible dashboards. Some chart types make a specific type of comparison easier to see than other chart types do.
>
> For example, if you want to quickly compare five sales regions to see which had the most sales, a bar chart is a great option. To identify the region with the highest sales, you just have to find the tallest bar.
>
> By contrast, if you want to understand changes in sales by region over time, a line chart may be a better option. With time on the x-axis, you can plot a line for each region. At any particular point in time, you can then easily see which region had the most sales and how it changed.

Let’s configure the bar chart.

1. Drag the `Airline` column to the **X-axis** section, and then drag `Departure Delay` and `Arrival Delay` to the **Y-axis** section.

![The Airline column is under the X-axis section, and the Y-axis section contains Sum of Departure Delay and Sum of Arrival Delay](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_4.png)

This creates a stacked bar chart with the sums of `Departure Delay` and `Arrival Delay`

2. Change the aggregate for `Departure Delay` and `Arrival Delay` to **Avg**.
3. In the **Chart type** section, select the icon for **No Stacking**.

![Under Chart type, the No stacking icon is selected](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_5.png)

4. Double click the name of the chart to rename it. Enter `Average of Departure and Arrival Delay by Airline`.

![The bar chart Average of Departure and Arrival Delay shows blue bars for Departure Delay and Yellow for Arrival Delay](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_6.png)

We now have a bar chart that can be used to quickly compare delays for each airline. We can quickly see that `AS`, `DL`, and `HA` have the least arrival delay, and that `NK` has the most. We can see that `DL` starts with a relatively average departure delay, but makes it up by arrival time. We can also see that arrival delay is generally lower than departure delay.

Having completed our first chart, we’re asked to make another chart comparing the two delay types over the course of the year. A line chart is suitable for the use case.

1. Return to the **Raw Data** page, and create another child chart element. Move it to the **Dashboard** page.
2. Change the **Chart type** to **Line chart**.

![The settings for a line chart show options fort x-axis, y-axis, and more](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_7.png)

3. Drag the `Departure Delay` and `Arrival Delay` columns to the **Y-axis** section. Set both of their aggregates to **Avg**.
4. Drag `Scheduled Departure DateTime` to the **X-axis** section. By default, the date is truncated to `Day of Scheduled Departure DateTime`, creating a highly detailed line chart.

![A line chart shows an overly detailed graph of daily data Average departure delay in blue and Average arrival delay in yellow](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_8.png)

This is a more detailed chart than we need. Our goal is to understand trends over the course of the year, and by charting the x-axis down to individual days, we introduce a significant amount of noise. The chart is spiky and erratic, reflecting the variation based on day of the week we observed in the previous lesson.

Thankfully, our work in lesson two preparing our datetime data can help solve the problem. Recall that we spent a significant amount of time in that lesson combining year, month, day, and time data into one column with the date data type. This transformation to date data gave us access to the default functionality for dates, like charting it along the x-axis as a time dimension.

Let’s adjust the chart to make the yearly trend easier to analyze.

5. In the **X-axis** section, open the menu for the `Day of Scheduled Departure DateTime` column. Select **Truncate Date** > **Week**.

![In the options for Day of Scheduled Departure Delay, a user selects Week from the Truncate date options](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_9.png)

Sigma automatically adjusts the line to plot points by week instead of by day.

![A smoother line chart plots delay for each week, with a blue line for departure delay and a yellow line for arrival delay](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_10.png)

6. Rename the chart `Average Departure and Arrival Delay by Week`.

We can now see a couple of trends more clearly.

* First, we can see that time of year impacts delay times. Delay times spike around holidays at the end of the calendar year, and they are also elevated for the entire summer.
* Additionally, we can see that arrival delay remains lower than departure delay for the entire year, which might be of interest to us later.

To round out this section, let’s use a pair of KPI elements to make this fact clear to users as soon as they open the dashboard.

1. Return to the **Raw Data** page.
2. Create two new child chart elements from the **FLIGHTS** table, and move them both to the **Dashboard** page.
3. Change the **Chart type** for both of these new elements to **KPI**.

![From the chart type options, a user hovers over the KPI chart type](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_11.png)

4. For one, drag `Departure Delay` to the **Value** section and change the aggregate to **Avg**.
5. For the other, drag `Arrival Delay` to the **Value** section and change the aggregate to **Avg**.

![A KPI shows that the average arrival delay is 4.39 minutes](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_12.png)

6. Rename them `Average Departure Delay in Minutes` and `Average Arrival Delay in Minutes` respectively.
7. Spend a few moments reorganizing the dashboard page by resizing and rearranging elements.

![The dashboard page is reorganized so that the KPIs and bar chart take up the top left quadrant, the line chart takes the top right quadrant, and the heatmap pivot table spans the bottom](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_13.png)

8. Click **Publish** to save your work to the published version.

## Review chart sources in workbook lineage

So far, all of our dashboard elements have shared one source. They have all been created directly from a single parent element: the **FLIGHTS** table. To confirm this, and see it represented visually, we can use Sigma’s lineage feature.

1. Click the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/lineage-outline.svg) **Lineage** in the bottom-right corner of the workbook.

![A user hovers over the Lineage icon in the workbook footer](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_14.png)

This opens the workbook lineage, where element relationships are displayed in a directed acyclic graph (DAG).

![A directed acyclic graph shows the connection to the FLIGHTS table as the source for two table elements. The FLIGHTS table element is the source for five charts](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_15.png)

The chart is read from left to right. Sources, like the **FLIGHTS** table in the Sigma Sample Database Snowflake connection, appear on the left-most edge of the chart. Dotted lines flow downstream (to the right) to elements that inherit data.

As an example, we can trace that the lineage for the line chart `Average Departure and Arrival Delay by Week` starts at the Sigma Sample Database **FLIGHTS** table, then moves downstream to the **FLIGHTS** table element on the **Raw Data** page, and terminates at the line chart `Average Departure and Arrival Delay by Week`.

In this section, let's add another layer to this lineage, and use this chart to verify that we’ve configured our elements correctly.

1. Return to the **Dashboard** page.

So far, all of our dashboard elements are focused on departure delay and arrival delay across all flights in 2015. It’s appropriate for them to share the same parent dataset, since they all visualize trends within that dataset.

Imagine we’ve been asked, however, to deepen our analysis of arrival delay by analyzing its root causes. Let’s return to our parent table to learn about some information we could use for this analysis.

2. Navigate to the **Raw Data** page, and create a child element table.
3. Rename it **FLIGHTS - Delay Breakdown**.

![On the same dashboard page, the FLIGHTS table and the FLIGHTS - Delay Breakdown table are shown](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_16.png)

4. Scroll over to the last handful of columns in the new **FLIGHTS - Delay Breakdown** child table.

![In the last five columns of the FLIGHTS - Delay Breakdown table, records are either entirely null, or contain values adding up to 15 or more across the 5 columns](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_17.png)

These five columns - `Air System Delay`, `Security Delay`, `Airline Delay`, `Late Aircraft Delay`, and `Weather Delay` - are the component parts of `Arrival Delay` for flights that arrived 15 minutes late or more.

For example, a flight with an `Arrival Delay` value of `15` minutes might have the following values for these five columns:

* `Air System Delay` - `7`
* `Security Delay` - `2`
* `Airline Delay` - `3`
* `Late Aircraft Delay` - `3`
* `Weather Delay` - `0`

These all add to the total `Arrival Delay` value of `15`. In other words, they can tell us why a flight was delayed.

Note the following:

* Any flight with less than 15 minutes of Arrival Delay has null values for all five of these columns.
* Cancelled flights have null values for all five of these columns.
* Diverted flights have null values for all five of these columns.

If you were doing discovery on this dataset independently, then you might want to verify which records have null values, and under what circumstances. You could confirm this by configuring filters on the **FLIGHTS - Delay Breakdown** table.

![In the Filters and controls menu for the FLIGHTS - Delay Breakdown table, a user selects the Add filter option](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_18.png)

5. Using the **Add filter…** option, create filters for `Arrival Delay`, `Cancelled`, `Diverted`, and `Air System Delay`. Alternatively, create them from the column menu for each field.
6. Change the **Filter type** for `Air System Delay` to **List**.

![Four filters are shown in the Filters and controls menu. A number range for Arrival Delay, and List values filters for Cancelled, Diverted, and Air System Delay](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_19.png)

7. In the **Arrival Delay** filter, set the min value to `15`.
8. In the **Cancelled** filter, select `False` only.
9. In the **Diverted** filter, select `False` only.

![In the filters and controls menu, Arrival Delay is filtered to entries 15 or greater, Cancelled is filtered to False only, Diverted to False only, and Air System Delay is left blank](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_20.png)

10. Open the **Air System Delay** list filter, and confirm that there are no records with a null value.

![A user opens the Air System Delay list values filter. There are no null values](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_21.png)

Using these filters, we’ve now limited our results to 1,060,551 flights that arrived 15 minutes late or more. Each record in this table has a breakdown of that delay as well. Using this table, we can make a new chart that visualizes this information.

1. Create a child chart element from the **FLIGHTS - Delay Breakdown** table.
2. Move the new chart element to the **Dashboard** page.
3. Set the chart type to **Donut**.
4. In the **Value** section, add an average calculation for each of the five sources of delay. In the **Donut Hole Value** section, add a calculation for the average of **Arrival Delay**.

![In the Editor panel, a donut chart shows 5 column aggregates in the value section - the averages of Late Aircraft Delay, Airline Delay, Air System Delay, Weather Delay, and Security Delay](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_22.png)

5. Rename the chart `Average Arrival Delay by Delay Type`.

![A donut chart shows small wedges for Security Delay and Weather Delay, and larger wedges for Air System Delay, Airline Delay, and Late Aircraft Delay](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_23.png)

We can now see that the average arrival delay for these flights is 58.88 minutes - almost an hour - and that the majority of that delay comes from `Late Aircraft Delay` and `Airline Delay`.

6. Open the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/lineage-outline.svg) **Lineage** again.

![A user hovers over the Lineage icon in the workbook footer](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_14.png)

Our newest chart appears on the far right of the lineage, as the furthest downstream element. It is a child element of the **FLIGHTS - Delay Breakdown** table, which is a child element of the **FLIGHTS** table that the rest of our charts are built from.

![In the DAG chart, the donut chart is downstream of the FLIGHTS - Delay Breakdown table, which is downstream of the FLIGHTS table.](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_24.png)

Because the **FLIGHTS** table is still upstream of all charts, any changes we make to it - like new filters - are still universal. Changes we make to **FLIGHTS** are reflected in the child table **FLIGHTS - Delay Breakdown**, which are in turn be reflected in its child elements like the `Average Delay by Delay Type` donut chart.

However, we don’t have to apply filters to every element. When we want to filter only from flights that were delayed 15 minutes or more, we can now filter **FLIGHTS - Delay Breakdown**.

> 💡
>
> #### When should I split the workbook lineage like this?
>
> When deciding on data sources for the elements in a workbook, less is more. If you can achieve the same functionality with fewer data sources, the workbook is easier to manage than one with more data sources.
>
> For example, if you were constructing a sales dashboard with one page on profit, one page on order volume, and one page on revenue by region, you could use the same data source for all of them. This is because you don’t need to filter the data source differently for each of these pages. They can all be derived from the same set of records.
>
> One key advantage of this is that, as you add more elements and interactions, you don’t have to track or maintain the various filters that should apply to them. They can all be added to the parent data source.
>
> Only split the lineage when there’s a significant group of elements that must reference a logically separate set of records.

7. Click **Publish** save your work to the published version.

## Organization

Before concluding this lesson, let’s briefly organize our workbook pages by topic, and hide our raw data from end users to make the workbook more legible. In a future lesson, we’ll take a closer look at organization and style.

1. Rename the **Dashboard** page to `Departure Delay vs Arrival Delay`.
2. Add a new page, and name it `Arrival Delay by Delay Type`.
3. Open the page menu for **Raw Data** and select **Hide page**.

![In the page menu for the Raw Data page, a user selects Hide page](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_25.png)

4. Hide the **Grouped Data** page as well, so that you have two hidden pages, and two named dashboard pages.

Hidden pages aren’t seen by the end users of the workbook. They’re useful for omitting unnecessary details for users that you still need as an editor. For more information on hidden pages, see [Manage workbook page visibility](/docs/manage-workbook-page-visibility#/).

![The workbook footer shows 2 hidden pages - Raw Data and Grouped Data - and 2 visible pages - Departure Delay vs Arrival Delay and Arrival Delay by Delay Type](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_26.png)

5. Move the donut chart **Average Arrival Delay by Delay Type** to the new **Arrival Delay by Delay Type** page.
6. Click **Publish** to save your work to the published version.

Now, let's view the published version of the workbook to see what our changes did for our users.

7. Open the workbook menu and select **Go to published version**.

You can now see what an end user would see: two published pages, one for each distinct set of records we’ve built chart elements from. Our data tables are hidden from the end user, directing their attention to the charts and visuals we’ve prepared for them.

![A user scrolls through the published version of the workbook so far. Only two pages are visible - Departure Delay vs Arrival Delay and Arrival Delay by Delay Type](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L4/L4_27.gif)

## Conclusion

At the end of lesson four, we’ve made significant progress developing our dashboard by adding and configuring several chart elements built on appropriate parent data tables. To do that, we learned about the following:

* Bar charts
* Line charts
* KPI elements
* Donut hole charts
* Workbook lineage
* Hiding workbook pages

Updated 3 days ago

---

[Lesson three: Grouped tables and pivot tables](/docs/lesson-three-grouped-tables-and-pivot-tables)[Lesson five: Controls and actions](/docs/lesson-five-controls-and-actions)

* [Table of Contents](#)
* + [Basic chart elements](#basic-chart-elements)
  + [Review chart sources in workbook lineage](#review-chart-sources-in-workbook-lineage)
  + [Organization](#organization)
  + [Conclusion](#conclusion)