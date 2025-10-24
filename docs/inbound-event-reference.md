# Inbound event reference

# Inbound event reference

Sigma supports the following inbound events, which are triggered by user input in the host application or parent window.

* For a list of the events emitted by actions in your Sigma embed, see [Outbound event reference](/docs/outbound-event-reference).
* For examples and more details, see [Implement inbound and outbound events in embeds](/docs/inbound-and-outbound-events-in-embeds).

## workbook:bookmark:create

This event creates a bookmark without using the embed UI.

Event structure:

JavaScript

```
{
   type: 'workbook:bookmark:create';
   name: string;
   isDefault: boolean;
   isShared: boolean;
}
```

Event properties:

|  |  |
| --- | --- |
| `name` | Name of the bookmark. |
| `isDefault` | If true, bookmark is viewed by default on opening the document. |
| `isShared` | If true, bookmark is shared with all users on this workbook. |

## workbook:bookmark:delete

This event deletes a bookmark without using the embed UI.

Event structure:

JavaScript

```
{
   type: 'workbook:bookmark:delete';
   bookmarkId: string;
}
```

Event properties:

|  |  |
| --- | --- |
| `bookmarkId` | The unique ID of the bookmark. |

## workbook:bookmark:select

This event selects or clears a bookmark in an embed.

Event structure:

JavaScript

```
{
   type: 'workbook:bookmark:select';
   bookmarkId?: string | null;
}
```

Event properties:

|  |  |
| --- | --- |
| `bookmarkId` | The unique ID of the bookmark. If specified, the user is redirected to the bookmark. If not specified, the bookmark is cleared and the user is redirected to the published version of the workbook. |

## workbook:bookmark:update

This event is used to update a bookmark with the changes from a user's exploration (custom view). The event is equivalent to clicking **Save updates to custom view** in the document menu in the Sigma UI.

Event structure:

JavaScript

```
{
   type: 'workbook:bookmark:update';
}
```

A `workbook:error` iframe event is triggered in the following circumstances:

| Cause | Error |
| --- | --- |
| The user didn't select a bookmark to update. | Bookmark not selected |
| The user didn't make any changes to the selected bookmark and thus it can't be updated. | Cannot update bookmark, no explore changes made |

## workbook:fullscreen:update

This event is used to update the fullscreen search parameter. If the targeted element is maximized, calling this function will minimize it and vice versa. Equivalent to **Maximize element** in the UI.

This event is useful for maximizing and minimizing elements without using the UI.

Event structure:

JavaScript

```
{
   type: 'workbook:fullscreen:update';
   nodeId: string | null;
}
```

Event properties:

|  |  |
| --- | --- |
| `nodeId` | The node ID corresponding to the element. |

## workbook:modal:toggle

This event is used to open or close a modal in an embed. This event requires the user to have the necessary permissions to interact with the modal in the UI. For example, the **Schedule exports** modal requires the `Schedule export` permission.

Event structure:

JavaScript

```
{
   type: 'workbook:modal:toggle';
   modalType: 'schedule' | 'export' | undefined;
}
```

Event properties:

|  |  |
| --- | --- |
| `modalType` | The type of modal to open. Pass `undefined` to close the currently open modal. Supported modal types: `'schedule'`, `'export'`, `undefined` |

## workbook:mode:update

This event is used to change between **View** mode and **Explore** mode in an embed. If the user does not have the necessary permissions to explore the content or if the embed does not support **Explore** mode, this event has no effect. For more information about workbook modes, see [Workbook modes overview](/docs/workbook-modes-overview).

Event structure:

JavaScript

```
{  
   type: 'workbook:mode:update';
   mode: 'view' | 'explore';
}
```

Event properties:

|  |  |
| --- | --- |
| `mode` | The mode in which the embed should present to the user. Supported modes are `view` and `explore`. |

## workbook:selectednodeid:update

This event is used to select a node ID (element ID or page ID) without using the UI.

Event structure:

JavaScript

```
{
   type: 'workbook:selectednodeid:update';
   selectedNodeId: string | null;
   nodeType: 'element' | 'page';
}
```

Event properties:

