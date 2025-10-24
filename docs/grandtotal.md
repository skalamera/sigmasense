# GrandTotal

# GrandTotal

The **GrandTotal** formula returns the grand total for the given aggregate formula. GrandTotal is shorthand for **Subtotal(aggregate, "grand\_total")**.

## Syntax

`GrandTotal(aggregate)`

Function arguments:

* **aggregate** (required) - The [aggregate](/docs/aggregate-functions-overview) formula to use in the function.
* Examples: `Count(), Sum([Sales Amount])`

## Example

In a chart visualizing order counts per Product Type and Region, you can add a calculated column with the formula to the tooltip:

`GrandTotal(CountDistinct([Order Number]))`

 To see an overall total count of distinct orders across all categories.

* The calculation is shown in the tooltip in this example, but is usable anywhere an aggregate formula is allowed.  
  ![company apps](https://files.readme.io/9ff429d-GrandTotal.png)

Updated 3 days ago

---

Related resources

* [Subtotal](/docs/subtotal)
* [PercentOfTotal](/docs/percentoftotal)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)