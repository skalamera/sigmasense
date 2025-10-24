# Latitude

# Latitude

The **Latitude** function obtains the latitude of a point.

The input column must be a valid location within the [Geographic Coordinate System.](https://en.wikipedia.org/wiki/Geographic_coordinate_system)

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

```
Latitude(point)
```

The function argument is:

point
:   Required
:   A valid Point value that can be located on the Earth's sphere; must comply with the [Geographic Coordinate System](https://en.wikipedia.org/wiki/Geographic_coordinate_system)
:   The function does not support other coordinate types, such as lines, polygons, and so on.

## Example

```
Latitude([Coordinates])
```

The function **Latitude** extracts the latitude of a point from the **Coordinate** column:

![](https://files.readme.io/850f42b-function-latitude-example.png)

Updated 3 days ago

---

Related resources

* [Geography](/docs/geography)
* [Longitude](/docs/longitude)
* [Geography functions](/docs/geography-functions)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)