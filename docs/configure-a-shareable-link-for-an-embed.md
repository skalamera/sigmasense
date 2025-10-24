# Configure a shareable link for an embed

# Configure a shareable link for an embed

You can enable your embed users to share workbooks, explorations, or bookmarks with other users using a link with your own domain name. Link sharing is not available for page or single element embeds.

These links can be copied and pasted, allowing recipients to access the content directly in your application. In addition, you can include the shareable link in the embed menu, embed footer, and scheduled export email notifications by configuring the `workbook:sharinglink:update` iframe event. See [Implement inbound and outbound events in embeds](/docs/inbound-and-outbound-events-in-embeds#workbooksharinglinkupdate) for details.

For a full example implementation, see [Embedding 13: Link Sharing](https://quickstarts.sigmacomputing.com/guide/embedding_13_link_sharing_v3/index.html#0) QuickStart and the accompanying sample code in the [GitHub repo](https://github.com/sigmacomputing/quickstarts-public/blob/main/embedding_qs_series_2/helpers/embed-api.js).

## Set up a shareable URL for your embed

To enable your embed users to share links, update your application code as follows:

1. Extract the `exploreKey` using the `workbook:exploreKey:onchange` iframe event. See [Outbound event reference](/docs/outbound-event-reference#workbookexplorekeyonchange).
2. Append a parameter that contains the `exploreKey` to your host application URL whenever an embed user makes or updates an exploration in your application.

   For example:

   JavaScript

   ```
   window.addEventListener('message', function (event) {
      if (event.source === document.getElementById('sigma-iframe').contentWindow &&
         event.origin === "https://app.sigmacomputing.com") {
         // Handle exploreKey changes
         if (event.data.type === 'workbook:exploreKey:onchange') {
            // Append exploreKey to your URL
            params.append(":exploreKey", event.data.exploreKey);
         }
      }
   });
   ```
3. Configure your application to parse the `exploreKey` from the URL when an embed user follows a link. This step allows your app to generate a secure embed URL for the embed user with the `exploreKey` so that Sigma can render the corresponding embed view. See [Create an embed API with JSON Web Tokens](/docs/create-an-embed-api-with-json-web-tokens) for a detailed example of how to generate a secure embed URL in your application.

   For example:

   JavaScript

   ```
   // Handle exploreKey if present
   const exploreKey = req.query.exploreKey;
   // Append exploreKey, if present, to the secure embed URL that will be passed to the iframe 
   if (exploreKey) {
       searchParams += `&:explore=${exploreKey}`;
   }
   searchParams += `&:bookmark=&{bookmarkId}`;
   ```
4. [optional] If you want your embed users to be able to share bookmarks, repeat steps 1 through 3 to extract the `bookmarkId` using the `workbook:bookmark:onchange` iframe event, append it to your host application URL, and include it as a parameter when generating your secure embed URL.

   For example:

   JavaScript

   ```
   window.addEventListener('message', function (event) {
    if (event.source === document.getElementById('sigma-iframe').contentWindow &&
        event.origin === "https://app.sigmacomputing.com") {
        // Handle bookmarkId changes
        if (event.data.type === 'workbook:bookmark:onchange') {
            // Append bookmarkId to your URL
            params.append(":bookmarkId", event.data.exploreKey); 
        }
    }
   });
   ```

   Example appending the bookmarkId to the embed URL:

   JavaScript

   ```
   // Handle bookmark if present
   const bookmarkId = req.query.bookmarkId;
   // Append bookmarkId, if present, to the secure embed URL that will be passed to the iframe
   if (bookmarkId) {
    searchParams += `&:bookmark=${bookmarkId}`;
   }
   ```

After you complete the above steps, users can share embeds with each other by copying and pasting the application URL from the browser address bar.

## Add sharing functionality to your application

1. Using `workbook:sharinglink:update`, provide the URL in the `sharingLink` property that will appear in the embed menu, embed footer, and scheduled exports. Include the `exploreKey` parameter in this link if you want the embed users to share explorations by default.
2. [optional] If you want to give the embed user the option to send a link to the current exploration or a link to the original workbook, supply a second URL that includes the value from the `exploreKey` parameter in the `sharingExplorationLink` property. If you want your users to always share their current exploration, you can choose to include the `exploreKey` in the value for `sharingLink` and omit the `sharingExplorationLink`. See [Inbound event reference](/docs/inbound-event-reference#workbooksharinglinkupdate) for details.

   For example:

   JavaScript

   ```
   // Function to send sharing links back to Sigma
   function sendSharingLinks() {
    const baseUrl = window.location.origin + window.location.pathname;
    const sharingLink = currentBookmarkId
        ? `${baseUrl}?&bookmark=${currentBookmarkId}`
        : baseUrl;
    const sharingExplorationLink = currentExploreKey
        ? currentBookmarkId
            ? `${baseUrl}?explore=${currentExploreKey}&bookmark=${currentBookmarkId}`
            : `${baseUrl}?explore=${currentExploreKey}`
        : null;
    iframe.contentWindow.postMessage(
        {
            type: "workbook:sharinglink:update",
            sharingLink: sharingLink,
            sharingExplorationLink: sharingExplorationLink,
        },
        "https://app.sigmacomputing.com"
    );
   }
   ```

   > 📘
   >
   > ### Sigma loads the URL you supply using this event to anyone given this sharing link. Ensure that your application authenticates users before displaying the content.

## Test the sharing links in your embed

After you complete the steps to set up shareable URLs and add them to your application, test the results in your application.

1. Confirm that a ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/share-user.svg) share icon appears in the footer of your embedded content and that the **Share...** option appears in the embed menu.

   > 📘
   >
   > ### If you configured your embed to exclude a footer, you can construct your own share modal or button in your application and supply the sharing link to your users that way.
2. Start customizing your embedded content, then click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/share-user.svg) **Share**.
3. In the **Share this content** modal, confirm that the **Link to current exploration** checkbox appears.

   > 📘
   >
   > ### The **Link to current exploration** checkbox appears only if the user has an active exploration on the embed and the embed application developer supplied a `sharingExplorationLink`.
4. Click **Copy Link** to test the link with the checkbox deselected. In a new private browser window, test the link to confirm that your user authentication works as you have configured it for your embed and that the page resolves to the URL configured in the `sharingLink` property.
5. If you see a **Link to custom view** checkbox, select the checkbox, then click **Copy Link** again. In a new private browser window, test the link to confirm that your user authentication works as you have configured it for your embed and that the page resolves to the URL configured in the `sharingExplorationLink` property.
6. In the embed menu, click **Schedule exports...**.
7. Create a new export schedule to send to your own email address, then click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Send now**.
8. Confirm that the email you receive contains an **Open** button. Click the **Open** button to confirm that your user authentication works as you have configured it for your embed and that page resolves to the URL configured in the `sharingLink` property.

Updated 3 days ago

---

[Manage iframes for embeds](/docs/manage-iframes-for-embeds)[Embed SDK for React](/docs/embed-sdk-for-react)

* [Table of Contents](#)
* + [Set up a shareable URL for your embed](#set-up-a-shareable-url-for-your-embed)
  + [Add sharing functionality to your application](#add-sharing-functionality-to-your-application)
  + [Test the sharing links in your embed](#test-the-sharing-links-in-your-embed)