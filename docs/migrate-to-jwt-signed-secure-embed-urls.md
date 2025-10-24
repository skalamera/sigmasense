# Migrate to JWT-signed secure embed URLs

# Migrate to JWT-signed secure embed URLs

If you securely embed Sigma into your host application, you must use JSON Web Tokens (JWT) to sign your secure embed URLs. This document guides you through the key differences in functionality between secure embed URLs secured with client credentials and secure embed URLs signed with JWT, as well as the steps involved to migrate to secure embed URLs signed with JWT.

> 🚩
>
> ### Secure embeds with URLs that are secured with client credentials, formerly known as user-backed embeds, are deprecated as of August 4, 2025 and will reach end of support early next year. Instead, migrate to secure embed URLs signed with JSON Web Token (JWT).

Secure embed URLs signed with JWT offer several improvements to embed URLs secured with client credentials:

* Simplified embed management:

  + JWT-based secure embeds are associated with the embed API key, instead of a specific Sigma user that owns the embed.
  + Edit embeds directly, instead of logging in to Sigma.
* Simplified user management enables stricter security:

  + Existing Sigma users can use their existing accounts
  + Disable automatic user generation
  + Remove team names, account types, and user attributes from the URL
* Expanded embed functionality

  + [Embed Ask Sigma](/docs/embed-ask-sigma).

## Key differences

Secure embeds that use JWT are functionally very similar to secure embeds secured with client credentials. Both use an iframe with a parameterized URL to securely embed content from Sigma, but there are some key differences:

| Functionality | URLs secured with client credentials | URLs signed with JWT |
| --- | --- | --- |
| User account used to access | Embed accounts | Embed and internal accounts |
| Automatically generate embed users | Always yes | Optionally turned off |
| ID used to reference the embedded content | Create an embed ID | Use the workbook ID |
| Support for embed URL parameters | All current URL parameters | Limited set of URL parameters |
| Workbook editing by embed users | Requires a workaround | Direct editing supported |
| URL signing | Entire URL is signed | Only JWT is signed |
| Admin management of the embed | Embed owner and client credentials owner | Client credentials owner |
| Embed Ask Sigma | Not supported | Supported |

## Migrate to JWT-signed secure embed URLs

To migrate from secure embed URLs secured with client credentials to secure embed URLs signed with JWT, you must replace several embed URL parameters with JWT claims and update your server side API function to generate new URLs signed with a JWT.

To migrate to JWT-signed secure embed URLs, do the following:

