# CumulativeCorr

# CumulativeCorr

The **CumulativeCorr** function calculates the correlation coefficient of the input column up to and including the current value.

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

```
CumulativeCorr([Column 1], [Column 2])
```

Function Arguments:

* **[Column 1]** (required) - The column representing the dependent data.
* **[Column 2]** (required) - The column representing the independent data.

> 📘
>
> Cumulative functions depend on the order of the given column. If you change the sorting you will change the result.

## Example

```
CumulativeCorr([Weekly Cost], [Weekly Revenue])
```

A table contains the weekly revenue of a store and the total amount spent by that store that week. The **CumulativeCorr** function can be used to find the correlation coefficient up to and including each row value.

![](https://files.readme.io/d33b12a-mmm.png)
> 📘
>
> This function is not currently supported on Snowflake or Redshift connections.

Updated 3 days ago

---

Related resources

* [Corr](/docs/corr)
* [MovingCorr](/docs/movingcorr)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)