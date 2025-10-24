# Effect

# Effect

The **Effect** function returns the effective annual interest rate.

Lending institutions advertise the *nominal* rate of their loans. The nominal interest rate does not take into account the effect of compounding. The *effective* interest rate takes the compounding period into account, and it is a more accurate measure of interest charges.

## Syntax

```
Effect(nominal_rate, num_per_year)
```

Function arguments:

|  |  |
| --- | --- |
| **nominal\_rate** | The nominal interest rate as a decimal (for example, for 7%, input `0.07`). |
| **num\_per\_year** | The number of compounding periods per year. |

## Notes

The general formula for the **Effect** function is:  
![Effect function](https://files.readme.io/6cee9da-function-effect.png)

## Examples

```
Effect(.0678, 12)
```

The effective annual interest rate for an effective rate of 6.78%, paid 12 times a year (monthly). This example returns 7.00%.

```
Nominal(0.677, 26)
```

The nominal annual interest rate for an effective rate of 6.77%, paid 26 times a year (bi-weekly). This example returns 7.00%.

```
Effect(0.1, [Number of Periods])
```

Explore how the the effective annual interest rate changes when the nominal interest rate is 10% applies to investments with a different number of periods.

![](https://files.readme.io/0feb8b8-image.png)

Updated 3 days ago

---

Related resources

* [Nominal](/docs/nominal)
* [EFFECT function in Microsoft documentation](https://support.microsoft.com/en-us/office/effect-function-910d4e4c-79e2-4009-95e6-507e04f11bc4)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Notes](#notes)
  + [Examples](#examples)