# ArrayAgg

# ArrayAgg

The **ArrayAgg** function identifies non-null row values in a column or group and aggregates them into a single array.

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

```
ArrayAgg(value)
```

Function argument:

|  |  |
| --- | --- |
| **value** | (required) The column containing values to join. |

## Example

```
ArrayAgg([County Name])
```

For each grouping (grouped by state name) the **ArrayAgg** function returns an array containing non-null values from the corresponding rows in the *County Name* column.

![Table showing counties grouped by state name, with a column aggregating all county names for each state using the ArrayAgg function.](https://files.readme.io/81a6047-image.png)

Updated 3 days ago

---

Related resources

* [ListAgg](/docs/listagg)
* [Concat](/docs/concat)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)