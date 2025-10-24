# RegexpMatch

# RegexpMatch

Returns True if a string matches a regular expression.

## Syntax

`RegexpMatch(string, pattern)`

string
:   Required
:   The string to search.

pattern
:   Required
:   The pattern to match within the subject.

> 📘
>
> ### When the regular expression you want to use contains a slash, quotation or other special character, you will need to use a backslash (\) to escape the special character. Regexp can vary based on the databases. Check the documentation of the database you use to find the correct syntax.

## Examples

**Example 1:**

Check if a name starts with an uppercase letter, followed by one or more lowercase letters, and then has another uppercase letter followed by one or more lowercase letters.

```
RegexpMatch([Name], "^[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+$")
```

![In a table with columns Name and RegexpMatch, the string Sigma Computing - capital S and C - returns True and the string sigma computing - lowercase s and c - returns false.](https://files.readme.io/b8c66e9-image.png)

**Example 2:**

Check if a string matches the social security pattern 'xxx-xx-xxxx'

```
RegexpMatch("123-45-6789", "[0-9]{3}-[0-9]{2}-[0-9]{4}")
```

Returns `True`.

**Example 3:**

Check if a string matches the phone number pattern '(xxx) xxx-xxxx'

```
RegexpMatch([Phone Number], "\\(\\d{3}\\) \\d{3}-\\d{4}")
```

![In a table with columns Phone Number and RegexpMatch Phone Number, (555) 555-5555 returns True, while 0123456789 returns False](https://files.readme.io/0390b43-image.png)

**Example 4:**

Check if an address starts with a numeric characters.

```
RegexpMatch([Address], "^[0-9]+")
```

![In a table with columns Address and RegexpMatch, three street addresses that start with numbers all return True](https://files.readme.io/078798b-3.png)

Updated 3 days ago

---

Related resources

* [Contains](/docs/contains)
* [RegexpExtract](/docs/regexpextract)
* [RegexpReplace](/docs/regexpreplace)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Examples](#examples)