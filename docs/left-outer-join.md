# Left Outer Join

# Left Outer Join

![Venn diagram of Current Worksheet and Joined Data, showing the entire Current Worksheet circle highlighted](https://files.readme.io/c89c21a-Left_Outer_Join.png)

Left Outer Join returns all of the rows in the current data and all the data from the matching rows in the joined data, adding rows when there is more than one match. This can result in an expanded row count.

In the example below, we are using Left Join to join a customer information table with an order information table. We are using Customer ID, shown in columns CUST ID, as the Join Key. There is more than one order from Customer ID 1 in the order table, so an additional row is added to the table to accommodate the information. There are now two rows in the table that hold Customer 1’s data.

![Example results of left outer join when one source contains multiple rows that match the Join Key, resulting in an added row](https://files.readme.io/8c7d132-LOJ_table.png)

Different Joins handle multiple matching values differently.

| # of matches | Lookup | Inner join | Left outer join |
| --- | --- | --- | --- |
| 0 | NULL | Remove row | NULL |
| 1 | (value) | (value) | (value) |
| 2+ | \* | Add rows | Add rows |

Updated 3 days ago

---

[Inner Join](/docs/inner-join)[Right Outer Join](/docs/right-outer-join)