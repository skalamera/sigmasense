# Supported regions, data platforms, and features

# Supported regions, data platforms, and features

Sigma supports various cloud platforms and regions, connections to many data platforms, and some features are supported only on specific data platforms.

## Supported cloud platforms and regions

Your Sigma organization is hosted on one of the following cloud platforms:

* Amazon Web Services (AWS)
* Microsoft Azure
* Google Cloud (GCP)

Your cloud deployment is chosen when your Sigma organization is created, and cannot be migrated or changed after creation.

> 💡
>
> If you're unsure which cloud platform hosts your organization, you can reference it in the **Administration** portal (if you're assigned the **Admin** [account type](/docs/user-account-types)). Go to **Administration** > **Account** > **General Settings**, then locate the **Site** section. The **Cloud** field identifies the platform hosting your organization.

The following table lists the specific supported cloud regions:

| Cloud platform | Region | Location | Cloud region code | API endpoint |
| --- | --- | --- | --- | --- |
| AWS logo | **United States West** | Oregon | us-west-2 (primary) us-east-1 (disaster recovery) | aws-api.sigmacomputing.com |
| **United States East** | N. Virginia | us-east-1 (primary) us-west-2 (disaster recovery) | api.us-a.aws.sigmacomputing.com |
| **Canada** | Central | ca-central-1 | api.ca.aws.sigmacomputing.com |
| **Europe** | Frankfurt | eu-central-1 (primary) eu-north-1 (disaster recovery) | api.eu.aws.sigmacomputing.com |
| **Asia Pacific** | Sydney | ap-southeast-2 | api.au.aws.sigmacomputing.com |
| **United Kingdom** | London | eu-west-2 (primary) eu-west-1 (disaster recovery) | api.uk.aws.sigmacomputing.com |
| Azure logo | **United States** | Virginia | eastus2 (primary) centralus (disaster recovery) | api.us.azure.sigmacomputing.com |
| **Europe1** | Netherlands | westeurope (primary) northeurope (disaster recovery) | api.eu.azure.sigmacomputing.com |
| **Canada** | Toronto | canadacentral (primary) canadaeast (disaster recovery) | api.ca.azure.sigmacomputing.com |
| **United Kingdom1** | London | uksouth (primary) ukwest (disaster recovery) | api.uk.azure.sigmacomputing.com |
| Google Cloud logo | **United States2** | Iowa | us-central-1 | api.sigmacomputing.com |

1Sigma users of Azure-hosted organizations in the EU and UK are not granted access to audit logs.

2GCP-hosted organizations don't support private connections.

## Supported data platforms and feature compatibility

Sigma connects to the following data platforms:

* AlloyDB
* Azure SQL Database
* Amazon Redshift
* Databricks
* Google BigQuery
* MySQL
* PostgreSQL
* Snowflake
* Starburst Galaxy
* SQL Server 2022 and Azure SQL Managed Instance

Connections support most Sigma features; however, due to technical variations (like SQL dialects, architecture, and security) some features are not currently compatible with all data platforms. The following table lists current feature limitations for each connection type.

