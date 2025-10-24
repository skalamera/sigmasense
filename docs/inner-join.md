# Inner Join

# Inner Join

![Venn diagram of inner join between Current Worksheet and Joined Data, showing only the overlapping area highlighted](https://files.readme.io/9c226e4-Inner_Join.png)

Inner Join returns the rows that exist in both the current data and the joined data. Removes all rows that do not have data in both the current data and the joined data.

In the example below, we are using Inner Join to join a customer information table with an order information table. We are using Customer ID, shown in columns CUST ID, as the Join Key. Only the rows with data in both tables are preserved. The rows with data from Customer ID 2, 4 and 6 are removed from the resulting table because they only exist in one of the original tables.

![Example results of inner join showing rows removed if the Join Key value does not appear in both tables](https://files.readme.io/d25e996-IJ_table.png)

Different Joins handle multiple matching values differently.

| # of matches | Lookup | Inner join | Left outer join |
| --- | --- | --- | --- |
| 0 | NULL | Remove row | NULL |
| 1 | (value) | (value) | (value) |
| 2+ | \* | Add rows | Add rows |

Updated 3 days ago

---

[Lookup join](/docs/lookup-join)[Left Outer Join](/docs/left-outer-join)