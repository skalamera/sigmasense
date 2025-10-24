# Lesson eight: Input tables and combining data

# Lesson eight: Input tables and combining data

Welcome to lesson eight: Input tables and combining data.

In the last lesson, we styled our dashboard using layout elements, workbook settings, and themes. At this point, our dashboard is in a reasonably polished state. We might want to have a peer review our work, or ask for feedback from stakeholders, but it has all the basic functionality we’d expect from a BI dashboard:

* A connection to live data
* Multiple charts
* Filter options
* Distinct pages for sub-topics

In this final lesson, we’ll go beyond this typical functionality of a BI dashboard and explore two use cases for input tables. First, we’ll enrich our dataset by uploading a CSV directly to Sigma. Then, we’ll create an interface where users can enter new flights into the dataset.

## Upload data to an input table

Input tables are Sigma elements we can use to enter or upload data.

> 📘
>
> Remember that Sigma never stores your data in Sigma, including data entered in input tables. Sigma stores input table data in a specific write-back schema in your data platform. Learn more about the details in [the documentation](/docs/intro-to-input-tables).

To see input tables in action, let’s upload a CSV of airport data to our workbook, and join it to our **FLIGHTS** data. Using that joined dataset, we can then create a map.

1. To download a CSV of airport coordinates, click on the [link provided here](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/airport-destinations-final.csv).
2. Save it somewhere you can easily locate.
3. Return to the **Flight Delay Times** workbook and enter **Edit mode**.
4. Add a new page, and name it **Airport Data**.
5. In the **Add element bar**, select **Input** > **CSV**.

![In the Add element bar, a user selects Input and then selects CSV](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_1.png)

6. In the prompt to upload a CSV-formatted file, click **Browse**.
7. Select the airport-destinations-final CSV-formatted file you downloaded previously and then click **Open**.
8. This opens a preview of the CSV file in table format, and provides some options to change settings for the upload.

![In the Parsing options, some settings Connection, and custom Delimiter options are shown](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_2.png)

The provided file works with the default options, so there’s no need to make any changes. In the future, this is where you can choose a connection with a write-back schema, and set parsing options for CSV-formatted data like the delimiter value and whether it has a header or not.

9. Click **Save**.
10. A new input table titled **New Input Table** is created. Rename it to **Airport Locations**.

This input table element closely resembles our existing table elements. Just like other tables, we can add calculated columns, summaries, filters, sorts, and more. Unlike other tables, though, we can add input columns that allow us to edit individual cells.

1. Select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) in the column header to add a new column to the input table, and select **Text**.

![In the Airport Locations input table, a user selects the option to add an additional column](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_3.png)

2. Double click a cell, and enter some text.

![A single cell in an input table shows custom text entry at the cell level](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_4.png)

Unlike other table elements, we can make cell-level entries in input tables. Just like the CSV data we uploaded when creating this input table, this data is stored in the write-back schema in your data platform. This new column is just a demonstration, and has no practical application for our use case, so we can delete it for now.

3. Right-click the header of the **Text** column, and select **Delete column**.

Now, let’s consider how we could use this newly entered data about airports to enrich our analysis of delay times. Our input table has three columns:

* **ID** - Lists the ID of the airport.
* **Latitude** - Provides a coordinate value for how far north or south the airport is.
* **Longitude** - Provides the coordinate for how far east or west the airport is.

If we combine this information with our existing information on flights, we can visualize departure delays by airport location. For example, we might use the airport ID to join the geographical coordinates as two additional columns in the flights table.

After we have that joined table, we can create detailed visualizations with geographical location. As an imagined end-state, we could build a map that shows larger, redder dots for airports with a higher average departure delay, like this:

![A point map of the United States shows larger, redder dots for some airports that are more delayed](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_5.png)

In the rest of this section we’ll walk through how to join tables to create this chart.

1. Navigate to the **Airport Data** page.
2. In the **Add element** bar, select **Data** > **Table**. In the **Select source** modal, click **Join**.

![A user selects Join from the Select source modal for a table element](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_6.png)

3. In the **Select source** modal for the join, select the **Elements** tab, and choose the **FLIGHTS** table from the **Raw Data** page.

![A user selects the FLIGHTS table from the Elements tab of the Select source modal](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_7.png)

By default, any column that is not hidden is selected for the join. Click **Select**.

4. The **Create join** screen opens, where you can identify elements to join onto the **FLIGHTS** table you selected in the previous step.
5. Select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg) **Add source**.

![From the Sources section, a user selects Add source](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_8.png)

6. Navigate to the **Elements** tab, and select **Airport Locations** from the **Airport Data** page.

