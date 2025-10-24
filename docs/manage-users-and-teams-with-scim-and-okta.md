# Manage users and teams with SCIM and Okta

# Manage users and teams with SCIM and Okta

Configuring SCIM for your Sigma organization will allow you to centralize management of users and teams through Okta. This guide provides the steps required to configure Okta Provisioning for Sigma Computing.

## Requirements

* You must be an organization Admin in Sigma to initiate provisioning.
* Your Sigma organization should already be authenticated with Okta using SAML; see [Manage authentication](/docs/manage-authentication).
* This feature does not work with Password or "SAML or password" authentication.

## Understanding SCIM

### What is SCIM?

The "System for Cross-domain Identity Management", better known by its acronym SCIM, is a standard for the automation of user and group provisioning between two services.

In this case, the two services are Okta and Sigma.

### SCIM with Sigma and Okta

Configuring SCIM for your organization allows you to create and manage users and groups in Okta and automatically push them to your Sigma organization as users and teams.

Once SCIM provisioning is enabled for both services, all management of users and teams must be done in Okta. These are visible in Sigma, but not editable.

### SCIM with SAML

Before you can configure SCIM for your organization, you will need to enable either SAML authentication in Okta and Sigma.

SAML allows Single Sign On (SSO) and management of users. However, syncing new users and updates between Okta and Sigma requires the user to log in to Sigma. When you add SCIM to your SAML configuration, you will gain the ability to manage Sigma teams from Okta, and both user and group/team data in Okta will automatically be pushed to your Sigma organization, regardless of user login.

## Features

The following provisioning features are supported:

**Push New Users**

* New users added to the Okta app are automatically added as members in Sigma. If a Sigma [account type](/docs/create-and-manage-account-types) isn't specified in Okta, the default Lite account type is assigned.

**Push User Profile Updates**

* Updates made to the user's name ('given name' and 'family name') in their Okta profile will automatically be pushed to Sigma.
* Updates made to a user's 'user type' (via that application Assignment page) will automatically be pushed to Sigma.

**Deactivate Users**

* Deactivating a user through Okta will deactivate the user in Sigma.
* Note: The user's profile information will be maintained as an inactive user.
* Note: Ownership of any documents created by the user will be transferred to the Admin performing the deactivation. Any documents located in the user’s My Documents folder will automatically be transferred to a folder in the Admin’s My Documents.

**Reactivate Users**

* Sigma user accounts can be reactivated by reactivating the corresponding account in Okta.
* Reactivated users will automatically regain their Sigma team memberships, if they were added to Sigma via an Okta group.

**Push Groups / Teams**

* Groups created in Okta will be created as Teams in Sigma.

**Push Group / Team Updates**

* Updates made to a group (group name and members) in Okta will be pushed to the corresponding team in Sigma.

**Deactivate Groups / Teams**

* Deactivating a group in Okta will deactivate the corresponding team in Sigma.
* Note: Any documents located in the team's workspace folder will automatically be transferred to the My Documents folder of the Admin performing the deletion.

## Transition to SCIM

Are you considering transitioning to SCIM after already creating users and teams in Sigma? Have you already created users with SAML authentication but are new to SCIM provisioning?  This section will discuss what to expect when you transition to SCIM.

### Can I edit users and teams in Sigma?

All management of users and teams must be done through your IdP. While not directly editable in Sigma, both will be displayed in your Sigma Admin Portal.

### What happens to my existing users?

This depends on where your users were created: in Sigma’s Admin Portal vs in Okta with SAML. Both scenarios are listed below.

#### If your pre-SCIM users were created in Sigma’s Admin Portal:

Existing users will remain in Sigma. However, they will no longer be editable through the Sigma Admin Portal.

**Users**: Okta allows you to link to an existing user with the same email address in Sigma. No work will be lost, and Admin management of that user can then be maintained through your IdP. Alternatively, you may be able to import users from Sigma into your IdP.

**User Account Types**: If you switch management of a user originally created in Sigma over to your IdP, Sigma will automatically respect the account type defined in the IdP, regardless of what was originally set in Sigma.

#### If your pre-SCIM users were created in Okta with SAML:

Okta requires that any users already assigned to the app be removed and re-added when provisioning is switched on for an existing application. This process will not result in the loss of any user work in Sigma.

We recommend the following process for handling this situation:

1. **Select an off-hours time slot in which you can conduct the switch.**
   During this time, your users will be temporarily removed from the application and subsequently will not be able to log into Sigma.
