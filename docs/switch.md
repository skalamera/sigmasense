# Switch

# Switch

The **Switch** function returns the result corresponding to the first matching value. If the **case** argument evaluates to True, then the corresponding result is returned, otherwise the **else** argument is returned.

## Syntax

```
Switch(value, case 1, result 1, [case 2], [result 2], ... , [else])
```

* **value** (required) The value to test.
* **case 1** (required): The case to test the value against.
* **result 1** (required): The result to be returned if its preceding case matches the input value.
* **case 2+, result 2+** (optional): Several pairs can be listed in a single function. Every supplied case must have a corresponding result.
* **else** (optional): The result to be returned if no cases match the value.

> 📘
>
> If no **else** condition is supplied, a Null result is returned when no cases are met.
>
> The **result(s)** argument must be of the same data type. #1 below will not work because the function is asked to return a string OR a number, whereas #2 will work because both outputs are strings.

1. `Switch([Number Column], 1, [String Value], 2, [Numeric Value])`
2. `Switch([Number Column], 1, [String Value], 2, [String Value])`

## Example

```
Switch(1, 0, "None", 1, "One", "Many")
```

* Returns "One"

```
Switch(2, 0, "None", 1, "One", "Many")
```

* Returns "Many"

A table contains Sales Revenue data that is grouped by a *Switch* column (i.e., dynamic dimension field) and *Month*.

```
Switch([dimension-param], "Product Family", [Product Family], "Product Type", [Product Type])
```

* With a single-select list parameter whose control id is `[dimension-param]`, you can can use the Switch function to return monthly Sales Revenue data by *Product Family* or *Product Type.*

![](https://files.readme.io/ca53b75-1.png)  
![](https://files.readme.io/f09d02a-2.png)

Updated 3 days ago

---

Related resources

* [If](/docs/if)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)