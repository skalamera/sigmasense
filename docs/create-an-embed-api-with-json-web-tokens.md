# Create an embed API with JSON Web Tokens

# Create an embed API with JSON Web Tokens

Sigma authenticates secure embeds using [JSON Web Tokens (JWTs)](https://jwt.io/). JWTs offer a secure way to embed content that can be accessed by both external users (users who do not have a registered account in Sigma) and internal users (users who access Sigma directly through their Sigma account).

## Configure your URL

You need to configure a URL for your embed by building out a base URL and then adding the specific parameters and claims you want to use:

* [What URL to use](#what-url-to-use)
* [Add your JWT claims](#add-your-jwt-claims)
* [Apply URL control values and string parameters](#apply-url-control-values-and-string-parameters)
* [Example script to generate a JWT-signed secure URL](#example-script-to-generate-a-jwt-signed-secure-url)
* [Example server-side API with JWT](#example-server-side-api-with-jwt)

### What URL to use

Embeds require a URL path to be provided in the signing process. The URL syntax varies depending on whether you are embedding a workbook, a page, a single element, or the Ask Sigma interface.

|  |  |
| --- | --- |
| Workbook | Navigate to the workbook that you intend to embed, ensure it is in Published mode, and copy the URL directly from the browser without altering the syntax.  API syntax for a workbook:  `https://app.sigmacomputing.com/organization-slug/workbook/workbookName/workbookId`  URL syntax for a workbook:  `https://app.sigmacomputing.com/organization-slug/workbook/workbookName-workbookId` |
| Tagged workbook version | For tagged versions of a workbook, add /tag/tagName to the URL. The /tag/tagName must come after the /workbook/workbookName-workbookUrlId path segment of a URL.  API syntax for a workbook:  `https://app.sigmacomputing.com/organization-slug/workbook/workbookName/workbookId/tag/tagName`  URL syntax for a workbook:  `https://app.sigmacomputing.com/organization-slug/workbook/workbookName-workbookId/tag/tagName` |
| Page | Select the desired workbook page, then copy the URL and edit it to follow the example syntax.  API syntax for a page:  `https://app.sigmacomputing.com/organization-slug/workbook/workbookId/page/pageId`  URL syntax for a page:  `https://app.sigmacomputing.com/organization-slug/workbook/workbookName-workbookId/page/pageId` |
| Single element | Select the desired workbook element, then copy the URL and edit it, following the example syntax.  API syntax for a page:  `https://app.sigmacomputing.com/organization-slug/workbook/workbookId/element/elementId`  URL syntax for a single element:  `https://app.sigmacomputing.com/organization-slug/workbook/workbookName-workbookId/element/elementId` |
| Ask Sigma | Copy the URL and edit it, following the example syntax.  URL syntax for Ask Sigma:  `https://app.sigmacomputing.com/organization-slug/ask`  For more about embedding Ask Sigma with JWT, see [Embed Ask Sigma](/docs/embed-ask-sigma-beta). |

> 📘
>
> ### The `/tag/tagName` parameter is optional, but must come after the `/workbook/workbookName-workbookUrlId` path segment of a URL.

### Add your JWT claims

Instead of URL parameters, JWT signed URLs use claims to specify parameters. See the [JWT claims reference](/docs/json-web-token-claims-reference) topic for details on how to specify parameters in a JWT-signed URL.

### Sign your JWT with client credentials and secret

Use client credentials in your JWT to secure access to embed URL.

1. Enter your client ID in the `kid` claim.
2. Use your corresponding JWT package for your desired coding language to enter your client secret. The JavaScript [example](/docs/create-an-embed-api-with-json-web-tokens#example-server-side-api-with-jwt) below uses the `jwt.sign` function.

### Apply URL control values and string parameters

JWT-signed URLs support applying control values with URL parameters. See [Set control values in a URL using query string parameters](/docs/workbook-control-values-in-the-url). This enables you to pre-populate the control values in an embedded workbook.

For a complete list of string parameters, see [Embed URL parameters](/docs/embed-url-parameters).

## Example script to generate a JWT-signed secure URL

The following script demonstrates how to programmatically generate a secure URL signed with a JWT.

The script makes use of an environment file for some required values. In a production environment, these values would be generated dynamically by the parent application. See [Generate embed client credentials](/docs/generate-embed-client-credentials) for instructions on how to generate the embed client id and secret.

```
# .env file

# Required Embed Configuration
BASE_URL={url path to embed}
CLIENT_ID={your client id}
SECRET={your embed secret}

# User-Specific JWT Claims
EMAIL={your embed user's email}
ACCOUNT_TYPE={embed user's account type}
TEAM={embed user's team}
```

## Example server-side API with JWT

Values in the .env file (except keys) are typically generated at runtime by the parent application. This example script is written in JavaScript and uses the `jsonwebtoken` package. Refer to the documentation for the package you use for the construction of the JWT and how to pass claims.

JavaScript

```
const jwt = require('jsonwebtoken');
const { v4: uuid } = require('uuid');
const dotenv = require('dotenv');

dotenv.config();

async function generateSignedUrl() {
    try {
        const time = Math.floor(Date.now() / 1000); // Current Unix timestamp
        const expirationTime = time + Math.min(parseInt(process.env.SESSION_LENGTH) || 3600, 2592000);

        // Convert TEAM into an array if it is a single value
        const teamsArray = process.env.TEAM ? [process.env.TEAM] : [];

        const token = jwt.sign({
            sub: process.env.EMAIL,
            iss: process.env.CLIENT_ID,
            jti: uuid(),
            iat: time,
            exp: expirationTime,
            account_type: process.env.ACCOUNT_TYPE,
            teams: teamsArray,
        }, process.env.SECRET, {
            algorithm: 'HS256',
            kid: process.env.CLIENT_ID
        });

        // Decode the JWT to inspect its content and log it
        const decodedToken = jwt.decode(token, { complete: true });
        console.log('Decoded JWT:', decodedToken); // Log the decoded JWT for debugging
        
        const signedEmbedUrl = `${process.env.BASE_URL}?:jwt=${encodeURIComponent(token)}&:embed=true`;
        // Log important configuration details to ensure they are correctly set
        console.log('BASE_URL:', process.env.BASE_URL);
        console.log('CLIENT_ID:', process.env.CLIENT_ID); // Verify the client ID
        console.log('SESSION_LENGTH:', process.env.SESSION_LENGTH);
        console.log('TEAMS:', teamsArray);
        console.log('ACCOUNT_TYPE:', process.env.ACCOUNT_TYPE);
        console.log('Signed Embed URL:', signedEmbedUrl);

        return signedEmbedUrl;
    } catch (error) {
        console.error("Failed to generate JWT:", error);
        throw new Error("JWT generation failed");
    }
}

module.exports = { generateSignedUrl };  
```

The resulting `signedUrl` follows this structure:

`https://app.sigmacomputing.com/{organization-slug}/workbook/{workbook_id}?:jwt={JWT VALUE}&:embed=true`

For a detailed discussion and demonstration of using JWT when embedding Sigma, see [Embedding 03: Using JWT Claims and Embed Parameters](https://quickstarts.sigmacomputing.com/guide/embedding_03_using_jwt_claims_and_embed_parameters_v3/index.html) in the Sigma QuickStarts.

Updated 3 days ago

---

[Manage access to a secure embed](/docs/manage-access-to-a-secure-embed)[JSON web token claims reference](/docs/json-web-token-claims-reference)

* [Table of Contents](#)
* + [Configure your URL](#configure-your-url)
  + - [What URL to use](#what-url-to-use)
    - [Add your JWT claims](#add-your-jwt-claims)
    - [Sign your JWT with client credentials and secret](#sign-your-jwt-with-client-credentials-and-secret)
    - [Apply URL control values and string parameters](#apply-url-control-values-and-string-parameters)
  + [Example script to generate a JWT-signed secure URL](#example-script-to-generate-a-jwt-signed-secure-url)
  + [Example server-side API with JWT](#example-server-side-api-with-jwt)