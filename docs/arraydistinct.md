# ArrayDistinct

# ArrayDistinct

The **ArrayDistinct** function returns the input array *without* duplicate values and including null values.

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

```
ArrayDistinct(array)
```

The **ArrayDistinct** function has the following argument:

array
:   Required.
:   The input array that Sigma parses to find and remove duplicates,
:   Must be an array structure; to create single array from a column, use the [ArrayAgg](/docs/arrayagg) function,

## Example

```
ArrayDistinct(Array('a', 1, 2, 1, ‘a'))
```

This may return `[1, 2, 'a']`. Note that the order elements in the the resulting array may not match the order of the input array.

```
ArrayDistinct([Open prices array])
```

The **ArrayDistinct** function returns the following values for the **Open prices array** column as **Distinct open prices array**; note the differences in array length for each column:

![](https://files.readme.io/1b908cd-function-arraydistinct-example.png)

Updated 3 days ago

---

Related resources

* [ArrayLength](/docs/arraylength)
* [ArrayContains](/docs/arraycontains)
* [ArraySlice](/docs/arrayslice)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)