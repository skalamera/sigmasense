# Lesson three: Grouped tables and pivot tables

# Lesson three: Grouped tables and pivot tables

Welcome to lesson three: Grouped tables and pivot tables.

In the last lesson, we manipulated and transformed a table at the column level, preparing fields so that they use the correct data type and format for later use in our calculations.

Now, we’ll work with grouped tables to explore our data, as well as pivot tables to present organized data to users. By the end of this lesson, we’ll have our raw data sectioned off from what will eventually be our dashboard.

This lesson covers the following Sigma features:

* Grouped tables
* Calculations in groupings
* Hierarchical groupings
* Duplicate elements
* Pivot tables
* Parent-child relationships

## Grouped tables

With our data organized and transformed, let’s turn our attention to exploration.

As an FAA analyst, we’ve been tasked with understanding trends in flight delay times and their potential sources. One way to investigate how delay time changes with other variables is to create groupings.

![The FLIGHTS table grouped by airline shows the total and average departure delay for each airline](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_1.png)

The transformations we did in the previous section were all done at the individual record level. This can be contrasted with groupings, which allow us to perform calculations for sets of records that share some set of characteristics. This allows us to compare groups of flights, to see if any of those characteristics impact delay times.

Groupings in Sigma can be created directly on tables. Let’s make a duplicate table to experiment with!

1. Open the **Flight Delay Times** workbook for editing.

![The FLIGHTS workbook draft opened. The workbook contains only the FLIGHTS table from the previous lesson](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_2.png)

2. At the bottom of your workbook, double click on the tab that says `Page 1`. This will allow you to edit the title of the page. Change it to `Raw Data` and press enter to finish renaming the page.
3. Next to your **Raw Data** page, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg) **Add page** to add a new page.
4. Rename this page `Grouped Data`

You now have two pages in your workbook to place elements on. Let’s add a table element to our **Grouped Data** page so we can start experimenting.

5. Back on the **Raw Data** page, select the **FLIGHTS** table element, and open the element menu. Select **Duplicate**.

![In the element menu for the FLIGHTS table, a user hovers over the Duplicate option](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_3.png)

You now have two identical table elements on your **Raw Data** page.

Notice that this table element is a true duplicate of our first table. It has all the changes we made in the previous lesson. After the duplicate is created, though, changes made to the original don’t appear in the copy. It’s important to note the difference between duplicates and child elements, which is discussed in more detail later in this lesson.

6. Select the duplicate **FLIGHTS** table, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) to open the element menu, and select **Move to** > **Grouped Data**.

![In the element menu for the duplicate FLIGHTS table, a user hovers over the  Move to option](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_4.png)

This immediately moves the element to the **Grouped Data** page. Notice as well that Sigma automatically navigates us to that page.

7. Rename the table so that we can identify it more easily. Double click the title and rename it `FLIGHTS - GROUPED` so that your **Grouped Data** page looks like this:

![The FLIGHTS - GROUPED table on the new Grouped Data page](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_5.png)

Now we can begin grouping.

8. Select the **FLIGHTS - GROUPED** table.
9. In the editor panel, under the **Groupings** section, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg) **Add grouping…**

![Under groupings, a user hovers over the Add grouping option](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_6.png)

10. From this menu, select `Airline`.

![A user selects Airline from a list of columns for the grouping](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_7.png)

Our table now shows a new section on the left-hand side, titled `Airline`. It’s separated from the rest of the table by a vertical gray bar. This is a grouping, and the vertical gray is the visual indication that separates groupings.

![The FLIGHTS - GROUPED table shows a separation between the grouping (Airline) and the records the fall under that grouping](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_8.png)

11. Click the minus icon next to `Airline` to collapse the grouping. The table now shows only the groupings, rather than individual records.

![The FLIGHTS - GROUPED table with the groupings collapsed shows a line for each Airline ](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_9.png)

Every record has been organized according to its value in the `Airline` field. There are 14 groups, and each of our 5.8 million records belongs to one of them. We can expand individual groups with the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg) for that airline, or expand all groups again with the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg) at the top of the field.

When our groupings are collapsed, the rest of our fields are blank. This is because the rest of our fields are not grouped - they contain record-level information. Because no single record could represent the entire group, they remain blank unless the group is expanded and all records are made visible again. In the screenshot below, the expanded grouping for the Airline HA shows record-level information for that group.

