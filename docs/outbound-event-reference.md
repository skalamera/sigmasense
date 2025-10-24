# Outbound event reference

# Outbound event reference

Sigma supports the following outbound events that describe user interactions with embedded Sigma content. Each event includes specific properties about the interaction that allow the host application to process and respond accordingly.

* For a list of the events that are possible to set, see [Inbound event reference](/docs/inbound-event-reference).
* For examples and more details, see [Implement inbound and outbound events in embeds](/docs/inbound-and-outbound-events-in-embeds).

## action:outbound

This event occurs when a **Generate iframe event** workbook action is triggered. This event can be used to react to user actions taken in the workbook. See [Create actions that trigger embed iframe events](/docs/create-actions-that-trigger-embed-iframe-events).

Event structure:

JavaScript

```
{
   type: 'action:outbound';
   name: string;
   values: Record<string,unknown>;
}
```

Event properties:

|  |  |
| --- | --- |
| `name` | A name for the event. Enter this name in the **Event name** field in the workbook action. |
| `values` | One or more event keys and values to pass to your host application. Enter the corresponding key-value pairs in the **Event key** fields in the workbook action. |

## url:onchange

This event occurs when the URL path changes, but not when URL search parameters change. This event returns the URL of the embed.

This event gives insight into when the user creates their own workbook that they can edit.

Event structure:

JavaScript

```
{
   type: 'url:onchange';
   url: string;
}
```

Event properties:

|  |  |
| --- | --- |
| `url` | The embed pathname without search or query parameters. |

## workbook:bookmark:onchange

This event occurs when a user selects or deselects a bookmark.

Event structure:

JavaScript

```
{
   type: 'workbook:bookmark:onchange', 
   bookmarkName: string; 
   workbookId: string;
   versionTagName: string | null; 
   bookmarkId: string;
}
```

Event properties:

|  |  |
| --- | --- |
| `bookmarkName` | The name of the bookmark. |
| `workbookId` | The ID of the workbook where the bookmark was created. |
| `versionTagName` | The tag assigned to the workbook version. Always null in embeds. |
| `bookmarkId` | The unique ID of the bookmark. |

## workbook:bookmark:oncreate

This event occurs when an embed user creates a bookmark using the embed UI.

This event is useful for analyzing when users create their bookmarks.

Event structure:

JavaScript

```
{
   type: 'workbook:bookmark:oncreate';
   bookmarkName: string;
   workbookId: string;
   versionTagName: string | null;
   bookmarkId: string;
}
```

Event properties:

|  |  |
| --- | --- |
| `bookmarkName` | The name of the bookmark. |
| `workbookId` | The ID of the workbook where the bookmark was created. |
| `versionTagName` | The tag assigned to the workbook version. |
| `bookmarkId` | The ID of the created bookmark. |

## workbook:bookmark:ondelete

This event occurs when an embed user deletes a bookmark using the embed UI.

Event structure:

JavaScript

```
{  
   type: 'workbook:bookmark:ondelete';  
   bookmarkName: string;  
   workbookId: string;  
   versionTagName: string | null;  
   bookmarkId: string;  
 }
```

Event properties:

|  |  |
| --- | --- |
| `bookmarkName` | The name of the bookmark. |
| `workbookId` | The ID of the workbook where the bookmark was deleted. |
| `versionTagName` | The tag assigned to the workbook version. |
| `bookmarkId` | The ID of the deleted bookmark. |

## workbook:bookmark:onupdate

This event occurs when an embed user updates a bookmark using the embed UI by either changing the name, setting or removing it as the default view, sharing the bookmark, or unsharing the bookmark by setting it as a personal view.

Event structure:

JavaScript

```
{  
   type: 'workbook:bookmark:onupdate';  
   workbookId: string;  
   versionTagName: string | null;  
   bookmarkId: string;  
   bookmarkName?: string;  
   isShared?: boolean;  
   isDefault?: boolean;  
}
```

Event properties:

|  |  |
| --- | --- |
| `workbookId` | The ID of the workbook where the bookmark was updated. |
| `versionTagName` | The tag assigned to the workbook version. |
| `bookmarkId` | The ID of the updated bookmark. |
| `bookmarkName` | Optional. The name of the bookmark. Only defined in the event if updated by the user. |
| `isShared` | Optional. Whether or not the bookmark is shared. Only defined in the event if updated by the user. |
| `isDefault` | Optional. Whether or not the bookmark is set as the default view. Only defined in the event if updated by the user. |

## workbook:chart:error

This event occurs when a chart produces an error.

This event is useful for detecting errors and taking action in response.

Event structure:

JavaScript

```
{
   type: 'workbook:chart:error';
   nodeId: string;
   message: string | undefined;
   code: string;
}
```

Event properties:

|  |  |
| --- | --- |
| `nodeId` | The element ID of the chart. |
| `message` | The error message. |
| `code` | The error code. |

## workbook:chart:onvalueselect

