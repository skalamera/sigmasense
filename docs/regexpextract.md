# RegexpExtract

# RegexpExtract

The **RegexpExtract** function returns the substring that matches a regular expression within a string.

If the regular expression contains a [capture group](https://docs.oracle.com/javase/tutorial/essential/regex/groups.html#:~:text=Capturing%20groups%20are%20a%20way,o%22%20and%20%22g%22%20.) (`(...)`) and there are one or more matches for that capture group, Sigma returns the first capture group across all matches. Otherwise, Sigma returns the full regular expression.

## Usage

```
RegexpExtract(string, substring, [position])
```

Function arguments:

* **string** (required): The string to search
* **substring** (required): The substring to extract with.
* **position** (optional): The index of the match to return.

> 📘
>
> ### When the regular expression contains a slash, quotation or other special character, use a backslash (\) to escape the special character. Regexp can vary based on the database. Check the documentation of the database you use to find the correct syntax.

## Examples

**Example 1:**

```
RegexpExtract([Address], "[0-9]+")
```

Extracts the first match of numeric characters in the string. No position is specified so position defaults to 1.

![In a table with columns Address and RegexpExtract, the street address is extracted from the address. 345 South Court 10016 becomes 345](https://files.readme.io/da9baf7-1.png)

**Example 2:**

```
RegexpExtract([Address], "[0-9]+", 2)
```

Extracts the second match of numeric characters in the string.

![In a table with columns Address and RegexpExtract, the zip code is extracted. 345 South Court 10016 becomes 10016](https://files.readme.io/17d232e-2.png)

**Example 3:**

```
RegexpExtract([Address], "\\s*([a-zA-Z]+)", 2)
```

Extracts the second match of alphabetical characters in the string.

![In a table with columns Address and RegexpExtract, the zip code is extracted. 345 South Court becomes Court](https://files.readme.io/77b7734-3.png)

**Example 4:**

```
RegexpExtract([Date], "(\\d{2})", 2)
```

Extracts the second match, day of date, of the 2-digit character group in the date.

![In a table with columns Date and RegexpExtract, the day is extracted. 01.05.2022 becomes 05](https://files.readme.io/07f6765-4.png)

Updated 3 days ago

---

Related resources

* [RegexpMatch](/docs/regexpmatch)
* [RegexpReplace](/docs/regexpreplace)

* [Table of Contents](#)
* + [Usage](#usage)
  + [Examples](#examples)