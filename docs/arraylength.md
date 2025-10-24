# ArrayLength

# ArrayLength

The **ArrayLength** function returns the number of entries in a list.

## Syntax

```
ArrayLength(array)
```

The **ArrayLength** function has the following argument:

array
:   Required
:   Sigma counts the number of entries in this list
:   Must reference a list parameter, or a column that contains list values

## Example

A table contains a *Products Bought* column that has list values. You can use the **ArrayLength** function to count the number of products in the list of values.

```
ArrayLength([Products Bought])
```

![](https://files.readme.io/dd0face-Screenshot_2023-03-06_at_6.17.23_PM.png)

Updated 3 days ago

---

Related resources

* [ArrayContains](/docs/arraycontains)
* [ArrayDistinct](/docs/arraydistinct)
* [ArraySlice](/docs/arrayslice)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)