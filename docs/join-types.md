# Join types

# Join types

## System requirements

Joins and lookups in workbooks and datasets must use sources from the same connection.

## Join types in Sigma

### Lookup

A lookup returns all rows from the current data and all data from matching rows in the joined data. When more than one match exists for a single row in the current data, the lookup returns an asterisk (\*), maintaining the number of rows in the current data.

Lookup functions like a VLOOKUP Excel function. For more information, see [Lookup join](/docs/lookup-join).

![](https://files.readme.io/e738471-Lookup.png)

### Inner join

An inner join returns rows that contain matching data in the current and joined data. It omits rows that don't contain matching data.

For more information, see [Inner join](/docs/inner-join).

![](https://files.readme.io/024edc4-Inner_Join.png)

### Left outer join

A left outer join returns all rows from the current data and all data from matching rows in the joined data. When more than one match exists for a single row in the current data, the join adds a row for each match in the joined data, which can result in an expanded row count.

For more information, see [Left outer join](/docs/left-outer-join).

![](https://files.readme.io/4b3adca-Left_Outer_Join.png)

### R‍ight outer join

A right outer join returns all rows from the joined data and all data from matching rows in the current data. When more than one match exists for a single row in the joined data, the join retains all matching rows in the current data.

For more information, see [Right outer join](/docs/right-outer-join).

![](https://files.readme.io/b835b2b-Right_Outer_Join.png)

### Full outer join

A full outer join returns all rows from the current data and all rows from the joined data, consolidating matching rows where applicable.

For more information, see [Full outer join](/docs/full-outer-join).

![](https://files.readme.io/b355faf-Full_Outer_Join.png)

Updated 3 days ago

---

[Upload CSV data](/docs/upload-csv-data)[Lookup join](/docs/lookup-join)

* [Table of Contents](#)
* + [System requirements](#system-requirements)
  + [Join types in Sigma](#join-types-in-sigma)
  + - [Lookup](#lookup)
    - [Inner join](#inner-join)
    - [Left outer join](#left-outer-join)
    - [R‍ight outer join](#right-outer-join)
    - [Full outer join](#full-outer-join)