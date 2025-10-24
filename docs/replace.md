# Replace

# Replace

The **Replace** function searches through a input string for a substring and replaces every instance of it with a replacement string.

This is useful for standardizing alternative abbreviations and names, fixing common misspellings, changing one delimiter for another, and selectively removing particular substrings. For more complex pattern matching, or to match multiple patterns at once, the **[RegExReplace](/docs/regexreplace)** may be useful.

## Usage

```
Replace(string, substring, replacement)
```

**string** (required)- String to be searched and modified.

**substring** (required)- Substring to be found and replaced.

**replacement** (required)- String to replace the substring.

## Examples

```
Replace("SF County","SF","San Francisco")
```

* Returns: "San Francisco County"

`Replace("File Name"," ","")`

* Returns: "FileName"
* Using an empty string as your replacement string allows you to remove every instance of the substring

```
Replace(Replace([Order Manual], "Cold Slaw", "Cole Slaw"), "Ice Tea", "Iced Tea")
```

* When applied to the [Order Replaced] column, returns:

![](https://files.readme.io/1d204b7-mceclip0.png)

Updated 3 days ago

---

Related resources

* [Find](/docs/find)

* [Table of Contents](#)
* + [Usage](#usage)
  + [Examples](#examples)