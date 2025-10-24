# Full Outer Join

# Full Outer Join

![Venn diagram of Current Worksheet and Joined Data, showing entire area of Venn Diagram highlighted](https://files.readme.io/f43af76-Full_Outer_Join.png)

A Full Outer Join returns all of the rows from the current data and all of the rows in the joined data, making matches where possible.

In the example below, we are using Outer Join to join a customer information table with an order information table. We are using [Cust ID], shown in columns [CUST ID], as the Join Key. All of the rows from both tables are added to the joined table. When possible, the rows are joined. When that isn’t possible, null values are added to the row.

‍![Example result set of full outer join, showing all rows from both tables added to joined table](https://files.readme.io/e122b43-FOJ_table.png)

An additional row of Customer 1 data is added to accommodate multiple orders in the joined order table. Customer 2 and Customer 4 have NULL values for order data, as there was no data for them in the order table. Customer 6 has NULL values for First and Last as the original data had no information for Customer 6.

Updated 3 days ago

---

[Right Outer Join](/docs/right-outer-join)[Join data in datasets](/docs/join-data-in-datasets)