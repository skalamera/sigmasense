# Change the account time zone

# Change the account time zone

By default, Sigma displays all date data in UTC. You can change this to display all time data according to your organization's preferred time zone using the **Account time zone** setting.

## Requirements

* To change the account time zone, you must be assigned the **Admin** [account type](/docs/user-account-types).

## Select a time zone

1. Go to the **Administration** > **Account** > **General Settings** tab.
2. In the **Time** section, click **Edit**.
3. In the **Account Timezone** dropdown, select your time zone.

> 📘
>
> If your desired time zone is not listed, contact your Account Manager or Support.

4. Click **Save**.

## Time zone change considerations

After you change the account time zone, you can expect the following:

* **Existing absolute date filters** show the date range in the new time zone. For example, after switching from `UTC` to `Americas/Los_Angeles`, an absolute period originally defined as starting at `1/1/2021 0:00:00` is displayed as starting at `12/31/2020 16:00:00`, the same time converted to PST. For a date during daylight savings time, like `7/1/2021 0:00:00`, it is displayed as `6/30/2021 17:00:00`.
* **Existing relative date filters** defined in days or less-granular units reflect the new time zone. The values for the date filters are shown the same way (e.g. 30 days ago), but the meaning changes (e.g. from midnight UTC 30 days ago to midnight Pacific Time 30 days ago).
* Date values passed in to workbook control values via the URL are parsed according to your account time zone. You can override this default behavior so that Sigma parses the date values as being in the UTC time zone by appending a Z to the timestamp in the URL. For more information, see [Workbook control values in the URL](/docs/workbook-control-values-in-the-url#date-examples).
* [Materialized datasets](/docs/materialization) do not update to the new time zone until refreshed. If you use materialized datasets, changing your account time zone might lead to temporary inconsistencies until all materializations are refreshed.
* **Data stored in time zone aware columns** is interpreted according to your account time zone and changes accordingly when you change the account time zone. For example, if you insert `1/1/2021` into a TIMESTAMP\_TZ column in Snowflake using the UTC session time zone:

  + If your account time zone is set to UTC, Sigma displays it as `1/1/2021 00:00:00`.
  + If your account time zone is set to `Americas/Los_Angeles`, the same timestamp displays as `12/31/2020 16:00:00`.

> 🚧
>
> [CSV files uploaded to Sigma](/docs/enable-csv-upload) use a time zone aware column to store time and date values. If you have previously uploaded a CSV file with a date column, it will not update to the new time zone unless the CSV is re-uploaded. Otherwise, it is converted to the same moment in absolute time for the new account time zone.

## How Sigma displays date data

Sigma displays all date data according to your organization's account time zone. This has the following consequences:

* If a column in your data platform has time zone data, Sigma converts the timestamp to your organization’s time zone while preserving the moment in time. For example, a column stating the timestamp `2025-09-10 10:00:00.000` for the `America/New_York` time zone is converted to `2025-09-10 07:00:00.000` if your Sigma organization has the `America/Los_Angeles` account time zone.
* If a column in your data platform has no time zone, Sigma displays it in your organization’s time zone, leaving the timestamp unchanged. For example, a TIMESTAMP\_NTZ column stating the timestamp `2025-09-10 00:00:00.000` preserves the timestamp as `2025-09-10 00:00:00.000` but adds your account time zone to the data.

> 💡
>
> If you need to preserve the timestamp, Sigma recommends casting the column to a data type without a time zone, such as TIMESTAMP\_NTZ, in your data platform. Alternatively, you can set your Sigma organization's time zone to match data from your data platform.

## Warehouse views time zone limitation

If the time zone of your Sigma organization and your data platform are different, creating a warehouse view from a Sigma element that includes date columns is not supported and may produce unexpected results.

Consider the following example scenario:

* A record in your data platform in a TIMESTAMP\_NTZ column has the timestamp `2025-09-28 21:00:00.000`.
* Your Sigma organization is set to the `America/New_York` time zone.
* Your data platform is set to the `America/Los_Angeles` time zone.
* You create a filter in Sigma for records on the date `2025-09-29`.

In Sigma, the record displays as `2025-09-28 21:00:00.000-4:00`. But, after creating a warehouse view, it displays as `2025-09-28 21:00:00.000-7:00` in your data platform. In both Sigma and the data platform, the filter is for the absolute time range `2025-09-29T00:00:00.000000000-04:00` to `2025-09-29T23:59:59.999000000-04:00`. In Sigma, this record does not meet the filter criteria. In the data platform, it does. To resolve this issue, set the Sigma account time zone to match your data platform.

This is true for any scenario where:

* The Sigma organization and connected data platform have different account time zones.
* A calculation is performed on a date column, such as a filter targeting that column, or a calculated column that uses the date column.

Sigma creates date filters using an absolute moment in time based on your account time zone, but reads the column using session time zone. Because session time zone differs between the data platform and Sigma, the filter selects for a different set of values in each location.

Updated 3 days ago

---

Related resources

* [CurrentTimezone](/docs/currenttimezone)
* [ConvertTimezone](/docs/converttimezone)
* [Account Time Zone](/docs/account-time-zone)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [Select a time zone](#select-a-time-zone)
  + [Time zone change considerations](#time-zone-change-considerations)
  + [How Sigma displays date data](#how-sigma-displays-date-data)
  + [Warehouse views time zone limitation](#warehouse-views-time-zone-limitation)