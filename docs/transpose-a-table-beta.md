# Transpose a table

# Transpose a table

Sigma supports transposing a table from rows to columns, or columns to rows. Transposing data can be useful for data analysis, as it allows you to pivot or unpivot your data according to your individual use case.

For example, the table below shows a record of parking lot entries and exits, with each row showing the entry and exit date for each car.

![](https://files.readme.io/5a2bfacbe27d0f3c2068919eac137242c52fdb6552bfa07cb4cb2f2f80bfe317-carexample.png)

To shape the data such that all the date values are in a single row, a row to column transpose can be performed, resulting in the table transforming into something like this:

![](https://files.readme.io/d7193a2cc515a058a135b032b07360038eb6f1c9330ebf2642682cb43c9fc576-cartransposed.png)

This can be especially useful for visualizations, as you may want to reshape your data to suit specific chart types –such as needing date values oriented in a single column for line charts).

This document explains how to transpose your data from [rows to columns](/docs/transpose-a-table-beta#transpose-row-to-columns), or [columns to rows](/docs/transpose-a-table-beta#transpose-columns-to-rows), and includes examples of each.

## System and user requirements

You must be the workbook owner or be granted **Can explore** or **Can edit** access to the workbook.

## Limitations

The following is not supported:

* Transposing input tables.
* Transposing calculated columns. If you transpose a table with calculated columns, any existing filtering, sorting or grouping is not reflected in the transposed output. This is because transposing is performed on the data from your data platform, not the data element in your workbook.

In addition, the following limitation applies:

* When transposing rows to columns, a limit of 200 unique row values can be transposed from a single column, resulting in a maximum of 200 columns. There is no limit when transposing columns to rows.

## Transpose row to columns

You can transpose table rows to columns to use the values of a given column as the column headers for a table. For example, transpose the rows of a *Store Region* column to use the values of the *Store Region* column (East, Midwest, South, and so on) as column headers and view aggregate values for those region values.

To transpose rows to columns:

1. From your desired table, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**.
2. From **Element source**, select **Transpose**.
3. In the **Transpose Table** modal, select **Row to column**.
4. Select your desired **Column to transpose**. When transposed, the data in this column is rearranged such that each unique value becomes a new column.

> ❗️
>
> ### If your selected column has more than 200 unique values, resulting in more than 200 columns in a transposed table, an error appears.

5. Select your **Value column**. This is the column that is used for the calculation that you select in **Aggregate**.
6. Select your preferred **Aggregate** method. The aggregation methods shown vary based on the data type of the selected **Value column**.
7. Select the checkboxes next to your desired **Output columns**. These are the columns you want included in the transposed output, and do not impact any other calculations in the transpose. A preview of your transposed table is available under **Output preview**.
   * The order you select the columns in is the order they appear in the table, from left to right.
   * Any remaining source columns from the original source table are used to group the transpose. For an example of these groupings, see [Example: Counting games won and lost](#example-counting-games-won-and-lost). For more information on groupings in general, see [Group columns in a table in Create and manage tables](/docs/create-and-manage-tables#group-columns-in-a-table).
8. Select **Submit**.

### Example: Counting games won and lost

For example, you might have a table of baseball games that your team has played at home, with one row of data for each game played and columns for opponent, result, and division rank after the game.

If you want to calculate the total games that your team has won or lost at each division rank, you can transpose the table by division rank.

![](https://files.readme.io/54ace8ffa9210d93d5ee36eb0e499a42879d3a6d8eaaa17eec7c20f481f91883-transpose1.png)

To obtain this count:

1. Select **Row to column** transpose.
2. To set **L** (Loss) and **W** (Win) as the column headers for the transposed table, select **Win Loss** as the **Column to transpose**. The **L** (Loss) and **W** (Win) values appear as new columns in the transposed table.
3. To calculate the number of wins or losses for a given opponent, select Opponent as the **Value Column**.
4. To calculate the number of non-null and non-empty values, select **Count** for the **Aggregate**.
5. Select **Division Rank**, **L** and **W** as **Output columns**. The table output is automatically grouped by **Division Rank**, as that is the only remaining source column. This sums the total **Count** of wins and losses at each division rank.

You might want the output to be additionally grouped by another column, like **Start Time**. To do this:

1. In **Output columns**, select **Start Time** (keeping the existing selections of **Division Rank**, **L** and **W**). For each game start time, the transpose shows the number of wins and losses, at each division rank. Note that not all start times show all four division ranks, as no wins and losses were recorded at those times.
2. [optional] To make the output easier to understand, you can also sort the **Start Time** column to ascending, so that the data is sorted from earliest to latest game in the day. In the **Start Time** column, right click or click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu, then select **Sort ascending**. Once sorted, the output will look something like:

![](https://files.readme.io/950116fb0cf84de188cdff2f32b9ebff80e898b3cde615dee8148973423a4def-sortedtranspose.png)

You might also want to find out the number of unique opponents that your team has won or lost against at each division rank. To obtain this:

* Change the **Aggregate** method to **CountDistinct**. **CountDistinct** provides the number of unique values within the **Opponent** column. The values represent the number of different opponents the team has beaten at each division rank. Your output will look something like:

![](https://files.readme.io/ac42dd3dc777fadc51f90e37a2622a8f1a5a9510d17c2ca5f3d5f3baaa076395-countdistinct.png)

## Transpose columns to rows

1. From your desired table, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**.
2. From **Element source**, select **Transpose**.
3. In the **Transpose Table** modal, select **Column to row**.
4. Select your **Columns to merge**.
5. Enter a **Column label for merged columns**. This label is the column header of the new column that contains the previous header values of the merged columns.
6. Enter a **Column label for values**. This is your column headers for the new column containing the values of your merged columns.
7. Select the checkboxes next to your desired **Output columns**. These are the columns you want included in the transposed output, and do not impact any other calculations in the transpose. A preview of your transposed table is available under **Output preview**.
8. Select **Submit**.

### Example: Merging audit log event times

For example, you might have a table of audit log events. Each row details one unique table sync, with information like connector ID, table name, write to table start/end, sync start/end, and unique table sync key.

If you want a table with rows for every table event and its timestamp, you can transpose the table and merge these columns. To obtain this new table:

![](https://files.readme.io/6a2f4de6ceef391b5d07e2c72041deb8c0172cb1faafa97cd7dad302961a40eb-transpose2.png)

1. Select **Column to row** transpose.
2. For **Columns to merge**, select **Write to Table Start**, **Write to Table End**, **Sync Start** and **Sync End**. These are all merged into one column.
3. For **Column label for merged columns**, enter **Event Type** as the name for the merged column.
4. For **Column label for values**, enter **Timestamp**.
5. Select the rows you want represented in the table: **Unique Table Sync Key** (so it is clear which table the event is linked to), and the new columns, **Event type** and **Timestamp**.
6. [optional] To make the output easier to understand, you can also sort the **Unique Table Sync Key** column to ascending, so that the events for each table are in ordered rows. To sort a table by one column ascending, right-click or click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu, then select **Sort ascending**.

## Undo a transpose

The most effective way to undo a transpose is to change the source of your element to the original data source. For details, see [Change the data source for a workbook or element](/docs/change-the-data-source-for-a-workbook-or-element).

Updated 3 days ago

---

[Hierarchies (Beta)](/docs/hierarchies)[Write code](/docs/write-code)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Limitations](#limitations)
  + [Transpose row to columns](#transpose-row-to-columns)
  + - [Example: Counting games won and lost](#example-counting-games-won-and-lost)
  + [Transpose columns to rows](#transpose-columns-to-rows)
  + - [Example: Merging audit log event times](#example-merging-audit-log-event-times)
  + [Undo a transpose](#undo-a-transpose)