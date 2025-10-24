# Ceiling

# Ceiling

Rounds the input number up to the closest multiple of equal or greater value.

## Usage

`Ceiling(number, factor)`

**number** (required) The number to be rounded.

**factor** [optional] The multiple to which the number will be rounded. The direction of rounding aligns with the positive or negative sign of the factor. The factor cannot be 0. Its default value is 1.

## Examples

(1) Returns 4.

`Ceiling(3.2)`

(2) Returns -3.

`Ceiling(-3.6)`

(3) Returns the **Ceiling** for each row in the input column.

`Ceiling([Cost])`

![For given cost data of 12.14, 12.25, 12.46, 12.58, 13.07, 13.21, 13.24, 18.05, and others, the ceiling of cost column has values of 13, 13, 13, 13, 14, 14, 14, and 19.](https://files.readme.io/853e391-1.png)

(4) Returns the **Ceiling** at a factor of 0.5 for each row in the input column.

`Ceiling([Cost], 0.5)`

![For given cost data of 12.14, 12.25, 12.46, 12.58, 13.07, 13.21, 13.24, 18.05, and others, the ceiling of cost column has values of 12.5, 12.5, 12.5, 13, 13.5, 13.5, 13.5, and 18.5.](https://files.readme.io/0d7b798-2.png)

(5) Returns the **Ceiling** at a factor of -0.25 for each row in the input column.

`Ceiling([Cost], -0.25)`

![For given cost data of 12.14, 12.25, 12.46, 12.58, 13.07, 13.21, 13.24, 18.05, and others, the ceiling of cost column has values of 12, 12.25, 12.25, 12.5, 13, 13, 13, and 18.](https://files.readme.io/a04957c-3.png)

(6) Returns the **Ceiling** at a factor of 2 for each row in the input column.

`Ceiling([Cost], 2)`

![For given cost data of 12.14, 12.25, 12.46, 12.58, 13.07, 13.21, 13.24, 18.05, and others, the ceiling of cost column has values of 14, 14, 14, 14, 14, 14, 14, and 20.](https://files.readme.io/be2c4e4-4.png)

Updated 3 days ago

---

Related resources

* [Floor](/docs/floor)
* [Round](/docs/round)

* [Table of Contents](#)
* + [Usage](#usage)
  + [Examples](#examples)