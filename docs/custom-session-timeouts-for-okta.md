# Custom Session Timeouts for Okta

# Custom Session Timeouts for Okta

Organization that use [SAML authorization](/docs/single-sign-on-with-saml) can set up custom session timeouts. By default, a Sigma user session is 30 days. Once a user logs in to Sigma, their session lasts for 30 days, unless they explicitly log out before then.  Security-minded admins may want to force their users to log out and log back in more often than this.

To set up a custom session time out, you must have SAML enabled for your organization and admin access to your SAML provider.

## Setup

To enforce a custom session length for your users, follow these steps:

1. Enable SAML SSO to your Sigma workspace.
2. Verify that you have admin privileges within your SAML provider.
3. In your SAML provider, set the **refreshTokenTimeoutSecs** SAML attribute in your Sigma app.

* The value must be a positive integer.
* The units are in seconds; if you want your users to reauthenticate every 8 hours, set the value to (8 hours) \* (60 minutes/hour) \* (60 seconds/minute) = 28800.

5. Save all changes in your SAML provider.
6. The next time your users log out and log in to Sigma, your custom session timeout is applied.

## Details

Like many SaaS apps, Sigma uses a two-tiered token system for authentication. Users are granted a long-lived refresh token which they can use to get short-lived access tokens. They then use the access tokens for authentication and authorization within Sigma.

The custom session timeout feature allows SAML admins to configure the lifetime of the long-lived refresh token. However, this feature does not affect the lifetime of the short-lived access tokens, which are always valid for one hour.

This means that if you configure your refresh tokens to be valid for 8 hours, users could theoretically stay logged in for up to 9 hours if they happen to get a new access token (lifetime 1 hour) right before their refresh token (lifetime 8 hours) expires.

## Test your configuration

For a complete end-to-end test, you should:

1. Configure a custom session timeout as described above.
2. Log out of Sigma.
3. Log back into Sigma.
4. Wait for your session timeout + one hour.
5. Verify that you've been logged out.

To quickly verify that you configured your SAML settings correctly, view your SAML assertion directly to ensure the correct value is set.

1. Get the SAML assertion from your SAML provider:

   * Most SAML providers allow you to generate an example assertion for any app. Refer to your provider's documentation for specific instructions.
2. Get the SAML assertion from Sigma:

   1. Log out of Sigma.
   2. Open your browser's developer tools and navigate to the network pane.
   3. Log in to Sigma using SSO.
   4. Find the request to the "assert" endpoint in the network pane (this request should be early in the request log) and click on it.
   5. In the network pane, locate the parameters for this request (in Firefox, this is under "Params"; in Chrome it's under "Headers > "Form Data").
   6. Copy the value of the SAMLRequest form parameter.
   7. Decode the value, which is encoded in base64:

      * If you're on a Mac, run `pbpaste | base64 -D > saml.xml` from your terminal.
      * If you're on Linux, paste the value into a plain text file and run `base64 -d $FILE_NAME > saml.xml` from your terminal.
      * If you're on Windows, paste the value into a plain text file and run `certutil -decode $FILE_NAME saml.xml` from your terminal.
   8. Open saml.xml in your preferred editor and, optionally, improve readability:

      * Add newlines after each ">" character (use find and replace).
      * If your editor supports it, auto-indent the file.
   9. Look for the AttributeStatement section of the XML document and ensure that your custom value for refreshTokenTimeoutSecs is present. It should appear similar to this:

XML

```
 <saml2:AttributeStatement xmlns:saml2="urn:oasis:names:tc:SAML:2.0:assertion">

   <saml2:Attribute Name="firstName" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified">

     <saml2:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">

     YOUR FIRST NAME</saml2:AttributeValue>

   </saml2:Attribute>
```

Updated 3 days ago

---

[Use custom account types with your IdP](/docs/use-custom-account-types-with-your-idp)[Configure OAuth](/docs/configure-oauth)

* [Table of Contents](#)
* + [Setup](#setup)
  + [Details](#details)
  + [Test your configuration](#test-your-configuration)