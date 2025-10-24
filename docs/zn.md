# Zn

# Zn

# Zn

The **Zn** function returns the argument value if it is not Null, otherwise returns zero. Zn allows the convenient use of zero values in place of Null values.

## Syntax

`Zn(argument)`

**argument** (required) The number value to check.

> 📘
>
> ### The **Zn** function can analyze one argument at a time.

## Example

```
Zn(3)
```

* Returns 3

```
Zn(Null)
```

* Returns 0

```
Zn([Quantity])
```

![](https://files.readme.io/4b310ba-jk.png)

* Returns 0 for every row in the column that is Null.

Updated 3 days ago

---

Related resources

* [Coalesce](/docs/coalesce)
* [IsNull](/docs/isnull)
* [IsNotNull](/docs/isnotnull)

* [Table of Contents](#)
* + [Zn](#zn)
  + - [Syntax](#syntax)
    - [Example](#example)