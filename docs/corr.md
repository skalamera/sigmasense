# Corr

# Corr

The **Corr** function calculates the Pearson correlation coefficient, also known as the bivariate correlation, of two numerical columns.

> 📘
>
> This function isn't compatible with all data platform connections. To check if your connection supports it, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

## Syntax

`Corr(number column 1, number column 2)`

Function arguments:

* **number column 1** (required) - A column of numbers representing the dependent data.
* **number column 2** (required) - A column of numbers representing the independent data.

## Example

`Corr([Quantity], [Price])`

![](https://files.readme.io/11d49f2-Screenshot_2023-03-07_at_12.49.31_PM.png)
> 📘
>
> ### With this negative correlation, we can see that as price increases, the quantity of purchased item decreases.

Updated 3 days ago

---

Related resources

* [CumulativeCorr](/docs/cumulativecorr)
* [MovingCorr](/docs/movingcorr)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)