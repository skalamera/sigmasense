# MRound

# MRound

Rounds the input number to the closest multiple of the given factor.

## Usage

```
MRound(number, [factor])
```

**number** (required) The number to be rounded.

**factor** [optional] The multiple to which the number will be rounded. The positive or negative sign of the factor is not considered. This value cannot be 0. The default value is 1.

## Examples

(1) Rounds the Number column by a factor of 1 because no argument is passed. This is equivalent to the result of the factor of (-1).

```
MRound([Number])
```

![](https://files.readme.io/d9eb5d4-1.png)

(2) Rounds the value for each row in the input column to a multiple of 50. The positive or negative sign of the factor (-50) is not considered. As such, they return the same result.

```
MRound([Cost], 50)
```

![](https://files.readme.io/63b93f6-2.png)

(3) Returns 500.

```
MRound(-456, 100)
```

Updated 3 days ago

---

Related resources

* [Round](/docs/round)
* [Ceiling](/docs/ceiling)
* [Floor](/docs/floor)

* [Table of Contents](#)
* + [Usage](#usage)
  + [Examples](#examples)