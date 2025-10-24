# Use comments in workbooks

# Use comments in workbooks

You can add comments to workbooks and data models, including individual elements, to provide context for charts or control elements, solicit feedback from colleagues, or make requests. When you comment on a workbook or data model, an email is sent to all editors of the document that have previously published a version.

When you add comments, make sure that your workbook is published or saved. If you want to add comments to an exploration, you must first save the exploration as a new workbook. If you add comments to a custom view of a workbook, merge your changes into the workbook or save your custom view before commenting.

## User requirement

To view and add comments in workbooks, you must be assigned an [account type](/docs/create-and-manage-account-types) with the **Can comment on workbooks** permission enabled.

## View comments

To see comments on a workbook or data model, click the document name, then in the document menu, select **Comments**.  
A panel opens and displays all comment threads.  
![An example workbook with the comments panel open, showing a comment from Sigma Docs made 22 minutes ago saying This is the most useful workbook ever! with an option to reply. Above the comment is a text box to add new comments.](https://files.readme.io/33f3b8347bbc7f6b7f0169c3b9446f4d3b66e84dd00a41026e4c7e7f81174188-comments.png)

### Close the comments panel

To close the comments panel, ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/close2.svg) **Close comments panel** in the top right corner of the panel.

## Add a new comment

To add a new comment to a workbook or data model:

1. In the document header, click the document name, then in the document menu, select **Comments**.
2. Type your comment in the text box. You can @-mention other Sigma users in your comment to notify them of your comment.
3. Click **Comment** or press the keyboard shortcut (⌘ + enter on Mac, ctrl + enter on Windows).  
   ![Comment panel open for a data model on the data model overview page with an at-mention of @test@example.com, saying This is the data model I want you to use for the future! and options to comment or cancel.](https://files.readme.io/b33a5fd796e63c1e0de927f87335c951a5a4634f7e44001475ba3b6ba54db7f4-comment-at-data-model.png)

> 💡
>
> ### You can also add images to comments. See [Capture and annotate images in comments](/docs/annotate-element-images-as-comments).

## Comment on an individual element

To add a comment to a specific element:

1. Hover over the element.
2. Click the element menu at the element's top right corner.
3. Select **Comment**.  
   The comment panel opens with the the specific element selected.  
   ![Example workbook open with the comment panel open. The Organic Traffic by Country element is selected in the comment panel and on the canvas, with a comment of "@test@example.com Can you take a look at this?"](https://files.readme.io/778eb6543d8d60f3a05a29ef45f85a40d017c11d3ce089511c46813639ae3477-comment-at-element.png)
4. Enter your comment.
5. Click **Comment**.

## Mention a user in a comment

The mentioned users receive an email notification about your comment.

1. When adding a comment, type “@” and a list of all users who can be mentioned will appear.
2. Start searching for a user by typing their name or email.
3. Scroll or use the arrow keys to locate who you want to mention, then click or press Enter or Tab to select the user.
4. After you save your comment, the user receives an email notification.
5. If a mentioned user does not have permissions to view the workbook, a gray box appears under the comment prompting you to grant those permissions. To grant the user view access, click **Grant view access**. If you do not grant the user permission to view the workbook, they do not receive an email notification.

## Reply to a comment

To reply to a specific comment and start a comment thread:

1. In the **Comments** panel, scroll to the comment you want to reply to.
2. In the bottom left corner of the comment, click **Reply**.

   A text box opens.
3. Add your response.
4. Click **Reply** to add your reply.

## Manage comments

You can edit, delete, and resolve comments on a workbook or data model.

### Edit a comment

You can only edit your own comments. To modify a comment that you made:

1. In the **Comments** panel, locate the comment you want to edit, then click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**.
2. Select **Edit**.
3. Update the comment.
4. Click **Save changes**.

### Delete a comment

Users can delete their own comments. Users assigned the Admin account type can delete any comment.

1. In the **Comments** panel, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** for the comment that you want to edit.
2. Select **Delete**.

If the deleted comment had replies, the replies are still visible. If it had no replies, Sigma removes the thread.

### Resolve a comment thread

When you resolve a comment, the comment and any replies are hidden from the comments panel unless the option to **Show resolved** is turned on.

To resolve a comment thread:

1. Hover over the first comment in the comment thread that you want to resolve.
2. Select the checkbox ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/check-circle_outline.svg) (**Resolve thread**).  
   The entire comment thread is resolved, including replies to the resolved comment.

### Reopen a comment thread

To reopen a previously resolved comment thread:

1. From the comments panel, turn on the option to **See resolved**.
2. Scroll to the comment thread you want to reopen.
3. Click **Re-open thread**, or add a reply by clicking **Reply** at the bottom of the thread.  
   The comment thread is reopened.

## Find your comment notifications

All users who have published a version of the document receive email notifications for any comments added to the workbook or data model. In addition, when you are mentioned specifically in a comment, you receive an email notification. The email is titled “[Sigma Computing] New Mention on <workbook name>”.

Updated 3 days ago

---

[Highlight chart values](/docs/highlight-chart-values)[Capture and annotate images in comments](/docs/annotate-element-images-as-comments)

* [Table of Contents](#)
* + [User requirement](#user-requirement)
  + [View comments](#view-comments)
  + - [Close the comments panel](#close-the-comments-panel)
  + [Add a new comment](#add-a-new-comment)
  + [Comment on an individual element](#comment-on-an-individual-element)
  + [Mention a user in a comment](#mention-a-user-in-a-comment)
  + [Reply to a comment](#reply-to-a-comment)
  + [Manage comments](#manage-comments)
  + - [Edit a comment](#edit-a-comment)
    - [Delete a comment](#delete-a-comment)
    - [Resolve a comment thread](#resolve-a-comment-thread)
    - [Reopen a comment thread](#reopen-a-comment-thread)
  + [Find your comment notifications](#find-your-comment-notifications)