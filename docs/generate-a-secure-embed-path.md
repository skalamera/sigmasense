# Generate a secure embed path

# Generate a secure embed path

> 🚩
>
> Secure embeds with URLs that are secured with client credentials, formerly known as user-backed embeds, are deprecated as of August 4, 2025 and will reach end of support early next year. Instead, migrate to secure embed URLs signed with JSON Web Token (JWT). See [Migrate to secure embed URLs signed with JWT](/docs/migrate-to-jwt-signed-secure-embed-urls) .

To create a secure embed within a host application, you must first generate a secure embed path (URL) that points to the specific Sigma content you want to embed (an entire workbook, a specific page, or an individual chart or table element.)

> 📘
>
> ### This step is only necessary if you are creating secure embed URLs without JSON Web Tokens (JWTs). If you are signing your embed URLs with JWTs, see [What URL to use](/docs/create-an-embed-api-with-json-web-tokens#what-url-to-use) to construct your secure URL.

This document provides an overview of the requirements and explains how to generate a secure embed path.

## System and user requirements

The ability to create and manage embeds requires the following:

* Secure embedding must be enabled for your organization.
* You must be assigned the **Admin** [account type](/docs/user-account-types) or have been granted embedding credentials by an admin. See [Generate embed client credentials](/docs/generate-embed-client-credentials) for more information.
* You must have created at least one embed user team and shared the content you want to embed with that team. See [Create a team for embed users](/docs/create-a-team-for-embed-users).

## Generate the secure embed path

Before you can embed Sigma content into a host application, you must generate a secure embed path within Sigma.

1. Open the workbook containing the content you want to embed.
2. Ensure that the version of the content you want to embed is published. If it isn't, open the workbook in **Edit** mode and click **Publish**.

   > 📘
   >
   > ### Embeds only display published content. If a workbook, page, or element is updated in the draft version and not published, the embed displays the published version.
3. In the workbook header, click the caret (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) associated with the workbook's name.
4. In the workbook menu, select **Embedding**.

   ![](https://files.readme.io/d99518cc274b236950d34ab6a418c55fe382c600ef301f7e422f19251bfc7919-embedding-in-menu.png)
5. In the **Embed workbook** modal, select the **Secure** tab.
6. In the **Generate secure embed path for** dropdown, select the content you want to embed. This can be the entire workbook, a specific page, or an individual chart or table element.

   ![](https://files.readme.io/b55008db0e0d661e3e0079b953e3348b5e6a48b5f9563cc35b51d25285100ea1-select-content-to-embed.png)
   > 📘
   >
   > ### If you want to embed a workbook page that opens a modal, you must embed the entire workbook.
7. Sigma immediately generates a secure embed path. Click **Copy** to use the URL in the host application's API.

   You can securely store the embed path for future reference, or you can return to this modal to retrieve the embed path at any time.

   ![](https://files.readme.io/343ec6f33e0ad3da197ab035ef4ae30df7c34f5a4129d8b7c1780ed7b26090c7-copy-secure-embed-path.png)
8. To test the embed in Sigma's embed sandbox, click **Test** and see [Test embeds in sandbox environment](/docs/test-an-embed-url-in-the-embed-sandbox).

Updated 3 days ago

---

[About Sigma](/docs/about-sigma)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Generate the secure embed path](#generate-the-secure-embed-path)