| CDW/DBMS | Feature limitations |
| --- | --- |
| AlloyDB | AlloyDB connections *don't* support the following features:   * Dataset warehouse views created in Sigma * Input tables * Private link * Export to cloud storage * OAuth connections * Sigma result IDs cache * User attributes for role and warehouse switching * Running Python code * Geography data type * The following Array functions: Array, ArrayDistinct, ArrayExcept,   ArrayIntersection, ArrayJoin, ArraySlice, Sequence, SplitToArray * The following Aggregate functions: RegressionIntercept,   RegressionR2, RegressionSlope, SparklineAgg * All Geography functions: Area, Centroid, Distance, Geography,   Intersects, Json, Latitude, Longitude, MakeLine, MakePoint,   Perimeter, Text, Within * The following Passthrough functions: AggGeography, CallGeography |
| Amazon Redshift | Amazon Redshift connections *don't* support the following features:   * Dataset warehouse views created in Sigma * Private link on GCP platform * OAuth connections * Sigma result IDs cache * User attributes for role and warehouse switching * Running Python code * Geography data type * The following Array functions: ArrayContains, ArrayDistinct,   ArrayExcept, ArrayJoin, ArraySlice, Sequence, SplitToArray * The following Aggregate functions: ArrayAgg, ArrayAggDistinct, ArrayDistinct,   ArrayIntersection, Corr, RegressionIntercept, RegressionR2, SparklineAgg   RegressionSlope * All Geography functions: Area, Centroid, Distance, Geography,   Intersects, Json, Latitude, Longitude, MakeLine, MakePoint,   Perimeter, Text, Within * The following Passthrough functions: AggGeography, CallGeography * The following Window functions: CumulativeCorr, MovingCorr |
| Azure SQL | Azure SQL Database connections *don't* support the following features:   * Dataset warehouse views created in Sigma * Export to cloud storage * OAuth connections * Sigma result IDs cache * User attributes for role and warehouse switching * Write-back features: CSV uploads, Input tables, running Python code * Geography data type * All Geography functions: Area, Centroid, Distance, Geography,   Intersects, Json, Latitude, Longitude, MakeLine, MakePoint,   Perimeter, Text, Within * The following Array functions: Array, ArrayAggDistinct, ArrayConcat, ArrayTransform, ArrayFilter, Sequence, SplitToArray * The following Passthrough functions (including Call and Agg variations): Geography, Variant, Logical * The following Aggregate functions: ListAggDistinct, RegressionIntercept, RegressionR2, RegressionSlope * The following Date functions: DateParse, LastDay * The following Text functions: RegexpMatch, RegexpReplace, RegexpExtract, MD5, SHA256, SplitPart, Proper * The following Math functions: BinFixed * The following Window functions: CumulativeCorr, MovingCorr, Median, Corr, Nth * Regex text matching in filters * Custom SQL containing CTE's * Sample connections |
| Databricks | Databricks connections *don't* support the following features:   * Private link on GCP platform * Export to cloud storage * Sigma result IDs cache * User attributes for role and warehouse switching * The following Array functions: Array, ArrayConcat, ArrayDistinct,   ArrayExcept, ArrayIntersection, ArraySlice * The following Geography functions: Centroid, Intersects, Within * SSH * Stored procedure actions * Multi-select columns for input tables |
| Google BigQuery | Google BigQuery connections *don't* support the following features:   * Private link * Export to cloud storage * OAuth connections * User attributes for role and warehouse switching * Running Python code * The following Array functions: Sequence * The following Aggregate functions: RegressionIntercept,   RegressionR2, RegressionSlope |
| MySQL | MySQL connections *don't* support the following features:   * Dataset warehouse views created in Sigma * Input tables * Private link on GCP platform * Export to cloud storage * OAuth connections * Sigma result IDs cache * User attributes for role and warehouse switching * Running Python code * Geography data type * The following Array functions: ArrayAgg, ArrayAggDistinct,   ArrayDistinct, ArrayExcept, ArrayIntersection, ArrayJoin, Sequence,   SplitToArray * The following Aggregate functions: Corr, RegressionIntercept,   RegressionR2, RegressionSlope * All Geography functions: Area, Centroid, Distance, Geography,   Intersects, Json, Latitude, Longitude, MakeLine, MakePoint,   Perimeter, Text, Within * The following Passthrough functions: AggGeography, CallGeography * The following Window functions: CumulativeCorr, MovingCorr |
| PostgreSQL | PostgreSQL connections *don't* support the following features:   * Dataset warehouse views created in Sigma * Private link on GCP platform * Export to cloud storage * OAuth connections * Sigma result IDs cache * Running Python code * Geography data type * The following Array functions: Sequence * The following Text functions: SHA256 * All Geography functions: Area, Centroid, Distance, Geography,   Intersects, Json, Latitude, Longitude, MakeLine, MakePoint,   Perimeter, Text, Within * The following Passthrough functions: AggGeography, CallGeography |
| Snowflake | Snowflake connections *don't* support the following features:   * Private link on GCP platform * The following Window functions: CumulativeCorr, MovingCorr |
| Starburst Galaxy | Starburst Galaxy connections *don't* support the following features:   * Dataset warehouse views created in Sigma * Workbook warehouse views * Write-back features: Input tables, CSV upload, and Materialization * Private link * Export to cloud storage * OAuth connections * Sigma result IDs cache * User attributes for role and warehouse switching * Running Python code * The following Array functions: Array, ArrayConcat, ArrayDistinct, ArrayExcept,   ArrayIntersection, ArraySlice * The following Aggregate functions: RegressionIntercept,   RegressionR2, RegressionSlope * The following Geography functions: Centroid, Within, Intersects,   Perimeter |
| SQL Server 2022 and Azure SQL Managed Instance | SQL Server 2022 and Azure SQL Managed Instance connections *don't* support the following features:   * Dataset warehouse views created in Sigma * Export to cloud storage * OAuth connections * Sigma result IDs cache * User attributes for role and warehouse switching * Write-back features: CSV uploads, input tables, running Python code * Geography data type * All Geography functions: Area, Centroid, Distance, Geography,   Intersects, Json, Latitude, Longitude, MakeLine, MakePoint,   Perimeter, Text, Within * The following Array functions: Array, ArrayAgg, ArrayAggDistinct, ArrayTransform, ArrayFilter, Sequence, SplitToArray * All Passthrough functions * The following Aggregate functions: ListAggDistinct, RegressionIntercept, RegressionR2, RegressionSlope, SparklineAgg * The following Date functions: DateParse, LastDay * The following Text functions: RegexpMatch, RegexpReplace, RegexpExtract, MD5, SHA256, SplitPart, Proper * The following Math functions: BinFixed * The following Window functions: CumulativeCorr, MovingCorr, Median, Corr, Nth * Regex text matching in filters * Custom SQL containing CTE's * Sample connections |

## Supported web browsers

Sigma supports the following web browsers:

* **Google Chrome** (recommended): latest version
* **Safari**: latest version
* **Mozilla Firefox**: latest version
* **Microsoft Edge**: latest version
* **Opera**: latest version

## Supported authentication methods

Sigma supports the following authentication methods:

* **[Security Assertion Markup Language 2.0](/docs/single-sign-on-with-saml)** (SAML 2.0)
* **[OAuth](/docs/configure-oauth)**

Updated about 6 hours ago

---

[Sigma product releases](/docs/sigma-product-releases)

* [Table of Contents](#)
* + [Supported cloud platforms and regions](#supported-cloud-platforms-and-regions)
  + [Supported data platforms and feature compatibility](#supported-data-platforms-and-feature-compatibility)
  + [Supported web browsers](#supported-web-browsers)
  + [Supported authentication methods](#supported-authentication-methods)