This event is specifically designed for user interactions with embedded visualization elements, like clicking data points in a bar chart. This event extends beyond the basic interaction details and includes a `values` object that provides insight about the specific chart component selected.

This event is crucial for applications that must respond to precise user interactions within embedded visualization elements. It offers a nuanced understanding of the chart component a user focuses on and analyzes.

Event structure:

JavaScript

```
{
   type: 'workbook:chart:onvalueselect';
   nodeId: string;
   title: string;
   values: valuesObject;
}
```

Event properties:

|  |  |
| --- | --- |
| `nodeId` | The element ID of the chart. |
| `title` | The title of the chart. |
| `values` | Contains key-value pairs representing any selected field column value, including color, axis, and value of the selected chart component. For example, the category label and corresponding value of a specific data point. |

Example scenario:

A user clicks on a specific bar in a bar chart. The event returns detailed information about that bar, including its category label and value. This enables the host application to provide context-specific responses or further data insights related to that precise interaction.

## workbook:dataloaded

This event occurs when a workbook finishes loading its data.

This event is useful for signaling when an iframe finishes loading a Sigma embed.

Event structure:

JavaScript

```
{  
   type: 'workbook:dataloaded' 
}
```

Example scenario: When a user exports the workbook as PDF via API immediately after accessing a workbook, they might see in the PDF that the embed element hasn't finished loading. Developers can add a check for iframe elements and check that the iframe contents are fully loaded before exporting.

## workbook:error

This event occurs when a workbook produces an error. Common error codes and messages that might occur that you might catch and handle with this event are listed in [Common embed error codes and messages](/docs/common-embed-error-codes-and-messages).

This event is useful for detecting errors and taking action in response.

Event structure:

JavaScript

```
{
   type: 'workbook:error';
   message: string | undefined;
   code: string;
}
```

Event properties:

|  |  |
| --- | --- |
| `message` | The error message. |
| `code` | The error code. |

## workbook:exploreKey:onchange

This event occurs when a new exploration is created on an embed.

Event structure:

JavaScript

```
{
   type: 'workbook:exploreKey:onchange', 
   exploreKey: string;
}
```

Event properties:

|  |  |
| --- | --- |
| `exploreKey` | The unique ID associated with the exploration. |

## workbook:fullscreen:onchange

This event occurs when the user minimizes or maximizes an element.

This event is useful for taking an action in response to an element being minimized or maximized.

Event structure:

JavaScript

```
{
   type: 'workbook:fullscreen:onchange';
   fullScreen: boolean;
}
```

Event properties:

|  |  |
| --- | --- |
| `fullScreen` | If true, the element was maximized; if false, the element was minimized. |

## workbook:id:onchange

This event occurs when the ID of the displayed workbook changes.

This event gives insight into when the user creates their own workbook that they can edit.

Event structure:

JavaScript

```
{ 
   type: 'workbook:id:onchange'; 
   id: string 
}
```

Event properties:

|  |  |
| --- | --- |
| `id` | The workbook ID. |

## workbook:loaded

This event occurs when a workbook's metadata has loaded, but the elements haven't been evaluated.

This event is crucial for scenarios in which an initial setup or a pre-processing step is required before the workbook becomes interactive. It provides an opportunity to implement any preparatory actions in the host application based on the workbook's metadata.

Event structure:

JavaScript

```
{
  type: 'workbook:loaded',
  workbook: {
    variables: encodedVariables // Contains workbook metadata
  },
}
```

## workbook:ondelete

This event occurs when a user clicks **Delete** in the embed menu and a workbook is successfully deleted.

Event structure:

JavaScript

```
{
   type: 'workbook:ondelete';
   id: string;
}
```

Event properties:

|  |  |
| --- | --- |
| `id` | The workbook ID. |

## workbook:pageheight:onchange

This event communicates the document height to the parent whenever it changes.

This event is useful for avoiding situations where the body of a frame might scroll due to dynamic sizing. Use this function to calculate the height of the iframe.

