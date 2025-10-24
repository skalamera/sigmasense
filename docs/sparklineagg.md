# SparklineAgg (Beta)

# SparklineAgg (Beta)

> 📘
>
> This feature isn't supported in all regions. To check if it is supported in your region, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

The **SparklineAgg** function generates sparkline charts by aggregating values over time. If you want to create sparklines for JSON data, see the [Sparkline](/docs/sparkline) function.

> 💡
>
> ### Sparklines can also be created from a column containing pre-formatted data. See [Create sparklines from a table](/docs/create-sparklines-in-a-table).

## Syntax

```
SparklineAgg(category, aggregate)
```

### Function arguments

|  |  |
| --- | --- |
| **category** | The column to be used for the sparkline’s x-axis. |
| **aggregate** | The aggregate formula to be used for the sparkline’s y-axis, representing the aggregate of the category argument. |

## Notes

* To create meaningful sparklines, add a grouping to your table. Groupings ensure multiple values are available for use in the sparkline. For more information on groupings, see [Group columns in a table](/docs/create-and-manage-tables#group-columns-in-a-table).
* **SparklineAgg** charts the values provided in the **category** column and returns variant data that renders as a sparkline chart in the table. You cannot copy from the chart canvas.
* To format the chart output of **SparklineAgg** (color, chart type, interpolation, etc), see [Format sparklines](/docs/create-sparklines-in-a-table#format-sparklines) in [Create sparklines in a table](/docs/create-sparklines-in-a-table).

## Example

A table, **PLUGS\_ELECTRONICS\_HANDS\_ON\_LAB\_DATA**, contains information an electronic retailer’s sales, including columns such as:

* *Product Name*: Name of electronic product sold
* *Date*: Date and time of sale transaction
* *Quantity*: Number of a specific product sold during the transaction

To see how the sales of each product have changed month to month, you can use **SparklineAgg**:

1. Group the table by product name. Select + **Add grouping**, then search for and select **Product Name**.
2. Select + **Add calculation**. In the formula bar, enter:

```
SparklineAgg(DateTrunc("month", [Date]), Sum([Quantity]))
```

Entering `DateTrunc("month", [Date])` as the **category** argument uses the [DateTrunc](/docs/datetrunc) function to truncate the value in the *Date* column to months. These month values form the x-axis of the sparkline. Entering `Sum([Quantity])` as the **aggregate** argument ensures the y-axis reflects the total quantity of products sold in each month.

Your table might look something like:

![Grouped table with a product name column and a sparkline column showing the aggregate sum of quantity sold for each product name by month.](https://files.readme.io/a2fec4ff1a67c2152b3ca261552ed204c34ea935361b980a49fda5810e1572d3-sparklineagg_function_image.png)

The sparklines here represent changes in the quantity of each product sold by month.

If you want to change the format (e.g. chart type, color, interpolation) of your sparklines, see [Format sparklines](/docs/create-sparklines-in-a-table#format-sparklines) in [Create sparklines in a table](/docs/create-sparklines-in-a-table).

Updated 3 days ago

---

[Sparkline (Beta)](/docs/sparkline)[Date functions](/docs/date-functions)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + - [Function arguments](#function-arguments)
  + [Notes](#notes)
  + [Example](#example)