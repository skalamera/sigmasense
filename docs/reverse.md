# Reverse

# Reverse

The **Reverse** function reverses the order of the characters in a string.

This function is useful for making text functions that normally work forwards from the beginning of a string, such as **Mid** or **Substring**, to instead work backwards from the end of the string.

## Usage

```
Reverse(text)
```

**text** (required)- Text or a column of text that you want to reverse.

## Example

```
Reverse("desserts")
```

* Returns “stressed”

```
[Extract Area Code (Failure)] = Mid([Phone Number], 5, 3)
[Extract Area Code (Success)] = Reverse(Mid(Reverse([Phone Number]), 6, 3))
```

![](https://files.readme.io/0d29469-mceclip0_1.png)

Updated 3 days ago

---

Related resources

* [Mid](/docs/mid)

* [Table of Contents](#)
* + [Usage](#usage)
  + [Example](#example)