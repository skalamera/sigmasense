# Nominal

# Nominal

The **Nominal** function returns the nominal annual interest rate.

Lending institutions advertise the *nominal* rate of their loans. The nominal interest rate does not take into account the effect of compounding. The *effective* interest rate takes the compounding period into account, and it is a more accurate measure of interest charges.

## Syntax

```
Nominal(effective_rate, num_per_year)
```

Function arguments:

|  |  |
| --- | --- |
| **effective\_rate** | The effective interest rate as a decimal (for example, for 7%, input 0.07). |
| **num\_per\_year** | The number of compounding periods per year. |

## Notes

The general formula for the **Nominal** function is:

![](https://files.readme.io/52f0e7a-1.png)

## Examples

```
Nominal(.07, 12)
```

The nominal annual interest rate for an effective rate of 7%, paid 12 times a year (monthly). This example returns 6.78%.

```
Nominal(0.7, 26)
```

The nominal annual interest rate for an effective rate of 7%, paid 26 times a year (bi-weekly). This example returns 6.77%.

```
Nominal([Effective Rate], [Number of Periods])
```

You can use the nominal function to explore the change in the nominal interest rate based on the number of times it compounds.

![](https://files.readme.io/5cf4645-image.png)

Updated 3 days ago

---

Related resources

* [Effect](/docs/effect)
* [NOMINAL function in Microsoft documentation](https://support.microsoft.com/en-us/office/nominal-function-7f1ae29b-6b92-435e-b950-ad8b190ddd2b)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Notes](#notes)
  + [Examples](#examples)