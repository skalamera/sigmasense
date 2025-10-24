# MakePoint

# MakePoint

The **MakePoint** function constructs a point from latitude and longitude data that describe a location within the [Geographic Coordinate System.](https://en.wikipedia.org/wiki/Geographic_coordinate_system)

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

```
MakePoint(longitude, latitude)
```

The function arguments are:

longitude
:   Required
:   A valid longitude value. Must be within the range of `-180` to `180`.


latitude
:   Required
:   A valid latitude value. Must be within the range of `-90` to `90`.

> 🚩
>
> On Databricks connections, the longitude value `180` is not valid. It is equivalent to the longitude value `-180`.

## Example

```
MakePoint([Longitude],[Latitude])
```

The MakePoint function constructs the following points from the Longitude and Latitude columns:

![Example of the MakePoint function shown over three columns. Latitude and Longitude are combined to make a column of point values.](https://files.readme.io/baa19bf-function-makepoint-example.png)

Updated 3 days ago

---

Related resources

* [MakeLine](/docs/makeline)
* [Latitude](/docs/latitude)
* [Longitude](/docs/longitude)
* [Geography functions](/docs/geography-functions)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)