# Restrict access to Sigma by IP address

# Restrict access to Sigma by IP address

You can restrict access to Sigma and the Sigma API for your organization by adding IP addresses to an allowlist. When you enable the allowlist and add IP addresses or IP address ranges using CIDR notation, only users from allowed IP addresses can successfully log in or make requests.

## Requirements

You must be assigned the **Admin** account type.

## Considerations

* Sigma checks for a valid IP address at the login and refresh token endpoints.
* If you use a proxy server or VPN to access the internet, talk to your network team before adding IP addresses.
* Sigma does not allow you to save changes that would remove your own IP address from the allowlist. This measure prevents users from locking themselves out.

## Add IP addresses to the allowlist

To restrict access to Sigma, add IP addresses to an allowlist:

1. Open the Admin Portal by selecting **Administration** in the user menu at the top right of your screen.
2. In the left panel, select **Authentication**.
3. In the **IP allowlist** section, turn the **Restrict** toggle on to enable the allowlist.
4. Select **Enable** to confirm that you want to start using the allowlist.

   > 📘
   >
   > ### By default, the allowlist includes all IPv4 and IPv6 accesses with the allowlist entries: `0.0.0.0/0` and `::/0`.
5. Add an IP address or range:

   1. In the **IP address** section, select **Add**.
   2. In the **Add IP** modal, add one or more IP addresses or ranges at a time:
      1. To allow the listed IP address to access the Sigma application and API for your organization, select **Both** for **Scope**. To allow access to only one or the other, select**Application** or **API**.
      2. To add one IP address or IP address range using CIDR notation to the allowlist, for **IP address or CIDR range**, enter the IP or range. Optionally add a description.
      3. To add a comma-separated or space-separated list of IP addresses or IP address ranges using CIDR notation, turn on the **Bulk add IPs** switch and enter the list in the text box.
   3. Click **Save**.
6. To add more IP addresses or ranges, select **Add**. You can add up to 200 addresses or CIDR ranges in total.
7. After you finish adding IP addresses and ranges to the allowlist, remove the default IP address and range:

   1. Search for `0` or locate the default IP address and range in the list.
   2. For each IP that you want to remove, select ![](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/Icons/more.svg) **More** > **Remove**.

The allowlist takes effect within a few minutes. Any new IP address added after enabling the allowlist also takes effect within a few minutes.

Updated 3 days ago

---

[Configure OAuth authentication for your Sigma organization](/docs/configure-oauth-authentication-for-your-sigma-organization)[Set up inactivity timeouts](/docs/set-up-inactivity-timeouts)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Considerations](#considerations)
  + [Add IP addresses to the allowlist](#add-ip-addresses-to-the-allowlist)