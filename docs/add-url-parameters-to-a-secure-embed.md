# Add URL parameters to a secure embed

# Add URL parameters to a secure embed

> 🚩
>
> Secure embeds with URLs that are secured with client credentials, formerly known as user-backed embeds, are deprecated as of August 4, 2025 and will reach end of support early next year. Instead, migrate to secure embed URLs signed with JSON Web Token (JWT). See [Migrate to secure embed URLs signed with JWT](/docs/migrate-to-jwt-signed-secure-embed-urls) .

After you [generate a secure embed path](/docs/generate-a-secure-embed-path) that you plan to sign with your embed credentials, use specific query string parameters on the embed URL to define the functionality of your embed:

* Set [required parameters](#required-parameters).
* Customize functionality and display with [interface parameters](#optional-interface-parameters).
* Manage access and data security with [security parameters](#optional-security-parameters) and [user attributes](#optional-user-attribute-parameters).

If you want to embed the tagged version of a workbook, reference the tag in the URL, then set query string parameters. See [Link to a tagged version of a workbook](/docs/add-version-tags-to-workbooks-and-data-models#link-to-a-tagged-version-of-a-workbook).

The best way to construct the embed URL is with code. For an example using JavaScript, see [Example embed API and URL](/docs/example-embed-api-and-url).

This document provides an overview of all required and optional embed URL parameters.

## Usage notes

Query string parameters are applied at the end of a URL path. The first parameter follows a question mark (`?`) and additional parameters are added after an ampersand (`&`).

For example:

`https://app.sigmacomputing.com/embed/{embedID}?:nonce={nonce}&:client_id={CLIENT_ID}&:mode=userbacked`

> 🚩
>
> ### Unless otherwise noted, each parameter listed in these reference tables must be prepended with a colon (:). For example, the parameter "nonce" should appear as ":nonce" in your secure embed URL.

Values that you provide in the embed URL must be URL-encoded, with some exceptions:

* If you provide multiple values for a parameter, such as for a user attribute, separate each value with a comma. Do not URL-encode the comma.
* Key values, such as a user attribute name or value, a team, a custom account type, or a custom theme, must not be encoded. If your user attribute, account type, team, or theme name contains spaces or special characters other than an underscore (`_`), consider changing the name.

For details about how to URL-encode values, see [Special characters for URL parameters](/docs/special-characters-for-url-parameters).

## Required parameters

The following parameters must be appended to the base URL (embed path) in the embed URL:

| Parameter | Description |
| --- | --- |
| `nonce` | A unique, random string used for security purposes. The value is valid for a single request. |
| client\_id | The ID paired with and used to define the embed secret. |
| mode | The embed type (must be set to `userbacked` for secure embeds) |
| email | The email address linked to the embed user's account. |
| external\_user\_id | A unique identifier for the embed user. This can be the user\_id value from the host application's security system, or another value associated with the individual user. |
| external\_user\_team | The Sigma team referenced to determine access and permissions. |
| session\_length | The duration (in seconds) of the embed URL's browser session validity. After the session expires, the embed URL must be regenerated with a new nonce. |
| time | A UNIX timestamp used with the `session_length` parameter. |
| signature | A Hash-based Message Authentication Code (HMAC) signature produced by combining the encrypted embed secret with a hash function. Unique to the message and key, the cryptographic signature authenticates the request and protects data integrity. This signature ensures that only parties with access to the secret key can verify the authenticity of the message. |

## Optional interface parameters

| Parameter | Description |
| --- | --- |
| control\_id | Set one or more values in a specific control element in the embedded content. Set one or more control values, depending on the type of control. See [Set control values with query string parameters](/docs/workbook-control-values-in-the-url).  Unlike other parameters, do not prepend this parameter with a colon. |
| disable\_mobile\_view | When set to `true`, disables automatic resizing for a mobile layout. |
| eval\_connection\_id | Dynamically switch the connection being used for any query in the embed.    Not supported on OAuth connections.   See [Embedding 14: Connection Swapping](https://quickstarts.sigmacomputing.com/guide/embedding_14_connection_swapping_v3/index.html) in the QuickStarts for a walkthrough of using this parameter.   **Usage notes:**   * Connection switching is not supported when using write-back features, such as input tables or materialization. * Connection switching overrides any user attribute-based warehouse or role switching. * Scheduled exports use the connection in the URL at the time the schedule was created or modified. * Immediate exports use the connection from the current URL. * The connection is used for any workbook opened in the embed session. * The connection replaces all connections used in the workbook.   You can use an ID returned from the [list connections API](https://help.sigmacomputing.com/reference/listconnections) or the connection listed in the URL. See [Indentify unique IDs in Sigma](https://help.sigmacomputing.com/reference/identify-unique-ids-in-sigma) for more information. |
| first\_name | Set the first name of the current embed user. When set, the name displays in the folder menu and system-generated emails. Must be used with the `last_name` parameter. When one or both is absent, a new member created in Sigma is named `Embed` (first) `User` (last). |
| hide\_bookmarks | When set to `true`, hides saved views from the embed menu. |
| hide\_folder\_navigation | When set to `true`, hides the folder navigation. |
| hide\_menu | When set to `true`, hides the embed menu in saved workbooks. Must be used with `menu_position` and only applies when `menu_position` is set to `top` or `bottom`. |
| hide\_run\_as\_recipient | When set to `true`, hides the **Run queries as recipient** option in the **Send Now** and **Schedule Exports** modals. |
| hide\_schedule | When set to `true`, hides the **Schedule exports** option in the embed menu in saved workbooks. |
| hide\_send | When set to `true`, hides the **Send now** option in the embed menu in saved workbooks. |
| hide\_sheet\_interactions | When set to `true`, hides sort and filter options in embedded elements. |
| hide\_tooltip | When set to `true`, hides chart mark tooltips. |
| last\_name | Set the last name of the current embed user. When set, the name displays in the folder menu and system-generated emails. Must be used with the `first_name` parameter. When one or both is absent, a new member created in Sigma is named `Embed` (first) `User` (last). |
| loading\_bg | Specify a custom background color with a hex code to the loading and error screens. |
| loading\_text | Specify a custom font color with a hex code to the loading and error text. |
| lng | Apply an existing translation added via [localization](/docs/manage-workbook-localization) to the embed. |
| lng\_variant | Apply a custom translation file added via [localization](/docs/manage-workbook-localization) to the embed. Must be used with `lng`. |
| menu\_position | Specify the toolbar position (`top`, `bottom`) or remove it (`none`). When no value is specified, defaults to `bottom`. |
| responsive\_height | When set to `true`, enables developer access to the JavaScript event called [`workbook:pageheight:onchange`](/docs/outbound-event-reference#workbookpageheightonchange).  For details, see the section about responsive iframes in the [Embedding 11: Responsive Embeds](https://quickstarts.sigmacomputing.com/guide/embedding_11_responsive_embeds_v3/index.html) Sigma QuickStart. |
| show\_footer | When set to `false`, hides the file explorer, workbook page tabs, **Save As** and **Edit** options, and Sigma logo in the embed footer. |
| showUnderlyingData | Whether the underlying data for a chart is shown when the embed first loads. When set to `false`, hides the underlying data behind a context menu. Only applicable to embeds that contain a single chart element. |
| theme | Apply a [workbook theme](/docs/create-and-manage-workbook-themes) by name, case sensitive. Specify one of the default workbook themes (`Light`, `Dark`, or `Surface`) or any custom theme defined for your organization. |
| use\_user\_name | Display the workbook owner's name instead of their email address in the embed menu and system-generated emails. |

## Optional security parameters

| Parameter | Description |
| --- | --- |
| account\_type | Apply the permissions granted to the specified [account type](/docs/user-account-types).  Recommendation: Set a value with the lowest level of permissions (for example, `View`), unless the embed users must be granted a higher level of permissions. |

## Optional user attribute parameters

[User attributes](/docs/user-attributes) are variables that users assigned the **Admin** account type can create in Sigma. The host application can use the embed API to apply user attribute parameters and update values at runtime for individual users, affecting all sessions for those users.

Example use cases for user attributes:

* Enforce row-level security for a dataset or data model. See [Apply row-level security to your secure embed](/docs/restrict-access-to-data-in-embedded-content#apply-row-level-security-to-your-secure-embed).
* Enforce row-level security using custom SQL with a `WHERE` clause. See [Set up row-level security](/docs/set-up-row-level-security).
* Dynamically switch the role of a user to take advantage of RBAC in your data platform. See [Dynamically assign data platform roles with a user attribute](/docs/restrict-access-to-data-in-embedded-content#dynamically-assign-data-platform-roles-with-a-user-attribute)
* Dynamically switch the Snowflake virtual warehouse to use different compute. See the note about Snowflake in [Dynamically assign roles used by a connection](/docs/dynamically-assign-roles-used-by-a-connection).

### Construct a user attribute parameter for a secure embed URL

To construct a user attribute parameter for a secure embed URL, do the following:

* Prepend the name of the user attribute with `:ua_`
* Include the name of the user attribute.
* Set the user attribute parameter equal to one or more values

For example:

`&:ua_Region=West,Midwest`

> 📘
>
> ### Do not encode any special characters in the name of the user attribute. If your user attribute contains special characters other than an underscore (`_`), consider renaming it.

### Example code for user attribute parameters

Example JavaScript code to apply a user attribute parameter and value in the embed URL.

This example code assumes that you have two environment variables set up:

* `uaName` to store the name of the user attribute.
* `uaValue` to store the value of the user attribute.

JavaScript

```
//Pass the user attribute name from Sigma and value to set it to:
searchParams += '&:ua_{uaName}={uaValue}';

// Example output:
// searchParams += '&:ua_Region=East';

// or for multiple values:
// searchParams += '&:ua_{uaName}={uaValue1},{uaValue2}';
// searchParams += '&:ua_Region=East,West';
```

Updated 3 days ago

---

[About Sigma](/docs/about-sigma)

* [Table of Contents](#)
* + [Usage notes](#usage-notes)
  + [Required parameters](#required-parameters)
  + [Optional interface parameters](#optional-interface-parameters)
  + [Optional security parameters](#optional-security-parameters)
  + [Optional user attribute parameters](#optional-user-attribute-parameters)
  + - [Construct a user attribute parameter for a secure embed URL](#construct-a-user-attribute-parameter-for-a-secure-embed-url)
    - [Example code for user attribute parameters](#example-code-for-user-attribute-parameters)