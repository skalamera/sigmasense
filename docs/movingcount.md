# MovingCount

# MovingCount

The **MovingCount** function counts the number of non-null values within a column in a moving window.

## Syntax

```
MovingCount([Column], above, below)
```

Function Arguments

* **[Column]** (required) - The column of numbers, text, or dates to count. Null values are skipped.
* **above** (required) - The first row to include, counting backward from the current row.
* **below** (optional) - The last row to include, counting forward from the current row. Defaults to 0 (current row will be the last row included).

> 📘
>
> When using this function without a sort enforced, there can be unexpected results. In order to ensure that the values are stable, verify that there is a sorted column within the table.

## Example

A table contains data about the amount of violations found by day during inspections in restaurants.  The **MovingCount** function can be used to find the number of non-null values within different moving windows.

```
MovingCount([Violations], 4)
```

With [Violations] as the **column** argument and 4 as the **above** argument, the number of non-null values are calculated for each day along with the four previous days. Since the **below** argument was not specified, it defaults to 0.

![](https://files.readme.io/8a4c0ff-11.png)

```
MovingCount([Violations], 0, 4)
```

Here, the **above** argument is 0, so no previous days are included in the count. The **below** average is 4, so the count is computed for each day along with the next 4 days.

![](https://files.readme.io/8bb53a3-22.png)

```
MovingCount([Violations], 2, 2)
```

Here, the **above** argument is 2, so the previous two days will be included in the count. In addition, the **below** argument is 2, so the following two days will be included as well.

![](https://files.readme.io/568808b-33.png)

```
MovingCount([Violations], 8, -4)
```

Here is an example where the **below** parameter is negative. The **below** parameter can be negative as long as the value is less than that of the **above** parameter. In this example, each window begins 8 days before the current day and ends 4 days before the current week, inclusive.

![](https://files.readme.io/5e97f41-44.png)

Updated 3 days ago

---

Related resources

* [Count](/docs/count)
* [CumulativeCount](/docs/cumulativecount)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)