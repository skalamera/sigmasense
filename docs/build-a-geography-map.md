# Build a geography map

# Build a geography map

Geography maps (**Map - Geography** chart type) support datasets with [geography data (WKT format) or variant data (GeoJSON format)](#data-prerequisites) and are typically used to illustrate geospatial objects on a map. Create a [connection map](#geography-map-variations) to display spatial networks, correlations, and relationships, or build a [choropleth map](#geography-map-variations) to identify variability and patterns across distinct geographic areas.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Intro+to+Visualizations/geography-map.png)

> 💡
>
> ### Example use cases:
>
> * **Land use analytics**: Represent land parcels by zoning code to identify land use patterns and conflicts with proximal areas
> * **Marketing analytics**: Quantify customers across specific regions to analyze customer distribution and understand market reach.
> * **Environmental analytics**: Map oil and gas pipelines to assess proximity to residential areas and natural resources.

## User requirements

The ability to create geography maps and other charts requires the following:

* You must be assigned an [account type](/docs/user-account-types) with the **Create, edit, and publish workbooks** and/or **Explore workbooks permission** enabled.
* You must be the workbook owner or be granted **Can explore** or **Can edit** [workbook permission](/docs/folder-and-document-permissions).

If you’re granted **Can explore** access to the workbook, you can create and modify chart properties and formatting in **Explore** mode, but you cannot publish your changes.

## Data prerequisites

A geography map requires one of the following [data types](/docs/data-types-and-formats):

* Geography data (WKT)1
* Variant data (GeoJSON)

If your dataset isn’t compatible, you might be able to use functions (such as [type](/docs/type-functions-overview) or [geography](/docs/geography-functions-overview) functions) to convert data to a supported type. Alternatively, when building a choropleth map, you can also use the **Map - Region** chart.

1The geography data type is available with Snowflake and BigQuery connections only.

## Geography map variations

|  |  |
| --- | --- |
|  | Connection (link) map Connect geographic locations (cities, landmarks, points of interest, and more) to illustrate spatial networks, correlations, and relationships. |
|  | Choropleth map Define regions and compare values to identify variability and patterns across distinct geographic areas. |

> 🚩
>
> ### The **Map - Geography** chart doesn't support point (link) maps. However, you can build point maps using the **Map - Point** chart if your dataset contains geospatial data that represents points.
>
> If points are represented by the geography data type, use the [Latitude](/docs/latitude) and [Longitude](/docs/longitude) functions to extract the coordinates from the WKT format. If points are represented by the variant data type, select the **Extract columns** option in the column menu to extract the coordinates from the GeoJSON format. You can then plot the extracted data in the **Map - Point** chart.

## Basic geography map configurations

Geography maps require the following element properties:

* **Chart**: chart type used to illustrate the data
* **Geography**: source column that defines the geospatial objects

> 📘
>
> ### At the core of every chart is an underlying data table (derived from the data source) that supplies the information visualized by the chart. As you build a geography map, Sigma automatically calculates and structures the data to map the element properties to source columns in the underlying data table. For information about how to view the underlying data while you configure the chart, see [Maximize or Minimize a Data Element](/docs/maximize-or-minimize-a-data-element).

### Add a geography map

Add a new chart element and designate it as a geography map.

1. Open a workbook in **Explore** or **Edit** mode and [add a new chart element](/docs/create-a-data-element).
2. In the new element’s **Chart** property, click the dropdown field and select **Map - Geography** from the list.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+geography+map/geography_select-visualization-type.png)

### Define the geospatial objects

Configure a source column that defines the geospatial objects (lines or polygons) representing landmarks, routes, regions, or other features. The column must contain geography data in WKT format or variant data in GeoJSON format.

1. In the **Geography** property, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/button-add.svg) **Add column** and select an option from the menu:

   * To map objects from an existing column, search or scroll the **Select geography/variant column** list and select the column name.
   * To create a new column using a custom formula, select **Add new column** and enter the formula or value in the toolbar.
   > 💡
   >
   > ### You can also select or replace an existing column by dragging and dropping a column name from the **Columns** list to the **Geography** property.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+geography+map/geography_select-geography-source-column.png)

   When the Geography **property** is configured, the map illustrates the geospatial objects represented by the source column data.

   ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+geography+map/geography_illustrate-geospatial-objects.png)

## Advanced geography map properties and formatting

### Configure mark colors

Configure the line or polygon mark colors in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/wb-element_viz.svg) **Element properties** > **Marks** > **Color** tab to visualize patterns, highlight variations, improve readability, and more.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+geography+map/geography_marks_color.png)

| Mark color |  |  |
| --- | --- | --- |
| **Single color** | Enter a hex code or select an option from the color palette or color picker. |  |
| **By scale** | Select a source column to define the color scale, then select a color range to apply to the marks.  Column values associated with color scale are automatically included in the mark tooltips. For more information, see [Customize tooltip fields](#customize-tooltip-fields). |  |

### Customize tooltip fields

Configure source columns in the ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/wb-element_viz.svg) **Element properties** > **Marks** > **Tooltip** property to add fields to the map tooltips.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+geography+map/geography_marks_tooltip.png)

If a source column is configured in the **Marks** > **Color** property, its values are automatically displayed in the tooltips. For information about changing tooltip defaults and adding fields, see [Customize chart mark tooltips fields](/docs/customize-chart-mark-tooltip-fields).

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+geography+map/geography_marks_tooltip_add.png)

### Change map style

Change the base style of your map in the **Element format** > **Map** style section.

![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Workbooks/Visualizations/Build+a+geography+map/geography_format_map-style.png)

| Base style |  |
| --- | --- |
| Light |  |
| Dark |  |
| Streets |  |
| Satellite |  |
| Custom *(example)* |  |

## All geography map format options

* [Title](/docs/customize-element-title)
* [Map style](#change-map-style)
* [Legend](/docs/format-chart-legend)

Updated 3 days ago

---

Related resources

* [Intro to charts](/docs/intro-to-visualizations)
* [Create a data element](/docs/create-a-data-element)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Data prerequisites](#data-prerequisites)
  + [Geography map variations](#geography-map-variations)
  + [Basic geography map configurations](#basic-geography-map-configurations)
  + - [Add a geography map](#add-a-geography-map)
    - [Define the geospatial objects](#define-the-geospatial-objects)
  + [Advanced geography map properties and formatting](#advanced-geography-map-properties-and-formatting)
  + - [Configure mark colors](#configure-mark-colors)
    - [Customize tooltip fields](#customize-tooltip-fields)
    - [Change map style](#change-map-style)
  + [All geography map format options](#all-geography-map-format-options)