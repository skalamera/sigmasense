# RoundUp

# RoundUp

The **RoundUp** function rounds a number up to the specified number of digits. When digits is not specified, the number is rounded to the nearest whole number by default.

## Usage

`RoundUp(number, [digits])`

Function arguments:

* **number** (required) The number to be rounded.
* **digits** (optional) The number of decimal places to which to round. If not provided, defaults to 0.

If the digits value is negative, the function will return an integer with that many least-significant digits zeroed (see the example using `RoundUp([Cost], -2)` below).

## Example

`RoundUp(3.141, 2)`

* Returns 3.15

`RoundUp(-3.141, 2)`

* Returns -3.14.

`RoundUp([Cost], 2)`

* Rounds the value for each row in the input column up. Numbers are rounded by 2 digits.

  ![Screenshot of results rounded to two decimal places](https://files.readme.io/ab56919-a.png)

`RoundUp([Cost], -2)`

* Rounds the input number up and replaces its last 2 digits with 0s. A negative digits value returns an integer with that many least-significant digits zeroed.

  ![Screenshot of results rounded to whole numbers](https://files.readme.io/cfd80ed-b.png)

Updated 3 days ago

---

Related resources

* [Ceiling](/docs/ceiling)
* [Round](/docs/round)
* [RoundDown](/docs/rounddown)
* [MRound](/docs/mround)
* [Floor](/docs/floor)

* [Table of Contents](#)
* + [Usage](#usage)
  + [Example](#example)