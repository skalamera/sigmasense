# Intro to UI elements

# Intro to UI elements

UI elements add additional context, styling, and navigation to workbook pages. They include buttons, dividers, images, spacers, embeds, and text.

## User requirements

To create and edit UI elements:

* You must have **Can edit** or **Can explore** [access](/docs/folder-and-document-permissions#document-permissions) to the individual workbook.
* You must be in a draft, custom view, or saved view of the workbook.

## UI element types

UI elements can be broken down into several distinct types, each with their own purpose and level of customization.

### Text

Text UI elements allow you to add titles and captions to your workbook pages. You can choose the size, style, and font. The text can include dynamic content from formulas. For more information, see [Text elements](/docs/text-elements).

### Image

Add an image by uploading a file or referencing a URL. Customize how the image fits within the element container, modify the element style, and configure it as an [action trigger](/docs/intro-to-actions#action-triggers). For more information, see [Image elements](/docs/image-elements).

### Button

Add a button to create a one-click action in a workbook. You can customize the button display and configure it as an [action trigger](/docs/intro-to-actions#action-triggers) that navigates to a specific destination, modifies or refreshes elements, downloads and exports data, etc. For more information, see [Button elements](/docs/create-a-button-element).

### Divider

Add a horizontal divider to visually partition elements or groups of elements on a page. You can customize the orientation, color, thickness, and alignment to match your needs and workbook design.

### Page break

The page break element allows greater control over the layout and formatting of PDF files. It specifies where breaks should occur in the exported PDF. You can not customize its formatting or appearance on the workbook page.

### Embed element

An embed element adds a webpage, video, or Sigma workbook to a workbook page. Any iFrame-enabled URL can be embedded. Use control variables and dynamic text within your embed URL to customize what content is displayed according to different inputs.

> 🚧
>
> ### URL fragments, such as anchor tags at the end of an iFrame-enabled URL, do not work with embed elements and will cause the element to break or display content incorrectly. Remove fragments from your iFrame URL before adding it to your embed element.

## Create a UI element

1. In the **Add element** bar, click **UI**.
2. Select a UI element. The new element appears on the page.
3. (Optional) Drag and drop the element anywhere on the page canvas to move it.
4. (Optional) Use the editor panel to configure the new element.

Updated 3 days ago

---

Related resources

* [Workbooks overview](/docs/workbooks-overview)
* [Intro to Element Types](/docs/intro-to-element-types)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [UI element types](#ui-element-types)
  + - [Text](#text)
    - [Image](#image)
    - [Button](#button)
    - [Divider](#divider)
    - [Page break](#page-break)
    - [Embed element](#embed-element)
  + [Create a UI element](#create-a-ui-element)