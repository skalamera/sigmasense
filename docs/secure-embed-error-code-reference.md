# Secure embed error code reference

# Secure embed error code reference

> 🚩
>
> Secure embeds with URLs that are secured with client credentials, formerly known as user-backed embeds, are deprecated as of August 4, 2025 and will reach end of support early next year. Instead, migrate to secure embed URLs signed with JSON Web Token (JWT). See [Migrate to secure embed URLs signed with JWT](/docs/migrate-to-jwt-signed-secure-embed-urls) .

This error code reference is specific to secure embed URLs secured with client credentials.

## General error codes

These error codes can be emitted while a user interacts with the embedded content.

| Error code | Definition | Possible cause |
| --- | --- | --- |
| EEXIST | Duplicate record detected. | User or team already exists. |
| EPERM | The requested operation is not permitted. | User does not exist in Sigma. |
| ESTALE | Stale object. | The workbook page, or element might have been deleted or archived, or the connection used by the embedded content was archived. |
| ENOENT | Object does not exist. | Embed was deleted or the embed user is deactivated. |
| EACCES | Permission denied. | The `:email` parameter matches an internal user that already has a Sigma account, the embedded workbook is not shared or no longer shared with the user, or the user does not have a required permission enabled on their assigned account type. |
| EINVAL | Invalid argument. | The embed URL is invalid. A URL parameter is mistyped or doesn't exist, an embed URL nonce has already been used, or one or more teams in the `external_user_team` that do not exist. |
| ETIMEDOUT | Request timed out. | A query sent to the warehouse timed out, including an export request. The warehouse is overloaded. |
| NETWORK | Unable to connect to Sigma. | Your local network is unavailable or a firewall or browser extension is preventing access to Sigma. |
| UNKNOWN | Default API error message for all other errors. | Some other error. |

## Parameter-based error messages

Some error messages are displayed to the user without a code. Most of these are due to invalid [query string parameters in the embed URL](/docs/embed-url-parameters):

| Error message | Description | Next step |
| --- | --- | --- |
| Invalid embed request. | Invalid embed mode. | Check that `mode=userbacked` for a secure embed. |
| Invalid embed request. ":email" is not valid. | Invalid email address. | Check the format of the email address in the `email` parameter. |
| Invalid embed request. ":session\_length" exceeds maximum | Invalid session length specified. | Check that the `:session_length` is less than **3600**. |
| Session expired. Reload the page. | Session length has been exceeded | Consider auto-refreshing the embed for your users on a timer to avoid this error. |
| The page you're looking for does not exist. Embed not found. | Invalid embed path. | Check the URL used for the embed and make sure that IDs are correctly formatted. |
| The specified teams in ":external\_user\_team" do not exist. Please check spelling or create new teams in the admin portal. | Invalid `external_user_team` (when team is specified) | Validate that the team specified in the `external_user_team` parameter exists. |
| You don't have permission to access this page. | Invalid clientID or `external_user_team` (when team is not specified) | Validate that your client ID is passed to the embed correctly and is active. |
| You don't have permission to access this page. Invalid embed signature. | Invalid embed secret | Validate that your embed secret is passed to the embed correctly and is active. |
| You don’t have permission to access this page. Sigma embed is expired. | Session length has been exceeded | Reload the page. Consider auto-refreshing the embed for your users on a timer to avoid this error. |

Updated 3 days ago

---

[About Sigma](/docs/about-sigma)

* [Table of Contents](#)
* + [General error codes](#general-error-codes)
  + [Parameter-based error messages](#parameter-based-error-messages)