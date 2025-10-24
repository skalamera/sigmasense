# CurrentUserFullName

# CurrentUserFullName

The **CurrentUserFullName** function returns the current (signed-in) user’s first and last name as configured in the user’s profile.

To return the user's first name or email address, use the **[CurrentUserFirstName](/docs/currentuserfirstname)** or **[CurrentUserEmail](/docs/currentuseremail)** function.

## Syntax

```
CurrentUserFullName()
```

> 📘
>
> ### **CurrentUserFullName** has no function arguments because it’s context-sensitive and doesn’t depend on any explicitly provided values.

## Example

An admin applies a workbook as the custom homepage for their team. The workbook contains a text element with the message “Welcome” followed by a dynamic value that references the **CurrentUserFullName** function.

When John Wooden logs into Sigma, the custom homepage displays a “Welcome John Wooden” message.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Functions/currentuserfullname_example1.png)

Likewise, when Bill Walton logs in, the custom homepage displays a “Welcome Bill Walton” message.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Functions/currentuserfullname_example2.png)

Updated 3 days ago

---

Related resources

* [CurrentUserFirstName](/docs/currentuserfirstname)
* [CurrentUserEmail](/docs/currentuseremail)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)