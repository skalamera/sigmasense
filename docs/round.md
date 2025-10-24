# Round

# Round

The **Round** function rounds a number to the specified number of digits. When digits is not specified, the number is rounded to the nearest whole number by default.

## Usage

```
Round(number, [digits])
```

Function arguments:

* **number** (required) Number to be rounded.
* **digits** (optional) Number of decimal places to round the number. If not provided, defaults to 0.

The underlying formula is as follows:

```
(number/10^digits) * (10^digits)
```

> 📘
>
> ### A negative digits value returns an integer with the specified least-significant digits zeroed.

> 📘
>
> ### Rounding is different than formatting. The result can have fewer digits than specified. Rounding does not add trailing zeroes.

## Example

```
Round(Pi())
```

* Returns 3

```
Round(3.1, 2)
```

* Returns 3.1

```
Round(1234, -2)
```

* Returns 1200

## More examples

![Table showing numbers rounded by different decimal places, including rounding by 1, 2, -1 and -2](https://files.readme.io/76abc1d-vvv.png)

Updated 3 days ago

---

Related resources

* [Ceiling](/docs/ceiling)
* [Floor](/docs/floor)
* [RoundUp](/docs/roundup)
* [RoundDown](/docs/rounddown)

* [Table of Contents](#)
* + [Usage](#usage)
  + [Example](#example)
  + [More examples](#more-examples)