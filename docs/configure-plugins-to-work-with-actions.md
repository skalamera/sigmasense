# Configure plugins to work with actions

# Configure plugins to work with actions

Workbooks support actions that use plugins in two ways:

* **Plugins as trigger elements**: You can use a plugin to trigger an action in a workbook element. For example, a plugin can be used to trigger an action that updates a workbook control or chart.
* **Plugins as target elements**: You can create an action that enables a workbook element to trigger effects within a plugin. For example, an action like selecting a table cell can filter a plugin visualization.

This document covers how to edit your plugin code to work with workbook actions.

For more information on plugins as trigger elements, see [Action triggers in Intro to actions](/docs/intro-to-actions#action-triggers). For more information on plugins as target elements, see [Create actions that modify plugins](/docs/create-actions-that-modify-plugins).

## Prerequisites

* You must create a base plugin. See [Getting Started](https://github.com/sigmacomputing/plugin) for instructions.
* Ensure you have a Dev Playground set up. See [Using the development playground](https://github.com/sigmacomputing/plugin?tab=readme-ov-file#testing-your-plugin) for setup instructions.

## Configure plugins to use as trigger elements

To use a plugin to trigger an action in a workbook element, make the following changes to your plugin code. For more information on the functions used, refer to the [README in the Sigma plugins repository](https://github.com/sigmacomputing/plugin/blob/main/README.md).

1. Call `useEditorPanelConfig()` to create a list of configuration objects. `useEditorPanelConfig()` expects a list of configuration objects of the following types:
   * `type : string`, the field type, which must be `'action-trigger'` if you are using a plugin as a trigger element
   * `name : string`, the name of the action trigger you are defining
2. Access the configuration objects defined in `useEditorPanelConfig()` with the `useConfig()` function.
3. To return a function that calls the action configured within Sigma, call the `useActionTrigger()` function with the name of the configuration object defined in `useEditorPanelConfig()`. For example, if the name of your config object is `'ExampleAction'`, call `useActionTrigger(config.ExampleAction)`.
4. Program your desired action. The action must call the function returned by `useActionTrigger()`. For example, you could configure a UI button in your workbook that allows your stored function from step 3 to be called upon clicking.
5. Save and refresh your plugin. Your plugin is now compatible with actions in Sigma.
6. In your workbook, set up your desired action sequence. For more information on what effects can be triggered and how to create these actions, see [Action effects in Intro to actions](/docs/intro-to-actions#action-effects).

## Configure plugins to use as target elements

To create an action that enables a workbook element to trigger effects within a plugin, you will first need to make the following changes to your plugin code. For more information on the functions used, refer to the [README in the Sigma plugins repository](https://github.com/sigmacomputing/plugin/blob/main/README.md).

1. Call `useEditorPanelConfig()` to create a list of configuration objects. `useEditorPanelConfig()` expects a list of configuration objects of the following types:
   * `type : string`, the field type, which must be `'action-effect'` if you are using an element to trigger plugin effects
   * `name : string`, the name of the action effect you are defining
2. Access the configuration objects defined in `useEditorPanelConfig()` with the `useConfig()` function.
3. Create a function that, when called, results in your desired effect in the plugin.
4. Call `useActionEffect()`. `useActionEffect()` takes in a configuration object (defined in `useEditorPanelConfig()`) and a function (the function you created that results in your desired plugin effect). Note that `useActionEffect()` does not return anything.
5. Save and refresh your plugin. Your plugin is now compatible with actions in Sigma.
6. In your workbook, create the element you want to use to trigger an effect in your plugin.
7. Configure your desired action sequence. See [Create actions that modify plugins](/docs/create-actions-that-modify-plugins).

Updated 3 days ago

---

[Plugin examples](/docs/plugin-examples)[Administer Sigma](/docs/access-the-administration-portal)

* [Table of Contents](#)
* + [Prerequisites](#prerequisites)
  + [Configure plugins to use as trigger elements](#configure-plugins-to-use-as-trigger-elements)
  + [Configure plugins to use as target elements](#configure-plugins-to-use-as-target-elements)