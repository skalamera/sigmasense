# Capture and annotate images in comments

# Capture and annotate images in comments

Sigma allows you to capture images of workbook elements, which you can annotate and share in comments.

This document explains how to capture and annotate images.

## System and user requirements

The ability to annotate screenshots requires the following:

* You must be the workbook owner or be granted **Can explore** workbook permission.
* The workbook must be saved. *Comments are not supported in[explorations](/docs/ad-hoc-data-explorations).*

## Image storage and deletion

Sigma stores annotated screenshots in its cloud storage. Sigma encrypts images on the server side with an encryption key that is unique to your organization. Access to the stored images is protected by IAM policy and requires user authentication and permission to the workbook it is from. Sigma also encrypts images during transit via TLS.

By default, images expire after 90 days. Sigma deletes images within 24 hours of expiration. A Sigma organization’s Admin can update the expiration policy to extend it up to 2 years or reduce it down to the 1 day minimum.

To delete all images from an organization, an Admin can set the image time out period to 1 then turn off annotations. All images will be deleted from Sigma storage within 48 hours.

Comments with deleted annotated images show a placeholder where the images used to be. All the text in the comments remain.

## Capture and annotate an image of an element

1. From the element's menu, select **Comment**.

   A menu opens to the right of the workbook page with options to add a comment.

   ![Comment menu with the element selected, a text box to add a comment, an option to capture a screenshot, and cancel and comment buttons.](https://files.readme.io/0a2fa88-comment-image-context.png)
2. Select **Capture screenshot**.
3. In the modal that appears, annotate the image by drawing with your cursor.

   * (Optional) Change the color of the line using the color picker.
   * (Optional) Use the undo/redo options.

   ![Modal with an image of the element, a color picker, and undo and redo buttons. This example is a gauge chart with the gauge pointing to a value less than a reference line, with a red circle around the gap. A comment asks "What are we doing to get back on track and reach our goal?](https://files.readme.io/a6b4eee-comment-image-modal.png)
4. Add a comment to the image. Use the @username convention to mention team members in your comment.
5. Click **Share in comment**.   
   Sigma places the annotated image in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/comment.svg) **Comments** panel of the workbook and sends an email to the users mentioned in the comment.

   ![Workbook comments pane open with an option to add a comment, and the added comment with the element name as the title, workbook name mentioned, image of the element, and comment below.](https://files.readme.io/170631d-comment-image-final.png)

Updated 3 days ago

---

Related resources

* [Workbook comments](/docs/workbook-comments)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Image storage and deletion](#image-storage-and-deletion)
  + [Capture and annotate an image of an element](#capture-and-annotate-an-image-of-an-element)