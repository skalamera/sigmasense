# Coalesce

# Coalesce

The **Coalesce** function returns the value of the first argument that is not `Null`. This function is often applied to one or more columns of data to check for `Null` values and assign the placeholder value in replacement of `Null`.

> 📘
>
> **Coalesce** is not an aggregate function and is not to be confused with [FirstNonNull](/docs/firstnonnull), which returns the row of a column with the first non-Null value.

## Syntax

```
Coalesce(argument 1, ...)
```

**argument 1** (required)- The number, date, string, column, or function to be evaluated.

**argument 2+** (optional)- The additional arguments to be evaluated.

> 📘
>
> Arguments must all be of the same data type. If you need to evaluate different types of arguments, you can use [Text](/docs/text-1) to force the **Coalesce** function to read the input as a string.

> 📘
>
> If all arguments to be evaluated are `Null`, `Null`is returned.

## Example

```
Coalesce(Null, 1/0, 1/1, 1/2) = 1
```

* Returns the third argument as it is the first non-Null value.

```
Coalesce([Sales], 0)
```

* Converts all the Null values in *Sales* to 0.

```
Coalesce([Profit]/[Sales], 0)
```

* Return profit per sale when *Sales* >0; return 0 if there are no sales. This avoids creating unintentional `Null` values when the formula encounters situations that divide by 0.

If you want a report that lists Product Types for all purchase transactions, you can use the **Coalesce** function to search multiple columns for the first non-Null value per row.

```
Coalesce([Product Type], [Product Family], [Sku Number])
```

* Return *Product Type* if it exists; return *Product Family* if there is no Product Type. If both *Product Type* and *Product Family* do not exist, return *SKU Number.*

![](https://files.readme.io/9aa504b-ll.png)

Alternatively, assume the role of a business owner who is updating pricing to reflect the seasonal discount for one of their product types. You can use the **Coalesce** function on a non-constant argument to assign a placeholder value if no discount exists for the product type.

```
Coalesce([Discounted Price], [Sticker Price])
```

* Return *Discounted Price* if discount data exists, otherwise return *Sticker Price.*

![](https://files.readme.io/7ef8aef-Screen_Shot_2023-04-16_at_6.54.23_PM.png)

Updated 3 days ago

---

Related resources

* [If](/docs/if)
* [IsNull](/docs/isnull)
* [Zn](/docs/zn)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)