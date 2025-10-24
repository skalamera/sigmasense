# Lesson five: Controls and actions

# Lesson five: Controls and actions

Welcome to lesson five: Controls and actions.

In the last lesson, we built our first charts and visualizations, and our dashboard began to take shape. We also learned more about lineage in Sigma to help simplify our development process.

Now, we’ll make our dashboard interactive for end users by configuring controls and actions. At the end of this lesson, our dashboard will have several customizable controls that filter our parent data table and update our visualizations.

This lesson covers the following Sigma features:

* Controls
* Converting filters to controls
* Placing filters on parent elements
* Actions
* Conditional actions

## Creating basic interaction with controls

[Controls](/docs/intro-to-control-elements) are Sigma elements that allow you to define specific interactions a user can have with your workbook. There are [many different types of controls](/docs/intro-to-control-elements#types-of-controls), each of which offers different functionality.

To start, let’s configure a few basic controls to let users filter data on the dashboard pages. We can use controls to filter our parent table, which updates the various child charts to show trends and totals for the filtered dataset. In the next lesson, we’ll expand on this by discussing user experience, and making it clear what filters are active when.

There are two main methods for creating a filter control:

* Creating a control from the **Add element** bar and targeting a table
* Creating a filter from the table and converting it to a page control

This lesson covers both of these methods.

Let’s start by creating a control from the **Add element** bar, and targeting our parent table.

1. Open your workbook for editing, and navigate to the **Departure Delay vs Arrival Delay** page.
2. In the **Add element bar**, select **Controls** > **Date range**.

![In the Add element bar, a user selects controls, and hovers over the Date range control option](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_1.png)

This creates a new date range control with default settings.

3. Select the date range control. It displays options for selecting a date range.

![A user opens a date range control, which shows options for a date range between July 24, 2025, and July 24, 2025](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_2.png)

4. Make a selection in the date range control.

Notice that no matter what we change about this control, nothing changes about our dashboard. This is because we haven’t configured the control to target any elements.

5. Clear the date range control.
6. In the editor panel, select **Targets (0)** and then ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg) **Add filter target**.

![In the editor panel, under Targets, a user selects Add filter target](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_3.png)

7. Select **Raw Data** > **FLIGHTS** and set the column to **Scheduled Departure DateTime**.

![In the Target options, a user selects the FLIGHTS table from the Raw Data page, and then selects the column Scheduled Departure DateTime](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_4.png)

8. In the control, set a date range between `07/01/2015` and `07/31/2015`.

All the elements on the workbook page update to only reflect data from flights that were scheduled to depart in July of 2015.

9. Clear the control, and the elements update to reflect data from the entire year again.

By configuring a target for our control, and selecting the `Scheduled Departure DateTime` column of our parent **FLIGHTS** table, we made it so that our control directly filters the parent table of all of our dashboard elements. By targeting the parent table, we can filter the data for all of our dashboard elements from just one control. This is another advantage of building our dashboard elements from one parent table.

Now, let’s look at an even easier way to configure a control that filters our parent table, by adding a filter to the table directly, and converting it to a page control.

1. Navigate to the **Raw Data** page.
2. Select the **FLIGHTS** table, and add a filter on the `Airline` column.

![In the Select column modal, a user selects the Airline column](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_5.png)

3. Select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** for the filter and click **Convert to page control**.

![In the Filters and controls menu, a user opens the options for the Airline filter, and selects Convert to page control](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_6.png)

This creates a list values control that targets the `Airline` column of the **FLIGHTS** table.

4. Select the **Airline** control, and click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Move to** > **Departure Delay vs Arrival Delay** to move it to a user-facing page.

We now have a second control that filters our parent table.

Because we created it as a filter on our parent table first, and then converted it to a page control, we didn’t have to configure the target like we did with the date range control.

> 💡
>
> #### When should I convert a filter to a page control?
>
> Every filter in Sigma corresponds to a particular type of control element, meaning we can convert any filter to a control. The filter converts to a control with one target on the table element it originated from. Additionally, a control created this way auto-populates control values based on the table, meaning less manual configuration is required for controls like value lists.
>
> This means that the convert to page control workflow is most useful when you need to quickly create several controls that target one table element. It’s less useful when the controls need to target several elements, as they still need to be manually configured.

To get more comfortable with this workflow for creating a control, let’s do it two more times to create filter controls for our Origin and Destination Airports.

1. Navigate to the **Raw Data** page.
2. Select the **FLIGHTS** table.
3. Add filters for both the `Origin Airport` and `Destination Airport` fields.

![In the Filters and controls menu, new filters appear for Origin Airport and Destination Airport](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_7.png)

4. For both filters, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** and select **Convert to page control**.

Both filters are converted to controls.

![On the workbook page, two list values controls, one for Origin Airport and one for Destination Airport](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_8.png)

5. For both controls, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Move to** > **Departure Delay vs Arrival Delay** to move them to a user-facing page.

![On the workbook page, 4 filter controls, for Origin Airport, Destination Airport, Scheduled Departure DateTime, and Airline](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_9.png)