![When the grouping for the airline HA is opened, the individual flight records for HA are visible](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_10.png)

Now, let’s add information at the grouping level with a calculation.

1. In the **Groupings** section of the editor panel, under **Group By** **Airline,** click the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg) **Add calculation…** to add a calculation.

![In the Airline Grouping, a user selects Add calculation](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_11.png)

The **Aggregate column** menu opens.

2. Select `Departure Delay`.

![A user selects Departure Delay as the aggregate column for the grouping calculation](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_12.png)

This action adds a calculation for the `Sum of Departure Delay`, like the screenshot below.

![With the groupings collapsed, the Sum of Departure Delay column shows the total departure delay for each airline](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_13.png)

We can now see the total minutes of departure delay for each airline.

Notice that the aggregate is treated like a new column, rather than a transformation of `Departure Delay`. Our table now has 30 columns instead of 29 listed under the summary, and the `Departure Delay` column still appears in our column list and table independently.

This is great, but single calculations like this don’t make for excellent data exploration. For example, airline `WN` has the greatest total departure delay, but that doesn’t tell us that they’re necessarily the most delayed airline. Perhaps they have ten times as many flights as any other airline, and their delay per flight is actually quite low. Currently, we can’t tell if that’s the case. Let’s add on another calculation to resolve this ambiguity.

3. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg) **Add calculation…** to add another calculation.
4. Select `Departure Delay` again.

This adds a second `Sum of Departure Delay` column to our grouping, like the below.

![A second calculated column shows the sum of departure delay](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_14.png)

5. Open the column menu for `Sum of Departure Delay (1)`, navigate to **Set aggregate** and select **Avg**.

![In the column menu for the second calculation, a user selects Avg from the set aggregate menu](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_15.png)

Now, the grouping shows two calculations - `Sum of Departure Delay` and `Avg of Departure Delay` for each airline. We can see now that the airline `NK` has the highest average departure delay.

![After selecting Avg, the second calculated column shows the Average of departure delay for each airline](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_1.png)
> 💡
>
> #### Customizing calculations
>
> You’ve used two of the default aggregates available for columns with number data - sum and avg. But, what if you want to customize your calculations? For greater control, consider combining calculations with filters or writing custom formulas.
>
> Filters can be used to perform calculations on a subset of records. For example, if you wanted to see the sum and avg of departure delay for only flights that were delayed, you could set a filter on our table for flights where departure delay is greater than zero. This would filter out flights that left on time before performing any calculations.
>
> Formulas allow you to perform custom calculations. For example, if you want to see the avg departure delay expressed in seconds rather than minutes, you could edit the formula for the `Avg([Departure Delay])` calculation in the formula bar. Changing the formula to `Avg([Departure Delay]) * 60` would return the departure delay in seconds.

## Multiple Groupings

Our exploration of the differences between airlines is getting interesting. Based on these two calculations, there seems to be serious variation in departure delay based on the airline. `HA` and `AS` are almost always on time, while `NK` and `UA` are delayed about 15 minutes on average.

At a glance, we might suspect this has something to do with the total volume of flights each airline serves. Perhaps smaller airlines like `HA` can keep flights on time because they have fewer flights to coordinate. Let’s add more groupings to investigate this hypothesis more closely.

1. Add a calculation to the `Airline` grouping using the column `Flight Number` and **Set aggregate** to **Count**.

This adds a third calculation column for the number of flights each airline conducted in 2015.

2. Sort the new `Count of Flight Number` column in descending order.

![The FLIGHTS - GROUPED table is sorted by the count of flights in descending order](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_16.png)

With our groupings organized this way, it doesn’t seem that there’s a strong relationship between flight volume and delay time. Some smaller airlines like `NK` and `F9` have long delays, and some of the larger airlines like `DL` and `OO` have relatively average delays.

Keep this in mind for when we make our dashboard later. We need tools for a more robust exploration of factors that contribute to the variance between airlines.

Imagine now that one of your managers offers you a lead based on their industry knowledge. They suggest you view the variation by day of the week for each airline as well, since they know anecdotally that flight delay times vary depending on the day of the week.

In other words, they’re suggesting you place a grouping for the day of the week within the `Airline` grouping.

3. Add another grouping by clicking **Add grouping…** in the editor panel.

![Above the Airline grouping, a user selects Add grouping](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_17.png)