To use this event, the `responsive_height` parameter must be set to true. See [Embed URL parameters](/docs/embed-url-parameters#optional-interface-parameters).

Event structure:

JavaScript

```
{
   type: 'workbook:pageheight:onchange';
   pageHeight: number;
}
```

Event properties:

|  |  |
| --- | --- |
| `pageHeight` | The height of the page, in pixels. |

## workbook:pivottable:oncellselect

This event occurs when a user selects a cell or multiple cells in an embedded pivot table. This event provides an array of selected cells and their properties.

This event is crucial for applications that require responsive interaction with pivot table data within Sigma, allowing the host application to tailor its response based on user selection in the embedded workbook.

Event structure:

JavaScript

```
{
   type: 'workbook:pivottable:oncellselect';
   nodeId: string;
   title: string;
   cells: cellsObject;
}
```

Event properties:

|  |  |
| --- | --- |
| `nodeId` | The element ID of the pivot table. |
| `title` | The title of the pivot table. |
| `cells` | A collection of of objects for each cell, including the following:   * `type`: 'valueCell' to identify the cell as a standard value cell. * `value`: Value to identify the actual cell data. * `columnName`: String to name the column containing the cell. |

## workbook:published

This event occurs in secure embeds when a user saves and publishes a workbook.

This event is useful for taking some action in the host application when a workbook is published and for tracking when changes are made to a workbook.

Event structure:

JavaScript

```
{
   type: 'workbook:published';
   workbookId: string;
}
```

Event properties:

|  |  |
| --- | --- |
| `workbookId` | The ID of the published workbook. |

## workbook:saveas

This event occurs when a user successfully saves a workbook using the **Save as** option on the embed menu of the workbook.

Event structure:

JavaScript

```
{
   type: 'workbook:saveas';
   workbookId: string;
   saveWorkbookId: string;
}

```

Event properties:

|  |  |
| --- | --- |
| `workbookId` | The ID of the original workbook. |
| `savedWorkbookID` | The ID of the newly saved workbook. |

## workbook:table:oncellselect

This event occurs when a user selects a cell or multiple cells in an embedded table. This event provides an array of selected cells and their properties.

This event is crucial for applications that require responsive interaction with table data within Sigma, allowing the host application to tailor its response based on user selection in the embedded workbook.

Event structure:

JavaScript

```
{
   type: 'workbook:table:oncellselect';
   nodeId: string;
   title: string;
   cells: cellsObject;
}
```

Event properties:

|  |  |
| --- | --- |
| `nodeId` | The element ID of the table. |
| `title` | The title of the table. |
| `cells` | A collection of of objects for each cell, including the following:   * `type`: 'valueCell' to identify the cell as a standard value cell. * `value`: Value to identify the actual cell data. * `columnName`: String to name the column containing the cell. * `underlyingData`: An array of rows contributing to the aggregate value. The data is subject to size limitations. A truncation flag indicates when the data exceeds the limit. |

Example scenario:

When a user selects a specific cell (for example, in the *Sum of Revenue* column) for a particular order, the event returns detailed information about the cell, including its value, column name, and any underlying data (if it's an aggregate value).

## workbook:variables:onchange

This event occurs when a user- or system-initiated update is applied to a control element within the embedded Sigma content.

This event is essential for situations where the host application needs to respond to changes within the embedded Sigma content. This event provides information about user interactions with the embedded content, allowing for a dynamic and responsive integration within the host application.

For detailed examples on how values are encoded for URLs, refer to [Add query string parameters to a URL](/docs/workbook-control-values-in-the-url#add-query-string-parameters-to-a-url).

Event structure:

JavaScript

```
{
  type: 'workbook:variables:onchange',
  workbook: {
    variables: { 'Variable1': 'value1', 'Variable 2': 'value2' } // Updated variable values
  },
}
```

Event properties:

|  |  |
| --- | --- |
| `workbook.variables` | Contains the controls and their values updated within the workbook. The format follows the structure `{ 'control-ID': 'value' }`, with URL-encoded values. |

Example scenario:

If you have a multi-select list values control configured with a control ID of `store-region` and a user selects two regions, *East* and *Midwest*, the event emitted is of the following format:

JavaScript

```
{
  type: 'workbook:variables:onchange',
  workbook: {
    variables: { 'store-region': "East,Midwest" }
  },
}
```

Updated 3 days ago

---

[Inbound event reference](/docs/inbound-event-reference)[Manage iframes for embeds](/docs/manage-iframes-for-embeds)

* [Table of Contents](#)
* + [action:outbound](#actionoutbound)
  + [url:onchange](#urlonchange)
  + [workbook:bookmark:onchange](#workbookbookmarkonchange)
  + [workbook:bookmark:oncreate](#workbookbookmarkoncreate)
  + [workbook:bookmark:ondelete](#workbookbookmarkondelete)
  + [workbook:bookmark:onupdate](#workbookbookmarkonupdate)
  + [workbook:chart:error](#workbookcharterror)
  + [workbook:chart:onvalueselect](#workbookchartonvalueselect)
  + [workbook:dataloaded](#workbookdataloaded)
  + [workbook:error](#workbookerror)
  + [workbook:exploreKey:onchange](#workbookexplorekeyonchange)
  + [workbook:fullscreen:onchange](#workbookfullscreenonchange)
  + [workbook:id:onchange](#workbookidonchange)
  + [workbook:loaded](#workbookloaded)
  + [workbook:ondelete](#workbookondelete)
  + [workbook:pageheight:onchange](#workbookpageheightonchange)
  + [workbook:pivottable:oncellselect](#workbookpivottableoncellselect)
  + [workbook:published](#workbookpublished)
  + [workbook:saveas](#workbooksaveas)
  + [workbook:table:oncellselect](#workbooktableoncellselect)
  + [workbook:variables:onchange](#workbookvariablesonchange)