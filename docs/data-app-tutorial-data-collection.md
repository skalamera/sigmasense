# Data app tutorial: Build an employee feedback survey

# Data app tutorial: Build an employee feedback survey

In this tutorial, you'll learn the fundamentals and best practices needed to efficiently build a basic data collection app. The app includes a simple employee feedback form that collects and records the following information in an input table:

* Employee sentiment
* Net promoter score (NPS) rating
* Workplace preference
* Leadership feedback
* Date of form submission

As a basic data collection app, the resulting solution writes the user input back to your data platform, but it doesn't integrate source data or feature any analytics. Both, however, can be incorporated into the data app to meet expanded objectives.

When you successfully complete this tutorial, you'll have a working data app like the one embedded below. You can submit the form and see how the data is recorded in the *Form submissions* input table.

> 📘
>
> The input table is displayed below to demonstrate how form submissions are recorded. In a real-world implementation of this data app, the input table would not be visible to form responders.

## Required tasks

To build the employee survey data app, you'll need to complete the following tasks in the order listed:

* [Task 1: Create and save a workbook](#task-1-create-and-save-a-workbook)
* [Task 2: Build an input table](#task-2-build-an-input-table)
* [Task 3: Build the form](#task-3-build-the-form)
* [Task 4: Configure interactivity](#task-4-configure-interactivity)

## Key considerations for data apps

Data apps are often built with several layers of dependencies and interconnected components, which can include a multitude of data tables, control elements, actions, etc. Maintaining referential integrity (the validity and consistency of relationships between data, elements, etc.) can become a challenge, whether you're building a simple data collection form, leveraging existing workbook content, or expanding the scope of the data app.

To prevent referential issues, it's important to implement clear, consistent naming conventions while utilizing the workbook architecture and layout elements to organize your data app components. This tutorial provides guidance to help you establish referential integrity that supports the primary objective of this data app and lays the groundwork for an expanded data app use case.

## Task 1: Create and save a workbook

Workbooks are the foundation on which data apps are built, so your first task is to create and save a new workbook.

> 💡
>
> Sigma automatically stores all unsaved/unnamed workbooks as timestamped explorations in your **Recent** page. So while it isn't essential to immediately save it with a specific name and destination, doing so can ensure you can quickly locate and identify the workbook if you need to return to it later.

1. From your Sigma **Home** page, click **Create New** and select **Workbook** from the menu.
2. The new, unsaved workbook opens as an exploration. To save it as a named workbook, click **Save as** in the document header.

   ![](https://files.readme.io/d782fcdf331d983721fbd65d6fb9fd2842bd58c924e42b16973d8c479f8c4f67-image.png)
3. In the **Save as** modal, name the workbook and choose where to save it:

   1. In the **Name** field, enter `Employee survey`.
   2. In the **Destination** section, keep the **My documents** folder selected (default).
   3. In the modal footer, click **Create folder** to add a subfolder to **My documents**, then enter `My data apps` as the subfolder name.

      > 💡
      >
      > Maintaining a designated folder for data apps can improve document management and make it easier for you to search for and locate the workbook.

      ![](https://files.readme.io/1c1dea5a28121678b9e5983c63e017152b3c315888b4c5293b67effd6e541642-image.png)
   4. Select the new *My data apps* subfolder.
   5. Click **Save**.

      ![](https://files.readme.io/3adb60b5c8bb38817758ee3cad0d38c2660877159aa6315cc5acafc24568e37e-image.png)

## Task 2: Build an input table

You're now ready to build your data app. Begin by creating an input table to record data from the form submissions.

> 💡
>
> Starting with the input table allows you to establish the table schema based on the data you want to collect. Defining the table columns, data types, and relationships gives you a clear direction to efficiently build the rest of your data app.

### 2.1 Create an input table element

The input table records form submissions as new data points that are written to your data platform.

1. In the **Add element** bar, select **Input** > **Empty**.

   ![](https://files.readme.io/3e313bde15d89807613c37a51990c83dd9cd5753eaa32306a13284b6e1a05159-image.png)
2. In the **Select source** modal, select the *Sigma Sample Database* connection, then click **Create**.

   *This is the connection that Sigma will use to write data to your data platform.*

   ![](https://files.readme.io/e49254ea5204dfc4b2c94aa06dcc03b29719eb05e428dfe0293a2b7cdc0b2cd9-image.png)
3. The workbook now displays a new input table element with a default text column. Double-click the default title ("New input table") to enable editing, then enter `Form submissions` to rename it.

   ![](https://files.readme.io/b84005e8ac448061c4850583ae30033115a84b92768738fc6b3084257e48bfd2-image.png)

### 2.2 Add columns to the input table

Each column corresponds to a data point collected through the form submissions.

> 💡
>
> Building the input table with clear structure and relevant data types ensures efficient mapping of columns to form fields when you [configure the data app interactivity](#configure-interactivity).

1. Add a column to record employee satisfaction levels:

   1. Double-click the default text column's header and enter `Sentiment` to rename it.

      *This column will record text values defined in a future task (Very satisfied, Somewhat satisfied, Neither satisfied nor dissatisfied, Somewhat dissatisfied, and Very dissatisfied).*
2. Add a column to record NPS ratings (the likelihood employees will recommend the company):

   1. In the table header, click the plus (+) icon and select **Number** from the menu.
   2. Double-click the new column's header and enter `NPS rating` to rename it.

      *This column will record number values from 0 to 10.*
3. Add a column to record employee workplace preference:

   1. In the table header, click the plus (+) icon and select **Text** from the menu.
   2. Double-click the new column's header and enter `Workplace preference` to rename it.

      *This column will record one of three text values defined in a future task (Remote, Hybrid, and In-office).*
4. Add a column to record employee feedback about leadership:

   1. In the table header, click the plus (+) icon and select **Text** from the menu.
   2. Double-click the new column's header and enter `Feedback` to rename it.

      *This column will record open-ended text input.*
5. Add a column to record the date and time of each form submission:

   1. In the table header, click the plus (+) icon and select **Date** from the menu.
   2. Double-click the new column's header and enter `Date received` to rename it.

      *This column will record a system-generated timestamp.*

Your input table should now look like the screenshot below. If you don't intend to pre-populate data directly in the input table prior to collecting form submissions, delete the default empty rows.

![](https://files.readme.io/af68918e1b88e30d5424824f8e30e3062c78530a45f6b84ea852fdc998c94a42-image.png)

## Task 3: Build the form

Next, you'll build the form by configuring UI and control elements to present the survey questions and form fields.

> 💡
>
> When configuring control elements, it's important to implement a clear, consistent naming convention. Doing so can make it easier to identify individual controls and prevent referential issues. The naming convention in this tutorial follows this format: `form-<topic>`, where topic is a single word that describes the information collected through the control.

### 3.1 Create the employee sentiment field

The employee sentiment field uses a collapsed **List value** control element that prompts employees to select one of five options from a dropdown. The employee's selection is then displayed in the collapsed field.

> 💡
>
> Using a collapsed list allows you to offer several options while taking up minimal space in the form.

1. Add a **Text** element to display the survey question:

   1. In the **Add element** bar, select **UI** > **Text**.

      ![](https://files.readme.io/d6fb54594a63488d5601c4a774e5bb9433c61214a6aab8f33e8167425e909327-image.png)
   2. In the new element, enter the following question: `Overall, how satisfied or dissatisfied are you with your current role and responsibilities?`

      ![](https://files.readme.io/ca1059126a5f1328da81535170ba02dad86be65cd6780d15d7347a3ce91e6319-image.png)
2. Add and configure a **List value** control element as the response field:

   1. In the **Add element** bar, select **Controls** > **List value**.

      ![](https://files.readme.io/0472cf776e98b89a8fa2dc0f6a1d1dd0fd7a7fb6eeced7307b27c83c322143c5-image.png)
   2. With the new element selected, open the **Properties** tab in the side panel and configure the value settings:

      1. Keep the default value source (manual list) and type (text).

         ![](https://files.readme.io/3d258028e18a6270f3b3e5d3cd80fd6f1bd2c40485a924a4de2b1f5515fb0747-image.png)
      2. In the **Values** section, toggle the **Set display values** switch to the off position, then add the following values (in the order listed) in the **Add text value** fields. When you add a value, another **Add text value** field appears below it.

         * Very satisfied
         * Somewhat satisfied
         * Neither satisfied nor dissatisfied
         * Somewhat dissatisfied
         * Very dissatisfied

         ![](https://files.readme.io/11cb29b37cec4303069a53b9f54e8e3cb3f3e3ba8549276e7ea1e769282f65fb-image.png)
      3. To ensure employees select one of the five satisfaction levels, clear the **Allow multiple selection** and **Show null option** checkboxes (both enabled by default). The only selected option should be the **Show clear button** checkbox (also enabled by default), which allows the employee to clear the control after a value is selected.

         ![](https://files.readme.io/36a5887eb90142b9437716d88e3e1f41da5c4ff03874ff179e85c535ccd88462-image.png)
      4. In the **Control ID** field, clear the default ID and replace it with `form-sentiment` to align with the established naming convention, then press `Enter` on your keyboard to save the change.

         *You'll use this ID when referencing the control value in a later step.*

         ![](https://files.readme.io/9b01790117645cfc0a89fd0919404db89d2091af80919ac50d237766720cbf4b-image.png)
   3. In the side panel, open the **Format** tab and edit the element style and label:

      1. Click the **Element style** header to expand the settings.
      2. In the **Placeholder** field, clear the default text and enter `Select an option` to display this text when a value has not been selected.

         > 💡
         >
         > Customizing the placeholder text provides employees with relevant guidance on the type of response expected.

         ![](https://files.readme.io/698498d9df548565e267493b9449491e0357c675e9c5de290881d2fc9e095d82-image.png)
      3. Click the **Label** header to expand the element settings.
      4. Clear the **Show label** checkbox to hide the label.

         ![](https://files.readme.io/53ce99860c74d11986fc9659cbcd0d995e6b3779cb00001a59ed19246e0f5b60-image.png)

   The sentiment form field should now look like the screenshot below when the dropdown is expanded:

   ![](https://files.readme.io/7922a871415761a284f1167566ec7bf5a918591942a133d5b4be403e93a29369-image.png)

### 3.2 Create the NPS rating field

The NPS rating field uses a **Slider** control element that allows employees to set their rating by sliding a handle along a track or by clicking a specific position on the track.

> 💡
>
> Using a **Slider** control element saves space and enables single-click input with intuitive visual feedback.

1. Add a **Text** element to display the survey question:

   1. In the **Add element** bar, select **UI** > **Text**.

      ![](https://files.readme.io/627af57136bd06796d6286f37b15d4909393e62d5f852af9625b3c6e4243829a-image.png)
   2. In the new element, enter the following question: `How likely are you to recommend this company as a great place to work? (0 being not at all likely and 10 being extremely likely)`

      ![](https://files.readme.io/3cccd1ca467b5ea4a7fd771365d2d45bcf025f77d8e6575129756e7467ed5b83-image.png)
2. Add and configure a **Slider** control element as the response field:

   1. In the **Add element** bar, select **Controls** > **Slider**.

      ![](https://files.readme.io/9a475dbe2ea374fd6549d7d866e0b750e27b187e19b325d0635c27e0ae42b4e1-image.png)
   2. With the new element selected, open the **Properties** tab in the side panel and configure the slider settings:

      1. Set the **Max** value to 10, and leave the default settings for **Min** (0), **Step** (1), and **Format** (Automatic).

         *The resulting slider has a range of 0 to 10 and allows employees to move the slider handle left and right at intervals of 1.*

         ![](https://files.readme.io/0325d93a4a8a61fe0de840a0a67377aa3264aa86bc5382be00e6b86d3b89da53-image.png)
      2. In the **Filter** setting select **=** from the dropdown.

         > 💡
         >
         > The slider control element isn't applied as a filter, but the setting affects how the slider is reset. When the "equal to" (=) option is selected, the slider resets to 0, which is the preferred behavior for the form.

         ![](https://files.readme.io/aada8afb7efd2277c470a334e37cacdeb0de411a76aa9c790617663eb1c2df4d-image.png)
      3. In the **Control ID** field, clear the default ID and enter `form-nps` to align with the established naming convention, then press `Enter` on your keyboard to save the change.

         *You'll use this ID when referencing the control value in a later step.*

         ![](https://files.readme.io/43751fd50cea19027ffc931451d174f9ea0049b3317db16a696482097a7b8241-image.png)
   3. In the side panel, open the **Format** tab and edit the element label:

      1. Click the **Label** header to expand the label settings.
      2. Clear the **Show label** checkbox to hide the label.

         ![](https://files.readme.io/b44b52904fff540b4ba141e8556da22f29449f489c25659f1ece3b08126829f8-image.png)

   The NPS rating form field should now look like the screenshot below:

   ![](https://files.readme.io/2ed957b8886c4315aa7a61c804f7ee814cdbde3ca55ddf414d30132294ae427b-image.png)

### 3.3 Create the workplace preference field

The workplace preference field uses a **Segmented** control element that allows employees to select one of three displayed options.

> 💡
>
> While you can use a **List value** control element for this field, a **Segmented** control element provides clear, scannable options in a compact display while enabling single-click input with intuitive visual feedback.

1. Add a **Text** element to display the survey question:

   1. In the Add element bar, select **UI** > **Text**.

      ![](https://files.readme.io/813abcaf680eadbd8cfb32fca27015e5838f5228f7710a59ec760b70d6b48e61-image.png)
   2. In the new element, enter the following question: `What work environment do you prefer?`

      ![](https://files.readme.io/c986ec2be0af44fc640f52384e6edc96a01f6bc137b239e3f8a87d4ecde0e940-image.png)
2. Add and configure a **Segmented** control as the response field:

   1. In the **Add element** bar, select **Controls** > **Segmented**.

      ![](https://files.readme.io/a1b75b5834833e9361fb981c5947196bbe863590d073ae33f5e8bd6f000de5a9-image.png)
   2. With the new element selected, open the **Properties** tab in the side panel and configure the value settings:

      1. Keep the default value source (manual list) and type (text).

         ![](https://files.readme.io/98829ba885da07da2aa646172c2bb500c7acfeea9a5682ec5e8c23e1e116f306-image.png)
      2. In the **Values** section, toggle the **Set display values** switch to the off position, then add the following values (in the order listed) in the **Add text value** fields. When you add a value, another **Add text value** field appears below it.

         * Remote
         * Hybrid
         * In-office

         ![](https://files.readme.io/b21b954a08bb0043eec39ed6d5752c3354f39ce6095eb56f375d15b70952e5b7-image.png)
      3. In the **Control ID** field, clear the default ID and enter `form-preference` to align with the established naming convention, then press `Enter` on your keyboard to save the change.

         *You'll use this ID when referencing the control value in a later step.*

         ![](https://files.readme.io/98848fea275d8598374376c5eddf629261cdd1c3be8005cb748a922d4c2283c3-image.png)
   3. In the side panel, open the **Format** tab and edit the element label:

      1. Click the **Label** header to expand the label settings.
      2. Clear the **Show label** checkbox to hide the label.

         ![](https://files.readme.io/633cdae10bc4502cb48b3a7e9aae308fe855cfa11b9ee75b20ae9bf5d35da42d-image.png)

   The workplace preference form field should now look like the screenshot below:

   ![](https://files.readme.io/ce34e4856eadcf4e84016059f578b8127619b250a047330063f2732078136036-image.png)

### 3.4 Create the feedback field

The feedback field uses a **Text area** control element that allows employees to enter open-ended comments.

> 💡
>
> While you can use a **Text input** control element for this field, a **Text area** control is more suitable for lengthier open-ended input that can be easily viewed in a larger field with customizable height and width. When the text extends beyond the text area, the employee can scroll to view additional lines of text.

1. Add a **Text** element to display the survey question:

   1. In the **Add element** bar, select **UI** > **Text**.

      ![](https://files.readme.io/7f0644e14d9d297b52c44695d41e5174512ba1962e0f74b459b3e71a7cda9c0f-image.png)
   2. In the new element, enter the following question: `What can leadership do to make your work experience more positive?`

      ![](https://files.readme.io/039233dd610ad7793d9438ea9c0e7ff7c087a1ecb59255ad68019bd5e7c6e1ae-image.png)
2. Add and configure a **Text** area control as the response field:

   1. In the **Add element** bar, select **Controls** > **Text area.**

      ![](https://files.readme.io/69f23cb302d4d1dfb6cc75b5f3a78457effe77db43cbb8fc911a8fa9d61e0b7a-image.png)
   2. With the new element selected, open the **Properties** tab in the side panel to edit the control ID.
   3. In the **Control ID** field, clear the default ID and enter `form-feedback` to align with the established naming convention, then press `Enter` on your keyboard to save the change.

      *You'll use this ID when referencing the control value in a later step*

      ![](https://files.readme.io/6a4ee43227c5ff794573ed6a16ee7b22755c1bb585be8c596f7b7aafceaa02bb-image.png)
   4. In the side panel, open the **Format** tab and edit the element style and label:

      1. Click the **Element style** header to expand the style settings.
      2. In the **Placeholder** field, enter `Share feedback to help us improve` to display this text when employee input has not been added.

         > 💡
         >
         > Customizing the placeholder text provides employees with additional context and guidance on the type of response expected.

         ![](https://files.readme.io/ed83ca1692b253136345c56af10ddd7437f1b8762998c09d3588f1fbbc849da3-image.png)
      3. Click the **Label** header to expand the label settings.
      4. Clear the **Show label** checkbox to hide the label.

         ![](https://files.readme.io/c2776d334c6bd0042e033d843e4f328bc8207ff645131077fe8bf3d7cb206655-image.png)

   The feedback form field should now look like the screenshot below. You can select and drag the handles of the **Text area** control to resize the response field:

   ![](https://files.readme.io/8db176ff005228b093dfe3a4d416e57066fd834b9d9fb62e15adf21257254d8e-image.png)

### 3.5 Create the form buttons

The form will include two buttons (*Submit* and *Clear*) on which you'll configure interactivity. The *Submit* button will enable employees to send their form entries, which are recorded in the input table. The *Clear* button will provide an easy way to reset the form fields.

1. Create the *Submit* button:

   1. In the **Add element** bar, select **UI** > **Button**.

      ![](https://files.readme.io/dca329e39d91c6e055dbb20b887dd61721c02b32258115d827636033cfec4702-image.png)
   2. With the new element selected, open the **Properties** tab in the side panel to edit the button text.
   3. In the **Text** field, clear the default text and enter `Submit`, then press `Enter` on your keyboard to save the change.

      ![](https://files.readme.io/25c3fb562135f11144b5e0138922d4e7817bd150846ef5c17d6e23bad68e200e-image.png)
   4. In the **Alignment** section, set the **Horizontal** setting to ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/align_stretch.svg) **Stretch**.

      > 💡
      >
      > Stretching the horizontal alignment of both buttons allows you to make them the same width.

      ![](https://files.readme.io/3af8b1c8339eb889ed0348a35785a6e85db172f049287f56ac8181b2a4f286c3-image.png)
2. Create the *Clear* button:

   1. In the **Add element** bar, select **UI** > **Button**.

      ![](https://files.readme.io/5a76db0c19ee2f8ce460170d3e0799c20110423a63a83f67f1619fdeb16f2fda-image.png)
   2. With the new element selected, open the **Properties** tab in the side panel to edit the button text.
   3. In the **Appearance** field, select **Outline** from the dropdown.

      > 💡
      >
      > The outline appearance indicates that the *Clear* button is secondary to the *Submit* button. This is UI/UX best practice that creates a visual hierarchy and cleaner design.

      ![](https://files.readme.io/f5b68b2cd50dba620516b9c005c1effcb1222111d80bb7fa69b275fb9d716646-image.png)
   4. In the **Text** field, clear the default text and enter `Clear`, then press `Enter` on your keyboard to save the change.

      ![](https://files.readme.io/587e845c51909a330e64d4d25801b5acd29eb007f0ddbb8aa96a7edfe00b2dfa-image.png)
   5. In the **Alignment** section, set the **Horizontal** setting to ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/align_stretch.svg) **Stretch**.

      ![](https://files.readme.io/7034b8512fe7b5aa4b737f08c6ec09e1006ad951b00e0444d9222b9e5f29fa1b-image.png)
3. Select and drag the button elements to arrange them side-by-side below the form fields.

   ![](https://files.readme.io/46c4801508288bc21584d6f7bad13f9a142ea42bb6c426a7e4758452f6228ede-image.png)

### 3.6 Create a container

The container will enclose the essential components of the form.

> 💡
>
> While containers and other layout elements are utilized primarily to customize the data app design, enclosing all of the form items in a container can also simplify the process of configuring interactivity for this data app. When actions need to apply to the entire form, you'll be able to configure a single action that references all elements in the container rather than configuring a separate action for each control element.

1. Click and drag to multi-select all UI and control elements created in the previous subtasks. Do not include the input table element.
2. In the element toolbar, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/container.svg) **Create container** to enclose the elements in a single container.

   ![](https://files.readme.io/688b5494911cc9edc5774d1a1d06cc4fe4faf53a31ac63c46021d29e7a46c65a-image.png)
3. With the container selected, you'll see the default container name (*Container 1*) in the side panel header. Double-click the header to enable editing, then enter `Form fields` to rename it.

   ![](https://files.readme.io/141c05321780ab5d90562dc8d99a2d7c8601db2fbaaa5d35c7b7a3235079ab76-image.png)

   The feedback form field should now look like the screenshot below:

   ![](https://files.readme.io/f9f788bb80c021bac37371c065a2aed38cede388f202e69c9f143b66fb4f626d-image.png)

## Task 4: Configure interactivity

With the form fields set up, you can now configure action sequences on the *Submit* and *Clear* buttons.

> 💡
>
> When configuring actions, it can be beneficial to rename individual actions and sequences. Applying more specific and descriptive names can provide clarity about the actions at first glance.

### 4.1 Configure actions on the *Submit* button

When an employee clicks the *Submit* button, the data app will first insert a new input table row based on the form entries, then it will clear the form fields to reset them to their initial states.

1. Select the *Submit* button element.
2. In the side panel, open the **Actions** tab.
3. In the default empty action sequence, click **+ Add action**.

   ![](https://files.readme.io/e409c2fa93aa467320b4f392378c9ff392289a2b89507f9fbe9312a18e8b2119-image.png)
4. In the **Action** modal, configure the first action that will insert a new row in the input table:

   1. In the **Action** field, select **Insert row** from the dropdown.
   2. In the **Into** field, select the *Form Submissions* input table you previously created.
   3. The **With values** section lists all columns from the input table and requires you to specify the source of each column's value for the inserted row.

      > 💡
      >
      > Controls can only be mapped to columns when they're compatible with the column type. For example, a **List value** control cannot be set as the source for a number column.
      >
      > If you're unable to select the required control when configuring the action, check and update the column type or control type as needed.

      Configure the sources for each column as follows:

      1. For the *Sentiment* column, select **Control** from the first dropdown, then select the *Form Sentiment* (*form-sentiment*) control from the second dropdown.

         > 💡
         >
         > If the column type (text) and control type (List value) are correctly applied and you're still unable to select the form-sentiment control, go to the control's properties and ensure the **Allow multiple selection** checkbox is cleared.
      2. For the *NPS rating* column, select **Control** from the first dropdown, then select the *Form Nps* (*form-nps*) control from the second dropdown.
      3. For the *Workplace preference* column, select **Control** from the first dropdown, then select the *Form Preference* (*form-preference*) control from the second dropdown.
      4. For the *Feedback* column, select **Control** from the first dropdown, then select the *Form Feedback* (*form-feedback*) control from the second dropdown.
      5. For the *Date received* column, select **Formula** from the first dropdown, then click the secondary field to open the formula bar. Enter the [Now()](/docs/now) function, then click the checkmark or press `Enter` on your keyboard to save the formula.

         *This formula produces a system-generated timestamp at the time the employee clicks the button to submit the form.*

      ![](https://files.readme.io/1df8c0a9fce8caf9d8ab100ab36ff6e82be41071572ba04abd65096479e7365b-image.png)
5. In the action sequence, double-click the action, then enter `Record form submission` to rename it.

   ![](https://files.readme.io/199921ed7900e2b44ab993e2d7c55645607ace764be138d44df6eec342d39f6a-image.png)
6. In the same action sequence, click **+ Add action** to add a second action.

   ![](https://files.readme.io/dfd248e7cf2dd2ba4c34846963b28e119431fdb6f617b36bf66b32a0ae476121-image.png)
7. In the **Action** modal, configure the second action that will clear all the controls configured as form fields:

   1. In the **Action** field, select **Clear control** from the dropdown.
   2. In the **Apply to** field, select **Container** from the dropdown.
   3. In the **Container** field, select the *Form fields* container from the dropdown.

      ![](https://files.readme.io/105cc1de1c8bce216b0b8bc3f8718bb3405c28b3377f03458f99f9fc2d3fd033-image.png)
8. In the action sequence, double-click the second action, then enter `Reset form` to rename it.

   ![](https://files.readme.io/bdb904fd8f5ed41035ceb605ecfe6d67de662538f0309bbf558232e2f8e92964-image.png)

### 4.1 Configure actions on the *Clear* button

When an employee clicks the *Clear* button, the data app will clear the form fields.

1. Select the *Clear* button element.
2. In the side panel, open the **Actions** tab.
3. In the default empty action sequence, click **+ Add action**.

   ![](https://files.readme.io/f0b47581fce0e5cab1b29996168132788c43f283f66ae0f2b46cfcb38c74af1f-image.png)
4. In the **Action** modal, configure the action that will clear all the controls configured as form fields:

   1. In the **Action** field, select **Clear control** from the dropdown.
   2. In the **Apply to** field, select **Container** from the dropdown.
   3. In the **Container** field, select the *Form fields* container from the dropdown.

      ![](https://files.readme.io/d402ebf4bd33f8b015c1d6e4f0a255881ffad220c5325dd1b0a0856487477b58-image.png)
5. In the action sequence, double-click the second action, then enter `Reset form` to rename it.

   ![](https://files.readme.io/48866d26910b746ab4b7199a2c3b5e7c17641992c813f00d27ed6e4ff829ced4-image.png)

   The form should now be interactive! Test your data app by completing the form fields and ensuring the entries and submission timestamp are accurately recorded in the input table.

## Next steps

* Customize the design: Before deploying your data app, customize styles and add UI components to refine the presentation and comply with company brand guidelines. See [Design layout](/docs/design-layout), [UI elements](/docs/ui-elements) and [Workbook formatting](/docs/workbook-elements).
* Organize elements on pages: Create separate pages for the form and input table, then hide the page containing the input table to ensure it's not visible to employees granted access to the workbook. This also enables you to only display the form when embedding it outside of the workbook. See [Manage workbook page visibility](/docs/manage-workbook-page-visibility).
* Edit data entry permission: Update the input table to only allow edits in the published version. This enables the input table to record form submissions from a view of the published workbook or in an embed. See [Set data entry permission](/docs/configure-data-governance-options-in-input-tables#set-data-entry-permission).
* Create a secure embed: Embed the form in another application to present it to employees outside of the workbook. See [Create a secure embed](/docs/create-a-secure-embed).

Updated 3 days ago

---

[About Sigma data apps](/docs/data-apps)[Add or collect data](/docs/add-or-collect-data)

* [Table of Contents](#)
* + [Required tasks](#required-tasks)
  + [Key considerations for data apps](#key-considerations-for-data-apps)
  + [Task 1: Create and save a workbook](#task-1-create-and-save-a-workbook)
  + [Task 2: Build an input table](#task-2-build-an-input-table)
  + - [2.1 Create an input table element](#21-create-an-input-table-element)
    - [2.2 Add columns to the input table](#22-add-columns-to-the-input-table)
  + [Task 3: Build the form](#task-3-build-the-form)
  + - [3.1 Create the employee sentiment field](#31-create-the-employee-sentiment-field)
    - [3.2 Create the NPS rating field](#32-create-the-nps-rating-field)
    - [3.3 Create the workplace preference field](#33-create-the-workplace-preference-field)
    - [3.4 Create the feedback field](#34-create-the-feedback-field)
    - [3.5 Create the form buttons](#35-create-the-form-buttons)
    - [3.6 Create a container](#36-create-a-container)
  + [Task 4: Configure interactivity](#task-4-configure-interactivity)
  + - [4.1 Configure actions on the Submit button](#41-configure-actions-on-the-submit-button)
    - [4.1 Configure actions on the Clear button](#41-configure-actions-on-the-clear-button)
  + [Next steps](#next-steps)