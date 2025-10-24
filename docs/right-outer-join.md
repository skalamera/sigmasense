# Right Outer Join

# Right Outer Join

![Venn diagram of right outer join between Current Worksheet and Joined Data, showing entire Joined Data circle highlighted](https://files.readme.io/ec2f9e1-Right_Outer_Join.png)

Right Outer Join returns all of the rows from the joined data and the data from the matching rows in the current data, adding rows when there is more than one match. When the current data has more than one row that matches to joined data, all of the matches rows are retained.

In the example below, we are using Right Join to join a customer information table with an order information table. We are using Customer ID, shown in columns CUST ID, as the Join Key. All of the data from the joined order table is preserved. All data from the customer information table that cannot be joined to the order table is removed.

![Example result set of right outer join, showing rows removed that did not have values in Join Key field in the customer information table](https://files.readme.io/0bcef43-ROJ_table.png)

Rows that show customer information for Customer ID 2 and 4 are removed because they do not have corresponding data in the order information table. Order information for Customer ID 6 is added to the table because it exists in the order table, even though it does not exist in the customer information table.

Updated 3 days ago

---

[Left Outer Join](/docs/left-outer-join)[Full Outer Join](/docs/full-outer-join)