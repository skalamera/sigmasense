# RegressionSlope

# RegressionSlope

The **RegressionSlope** function calculates the slope of the linear regression line. This slope can be used to estimate how changes in one variable affects another.

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

```
RegressionSlope(y, x)
```

### Function arguments

|  |  |
| --- | --- |
| **y** | The dependent variable, expected to change as a result of changes in `x`. |
| **x** | The independent variable. |

## Notes

* The function returns null if the arguments used provide only a single data point.

## Example

A table contains an *AdSpend* column (tracking monthly advertising spend) and a *Revenue* column (tracking month revenue). You can use the **RegressionSlope** function to find the linear trend of *Revenue* as a function of *AdSpend*.

```
RegressionSlope([Revenue], [AdSpend])
```

A positive output means that as monthly advertising spend increases, monthly revenue increases. A negative output that as monthly advertising spend increases, monthly revenue decreases.

Updated 3 days ago

---

[RegressionR2](/docs/regressionr2)[StdDev](/docs/stddev)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + - [Function arguments](#function-arguments)
  + [Notes](#notes)
  + [Example](#example)