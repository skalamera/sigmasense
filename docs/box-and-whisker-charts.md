# Box and whisker charts

# Box and whisker charts

Box and whisker charts display the distribution of a set of values along an axis. They are also commonly known as box plots.

## Requirements

* To create a data element, you must have Can Edit [access](/docs/folder-and-document-permissions) to the individual workbook and be in Edit mode.
* Many exploratory actions are also supported in Explore mode; see [Workbook modes.](/docs/workbook-modes-overview-view-explore-edit)

## Anatomy of a box and whisker chart

Box and whisker charts break data into quartiles. The upper quartile, median, and lower quartile make up what we refer to as box. The entire spread from whisker minimum to whisker maximum, including the box, accounts for the statistically central range of data. This is called the interquartile range (IQR) and is calculated as `Q3 - Q1`. Data points that fall out of the IQR are called outliers.

**Maximum**: The data point with the highest value below `Q3 + 1.5*IQR`

**Upper Quartile:** Values contained in the upper 25% of data.

**Median**: The data range's midpoint.

**Lower Quartile**: Values contained in the lower 25% of data.

**Minimum**: The data point with the lowest value above `Q1 - 1.5*IQR`

**Outliers**: Values that fall above or below the IQR. Outliers are calculated as `is > Q3 + 1.5*IQR` and `is < Q1 - 1.5*IQR`

![](https://files.readme.io/ee8a4b5-1.png)

## Plot a box and whisker chart

You can [create a chart](/docs/create-a-data-element) from the **Add element** section of your workbook's editor panel or directly from [an existing data element](/docs/create-a-data-element#create-a-data-element-from-an-existing-element-using-the-editor-panel).

Visualized data will not display on the page canvas until all required plot fields are defined.

Add columns to open fields using either the field's + menu or dragging and dropping the column.

### Fields

* **X-AXIS** (1 column)  
  Categorical data is first grouped by the column on the X-axis.
* **Y-AXIS** (1+ columns)  
  Columns added to the chart's Y-axis are aggregated by default. Aggregation type (e.g. Sum vs Count) is dependent on the original column’s value type.  
  In some cases, you might want to uncheck the **AGGREGATE VALUES** option. Aggregating the value on the **Y-AXIS** value gives you an option to **SPLIT BY**.
* **SPLIT BY** (1 column - optional)  
  Creates a second grouping under the first grouping (defined on the X-AXIS).

**Example**: In the screenshot below, the **X-AXIS** is set to [Store State], grouping the rows of data into states. The column on the **Y-AXIS**, [Store Sales] defines the numerical range of the plotted data. The column added to **SPLIT BY**, [Store Name], acts as a grouping below [Store State]. In other words, data is grouped by state and then each state's data is grouped by (aka "split by") individual stores' names. Points on the y-axis represent the aggregate [Store Sales] values listed under the second, "split by", grouping.

![Screen_Shot_2021-10-26_at_11.30.15_AM.png](https://files.readme.io/ff4678b-2.png)

### Marks

* **COLOR**
* **TOOLTIP** (1+ columns)

### Display orientation (horizontal vs vertical)

Box and whisker charts can be displayed both vertically and horizontally.

To select your chart’s orientation, select either the display vertical ( viz-box-vertical.svg ) or display horizontal ( viz-box-horizontal.svg ) icon button in the chart’s editor panel view.

![Screen_Shot_2021-10-26_at_2.45.15_PM.png](https://files.readme.io/4dbe6bb-5.png)

## Format options

**Before you start:** This action uses the editor panel. If you have not done so already, open the editor panel from either Explore or Edit mode.

To begin editing an chart's format options:

1. Select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/element-format.svg) **Element format** in the side navigation.
2. Select a format option to view and edit its settings.

The following format categories are available for box and whisker charts:

* **[BACKGROUND](/docs/customize-element-background)**
* **[TITLE](/docs/customize-element-title)**
* **[X-AXIS](/docs/format-chart-axis-position)**
* **[Y-AXIS](/docs/format-chart-axis-position)**
* **[LEGEND](doc:doc:format-chart-legend)**
* **[BOX SHAPE](#customize-point-display-options)**
* **[DATA LABELS](/docs/visualization-data-labels)**
* **[REFERENCE MARKS](/docs/visualization-reference-marks)**

## Customize point display options

**Before you start:** This action uses the editor panel. If you have not done so already, open the editor panel from either Explore or Edit mode.

1. Select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/element-format.svg) **Element format** in the side navigation.
2. Click **BOX SHAPE**.
3. Select **BOX SHAPE** formatting from the options presented:
   * The **Show points** checkbox is checked by default. Uncheck to hide all points.
   * If **Show points** is selected, you can choose:
     + **Outliers only** – Shows only the points that fall outside the box.
     + **All points** – Shows all points, regardless of position.  
       ![Screen_Shot_2021-10-26_at_2.48.24_PM.png](https://files.readme.io/2a33b62-7.png)

Updated 3 days ago

---

Related resources

* [Intro to charts](/docs/intro-to-visualizations)
* [Create a data element](/docs/create-a-data-element)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Anatomy of a box and whisker chart](#anatomy-of-a-box-and-whisker-chart)
  + [Plot a box and whisker chart](#plot-a-box-and-whisker-chart)
  + - [Fields](#fields)
    - [Marks](#marks)
    - [Display orientation (horizontal vs vertical)](#display-orientation-horizontal-vs-vertical)
  + [Format options](#format-options)
  + [Customize point display options](#customize-point-display-options)