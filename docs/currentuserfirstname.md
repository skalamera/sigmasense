# CurrentUserFirstName

# CurrentUserFirstName

The **CurrentUserFirstName** function returns the current (signed-in) user’s first name as configured in the user’s profile.

To return the user's full name or email address, use the **[CurrentUserFullName](/docs/currentuserfullname)** or **[CurrentUserEmail](/docs/currentuseremail)** function.

## Syntax

```
CurrentUserFirstName()
```

> 📘
>
> ### **CurrentUserFirstName** has no function arguments because it’s context-sensitive and doesn’t depend on any explicitly provided values.

## Example

The VP of Sales creates a *Sales Performance* workbook and implements row-level-security so each Sales representative can only view their own performance data. For added personalization, the VP adds a text element that contains the message “Hey there,” and a dynamic value that references the **CurrentUserFirstName** function followed by an exclamation point.

When Jim Halpert logs into Sigma and views the *Sales Performance* workbook, the text element displays “Hey there, Jim!”

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Functions/currentuserfirstname_example1.png)

Likewise, when Stanley Hudson logs in and views the same workbook, the text element displays a “Hey there, Stanley!"

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Functions/currentuserfirstname_example2.png)

Updated 3 days ago

---

Related resources

* [CurrentUserFullName](/docs/currentuserfullname)
* [CurrentUserEmail](/docs/currentuseremail)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)