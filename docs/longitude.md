# Longitude

# Longitude

The **Longitude** function obtains the longitude of a point.

The input column must be a valid location within the [Geographic Coordinate System.](https://en.wikipedia.org/wiki/Geographic_coordinate_system)

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

```
Longitude(point)
```

The function argument is:

point
:   Required
:   A valid point value that can be located on the Earth's sphere; must comply with the [Geographic Coordinate System](https://en.wikipedia.org/wiki/Geographic_coordinate_system)
:   The function does not support other coordinate types, such as lines, polygons, and so on.

## Example

```
Longitude([Coordinates])
```

The function **Longitude** extracts the latitude of a point from the **Coordinate** column:

![](https://files.readme.io/ed0e95d-function-logitude-example.png)

Updated 3 days ago

---

Related resources

* [Latitude](/docs/latitude)
* [Geography functions](/docs/geography-functions)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)