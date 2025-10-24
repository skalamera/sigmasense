# MovingStddev

# MovingStddev

The **MovingStddev** finds the the standard deviation of a column within a moving window.

## Syntax

```
MovingStddev(column, above, [below])
```

Function Arguments:

* **column** (required) - The column to be searched.
* **above** (required) - The first row to include, counting backward from the current row.
* **below** (optional) - The last row to include, counting forward from the current row. Defaults to 0 (current row will be the last row included).

> 📘
>
> ### When using this function without a sort enforced, there can be unexpected results. In order to ensure that the values are stable, verify that there is a sorted column within the table.

## Example

A table lists the weekly sales for the past year. The table is sorted ascending by the week. The **MovingStddev** function can be utilized in order to find the maximum value within specific windows.

```
MovingStddev([Weekly Sales], 4)
```

With [Weekly Sales] as the **column** argument and 4 as the **above** argument, the standard deviation of the weekly sales is calculated for each week along with the four previous weeks. Since the **below** argument is not specified, it defaults to 0.

![](https://files.readme.io/4d6cc13-1.png)

```
MovingStddev([Weekly Sales], 0, 4)
```

Here, the **above** argument is 0, so no previous weeks are included in the standard deviation calculation. The **below** average is 4, so the standard deviation of the weekly sales is computed for each week along with the next 4 weeks.

![](https://files.readme.io/c395f9e-2.png)

```
MovingStddev([Weekly Sales], 2, 2)
```

Here, the **above** argument is 2, so the previous two weeks are included in the standard deviation calculation. In addition, the **below** argument is 2, so the following two weeks are included as well.

![](https://files.readme.io/e7f18d0-3.png)

```
MovingStddev([Weekly Sales], 8, -4)
```

Here is an example where the **below** parameter is negative. The **below** parameter can be negative as long as the value is less than that of the **above** parameter. In this example, each window begins 8 weeks before the current week and ends 4 weeks before the current week, inclusive.

![](https://files.readme.io/48f640d-4.png)

Updated 3 days ago

---

Related resources

* [CumulativeStdDev](/docs/cumulativestddev)
* [StdDev](/docs/stddev)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)