# CumulativeMin

# CumulativeMin

The **CumulativeMin** function identifies the minimum value of a column up to and including the current row value.

## Syntax

```
CumulativeMin(column)
```

Function Arguments:

|  |  |
| --- | --- |
| **column** | The column to reference when evaluating the cumulative minimum. |

> 🚧
>
> ### Cumulative functions depend on the order of the referenced column. When you change the column's sort order, the function output may change.

## Example

```
CumulativeMin([Sales])
```

A table contains the monthly sales for a store. The **CumulativeMin** function can be used to find the minimum monthly sales amount up to and including the current month.

![](https://files.readme.io/a630398-image.png)


---

(No changes were needed as the content was already valid MDX.)

Updated 3 days ago

---

Related resources

* [CumulativeMin](/docs/cumulativemin)
* [Min](/docs/min)
* [MovingMin](/docs/movingmin)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)