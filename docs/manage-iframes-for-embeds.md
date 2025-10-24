# Manage iframes for embeds

# Manage iframes for embeds

When utilizing Sigma's embedded analytics, you can implement static or responsive design solutions to optimize the viewing experience across a range of devices.

This document describes a few solutions that can help you achieve a the ideal design for your embedded Sigma content. For details about how to implement these solutions, see  [Embedding 11: Responsive Embeds](https://quickstarts.sigmacomputing.com/guide/embedding_11_responsive_embeds_v3/index.html) in the Sigma QuickStarts.

## Set a fixed iframe height in your CSS

Use CSS to set a fixed iframe height that displays most or all of the embedded content, regardless of screen size. This solution allows you to control content visibility up to the specified height. When the content exceeds the fixed height, the iframe features a scrollbar.

> 📘
>
> ### A fixed iframe height may result in excessive scrolling or content display issues (like overflow or truncation) depending on the screen size.

## Set a dynamic iframe height using the calc() function

Use the calc() function in your CSS to dynamically set the iframe height based on the viewport height and other page elements. You can also use the calc() function to dynamically compute values for other CSS properties.

> 📘
>
> ### The calc() function allows you to implement an iframe that's responsive to the viewport and other page elements, but it doesn't enable adjustments to content within the iframe.

## Adjust the iframe height using JavaScript (recommended)

Use JavaScript to dynamically adjust the iframe height based on the embedded content height. A JavaScript event listener detects the content height in real time (using the `workbook:pageheight:onchange` event) and adjusts the iframe height to match the content precisely.

Updated 3 days ago

---

[Outbound event reference](/docs/outbound-event-reference)[Configure a shareable link for an embed](/docs/configure-a-shareable-link-for-an-embed)

* [Table of Contents](#)
* + [Set a fixed iframe height in your CSS](#set-a-fixed-iframe-height-in-your-css)
  + [Set a dynamic iframe height using the calc() function](#set-a-dynamic-iframe-height-using-the-calc-function)
  + [Adjust the iframe height using JavaScript (recommended)](#adjust-the-iframe-height-using-javascript-recommended)