|  |  |
| --- | --- |
| `selectedNodeId` | The node ID of the element or page to select. |
| `nodeType` | The node type. Can be either `'element'` or `'page'`. |

## workbook:sharinglink:update

This event is used to make a link available that embed users can share with other users though the embed menu, embed footer, and scheduled exports email notifications. See [Configure a shareable link for an embed](/docs/configure-a-shareable-link-for-an-embed#add-sharing-functionality-to-your-application) for instructions.

> 📘
>
> ### Sigma loads the URL you supply using this event to anyone given this sharing link. Ensure that your application authenticates users before displaying the content.

Event structure:

JavaScript

```
{
  type: 'workbook:sharinglink:update';
  sharingLink: string | null;
  sharingExplorationLink?: string | null;
}
```

Event properties:

|  |  |
| --- | --- |
| `sharingLink` | The URL received by the embed user who wants to share an embedded workbook though the embed menu or footer. Once set, if the embed user schedules exports, the emails received by recipients will contain this link. |
| `sharingExplorationLink` | Optional. The URL received by the embed user who wants to share an embedded workbook though the embed menu or footer. It must include the `explorekey`, which can be obtained using the [workbook:explorekey:onchange](#workbookexplorekeyonchange) outbound event. Once set, embed users will be able to choose if they want to share the exploration or the original workbook. |

Sigma validates the strings passed in `sharingLink` and `sharingExplorationLink` using two regular expressions. Your URL must match one of these:

Text

```
^https?:\/\/(www\.)?[-a-zA-Z0-9\.~%:_\-@\/\?=&\+\*!\$]{2,50}\.[a-z]{2,10}\b([-a-zA-Z0-9\.~%:_\-@\/\?=&\+\*!\$]*)$
```

Or:

Text

```
^https?:\/\/[-a-zA-Z0-9\.~%:_\-@\/\?=&\+\*!\$]+(\\.[-a-zA-Z0-9\.~%:_\-@\/\?=&\+\*!\$]+)*(:[0-9]+)\/?(\/[.[-a-zA-Z0-9\.~%:_\-@\/\?=&\+\*!\$]+]*)*$
```

The links cannot be longer than 1000 characters. If the value does not pass validation, the sharing link is not set.

## workbook:variables:list

This event is used to list the controls and their values.

Event structure:

JavaScript

```
{  
   type: 'workbook:variables:list' 
}
```

Will return:

JavaScript

```
{
   type: 'workbook:variables:current';
   variables: variablesObject;
}
```

Event properties (returned):

|  |  |
| --- | --- |
| `variables` | A mapping of key value pairs for the controls and control values in a workbook. |

## workbook:variables:update

This event is used to update the controls and control values of a workbook without using the UI.

For more details about the expected format of control values for specific control types, see [Set control values in a URL using query string parameters](/docs/workbook-control-values-in-the-url)

Example call: `frame.contentWindow.postMessage({type: "workbook:variables:update", variables: {ua: 'south'}})`

JavaScript

```
{  
   type: 'workbook:variables:update';
   variables: variablesObject 
}
```

Event properties:

|  |  |
| --- | --- |
| `variables` | A mapping of key value pairs for the controls in a workbook. |

Updated 3 days ago

---

[Implement inbound and outbound events in embeds](/docs/inbound-and-outbound-events-in-embeds)[Outbound event reference](/docs/outbound-event-reference)

* [Table of Contents](#)
* + [workbook:bookmark:create](#workbookbookmarkcreate)
  + [workbook:bookmark:delete](#workbookbookmarkdelete)
  + [workbook:bookmark:select](#workbookbookmarkselect)
  + [workbook:bookmark:update](#workbookbookmarkupdate)
  + [workbook:fullscreen:update](#workbookfullscreenupdate)
  + [workbook:modal:toggle](#workbookmodaltoggle)
  + [workbook:mode:update](#workbookmodeupdate)
  + [workbook:selectednodeid:update](#workbookselectednodeidupdate)
  + [workbook:sharinglink:update](#workbooksharinglinkupdate)
  + [workbook:variables:list](#workbookvariableslist)
  + [workbook:variables:update](#workbookvariablesupdate)