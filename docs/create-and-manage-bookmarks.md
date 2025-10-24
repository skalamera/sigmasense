# Create and share saved views

# Create and share saved views

> 📘
>
> ### Saved views were formerly known as bookmarks.

Saved views allow you to “bookmark” changes you’ve made on top of a published workbook and return to them at any time. Saved views support saving changes of varying complexity, from adding just a filter or control, to adding new charts and data. You can create saved views just for yourself (personal views), or share them with other members of your organization (shared views).

This document explains:

* **Considerations when using saved views**: [Evaluate whether saved views are suitable for your workflow](/docs/create-and-share-saved-views#considerations-when-using-saved-views)
* **Bookmarking your changes in a saved view**: Create a [new personal or shared view](/docs/create-and-share-saved-views#create-or-share-a-new-saved-view)
* **Collaborating with other users by sharing views**: [Share an existing saved view](/docs/create-and-share-saved-views#share-an-existing-saved-view) with others users
* **Accessing your previous views**: [View your most recent or all saved views](/docs/create-and-share-saved-views#accessing-previously-saved-views)
* **Managing your saved views**: [Edit an existing](/docs/create-and-share-saved-views#editing-saved-views) saved view, or [rename/delete](/docs/create-and-share-saved-views#renaming-or-deleting-saved-views) a saved view

## System and user requirements

* All users with access to a workbook are able to save personal views.
* You need **Create, edit, and publish workbooks** account type permissions to share a saved view. See [Account type and license overview](/docs/account-type-and-license-overview).
* Guest users cannot create shared views.

## Considerations when using saved views

Saved views depend on the underlying workbook. Any changes, such as adding/removing filters, duplicating pages, or deleting elements in the underlying published workbook can affect or break saved views. If there are conflicts between the published version of the workbook and the saved view, you might need to manually update your saved view.

For example:

* Deleting a filter from the published workbook removes the filter from all saved views.
* Deleting a data table from the published workbook results in all child elements (such as charts, pivot tables) being removed from the related saved views.

The more changes are made on the bookmark, the more likely it is that small changes in the underlying workbook will affect or break your analysis in the bookmark.

As a result, saved views are not recommended as a version control tool. Saved views are best for preserving a particular workbook configuration for later reference and editing, such as saving a set of filters that a specific team may want to return to frequently.

If you want to support a version control workflow, consider using [version tags](/docs/create-and-manage-version-tags) instead. Version tags are best for preserving a static snapshot of a workbook at a particular state in time, but cannot be edited directly like saved views. See [Create and manage version tags](/docs/create-and-manage-version-tags).

## Create or share a new saved view

When creating a saved view, you can create them as either personal or shared views. Personal views are visible to only you, and are useful to save changes only you need to access. Shared views can be shared with multiple members of your organization, and can be used for collaboration.

To create a saved view:

1. Make changes in a custom view.
2. From the document menu, select **Custom view**, then **Save this custom view**.
3. Enter your desired view name.
4. Save it as either a personal or shared view:

> ❗️
>
> ### There is a limit of 10 shared views for each version of a workbook. There is no limit on personal views.

* **Personal view**: Select **Save**.
* **Shared view**: Select the checkbox next to **Shared view**, then select **Save**.
* (Optional) To set this view as your default landing page when viewing the workbook, select **Set as default view**.

## Share an existing saved view

> 💡
>
> ### Sending a link of a saved view (personal or shared) to another user will make the changes in your saved view available to the user as a new custom view. This custom view will continue to inherit any updates you make to your saved view. To collaborate on the same shared view, you should make the personal view a shared view.

To share an existing personal view as a shared view:

1. From the document menu, select **Custom views**, then **All views**.
2. From the Saved views tab, select click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** next to the personal view you want to share, then select **Set as shared view**. This makes the shared view visible to all users who have **Can view** or **Can edit** access to the workbook.

## Accessing previously saved views

To access previously saved views:

1. From the document menu, select **Custom views**.
2. To view your most recent saved views, select the view under **Recent saved views**.
3. To view all previous custom views, select **All views**.
4. Select the **Saved views** tab to see previous custom views.

## Manage saved views

### Editing saved views

To edit and save changes to an existing saved view:

1. Open your saved view. From the document menu, select **Custom views**, then **All Views**. From the **Saved views** tab, select your saved view.
2. On your saved view, make changes to the workbook.
3. From the document menu, select **Custom views** > **Save to[Name of your saved view]**.

### Renaming or deleting saved views

To rename or delete existing saved views:

1. From the document menu, select **Custom views**, then **All Views**.
2. From the **Saved views** tab, select **More** ⋮ next to your saved view.
3. Select **Edit name** or **Delete**:
   * **Edit name**: Enter your desired name.
   * **Delete**: Select **Delete**.

Updated 3 days ago

---

[Create and interact with custom views](/docs/create-and-interact-with-custom-views)[View column details](/docs/view-column-details)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Considerations when using saved views](#considerations-when-using-saved-views)
  + [Create or share a new saved view](#create-or-share-a-new-saved-view)
  + [Share an existing saved view](#share-an-existing-saved-view)
  + [Accessing previously saved views](#accessing-previously-saved-views)
  + [Manage saved views](#manage-saved-views)
  + - [Editing saved views](#editing-saved-views)
    - [Renaming or deleting saved views](#renaming-or-deleting-saved-views)