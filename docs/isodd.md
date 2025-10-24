# IsOdd

# IsOdd

The **IsOdd** function returns True if the integer part of a number is odd and returns False is it is even.

To return True for even values and False for odd, see [IsEven](/docs/iseven).

## Syntax

```
IsOdd(value)
```

### Function arguments

|  |  |
| --- | --- |
| **value** | The value that to test. Non-integer values are truncated to the integer part and the integer part is tested. |

## Notes

* The function is equivalent to the expression `Trunc(value) % 2 = 1`

## Examples

### Examples with integer values

```
IsOdd(2)
```

Tests whether `2` is odd or not, and returns False.

```
IsOdd(3)
```

Tests whether `3` is odd or not, and returns True.

### Examples with non-integer values

```
IsOdd(2.3)
```

Tests whether the integer part of `2.3` is odd or not, and returns False.

```
IsOdd(Pi())
```

Tests whether the integer part of the mathematical constant π is odd or not, and returns True.

Updated 3 days ago

---

Related resources

* [IsEven](/docs/iseven)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + - [Function arguments](#function-arguments)
  + [Notes](#notes)
  + [Examples](#examples)
  + - [Examples with integer values](#examples-with-integer-values)
    - [Examples with non-integer values](#examples-with-non-integer-values)