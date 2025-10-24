# MaxIf

# MaxIf

The **MaxIf** function finds the maximum value for a column or group if the conditions are true.

## Syntax

`MaxIf(field, condition)`

Function arguments:

* **field** (required) - The column to be searched. Can be of type Number, Date, and String.
* **condition** (required) - The condition to test. If the condition is True, then the row will be factored into the aggregate.  You can use [operators](/docs/operators-overview) in conditions.

> 📘
>
> The maximum of strings is determined by sort order, which is affected by your database settings. Sort order is most often blank spaces > special characters > numbers > uppercase letters > lowercase letters.
>
> For numbers, preceding and trailing zeroes most often have no effect on sort order.

## Examples

```
MaxIf([Invoice Date], [State] = "TX")
```

* Finds the greatest Invoice Date for all entries where the State indicated is Texas.

```
MaxIf([Sales], [Region] = "East" AND [Status] = "Complete")
```

* Finds the maximum Sale value for entries in the "East" Region that are marked as "Complete".

Updated 3 days ago

---

Related resources

* [Max](/docs/max)
* [AvgIf](/docs/avgif)
* [MinIf](/docs/minif)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Examples](#examples)