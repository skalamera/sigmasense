# Extract columns from JSON or variant data

# Extract columns from JSON or variant data

The JSON data type stores inherently hierarchical data. You can extract fully structured and semi-structured data from a table column that contains JSON [using the column menu](#extract-json-data-from-a-column) or by writing a [formula that uses dot notation](#use-dot-notation-to-extract-values-from-json-columns).

## Requirements

The ability to extract columns from JSON or variant data requires the following:

* You must be assigned an [account type](/docs/license-and-account-type-overview) with the **Basic explore** permission enabled.
* You must be the workbook owner or be granted **Can explore** or **Can edit** [workbook permission](/docs/folder-and-document-permissions).

## Extract JSON data from a column

You can extract JSON data from one column into separate columns in any data element. Columns with a data type of JSON or Variant have an **Extract columns...** option in the column menu. If your data is semi-structured and you do not see the option to **Extract columns**, you can [convert the data type](#convert-the-data-type-of-a-column). It is a best practice to extract columns in upstream elements.

> 🚧
>
> ### The list of extracted columns is retrieved from the first 1,000 rows of the table. Key-value pairs in later rows are not extracted.

To extract JSON data from one column into separate columns that match the keys in the JSON data:

1. Go to the column in the workbook. This example uses the *Cust Json* column of the EXAMPLES.PLUGS\_ELECTRONICS\_HANDS\_ON\_LAB\_DATA sample data.
2. For a column, click the down arrow (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/caret.svg)) to open the column menu.
3. Select **Extract columns**.

   The **Extract Fields** modal opens.
4. In the modal, select the JSON keys that you want to extract into their own columns. One column is created for each JSON key that you select.
5. Click **Confirm** to extract the selected key-value pairs and create corresponding columns.

   ![](https://files.readme.io/1740b22dd46ddd5706ead9883a0a60ff5be62b63c333c703d7748ab7f6897ef2-extractjson_4.png)

You can then use the new columns in your data exploration and analysis.

## Convert the data type of a column

If you want to extract JSON or semi-structured data from a column and you do not see the **Extract columns** option in the column menu, convert the data type of the column to JSON or Variant:

* Modify the column formula with the [Json](/docs/json) or [Variant](/docs/variant) type functions.
* Open the column menu and select **Transform** > **Convert to JSON**.

## Use dot notation to extract values from JSON columns

You can also extract values from JSON arrays and objects in a JSON column by writing a formula using dot notation.

### Extract values from JSON data

To extract values from a JSON data type column, write a formula that uses dot notation and supplies constant values to reference the JSON keys, like the following syntax:

```
[ColumnName].fieldName.subFieldName...
```

Where

* **Column name** is the name of the primary object.
* **fieldName** is the name of one of the fields of the primary object.
* **subFieldName** is the name of one of the fields of a secondary field.
* and so on...

For example, given the following JSON structure in a column called *Order JSON*:

JSON

```
{
  "order": { "orderId": 6 },
  "product": { "productId": 49, "productName": "Pumpkin Muffin Mix" },
  "user": { "firstName": "Sally", "lastName": "Sigma", "userId": 1 }
}
```

You can write a formula with dot notation to extract the *productName* into a new column, wrapping the syntax in the [Text](/docs/text) function to convert the data type from JSON to text:

```
Text([Order JSON].product.productName)
```

![Excerpt of the table showing an Order JSON column with contents {"order":{"orderId":1}, "product":{"productId":117,"productName":"Ground... and a productName field that extracts the product name from the JSON, listing "Ground Turkey Chub" as plain text data.](https://files.readme.io/63d88f0-4.png)

If the key that you extract has a JSON object as the value, you can create a column with the JSON objects with a formula like the following:

```
[OrderJSON].product
```

The new column contains JSON data with values like the following:

JSON

```
{ "productId": 49, "productName": "Pumpkin Muffin Mix" }
```

### Extract values from JSON arrays

You can also use dot notation to extract values from JSON arrays by referencing the index of the value in the array in a formula:

```
[ColumnName].fieldName[i]
[ColumnName].fieldName.subFieldName[i]...
```

Where **i** is the index of the array, starting with 0.

For example, given the following JSON structure in a column called *Cart Details*:

JSON

```
{
    "cart": [
        "apples",
        "yogurt",
        "steak"
    ],
    "orderId": 1
}
```

You can use dot notation to retrieve the items in the `cart` array. For example, write a formula that returns the item that corresponds to index 0 of the *cart* array as text data:

```
Text([Cart Details].cart[0])
```

The output appears in the new column you created:

![A table with one column named Cart Details with one row of data corresponding to the described JSON and another column called cart[0] which has been renamed from Calc and which lists apples.](https://files.readme.io/407246cb1cda9612c175ef2607f4ffe41bbfaf53eab7a4fe231303604569c720-cart-json.png)

### Extract values from JSON objects in JSON arrays

You can combine the dot notation to retrieve values from JSON arrays and JSON objects to extract values from more complex JSON structures.

For example, given JSON like the following in a column named *Weather Report*:

JSON

```
{
  "city": {
    "coord": { "lat": 43.000351, "lon": -75.499901 },
    "country": "US",
    "id": 5128638,
    "name": "New York",
  },
  "weather": [
    {
      "description": "broken clouds",
      "icon": "04d",
      "id": 803,
      "main": "Clouds"
    }
  ],
  "main": {
    "humidity": 60,
    "pressure": 1018,
    "temp": 293.68,
    "temp_max": 294.26,
    "temp_min": 293.15
  },
  "time": 1473614247,
}
```

You can extract the weather description into a column using a formula like the following:

```
Text([Weather Report].weather[0].description)
```

To output column values like:

```
broken clouds
```

Updated 3 days ago

---

[Add hyperlinks and images to columns](/docs/add-hyperlinks-to-columns)[Pivot tables](/docs/pivot-tables)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Extract JSON data from a column](#extract-json-data-from-a-column)
  + [Convert the data type of a column](#convert-the-data-type-of-a-column)
  + [Use dot notation to extract values from JSON columns](#use-dot-notation-to-extract-values-from-json-columns)
  + - [Extract values from JSON data](#extract-values-from-json-data)
    - [Extract values from JSON arrays](#extract-values-from-json-arrays)
    - [Extract values from JSON objects in JSON arrays](#extract-values-from-json-objects-in-json-arrays)