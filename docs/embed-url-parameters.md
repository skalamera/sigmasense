# Embed URL parameters

# Embed URL parameters

When you create a secure embed, you can use URL query string parameters to customize additional functionality, in addition to what is provided by [JWT claims](/docs/json-web-token-claims-reference) for your secure embed.

The query string parameters listed in the [available interface parameters](#available-interface-parameters) table are supported for a JWT-signed URL.

> 📘
>
> For details about URL parameters available for secure embed URLs secured with client credentials, see [Add URL parameters to a secure embed](/docs/add-url-parameters-to-a-secure-embed).

You can also set control values using query string parameters, making sure that your secure embed loads with specific control values specified. See [Set control values in a URL using query string parameters](/docs/workbook-control-values-in-the-url).

## Usage notes

Query string parameters are applied at the end of a URL path. The first parameter follows a question mark (`?`) and additional parameters are added after an ampersand (`&`).

Values that you provide in the embed URL must be URL-encoded. For details, see [URL encoding reference for parameters](/docs/special-characters-for-url-parameters).

Ensure that each URL parameter is prefixed with a colon (`:`).

> 📘
>
> If a parameter contains multiple values, do not encode the commas separating the values. In your URL, the value of your parameter should be passed to Sigma as `value1,value2` rather than `value1%2Cvalue2`.

## Available interface parameters

| Parameter | Description |
| --- | --- |
| `hide_bookmarks` | When set to `true`, hides saved views from the embed menu. |
| `hide_explore_toggle` | When set to `true`, hides explore toggle from the embed menu. |
| `hide_folder_navigation` | When set to `true`, hides the folder navigation. |
| `hide_menu` | When set to `true`, hides the embed menu in saved workbooks. Must be used with `menu_position` and only applies when `menu_position` is set to `top` or `bottom`. |
| `hide_tooltip` | When set to `true`, hides chart mark tooltips. |
| `lng` | Sets the language to use for Sigma text to the embed. If a [translation file is defined](/docs/manage-workbook-localization) for that locale, applies any defined translations to custom text in the workbook. |
| `lng_variant` | Applies any defined translations from a [custom translation file](/docs/manage-workbook-localization) to the embed. Must be used with `lng`. |
| `menu_position` | Changes the toolbar position (`top`, `bottom`) or removes it (`none`). When no value is specified, defaults to `none`. |
| `responsive_height` | When set to `true`, enables developer access to the JavaScript event called [`workbook:pageheight:onchange`](/docs/outbound-event-reference#workbookpageheightonchange). If adding this parameter to workbook edit URLs (which include `/edit`), set to `false`. |
| `theme` | Apply a [workbook theme](/docs/create-and-manage-workbook-themes) by name, case sensitive. Specify one of the default workbook themes (`Light`, `Dark`, or `Surface`) or any custom theme defined for your organization. |

Parameters not listed in this table are available as [JWT claims](/docs/json-web-token-claims-reference), account type permissions, or are not supported.

> 💡
>
> ### For more information about the `responsive_height` parameter and implementing responsive embeds, see the section about responsive iframes in the [Embedding 11: Responsive Embeds](https://quickstarts.sigmacomputing.com/guide/embedding_11_responsive_embeds_v3/index.html) Sigma QuickStart.

Updated 3 days ago

---

[JSON web token claims reference](/docs/json-web-token-claims-reference)[URL encoding reference for parameters](/docs/special-characters-for-url-parameters)

* [Table of Contents](#)
* + [Usage notes](#usage-notes)
  + [Available interface parameters](#available-interface-parameters)