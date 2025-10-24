# Geography

# Geography

The **Geography** function converts [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON) or [WKT](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) data into the [Geography](/docs/data-types-and-formats) data type.

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

In GeoJSON and the `Geography` data type, coordinate order is always `longitude, latitude`.

```
Geography(value)
```

The function arguments are:

value
:   Required
:   The content to convert to the [Geography](/docs/data-types-and-formats) data type.
:   Must be valid GeoJSON or WKT. Otherwise, the function returns `Null`.

## Notes

* Valid coordinates have longitude values between `-180` and `180`, and latitude values between `-90` and `90`.
  + Values outside of these ranges return `null`, and do not appear on maps like [Map - Geography](/docs/maps).
* On Databricks connections, the longitude value `180` is not valid. It is equivalent to the longitude value `-180`.

## Examples

```
Geography('{"coordinates":[-78,42],"type":"Point"}')
```

Converts the GeoJSON string `'{"coordinates":[-78,42],"type":"Point"}'` to the Geography data type, and returns `POINT(-78 42)`.

```
Geography([GeoJSON])
```

The **Geography** function returns the following values for the **GeoJSON** column:

![](https://files.readme.io/6bf01c8-1.png)

```
Geography("POINT(-78 42)")
```

Converts the WKT string `"POINT(-78 42)"` to the Geography data type, and returns `POINT(-78 42)`.

```
Geography([WKT])
```

The **Geography** function returns the following values for the **WKT** column:

![](https://files.readme.io/1b3357e-2.png)

Updated 3 days ago

---

Related resources

* [Json](/docs/json)
* [Text](/docs/text)
* [Geography functions](/docs/geography-functions)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Notes](#notes)
  + [Examples](#examples)