![In the Select source modal, a user selects the Airport Locations table from the elements menu](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_9.png)

7. Click Select.
8. Configure the following join settings:

* **Join with** - FLIGHTS
* **Selected source** - Airport Locations
* **Join type** - Inner join
* **Join keys** - Origin Airport = ID

![Airport Locations is joined with FLIGHTS by an Inner JOIN on the keys Origin Airport = ID](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_10.png)

9. Click **Preview output**.

In the provided preview, we can see a directed acyclic graph (DAG) representing the join of the two tables, as well as a set of sample records. The DAG shows us that the two sources we selected - **FLIGHTS** and **Airport Locations** - will join into a new table. In the sample records, we can see what the new table will look like, with colors indicating which table the columns originated from. The orange columns are from **FLIGHTS** while the green columns are from **Airport Locations**.

![The join preview shows a visual representation of the join and sample data](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_11.png)
> 💡
>
> #### What’s a join?
>
> For those unfamiliar with joins, let’s take a moment to describe what we just did. Joining is the general term for combining two tables based on matching information in each table. We used the `Origin Airport` column from **FLIGHTS** and the `ID` column from **Airport Locations** as keys to match information from the two tables and combine it into new records.
>
> We can describe the result as the following:
>
> *For each record in FLIGHTS with an Origin Airport value that appears in Airport Locations, add the latitude and longitude for the ID that matches the Origin Airport value for that record.*
>
> So, for a flight record in **FLIGHTS** that lists `SNA` as the origin airport, we get the coordinates for `SNA` from the **Airport Locations** table, and add them to the record.
>
> Because we performed an inner join, we only keep records where there’s a match in both tables. If we wanted to keep all records in one set but add on information from another set where it exists, we’d use a different join type. See [Join types](/docs/join-types).
>
> Bonus: This is similar to the concept of a [Lookup](/docs/lookup). The main difference in this case is that we only kept records that had a key value in both tables, so any airports without coordinates were removed from the dataset. Because of this, the table that results from the join has fewer records than the original **FLIGHTS** table.

10. Click **Done**.

Back on the workbook page, the new table element **FLIGHTS +1** appears.

Now that each of our flight records has the coordinates for the origin airport, let’s try mapping them.

1. Create a new child chart element from the **FLIGHTS +1** table.
2. In the editor panel, set the **Chart type** to **Map - Point**. In the **Latitude** and **Longitude** sections, select the columns of the same name from our data source.

![In the Editor panel, a chart with the type Map - Point, uses Latitude and Longitude columns in settings of the same name](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_12.png)

The map element populates with a point for each airport.

While this is helpful, we could have made this chart with just the **Airport Locations** table. All it requires is a latitude and longitude, which we already had. The real advantage of joining coordinates onto each flight record is that we can now include aggregate information about the flights at each airport on our map. Let’s color-code and scale the dots for each airport according to the average departure delay for flights that originated there.

3. In the editor panel, under the **Color** tab, open the dropdown menu and select **By scale**.

![In the Color settings, a user selects the By scale option](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_13.png)

4. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg) **Add calculation…** and add the **Departure Delay** column. Change the aggregate from **Sum** to **Avg**.
5. To create a color scale like the example from earlier, change the color scale to **Diverging**, select **Reverse color scale**, and select this blue-to-red diverging scheme.

![In the Color options, a user selects the Diverging color scheme options, and then selects a color scheme that ranges from blue on the left-hand side, to white in the middle, to red on the right-hand side, as well as checking the Reverse color scale box](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_14.png)

Airports with the highest average departure delay now appear in dark red, while airports with the lowest departure delay appear in dark blue.

6. In the editor panel, select the **Size** tab.
7. Under **Select column**, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg) **Add calculation…**
8. Select the **Departure Delay** column, and change the aggregate from **Sum** to **Avg**.

![In the Size options, Avg of Departure Delay is set as the column that determines the dot size](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_15.png)

Now, we’ve created a chart where we can see each origin airport by departure delay, allowing us to quickly scan the country for trends in the data. Any larger, redder dot means that that airport has a higher average departure delay for flights leaving there. We might notice that the largest, reddest dots happen to cluster around population centers in the East and on the West coast of the United States.