2. **Create Okta groups for your users** prior to removing them from your application.
   This is not required; users can be added individually. However, bundling users into groups is recommended for two reasons:
   (1)  If you have a large user base, re-assigning your temporarily removed users in groups will reduce the period of time that your users are locked out of their Sigma accounts.
   (2)  These user groups can be repurposed when [you](/docs/manage-users-and-teams-with-scim-and-okta) [push Okta groups to Sigma to create teams](/docs/manage-users-and-teams-with-scim-and-okta).
3. **Un-assign all users from your Sigma application in Okta.**
   This can be done from the Assignments tab. Be sure to un-assign individuals and groups.
4. [Turn on provisioning.](/docs/manage-users-and-teams-with-scim-and-okta#enable-scim-provisioning)
5. Re-[assign all users](/docs/manage-users-and-teams-with-scim-and-okta#add-users-and-assign-account-types) to your application.
6. [Push groups to create teams](/docs/manage-users-and-teams-with-scim-and-okta#push-groups--teams).

### What will happen to my teams previously created in Sigma?

Existing teams will remain in Sigma, but you can't edit them in Sigma.

Okta allows you to link a group in your application to an existing team in Sigma. No work will be lost, and Admin management of that group/team can then be maintained through Okta. When the link is created, the team's membership will automatically be updated to reflect membership of the linked Okta group.

## Step-­by-­Step Configuration Instructions

### [Prerequisite] Set Up Authentication

If you have not already, connect your Okta instance to Sigma using SAML for authentication; see [Single Sign-On with SAML](/docs/single-sign-on-with-saml).

### Enable SCIM Provisioning

#### In Sigma:

1. Log in to Sigma as an organization Admin.
2. Navigate to your Sigma Admin Portal.
3. In the left panel, click **Authentication** to open your organization’s Authentication page.
   **Note**: If you have not yet configured SAML, please do so now using the "SAML or password" authentication method; see [Single Sign-On with SAML](/docs/single-sign-on-with-saml).
4. If your authentication method is set to "SAML or Password", please change it to SAML only.
5. Click the **Setup** button under **Role and Team Provisioning** to open the Provisioning modal.
   **Note**: This section is visible if your Authentication method is SAML (not SAML or Password).
   ![](https://files.readme.io/0ab3a45-1.png)
6. Review the notes provided on the getting started section of the Provisioning modal. Check the confirmation box, and click **Next** to continue.
7. You will now be asked to create a token to authenticate your integration with Okta. Enter a **token name**. Then click **Next**.
   ![](https://files.readme.io/1ce1b91-2.png)
8. Sigma provides you with a **Bearer Token**. Copy and store it in a secure location. It will be needed to complete your integration.
   **Note**: If you are configuring provisioning in an Okta Sigma app created prior to February 3, 2021, you will also need the Directory Base URL.
   ![](https://files.readme.io/6160fbe-3.png)
9. Click **Done**.
   **Next Steps**: Enable SCIM provisioning **in Okta**.

#### In Okta:

The following instructions support SCIM enablement for Sigma applications created via Okta's marketplace\*\*.\*\* **Note**: These instructions only apply to applications created AFTER February 3, 2021. To enable SCIM and Provisioning for older applications follow [instructions for SCIM for Pre-2021 applications](/docs/manage-users-and-teams-with-scim-and-okta#instructions-for-scim-for-pre--feb-3-2021-applications).

1. Open your Sigma application in Okta.
2. Open the application’s **Provisioning** tab.
3. Click **Configure API Integration**.
   ![](https://files.readme.io/75eea31-4.png)
4. Check **Enable API Integration**.
5. Under **API Token**, enter the **Bearer Token** that you received when setting up provisioning in Sigma’s Admin Portal.
6. Click **Test API Credentials** to verify your token.
   ![](https://files.readme.io/36fbf04-5.png)
7. After passing the configuration test, click **Save.**
8. You now see **Provisioning to App** settings. Click **Edit** and check the **Enable** options next to **Create Users**,**Update User Attributes**, and **Deactivate Users**.
   ![](https://files.readme.io/3298992-6.png)
9. Click **Save**.
   **Next Steps**: add users and add teams.

#### Instructions for SCIM for Pre- Feb 3, 2021 applications:

1. Open your Sigma application in Okta.
2. Open the application’s **General** tab.
3. Click **Edit**.
4. Under **Provisioning**, select **SCIM**.
5. Click **Save**.
6. Open the application’s **Provisioning** tab.
7. Click **Edit**.
8. Under **SCIM connector base URL**, enter the **Directory Base URL** that you received when setting up provisioning in Sigma’s Admin Portal.Note: This value can also be found on your S**igma Admin Portal's Authentication** page, under the header **Role and Team Provisioning**.
9. Under **Unique identifier field for users**, enter ‘userName’.
10. Check all four checkboxes beside **Supported provisioning actions**.
11. Under **Authentication Mode**, select ‘HTTP Header’.
12. Under **HTTP HEADER** > **Authorization**, enter the **Bearer Token** that you received when you configured provisioning in Sigma’s Admin Portal.
13. Click **Test Connector Configuration** to test your configuration\*\*.\*\*
14. After passing the configuration test, click **Save**.
15. You now see **Provisioning to App** settings. Click **Edit** and check the **Enable** options next to **Create Users**, **Update User Attributes**, and **Deactivate Users**.
16. Click **Save**.
    **Next Steps**: add users and add teams.

## Add Users and Assign Account Types

### Add Users Individually

Follow the steps below to add individual users. If a user has a custom account type, or an user type in Okta that doesn't directly map to Sigma, see [Use Custom Account Types with your IdP](/docs/use-custom-account-types-with-your-idp).

1. Open your Okta Admin console.
2. Open your Sigma application.
3. Go to the **Assignments** tab.
4. Click **Assign** > **Assign to People.**
5. Select the user(s) you would like to add to Sigma.
6. Use their email address as the **User Name** value.
7. Confirm that **Given name** and **Family name** are both defined.
   **Note**: These values are pulled directly from the user’s Okta profile.
8. Select a **User Type**.
   ![](https://files.readme.io/45b76b6-7.png)

> 🚧
>
> ### The user type attribute is case-sensitive. When configuring default account types (Admin, Lite, Essential, Pro), the value indicated should be lower case (e.g. "essential"). Other account type configurations are also case-sensitive, and the value set in your IdP must match the value in Sigma exactly, or errors may occur when trying to provision users.

9. Save your changes. They are sent from Okta to Sigma automatically.

Provisioning users and groups may take a few moments. To check on provisioning status from Okta, open your Provisioning activity log under [Reports](https://help.okta.com/en/prod/Content/Topics/Reports/Reports.htm). You can also check the People page in your Sigma Admin Portal to confirm that your new user(s) have been added and assigned the appropriate account type.

#### **Errors**

If you encounter the error below, remove all existing user types in Okta. Then add the user types in Okta again, mirroring the [account types](/docs/user-account-types) found in Sigma.

```
Error while trying to push profile update for {email address}: Bad Request. Errors reported by remote server: Request is malformed: Error: Expecting string at 0.1.userType but instead got: null.
```

### Add Users by Group

Follow the instructions below to add users to Sigma in bulk. The process adds users and assigns roles; it does not trigger [team creation](/docs/manage-users-and-teams-with-scim-and-okta#push-groups--teams).

1. Open your Okta Admin console.
2. If needed, update your user group(s) under **Directory > Groups**.
3. Go to **Applications**, and open your Sigma application.
4. Go to the **Assignments** tab.
5. Click **Assign** > **Assign to Groups** to view your group list.
6. Locate the group that contains the users you want to add to Sigma, and click **Assign**.
7. Select a **User Type**. This user type is assigned to all users in the group.
   **Note**: Any users previously assigned a role individually will keep their existing user role rather than inheriting their group assigned role.
   ![](https://files.readme.io/31c7387-8.png)
8. Save your changes. They will be sent from Okta to Sigma automatically.
   **Note**: Provisioning users and groups may take a few moments. To check on provisioning status from Okta, open your ***Provisioning activity*** log under [**Reports**](https://help.okta.com/en/prod/Content/Topics/Reports/Reports.htm). You can also check the **People** page in your Sigma Admin Portal to confirm that your new user(s) have been added and assigned the appropriate account type.

## Push Groups / Teams

[Groups](https://help.okta.com/en/prod/Content/Topics/users-groups-profiles/usgp-groups-main.htm) in Okta are equivalent to teams in Sigma. Once you configure provisioning in Okta, you can't create new teams directly in the Sigma Admin Portal - all teams must be created as groups in Okta and pushed to Sigma.

Teams created in Sigma prior to setting up provisioning remain accessible (but not editable) from your Sigma Admin Portal. You may choose to transition management of these teams to Okta by selecting the **Link Group** push option listed in the instructions below.

1. Open your Okta Admin console.
2. If needed, update your user group(s) under **Directory > Groups**.
3. If any users in the group are not yet assigned to Sigma, please add them now. The quickest way to add new users is [by group](/docs/manage-users-and-teams-with-scim-and-okta#add-users-by-group); however, you can also [add users individually](/docs/manage-users-and-teams-with-scim-and-okta#add-users-individually).
4. Go to **Applications**, and open your Sigma application.
5. Open the **Push Groups** tab.
6. Click the **Push Groups** button. Then select **Find Groups by name** from the menu.
   ![](https://files.readme.io/ed6c4b0-9.png)
7. Search for and select your group.
8. Select your group **push option**.
   When you select a group, Okta checks if a team with the same name exists in Sigma.

* If no group exists, it will suggest a **Create Group** push option.
* If a team already exists, you will be directed to use the **Link Group** option.
* You may also choose to use the **Link Group** option to link a group to a existing
  ![](https://files.readme.io/741c20f-10.png)
* Click **Save**.
* From the push groups list, you can see the **push status** of each group. Once marked **Active**, the group will appear as a team in Sigma.
  ![](https://files.readme.io/0efd3c7-11.png)
  ***Note**: Provisioning users and groups may take a few moments. To check on provisioning status from Okta, open your* ***Provisioning activity*** *log under* [***Reports***](https://help.okta.com/en/prod/Content/Topics/Reports/Reports.htm)*. You can also check the* ***Teams*** *page in your Sigma Admin Portal to confirm that your team has been created or linked.**Note:** To immediately push changes to a group at any time, select the Push now option from the group’s* ***Push Status*** *menu.*

### Push external embed users with SCIM

You can use Okta (or other IdP) to push and sync both internal and embed using SCIM through a custom user profile attribute in your IdP. This enables you to maintain separation of embed and internal users, while still managing them under the same IdP. Your internal users can access content from the native Sigma application or a Sigma embed, while your embed users can only access content from a Sigma embed. You must:

* Configure Sigma authentication as SAML only.
* Set up the web application hosting Sigma embed to leverage the same IdP.
* Disable automatic embed user generation.
  + Generate JWTs with the `sub` claim only.

The following is a example using Okta to add a [custom user profile attribute](https://help.okta.com/oie/en-us/content/topics/users-groups-profiles/usgp-add-custom-attribute.htm). To configure your user profile attributes:

1. In your Okta Admin Console access the **Apps** section of the **Profile Editor** page.
2. Select the user profile you want to apply a custom attribute for.
3. Configure these values on the custom attribute to differentiate internal and embed user:

   | Field | Description |
   | --- | --- |
   | Display name | UserKind or User Kind. It's recommended that you use this as a naming convention, as it matches the fields in the Sigma API. |
   | External namespace | Use this schema extension for embed users `urn:sigma:scim:schemas:extension:2.0:User` |
   | Enum | Select to this checkbox to display and add attribute members. |
   | Attribute members | Add your display names and values. Sigma expects these values to be: * `internal` * `embed` * `guest` * `external` |
   | Attribute members | Select the **Personal** option |
4. Save the attribute to return to the **Profile Editor** page. Select the **Mappings** option.
5. Select the new custom attribute from the drop down menu.
6. Select the **Apply** mapping on user create and update option from the green arrow drop down menu to apply the new custom attribute to the.
7. Click **Save Mappings**.

For more information on applying new or custom account types, see [Adding New Custom Account Types to Okta Using SCIM](https://community.sigmacomputing.com/t/adding-new-custom-sigma-account-types-to-okta-using-scim/5856).

## Troubleshooting Tips & FAQ

Please reach out to Sigma Support with any questions during your configuration process.

#### (1) I added a new user to my Sigma application, but their account has not shown up in Sigma. What should I do?

* Was the user’s account added to Okta before you set up provisioning? If so, you will need to un-assign and re-assign the user to the application.
* Provisioning users and groups may take a few moments. To check on provisioning status from Okta, open your **Provisioning activity** log under [**Reports**](https://help.okta.com/en/prod/Content/Topics/Reports/Reports.htm).
* In Okta, check for an error next to the user in the people’s list under the Assignments tab in your Sigma application.
* Does the user have a first name and last name listed in their Okta Profile?

#### (2) My Sigma organization has existing users and teams that were previously created through the Sigma Admin Portal. Will these be affected when I set up provisioning with Okta?

* No. Existing users and teams will remain in Sigma; however, they will no longer be editable through the Sigma Admin Portal.
* A user in Okta can be linked to an existing user with the same email address in Sigma. No work will be lost, and Admin management of that user will now be maintained through Okta.
* You may choose to link a group in Okta to an existing team in Sigma. No work will be lost, and Admin management of that group/team will now be maintained through Okta.

#### (3) My Sigma organization has existing users and teams that were previously created through the Sigma Admin Portal but are not part of my Okta organization. What options do I have?

* Option 1: Define the corresponding users and groups in Okta before turning on provisioning, so that Okta can link them together.
* Option 2: You can use Okta’s import feature. In the **Import** tab, click on **Import Now**. This will scan for existing users and groups that are not defined in Okta but are present in Sigma. When Okta is done scanning, it will present a list of users that it found in Sigma but not in Okta. For each user that it found, you can decide to create a new user in Okta, to link to an existing user in Okta or to ignore the user. It is suggested that you ignore the scheduler user that Sigma creates as part of your Sigma organization ([[email protected]](/cdn-cgi/l/email-protection#601303080504150c05124d120f020f14201309070d01030f0d101514090e074e030f0d)). Refer to Okta’s documentation about [Import users](https://help.okta.com/en/prod/Content/Topics/users-groups-profiles/usgp-import-users-main.htm) for more information. If you choose this option, check [Known Issues](https://docs.google.com/document/d/1Na1BUup1lbLEgaPD0c1CUT7eLS56bRDjzqm5p37GYBk/edit#heading=h.rhesbrw3gnh2).

#### (4) I assigned users to my Sigma application in Okta prior to turning on provisioning. Their accounts are not appearing in Sigma. What should I do?

* Try un-assigning and reassigning these users to your Okta Sigma application.

#### (5) The Admin who originally set up our provisioning has left or taken on a new role (account deactivated, unassigned, or user type changed). Now we’re hitting errors when attempting to push data from Okta to Sigma. What happened?

* Provisioning is associated with the Sigma Admin who originally [set up provisioning in Sigma](/docs/manage-users-and-teams-with-scim-and-okta#enable-scim-provisioning). If you wish to remove or update this user’s account type, **you will also need to remove and re-enable provisioning in Sigma with a new Admin user**. This will generate a new bearer token. Provide Okta with the updated bearer token (see [enabling provisioning in Okta](/docs/manage-users-and-teams-with-scim-and-okta#in-okta)) and rerun any provisioning tasks that might have failed.

#### (6) Can I change a user’s user name?

* This action is not recommended. Changing a user’s username will result in the creation of a new account in Sigma. It **will not** update the existing user’s username.

## Limitations

* Importing groups from Sigma teams is currently unsupported. The group gets created in Okta but has no members. As a workaround, after the group is created as part of the import process which imports both users and groups, delete the group in Okta and then recreate the group with the appropriate members. Then, [push the group](/docs/manage-users-and-teams-with-scim-and-okta#push-groups--teams) into Sigma by creating a link with the corresponding team in Sigma.
* Importing users using the “link to an existing user in Okta” option is currently unsupported. As a workaround, please assign the Sigma app to the user you wish to link.

Updated 2 days ago

---

Related resources

* [Manage Users and Teams with SCIM](/docs/manage-users-and-teams-with-scim)
* [How to Configure SAML 2.0 for Sigma on GCP (Okta documentation)](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Sigma.html)
* [How to Configure SAML 2.0 for Sigma on AWS (Okta documentation)](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Sigma-AWS)
* [Using multiple identity providers for your Sigma organization (Beta)](https://help.sigmacomputing.com/docs/using-multiple-identity-providers-for-your-sigma-organization)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Understanding SCIM](#understanding-scim)
  + - [What is SCIM?](#what-is-scim)
    - [SCIM with Sigma and Okta](#scim-with-sigma-and-okta)
    - [SCIM with SAML](#scim-with-saml)
  + [Features](#features)
  + [Transition to SCIM](#transition-to-scim)
  + - [Can I edit users and teams in Sigma?](#can-i-edit-users-and-teams-in-sigma)
    - [What happens to my existing users?](#what-happens-to-my-existing-users)
    - [What will happen to my teams previously created in Sigma?](#what-will-happen-to-my-teams-previously-created-in-sigma)
  + [Step-­by-­Step Configuration Instructions](#step-by-step-configuration-instructions)
  + - [[Prerequisite] Set Up Authentication](#prerequisite-set-up-authentication)
    - [Enable SCIM Provisioning](#enable-scim-provisioning)
  + [Add Users and Assign Account Types](#add-users-and-assign-account-types)
  + - [Add Users Individually](#add-users-individually)
    - [Add Users by Group](#add-users-by-group)
  + [Push Groups / Teams](#push-groups--teams)
  + - [Push external embed users with SCIM](#push-external-embed-users-with-scim)
  + [Troubleshooting Tips & FAQ](#troubleshooting-tips--faq)
  + [Limitations](#limitations)