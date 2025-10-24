# CurrentTimezone

# CurrentTimezone

The **CurrentTimezone** function returns the name of the [IANA time zone](https://www.iana.org/time-zones) configured as your organization's [account time zone](/docs/account-time-zone).

> 🚧
>
> ### Workbook elements that use this system function are not supported by [materialization](/docs/materialization).

## Syntax

```
CurrentTimezone()
```

> 📘
>
> ### **CurrentTimezone** has no function arguments because it’s context-sensitive and doesn’t depend on any explicitly provided values.

## Example

```
CurrentTimezone()
```

The organization's account time zone is set to America/Los\_Angeles. **CurrentTimezone** returns the IANA time zone name, `America/Los_Angeles`.

![This image shows example output from the CurrentTimezone function. The left column shows a series of sample dates/times, and the right column shows the respective output from CurrentTimezone.](https://files.readme.io/415d84eb6300c607fb28b47bc3c6686d1c73949044b78a76acaa1ef24ed384ad-function_currenttimezone_example.png)

Updated 3 days ago

---

Related resources

* [Now](/docs/now)
* [ConvertTimezone](/docs/converttimezone)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)