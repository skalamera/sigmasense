# Distance

# Distance

The **Distance** function calculates the minimum distance between two geographies, in specified units.

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

```
Distance(units, geog1, geog2)
```

The function arguments are:

units
:   Required
:   The unit of measurement for the distance.
:   Valid values are `"kilometers"`, `"meters"`, and `"miles"`.

geog1
:   Required
:   First geography of the pair between which we calculate the distance.
:   Must be in valid Geography format.
:   To work from known latitude and longitude values, use the [MakePoint](/docs/makepoint) or [MakeLine](/docs/makeline) functions.

geog2
:   Required
:   Second geography of the pair between which we calculate the distance.
:   Must be in valid Geography format.
:   To work from known latitude and longitude values, use the [MakePoint](/docs/makepoint) or [MakeLine](/docs/makeline) functions.

## Examples

```
Distance("kilometers", [Coordinates], MakePoint(0, 0))
```

```
Distance("miles", [Coordinates], MakePoint(0, 0))
```

The **Distance** function returns the following values for the **Coordinates** column, when specifying distance in either kilometers or miles from coordinates (0, 0):

![Example of the Distance function, showing the distance in kilometers and miles from a set of coordinates to the origin](https://files.readme.io/19770ed-function-distance-example.png)
> 🚩
>
> On Databricks connections, values might differ slightly from those shown in the examples. This is because Databricks represents earth using the [WGS 84 ellipsoid](https://en.wikipedia.org/wiki/World_Geodetic_System), while other connections assume a perfect sphere.

Updated 3 days ago

---

Related resources

* [Area](/docs/area)
* [Perimeter](/docs/perimeter)
* [Geography functions](/docs/geography-functions)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Examples](#examples)