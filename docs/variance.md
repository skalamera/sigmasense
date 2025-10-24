# Variance

# Variance

The **Variance** function estimates the sample variance of a column or group. This statistical measure determines the spread of distribution or degree to which the column or grouped values deviate from the mean. A small variance indicates the values are close to the mean (little variability), while a large variance indicates the values are dispersed farther from the mean (greater variability).

**Variance** assumes your dataset is a sample of a larger population. If the dataset represents an entire population, use the **[VariancePop](/docs/variancepop)** function to calculate actual variance.

> 📘
>
> ### Sigma calls the underlying CDW or DBMS function that uses the statistical sample variance definition. Refer to your CDW or DBMS provider’s documentation for details about the called function.

## Syntax

```
Variance(field)
```

Function argument:

field
:   (required) The column to reference when estimating sample variance.

## Underlying formula

|  |
| --- |
| ∑( xi – x̄ )2 |
| n – 1 |

* xi = each sample value
* x̄ = the mean of all sample values
* n = the total number of sample values (sample size)

## Example

A table contains a sample of customer ratings for specific products. If the data is grouped by product, you can use the following formula to measure and compare the ratings variability for each product.

```
Variance([Customer rating (0-5)])
```

When you calculate the formula in the *Product* grouping, the function returns the sample variance for each product. This example indicates a broader range of customer ratings for Product B.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Functions/variance_example.png)

Updated 3 days ago

---

Related resources

* [VariancePop](/docs/variancepop)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Underlying formula](#underlying-formula)
  + [Example](#example)