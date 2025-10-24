# ArrayExcept

# ArrayExcept

The **ArrayExcept** function returns an array of all unique elements from one specified array not included in another specified array. The output array is unordered.

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

```
ArrayExcept(array1, array2)
```

### Function arguments

|  |  |
| --- | --- |
| **array1** | An array that contains elements to be *included* in the new array. |
| **array2** | An array that contains elements to be *excluded* from the new array. |

## Notes

* If either or both input arguments are null values, the function returns `null`.
* If all values in the first array are included in the second array, an empty array is returned.

## Example

A table lists all available colors of different clothing items. To see all colors available for each item, excluding the colors black and white, use the **ArrayExcept** function:

```
ArrayExcept([Colors], Array("black", "white"))
```

ArrayExcept returns all colors listed in the `[Colors]` column, excluding the colors specified in the `("black", "white")` array.

![5 rows of data with an item column, a colors column, and a column showing the output of ArrayExcept. The colors column has arrays of colors for each item. The shirt row has an array of white, black, black, and the dress array has red, green white. The ArrayExcept column for shirt shows an empty array and for dress shows red, green.](https://files.readme.io/b115458f7b1a7a31fe4b19e58f6474838c67b22b666c2d20ef386880b207fdd9-arrayexcept.png)

Updated 3 days ago

---

[ArrayDistinct](/docs/arraydistinct)[ArrayIntersection](/docs/arrayintersection)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + - [Function arguments](#function-arguments)
  + [Notes](#notes)
  + [Example](#example)