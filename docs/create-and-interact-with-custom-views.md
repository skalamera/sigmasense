# Create and interact with custom views

# Create and interact with custom views

Sigma supports the creation of custom views in your workbooks. Custom views allow you to interact with your workbook and make changes, without affecting the published version of your workbook.

Custom views are useful for ad hoc data analysis - you can sort or filter data, add new workbook elements, edit your workbook layout and more, in a view that is visible to only you. For example, you may want to filter a table to show data for specific teams or regions, or try adding a new chart, without changing what other users with access to the workbook can see. Multiple users are able to open custom views on the same workbook simultaneously, without affecting each other’s work.

Custom views support several different customization and collaboration workflows:

* **Create and change for ad hoc analysis**: [Begin ad hoc data exploration](/docs/create-and-interact-with-custom-views#start-customizing-your-workbook) by making changes in your workbook. Depending on your permissions, you can also [make more advanced changes](/docs/create-and-interact-with-custom-views#make-more-changes-while-in-a-custom-view) to element properties, format or actions.
* **Saving or discarding your changes**: Once you are done exploring, you can [save your change](/docs/create-and-interact-with-custom-views#saving-or-discarding-your-changes)s for personal or shared use, [exit the view](/docs/create-and-interact-with-custom-views#exit-a-custom-view), or [merge your changes into the published workbook](/docs/create-and-interact-with-custom-views#merge-your-changes-to-the-published-version).
* **Return to previous customized changes**: You can [access past custom views](/docs/create-and-interact-with-custom-views#access-your-previously-closed-custom-views).
* **Share your analysis with others**: You can either [send a link to share your custom view](/docs/create-and-interact-with-custom-views#share-by-link), or [create a shared view](/docs/create-and-interact-with-custom-views#save-as-shared-view).

## User and system requirements

* You must have access to the workbook you want to create custom views in.
* All users can create custom views, but the options available when customizing and sharing depend on individual account permissions (necessary permissions are noted in the task sections below). For more information, see [Account type and license overview](/docs/account-type-and-license-overview).

## Make updates in custom views

### Start customizing your workbook

From the published version of your workbook, there are two ways to enter a custom view:

* Interacting with an element: Changes to an element such as filtering, sorting, adding or renaming data will also open a custom view.
* *(Account type with **Full explore** permissions required)* Selecting the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/custom-view.svg) **Customize this view** icon.

When performing either of these actions from a published workbook, the workbook header will turn green, indicating that you are in a custom view.

### Make more changes while in a custom view

If you have **Can explore** workbook access and **Full explore** permissions, you are able to make more advanced changes from a custom view by accessing the editor panels:

* Once in a custom view, select the **Show panels** icon to access the **Properties**, **Format** and **Actions** tabs. Depending on what you are interacting with in your workbook, different panels are shown.

Depending on your individual account type permissions, you can use the full scope of analytical workbook functionality from the editor panel, like [creating new elements](/docs/create-a-data-element), [copy and pasting elements](/docs/copy-and-paste-elements), [editing your workbook layout](/docs/create-and-manage-workbook-layouts), [drilling into underlying data](/docs/drill-into-data), and [sending or scheduling exports](/docs/send-or-schedule-workbook-exports).

## Saving or discarding your changes

Your changes in a custom view are automatically saved as you work, but you can save your changes in other formats or configurations.

### Save as saved view

To bookmark a specific configuration of changes, like a frequently accessed set of filters or visualizations, you can create a saved view. See [Create and share saved views](/docs/create-and-share-saved-views) for more information.

### Save as a new workbook or template

If you have **Create, edit, and publish workbooks** account type permission, you can also save your changes as a new workbook, or as a template for yourself or others to duplicate and work off of.

To save your custom view as a new workbook or template:

1. From the document menu, select **File** , then select **Save as workbook** or **Save as template**.
2. Configure your desired fields:
   * **Save as a workbook:** Enter a name for your new workbook, then select the location you want to save the new workbook to.
   * **Save as template:** Enter a name for the template. If you want to share the template with other users, search for and select your desired members/teams, and select the usage permissions you want to give them.
3. Select **Save**.

### Merge your changes to the published version

If you have **Can edit** access to the workbook you are customizing, you can merge changes made in your custom view into the published version of the workbook:

1. From the document menu, select **Edit** > **Edit workbook**.
2. In the **Merge changes into draft** modal, review the changes and select **Merge changes**.

If you don’t want to merge changes at this time, you can select **Discard changes** and return to them at a later time. See [Return to previous customized changes](/docs/create-and-interact-with-custom-views#return-to-previous-customized-changes).

### Exit a custom view

When exiting a custom view, you can navigate back to the published version of the workbook, or to a workbook draft:

* **To exit to the published version**: Select **Close view**. The workbook header will turn back to white, indicating you have exited the custom view.
* **To exit to a draft**: From the document menu, select **Edit** > **Edit workbook**. Select **Discard changes**.

If you want to return to your changes at a later time, see [Return to previous customized changes](/docs/create-and-interact-with-custom-views#return-to-previous-customized-changes).

## Return to previous customized changes

### Access your previously closed custom views

You can view your own previous custom views:

1. From the document menu, select **Custom views**.
2. To view your most recent custom view, select the view under **Recent custom view**.
3. To view all previous custom views, select **All views**.
4. Select the **Custom views** tab to see previous custom views.

You are not able to access the custom view history of other users.

## Share your analysis with others

### Share by link

If you want to quickly share changes in your custom view that you don’t need to store and access, you can send a link to your workbook by copying and pasting the link from your browser address bar. You may need to configure access for users before they can view your workbook. See [Share a workbook](/docs/share-a-workbook).

### Save as shared view

If you want to work and collaborate with other users on your custom view more extensively, create a saved view and share it. See [Create and share saved views](/docs/create-and-share-saved-views).

Updated 3 days ago

---

[Build if/else control flow in an action sequence (Beta)](/docs/build-if-else-control-flow-in-an-action-sequence)[Create and share saved views](/docs/create-and-share-saved-views)

* [Table of Contents](#)
* + [User and system requirements](#user-and-system-requirements)
  + [Make updates in custom views](#make-updates-in-custom-views)
  + - [Start customizing your workbook](#start-customizing-your-workbook)
    - [Make more changes while in a custom view](#make-more-changes-while-in-a-custom-view)
  + [Saving or discarding your changes](#saving-or-discarding-your-changes)
  + - [Save as saved view](#save-as-saved-view)
    - [Save as a new workbook or template](#save-as-a-new-workbook-or-template)
    - [Merge your changes to the published version](#merge-your-changes-to-the-published-version)
    - [Exit a custom view](#exit-a-custom-view)
  + [Return to previous customized changes](#return-to-previous-customized-changes)
  + - [Access your previously closed custom views](#access-your-previously-closed-custom-views)
  + [Share your analysis with others](#share-your-analysis-with-others)
  + - [Share by link](#share-by-link)
    - [Save as shared view](#save-as-shared-view)