# Manage workbook localization

# Manage workbook localization

By default, Sigma only supports displaying English text. When you use localization, you can translate user-added text in your workbook into other languages. Translations are available when previewing or embedding the workbook. When you edit a workbook or view a published workbook version in Sigma, text is not translated.

An admin can also create organization-level translations that apply to all workbooks in your Sigma organization. For more information about organization-level translation files managed by your admin, see [Manage organization translation files](/docs/manage-organization-translation-files).

## Requirements

To manage workbook translations, you must be granted **Can edit** [access to the workbook](/docs/folder-and-document-permissions).

> 📘
>
> Any user with a workbook preview or embed URL and a valid locale definition can view a translated workbook.

## Supported languages and locales

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

## Current limitations

* Translations for a custom view of a workbook are not supported.
* Number and date formats are not supported.

## Create a workbook translation

To add a translation for your workbook, open the workbook settings and choose a language that matches your locale:

> 💡
>
> To translate the user interface text in your workbook, such as menu labels and modal text, add a new locale. To translate any user-added text in your workbook, such as element titles and descriptions, complete the steps to [add a translation for user-added text](#add-a-translation-for-user-added-text-in-your-workbook).

1. Open the workbook for editing.
2. In the editor panel with no elements selected, click **Workbook settings**.
3. Click **Manage locales**.
4. To add a new language, click **Add new locale** (**+**), then select a language from the dropdown menu.

## Add translations for user-added text in your workbook

Before adding translations for user-added text in your workbook, you must have one of the following:

* A locale defined [at the workbook level](#create-a-workbook-translation)
* A locale defined by an admin at the [organization level](/docs/manage-organization-translation-files)
* A custom translation [added as a language variant to the workbook](#add-a-custom-translation-for-a-language).

### Download a JSON-formatted file of user-added text

To add a translation for user-added text, first download the key-value pairs of user-added text and translations for the workbook:

1. Open the workbook for editing.
2. In the editor panel with no elements selected, click **Workbook settings**.
3. Click **Manage locales**.
4. For a locale, click **More** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg)) and select the relevant option:

| Option | What to expect | When to use |
| --- | --- | --- |
| **Download** | This option appears if no organization-level translation file exists. The resulting JSON-formatted file contains all key-value pairs for custom strings in the workbook. | Choose this option to define translations for your user-added text when your admin has not defined any translations that apply to the entire organization. |
| **Download untranslated strings** | If an organization-level translation file exists, this option allows you to download a JSON-formatted file that contains only the key-value pairs for custom strings in the workbook that do not match keys in the organization-level translation file. Translations that exist in an organization-level translation file are omitted. Keys that are not translated in the organization-level file are shown with either the English values (if no custom translation has been provided) or the previously defined translations for this workbook. | Choose this option when you want to avoid overwriting any values defined at the organization-level. |
| **Download all strings** | If an organization-level translation file exists, this option allows you to download a JSON-formatted file that contains all key-value pairs for custom strings in the workbook. Any keys that are translated in the organization-level file show the values defined in that file. Any keys that are not translated in an organization-level file show the translations defined for this workbook, if any, or show the English values if no translation has yet been provided. Any keys that are translated in both an organization-level file and the workbook-level file show the translations defined for this workbook. | Choose this option when you want to see all translations that apply to the custom strings in this workbook, or if you want to overwrite any organization-level translations with different translations for this workbook. |

### Add user-added text translations to your workbook

To add user-added text translations to your workbook, do the following

1. Open the downloaded file.
2. In the JSON-formatted [list of key-value pairs](https://en.wikipedia.org/wiki/JSON#Syntax), update the values to the appropriate translations.

   > 🚩
   >
   > Do not edit any of the keys.

   ![JSON-formatted key-value pairs, identifying the first string in the list as a key and the second string following a colon as the value.](https://files.readme.io/e24ef59-5.png)
3. Save your file. Do not change the filename.
4. Return to your workbook in Sigma, and open it for editing.
5. In the editor panel, select **Workbook settings** and click **Manage locales**.
6. For the locale and language for which you want to add a custom translation, click **More** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg)), then click **Upload**.
7. In the file browser, select your updated JSON-formatted file.
8. After uploading, select **More** (![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg)), then click **Preview** to open a workbook preview with translated text in a new tab.

## Update a workbook translation

To keep your custom workbook translations updated, each time you publish text changes to your workbook you must download, add or update translations, and upload a new JSON-formatted locale file.

> 💡
>
> Newly added strings appear at the bottom of the JSON-formatted file.

Follow the steps in [Add a translation for user-added text in your workbook](#add-a-translation-for-user-added-text-in-your-workbook) to update the translations.

## Add a custom translation for a language

You can maintain multiple separate translations for a given language. A custom translation for a language is also referred to as a language variant. For example, if you want to translate the strings in your workbook differently for different consumers of embedded charts, add a custom translation.

You can also inherit custom translations from organization-level files added by a Sigma admin.

To add a custom translation for a language:

1. Open the workbook for editing.
2. In the editor panel with no elements selected, click **Workbook settings**.
3. Click **Manage locales**.
4. To add a new language, click **Add new locale** (**+**).
5. In the dropdown menu, select **Add custom translations**.
6. Enter a name for your custom translation file.

   > 🚩
   >
   > To inherit a custom set of organization-level translations for this language, enter the same name as the the custom organization-level translation file. If you do not know the name, ask the admin that added the organization-level translation for the name of the file.
7. Select a **Base language** to specify the language to use for all standard Sigma interface text, such as menu labels and modal text.
8. Click **Add**.

To add custom translations for this language variant that translate the user-added text in your workbook, follow the steps in [Add a translation for user-added text in your workbook](#add-a-translation-for-user-added-text-in-your-workbook) for the language variant.

## Translations for version tagged workbooks

When you tag a workbook version, any workbook-level translations that exist when you tag the workbook are used for the tagged version. If a workbook-level translation does not exist, the latest organization-level translation file is used.

## Use markdown and dynamic text in a translation file

To support rich text in your translations, you can use Markdown and add dynamic text formula to your JSON values.

To add rich text, apply formatting to the text in your workbook, then download the user-added text strings. Based on the Markdown syntax in the user-added text strings, modify the formatting for the translated text that you add as needed. Not all user-added text supports rich text formatting.

| Displayed | Markdown syntax |
| --- | --- |
| I love **bold** text. | I love \*\*bold\*\* text. |
| *Italics* are great too. | \*Italics\* are great too. |
| Visit the [Sigma documentation](https://help.sigmacomputing.com). | Visit the [Sigma documentation](<https://help.sigmacomputing.com>). |
| * Bullet points * Make bulleted lists | \* Bullet points   \* Make bulleted lists |
| 1. Numbers 2. Make numbered lists | 1. Numbers   2. Make numbered lists |

To add a dynamic text formula to a JSON value, add the dynamic text formula in the workbook first, then retrieve the generated formula ID from the downloaded strings of user-added text. Reference the same formula ID in your translations, using the following syntax:

```
[={formula-id}]
```

## Apply locales and translations to embeds or previews

To localize a secure or public embed, or a workbook preview, use the `lng` query string parameter in the URL with the syntax `:lng=<your-locale>`. For example, `:lng=en`. Locale values are case sensitive. See [Embed URL parameters](/docs/embed-url-parameters).

Setting a locale with the `lng` query string parameter translates the standard Sigma text, such as menu labels and Sigma modal text, into the language associated with the locale. If a translation file is defined for that locale [for the workbook](#create-a-workbook-translation) or [for all workbooks in the organization](manage-organization-translation-files#add-a-translation-file), setting a locale also translates user-added text in the workbook with any translations in the file.

If you want to use a [custom translation variant of a language](#add-a-custom-translation-for-a-language), allowing you to use a custom translation instead of the base language file, specify the name of the variant with the `lng_variant` query string parameter in the URL with the syntax `:lng_variant=<variant+name>`. Use URL encoding for any special characters in the name of the language variant. The name of the custom translation is case sensitive.

### Example embed API code

To apply the French Canadian locale to a workbook:

JavaScript

```
searchParams += '&:lng=fr-ca';
```

To apply the French Canadian locale to a workbook and use a `Custom Québécois` translation file that overrides specific values in the base locale, add the `lng_variant` parameter. You must URL-encode special characters in the file name. For example:

JavaScript

```
searchParams += '&:lng=fr-ca&:lng_variant=Custom+Qu%C3%A9b%C3%A9cois';
```

To preview a workbook with the URL parameters, use the following URL format:

```
https://app.sigmacomputing.com/{organization-slug}/workbook/{workbookName}-{workbookId}?:embed=true&:lng={locale}
```

For more details about applying query string parameters for an embed, see [Embed URL parameters](/docs/embed-url-parameters-1).

> 💡
>
> A translation file is not required to apply a locale.
>
> Even if no translation file has been defined at the workbook or organization level, you can use the `lng` parameter to apply a locale to an embed or preview in order to display the standard Sigma text, such as menu labels and modal text, in a different language.
>
> For example, if your workbook is written in Japanese and the source data it displays is also in Japanese, you can set the `&:lng=ja` parameter so that the menu labels and other standard text in the workbook also display in Japanese.

Updated 3 days ago

---

[Manage workbook refresh options](/docs/workbook-refresh-options)[Manage workbook page visibility](/docs/manage-workbook-page-visibility)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Supported languages and locales](#supported-languages-and-locales)
  + [Current limitations](#current-limitations)
  + [Create a workbook translation](#create-a-workbook-translation)
  + [Add translations for user-added text in your workbook](#add-translations-for-user-added-text-in-your-workbook)
  + - [Download a JSON-formatted file of user-added text](#download-a-json-formatted-file-of-user-added-text)
    - [Add user-added text translations to your workbook](#add-user-added-text-translations-to-your-workbook)
  + [Update a workbook translation](#update-a-workbook-translation)
  + [Add a custom translation for a language](#add-a-custom-translation-for-a-language)
  + [Translations for version tagged workbooks](#translations-for-version-tagged-workbooks)
  + [Use markdown and dynamic text in a translation file](#use-markdown-and-dynamic-text-in-a-translation-file)
  + [Apply locales and translations to embeds or previews](#apply-locales-and-translations-to-embeds-or-previews)
  + - [Example embed API code](#example-embed-api-code)