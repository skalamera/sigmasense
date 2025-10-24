# Embed Ask Sigma

# Embed Ask Sigma

You can embed the Ask Sigma interface, which offers your users the ability to ask natural language queries of your data, into your own application or website. For more about Ask Sigma, see [Ask natural language queries with Ask Sigma](/docs/ask-natural-language-queries-with-ask-sigma).

## Requirements

* Complete all steps in [Create an embed API with JSON Web Tokens](/docs/create-an-embed-api-with-json-web-tokens) to prepare a JWT-signed secure URL.
* Set the account type for your embed users to an account type that includes the **Use Ask Sigma** permission.
* Ensure that your embed user teams have permission to access the data sources that you intend for them to be using when they ask questions using Ask Sigma.

## Customize the display of Ask Sigma in your application

The embed URL signed with a JWT token will have this structure: `https://app.sigmacomputing.com/{org-slug}/ask?:jwt=<jwt>`.

To customize the appearance of Ask Sigma, you can add two optional URL parameters:

| URL parameter | Effect |
| --- | --- |
| `&:embed=true` | When set to true, this parameter removes Sigma branding from the Ask Sigma interface. When you apply this setting, the Sigma logo is removed and the step and answer text do not make any references to Sigma. |
| `&:theme={theme-name}` | Theme applies a default [workbook theme](/docs/create-and-manage-workbook-themes) (Light, Dark, or Surface) or any custom theme defined for your organization. The value must be the name of the theme and is case-sensitive. |

Using both of these parameters, you can seamlessly integrate the Ask Sigma experience into your own application or website. For example, you can apply a custom theme so that Ask Sigma adopts the colors of your portal, and set `embed=true` to remove Sigma branding from the experience.

![](https://files.readme.io/b100a78ba266950e7b67d86f994feaa46d1613486a73ab420a5d8a5c0119953b-ask-sigma-embed-themed.png)

Updated 3 days ago

---

[Restrict access to data in embedded content](/docs/restrict-access-to-data-in-embedded-content)[Additional embedding configurations](/docs/additional-embedding-configurations)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Customize the display of Ask Sigma in your application](#customize-the-display-of-ask-sigma-in-your-application)