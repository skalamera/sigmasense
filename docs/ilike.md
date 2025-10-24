# ILike

# ILike

Returns true if the string value matches the case-insensitive pattern.

## Usage

`ILike(string, pattern)`

**string** (required) The text string that is being searched.

**pattern** (required) The search pattern.  
An '\_' matches any character.  
A '%' matches any sequence of zero or more characters.

## Examples

```
ILike("Piano", "P_ano") = true
```

```
ILike("Piano", "p_ANO") = true
```

```
ILike("Piano", "p%o") = true
```

**Try it in Sigma Sample Data**

In Sigma's sample baby name data, the following formula returns *true* for values in the `[Name]` column that include “em”, like "Emma", “Gemma” and “Jeremy”.

```
ILike([Name], “%em%”)
```

![](https://files.readme.io/9dcef1f-mceclip0.png)

Updated 3 days ago

---

Related resources

* [Like](/docs/like)
* [RegexpMatch](/docs/regexpmatch)
* [Contains](/docs/contains)

* [Table of Contents](#)
* + [Usage](#usage)
  + [Examples](#examples)