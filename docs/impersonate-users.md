# Impersonate users

# Impersonate users

This document describes how users assigned the Admin account type can assume the permissions and access of another user in their organization to assist with troubleshooting, data security, and better manage documents.

## Requirements

> 🚩
>
> If you use OAuth to authenticate to your organization, you cannot impersonate users in the UI.

To impersonate another user, you must be assigned the **Admin** [account type](/docs/create-and-manage-account-types). Users who are only *team* admins cannot impersonate other users.

## Overview

Impersonating users allows admins to act as a user and view, edit, and access Sigma resources based on the [user's account type](/docs/user-account-types).

An admin can impersonate a user in the UI or when using the API:

* [Impersonate a user in the UI](#impersonate-a-user), for example, to identify and troubleshoot issues that a user experiences from their perspective, or validate row-level security (RLS) and column-level security (CLS).
* [Impersonate a user in the API](#impersonate-users-for-api-calls), for example, to verify which documents a user can access and the corresponding access levels, retrieve a list of files in a user's My Documents folder, or make changes on behalf of a user in embedded content.

When you impersonate a user, an event is created in [audit logs](/docs/access-and-explore-audit-logs) that identifies the user and the impersonating user.

## Impersonate a user

Follow the steps below to impersonate a user in your organization. You can impersonate a user on the **Users** or **Team** tabs.

> 📘
>
> ### Users assigned the Admin account type can only impersonate non-admin users. Admins cannot impersonate other admins.
>
> For Snowflake and PostgreSQL connections, the impersonation also applies to the role and warehouse attribute used on your connection.

### Impersonate a user from the Users tab

1. Go to **Administration** > **Users**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Users**.
2. Select a user to impersonate.
3. On the user profile, click **Impersonate user**.

   ![Image of the user's profile, with the option to impersonate user highlighted.](https://files.readme.io/7971f57-1.png)
4. At top of the Sigma UI, you see a yellow banner that identifies the user that you are impersonating. During the impersonation session, you can view, edit, and access Sigma resources based on the [user's account type](/docs/user-account-types).

   ![Image of the yellow banner, indicating that you are logged in as Test User 2 (tom@computing.com) and a button with the option to Stop Impersonation.](https://files.readme.io/7c7c2b2-2.png)
5. To end the session, in the yellow banner, click **Stop Impersonation**. You return to the user's profile logged in as yourself.

### Impersonate a user from the Team tab

1. Go to **Administration** > **Teams**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Teams**.
2. Select the team with the user that you want to impersonate.
3. Locate the user that you want to impersonate, then click the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) (**More**) menu and select **Impersonate user**.
4. ![List of team members on the team tab, with a kebab menu open and the option to impersonate user highlighted.](https://files.readme.io/ef9d3a9-3.png)
5. At top of the UI, you see a yellow banner that confirms the identity of the user you are impersonating. During the impersonation session, you can view, edit, and access Sigma resources based on the [user's account type](/docs/user-account-types).

## Impersonate users for API calls

> 🚩
>
> This documentation describes one or more public beta features that are in development. Beta features are subject to quick, iterative changes; therefore the current user experience in the Sigma service can differ from the information provided in this page.
>
> This page should not be considered official published documentation until Sigma removes this notice and the beta flag on the corresponding feature(s) in the Sigma service. For the full beta feature disclaimer, see [Beta features](/docs/sigma-product-releases#beta-features).

For most API endpoints, you can impersonate other users and retrieve information or perform actions on behalf of other users. As with all impersonation, you must be assigned the Admin account type.

To impersonate users for API calls, do the following:

1. [Generate client credentials](/reference/generate-client-credentials), if you do not already have them, to use for the Sigma REST API.
2. [Get an access token](/reference/posttoken) with your client credentials to use in a future API call.
3. Generate a self-signed JWT token for each user that you want to impersonate:

   * Provide the `sub` claim to specify the email address of the user that you want to impersonate.
   * If the user is in a tenant organization, provide the `tenant` claim with the organization ID of the tenant organization.
4. [Get an impersonation token](/reference/posttoken):

   * Provide the access token to authenticate the request and as the `actor_token`.
   * Provide the self-signed JWT token as the `subject_token`.
5. Use the impersonation token included in the response as the bearer token to authenticate API requests that you perform as the impersonated user.

For an example script that performs all of these steps, refer to the [Example Python script for impersonated API calls](#example-python-script-for-impersonated-api-calls).

### Limitations

The following API endpoints do not support an impersonation token. Requests made with an impersonation token to any of the following endpoints fail to return results:

* [Get connection path for a table](/reference/getinodeconnectionpath) (`GET /v2/connections/paths/{inodeId}`)
* [Look up connections by path](/reference/lookupconnection) (`GET /v2/connection/{connectionId}/lookup`)
* [Export data from a workbook](/reference/exportworkbook) (`POST /v2/workbooks/{workbookId}/export`)
* [Export a workbook](/reference/sendworkbook) (`POST /v2/workbooks/{workbookId}/send`)
* [Add workbook schedule](/reference/postworkbookschedule) (`POST /v2/workbooks/{workbookId}/schedules`)

### Example Python script for impersonated API calls

The following example Python script does the following:

* Gets an access token and prints it to the console.
* Generates a self-signed JWT token using the [jwt](https://pypi.org/project/jwt/) library
* Generate an impersonation token using the access token and the self-signed JWT token.
* Get current user details with both the access token and the impersonation token.
* Get the list of datasets accessible to the admin and impersonated user using the [List files](/reference/fileslist) (`GET /v2/listfiles`) endpoint.

> 🚧
>
> ### Do not use this script in any client-facing code. This example script prints sensitive details to the console, such as API access tokens, for testing and validation purposes.

Before running the script, update the code to provide the following details as environment variables or with another secure method:

* REST API client ID
* REST API client secret
* [Base URL for API calls](/docs/region-warehouse-and-feature-support#supported-cloud-platforms-and-regions)
* Email address of the user to impersonate

Python

```
import requests
import jwt
import json

requests.packages.urllib3.disable_warnings()

# provide your client ID, client secret,
# and base URL for Sigma REST API calls
# as environment variables
client_id=""
client_secret=""
url = ""

# Get the admin access token to use as the actor token
def get_actor_token():
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    try:
        response = requests.post(f"{url}/v2/auth/token", headers=headers, data=payload, verify=False)
        response.raise_for_status()
        result = response.json()
        print(f"Generated actor token: {result}")
        return result["access_token"]
    
    except requests.exceptions.RequestException as e:
        print(f"Error getting actor token: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response status: {e.response.status_code}")
            print(f"Response body: {e.response.text}")
        raise

# Generate the self-signed JWT token
# Provide the email address of the user to impersonate
def generate_subject_token():
    jwt_payload = {
        "sub": "<email address of user to impersonate>",
        # tenant claim is optional and relevant only to impersonate users in Sigma tenant organizations
        # "tenant": "<organization ID of a tenant organization>",
    }

    jwt_header = {
        "alg": "HS256",
        "kid": client_id,
        "typ": "JWT"
    }

    try:
        jwt_token = jwt.encode(
            jwt_payload,
            client_secret,
            algorithm="HS256",
            headers=jwt_header
        )
        print(f"Generated subject token: {jwt_token[:50]}...")
        return jwt_token
    except Exception as e:
        print(f"Error generating subject token: {e}")
        raise

def exchange_token(subject_token, actor_token):

    # Get impersonation token
    try:
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "User-Agent": "Python-OAuth-Client/1.0",
            "Authorization": f"Bearer {actor_token}"
        }

        payload = {
            "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
            "subject_token": subject_token,
            "subject_token_type": "urn:ietf:params:oauth:token-type:jwt",
            "actor_token": actor_token,
            "actor_token_type": "urn:ietf:params:oauth:token-type:access_token",
        }

        print(f"Token exchange payload: {json.dumps({k: v[:50] + '...' if len(str(v)) > 50 else v for k, v in payload.items()}, indent=2)}")

        response = requests.post(
            f"{url}/v2/auth/token",
            headers=headers,
            data=payload,
            verify=False,
            timeout=30
        )

        print(f"Token exchange response status: {response.status_code}")
        print(f"Token exchange response headers: {dict(response.headers)}")
        print(f"Token exchange response body: {response.text}")

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error during token exchange: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response status: {e.response.status_code}")
            print(f"Response body: {e.response.text}")
        raise
    except Exception as e:
        print(f"Unexpected error during token exchange: {e}")
        raise

# Retrieve the ID of the impersonated user
def get_current_user(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(
            f"{url}/v2/whoami",
            headers=headers,
            verify=False,
            timeout=30
        )

        print(f"Whoami response status: {response.status_code}")

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error retrieving current user: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response status: {e.response.status_code}")
            print(f"Response body: {e.response.text}")
        raise
    except Exception as e:
        print(f"Unexpected error retrieving current user: {e}")
        raise

# List dataset files accessible by current user
def list_files_for_user(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(
            f"{url}/v2/files?typeFilters=dataset",
            headers=headers,
            verify=False,
            timeout=30
        )

        print(f"List dataset files response status: {response.status_code}")

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error listing dataset files for the current user: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response status: {e.response.status_code}")
            print(f"Response body: {e.response.text}")
        raise
    except Exception as e:
        print(f"Unexpected error listing dataset files for the current user: {e}")
        raise

# Run all defined functions as a test
def main():
    print("=== OAuth Token Exchange Test ===")

    try:
        print("\n1. Generating subject token...")
        subject_token = generate_subject_token()
        print(f"Subject token: {subject_token[:100]}...")

        print("\n2. Getting actor token...")
        actor_token = get_actor_token()
        print(f"Actor token: {actor_token[:100]}...")

        print("\n3. Exchanging tokens to impersonate user...")
        result = exchange_token(subject_token, actor_token)
        print(f"Token impersonation result: {json.dumps(result, indent=2)}")

        print("\n4. Get current user with actor token...")
        whoami_a = get_current_user(actor_token)
        print(f"Current user: {whoami_a}")

        print("\n5. Get current user with impersonation token...")
        whoami_b = get_current_user(result["access_token"])
        print(f"Current user: {whoami_b}")

        print("\n6. Listing dataset files for user with actor token...")
        datasets = list_files_for_user(actor_token)
        print(f"Datasets accessible by current user: {datasets}")

        print("\n7. Listing dataset files for user with impersonation token...")
        datasets = list_files_for_user(result["access_token"])
        print(f"Datasets accessible by current user: {datasets}")

    except Exception as e:
        print(f"Script failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
```

Updated about 6 hours ago

---

Related resources

* [Manage Teams](/docs/manage-teams)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Overview](#overview)
  + [Impersonate a user](#impersonate-a-user)
  + - [Impersonate a user from the Users tab](#impersonate-a-user-from-the-users-tab)
    - [Impersonate a user from the Team tab](#impersonate-a-user-from-the-team-tab)
  + [Impersonate users for API calls](#impersonate-users-for-api-calls)
  + - [Limitations](#limitations)
    - [Example Python script for impersonated API calls](#example-python-script-for-impersonated-api-calls)