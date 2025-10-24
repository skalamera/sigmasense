# MovingMin

# MovingMin

The **MovingMin** function finds the minimum value of a column within a moving window.

## Syntax

```
MovingMin(column, above, [below])
```

Function Arguments:

* **column** (required) - The column to be searched.
* **above** (required) - The first row to include, counting backward from the current row.
* **below** (optional) - The last row to include, counting forward from the current row. Defaults to 0 (current row will be the last row included).

> 📘
>
> ### When using this function without a sort enforced, there can be unexpected results. In order to ensure that the values are stable, verify that there is a sorted column within the table.

## Example

A table lists the weekly sales for the past year.  The table is sorted ascending by the week.  The **MovingMin** function can be utilized in order to find the minimum value within specific windows.

```
MovingMin([Weekly Sales], 4)
```

With [Weekly Sales] as the **column** argument and 4 as the **above** argument, the minimum weekly sales value is calculated for each week along with the four previous weeks. Because the **below** argument is not specified, it defaults to 0.

![](https://files.readme.io/b573f44-11.png)

```
MovingMin([Weekly Sales], 0, 4)
```

Here, the **above** argument is 0, so there isn't any previous weeks included in the minimum calculation. The **below** average is 4, the minimum weekly sales value is computed for each week along with the next 4 weeks.

![](https://files.readme.io/e467e32-22.png)

```
MovingMin([Weekly Sales], 2, 2)
```

Here, the **above** argument is 2, so the previous two weeks is included in the minimum calculation. In addition, the **below** argument is 2, so the following two weeks is also included.

![](https://files.readme.io/9527048-33.png)

```
MovingMin([Weekly Sales], 8, -4)
```

Here is an example where the **below** parameter is negative. The **below** parameter can be negative as long as the value is less than that of the **above** parameter. In this example, each window begins 8 weeks before the current week and ends 4 weeks before the current week, inclusive.

![](https://files.readme.io/9e441cb-44.png)

Updated 3 days ago

---

Related resources

* [CumulativeMin](/docs/cumulativemin)
* [Min](/docs/min)
* [MovingMax](/docs/movingmax)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Example](#example)