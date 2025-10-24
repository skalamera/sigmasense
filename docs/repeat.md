# Repeat

# Repeat

The **Repeat** function returns the results of repeating a string a specified number of times.

**Repeat** is one of the [Text functions](/docs/type-functions-overview) supported by Sigma.

## Syntax

```
Repeat(string, number)
```

Repeat has the following arguments:

string
:   Required
:   The string that the function repeats

number
:   Required
:   The number of times the string repeats.
:   The zero, `0`, and negative values both return a `NULL` string.

## Examples

TextTextTextTextText

```
Repeat([Product Type],0)
```

```
Repeat([Product Type],1)
```

```
Repeat([Product Type],2)
```

```
Repeat([Product Type],3)
```

```
Repeat([Product Type],-1)
```

The **Repeat** function returns the following values for the **Product Type** column:

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/img/function-repeat-example.png)

Updated 3 days ago

---

Related resources

* [Contains](/docs/contains)
* [Substring](/docs/substring)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Examples](#examples)