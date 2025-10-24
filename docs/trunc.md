# Trunc

# Trunc

Truncates the input value to the specified number of digits or decimal places.

## Usage

```
Trunc(number, [digits])
```

**number** (required) The number to be truncated

**digits** [optional] The number of decimal places to which to round. Defaults to 0.  
If "digits" value is negative, the function will return an integer with that many least-significant digits zeroed (see example 4 below).

## Examples

(1) Returns 5.24

```
Trunc(5.2463, 2)
```

(2) Returns 5.

```
Trunc(5.678)
```

(3) Truncates the value in each row of the input column to 3 decimal places.

```
Trunc([Cost], 3)
```

![Screenshot showing an applied Trunc truncating the value of each row of the input column to 3 decimal places](https://files.readme.io/153bbaa-c.png)

(4) Rounds the input number down and replaces its last 2 digits with 0s. A negative "digits" value returns an integer with that many least-significant digits zeroed.

```
Trunc([Cost], -2)
```

![Applied Trunc rounding the input down and replacing last two digits with zeroes](https://files.readme.io/1b3a2a2-d.png)

Updated 3 days ago

---

[Tan](/docs/tan)[Passthrough functions](/docs/passthrough-functions)

* [Table of Contents](#)
* + [Usage](#usage)
  + [Examples](#examples)