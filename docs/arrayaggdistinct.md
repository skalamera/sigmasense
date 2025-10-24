# ArrayAggDistinct

# ArrayAggDistinct

The **ArrayAggDistinct** function identifies distinct non-null row values in a column or group and aggregates them into a single array.

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

```
ArrayAggDistinct(value, [direction])
```

Function arguments:

|  |  |
| --- | --- |
| **value** | (required) The column containing values to join. |
| **direction** | (optional) The directional order to sort the column values.   * `“asc”` sorts values in ascending order. * `“desc”` sorts values in descending order.   When a direction isn’t specified, Sigma sorts values in the same order as the column referenced in the **value** argument. If the referenced column isn’t sorted, Sigma sorts values in ascending order by default. |

## Example

```
ArrayAggDistinct([Product Type], “asc”)
```

For each grouping (grouped by order number) the **ArrayAggDistinct** function returns an array containing distinct non-null values—sorted in ascending order—from the corresponding rows in the *Product Type* column.

![Table showing product data grouped by order number, with a column aggregating distinct product type values using the ArrayAggDistinct function.](https://files.readme.io/e409c19-image.png)

Updated 3 days ago

---

[ArrayAgg](/docs/arrayagg)[Avg](/docs/avg)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)