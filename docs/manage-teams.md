# Create and manage teams

# Create and manage teams

Teams allow you to create groups of users in Sigma that you can use to manage access to data, documents and more. When you grant access and permissions to a team, the grants apply to all members assigned to the team.

This document explains how to create, edit, and delete teams in Sigma. For information about managing team members and team admins, see [Manage team members](/docs/manage-team-members) and [Manage team admins](/docs/manage-team-admins).

> 📘
>
> ### If your organization uses an identity provider (IdP) to manage users and teams, see [Manage users and teams with SCIM](/docs/manage-users-and-teams-with-scim).

## User requirements

To create teams, you must be assigned the **Admin** [account type](/docs/user-account-types). To edit team details and delete a team, you must be assigned the **Admin** account type or be assigned **Team Admin** status.

## Create a team

1. Go to **Administration** > **Teams**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Teams**.
2. In the **Teams** page, click **Create Team**.
3. In the **New Team** page, provide the team details:

   1. In the **Team Name** field, enter a unique name to identify the team.
   2. (optional) In the **Team Description** field, enter a description about the team and its members.
   3. In the **Team Access** section, select an option to determine who can access the team:

      |  |  |
      | --- | --- |
      | **Public** | Accessible to the entire organization *(guest and embed users excluded)*.  For example, all organization users can perform the following:  * View the team and its details in the **Profile** > **Teams** > **Public teams** tab. * Grant the team permissions to folders and documents. |
      | **Private** | Accessible to team members and admins only.  For example, only team members can perform the following:  * View the team and its details in the **Profile** > **Teams** > **My teams** tab. * Grant the team permissions to folders and documents. |
   4. (optional) To create a workspace for the team and automatically grant members **Can contribute** permission, select the **Create a workspace associated with the team** checkbox.

      > 📘
      >
      > ### Teams and workspaces have a many-to-many relationship. A single team can be granted different permissions for multiple workspaces, and multiple teams can be granted different permissions for a single workspace. For example, your organization can create a workspace for each team while also maintaining quarterly workspaces shared with a select few teams.
      >
      > For more information about workspaces, see [Manage workspaces](/docs/manage-workspaces).
4. Click **Create** to save the new team.

## Edit team details

To edit details about a team, such as the description or team name, do the following:

1. Go to **Administration** > **Teams**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Teams**.
2. In the list of teams, select the team you want to edit.
3. In the team details page, click **Edit**.
4. Rename the team, update the description, or change the **Team Access** setting, then click **Save**.

To manage team membership, see [Manage team members](/docs/manage-team-members) .

## Delete teams

You can delete one or more teams from Sigma.

### Delete an individual team

1. Go to **Administration** > **Teams**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Teams**.
2. In the list of teams, select the team you want to delete.
3. In the team details page, click **Delete Team**.
4. In the **Delete Team** modal, click **Confirm** to proceed.

   Sigma permanently deletes the team from your organization.

   > 💡
   >
   > ### If a workspace was previously created in association with the team, you must delete the workspace separately. For more information, see [Manage workspaces](/docs/manage-workspaces).

### Delete teams in bulk

1. Go to **Administration** > **Teams**:

   1. In the Sigma header, click your user avatar to open the user menu.
   2. Select **Administration** to open the **Administration** portal.
   3. In the side panel, select **Teams**.
2. In the list of teams, select the checkbox associated with each team you want to delete.
3. Click **Delete** to delete the selected teams.
4. In the **Delete team** modal, click **Confirm** to proceed.

   Sigma permanently deletes the selected teams from your organization.

Updated 3 days ago

---

Related resources

* [Manage team members](/docs/manage-team-members)
* [Manage team admins](/docs/manage-team-admins)
* [Manage Users and Teams with SCIM](/docs/manage-users-and-teams-with-scim)
* [Manage Workspaces](/docs/manage-workspaces)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Create a team](#create-a-team)
  + [Edit team details](#edit-team-details)
  + [Delete teams](#delete-teams)
  + - [Delete an individual team](#delete-an-individual-team)
    - [Delete teams in bulk](#delete-teams-in-bulk)