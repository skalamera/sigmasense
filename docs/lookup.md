# Lookup

# Lookup

The **Lookup** function finds matching data inside a workbook data element, either in the same table, or in an external table.

To understand how to apply the Lookup function without directly using the formula bar, see [Add columns through Lookup](/docs/add-columns-through-lookup).

All elements must be on the same data connection.

## Syntax

```
Lookup(formula, local key 1, external key 1, [local key 2], [external key 2], ...)
```

This function has the following arguments:

formula
:   Required
:   The formula to compute (or the target column to reference) for the row in the target element.

local key 1
:   Required
:   The column to use as a join key in the local data element.

external key 1
:   Required
:   The column to use as a join key in the target data element.

local key 2
:   Optional
:   The additional column to use as a join key in the local data element.

external key 2
:   Optional
:   The additional column to use as a join key in the target data element.

## Notes

* The **Lookup** function can only reference one external data element at a time. If external keys from two different elements are referenced, **Lookup** will return the error `Rollup cannot reference more than one external relation`. To help avoid this error and more easily identify the source of external keys, Sigma recommends giving unique names to data elements.

## Examples

### Lookup with one external key

```
Lookup([Customers/Cust Name], [Cust Key], [Customers/Cust Key])
```

Data is inserted into the *Sales* table’s **[Calc]** column from the *Customer* table’s **[Cust Name]** column.

These two tables are joined using a single column (join key) from each table. In this case, both join keys are named **[Cust Key]**.

The function’s *formula* parameter directly references a column in the joined table.

> 📘
>
> ### In formulas, reference columns from other tables with the **[table name/]** prefix (e.g. **[Customers/Cust Name]**).

![A user enters the provided example formula in the Sigma UI, demonstrating the output over several records in a table.](https://files.readme.io/458c4704f0b97a6e643e126db3276fa88603ebe9bbdaf4048af05efd854aa255-Lookup_Screenshot_1_Update.png)

### Lookup with two external keys

```
Lookup([Customers/Zip Code], [Cust Name], [Customers/Name], [Cust Key], [Customers/Cust Key])
```

Data is inserted into the *Ordered Items* table’s **[Calc]** column from *Customer* table’s **[Zip Code]** column.

The function’s *formula* parameter directly references a column in the joined *Customers* table.

These two tables are joined using two sets of join keys:

* *Order Items’* **[Cust Name]** column is joined with *Customer*’s **[Name]** column;
* *Order Items’* **[Cust Key]** column is joined with *Customer*’s **[Cust Key]** column

![A user enters the provided example formula in the Sigma UI, demonstrating the output over several records in a table.](https://files.readme.io/e3bf0f22cc6da83de740b117076cf60b5f5664e64b385332b71abc16d0cb97f5-Lookup_Screenshot_2_Update.png)

### Lookup with an aggregate result

```
Lookup(Sum([Sales Amounts/Sales Amount]), [Order Number], [Sales Amounts/Order Number])
```

Data is inserted into the *Orders* table’s **[Calc]** column from *Sales Amount* table’s **[Sales Amount]** column.

The function’s *formula* parameter uses the Sum function to aggregate values from the *Sales Amount* table’s **[Sales Amount]** column. For each order in *Orders*, the **Lookup** function returns the sum of all **[Sales Amount]** values with that **[Order Number]**.

These two tables are joined using a single set of join keys: *Orders’* **[Order Number]** column is joined with *Sales Amounts’* **[Order Number]** column.

![A user enters the provided example formula in the Sigma UI, demonstrating the output over several records in a table.](https://files.readme.io/2270c8da618300ce7c51ef96b6f234b201c343d98a91fed8fc904aff65cd1c6d-Lookup_Screenshot_3_Update.png)

Updated 3 days ago

---

Related resources

* [Rollup](/docs/rollup)
* [Add columns through Lookup](/docs/add-columns-through-lookup)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Notes](#notes)
  + [Examples](#examples)
  + - [Lookup with one external key](#lookup-with-one-external-key)
    - [Lookup with two external keys](#lookup-with-two-external-keys)
    - [Lookup with an aggregate result](#lookup-with-an-aggregate-result)