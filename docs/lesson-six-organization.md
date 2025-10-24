# Lesson six: Organization

# Lesson six: Organization

Welcome to lesson six: Organization.

In the last lesson, we added interactivity to our workbook by configuring controls and actions. Using these elements, we defined how users could filter data in the workbook.

Now, we’ll organize our filters and charts according to some best practices of user experience and extensible design.

This lesson covers the following Sigma features:

* Modals
* Text elements
* Dynamic text
* Extensible design
* Chart formatting

## A Note on Organization and Style

Up to now, we’ve improved our dashboard by adding functionality - new tables, charts, and controls. However, we’ve spent almost no time considering the appearance of our dashboard. As a result, it’s difficult to navigate.

Some design choices ultimately come down to personal preference: picking just the right shade of green, or choosing the perfect font for your brand. Those aren’t covered in this course.

Other design choices play important roles in making a clear, accessible user experience:

* Some color differences are harder for some users to see than others
* Placing elements in logical orders or groups can boost comprehension
* Larger details are noticed more immediately and perceived as more important

These are covered in this course. The next two lessons focus on making a clear user experience, and directing you towards features you can use for design and aesthetics along the way.

## Managing global filters

Currently, we have five filters for our dashboard, at the bottom of the **Arrival Delay vs Departure Delay** page. They are functional, but there are a few key user experience problems we should consider:

* **Space**: As users request more filters and controls, our **Arrival Delay vs Departure Delay** page becomes longer and more cluttered
* **Scope**: These filters target our parent **FLIGHTS** table, meaning they impact all child elements on all pages, regardless of what page the filters themselves are on
* **Legibility**: When a user opens any page, how do they know what filters are being applied? Currently, they have to toggle to this specific page and look at the controls to see this.

Let’s solve these problems by storing our filters in a modal, and displaying their settings on every page in a dynamic text element.

1. At the bottom of the workbook, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg) **More options** > **Add modal**.

![In the workbook footer, a user opens a menu from a caret, revealing the Add modal option](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_1.png)

2. Return to the **Arrival Delay vs Departure Delay** page.
3. In the **Add element bar**, select **UI** > **Button**.

![In the Add element bar, a user selects UI and hovers over the option for adding a button](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_2.png)

4. In the editor panel, under **Properties**, change the **Text** attribute for the button to `Set Filters`, and then press `enter` (`return` on Mac) on your keyboard.

![In the properties panel, a user changes the text of the button to read Set Filters](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_3.png)

5. In the editor panel, select **Actions**.
6. Add a new action to the existing **Action sequence**.
7. For the **Action type**, select **Open modal**. Under **Select modal**, choose **Modal 1**.

![In the Actions panel, a users adds an Open Modal action to open the modal Modal 1](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_4.png)

8. Click the new **Set Filters** button to see the modal open.

![A user selects the Set Filters button, which opens the empty modal titled Modal 1. An option in the center of the modal allows users to edit the modal](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_5.png)

This is a modal in Sigma as an end-user might see it. When opened by an action, it obscures the current page, and provides an overlay with new content. Since modals are not part of the current page, we can open them anywhere in the workbook. This means they’re a great place to store globally applicable content, like filters or forms.

> 💡
>
> #### Can I reuse a modal?
>
> Yes! Modals are distinct from any page in the workbook, and can be opened from any page. One modal can be opened by actions on several different pages.
>
> For example, if you were to write a reminder about your organization’s data usage policies, and wanted users to be able to access it on every page, you could add an `Our Policies` button on each page that opens a modal with the explanation.

Users can’t directly navigate to modals in the published workbook like they would with a page. They don’t appear as an option at the bottom of the workbook. This means you have a high degree of control over when and how users access modals.

Let’s configure this modal for use with our filters.

1. If you still have the empty modal open, select **Edit modal**. Otherwise, click **Modal 1** at the bottom of the workbook to begin editing the modal.

![The modal titled Modal 1 in the footer appears with the title New Modal along with buttons for Secondary and Primary actions](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_6.png)

2. Double-click the current title - **New Modal** - and rename it to `Filters`.
3. Double-click the page title - **Modal 1** - and rename it to `Filters`.
4. In the editor panel, select **Format**. Open the **Footer** section. Rename the **Primary** button to `Close Modal` and the **Secondary** button to `Clear Filters`.

