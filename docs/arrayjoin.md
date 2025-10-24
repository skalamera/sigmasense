# ArrayJoin

# ArrayJoin

The **ArrayJoin** function joins elements of an array into a single text string.

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

```
ArrayJoin(array, [separator], [nullReplacement])
```

Function arguments:

|  |  |
| --- | --- |
| **array** | An array containing elements to join into a single text string.   * If you reference a column, it must be a variant column containing data structured as a JSON array (for example, `[“red”, “blue”, “yellow”]`). Other column types or data structured as JSON objects return `null` values. |
| **separator** | [optional] A character or string to return between joined elements.   * If unspecified, Sigma applies a comma without spaces by default. |
| **nullReplacement** | [optional] A character or string to replace elements with `null` values.   * If unspecified, Sigma omits `null` values by default |

## Notes

* Nested JSON arrays or objects in the **array** arguments are converted into text strings using your data platform’s JSON-to-text method. This can impact the nested JSON structure, key-value pair order, and white space (like spaces, tabs, and line breaks).
* If any argument is `null`, the function returns `null`.

## Examples

### Example 1

```
ArrayJoin([JSON array], “, ”)
```

Returns a single text string containing each non-null element from the *JSON array* column separated by a comma and a space.

![](https://files.readme.io/46338cc-image.png)

### Example 2

```
ArrayJoin(Array(“red”, null, “blue”, “yellow”), “ or ”, “*”)
```

Returns `red or * or blue or yellow`.

### Example 3

```
ArrayJoin(Json('[[1,"a"], {"b":2}, "c", 3]'), ";")
```

Returns `[1,"a"];{"b":2};c;3`.

Updated 3 days ago

---

[ArrayIntersection](/docs/arrayintersection)[ArrayLength](/docs/arraylength)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Notes](#notes)
  + [Examples](#examples)
  + - [Example 1](#example-1)
    - [Example 2](#example-2)
    - [Example 3](#example-3)