4. Select `Day of Week` as the column.

The editor panel now shows two groupings.

![The Groupings sections shows two groupings for the table](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_18.png)

The table also shows two groupings, separated by an additional set of gray bars.

![The new grouping is divided from the previous grouping and the rest of the table by thicker vertical gray bars](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_19.png)

5. In the `Day of Week` grouping, add a calculation for the `Avg of Departure Delay`.

Because there is already a column titled `Avg of Departure Delay` in our first grouping, Sigma titles this one `Avg of Departure Delay (1)`.

![The Avg of Departure Delay calculation shows a (1) indicating it it is a duplicate in name with a column from the other grouping](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_20.png)

6. Rename `Avg of Departure Delay (1)` to `Avg of Departure Delay by Day of Week`.
7. Then, expand the groupings for `Airline`. Your table might look like the screenshot below.

![When the airline grouping is expanded, the Day of Week grouping shows calculations for each day of the week per airline](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_21.png)
> 📘
>
> In this dataset, `1` indicates Monday and `7` indicates Sunday.

With our highest grouping level (`Airline`) expanded, we can see the calculation values for each entry in our second grouping level (`Day of Week`). If we scroll down through the table, we can see that there’s more consistent variation by the `Day of Week` than there was for `Airline`.

> 💡
>
> #### Does it make sense to transform Day of Week?
>
> Reading a `Day of Week` value as a number can be unintuitive for end users. Does that mean we should transform it now? We could certainly create a calculated column and write an [**If**](/docs/if) statement in the formula bar that converts each value to the corresponding day as text data - 1 as Mon, 2 as Tues, etc.
>
> Though transforming this data might make it more legible, it might also make it harder to work with. For example, if we want to make a chart with `Day of Week` on the x-axis, number data allows us to easily sort the days in order from 1 to 7, which is more difficult with text data.

8. Remove the **Sort descending** from `Count of Flight Number` and apply a **Sort descending** to `Avg of Departure Delay by Day of Week`. This sorts the `Day of Week` values by this calculation within each `Airline`.

![The table is sorted in descending order by the average departure delay for each day of the week. The sort goes highest to lowest for each airline](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_22.png)

9. Scroll through the sorted grouping, and notice that Monday (1) ranks consistently among the days with the most delay, regardless of `Airline`.

Having done this simple exploration, we can begin to make some plans for our future dashboard:

* **Airline** - We know that the delay time changes by Airline, but we don’t quite yet understand why. Let’s plan to make a chart for our Airline delay data, and allow users to change various filters to see how they impact delays for each airline.
* **Day of Week** - We’ve observed a trend with Day of Week, where Monday has the greatest delay. Perhaps there’s more to learn here about how time impacts delays.

10. Click **Publish** to save your work to the published version.

## Pivot Tables

In the last section, we saw that there’s a relationship between flight delay time and day of the week that may need more exploration. In our imagined role as an analyst, we might realize that the variation among days of the week isn’t likely to change based on the airline, but it might change depending on the time of year. For example, a Monday like Labor Day might be even more delayed than other Mondays.

In this section, let’s place a pivot table onto the workbook to explore this two-dimensional relationship visually.

1. Add a new page to your workbook and call it `Dashboard`.
2. Back on the **Raw Data** page, select the **FLIGHTS** table, and select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add-dependent.svg) Create a child element.

![A user selects Create child element from the element menu](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_23.png)

3. Select **Pivot table**.

![A user selects pivot table from the child element menu](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_24.png)

This creates a pivot table titled **New Pivot Table**.

4. Select **New Pivot Table**, and then select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**. Select **Move to** and then **Dashboard**.

![A user selects the Move to option for the New Pivot Table and moves it to the Dashboard page](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_25.png)

This adds the pivot table to the **Dashboard** page.

Notice that the editor panel shows the **FLIGHTS** table as its data source. This is because **New Pivot Table** is a child element of the **FLIGHTS** table.

![In the editor panel, under Data Source, the FLIGHTS table is listed](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_26.png)

Child elements are distinct from duplicate elements and have some unique features that we can cover in a moment. First, let’s configure our pivot table to show delay time averages for each day of the week over the course of the year.

5. In the editor panel, drag `Day of Week` to the **Pivot columns** section, and `Scheduled Departure DateTime` to the **Pivot Rows** section.