![A map of the US with dots for each airport in the dataset. Airports that are more delayed are larger and darker red](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_16.png)
> 💡
>
> #### So more population equals more delays, right?
>
> Our chart seems to suggest that higher population areas see more delays, but let’s think about how we might use this chart and our dataset to prove or disprove that hypothesis.
>
> While it’s true that the areas with redder dots are in the higher population areas of the US, the trend doesn’t seem to hold true for individual airports in those regions. Airports like BOS, JFK, MSP, and SFO that are near big red dots don’t have big red dots themselves.
>
> Try a few bonus tasks on your own to investigate the trend more:
>
> * Add the total number of flights from each airport to the tooltip for each point
> * Add the airport name to the tooltip for each point
> * Add a bar chart next to the map that lists the top 10 airports with the greatest departure delay
> * Calculate the [correlation](/docs/corr) between flight volume and departure delay time per airport
>
> Do the airports with the greatest departure delays actually have more flights?

9. Move the map chart to a new page.
10. Name the new page **Departure Delay by Airport**.
11. Hide the **Airport Data** page that contains the CSV upload and join table.
12. Click **Publish** to save your work to the published version.

## Allow users to enter information on new flights

To round out this fundamentals course, we’ll do something that requires all the skills we’ve learned so far: create an interface where users can enter information about a flight, create a new record for that flight, and update all charts immediately with the new information.

Since this is the last section of the tutorial, the instructions are a little less direct than previous sections. This is to help you test your knowledge and reinforce what you’ve learned so far.

Take a moment and consider - how would you accomplish this?

Here are some questions to consider:

* What elements would allow users to enter information about a flight?
* How would you implement this as an intuitive user experience?
* Where would you store information once users have entered it?
* How would you integrate the new records into the charts as they’re created?

The rest of this section walks through one way we might implement this. Let’s break the problem down into steps with potential solutions:

* **Data entry** - Users can configure control values to indicate the origin and destination, flight duration, flight number, date, etc.
* **User experience** - The controls can all be stored in a modal that’s opened by a button, like our filter modal.
* **Storing information** - We can read the control values into a new record in an input table via an action sequence.
* **Live updates** - We can change our data source for the charts to a new table, and that new table will be the combination of the original **FLIGHTS** table with the input table.

Let’s configure the control interface where users can enter data.

1. Add a new modal to the workbook. Name it `New Flight Entry`, and set the title to `Enter Details on a New Flight`.

![The new modal, titled Enter Details on a New Flight](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_17.png)

2. In the **New Flight Entry** modal, add the following eight control elements:

* A list values control titled `Airline`
* A list values control titled `Origin Airport`
* A list values control titled `Destination Airport`
* A date control titled `Scheduled Departure Date`
* A number input control titled `Flight Number`
* A number input control titled `Departure Delay`
* A number input control titled `Arrival Delay`
* A number input control titled `Flight Duration`

![In the Enter Details on a New Flight modal, 8 controls are arranged in a 4x2 grid](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_18.png)

3. For the three list values controls, configure the list of values that users can select from.
4. Since there’s already a list of valid `Airline` and `Airport` values in the **FLIGHTS** table, configure each control to use the appropriate column in that table as a source of values.

For example, the configuration in the editor panel for the **Airline** control looks like this:

![In the settings for a list values control, the Value Source is Raw Data - Flights, and the Source column is Airline](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_19.png)

5. Using Airline as the **Source column** means that when users select the **Airline** list values control, they can select from the values that exist in the `Airline` column of **FLIGHTS**.
6. For each list values control, uncheck the boxes for **Allow multiple selection** and **Show null option**. You can find these in the **Properties** section of the editor panel. These settings ensure that users must select one and only one non-null option for these fields when creating a new record.

![In the settings for a list values control, only the checkbox for Show clear button is selected](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_20.png)

When you’ve done this for all three list values controls, move on to the next step.

7. Now, give all eight controls a reasonable **Control ID** you can reference later.

For example, give the **Airline** control an ID like `airline-entry`, so that you can identify that it’s not a filter. You can give **Origin Airport** an ID like `origin-airport-entry`, and so on for the remaining.

Before we can configure actions that read these control values, we need a place to store the data about these new flights. Let’s create an input table to capture the information.

1. Create a new page. Hide it, and rename it `New Flight Data`.
2. On the **New Flight Data** page, use the **Add element** bar to create a new input table. Select the **Empty** input table type.

![In the Add element bar, a user selects Input, and then selects Empty](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_21.png)

3. Select **Sigma Sample Database** as the connection, and click **Create**.
4. Name the table **New Flight Entries**.
5. Configure the new input table with the following nine columns:

* A number column titled `Flight Number`
* A date column titled `Scheduled Departure Date`
* A text column titled `Origin Airport`
* A text column titled `Destination Airport`
* A number column titled `Departure Delay`
* A number column titled `Arrival Delay`
* A number column titled `Flight Duration`
* A text column titled `Airline`
* A Calc column titled `Cancelled?`

