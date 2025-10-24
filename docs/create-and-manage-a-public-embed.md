# Create and manage a public embed

# Create and manage a public embed

Public embedding allows you to share publicly accessible Sigma content (an entire workbook, a specific page, or an individual chart or table element) and is typically used to display non-sensitive information. Public embeds reflect real-time data in your CDW or DBMS in addition to any changes published in the embedded workbook.

This document provides an overview of public embed access and explains how to create and manage a public embed.

## System and user requirements

The ability to create and manage public embeds requires the following:

* Public embedding must be enabled for your organization. See [Enable or disable public embeds](/docs/enable-or-disable-public-embeds).

* You must be assigned the **Admin** [account type](/docs/user-account-types).

## Public embed access

### Who can access a public embed?

Public embeds are accessible to anyone with the public URL or access to the host application in which the content is embedded.

### What data can users access in a public embed?

Embed users can only view and interact with the data presented in the embedded content. This includes the ability to set the value of any control element included in the embed.

Additional data can only be accessed by members of your Sigma organization with the required [workbook permissions](/docs/generate-a-secure-embed-path#share-the-workbook-with-the-embed-user-team).

### What can users export from a public embed?

Public embeds limit users to PNG export. Data cannot be exported to Excel, CSV, or PDF. This applies to all export functionality, including download buttons within the embed.

## Generate a public URL

Before you can embed workbook content, you must generate a public URL. You can then share this URL as a direct link or use it in an `<iframe>` tag to integrate the content into an application outside of Sigma.

1. Open an existing workbook or [create a new one](/docs/create-a-workbook).
2. In the workbook header, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) associated with the workbook's name.
3. In the document menu, select **Share and export** > **Embedding**.
4. In the **Embed workbook** modal, select the **Public** tab.
5. In the **Generate public URL for** dropdown, select the content you want to embed. This can be the entire workbook, a specific page, or an individual chart or table element.

   ![Embed workbook modal with generate public URL dropdown open to show the entire workbook, page 1 of the workbook, and two elements in the workbook by name.](https://files.readme.io/a2295fb7e83e0862c4440f974d31329721a02ddbb4755aef7e0d777c79e13857-public-embed-menu.png)
   > 📘
   >
   > ### If you want to embed a workbook page that opens a modal, you must embed the entire workbook.
6. Sigma immediately generates a public link and embed code. To direct users to the selected content as a web page, copy and share the public link. To integrate the selected content within an application outside of Sigma, copy the embed code and see [Display the public embed in a host application](#display-the-public-embed-in-a-host-application) for more information.

   ![Embed workbook modal with generated public link and the embed code for the generated public embed visible. The embed code provides default iframe syntax.](https://files.readme.io/c4302f7faf139f3c043305d2a3cbc993d19c2c1a3e54b6368e4a496cbdddaaa6-embed-code-public.png)

### Display the public embed in a host application

Use the embed code in an HTML document to integrate the selected Sigma content directly into another application.

1. In the HTML document, paste the embed code copied from the **Embed workbook** modal when you generated the public embed path.

   Example HTML

   ```
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Sigma Public Embed Sample</title>
       <style>
           body {
               margin: 0;
               height: 100vh;
               display: flex;
               flex-direction: column;
               align-items: center;
               justify-content: center;
           }
           iframe {
               border: none;
               width: 80%; /* Adjust width as needed */
               height: 80%; /* Adjust height as needed */
               max-width: 1000px; /* Max width limit */
           }
       </style>
   </head>
   <body>
       <h2>Sigma - Public Embed Sample</h2>
       <iframe src="https://app.sigmacomputing.com/embed/1-3UYrtvMY7HQPQgtIxBizvJ"></iframe>
   </body>
   </html>
   ```
2. Preview the HTML document in a browser to ensure the embedded content displays as expected.

   ![](https://files.readme.io/4148fd7-image.png)

## Delete a public URL

Delete a public URL to prevent the content from being shared publicly. This action permanently removes the URL from the corresponding workbook and breaks existing links and embeds that reference it.

1. Open the workbook containing the embed you want to delete.
2. In the workbook header, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) associated with the workbook's name.
3. In the document menu, select **Share and export** > **Embedding**.
4. In the **Embed workbook** modal, select the **Public** tab.
5. Locate the public URL you want to delete, then click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/trash.svg) **Delete embed**.

   ![Embed workbook modal with generated public link and the embed code for the generated public embed visible. The embed code provides default iframe syntax.](https://files.readme.io/c4302f7faf139f3c043305d2a3cbc993d19c2c1a3e54b6368e4a496cbdddaaa6-embed-code-public.png)
6. In the confirmation modal, click **Delete**.

   > 💡
   >
   > If you previously used the embed code to integrate the Sigma content into another application, make sure that you delete the embed code from the applicable HTML document.

Updated 3 days ago

---

Related resources

* [Enable or disable public embeds](/docs/enable-or-disable-public-embeds)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Public embed access](#public-embed-access)
  + - [Who can access a public embed?](#who-can-access-a-public-embed)
    - [What data can users access in a public embed?](#what-data-can-users-access-in-a-public-embed)
    - [What can users export from a public embed?](#what-can-users-export-from-a-public-embed)
  + [Generate a public URL](#generate-a-public-url)
  + - [Display the public embed in a host application](#display-the-public-embed-in-a-host-application)
  + [Delete a public URL](#delete-a-public-url)