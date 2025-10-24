# RegressionR2

# RegressionR2

The **RegressionR2** function calculates the R2 value, or coefficient of determination, of the linear regression line. This value is a goodness-of-fit measure, and explains how well the independent variable explains variations in the dependent variable.

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

```
RegressionR2(y, x)
```

### Function arguments

|  |  |
| --- | --- |
| **y** | The dependent variable, expected to change as a result of changes in `x`. |
| **x** | The independent variable. |

## Notes

* The function returns null if the arguments used provide only a single data point.

## Example

A table contains an *AdSpend* column (tracking monthly advertising spend) and a *Revenue* column (tracking month revenue). You can use the **RegressionR2** function to calculate how well advertising spend explains variations in revenue.

```
RegressionR2([Revenue], [AdSpend])
```

Possible output values range from `0` (no correlation) to `1` (perfect correlation), representing a percentage from 0 to 100. If the output is `0.4`, for example, 40% of the variation in revenue can be explained by changes in advertising spend.

Updated 3 days ago

---

[RegressionIntercept](/docs/regressionintercept)[RegressionSlope](/docs/regressionslope)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + - [Function arguments](#function-arguments)
  + [Notes](#notes)
  + [Example](#example)