6. In the formula bar for the `Cancelled?` column, enter `False` and click the green check. This updates the column to the logical data type, and populates it with the value `False` by default.

> 📘
>
> We’re configuring this default value for `Cancellations?` because each record needs this information to work with the filters we’ve configured in the workbook. We’re making an assumption here that if a user enters a new flight record, the flight was not cancelled. In a future version of this, we could provide users a method to input this information.

The editor panel for the **New Flight Entries** input table looks something like the following:

![In the editor panel, the column list reflects the entries from the previous set of instructions](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_22.png)

We’ve now configured a set of controls where users can enter data and a table in which to store that data. Next, let’s configure the necessary actions to create a new record in New Flight Entries based on the contents of the controls.

1. Navigate to the **New Flight Entry** modal.
2. In the editor panel, select **Format**.
3. Open the **Footer** section. Rename the **Primary** button to `Create Entry` and the **Secondary** button to `Clear Fields`.

![In the Format of the New Flight Entry modal, the Primary button is labelled Create Entry, and the secondary button is labelled Clear Fields](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_23.png)

4. In the editor panel, select **Actions**.
5. In the **Action sequence** with an **On click - primary** trigger, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg) **Add action**.
6. Configure an **Insert row** action to insert a row into the **New Flight Entries** input table. For each field in **New Flight Entries** select the corresponding control from the **New Flight Entry** modal to populate the value.

![In the configuration for an Insert row action, columns are connected to their corresponding controls](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_24.png)

Additionally, configure a condition for this action sequence that checks to make sure none of the entry controls are null before submitting a record.

1. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Add condition**.
2. Use the following formula:

```
IsNotNull([airline-entry]) and IsNotNull([scheduled-departure-date-entry]) and IsNotNull([origin-airport-entry]) and IsNotNull([departure-delay-entry]) and IsNotNull([destination-airport-entry]) and IsNotNull([arrival-delay-entry]) and IsNotNull([flight-number-entry]) and IsNotNull([flight-duration-entry])  
```

![In the action condition, the formula from the previous step is shown in the formula bar](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_25.png)
> 💡
>
> #### Why require all values?
>
> At first, it might seem unnecessary to check that all fields are populated before making a new record. But consider the alternative. What would happen if we allowed any set of the controls to be blank, resulting in a null value for that field?
>
> We’d have to:
>
> * Handle null values in every filter and condition we’ve previously configured
> * Handle null values for calculations - either exclude them from averages or indicate to users that they might impact averages
> * Justify that this extra labor is worth it to handle incomplete records. What value do we gain from getting the arrival delay for a flight with no listed airline or airports?
>
> Only allowing complete records is one way to minimize the amount of extra work we do downstream.

3. Add a second action to the same action sequence to clear all the controls in the **New Flight Entry** modal after you’ve created the new row. This way, the controls automatically clear after a new row is successfully created.

![A clear control action is set to Apply to the New Flight Entry modal](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_25_1.png)

4. In the **Action sequence** with an **On click - secondary** trigger, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg) **Add action**.
5. Configure a **Clear control** action to clear all controls in the **New Flight Entry** modal.

![A clear control action is set to Apply to the New Flight Entry modal](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_26.png)

We can now test the workflow. We can set control values like this:

![In the New Flight Entry Modal, a user enters Flight Number 1234567, Departure Date May 1st 2015, Origin Airport BOS, Destination Airport JFK, Departure Delay 10, Arrival Delay 6, Flight Duration 66, Airline WN](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_27.png)

And when we click **Create Entry**, the values appear in the input table like this:

![A record is shown in the input table with the entries from the previous step](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_28.png)

1. Navigate to the **Departure Delay vs Arrival Delay** page.
2. Add a new button element and rename it **Enter Flight**.

![On the workbook page, an Enter Flight button is added alongside the Filter buttons](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_29.png)

3. Select the button, and add an action to the **Action sequence** triggered **On click** to open the **New Flight Entry** modal.

At this point, we’ve created a system where users can open a modal, enter information about a flight, and click a button to enter that information into a new table. However, none of that information is reflected in our charts and graphs yet. The next section introduces a method to implement that functionality.

## Union new records to our data

One way we could update our charts each time a new entry is created is to change the data source all of our charts are connected to. If we were to replace the current **FLIGHTS** table with a new table that contains all of the records from **FLIGHTS** as well as new entries, then the new records would appear in charts, summaries, and calculations after they’re added.

