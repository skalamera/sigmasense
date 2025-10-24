# Restrict access to data in embedded content

# Restrict access to data in embedded content

Sigma offers a number of options to secure and manage access to the data used by your embedded content.

* [Use the role-based access control (RBAC) defined in your connected data platform](#use-role-based-access-control-in-your-data-platform) using OAuth or user attributes.
* Restrict columns from specific users or teams using [column-level security (CLS) in Sigma](#apply-column-level-security-to-embedded-content).
* Restrict specific rows of data from specific users or teams using [row-level security (RLS) in Sigma](#apply-row-level-security-to-your-secure-embed).

None of these methods are specific to embedded content, but can be used in a secure embed to restrict access to data.

> 💡
>
> You can use multiple options together to restrict access to data.

The method you use to assign values to restrict data access depends on how you [manage access to your embed](/docs/manage-access-to-a-secure-embed):

* If you rely on the automatic creation of embed users, you can either use JWT claims to set the user attribute values and teams for embed users, or pre-assign user attribute values to teams of embed users.
* You must assign user attribute values to existing Sigma users.
* If you manually manage users that can access your embed, assign user attribute values to teams in Sigma.

> 🚧
>
> ### JWT claims are specific to a user, not a session. Do not use user-specific claims (such as teams, account type, or user attribute values) to manage what a user in a given *session* can view in an embed. Instead, manage access on the user level. Each user must have their own account to access the embed with the correct access level and permissions. Use consistent claim values for the same embed user across different secure embeds.

## Use role-based access control in your data platform

You can use the role-based access control (RBAC) defined in your data platform to manage access to the data in your securely embedded content. Enforce RBAC in your embed using one of two methods:

* OAuth
* Dynamically assign roles with user attributes

> 📘
>
> ### You can also swap the data source that you use for your embedded content from one connection to another. You can use [version tags to swap the connection used](/docs/add-version-tags-to-workbooks-and-data-models#swap-the-source-of-a-tagged-workbook-version) (recommended), or follow the steps in [Embedding 14: Connection Swapping](https://quickstarts.sigmacomputing.com/guide/embedding_14_connection_swapping_v3/index.html) to use a JWT claim to swap the connection.

### Use OAuth for your secure embed

You can pass an OAuth token in your secure embed URL to authenticate users of the embed:

* If you use [OAuth for authentication to Sigma and authentication to your data platform](/docs/configure-oauth), use the `oauth_token` claim. Obtain the OAuth access token from your identity provider.
* If you use [OAuth only to authenticate to your data platform from Sigma](/docs/configure-oauth), use the `connection_oauth_tokens`. For the `connection_oauth_tokens` claim, keys are the desired connection IDs and values are encrypted OAuth tokens that the embed user uses to access data for that connection.
  + To retrieve the relevant connection IDs, use the [GET /v2/connections](/reference/listconnections) API endpoint.
  + Obtain the OAuth access token from your identity provider.

> 🚩
>
> The `oauth_token` or `connection_oauth_tokens` claims must be encrypted. See [JSON web token claims reference](/docs/json-web-token-claims-reference).

### Dynamically assign data platform roles with a user attribute

> 📘
>
> This feature isn't supported by all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

If you use key pair authentication and a supported connection, you can use user attributes to specify the role to be used by the user accessing the secure embed. See [Dynamically assign roles used by a connection](/docs/configure-user-attributes-on-a-snowflake-connection).

> 📘
>
> ### You cannot use this functionality with Snowflake if you use OAuth to connect.

For example, you might use this approach if each customer's data is stored in a separate schema in the same database, and you use row access or security policies in your data platform to ensure that each customer can access only their data.

To dynamically assign data platform roles based on a user attribute value, do the following:

1. Follow the steps to [configure a user attribute](/docs/user-attributes). Create a `Role` user attribute with values equivalent to each role in your data platform.
2. Follow the steps to [Dynamically assign roles used by a connection](/docs/configure-user-attributes-on-a-snowflake-connection). Select the user attribute that you configured in step 1.
3. Depending on how you [manage access to your embed](/docs/manage-access-to-a-secure-embed), assign user attributes to users or teams:

   * If you rely on the automatic creation of embed users, add the `user_attributes` JWT claim to your server-side embed API code and reference the `Role` user attribute, or assign the `Role` user attribute to the team that you use to manage embed users.

     > 📘
     >
     > ### Any internal users accessing your embed must be assigned user attribute values.
   * If you manually manage users that can access your embed, assign the relevant user attribute values to the relevant teams containing users provisioned in Sigma.

   To assign user attributes using the Sigma UI, see [Assign user attributes](/docs/user-attributes#assign-user-attributes). To assign attributes programmatically, use the [Set a user attribute for teams](/reference/setuserattributeforteams) API endpoint.

#### Example

In this example, assume that your customer data is stored in one database `CUSTOMER_DATA` in one Snowflake account, with one schema for each customer's data, such as `CUSTOMER_DATA.ABC`:

1. Create an associated Snowflake role granted the USAGE privilege on the database and the relevant schema contained within:

   SQL

   ```
   GRANT USAGE ON CUSTOMER_DATA.ABC TO ROLE ABC
   ```
2. In Sigma, create a user attribute called `Role`. Do not set a default value.
3. Create a connection to the Snowflake account using key pair authentication.
4. In the **Role** field for the Snowflake connection, select the `Role` user attribute.
5. Assign the user attribute values:

   * For each team of internal users, assign the team a user attribute value equivalent to the role with privileges to access the relevant Snowflake data. For example, `ABC`.
   * If you rely on the automatic creation of embed users, add a JWT claim for `user_attributes` to your server-side embed API code. Assign the relevant value at runtime based on a variable passed from the host application:

   JavaScript

   ```
   # .env file

   UA_ROLE = $role_var_from_host_app$
   SIGMA_WH_EMBED = $wh_var_from_host_app$
   ```

   Then set the `user_attributes` claim to the value of the environment variable set by the host application at runtime:

   JavaScript

   ```
   {
      "user_attributes": {
         "SnowflakeRole": UA_ROLE
         "Warehouse": SIGMA_WH_EMBED
      }
   }
   ```

## Apply row-level security to your secure embed

Row-level security (RLS) is a method for restricting data access. You can implement RLS in Sigma based on user identity, team membership, or assigned user attribute values. Set up RLS in a data model, dataset, or in custom SQL. See [Set up row-level security](/docs/set-up-row-level-security).

After setting up RLS in your data source using assigned user attributes, teams, or users, enforce it in your embedded content:

* If you rely on the automatic creation of embed users, use the relevant JWT claim: `user_attributes`, `teams`, or `users`. See [JSON web token claims reference](/docs/json-web-token-claims-reference).

  > 📘
  >
  > ### Any internal users accessing your embed must be assigned user attribute values or team membership directly. See [Assign user attributes](/docs/user-attributes#assign-user-attributes) and [Manage team membership](/docs/manage-team-members).
* If you manually manage users that can access your embed, assign user attributes to teams or users in Sigma, see [Assign user attributes](/docs/user-attributes#assign-user-attributes) to use the UI, or use the [Set a user attribute for teams](/reference/setuserattributeforteams) API endpoint.

## Apply column-level security to embedded content

Column-level security (CLS) enables you to restrict or grant access to column-level data. To apply CLS in a secure embed, you must use a data source with CLS configured. See [Configure column-level security](/docs/column-level-security).

To enforce the CLS rules for your embed:

* If you rely on the automatic creation of embed users, use one of the `user_attributes`, `teams`, or `users` JWT claims. See [JSON web token claims reference](/docs/json-web-token-claims-reference).

  > 📘
  >
  > ### Any internal users accessing your embed must be assigned user attribute values or team membership directly. See [Assign user attributes](/docs/user-attributes#assign-user-attributes) and [Manage team membership](/docs/manage-team-members).
* If you manually manage users that can access your embed and your CLS rules rely on user attributes, see [Assign user attributes](/docs/user-attributes#assign-user-attributes) to use the UI, or use the [Set a user attribute for teams](/reference/setuserattributeforteams) API endpoint.
* If you manually manage users that can access your embed and your CLS rules rely on teams, see [Manage team members](/docs/manage-team-members) to use the UI, or use the [Update team members](/reference/updateteammembers) API endpoint.

## Advanced examples for assigning values in JWT claims

If you combine multiple approaches for restricting access to the data in embedded content, refer to these examples for how the output of your embed API might look.

> 💡
>
> In a production use case, configure the host application to set these values dynamically at runtime using environment variables.

### Apply CLS and RLS with user attributes

Assign each relevant user attribute a value in the `user_attributes` claim:

JavaScript

```
{
  "user_attributes": {
     "CustomerName": "2",
     "Region": "West"
  }
}
```

### Apply CLS with teams and RLS with user attributes

Specify one value for the `user_attributes` claim to enforce RLS, then specify a team to use to enforce existing CLS rules on a data model:

JavaScript

```
{
  "user_attributes": {
     "Region": "West"
  }
  "teams": ["Customer ABC"]
}
```

### Dynamically switch the connection and role

If you use dynamic warehouse and role switching:

JavaScript

```
{
    "eval_connection_id": {
        "1a2b3456-c7d8-91ef-23g4-h56i7jkl8912"
    },
    "user_attributes": {
        "Warehouse": "SIGMA_EMBED_WH",
        "Role": "PUBLIC"
    }
}
```

Updated 3 days ago

---

[Common embed error codes and messages](/docs/common-embed-error-codes-and-messages)[Embed Ask Sigma](/docs/embed-ask-sigma)

* [Table of Contents](#)
* + [Use role-based access control in your data platform](#use-role-based-access-control-in-your-data-platform)
  + - [Use OAuth for your secure embed](#use-oauth-for-your-secure-embed)
    - [Dynamically assign data platform roles with a user attribute](#dynamically-assign-data-platform-roles-with-a-user-attribute)
  + [Apply row-level security to your secure embed](#apply-row-level-security-to-your-secure-embed)
  + [Apply column-level security to embedded content](#apply-column-level-security-to-embedded-content)
  + [Advanced examples for assigning values in JWT claims](#advanced-examples-for-assigning-values-in-jwt-claims)
  + - [Apply CLS and RLS with user attributes](#apply-cls-and-rls-with-user-attributes)
    - [Apply CLS with teams and RLS with user attributes](#apply-cls-with-teams-and-rls-with-user-attributes)
    - [Dynamically switch the connection and role](#dynamically-switch-the-connection-and-role)