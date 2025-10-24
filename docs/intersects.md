# Intersects

# Intersects

The **Intersects** function determines if one geography intersects another geography. If the two geographies intersect, the function returns `True`. Otherwise, it returns `False`.

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

**Intersects** is one of Sigma's [Geography functions](/docs/geography-functions-overview).

## Syntax

```
Intersects(geography1, geography2)
```

The function arguments are:

geography1
:   Required
:   The first geography to check for intersection.

geography2
:   Required
:   The second geography to check for intersection.

## Examples

```
Intersects(Geography("POLYGON((0 0, 2 0, 2 2, 0 2, 0 0))"), Geography("POLYGON((1 1, 3 1, 3 3, 1 3, 1 1))"))
```

The function returns `True` because the two polygons overlap.

```
Intersects([Brooklyn], [Queens])
```

If you define the Brooklyn and Queens boroughs as polygons (see [Geography functions overview](/docs/geography-functions-overview) for coordinates), then the **Intersects** function returns `True` because they share a waterway; see the following illustration.

![A map of the five boroughs of New York City shows that Brooklyn and Queens share a long border and a waterway](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/img/nyc-boroughs.png)

Updated 3 days ago

---

Related resources

* [Within](/docs/within)
* [MakePoint](/docs/makepoint)
* [MakeLine](/docs/makeline)
* [Geography functions](/docs/geography-functions)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Examples](#examples)