# Generate embed client credentials

# Generate embed client credentials

Client credentials (a unique client ID and embed secret) are crucial to creating secure embeds. You generate the JSON web token (JWT) with the embed secret.

This document explains how to generate the embed client credentials in Sigma.

## System and user requirements

The ability to generate embed client credentials requires the following:

* You must be assigned the **Admin** [account type](/docs/user-account-types).

## About embed credentials

Sigma uses the client ID to determine which embed secret is referenced in a request. Each time a request is made, the server-side embed API uses the embed secret to generate a JWT and Sigma uses that client secret to verify the JWT in the URL.

Together, the client ID and embed secret create a robust security framework for server-side interactions with Sigma.

* **Authentication**: The credentials authenticate your server and verify its identity to Sigma, confirming it as a recognized and authorized entity with valid access rights.
* **Authorization**: Based on the authentication, Sigma can control access to its resources and only allow requests from authorized entities to process further.
* **Data integrity and non-repudiation**: Signing the JWT with the embed secret ensures the JWT remains unaltered, enhancing trust in the security of the embed.
* **Confidentiality**: Use of the credentials in server-side API interactions secures sensitive data and operations by maintaining confidentiality and providing protection against unauthorized access or manipulation.

## Generate embed client credentials

1. Go to **Administration** > **Developer Access**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Developer Access**.
2. Click **Create New** to set up new credentials.
3. In the **Create client credentials** modal, complete the form fields:

   1. In the **Select privileges** section, select the **Embedding** checkbox.
   2. In the **Name** field, enter a unique name to identify the credentials.
   3. [optional] In the **Description** field, enter a description about the purpose of the credentials.
   4. In the **Owner** field, select an organization member. The embed secret uses the account type permissions associated with this user.
   5. Click **Create** to generate the credentials.
4. In the **Access Credentials** modal, copy the embed secret and securely store it for future reference (you cannot retrieve it in Sigma later).  
   You can also copy and securely store the client ID from the modal, but this information can be retrieved from the **Developer Access** page at any time.

> 🚧
>
> ### For security purposes, Sigma provides a one-time view of the embed secret at the time of creation and does not display it again. Because the secret is non-retrievable, it's important that you store the secret securely when you create it.
>
> If you lose the embed secret, or it becomes compromised, you can [revoke it and generate a new one](/docs/generate-embed-client-credentials#revoke-existing-embed-client-credentials); however, this invalidates the previous secret and all embeds that use it. When a new secret is generated, you must modify the embed API and update all existing embeds.

### Security rules for assigning embed credentials ownership

Sigma empowers organization admins to [impersonate other users](/docs/impersonate-users). Similarly, admins can log in and view a secure embed from the perspective of another user or account type.

The owner of the embed client credentials determines whether those credentials can be used for a single user or to log in with an account representing other users.

If the client credentials owner is an admin, the credentials can be used to log in as any user of that Sigma organization. You must be assigned the Admin account type to generate valid JWTs for other users.

## Revoke existing embed client credentials

If you lose the embed secret, or it becomes compromised, you can revoke it and generate a new one.

1. Go to **Administration** > **Developer Access**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Developer Access**.
2. In the list of credentials, locate the one you want to regenerate, then click **More** and select **Revoke**.
3. Complete the steps in [Generate embed client credentials](/docs/generate-embed-client-credentials#generate-embed-client-credentials) to generate new credentials.
4. Update any applications using the embed API containing the revoked credentials.

Updated 3 days ago

---

[Create a secure embed](/docs/create-a-secure-embed)[Manage access to a secure embed](/docs/manage-access-to-a-secure-embed)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [About embed credentials](#about-embed-credentials)
  + [Generate embed client credentials](#generate-embed-client-credentials)
  + - [Security rules for assigning embed credentials ownership](#security-rules-for-assigning-embed-credentials-ownership)
  + [Revoke existing embed client credentials](#revoke-existing-embed-client-credentials)