# CurrentUserEmail

# CurrentUserEmail

The **CurrentUserEmail** function returns the email address associated with the current (signed-in) user's account.

To return the user's first or full name, use the [CurrentUserFirstName](/docs/currentuserfirstname) or [CurrentUserFullName](/docs/currentuserfullname) function.

## Usage

```
CurrentUserEmail()
```

> 📘
>
> ### **CurrentUserEmail** has no function arguments because it’s context-sensitive and doesn’t depend on any explicitly provided values.

## Example

A dataset contains information about sales opportunities, including a *Rep Email* column that identifies the email address of the corresponding Sales representative. To implement email-based row-level security (RLS), an admin adds a new *RLS* column populated by the following formula:

```
CurrentUserEmail() = [Rep Email]
```

The *RLS* column returns `True` when the current user's email address matches the value in the *Rep Email* column.

To ensure each Sales representative can only view their own opportunities, the admin hides the *RLS* column and filters the dataset to only include rows in which the *RLS* value is `True`.

Updated 3 days ago

---

Related resources

* [CurrentUserFirstName](/docs/currentuserfirstname)
* [CurrentUserFullName](/docs/currentuserfullname)
* [Set up row-level security](/docs/set-up-row-level-security)

* [Table of Contents](#)
* + [Usage](#usage)
  + [Example](#example)