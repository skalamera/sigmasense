# Proper

# Proper

The **Proper** function converts text to proper case, which capitalizes the first letter of each word and renders all remaining letters in lowercase.

## Syntax

```
Proper(string)
```

Function arguments:

* **string** (required) - a text string or column to reference when converting text to proper case

> 🚧
>
> If the **string** argument references a column, the column must contain text values. Other [data value types](/docs/data-types-and-formats) result in an invalid formula.

## Examples

```
Proper("aPPles AnD oranGEs")
```

Returns *Apples And Oranges*.

```
Proper([Product Family])
```

Returns the proper form of the text value in the *Product Family* column.

![](https://files.readme.io/1847ed3-mceclip0_4.png)

Updated 3 days ago

---

Related resources

* [Text functions overview](/docs/text-functions-overview)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Examples](#examples)