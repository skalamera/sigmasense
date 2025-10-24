# Set up inactivity timeouts

# Set up inactivity timeouts

Sigma allows you to configure inactivity timeouts. These timeouts ensure users are automatically logged out after a certain length of inactivity in the product. This can help protect sensitive information and prevent unauthorized access to confidential data.

Activity in the product includes any mouse movement or keystroke input on Sigma tabs. Activity in other tabs is not registered.

## User requirements

* You must be assigned the Admin [account type](/docs/create-and-manage-account-types) to set up inactivity timeouts for your organization.

## Set up inactivity timeouts

1. Go to **Administration** > **Authentication**.
2. In **Authentication Method & Options**, select **Edit**.
3. Turn the **Enforce Inactivity Timeouts** toggle on.
4. Enter your desired time interval before users are logged out in the **Inactivity Timeout in Seconds** field. The minimum time interval you can enter is 5 minutes (300 seconds), and the maximum is 12 hours (43,200 seconds).
5. Select **Save**.

## Limitations

* Inactivity timeouts will not apply to embeds.

Updated 3 days ago

---

[Restrict access to Sigma by IP address](/docs/restrict-access-to-sigma-by-ip-address)[Third-party integrations](/docs/third-party-integrations)

* [Table of Contents](#)
* + [User requirements](#user-requirements)
  + [Set up inactivity timeouts](#set-up-inactivity-timeouts)
  + [Limitations](#limitations)