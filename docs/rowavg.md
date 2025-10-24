# RowAvg

# RowAvg

Returns the average value of the input numbers.

Unlike [Avg](/docs/avg), which calculates the aggregate average of a group of values in a column, RowAvg can be used to calculate the average of column values across individual rows.

## Usage

```
RowAvg(number, number, ...)
```

**number** [required] One of a list of numbers to be averaged

## Examples

### Example #1

```
RowAvg(2, 4, 12)
```

Returns 6.

### Example #2

```
RowAvg([Population 2000], [Population 2010])
```

Returns the average of the row values for each row in the [Population 2020] and [Population 2010] columns.

![](https://files.readme.io/b43823e-888.png)

Updated 3 days ago

---

Related resources

* [Avg](/docs/avg)

* [Table of Contents](#)
* + [Usage](#usage)
  + [Examples](#examples)
  + - [Example #1](#example-1)
    - [Example #2](#example-2)