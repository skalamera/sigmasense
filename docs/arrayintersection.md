# ArrayIntersection

# ArrayIntersection

The **ArrayIntersection** function compares two arrays and returns an array of all overlapping elements, without duplicates. The output array is unordered.

If you want to return an array of all unique elements from one specified array not included in another specified array, see [ArrayExcept](/docs/arrayexcept).

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

```
ArrayIntersection(array1, array2)
```

Function arguments:

|  |  |
| --- | --- |
| **array1** | Array to be compared for overlapping elements. |
| **array2** | Array to be compared for overlapping elements. |

## Notes

* If either or both input arguments are null values, the function returns `null`.
* The function is “null aware”. If both input arrays contain a null element, the returned array will contain one.
* If there are no overlapping values, an empty array is returned.
* If one or both of the input arguments are non-null values or non-array variants (such as an object, or other json), an empty array is returned.

## Example

A table lists all the available colors of different clothing items. To see what items are available in black or white, you can use the **ArrayIntersection** function:

```
ArrayIntersection([Colors], Array("black", "white"))
```

ArrayIntersection compares the arrays listed in the `[Colors]` column with the `("black", "white")` array.

![Example use of ArrayIntersection. A table with 3 columns - Items (listing clothing items), Colors (array of colors the item comes in), and ArrayIntersection (displaying function output).](https://files.readme.io/12b3d2a2b92b8f1bcd88937ff03b760a74a52e2fa4c06df94781319ffa1869d8-arrayintersection_example.png)

Both “*black*” and “*white*” are present in the *Colors* column for *Shoes*, so **ArrayIntersection** returns an array with both colors. As nothing is listed in the *Pants* row, the function returns a null value.

Updated 3 days ago

---

[ArrayExcept](/docs/arrayexcept)[ArrayJoin](/docs/arrayjoin)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Notes](#notes)
  + [Example](#example)