We now have four filter controls on our dashboard page that target our parent element. When we share our final dashboard, users can make selections on these controls to filter the visualizations by Date, Airline, and Airport, while the raw data remains hidden. In this way, Sigma control elements allow you to determine the interaction a user has with your dashboard. You can choose more than just what data should appear in what charts, you can also choose how users interact with that data.

To finish this section, let’s quickly configure some settings for these four controls.

1. Select the **Scheduled Departure DateTime** control. Double click the label and rename it **Scheduled Departure Date**.
2. In the editor panel, update the **Control ID** to `control-departure-date`.

![The Control ID value is set to control-departure-date](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_10.png)

Control IDs are customizable unique identifiers for control elements. Later in this course, we’ll use control IDs to reference controls and their values in workbook actions. For now, we just need to write unique, standardized, sufficiently descriptive ID values for each control.

3. Select the **Airline** control.
4. In the editor panel, deselect the checkbox for **Show null option**. This removes the null option from the list of values the user can select from.
5. Set the **Control ID** value to `control-airline`.

![The Control ID value is set to control-airline](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_11.png)

6. Select the **Origin Airport** control.
7. In the editor panel, deselect the checkbox for **Show null option**. Set the **Control ID** value to `control-origin-airport`.
8. Select the **Destination Airport** control.
9. In the editor panel, deselect the checkbox for **Show null option**. Set the **Control ID** value to `control-destination-airport`.
10. Click **Publish** save your work to the published version.

## Controls, lineage, and user experience

In the last section, we leveraged our workbook lineage, as well as the convert to page control feature to quickly make controls out of several filters that targeted our parent table. Now, let’s create another filter control that targets a different point in our workbook lineage.

1. Navigate to the Raw Data page, and select the **FLIGHTS - Delay Breakdown** table.

Recall that this is a child table of our **FLIGHTS** table, but also the parent table for our donut chart element in the dashboard. This means that all the control elements we made in the previous section impact this table as well, since they target the upstream data source this table is based on.

Let’s make a control that targets just this table and its child elements, without impacting the parent **FLIGHTS** table.

Our manager has asked us to add a control that lets users filter flights in the delay breakdown based on their total arrival delay time. For example, this control would allow a user to filter for flights that were delayed by an hour or more, or between two hours and three hours, so that they can observe how the different delay root causes vary with total delay time.

2. Select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/filter.svg) **Filters & controls** for the **FLIGHTS - Delay Breakdown** table.

You might see four filters like below:

![In the filters and controls menu, there are 4 filters for Arrival Delay, Cancelled, Diverted, and Air System Delay](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_12.png)

3. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg) **Add filter…** and select **Arrival Delay** as the column.

Notice that nothing changed. Because we already have a filter on the `Arrival Delay` column, Sigma prevents us from adding a second. This has advantages and disadvantages:

* **Advantage** - This protects users from having an unintuitive experience with our dashboard. Having two filters on the same column can be unclear for end users, especially if one of the filters is on a table that they don’t have access to.
* **Disadvantage** - This seems to remove some agency from us as the dashboard creator. Perhaps we want to offer users a control to filter on this field, but we also want some assurance that the table will always be filtered properly, which seems to require two filters.

There is a way to circumvent this limitation. But before we do that, it’s worth pausing to consider why we want to. In this case, it’s because we want to retain a filter on our parent table while also offering a control on that same column to end users. They should never be able to view a flight with less than 15 minutes in `Arrival Delay`. Beyond that, however, they can filter however they want.

4. Navigate to the **Arrival Delay by Delay Type** page.
5. In the **Add element bar**, select **Controls** > **Range slider**.
6. Rename the control `Total Arrival Delay`.

![The Total Arrival Delay controls ranges from 0 to 100](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_13.png)

7. In the editor panel, under **Settings**, set a **Min** value of `15`, a **Max** value of `1971`, and a **Control ID** of `control-total-arrival-delay`.

![In the editor panel, the range of the Total Arrival Delay control is set from a minimum of 15 to a maximum of 1971](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_14.png)

8. Under **Targets (0)**, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg) **Add filter target**. Select **FLIGHTS - Delay Breakdown**, and then select **Arrival Delay**.

We now have a control that functions as a second filter on the `Arrival Delay` column. No matter our settings in the control, that table is still filtered to only show flights with at least 15 minutes of arrival delay. Note that we set a maximum value of 1971 because that is the maximum number of minutes a flight was delayed by in the dataset.

Make some selections in the range control, and observe any trends in the **Average Arrival Delay by Delay Type** donut chart.

9. Click **Publish** save your work to the published version.

## Intro to actions

To conclude this lesson, let’s make one more control that relies on an action workflow.

In Sigma, actions are events, or sequences of events, that you can configure to happen on a trigger. As a simple example, you might add a button to your workbook, and configure an action to take place when a user clicks the button. Actions can also be configured with conditions, meaning that even if the trigger event happens, the action sequence only kicks off if a set of criteria are met.

Our goal is to create a segmented control that allows users to include or exclude cancelled flights. To do this, we need to configure a control on the `Cancelled` column, which can be either `True` or `False`.

