# NullIf

# NullIf

The **NullIf** function returns `Null` if the first argument is equal to the second. Otherwise, it returns the first argument.

To return the value of the first argument that is not null, see [Coalesce](/docs/coalesce).

## Syntax

```
NullIf(value1, value2)
```

### Function arguments

|  |  |
| --- | --- |
| **value1** | The value to return if both values are not equal. |
| **value2** | The value to compare to the first value. Must be the same data type as `value1`. |

## Notes

* `value1` and `value2` accept any data type.
* **NullIf** returns an error if `value1` and `value2` are not the same data type.

## Examples

```
NullIf(0, 1)
```

Tests `0` and `1` are equal. Since they are not, returns `0`.

```
NullIf(0, 0)
```

Tests `0` and `0` are equal. Since they are, returns `Null`.

```
NullIf("Sigma", "sigma")
```

Tests whether `"Sigma"` and `"sigma"` are equal. Since they are not, returns `"Sigma"`.

```
NullIf("3.1416", Text(3.1416))
```

Tests whether `"3.1416"` and the result of `Text(3.1416)` are equal. Since they are, returns `Null`.

Updated 3 days ago

---

Related resources

* [Coalesce](/docs/coalesce)
* [Zn](/docs/zn)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + - [Function arguments](#function-arguments)
  + [Notes](#notes)
  + [Examples](#examples)