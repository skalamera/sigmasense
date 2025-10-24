# VariancePop

# VariancePop

The **VariancePop** function calculates the population variance of a column or group. This statistical measure determines the spread of distribution or degree to which the column or grouped values deviate from the mean. A small variance indicates the values are close to the mean (less variability), while a large variance indicates the values are dispersed farther from the mean (greater variability).

**VariancePop** assumes your dataset represents an entire population. If the dataset is a sample of a larger population, use the **[Variance](/docs/variance)** function to estimate unbiased variance.

> 📘
>
> ### Sigma calls the underlying CDW or DBMS function that uses the statistical sample variance definition. Refer to your CDW or DBMS provider’s documentation for details about the called function.

## Syntax

```
VariancePop(field)
```

Function argument:

field
:   (required) The column to reference when calculating population variance.

## Underlying formula

|  |
| --- |
| ∑( xi – x̄ )2 |
| n |

* xi = each sample value
* x̄ = the mean of all sample values
* n = the total number of sample values (sample size)

## Example

A table contains the average temperature recorded for each month in 2021 and 2022. If the data is grouped by year, you can use the following formula to measure and compare the temperature variability throughout each year.

```
VariancePop([Avg monthly temp])
```

When you calculate the formula in the *Year* grouping, the function returns the population variance for each year. This example indicates greater temperature fluctuation in 2022.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Functions/variancepop_example.png)

Updated 3 days ago

---

Related resources

* [Variance](/docs/variance)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Underlying formula](#underlying-formula)
  + [Example](#example)