1. Navigate to the **Departure Delay vs Arrival Delay** page.
2. In the **Add element bar**, select **Controls** > **Segmented**.

A segmented control appears on the page.

![An empty segmented control on the workbook page](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_15.png)

3. Rename it `Include Cancellations?`
4. In the editor panel, under **Settings**, set the **Value** **source** to be the **FLIGHTS** table in our **Raw Data** page. For the column, select **Cancelled**.

The segmented control updates with values `True` and `False`.

Let’s pause for a moment: is this actually what we want to do with this control? Do we want users to toggle between `True` and `False` values for cancellations? If that were the case, we could configure the control to target the `Cancelled` column. Then, when users select `True`, they’d see data for flights that were cancelled, and when they select `False` they’d see information about flights that were not cancelled.

But this isn’t the same as including or excluding cancellations. What we actually want is for users to be able to select between one of two possible lists of values:

* If they want to include cancellations, we need to show flights that have a `Cancelled` value of either `True` or `False`.
* If they want to exclude cancellations, we need to show flights that have a `Cancelled` value of `False` only.

In other words, we want to offer our users a binary choice (include or exclude) but return data based on a set of values that aren’t binary. Let’s resolve this by using actions.

5. Select the **Include Cancellations?** control.
6. Change the **Value source** to **Create manual list**, and change the **Value type** to **Text**.
7. Enter the values `Yes` and `No`.
8. Change the **Control ID** to `control-cancellations-segmented`.

![The settings menu for the segmented control shows options Yes and No, and a control ID - control-cancellations-segmented](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_16.png)

9. Navigate to the **Raw Data** page and add a filter on the `Cancelled` column, then convert it to a page control.

A list values control labelled **Cancelled** appears.

![The workbook page shows the FLIGHTS table and a list values control titled Cancelled](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_17.png)

10. Select the **Cancelled** control and change the **Control ID** to `control-cancellations-list-values`.
11. Navigate back to the **Departure Delay vs Arrival Delay** page.
12. Select the **Include Cancellations?** segmented control.
13. In the editor panel, select **Actions**.

![In the editor panel, the actions panel is open, and shows a blank action sequence](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_18.png)

In the actions panel, we can configure one or more action sequences. Each action sequence contains a condition (optional), trigger, and action. By default, there is one action sequence with no actions configured.

Let’s configure the following action sequences:

* Action sequence one - include cancellations
  + Condition: When **Include Cancellations?** = `Yes`
  + Action: Set the `control-cancellations-list-values` control - **Cancelled** - to `True`, `False`
* Action sequence two - exclude cancellations
  + Condition: When **Include Cancellations?** = `No`
  + Action: Set the `control-cancellations-list-values` control - **Cancelled** - to `False`

14. In the first **Action sequence**, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Add condition**.

![In a blank action sequence, a user opens the options and selects Add condition](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_19.png)

15. Set the **Condition** as **Control value is equal to** > **Yes**.

![The Action sequence condition shows a condition for Control value is equal to Yes](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_20.png)

16. Back in the action sequence, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg) **Add action…**

![A user selects Add action in the action sequence](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_21.png)

17. Configure a **Set control value** action to update the **Cancelled (Raw Data)** control like below:

![The action sequence is configured with a set control value action set to update the control Cancelled with a static value, selecting the values True, False, and null](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_22.png)

18. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg) **Add action sequence** to add another action sequence.

![A user selects Add action in the action sequence](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_23.png)

19. Set the **Condition** for the second action sequence as **Control value is equal to** > **No**.

![A user configures an action condition for the condition when the control value is equal to No](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_24.png)

20. Configure a **Set control value** action to update the **Cancelled (Raw Data)** control like below:

![The action sequence is configured with a set control value action set to update the control Cancelled with a static value, selecting the values False](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L5/L5_25.png)

Test the action by changing the selection of the control. The table contents update to reflect the changes in the parent data table.

> 💡
>
> #### Controls can control other controls?
>
> You may have noticed that the segmented control we’re providing to the user has no targets, but can still update the table thanks to actions that change another control. This is one option for having one control set another control, but you can also use [synced controls](/docs/synced-controls).
>
> Synced controls allow you to create two identical controls, and automatically apply any updates made to one control to the other. This can be used to manage multiple controls on the same data source across several pages.
>
> In this lesson, however, we can't use a synced control, since the two controls we want to connect are of different types and have different contents. In instances like this, using an action sequence is more appropriate.

21. Click **Publish** save your work to the published version.

## Conclusion

At the end of lesson five, we’ve built interactivity into our dashboard so that users can explore and analyze the data independently. To do that, we learned about the following:

* Controls
* Converting filters to controls
* Placing filters on parent elements
* Actions
* Conditional actions

Updated 3 days ago

---

[Lesson four: Charts and visualizations](/docs/lesson-four-charts-and-visualizations)[Lesson six: Organization](/docs/lesson-six-organization)

* [Table of Contents](#)
* + [Creating basic interaction with controls](#creating-basic-interaction-with-controls)
  + [Controls, lineage, and user experience](#controls-lineage-and-user-experience)
  + [Intro to actions](#intro-to-actions)
  + [Conclusion](#conclusion)