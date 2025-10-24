# Join data in datasets

# Join data in datasets

When creating a join between warehouse tables or datasets, there are times where you need to make changes to the data in the input columns to make the join work. In those cases, you can add a formula to your input columns while creating a join.

You can define your join key with a scalar formula using any of the functions available in Sigma. The formula can be as simple as a [Type change](/docs/type-functions-overview) function, or a complex [If](/docs/if) statement.

![Join type options showing the option to add a formula as the target join key when joining datasets.](https://files.readme.io/f61d09a-join_calc_col.png)

## Add a formula to a join input column

1. On the right hand side of your worksheet, go to the Data Sources tab.
2. Click the **+** to add a new join.
3. Choose a data source.
4. Choose your join type.
5. Under join keys, open the drop down menu and click **+Add Formula** for the join key you want to modify.
6. Enter your formula.  
   Wait for the preview to load to ensure that your chosen join keys are joining your data as expected.
7. Click **Done** to finish creating the join.

Updated 3 days ago

---

[Full Outer Join](/docs/full-outer-join)[Join data in workbooks](/docs/join-data-in-workbooks)

* [Table of Contents](#)
* + [Add a formula to a join input column](#add-a-formula-to-a-join-input-column)