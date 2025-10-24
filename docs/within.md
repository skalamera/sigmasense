# Within

# Within

The **Within** function determines if one geography is fully contained within another geography.

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

```
Within(geography1, geography2)
```

The function has these arguments:

geography1
:   Required
:   The geography value that might be contained within geography2.
:   Can be a point, a line, or polygon

geography2
:   Required
:   The geography value that might contain geography1.

## Examples

```
Within(Geography("POLYGON((1 1, 2 1, 2 2, 1 2, 1 1))"), Geography("POLYGON((0 0, 3 0, 3 3, 0 3, 0 0))"))
```

The function returns `True`, because the first polygon is fully contained within the second.

```
Within([Centroid], [Coordinates])
```

```
Within(MakePoint(-73.985428, 40.748817), [Coordinates])
```

The first **Within** function determines if the **Centroid** of the polygon is within the polygon, while the second function determines if the Empire State Building (-73.985428, 40.748817) is within the polygon.

![Example of Within function, confirming that the centroid of a polygon is within it](https://files.readme.io/0cc74b9-1.png)

```
Within([Coordinates], [Brooklyn])
```

The **Within** function determines if the values in the **Coordinates** column are within the boundaries of Brooklyn.

![Example of Within function, determining if a location is in Brooklyn](https://files.readme.io/8016df4-2.png)

Updated 3 days ago

---

Related resources

* [Centroid](/docs/centroid)
* [MakePoint](/docs/makepoint)
* [MakeLine](/docs/makeline)
* [Intersects](/docs/intersects)
* [Geography functions](/docs/geography-functions)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Examples](#examples)