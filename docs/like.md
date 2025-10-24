# Like

# Like

Returns true if the string value matches the case-sensitive pattern.

## Usage

```
Like(string, pattern)
```

**string** (required) The text string that is being searched.

**pattern** (required) The search pattern.  
An '\_' matches any character.  
A '%' matches any sequence of zero or more characters.

### Examples

```
Like("Piano", "P_ano") = true
```

```
Like("Boat", "G_te") = false
```

**Try it in Sigma Sample Data**

In Sigma's sample baby name data, the following formula returns *true* for values in the [Name] column that include “em”, like “Gemma” and “Jeremy”.  
The Like function is case-sensitive, so string values such as "Emma" returns false.

```
Like([Name], “%em%”)
```

![](https://files.readme.io/62aa331-mceclip0_1.png)

Updated 3 days ago

---

Related resources

* [ILike](/docs/ilike)
* [RegexpMatch](/docs/regexpmatch)
* [Contains](/docs/contains)

* [Table of Contents](#)
* + [Usage](#usage)
  + - [Examples](#examples)