# Image elements

# Image elements

Image elements allow you to add images to a workbook page. You can upload a file directly to the image element, or display an image based on a static or dynamic URL.

## User requirements

To add and edit image elements:

* You must have **Can edit** or **Can explore** [access](/docs/folder-and-document-permissions#document-permissions) to the individual workbook.
* You must be in **Edit** or **Explore** mode for the workbook. See [workbook modes overview](/docs/workbook-modes-overview).

## Create an image element

To add an image element to a workbook:

1. In the **Add element** bar, select **UI** > **Image**. The new image element appears on the page.
2. Display an image in the image element using one of the following methods:
   1. [Upload an image to an image element](#upload-an-image-to-an-image-element)
   2. [Display an image from a static URL](#display-an-image-from-a-static-url)
   3. [Display an image from a dynamic URL](#display-an-image-from-a-dynamic-url)

### Upload an image to an image element

After creating an image element, you can upload a local image file to display it in your workbook:

1. In the editor panel, under **Properties**, set the toggle to **Upload**.
2. Select **Upload image**. The file browser opens.
3. Select an image file from the file browser and confirm.

The image appears in the image element.

### Display an image from a static URL

After creating an image element, you can display an image from a static URL:

1. In the editor panel, under **Properties**, set the toggle to **URL**.
2. Enter the URL in the **Image URL** field.

The image appears in the image element.

### Display an image from a dynamic URL

After creating an image element, you can display an image from a static URL:

1. In the editor panel, under **Properties**, set the toggle to **URL**.
2. Select the **Image URL** field and press `=` on the keyboard. A formula bar appears.
3. In the formula bar, configure a formula that outputs a URL.

The image appears in the element, and changes based on the formula.

> 📘
>
> ### For example, you can configure an image element based on the contents of a [control](/docs/intro-to-control-elements), a [Lookup](/docs/lookup) to a column in a data table, or use an [If](/docs/if) statement to change the image URL conditionally.

## Configure an image element

To configure the alt text and sizing of an image element:

1. In the editor panel, select the **Properties** tab, then configure the image properties:
   1. **Image alt**: Provide a description of the image used by screen readers and accessibility tools.
   2. **Sizing**: Select one of the available sizing options for the image:

| Sizing option | Description |
| --- | --- |
| **Shrink to fit** | Downsize the image to keep it entirely visible within the element. |
| **Scale to fit** | Expand the image to the maximum size, keeping it entirely visible within the element. |
| **Stretch to fit** | Stretch the image to match the size and aspect ratio of the element. |
| **Cover** | Expand the image so that the entire element is covered, even if it requires cropping. |
| **Default** | Maintain the original image dimensions regardless of the size of the element. |

To configure the border and corners of an image element:

1. In the editor panel, select the **Format** tab, then configure the following:
   1. **Border**: Set a border width and color for the element.
   2. **Corners**: Select square, round, or pill corners.

## Configure an action sequence on an image element

To configure actions and action sequences that execute when the image is clicked:

1. In the editor panel, select the **Actions** tab.

   1. By default, the image element has an empty **Action sequence** with an **On click** trigger.
2. Configure actions and action sequences as needed. For information about specific action effects and how to configure them, see [Action effects](/docs/intro-to-actions#action-effects) and the documentation linked in the table.

Updated 3 days ago

---

[Button elements](/docs/button-elements)[Text elements](/docs/text-elements)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Create an image element](#create-an-image-element)
  + - [Upload an image to an image element](#upload-an-image-to-an-image-element)
    - [Display an image from a static URL](#display-an-image-from-a-static-url)
    - [Display an image from a dynamic URL](#display-an-image-from-a-dynamic-url)
  + [Configure an image element](#configure-an-image-element)
  + [Configure an action sequence on an image element](#configure-an-action-sequence-on-an-image-element)