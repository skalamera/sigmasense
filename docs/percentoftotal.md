# PercentOfTotal

# PercentOfTotal

The **PercentOfTotal** function returns the percent of total for an aggregate formula. This function is shorthand for: aggregate / Subtotal(aggregate, mode, parameters).

> 📘
>
> ### This function must be used with aggregated data in a grouped table. For a detailed video walkthrough that uses this function, see [Building complex formulas with grouped data](https://www.sigmacomputing.com/resources/training-videos/table-grouping-and-functions#complex-formulas).

## Syntax

```
PercentOfTotal(aggregate, [mode], [parameters])
```

Function arguments:

* **aggregate** (required) - The [aggregate](/docs/aggregate-functions-overview) formula to use
* **mode** (optional) - The mode to use when calculating the aggregate formula. Mode determines which dimension(s) to use when performing the calculation.

  + General purpose modes

    - `“grand_total”` (default for visualizations and pivot tables) - Calculates the percent of grand total for the aggregate formula.
  + Visualization modes

    - `“color”` - Calculates the aggregate percent of total using only the column specified for COLOR.
    - `“x_axis”` - Calculates the aggregate percent of total using only the column(s) placed on the X-AXIS.
    - `“trellis_column”` / `“trellis_row”` - Calculates the aggregate percent of total using only the dimension specified for the TRELLIS COLUMN or TRELLIS ROW.
  + Pivot table modes

    - `“column”` / `“row”` - Calculates aggregate percent of total for the column or row total.
    - `“column_parent”` / `“row_parent”` - Calculates the aggregate percent of total for the column or row total, relative to the subtotal calculation for the parent dimensions.
  + Table modes

    - `“parent_grouping”` (default for tables) - Calculates the aggregate formula using the grouping keys from a parent grouping. This is equivalent to creating the aggregate calculation in a parent grouping and referencing it from a column in a lower grouping.
* **parameters** (optional) - An additional parameter specific to the mode.

  + Only applicable to the following modes: "column\_parent", "row\_parent" and "parent\_grouping". For these modes, this 3rd parameter specifies how many parent dimensions to ignore.

---

## Examples

```
PercentOfTotal(Sum([Quantity] * [Price]), "row")
```

* The numerator of the percentage is the aggregate formula calculated along rows and columns.
* The denominator of the percentage is the aggregate formula calculated along the rows.
* The pivot table subtotals calculate the percent of total at the expected granularity.

![](https://files.readme.io/ea6b487-percenttotal2.png)

```
PercentOfTotal(Sum([Quantity] * [Price]), "x_axis")
```

* The numerator of the percentage is the aggregate formula calculated along the x-axis and color.
* The denominator of the percentage is the aggregate formula calculated along the x-axis.
* The calculation is shown in the tooltip, but is usable anywhere an aggregate formula is allowed.

![](https://files.readme.io/ca53f0c-percentoftotal1A.png)

Updated 3 days ago

---

Related resources

* [GrandTotal](/docs/grandtotal)
* [Subtotal](/docs/subtotal)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Examples](#examples)