![In the Format panel, under the footer section, the primary and secondary buttons are renamed Close Modal and Clear Filters, respectively](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_7.png)

5. In the editor panel, select **Actions**.
6. For the **Action sequence** with an **On click - primary** trigger, add and configure a **Close modal** action.

![In the action sequence, an action is configured with the close modal action type](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_8.png)

7. For the **Action sequence** with an **On click - secondary** trigger, add a **Clear control** action.
8. Configure it to **Apply to** a **Page / modal / popover**, and select **Filters**.

![An action is configured to Clear controls in the Filters modal](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_9.png)

9. Add a second action to the **Action sequence** with an **On click - secondary** trigger. Configure it as a **Set control value** action. Under **Update control**, select the **Include Cancellations?** control and set it to a static value of `Yes`.

![In the action sequence triggered by the secondary button, a second action is configured to set the control value of the Include Cancellations? control to Yes](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_10.png)
> 💡
>
> #### Why can’t we just clear a segmented control?
>
> In the previous steps, we configured an action that clears the controls in the **Filters** modal, but then had to configure a separate action to reset the segmented **Include Cancellations?** control. Why is this?
>
> This is because the segmented control is always set to one of its options. There’s no empty state. As a consequence, it’s not clear what clearing it should mean, and so clearing the control doesn’t change it.
>
> However, in the context of our dashboard, we can decide that the “clear” state is the one that includes cancellations, and set a second action in the sequence to reset the control.

10. Navigate to the **Arrival Delay vs Departure Delay** page.
11. For each control, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Move to** > **Filters** to move them to the modal.

![A user opens the element menu for the Scheduled Departure Date date range control and selects Filters from the Move to options](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_11.png)

You can also click and drag your cursor or use `ctrl+click` (`cmd+click` on a Mac) to select multiple filters to move to the modal at once.

![A user selects the remaining controls on the page and opens the options to move them to the Filters modal](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_12.png)

12. When all five filters are in the modal, organize their size and position to your liking.

![The five filters that have been moved to the modal are organized in a grid](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_13.png)

13. Navigate back to the **Arrival Delay vs. Departure Delay** page.
14. Move the **Set Filters** button element to the top of the page.
15. Right click the button, and select **Duplicate**.

![A user duplicates the Set Filters button](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_14.png)

16. Select the duplicate button. In the editor panel, under **Properties**, set its **Appearance** to **Outline** and its **Text** to **Clear Filters**.

![In the editor panel for the duplicate button, the button Text is set to Clear Filters](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_15.png)

17. In the editor panel, select **Actions**, and configure the same action sequence you configured for the **On click - secondary** sequence in the modal.

Now, take some time to test the functionality of your new buttons and modal. Open the modal, set some filters. When you close the modal, the filter selections persist. You can clear them by using the **Clear Filters** button on the workbook page or back in the modal.

This is a strong start for a user experience, but we can make it even more intuitive and responsive. Recall that at the beginning of this section, we observed three problems about the existing layout of our filters: space, scope, and legibility.

We’ve solved the space problem by moving the filters into their own modal, giving us more space on the workbook page. We’ve even begun to solve the scope problem by storing our global filters outside of a specific workbook page. However, we still can’t access the modal from all workbook pages, and we certainly haven’t made the filter contents legible globally.

Let’s solve these problems by configuring a dynamic text element that displays control settings, and then copying our new on-canvas filter controls across all pages.

1. To start, make some space at the top of your workbook page, like in the screenshot below.

![On the dashboard page, a small area in the top-right quadrant is cleared](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_16.png)

2. In the **Add element bar**, select **UI** > **Text** to add a text element to the workbook page.

![In the Add element bar, a user selects UI and then selects the option for a Text element](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_17.png)

3. Bring the new text element to the blank space we created at the top of the page.

![The new text element is placed in the top-right corner of the workbook page](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_18.png)

4. Copy the following text into your text element:

```
Filter Selections

Airlines:
Date Range:
Including Cancelled Flights:
Origin Airports:
Destination Airports:
```

5. Put your cursor in the blank spot after the word `Airlines:` .
6. Press `=` on your keyboard to open the formula bar.

![In the text element, a formula bar opens to enter dynamic text](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_20.png)

7. Copy the following formula into the formula bar and press `Enter` (`return` on Mac) on your keyboard:

