# MakeLine

# MakeLine

The **MakeLine** function constructs a LineString from a series of Point or LineString data.

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

```
MakeLine(geo1, geo2, ...)
```

Function arguments:

geo1
:   Required
:   A valid point or line value that can be located on the Earth's sphere; must comply with the [Geographic Coordinate System](https://en.wikipedia.org/wiki/Geographic_coordinate_system)

geo2
:   Required
:   A valid point or line value that can be located on the Earth's sphere; must comply with the [Geographic Coordinate System](https://en.wikipedia.org/wiki/Geographic_coordinate_system)

geo3 through geoN
:   Optional
:   A valid point or line value that can be located on the Earth's sphere; must comply with the [Geographic Coordinate System](https://en.wikipedia.org/wiki/Geographic_coordinate_system)

## Notes

* On BigQuery, Databricks, and Snowflake connections, arguments can be either points or lines. On Starburst connections, arguments must be points.
* When using line segments in arguments, Sigma treats the terminal points of the line as separate points, in order. For example, the following expressions are identical:

  ```
  MakeLine(point1, MakeLine(point2, point3), MakeLine(point4, point5, point6))
  ```

  ```
  MakeLine(point1, point2, point3, point4, point5, point6)
  ```

## Examples

### Example 1

```
MakeLine([Point], MakePoint(-74.044502, 40.689247))
```

Creates lines between the points in the **Point** column, and the location of the Statue of Liberty at coordinates (`-74.044502`, `40.689247`)

### Example 2

```
MakeLine(MakePoint(2.294481, 48.85837), [Point], MakePoint(-74.044502, 40.689247))
```

Creates lines between the location of the Eiffel Tower (`2.294481`, `48.85837`), the **Point** column, and the location of the Statue of Liberty (`-74.044502`, `40.689247`)

### Example 3

```
MakeLine(MakeLine(MakePoint(48.85837, 2.294481), MakePoint(-0.075278, 51.505554)), [Point], MakeLine(MakePoint(40.689247, -74.044502), MakePoint(-77.050636, 38.889248)))
```

Creates lines between the line between the Eiffel Tower (`2.294481`, `48.85837`) and the Tower Bridge ( `-0.075278`, `51.505554`), the **Point** column, and the line between the Empire State building (`-73.985428`, `40.748817`) and the Lincoln Memorial (`-77.050636`, `38.889248`).

![](https://files.readme.io/642f5e7-function-makeline-example.png)

Updated 3 days ago

---

Related resources

* [MakePoint](/docs/makepoint)
* [Geography functions](/docs/geography-functions)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Notes](#notes)
  + [Examples](#examples)
  + - [Example 1](#example-1)
    - [Example 2](#example-2)
    - [Example 3](#example-3)