# Set up row-level security

# Set up row-level security

Row-level security (RLS) restricts access to data based on the characteristics of the person viewing the data.

Sigma supports both RLS and [column-level security (CLS)](/docs/column-level-security) to help protect sensitive data. While CLS protects all values in a column from being viewed by users without access, RLS can be used to protect specific rows of data based on the values.

You can set up RLS for a table in a data model or a dataset.

> 💡
>
> ### If your organization uses OAuth for a connection, any existing RLS rules in your data platform are respected by Sigma.

In Sigma, you can set up RLS based on the following:

* [User attribute value](#configure-row-level-security-with-user-attributes) (recommended)
* [Team membership](#configure-row-level-security-by-team) in Sigma
* [User email address](#configure-row-level-security-by-user)

When you configure RLS, you perform two steps:

1. Define a column with the RLS rule.
2. Filter the data to match.

> 🚧
>
> ### This approach relies on a filter which can be modified by anyone viewing the table to which the filter applies. As a result, only child elements and downstream data sources can be considered fully protected. If you configure RLS in a dataset or data model, all workbooks that rely on the data are protected.

## Requirements

* You must have **Can Edit** or **Can Explore** [access](/docs/folder-and-document-permissions) to the document where you want to set up RLS.

## Configure row-level security with user attributes

Setting up RLS with user attributes is recommended because assignment of user attributes to users and teams is handled separately from the column formulas that control RLS, so are easier to update. User attributes can also be used for RLS in embedding use cases or custom SQL queries.

Before configuring RLS with user attributes, create a user attribute and assign it to the relevant users in Sigma. See [Configure user attributes](/docs/user-attributes).

1. In the data model table, workbook data element, or dataset that you want to protect, add a new column.
2. Set the formula of the new column to the following formula, replacing `<attribute-name>` with the user attribute to use for RLS, and `[<column-name>]` with the column name that contains the matching values:

   ```
   CurrentUserAttributeText("<attribute-name>") = [<column-name>]
   ```

   > 🚩
   >
   > ### The attribute value must be the same data type as the column name. For example, text.

   The formula evaluate to `True` when the attribute value matches the row value, and `False` when it does not.
3. Add a filter on the new column to show only `True` values.
4. Hide the column so that downstream users do not see it by default.

For more details, see [CurrentUserAttributeText](/docs/currentuserattributetext).

### RLS in a data model

If you want to set up RLS on the `plugs_electronics` table of sales data by store region in a data model:

1. Create a user attribute called `Region` and assign the different available region values to different sales teams.

   * Sales US-West is assigned the value West
   * Sales US-East is assigned the value East
2. In a data model, add the `plugs_electronics` table, then add a new column called *Region RLS*.
3. Set the formula of the *Region RLS* column to the following:

   ```
   CurrentUserAttributeText("Region") = [Store Region]
   ```

   The *Region RLS* column shows `True` values for rows where the *Store Region* is `West` because you are a member of the Sales US-West team.

   ![Plugs Electronics Hands on Lab data in a data model table with a column titled Region RLS highlighted and a formula that matches the surrounding text. For rows with the Store Region column value of West, the Region RLS column is True, and for other rows the Region RLS column is False.](https://files.readme.io/226323e2b44bb82c5ceb714d467e6f4936828e7cf44fc1a445ae103b2f9cc970-rls-formula.png)
4. Add a filter on the *Region RLS* column and show only `True` values.

   ![Filters and controls option open on the data model table, with a list values filter on the Region RLS column enabled and the value True selected.](https://files.readme.io/0d66893348deae35468f8ed4aded7c90770b7e0ed01a5b613032983605e171a6-rls-filter.png)
5. [optional] Hide the *Region RLS* column so that downstream users do not see it by default.

### RLS with embedded analytics

If you embed Sigma, you can enforce RLS with a parameter in the embed URL or a JWT claim:

* [Embed URL parameters](/docs/embed-url-parameters)
* [Create an embed API with JSON Web Tokens](/docs/create-an-embed-api-with-json-web-tokens)

### RLS with custom SQL

After you successfully configure user attributes, you can filter the results of a SQL query based on the user attribute of the user running the SQL.

For example:

SQL

```
SELECT
  *
FROM
  EXAMPLES.PLUGS_ELECTRONICS.PLUGS_ELECTRONICS_HANDS_ON_LAB_DATA
WHERE 
  {{system::CurrentUserAttributeText::store_region}} = STORE_REGION
```

This query uses the [CurrentUserAttributeText](/docs/currentuserattributetext) function to retrieve the assigned value of the user attribute for the user running the query. The function requires a parameter that references the user attribute name.

> 📘
>
> ### If the user attribute name has spaces, use double quotes. For example:
>
> `{{system::CurrentUserAttributeText::"Store Region"}} = STORE_REGION`

For more details, see [Write custom SQL](/docs/write-custom-sql).

## Configure row-level security by team

You can configure RLS by team membership using the [CurrentUserInTeam](/docs/currentuserinteam) function:

1. In the data model table, workbook data element, or dataset that you want to protect, add two new columns.
2. Set the formula of one new column to a formula that associates a value in the data with a Sigma team name, using the [Switch](/docs/switch) or the [If](/docs/if) function.
3. Set the formula of the other new column to the following formula to set up the RLS rule:

   ```
   CurrentUserInTeam([Team Assignment])
   ```

   The formula evaluates to `True` when the current user is a member of one or more of the teams specified in the *Team Assignment* column.
4. Add a filter on the new column to show only `True` values.
5. Hide the columns so that downstream users do not see it by default.

For more details, see the [RLS by team example](#rls-by-team-example).

### RLS by team example

To set up RLS by team, create a column in your data that associates the data with the relevant Sigma team called *Team Region*. For example, given a *Store Region* column in your data and two Sigma teams, Sales US-West and Sales US-East, write a formula using the [Switch](/docs/switch) function:

```
Switch([Store Region], "West", "Sales US-West", "East", "Sales US-East")
```

You can expand this logic to include all of the teams you want to test for, then create a *Team RLS* column with the RLS rule to evaluate whether the current user belongs to the team indicated in the corresponding row of the *Team Region* column:

```
CurrentUserInTeam([Team Region])
```

You can then add a filter on the *Team RLS* column to show only `True` values and hide the *Team RLS* and *Team Region* columns.

## Configure row-level security by user

You can set up RLS by user with the [CurrentUserEmail](/docs/currentuseremail) function:

1. In the data model table, workbook data element, or dataset that you want to protect, add a new column.
2. Set the formula of the new column to the following formula, with one or more users to use for RLS:

   ```
   [<column-name>] = CurrentUserEmail()
   ```

   The formula evaluates to `True` when the current user is a member of one or more of the specified teams.
3. Add a filter on the new column to show only `True` values.
4. Hide the column so that downstream users do not see it by default.

### RLS by user example

If you have a table with sales results and you want each salesperson to see only their results, set up row-level security by user. To use this approach, you must create or identify a column in your data that contains email addresses of Sigma users. If you need to create a column, refer to the [RLS by team example](#rls-by-team-example) for sample syntax mapping data values.

For this example, assume that your data contains a column, *Salesperson Email*, that matches email addresses used by Sigma users.Add a new column called *Salesperson RLS* with the following formula to evaluate the RLS rule:

```
[Salesperson Email] = CurrentUserEmail()
```

This formula evaluates the emails in the column `[Salesperson Email]` and checks whether they match the email of the user currently viewing the data. The formula returns `True` for all rows where the current user’s email matches the salesperson email.

You can then add a filter on the *Salesperson RLS* column to show only `True` values and hide the *Salesperson RLS* column.

### RLS by team and user example

You can also set up filters to test for multiple conditions. For example, add a column to filter your data to show salespeople data only from leads that they own, but show all the data to sales managers:

```
( [Salesperson Email] = CurrentUserEmail() ) or ( CurrentUserInTeam(“Sales Manager”) )
```

This formula returns `True` for all rows when the viewer is in the "Sales Manager" team and for all other viewers returns `True` only for rows where the viewer email matches the Salesperson Email.

Updated 3 days ago

---

Related resources

* [Configure user attributes](/docs/user-attributes)
* [CurrentUserAttributeText](/docs/currentuserattributetext)
* [CurrentUserEmail](/docs/currentuseremail)
* [CurrentUserInTeam](/docs/currentuserinteam)
* [Configure column-level security](/docs/column-level-security)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Configure row-level security with user attributes](#configure-row-level-security-with-user-attributes)
  + - [RLS in a data model](#rls-in-a-data-model)
    - [RLS with embedded analytics](#rls-with-embedded-analytics)
    - [RLS with custom SQL](#rls-with-custom-sql)
  + [Configure row-level security by team](#configure-row-level-security-by-team)
  + - [RLS by team example](#rls-by-team-example)
  + [Configure row-level security by user](#configure-row-level-security-by-user)
  + - [RLS by user example](#rls-by-user-example)
    - [RLS by team and user example](#rls-by-team-and-user-example)