# Area

# Area

The **Area** function calculates the area of a geography polygon, in specified units.

When you apply the **Area** function to geography points or geography lines, Sigma returns 0.

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

```
Area(units, polygon)
```

The function arguments are:

units
:   Required
:   The unit of measurement for the area
:   Valid values are `"square_kilometers"`, `"square_meters"`, and `"square_miles"`.

polygon
:   Required
:   The object for which we calculate the area
:   Must be in valid Geography polygon format.
:   To work from known latitude and longitude values, use the [MakePoint](/docs/makepoint) or [MakeLine](/docs/makeline) functions.

## Examples

```
Area("square_kilometers", [Coordinates])
```

```
Area("square_meters", [Coordinates])
```

```
Area("square_miles", [Coordinates])
```

The **Area** function returns the following values for the **Coordinates** column values that define a polygon, when specifying area in square kilometers, square meters, or square miles:

![All three examples of the area function are shown in a table for several records worth of coordinates](https://files.readme.io/afb5234-function-area-example.png)
> 🚩
>
> On Databricks connections, values might differ slightly from those shown in the examples. This is because Databricks represents earth using the [WGS 84 ellipsoid](https://en.wikipedia.org/wiki/World_Geodetic_System), while other connections assume a perfect sphere.

Updated 3 days ago

---

Related resources

* [Distance](/docs/distance)
* [Perimeter](/docs/perimeter)
* [Geography functions](/docs/geography-functions)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Examples](#examples)