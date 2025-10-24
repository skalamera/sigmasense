# LPad

# LPad

Prepends a pattern to or truncates a string to the desired length.

## Usage

```
LPad(text, length, [fill])
```

**text** (required)- The string, or column of strings, to pad or trim to the desired length.

**length** (required)- The length of the returned string.

**fill** (optional)- The character with which to pad the text. Defaults to space.

## Example

```
LPad([Product Family], 4)
```

* Returns the Product Family column trimmed to a length of 4

![](https://files.readme.io/17b2570-mceclip0_2.png)

```
LPad("sigma", 10, "-")
```

* Returns "-----sigma"

```
LPad("Sigma Computing", 10)
```

* Returns "Sigma Comp"

Updated 3 days ago

---

Related resources

* [RPad](/docs/rpad)

* [Table of Contents](#)
* + [Usage](#usage)
  + [Example](#example)