1. [Review and update the URL parameters used by existing embeds](#review-and-update-existing-url-parameters).
2. [(Optional) Update the embed API key](#optionally-update-the-embed-api-key).
3. [Update the server side API function that generates embed URLs](#update-the-server-side-api-function-that-generates-embed-urls).
4. [Test and clean up previous embed artifacts](#test-and-clean-up-previous-embed-artifacts).

> 💡
>
> ### Users with access to view the usage dashboards in Sigma can identify existing embed URLs with the **Embedding** usage dashboard. Filter the dashboard by an **Embed Type** of `application - userbacked`.

### Review and update existing URL parameters

While secure embed URLs secured with client credentials use URL parameters for most customization options and settings, JWT-signed secure embed URLs use a combination of JWT claims and URL parameters. To migrate your secure embed URLs:

1. Review the URL parameters that you currently use.
2. Identify parameters that are unsupported or need to be replaced.

Only some URL parameters are supported in secure embed URLs signed with JWT. For the full list of supported URL parameters, see [Embed URL parameters](/docs/embed-url-parameters).

For unsupported URL parameters, review the following list for options:

| URL parameter | JWT option |
| --- | --- |
| `hide_run_as_recipient` | Disable the **Run exports as recipient** account type permission for embed users. |
| `hide_schedule` | Disable the **Schedule export** account type permission for embed users. |
| `hide_send` | Disable the **Download** account type permission for embed users. |
| `loading_bg` `loading_text` | Display a custom loading page, triggered by the `workbook:loaded` JavaScript event. For implementation, consider using the [Embed SDK for React](/docs/embed-sdk-for-react). |
| `show_footer` | Use the `menu_position` URL parameter to manage the position of the menu instead. |
| `hide_sheet_interactions` | Not supported. |
| `showUnderlyingData` | Not supported. |
| `use_user_name` | Not supported. |

Several URL parameters are not supported, but have direct equivalents as [JWT claims](/docs/json-web-token-claims-reference):

| URL parameter | JWT claim |
| --- | --- |
| `nonce` | `JTI` |
| `eval_connection_id` | `eval_connection_id` |
| `first_name` `last_name` | `first_name` `last_name` |
| `account_type` | `account_type` |
| `teams` | `teams` |
| `user_attributes` | `user_attributes` |

All URL parameters in a secure embed URL signed with JWT are visible to the user of the embed. As such, review the URL parameters that you currently set and determine if any should not be visible to the end users.

> 🚧
>
> ### If you use control values in the embed URL for row-level security (RLS), use user attributes instead and use the `user_attributes` JWT claim to manage the values. See [Restrict access to data in embedded content](/docs/restrict-access-to-data-in-embedded-content).

### Optionally update the embed API key

If you want to manage your JWT-signed secure embed URLs separately from the deprecated, non-JWT-signed secure embed URLs, create a new embed API key to use for signing the JWT-signed secure embed URLs.

> 🚩
>
> ### This step is not required — you can continue to use your existing embed API credentials for signing the JWT-signed secure embed URLs.

Creating a new embed API key also simplifies the cleanup process after you migrate your secure embed URLs to be signed by JWT. After you update your secure embed URLs to be signed with JWT, you can deactivate the old embed API key to prevent access to any secure embed URLs that are not signed by JWT.

To create new credentials, see [Generate embed client credentials](/docs/generate-embed-client-credentials).

### Update the server side API function that generates embed URLs

The most important part of the migration process is to update the server-side API function that you use to generate embed URLs:

1. [Update the URLs](#update-the-urls-in-use)
2. [Add a JWT](#write-a-new-function)

#### Update the URLs in use

Secure embed URLs signed with JWT use the workbook URL instead of a specific embed URL. All URLs still begin with `https://app.sigmacomputing.com`, but the rest of the base URLs that you use to construct secure embed URLs must be updated:

| Workbook type | Deprecated URL path | JWT-signed URL path |
| --- | --- | --- |
| Untagged workbook | `/embed/<embedId>` | `/<organizationSlug>/workbook/<workbookId>` |
| Tagged workbook | `/embed/<embedId>/tag/<tagName>` | `/<organizationSlug>/workbook/<workbookId>/tag/<tagName>` |
| Edit a workbook | `/embed/<embedId>/workbook/<workbookName>-<Id>/edit` | `/<organizationSlug>/workbook/<workbookId>/edit` |

For example, for an organization slug of `sigma-docs` tagged with `prod`, the URL would change from:

* Deprecated: `https://app.sigmacomputing.com/embed/1-1abCDEFG2hIjKLMnopqrST/tag/prod`
* JWT: `https://app.sigmacomputing.com/sigma-docs/workbook/12aBc3DEFgHiJk4lmnOPq5/tag/prod`

For more details, see [Create an embed API with JSON Web Tokens](/docs/create-an-embed-api-with-json-web-tokens).

#### Write a new function

With JWT embedding, your code must generate a JWT with parameters. Use a JavaScript library that can take in parameters and return a JWT, such as [jose](https://www.npmjs.com/package/jose) or [jsonwebtoken](https://www.npmjs.com/package/jsonwebtoken).

Keep any code that generates a UUID, then pass the nonce and your client credentials into a JWT generator and append the output to the workbook URL.

> 📘
>
> ### If you previously used the Sigma REST API endpoint [Create an embed for a workbook](/reference/createworkbookembed) (`POST /v2/workbooks/{workbookId}/embeds`) to create an embed URL to use for secure embedding, update your code to instead call the [List workbooks](/reference/listworkbooks) endpoint (`GET /v2/workbooks`) and use the `url` field in the response. If you only embed workbooks with a specific tag, you can also use the [List workbooks for a tag](/reference/listworkbooksfortag) endpoint (`GET /v2/tags/{tagId}/workbooks`) and use the `url` field in the response.

For more details, see [Create an embed API with JSON Web Tokens](/docs/create-an-embed-api-with-json-web-tokens).

If you want to allow internal users to log in to the embed, the embed code must be updated to support JWTs for internal users and different JWTs for embed users. A JWT-signed secure embed URL accessed by an internal user must not contain claims for `teams`, `user_attributes`, or `account_types`, because the team membership, user attributes, and account type permissions enabled for the Sigma user are used instead. See [Manage access to a secure embed](/docs/manage-access-to-a-secure-embed) for more details.

### Test and clean up previous embed artifacts

After setting up your new JWT-signed secure embed URLs, test them to make sure everything works as expected.

If your new secure embed URLs are working as desired, consider performing the following steps to remove deprecated secure embed URLs from your system:

* Delete the deprecated embeds.
* If you used the ["Landing Page" workaround](https://community.sigmacomputing.com/t/user-backed-embedding-custom-dashboard-homepage-set-by-users/2589) to enable editing a secure embed, delete the workbook(s) used to support that workaround.
* If internal users accessed secure embeds using duplicate, embed-specific accounts, deactivate the duplicate accounts.
* If you created new client credentials specifically for JWT-signed secure embed URLs, revoke the credentials used to sign the deprecated secure embed URLs.

Updated 3 days ago

---

[Intro to embedded analytics](/docs/intro-to-embedded-analytics)[Public embedding](/docs/public-embedding)

* [Table of Contents](#)
* + [Key differences](#key-differences)
  + [Migrate to JWT-signed secure embed URLs](#migrate-to-jwt-signed-secure-embed-urls)
  + - [Review and update existing URL parameters](#review-and-update-existing-url-parameters)
    - [Optionally update the embed API key](#optionally-update-the-embed-api-key)
    - [Update the server side API function that generates embed URLs](#update-the-server-side-api-function-that-generates-embed-urls)
    - [Test and clean up previous embed artifacts](#test-and-clean-up-previous-embed-artifacts)