# Display chart data labels

# Display chart data labels

You can display data labels for the following visualization types:

* [Area charts](/docs/area-charts)
* [Bar charts](/docs/build-a-bar-chart)
* [Box and whisker charts](/docs/box-and-whisker-charts)
* [Combo charts](/docs/combo-charts)
* [Donut & pie charts](/docs/pie-and-donut-charts)
* [Funnel charts](/docs/build-a-funnel-chart)
* [Gauge charts](/docs/build-a-gauge-chart)
* [Line charts](/docs/build-a-line-chart)
* [Scatter plots](/docs/build-a-scatter-plot)
* [Region and Point maps](/docs/maps)

You can also [format the appearance of data labels](#format-and-show-data-labels) .

## User requirements

* You must have **Can edit** or **Can explore** [access](/docs/folder-and-document-permissions) to the workbook.
* You must be in a draft, custom view, or saved view of the workbook.

## Format and show data labels

You can format and show data labels on your chart. For charts that can have more than one series, such as a bar chart, you can choose whether to apply the formatting settings to all series in the chart or a specific series.

1. Select the desired chart on the workbook page.
2. In the editor panel, select **Format**.
3. Click **Data labels** to expand the section.
4. To show default data labels on your chart, select one of the following:

   * To show data labels for all series on your chart, turn on **Show data labels**.
   * To configure which data labels appear for different series on a combo or cartesian (bar, line, area, or scatter) chart with multiple series of data, leave the default of **Apply to all series** selected or choose the data series that you want to display data labels for, then turn on **Show data labels** to show labels for that series.

   If you do not turn on **Show data labels**, any formatting options that you select apply only to [custom data labels](#add-custom-data-labels-to-a-chart-or-map).
5. Use the available options to customize your data labels.

   For example, customize the style of the labels to display minimum and maximum labels or endpoint labels, or customize the font color and size. For some charts, you can configure the orientation and position of labels, as well as whether to show an outline, or stroke, around the label text. You can also adjust the aggregation method of the data.

   > 📘
   >
   > ### Data label options vary by visualization type.

## Add custom data labels to a chart or map

By default, a chart can display data labels for the aggregate series of the chart, such as the Y-axis or X-axis values, depending on the chart and orientation. For some charts, and for region and point maps, you can specify a column to use to provide custom data labels for a chart.

You can add custom data labels to one of the following chart types:

* Bar charts
* Line charts
* Combo charts
* Area charts
* Scatter plots
* Region maps
* Point maps

Labels display with column values split by each chart segment, such as a region or point on a map.

To add custom data labels:

1. Select the element.

   The editor panel opens to the **Properties** section.
2. In the editor panel, click **Label**.
3. Add one or more columns whose values you want to display on the chart or map.
4. (Optional) Adjust the aggregation, format, or other settings of the column value so that the label appears as desired. See [Format and show data labels](#format-and-show-data-labels).

Updated 3 days ago

---

Related resources

* [Intro to visualizations](/docs/intro-to-visualizations)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Format and show data labels](#format-and-show-data-labels)
  + [Add custom data labels to a chart or map](#add-custom-data-labels-to-a-chart-or-map)