We can accomplish this with a union. Similar to a join, a union is a way of combining data from multiple tables. However, there’s a key difference. Whereas a join combines columns from multiple tables to make a wider table, a union combines records from multiple tables to create a longer table.

![A chart illustrates the difference between union and join. Two tables are shown unioned, creating a longer table, and joined, creating a wider table](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_Union_vs_Join.png)

Let’s union our new flight records onto the **FLIGHTS** table.

1. Navigate to the **New Flight Data** page.
2. In the **Add element** bar, select **Data** > **Table** > **Union**.

![In the Select source modal, a use selects Union](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_30.png)

3. In the **Select source** modal, select the **New Flight Entries** table, and then click **Select**.
4. In the **Create union** screen, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/add.svg) **Add source**.

![In the Sources, a user selects Add sourcel](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_31.png)

5. Select the **FLIGHTS** table.
6. Select the matching columns from each table so that the records are in line with one another in the final table.

![In the Sources screen, columns are matched between the New Flight Entries table and the FLIGHTS table](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_32.png)

7. Click **Done**.

A new table titled **Union of 2 Sources** appears.

8. Rename the table **FLIGHTS + Entries**.

This new table contains all records from our original **FLIGHTS** table along with the records users enter via the **New Flight Entry** modal. We can verify this in a couple different ways to check for accuracy.

For example, we might filter the new table to just the flight number of the example we entered when testing the New Flight Entry modal. If configured correctly, the new record appears in the filtered table.

Or we can observe that the table summary for the new table has a higher record count than the original **FLIGHTS** table. It has one more record, which is the test record we entered.

Now, let’s finish the setup by updating our charts to use this new table as their data source.

1. Navigate to the **Departure Delay vs Arrival Delay** table.
2. Select the bar chart **Average of Departure and Arrival Delay by Airline**.
3. In the editor panel, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg) under **Data source**, and select **Change source…**.

![In the editor panel, a user opens the Date source menu and selects Change source](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_33.png)

4. In the **Change source** modal, select the **FLIGHTS + New Entries** element as the new data source for the chart.

![In the change source modal, a user selects the FLIGHTS + Entries table](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_34.png)

The table refreshes, but nothing changes. This is because the new data source is not sufficiently different from the old one to have a visible impact on the chart.

5. Click the **Enter Flight** button.
6. In the **New Flight Entry** modal, enter the following details for a flight:

* Airline - DL
* Origin Airport - BOS
* Destination Airport - JFK
* Flight Number - 1234568
* Scheduled Departure Date - 05/01/2015
* Departure Delay - 10
* Arrival Delay - -2000000
* Flight Duration - 66

![In the Enter Details on a new New Flight modal, a user enters the sample data provided above](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L8/L8_35.png)

7. Click **Create Entry**.

The bar chart updates, and `DL` now has a negative **Average of Arrival Delay**.

Note that no flight could be two million minutes early. This is an extreme example, intended to demonstrate that the bar chart is updating based on any new entry we make to the input table. We can go into the input table and delete the entry, and `DL` returns to its previous, more realistic arrival delay average.

8. To complete this lesson, update the rest of the elements on this page to use the new unioned table as their data source, including:

* Both KPI elements at the top of the page
* The line chart
* Both pivot tables

Additionally, consider how you might update the other pages in the workbook to utilize this new table:

* What would happen if we update the filters in the **Filters** modal to target the unioned table?
* How would we reflect these updates in the **Arrival Delay by Delay Type** page?

There’s no single correct answer to these design questions. For example, you might decide it isn’t worth the effort to reflect these updates on every page in the workbook. Or, you might expand the **New Flight Entry** modal with new controls so that users can enter the entire delay type breakdown where appropriate.

## Conclusion

Try your hand at answering the questions above if you’d like to experiment. Otherwise, this is the end of the tutorial.

Hopefully, this course has helped you build an intuition for how you might go about solving these problems, as well as other tasks, in Sigma.

We’ve covered everything from creating your first workbook, all the way up to designing an intuitive user experience with live data entry. Along the way, we’ve tried out some core design patterns in Sigma, and considered how we could apply those designs in multiple contexts.

Now, try applying these principles to your organization’s data and use cases.

Happy calculating!

Updated 3 days ago

---

[Lesson seven: Style](/docs/lesson-seven-style)[Connect to data sources](/docs/connect-to-data-sources)

* [Table of Contents](#)
* + [Upload data to an input table](#upload-data-to-an-input-table)
  + [Allow users to enter information on new flights](#allow-users-to-enter-information-on-new-flights)
  + [Union new records to our data](#union-new-records-to-our-data)
  + [Conclusion](#conclusion)