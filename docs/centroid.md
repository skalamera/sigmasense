# Centroid

# Centroid

The **Centroid** function calculates the center of any geography object, and returns it as a point. You can use the Centroid function to determine the practical distance between two polygons.

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

```
Centroid(polygon)
```

The function argument is:

polygon
:   Required
:   The object for which to calculate the geometric center
:   Must be a valid point, line, or polygon.

## Examples

```
Centroid(MakePoint(0, 0))
```

Calculates the center of the point (0, 0) and returns `Point(0 0)`.

```
Centroid(MakeLine(MakePoint(0, 0), MakePoint(10, 0)))
```

Calculates the center of the line between (0, 0) and (10, 0) and returns `Point(5 0)`.

```
Centroid(Geography("POLYGON((-10 10, 10 10, 10 -10, -10 -10, -10 10))"))
```

Calculates the center of the polygon and returns `Point(0 0)`.

```
Centroid([Origin to Destination])
```

Calculates the center of the line between the origin and destination airports and returns the midpoint between them.

![A Sigma table shows columns for origin and destination airports, their coordinates, a line between them, and the midpoint of that line. The Midpoint column uses the Centroid function to calculate the midpoint between the origin and destination coordinates](https://files.readme.io/895f05ce8da06583089d77cae99d3ffe15dbbc5dabf7dccb050653597a887d0d-Flights_with_midpoints.png)

Updated 3 days ago

---

Related resources

* [Within](/docs/within)
* [Intersects](/docs/intersects)
* [Geography functions](/docs/geography-functions)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Examples](#examples)