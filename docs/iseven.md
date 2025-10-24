# IsEven

# IsEven

The **IsEven** function returns True if the integer part of a number is even and returns False is it is odd.

To return True for odd values and False for even, see [IsOdd](/docs/isodd).

## Syntax

```
IsEven(value)
```

### Function arguments

|  |  |
| --- | --- |
| **value** | The value to test. Non-integer values are truncated and the integer part is tested. |

## Notes

* The function is equivalent to the expression `Trunc(value) % 2 = 0`

## Examples

### Examples with integer values

```
IsEven(2)
```

Tests whether `2` is even or not, and returns True.

```
IsEven(3)
```

Tests whether `3` is even or not, and returns False.

### Examples with non-integer values

```
IsEven(2.3)
```

Tests whether the integer part of `2.3` is even or not, and returns True.

```
IsEven(Pi())
```

Tests whether the integer part of the mathematical constant π is even or not, and returns False.

Updated 3 days ago

---

Related resources

* [IsOdd](/docs/isodd)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + - [Function arguments](#function-arguments)
  + [Notes](#notes)
  + [Examples](#examples)
  + - [Examples with integer values](#examples-with-integer-values)
    - [Examples with non-integer values](#examples-with-non-integer-values)