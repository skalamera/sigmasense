# RegexpReplace

# RegexpReplace

The **RegexpReplace** function searches a string for a pattern and replaces all matches with the replacement string. If no matches are found, the original string is returned.

**RegExReplace** can be useful for complex text pattern matching, or matching multiple patterns at once. For one-to-one text replacements, the **[Replace](/docs/replace)** function may also be useful.

## Syntax

```
RegexpReplace(string, pattern, replacement)
```

Function arguments:

* **string** (required): The string to search.
* **pattern** (required): The pattern to extract with.
* **replacement** (required): String to replace the sought pattern.

> 📘
>
> When your regular expression statement contains a slash, quotation or other special character, use a backslash () to escape the special character. `Regexp` can vary by database. Check your database's documentation to find the correct syntax.

## Examples

**Example 1:**

```
RegexpReplace([Product Name], "(\\d+) (\\d+mm)", "\\1-\\2")
```

Replaces every space between digits and digits preceding "mm" with a dash to indicate the range of camera lenses.

![In a table with columns Product Name and RegexpReplace, any measurement range without a dash between the two ends has one added](https://files.readme.io/94d1c88-1.png)

**Example 2:**

```
RegexpReplace([Phone Number], "(\\d{3})(\\d{3})(\\d{4})", "(\\1) \\2-\\3")
```

Transforms a phone number to (xxx) xxx-xxxx formatting.

![In a table with columns Phone Number and RegexpReplace Phone Number, unformatted numbers are broken apart with the area code in parentheses and a dash between the 6th and 7th characters](https://files.readme.io/e6a3321-image.png)

**Example 3:**

```
RegexpReplace([City], "^(.*?),", "San Francisco,")
```

Replaces every character before the comma with the city in proper form.

![In a table with columns City and RegexpReplace, capitalization is corrected such that names have only their first letters capitalized](https://files.readme.io/4ae7a52-3.png)

**Example 4:**

```
RegexpReplace([Team], "[^a-zA-Z0-9\\s]", "")
```

Removes all punctuation marks in a string.

![In a table with columns Team and RegexpReplace, all punctuation is removed](https://files.readme.io/6fdae7b-4.png)

**Example 5:**

```
RegexpReplace([Text], "\\/", "&")
```

Replaces the slash with "&".

![In a table with columns Text and RegexpReplace, all forward slashes are replaced with an ampersand](https://files.readme.io/ba5d1e6-5.png)

Updated 3 days ago

---

Related resources

* [RegexpMatch](/docs/regexpmatch)
* [RegexpExtract](/docs/regexpextract)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Examples](#examples)