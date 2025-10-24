# If

# If

The **If** function returns Value 1 for every row where the first condition is met. If more than one condition is supplied, the second condition is evaluated and returns Value 2 for every row where the second condition is met. If all conditions are False, then the Else value is applied for every row that does not belong to the preceding conditions.

## Syntax

```
If(condition 1, value 1, [condition 2], [value 2],..., [else])
```

Function arguments:

* **condition 1** (required) Logical condition that returns a result that is either True or False.
* **value 1** (required) The value to be returned if its preceding condition is True.
* **condition 2+, value 2+** (optional) Several If/Then pairs can be listed in a single function. Every supplied condition must have a corresponding value.
* **else** (optional) The value to be returned if no conditionals evaluate to True.

> 📘
>
> If an **Else** argument is not specified, a Null result is returned by default when no conditions are met.

> 📘
>
> You can use [operators](/docs/operators-overview) in conditions.

---

## Example

```
If([size] < 3, "small", [size] < 6, "medium", "large")
```

* Assign “small” to sizes less than 3, “medium” to sizes less than 6, and “large” to all other sizes.

```
If([revenue] - [cost] > 0, "profit", "loss")
```

* Categorize a record as a profit or a loss based on revenue and cost.

```
If([Product Family] = "Cameras & Camcorders" OR [Product Family] = "Camera Accessories", "Photography")
```

* Categorize records in the product family with an overarching product type using the "OR" [operator](/docs/operators-overview).

```
If( 
Weekday([Today]) = 2 AND DateDiff("day", [Date], DateAdd("day", -3, [Today])) = 0, True, 
Weekday([Today]) = 1 AND DateDiff("day", [Date], DateAdd("day", -2, [Today])) = 0, True, 
Weekday([Today]) > 2 AND DateDiff("day", [Date], DateAdd("day", -1, [Today])) = 0, True, 
False)
```

* Assign True to rows where a date belongs to the previous weekday based on Today.

  > 📘
  > + Weekday(Sunday) is 1, Weekday(Saturday) is 7. For more information on the date functions used in this example, see Sigma's [Date Functions Overview](/docs/date-functions-overview)[.](/docs/date-functions-overview)

  If Today is Monday, then last Friday's data. If Today is Sunday, then return last Friday's data. If Today is either Tuesday/Wednesday/Thursday/Friday/Saturday, then return yesterday's data.

```
If([Number] > 0, If(Mod([Number], 2) = 0, "Even", "Odd"), "Not Positive")
```

* Check if a number is even or odd, but only if it is positive, from the column `[Number]`. This is a nested **If** statement, meaning the **If** statement in the second argument will only ever be evaluated for the outcome `"Even"` or `"Odd"` if the first condition of the outer **If** statement - `[Number] > 0` - is met.
  + For a row where `[Number]` has a value 7, this returns `Odd`.
  + For a row where `[Number]` has a value 2, this returns `Even`.
  + For a row where `[Number]` has a value -1, this returns `Not Positive`.

Updated 3 days ago

---

Related resources

* [SumIf](/docs/sumif)
* [CountIf](/docs/countif)
* [Switch](/docs/switch)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)