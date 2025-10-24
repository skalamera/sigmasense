# Perimeter

# Perimeter

The **Perimeter** function calculates the perimeter of a geography, in specified units.

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

```
Perimeter(units, polygon)
```

The function arguments are:

units
:   Required
:   The unit of measurement for the perimeter.
:   Valid values are `"kilometers"`, `"meters"`, and `"miles"`.

polygon
:   Required
:   The object for which we calculate the perimeter.
:   Must be in valid Geography polygon format.

## Examples

```
Perimeter("meters", [Coordinates])
```

```
Perimeter("kilometers", [Coordinates])
```

```
Perimeter("miles", [Coordinates])
```

The **Perimeter** function returns the following values for the **Coordinates** column values that define a polygon, when specifying area in meters, kilometers, or miles:

![Examples of the Perimeter function, showing the perimeter in meters, kilometers, and miles](https://files.readme.io/4bf256d-k.png)
> 🚩
>
> On Databricks connections, values might differ slightly from those shown in the examples. This is because Databricks represents earth using the [WGS 84 ellipsoid](https://en.wikipedia.org/wiki/World_Geodetic_System), while other connections assume a perfect sphere.

Updated 3 days ago

---

Related resources

* [Distance](/docs/distance)
* [Area](/docs/area)
* [Geography functions](/docs/geography-functions)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Examples](#examples)