# Use AI with formulas (Beta)

# Use AI with formulas (Beta)

> 🚩
>
> This documentation describes one or more public beta features that are in development. Beta features are subject to quick, iterative changes; therefore the current user experience in the Sigma service can differ from the information provided in this page.
>
> This page should not be considered official published documentation until Sigma removes this notice and the beta flag on the corresponding feature(s) in the Sigma service. For the full beta feature disclaimer, see [Beta features](/docs/sigma-product-releases#beta-features).

Sigma’s formula assistant uses AI to write new formulas, correct formula errors, and explain existing formulas applied to elements in workbooks and data models. These AI capabilities can help enhance productivity and accuracy, ensuring you get the most out of custom calculations and available functions.

This document explains how to use the formula assistant to write, correct, and explain formulas.

> 🚩
>
> The use of AI features is subject to the following [disclaimer](/docs/notice-for-enabling-ai-enabled-features-in-sigma).

## System and user requirements

The ability to use AI with formulas requires the following:

* An AI provider must be be configured for your organization. See [Configure an AI provider](/docs/configure-ai-features-for-your-organization#configure-an-ai-provider).
* If using Azure OpenAI, the [Embeddings model](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models) (`text-embedding-3-small`) must be configured in the OpenAI integration.
* You must be the workbook or data model owner or be granted **Can explore** or **Can edit** [document permission](/docs/folder-and-document-permissions).
* You must be assigned an account type with the **Use AI with formulas** permission enabled. See [Account types](/docs/license-and-account-type-overview).

## Write a formula with AI

The formula assistant evaluates your description of calculations, data references, manipulations, and other context, then suggests a formula to achieve the desired output.

1. To use the formula assistant in a workbook, open the workbook in **Explore** or **Edit** mode. To use the formula assistant in a data model, open the data model's [workbook page](/docs/intro-to-data-models#data-model-workbook-page).
2. In the element you want to update, select an existing column or create one to access the formula bar.

   > 📘
   >
   > ### For tables, pivot tables, and input tables, you can select or create a column in the **Element properties** > **Columns** list or directly within the element. For visualizations, you can accomplish this in the **Element properties** > **Columns** list or in the [underlying data table](/docs/view-underlying-data).
3. In the formula bar, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/ai-wand.svg) **Formula assistant** to open the menu, then select **Write a new formula**.

   ![Table showing an empty column. Formula assistant menu displayed with cursor over the "Write a new formula" option.](https://files.readme.io/95c5622-image.png)
4. In the **AI write formula** modal, generate and apply a formula suggestion:

   1. In the **Description** field, describe the formula or desired output.
   2. Click **Write formula** to submit the prompt.
   3. In the **AI response** field, review the formula suggestion:

      * To generate a different formula, repeat the previous steps (4a and 4b) with a modified description.
      * To apply the suggested formula to the column, click **Use formula**.

      !["AI write formula" modal with a prompt to write a formula that calculates gross profit margin.](https://files.readme.io/7cd9179-image.png)

   The column immediately reflects the output of the applied formula.

   ![Table with column data calculated by the AI-generated formula.](https://files.readme.io/8ce0bfe-image.png)

## Correct a formula with AI

When Sigma detects a formula error, the formula assistant interprets the intent of your original formula and either suggests valid formulas or provides information about the error and how to correct it. This can be used to correct formulas in existing columns (typically indicated by `Incomplete formula`, `Invalid Query`, or `Unknown column` cell values) or to help you correct a manually entered formula when adding a new column.

1. To use the formula assistant in a workbook, open the workbook in **Explore** or **Edit** mode. To use the formula assistant in a data model, open the data model's [workbook page](/docs/intro-to-data-models#data-model-workbook-page).
2. In the element you want to update, select an existing column containing a formula error, or create a new column and manually enter a formula. If your formula contains an error, Sigma highlights the formula bar with an orange border and displays a warning icon (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/warning.svg)).

   > 📘
   >
   > ### For tables, pivot tables, and input tables, you can select or create a column in the **Element properties** > **Columns** list or directly within the element. For visualizations, you can accomplish this in the **Element properties** > **Columns** list or in the [underlying data table](/docs/view-underlying-data).
3. In the formula bar, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/ai-wand.svg) **Formula assistant** to open the menu, then select **Correct this formula**.

   ![Table showing a column with a formular error.  Formula assistant menu displayed with cursor over the "Correct this formula" option.](https://files.readme.io/b6b8d77-image.png)
4. In the **AI correct formula** modal, the formula assistant suggests valid formulas or explains how to correct the existing formula. To replace the invalid formula with a suggestion, click **Apply**.

   !["AI correct formula" modal displaying three suggested formula corrections..](https://files.readme.io/fff47f8-image.png)

   The column immediately reflects the output of the applied formula.

   ![Table with column data populated by the AI-generated formula.](https://files.readme.io/13f26a9-image.png)

## Explain a formula with AI

The formula assistant evaluates an existing formula and explains what it accomplishes. Details can include columns referenced, transformations applied to the data, and other information about the formula output.

1. To use the formula assistant in a workbook, open the workbook in **Explore** or **Edit** mode. To use the formula assistant in a data model, open the data model's [workbook page](/docs/intro-to-data-models#data-model-workbook-page).
2. In the element containing the formula you want to explain, select the applicable column to access the formula bar.

   > 📘
   >
   > ### For tables, pivot tables, and input tables, you can select a column in the **Element properties** > **Columns** list or directly within the element. For visualizations, you can accomplish this in the **Element properties** > **Columns** list or in the [underlying data table](/docs/view-underlying-data).
3. In the formula bar, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/ai-wand.svg) **Formula assistant** to open the menu, then select **Explain this formula**.

   ![Table showing a column generated by a formula. Formula assistant menu displayed with cursor over the "Explain this formula" option.](https://files.readme.io/64f38c3-image.png)
4. In the **AI explain formula** modal, the formula assistant displays the AI-generated explanation. To view an alternative explanation, repeat the previous step.

   !["AI explain formula" modal showing an AI-generated explanation of the formula.](https://files.readme.io/5351c2c-image.png)

Updated 3 days ago

---

Related resources

* [Manage external AI integrations](/docs/manage-external-ai-integrations)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Write a formula with AI](#write-a-formula-with-ai)
  + [Correct a formula with AI](#correct-a-formula-with-ai)
  + [Explain a formula with AI](#explain-a-formula-with-ai)