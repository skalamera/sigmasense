# Json

# Json

The **Json** function converts a value to JSON (or [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON) when converting geography data).

## Syntax

```
Json(input)
```

Function arguments:

input
:   (required) The data to convert to JSON

## Notes

* On connections that support geography, the **Json** function can be used to convert valid geography data to [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON). For more information, see the second example in [examples](#examples).
* In GeoJSON and the `Geography` data type, coordinate order is always `longitude, latitude`.

## Examples

```
Json([Cust JSON as Text])
```

Returns Json values for the variant data in the *Cust JSON as Text* column.

![](https://files.readme.io/38dc49e-99.png)

```
Json(MakePoint(179, 90))
```

Converts the geography point (179, 90) to GeoJSON, and returns `{"coordinates":[179,90],"type":"Point"}` as variant data.

Updated 3 days ago

---

Related resources

* [Variant](/docs/variant)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Notes](#notes)
  + [Examples](#examples)