# Set up custom homepages

# Set up custom homepages

In Sigma, you can set up custom home pages to provide the most relevant information to different users in your organization. You can set up multiple custom home pages, each for different teams, and tailor them depending on individual team needs.

For example, you might want to create a “New user onboarding” home page that recommends guides, templates and internal experts to new users. Alternatively, you can recommend the most used documents for a specific sales or engineering team in a custom home page so those team members have convenient access.

These custom home pages let you embed the first page of a specific workbook as part of the Sigma home page your organization or team lands on. As they are embedded workbooks, they allow you to leverage all workbook elements, including charts, images, videos, text, links, KPIs and more.

This document covers how to set up custom home pages and how to change existing home page configurations.

![Image shows an example custom home page embedded in the Sigma Home Page, showing example team updates, top workbooks, popular metrics](https://files.readme.io/ad86f997bcea48748809b2238702d0dbf6715ee1e68256eb5ceec02a44ea6fec-customhomepagexample.png)

## System and user requirements

* You must be assigned the Admin [account type](/docs/create-and-manage-account-types) to enable and assign home pages.
* If you want different home pages for different groups of users, ensure you have created a [Sigma team](/docs/manage-teams) for them.
* The workbook you want to set as a custom home page must be shared with the intended users (users must have at least **Can view** workbook permission).

> 🚧
>
> ### If you use OAuth as an authentication method for your Sigma organization, users experience access errors when when their OAuth tokens expire, which can happen if they stay signed into Sigma for a long time.
>
> To avoid this scenario, configure any workbook you use on a custom homepage to run with service account credentials. See [Run a workbook with service account credentials](/docs/run-a-workbook-with-service-account-credentials).

## Set up a custom home page

To set up and a custom home page:

1. Go to **Administration** > **Account** > **General Settings**.
2. In the **Custom Home Pages** section, select **Enable**.
3. Click **Assign Attribute**.
4. Search for and select the user or team you want to set the custom home page for.

   * If you want to use the same home page for the entire organization, search for and select **All members of your Sigma organization**.
5. From the Assigned Value menu, search for and select the workbook you want to use for your custom home page.

   Select **Assign**.
6. (Optional) If you want a different home page for different teams, repeat Steps 5 and 6 for each team. If a team already has a custom home page set up, it does not show up in the dropdown list of available teams.

## Edit or remove a custom home page assignment

To edit or remove a custom home page assignment:

1. Go to **Administration** > **Account** > **General Settings**.
2. In the **Custom Home Pages** section, select **Edit**. The User Attributes page opens, set to the `home_page` attribute.
3. From the assignment you want to edit, click ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More**.

   * To change the home page assignment, select **Edit value**.
   * To delete the home page assignment, select **Unassign**.

## Edit custom home page priority

If you have users who belong to multiple teams, you can decide which home page listing takes priority and reorder them accordingly:

1. Go to **Administration** > **Account** > **General Settings**.
2. Under **Teams Assigned**, drag and drop the listings to change their priority. Sigma shows the higher priority assignment's workbook to the users.

   For example, you may have a home page for one team and another for all other users in your organization. Put the team in the first position, so they will see their assigned workbook. Users outside that team will see the workbook assigned to **All Members**.

![Example home page assignment priority list, with the "Accounting" team being assigned a higher priority page than the one set for all other members. ](https://files.readme.io/52c200008e432d0e0669b6d2a96e892a809f4d7aafc099e997e6f37c829aae1b-homepage_assignment_example.png)

Updated 3 days ago

---

Related resources

* [Get started with workbook templates](/docs/get-started-with-workbook-templates)
* [Folder and Document Permissions](/docs/folder-and-document-permissions)
* [Workbooks overview](/docs/workbooks-overview)

* [Table of Contents](#)
* + [System and user requirements](#system-and-user-requirements)
  + [Set up a custom home page](#set-up-a-custom-home-page)
  + [Edit or remove a custom home page assignment](#edit-or-remove-a-custom-home-page-assignment)
  + [Edit custom home page priority](#edit-custom-home-page-priority)