![Day of Scheduled Departure Date is shown under Pivot Rows, and Day of Week under Pivot columns](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_27.png)

By default, `Scheduled Departure DateTime` is truncated to the `Day`. Scroll through the pivot table to see that there is one row for each day of the year.

We want this pivot table to give a high-level overview, so this view is too detailed. To fix this, let’s change the date truncation.

6. Open the column menu for `Day of Scheduled Departure DateTime`, select **Truncate date**, and select **Month**.

![A user selects Date of Scheduled Departure Date, and then chooses Month from the Truncate date option](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_28.png)

The pivot table rows now show a row for each month.

![A pivot table has 13 rows, one for each month January 2015 to January 2016](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_29.png)

Before we populate the pivot with values for each cell, notice that there is a row for 2016-01, meaning that some number of records in our original table are actually from January of 2016. Our goal is to make a dashboard for 2015, so we don’t want to see these records in our dashboard. To address this, we’ll leverage the parent-child element relationship in Sigma to remove these records from all our future dashboard elements.

1. Navigate to the **Raw Data** page, and select the **FLIGHTS** table.
2. Open the **Filters & controls** menu and select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg) **Add filter…**

![Under filters and controls, a user selects Add filter](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_30.png)

3. Select the `Scheduled Departure DateTime` column. Set a date range filter for the dates `Between` `Jan 1, 2015` and `Dec 31, 2015`.

![A user selects Jan 1 2015 to Dec 31 2015 as the range for a date filter](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_31.png)

4. Navigate back to the **Dashboard** page. When the pivot table refreshes, there is no longer a row for `2016-01`.

Here, we’ve demonstrated a foundational use case for tying child elements to a parent element in Sigma. A change made by a filter on our parent table (**FLIGHTS**) is reflected in the child element (**New Pivot Table**). This is different from a duplicate element, which does not inherit new changes after it’s created.

> 💡
>
> #### Parent tables and global filters
>
> Filtering a parent table applies the filter to all its child elements. For this reason, Sigma recommends building dashboard elements off of a parent table, so that you can apply global filters from a single location.
>
> For the rest of this course, create charts and other elements as children of this **FLIGHTS** table so that you can apply global filters and other changes as needed.

With the 2016 records filtered out, let’s finish configuring our pivot table.

1. On the **Dashboard** page, select the **New Pivot Table** element.
2. In the editor panel, drag the `Departure Delay` column to the **Values** section.
3. Change the aggregate from `Sum of Departure Delay` to `Avg of Departure Delay`.

![The pivot table shows an average departure delay for each month and day of the week](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_32.png)

Our pivot values now populate correctly. Each cell shows the average number of minutes a flight was delayed in the corresponding month and day of the week. But, the trends aren’t as obvious as they could be. Let’s use some formatting to make the changes more visually obvious to ourselves and future users.

4. Rename the pivot table to **Departure Delay by Month and Day of the Week**.
5. In the editor panel, select **Format** > **Conditional Formatting**.

![In the Format panel, a user selects Conditional formatting](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_33.png)

6. Under **Apply to**, select **Avg of Departure Delay**.
7. Select **Color Scale**.

![In the conditional formatting options, the color scale tab shows options for how to configure the color scale on a pivot table](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_34.png)

Our pivot table now works as a basic heatmap, using darker colors to indicate higher delay times and lighter colors to indicate lower delay times. It’s now even easier to see that delay times are worst in the beginning of the week, and in the summer months of June and July.

![Following the conditional formatting, the longer departure delays are highlighted darker, and shorter delays are lighter in the pivot table](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L3/L3_35.png)

8. Click **Publish** to save your work to the published version.

## Conclusion

At the end of lesson three, we’ve started to explore our data for trends. We’ve placed our first element on our dashboard page, and used it to demonstrate one of our findings visually. To do that, we learned about the following:

* Grouped tables
* Calculations in groupings
* Hierarchical groupings
* Duplicate elements
* Pivot tables
* Parent-child relationships

Updated 3 days ago

---

[Lesson two: Working with data tables](/docs/lesson-two-working-with-data-tables)[Lesson four: Charts and visualizations](/docs/lesson-four-charts-and-visualizations)

* [Table of Contents](#)
* + [Grouped tables](#grouped-tables)
  + [Multiple Groupings](#multiple-groupings)
  + [Pivot Tables](#pivot-tables)
  + [Conclusion](#conclusion)