# Lookup join

# Lookup join

This document is about Sigma datasets. For Sigma Workbooks, see the [Lookup](/docs/lookup) function and how to [Add Columns through Lookup](/docs/add-columns-through-lookup).

> 🚩
>
> ### All elements involved in a lookup join must be on the same data connection.

![Venn diagram of Current Worksheet and Joined Data, showing the entire Current Worksheet circle highlighted](https://files.readme.io/945826b-Lookup.png)

Lookup returns all of the rows in your current data and all of matching data from the rows in the joined data without adding any rows to the current data. When there is more than one match, Sigma shows a \* to indicate that the joined data has more than one row with matching data. The Lookup join functions similarly to the VLOOKUP formula in Excel.

In the example below, we are using Lookup to join a customer information table with an order information table. We are using Customer ID, shown in columns CUST ID, as the Join Key. There is more than one order from Customer ID 1 in the order table, so Sigma displays a \* in place of pulling in any information. This preserves the number of rows in the Customer Information Table.

![Example results of join when one source contains multiple rows that match the Join Key](https://files.readme.io/f0a7425-Lookup_table.png)

Different Joins handle multiple matching values differently.

| # of matches | Lookup | Inner join | Left outer join |
| --- | --- | --- | --- |
| 0 | NULL | Remove row | NULL |
| 1 | (value) | (value) | (value) |
| 2+ | \* | Add rows | Add rows |

Updated 3 days ago

---

[Join types](/docs/join-types)[Inner Join](/docs/inner-join)