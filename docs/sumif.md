# SumIf

# SumIf

The **SumIf** function adds the numbers in a column if all the conditions are true for that row.

> 📘
>
> ### This function must be used with aggregated data in a grouped table. For a detailed video walkthrough that uses this function, see [Building complex formulas with grouped data](https://www.sigmacomputing.com/resources/training-videos/table-grouping-and-functions#complex-formulas).

## Syntax

`SumIf(field, condition 1, [condition 2], ...)`

Function arguments:

* **field** (required) - The column of numbers to add together. Null values are skipped.
* **condition 1** (required) - The logical condition that returns a result that is either True or False. If the condition is True, the number on the corresponding row is added to the sum. Note: you can use [operators](/docs/operators-overview) in conditions.
* **condition 2 +** (optional) - Additional conditions can be added after the first condition.

> 📘
>
> In the case of multiple conditions the "AND" logical operator is used by default. In order to use an "OR" operator the conditions should be encapsulated in a single condition chained by an explicit "OR."

---

## Examples

```
SumIf([Sales], [State] = "TX" )
```

Returns the sum values in the *Sales* column if the *State* column value is `TX`.

```
SumIf([Sales], [State] = "TX" OR [State] = "CA")
```

Returns the sum of values in the *Sales* column if the *State* column value is `TX` or `CA`.

```
SumIf([Sales], [State] = "TX", [CustomerID] = "1234" )
```

Returns the sum of values in the *Sales* column if the *State* column value is `TX` and the *CustomID* column value is `1234`.

```
SumIf([Sales], [State] = [list-control-state])
```

Returns the sum of values in the *Sales* column if the *State* column value matches the value selected in the *list-control-state* control element.

Updated 3 days ago

---

Related resources

* [Sum](/docs/sum)
* [If](/docs/if)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Examples](#examples)