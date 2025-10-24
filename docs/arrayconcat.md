# ArrayConcat

# ArrayConcat

The **ArrayConcat** function combines multiple arrays into one array.

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

```
ArrayConcat(array...)
```

Function arguments:

|  |  |
| --- | --- |
| **array** | One or more arrays to concatenate.  Arrays can include a variety of data types and lengths, and are combined in sequential order. |

## Notes

* Arrays in Sigma support a zero-based indexing system. To retrieve a value in the array based on its position, append the index in square brackets directly following the function call. For an example, see [Array](#doc:array#example-3).
* Arrays in Sigma can contain `null` values. Concatenating an array containing a `null` value with another array does not return an error. For an example, see [Example 2](#example-2).
* If any argument is `null`, the function returns `null`. For an example, see [Example 3](#example-3).

## Examples

### Example 1

```
ArrayConcat(Array(1, 2, 3), Array(4, 5, 6))
```

Returns the array `[1,2,3,4,5,6]` as [variant data](/docs/data-types-and-formats#variant).

### Example 2

```
ArrayConcat(Array(1, null, 3), Array("a", "b", "c"))
```

Returns the array `[1,null,3,"a","b","c"]` as variant data.

### Example 3

```
ArrayConcat(Array(1, 2, 3), null)
```

Returns `null`.

Updated 1 day ago

---

[Array](/docs/array)[ArrayContains](/docs/arraycontains)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Notes](#notes)
  + [Examples](#examples)
  + - [Example 1](#example-1)
    - [Example 2](#example-2)
    - [Example 3](#example-3)