```
If(ArrayLength([control-airline]) = 0, "Any", Text([control-airline]))  
```

When you press `Enter`, the dynamic text populates.

This formula uses an **If** statement to check the number of items selected in the `[control-airline]` filter from our filters modal. If there are no items selected, the formula returns the text value `Any`. If there are items selected, it returns the items listed in `[control-airline]` as a text value. Now, we can see what values are set for the filter without having to look at the control itself. Even when the modal is closed, users can read this dynamic text to see what is selected.

> 💡
>
> #### Using our Control IDs from previous lessons
>
> In previous lessons, whenever we made a control, we took time to set the Control ID field to a particular value. In previous lessons, the benefits of this may have been unclear, but they become indispensable when targeting several controls in formulas.
>
> Consider now a workbook with dozens or even hundreds of control elements. Without a strong naming convention, identifying the right control for a formula can become laborious and time-consuming.

8. Let’s configure similar dynamic text for each of our controls, to display their contents dynamically in this text element.
9. Use the following formulas for the corresponding line in the text element:

Date Range:

```
If((IsNull([control-departure-date].start) and IsNull([control-departure-date].end)), "Any", (IsNotNull([control-departure-date].start) or IsNotNull([control-departure-date].end)), (Text([control-departure-date].start) & " to " & Text([control-departure-date].end)))
```

Include Cancelled Flights:

```
If(Contains([control-cancellations-segmented], "Y"), "Yes", "No")
```

Origin Airports:

```
If(ArrayLength([control-origin-airport]) = 0, "Any", Text([control-origin-airport]))
```

Destination Airports:

```
If(ArrayLength([control-destination-airport]) = 0, "Any", Text([control-destination-airport]))
```

10. Click **Clear Filters**.

Your dynamic text appears like the screenshot below:

![In the text element, the dynamic text entries populate with “Any” or “Yes” depending on the formula](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_21.png)

We can now read the contents of our **Filters** modal from this page without having to open the modal or read the controls themselves directly. Though these controls are relatively simple to interpret, if we were to build more complex controls, a dynamic text representation like this might be the best way to make the filters legible to users.

For now, let’s finish configuring our global filters by copying our buttons and dynamic text to our other dashboard page.

1. Using `ctrl+click` (`cmd+click` on Mac), select the text element, **Clear Filters** button, and **Set Filters** button.
2. Select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More options** > **Duplicate**.

![The dynamic text and button elements on the Dashboard page are selected. A user selects the duplicate option](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_22.png)

3. Select the duplicates, and then ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More options** > **Move to** > **Arrival Delay by Delay Type**.

![The dynamic text and button elements on the Dashboard page are selected. A user selects the Move to option, and selects the Arrival Delay by Delay Type page](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_23.png)

Test the buttons and dynamic text on this page, and notice that they work identically to how they did on the page where we first created them. We have now solved the problems of space, scope, and legibility for our filter elements. They can be accessed from any page without cluttering the space, they impact all pages, and their current settings can be read on all pages.

> 💡
>
> #### How would we expand this design in the future?
>
> Throughout this tutorial, we’ve focused on extensible design. Choices made as early as lesson two, like building off of one parent table, are paying off now.
>
> If we wanted to add another control, we might create it from our parent **FLIGHTS** table, move it to our **Filters** modal, and then copy-paste a new dynamic text entry onto each page to display its contents.
>
> If we wanted to add another workbook page, we might copy-paste the buttons and text element from our existing workbook pages onto the new page, instead of having to copy-paste every control and synchronize them across the pages.

4. Click **Publish** save your work to the published version.

## Chart settings and style

To round out our workbook, let’s add in a couple more charts to help us clearly organize information for a user, and provide some information they might want that isn’t currently available.

1. Navigate to the **Arrival Delay vs Departure Delay** page.
2. Select the pivot table **Departure Delay by Month and Day of the Week**. Click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Duplicate**.
3. Rename the duplicate element **Arrival Delay by Month and Day of the Week**.
4. In the editor panel, under **Properties**, replace the **Value** of **Avg of Departure Delay** with **Avg of Arrival Delay**.

![The duplicate pivot table is selected. In the editor panel, Avg of Departure Delay is replaced by Avg of Arrival Delay](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_24.png)

