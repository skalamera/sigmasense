# EndsWith

# EndsWith

Returns True if a string ends with a substring.

## Usage

`EndsWith(string, substring)`

**string** (required) The text to search.

**substring** (required) The text to search with.

> 📘
>
> EndsWith is case-sensitive. To create a search that is not case-sensitive, combine EndsWith with [Lower](/docs/lower).

## Example

`EndsWith("Jane Doe", "oe")`

* Returns TRUE

`EndsWith(Lower("JANE DOE"), "oe")`

* Returns TRUE

Updated 3 days ago

---

Related resources

* [Contains](/docs/contains)
* [Find](/docs/find)
* [StartsWith](/docs/startswith)

* [Table of Contents](#)
* + [Usage](#usage)
  + [Example](#example)