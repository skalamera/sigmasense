# Implement inbound and outbound events in embeds

# Implement inbound and outbound events in embeds

Build interactivity between your embedded content and the host application using the inbound and outbound events available from Sigma's JavaScript embed API. You can set up your host application to emit events that send inbound events to the Sigma embed and code a listener in your host application to respond to outbound events emitted by the Sigma embedded application.

For example, when a user clicks a button in the host application, an inbound event can change the information displayed in the embedded Sigma content.

This document introduces the inbound and outbound events that make up the JavaScript embed API and provides examples demonstrating how to use them in Sigma embeds. Because you can use a variety of methods to implement events, and you might have unique integration requirements, this document does not provide step-by-step guidance on implementing events in embeds. Instead, it highlights examples that can provide helpful context that you can leverage as you develop your own approach.

* For a list of all inbound events, see [Inbound event reference](/docs/inbound-event-reference).
* For a list of all outbound events, see [Outbound event reference](/docs/outbound-event-reference).
* For an end-to-end recipe that walks you through sending and receiving events from a host application and Sigma, see [QuickStart: Embedding 09: Events](https://quickstarts.sigmacomputing.com/guide/embedding_09_events_v3/index.html).

> 📘
>
> ### Inbound events were previously called "actions". Sigma renamed "actions" to "inbound events" to differentiate between this feature and the [workbook actions](/docs/intro-to-actions) feature.

Sigma provides a JavaScript React SDK to assist you with integrating inbound and outbound events in your host application. For details, see [Embed SDK for React](/docs/embed-sdk-for-react).

> 💡
>
> ### You can use tools like Pendo for tracking and analyzing these events. For example, see [Configure Track Events](https://support.pendo.io/hc/en-us/articles/360032294291-Configure-Track-Events) in the Pendo documentation.

## Inbound events

Inbound events are mechanisms through which the host application communicates with the Sigma embed. Essentially, they are variables or commands that Sigma processes and responds to by dynamically modifying control values.

Sigma supports two methods of communicating inbound events:

* **JavaScript**: Typically used to send data from the host application to the embedded content without refreshing the embed. This method enables a more interactive and responsive user experience.
* **URL**: Primarily used at runtime to append variable values directly to the embed URL. This method is ideal for initializing the embed with specific parameters.

Both methods offer flexibility in how events are transmitted, allowing your embedded solution to accommodate different scenarios and requirements.

For a list of all inbound events, see [Inbound event reference](/docs/inbound-event-reference)

### Example inbound event: Update controls in Sigma

The following example script demonstrates a method of communicating information from the host application to the iframe of the embedded Sigma content. It utilizes the `postMessage` method to enable communication and allows the host application to send messages directly to the iframe's `contentWindow` to specify event type and controls to update.

The target origin `https://app.sigmacomputing.com` enhances security by ensuring the message reaches the intended recipient.

JavaScript

```
// Get the Sigma iframe element from the document
const sigma_iframe = document.getElementById('sigma-iframe');  

// Post a message to the Sigma iframe's content window
sigma_iframe.contentWindow.postMessage(  
  {  
    // Specify the type of event to perform
    type: 'workbook:variables:update',  

    // Define the controls to update in Sigma, with their new values
    variables: { 'Variable1': 'value1', 'Variable 2': 'value2' },  
  },  

  // Provide the target origin for where the message should be accepted
  'https://app.sigmacomputing.com',  
);
```

> 🚧
>
> ### This example event updates control values currently displayed in the embedded content. It does not apply to hidden controls.

### Example inbound event: Change the selected element or page

The following example snippet demonstrates how to programmatically change the selected element or page within an embed. It uses the `postMessage` method to enable communication and allows the host application to send messages that specify the `workbook:selectednodeid:update` event type and ID of the node to select (the `string` placeholder value would be replaced with `null` or an actual node ID).

The target origin is provided to ensure the message is sent to the correct domain.

JavaScript

```
const sigma_iframe = document.getElementById('sigma-iframe');  
sigma_iframe.contentWindow.postMessage(  
  {  
    type: 'workbook:selectednodeid:update';  
    selectedNodeId: string | null;  
  },  
  '<https://app.sigmacomputing.com'>,  
);
```

## Outbound events and listeners

Outbound events are messages the embedded Sigma content communicates to the host application to provide updates about interactions or changes applied to the content within Sigma. JavaScript event listeners must be implemented for the host application to detect and respond to outbound events. This facilitates the interactivity between the host application and Sigma embed.

For a list of all outbound events, see [Outbound event reference](/docs/outbound-event-reference).

### Example outbound event: Basic event listener

This first example demonstrates how an event listener can be added to the window object. The listener checks for event messages sent by the Sigma embed and logs the event data.

JavaScript

```
window.addEventListener('message', function (event) {
  if (event.source === document.getElementById('sigma-iframe').contentWindow &&
      event.origin === "https://app.sigmacomputing.com") {
    // Handle the received event data
    console.log(event.data);
  }
});
```

### Example outbound event: Filter specific event messages

This second example demonstrates how to filter out unrelated event messages, for example, from React DevTools.

JavaScript

```
window.addEventListener('message', (message) => {
  // Filter out messages not related to Sigma
  if (message.data.source !== 'react-devtools-bridge') {
    console.log(message.data);
  }
});
```

Updated 3 days ago

---

Related resources

* [QuickStart: Embedding 07: Events](https://quickstarts.sigmacomputing.com/guide/embedding_07_events/index.html?index=..%2F..index#0)

* [Table of Contents](#)
* + [Inbound events](#inbound-events)
  + - [Example inbound event: Update controls in Sigma](#example-inbound-event-update-controls-in-sigma)
    - [Example inbound event: Change the selected element or page](#example-inbound-event-change-the-selected-element-or-page)
  + [Outbound events and listeners](#outbound-events-and-listeners)
  + - [Example outbound event: Basic event listener](#example-outbound-event-basic-event-listener)
    - [Example outbound event: Filter specific event messages](#example-outbound-event-filter-specific-event-messages)