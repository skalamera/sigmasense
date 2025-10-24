# RegressionIntercept

# RegressionIntercept

The **RegressionIntercept** function calculates the y-intercept of the linear regression line. This provides you with the predicted value of a variable when the other variable is equal to zero.

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

```
RegressionIntercept(y, x)
```

### Function arguments

|  |  |
| --- | --- |
| **y** | The dependent variable, expected to change as a result of changes in `x`. |
| **x** | The independent variable. |

## Notes

* The function returns null if the arguments used provide only a single data point.

## Example

A table contains an *AdSpend* column (tracking monthly advertising spend) and a *Revenue* column (tracking month revenue). You can use the **RegressionIntercept** function to find what the baseline monthly revenue is when the monthly advertising spend is zero.

```
RegressionIntercept([Revenue], [AdSpend])
```

Updated 3 days ago

---

[PercentOfTotal](/docs/percentoftotal)[RegressionR2](/docs/regressionr2)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + - [Function arguments](#function-arguments)
  + [Notes](#notes)
  + [Example](#example)