5. In the editor panel, select **Format** > **Conditional formatting**.
6. Click **Color scale**. Select this yellow gradient and select **Reverse color scale**.

![In the Color Scale options for conditional formatting, a user selects a yellow color scale that goes from white at the left, to yellow in the middle, to black at the right. They select the checkbox for Reverse color scale](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_25.png)

7. Move the new **Arrival Delay by Month and Day of the Week** pivot table side-by-side with the **Departure Delay by Month and Day of the Week** pivot table.
8. Now, select one of the pivot tables. In the editor panel, select the **Avg of Departure Delay** calculation under the **Values** section so that it’s highlighted.

![In the Values section, Avg of Departure Delay is highlighted](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_26.png)

9. In the top-left corner of the workbook, select **Decrease decimal places** from the toolbar.

![A user selects the option to Decrease decimal places](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_27.png)

10. Then, select **Increase decimal places**.

![A user selects the option to Increase decimal places](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_28.png)

11. Repeat these steps for the other input table. As a result, both show only one point after the decimal for each cell, reducing visual clutter by truncating the previously long series of numbers.

![The pivot tables for Departure Delay and Arrival Delay side-by-side, color-scaled blue and yellow respectively. Each cell value contains one digit after the decimal place](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_29.png)

Let’s think through some of the practical reasons to make these design choices:

* **Thematic Consistency:** We already had both departure delay and arrival delay listed in our KPIs and both of our charts. If we provided the pivot table for only one of them, a user might naturally ask for the other.
* **Visual Clarity:** To help users read these tables as a pair, we configured them so that a darker color means a longer delay, regardless of delay type. This means that users can quickly scan both tables to see what times of year had the more or less delay.
* **Color selection**: We’ve used the same colors for departure delay (blue) and arrival delay (yellow) across the page. This helps them to scan across charts more quickly, and promotes extensibility.
* **Necessary precision:** By reducing each cell value to show only one digit after the decimal point, we removed unnecessary precision and visual clutter.

Let’s add one more chart to see other design choices in action.

1. Navigate to the **Raw Data** page.
2. Select the **FLIGHTS - Delay Breakdown** table and create a child chart element.
3. Select the new bar chart this creates. Select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Move to** > **Arrival Delay by Delay Type**

![On the Arrival Delay by Delay Type page, an empty new bar chart appears](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_30.png)

4. In the editor panel, configure the following settings for the new chart:

* **Chart type** - Line
* **X-axis** - Week of Scheduled Departure DateTime
* **Y-axis** - Sum of Late Aircraft Delay, Sum of Airline Delay, Sum of Air System Delay, Sum of Weather Delay, Sum of Security Delay

![In the editor panel for the line chart, week of scheduled departure delay is listed under the x-axis, and sums for each of the 5 delay types are listed under the y-axis](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_31.png)

This creates a line chart with five lines, each of which charts the variation in one source of delay time over the course of the year.

5. Rename the chart **Arrival Delay by Delay Type**.

![The Arrival Delay by Delay Type line charts show five lines, one for each of the delay types over the course of the year 2015](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/tutorials/docs-fundamentals/L6/L6_32.png)

This provides a few design advantages when paired with our donut chart:

* **Trends:** Using a chart with a time-dimension on the x-axis like this allows us to see how each source of delay varied over the course of the year.
* **Sums for each week:** Since we used the sum of each delay type in our y-axis, we can hover over the line for any week in our chart to see all five delay type sums in a tooltip, which we didn’t previously have access to on this page.

A user on this page could now observe trends in both the totals and averages for delay times based on global filter settings.

6. Click **Publish** to save your work to the published version.

## Conclusion

At the end of lesson six, we’ve made some basic design choices that made our dashboard more organized and easier to expand in the future. We chose how to handle our global filter options, and filled in some gaps in our dashboard pages.

To do that, we learned about the following:

* Modals
* Text elements
* Dynamic text
* Extensible design
* Chart formatting

Updated 3 days ago

---

[Lesson five: Controls and actions](/docs/lesson-five-controls-and-actions)[Lesson seven: Style](/docs/lesson-seven-style)

* [Table of Contents](#)
* + [A Note on Organization and Style](#a-note-on-organization-and-style)
  + [Managing global filters](#managing-global-filters)
  + [Chart settings and style](#chart-settings-and-style)
  + [Conclusion](#conclusion)