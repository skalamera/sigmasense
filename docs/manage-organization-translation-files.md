# Manage organization translation files

# Manage organization translation files

Creating organization translation files lets you serve the Sigma users in your organization and consumers of embedded analytics with custom workbook text in their preferred language. Custom workbook text includes any customizable workbook element titles and user-defined strings, including column names from source data.

Admins can manage organization translations by going to **Administration > Account > General Settings > Locale** or by using the API.

Organization translations are centrally managed translation files that translate commonly-used terms across all workbooks. As a result, workbook owners do not need to translate those common terms in each individual workbook.

Workbook owners can also manage translations for their workbooks on a per-workbook basis. A translated string in a workbook-level translation file takes precedence over a translation of the same string in an organization-level translation file.

For example, if you have hundreds of workbooks in your organization that use the term "Quantity" in data column names, you can upload a translation file for Spanish to specify that "Quantity" should appear as "Cantidad" for any users with their locale set to Spanish. If the owner of an individual workbook does not specify a translation for "Quantity" in their workbook-level translation file, Sigma applies the translation from the organization-level translation file and "Cantidad" will appear. If that workbook owner uploads a different translation for the term, Sigma uses the translation from the workbook-level translation file.

See [Manage workbook localization](/docs/manage-workbook-localization#update-a-workbook-translation) for details on how workbook-level and organization-level translation files interact.

> 📘
>
> ### Organization translations affect version-tagged workbooks.
>
> If an organization translation exists for a language, any version-tagged workbooks viewed in that language use the translations. If you want to control how a translation appears in a version-tagged workbook, apply a workbook-level translation file to that workbook.

## Supported languages

Sigma supports the following languages and locales:

| Language | Locale |
| --- | --- |
| Chinese (Simplified) | zh-cn |
| Chinese (Traditional) | zh-tw |
| Dutch | nl-nl |
| English (United States) | en |
| English (Australia) | en-au |
| English (Canada) | en-ca |
| English (Ireland) | en-ie |
| English (United Kingdom) | en-gb |
| French | fr |
| French (Canada) | fr-ca |
| German | de |
| Italian | it |
| Japanese | ja |
| Korean | ko-kr |
| Polish | pl |
| Portuguese | pt |
| Portuguese (Brazil) | pt-br |
| Russian | ru |
| Spanish | es |
| Spanish (Mexico) | es-mx |
| Swedish | sv-se |
| Thai | th |

## Requirements

* You must be assigned the **Admin** [account type](/docs/user-account-types).

## Add a translation file

To add a translation file, do the following:

1. Go to the **Administration** > **Account** > **General Settings** tab.
2. In the **Locale** section, click **Add** next to **Organization translations**.
3. Choose the language for which you would like to create an organization-wide translation file.

   > 📘
   >
   > ### To maintain multiple unique translation files for the same language, choose **Add custom translations**. Adding a custom translation for a language allows you to translate common strings differently for different consumers of embedded dashboards, for example.
4. Click the download icon in the **Actions** column to download the JSON-formatted file.
5. Open the file with a text editor. The default file contains an example to demonstrate the required syntax.

   JSON

   ```
   {
     "This is an example": "This is an example",
     "This is a second example": "This is a second example"
   }
   ```
6. Replace the example key-value pairs with valid JSON that represents the common phrases used in workbooks across your organization, and their translated values. For example:

   JSON

   ```
   {
      "Date": "Fecha",
      "Quantity": "Cantidad",
      "Cost": "Costs",
      "Price": "Precio",
      "Product Type": "Tipo de Producto"
   }
   ```
7. Save the json file. Do not change the file name.
8. In the **Actions** column, click the upload icon to upload the file you just edited.

The translations you provided in the file apply immediately to the corresponding locale version of any workbook in the organization that uses those phrases, provided the workbook does not already provide a translation file that contains different translations for those phrases.

To perform these steps programmatically, use the [Create organization translation file](/reference/createorgtranslation) API endpoint.

## Preview organization translations in a workbook

To preview the results of translations, go to a workbook that uses the phrases you translated.

1. Click **Edit**.
2. In the editor panel with no elements selected, click **Workbook settings**.
3. Click **Manage locales**.
4. Preview the translation:

   1. If a workbook-level translation for the language already exists, click **More** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg)), then select **Preview** to open the workbook in a new tab with that locale applied.
   2. If no translation exists at the workbook level:

      1. Click **Add new locale** (+) , then select the language.
      2. Click **More** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg)), then select **Preview** to open the workbook in a new tab with that locale applied.

## Update an organization translation file

To update an organization translation file:

1. Go to the **Administration** > **Account** > **General Settings** tab.
2. In the **Locale** section, locate the language in the **Organization translations**.
3. In the **Actions** column for the language, click **Download org translation file** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/download.svg)) to download the JSON-formatted file.
4. Open the file with a text editor.
5. Update the JSON-formatted file to edit existing key-value pairs or add new ones.
6. Save the file. Do not change the file name.
7. In the **Actions** column for the language, click **Upload org translation file** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/upload.svg)) to upload the file that you just edited.

The translations you provided in the file apply immediately to the corresponding locale of any workbook in the organization that uses those phrases. If a workbook already provides a translation file that contains different translations for those phrases, the workbook-level translations take precedence.

To update an organization translation file programmatically, use the [Update organization translation file](/reference/updateorgtranslation) API endpoint or the [Update organization translation file with variant](/reference/updateorgtranslationwithvariant) API endpoint, depending on the type of translation that you want to update.

Updated 3 days ago

---

[Manage organization locale](/docs/manage-organization-locale)[Manage assets](/docs/manage-assets)

* [Table of Contents](#)
* + [Supported languages](#supported-languages)
  + [Requirements](#requirements)
  + [Add a translation file](#add-a-translation-file)
  + [Preview organization translations in a workbook](#preview-organization-translations-in-a-workbook)
  + [Update an organization translation file](#update-an-organization-translation-file)