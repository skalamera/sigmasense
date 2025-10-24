# ArrayContains

# ArrayContains

The **ArrayContains** function searches for a specific value in a list or array. If the value is found, the function returns `True`, otherwise it returns `False`.

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

```
ArrayContains(list, target)
```

Function arguments:

|  |  |
| --- | --- |
| **list** | A column containing lists or arrays to reference when searching for a value. |
| **target** | A text string or column containing the value to find. |

> 🚧
>
> ### The list argument must reference a list parameter or a column containing list values. When the target argument references a column, the column must contain text values. Other [data value types](/docs/data-types-and-formats) result in an invalid formula.

## Example

A table contains an *Array* column that returns list values from the *Product Type PRM* list parameter. You can use the **ArrayContains** function to search the *Array* column list for the value in the *Product Type* column.

```
ArrayContains([Array], [Product Type])
```

You can also use the function to determine whether or not the value in the *Product Type* column is currently selected in the *Product-Type-PRM* list parameter.

```
ArrayContains([Product-Type-PRM], [Product Type])
```

When the value in the *Product Type* column is found in the *Array* column or *Product Type PRM* list parameter, the function output is `True`. If the value is not found, the function output is `False`.

![](https://support.sigmacomputing.com/hc/article_attachments/14391625445395)

Updated 3 days ago

---

Related resources

* [Contains](/docs/contains)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)