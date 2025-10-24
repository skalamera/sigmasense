# Function index

# Function index

Sigma supports over 200 functions that enable you to perform simple and complex calculations, transformations, and extractions to get the most out of your data.

Browse this function index by category to learn more about the specific types of functions available to you.

## Aggregate functions

Aggregate functions evaluate multiple rows of data to return a single value. For example, you can use aggregate functions to perform group calculations (like **Sum** and **Avg**), retrieve specific values (like **Min** and **Max**), assess the data to provide insights (like **Count** and **CountDistinct**), or join multiple values (like **ArrayAgg** and **ListAgg**).

|  |  |
| --- | --- |
| [ArrayAgg](/docs/arrayagg) | Identifies non-null row values in a column or group and aggregates them into a single array. |
| [ArrayAggDistinct](/docs/arrayaggdistinct) | Identifies distinct non-null row values in a column or group and aggregates them into a single array. |
| [Avg](/docs/avg) | Calculates the average value of a column or group. |
| [AvgIf](/docs/avgif) | Calculates the average value of a column or group *when the specified condition is* `True`. |
| [Corr](/docs/corr) | Calculates the Pearson correlation coefficient (bivariate correlation) of two columns. |
| [Count](/docs/count) | Counts the number of non-null and non-empty values in a column or group. |
| [CountDistinct](/docs/countdistinct) | Counts the number of unique non-null and non-empty values in a column or group. Does not count duplicate values. (Same as **[Ndv](/docs/ndv)**.) |
| [CountDistinctIf](/docs/countdistinctif) | Counts the number of unique non-null and non-empty values in a column or group *when the specified condition is* `True`. Does not count duplicate values. |
| [CountIf](/docs/countif) | Counts the number of non-null and non-empty values in a column or group *when the specified condition is* `True`. |
| [GrandTotal](/docs/grandtotal) | Calculates the grand total for column or group. |
| [ListAgg](/docs/listagg) | Joins the values of a group or column into a single text string. |
| [ListAggDistinct](/docs/listaggdistinct) | Joins the unique values of a group or column into a single text string. Does not include duplicate values. |
| [Max](/docs/max) | Retrieves the maximum (largest or latest) value in a column or group. |
| [MaxIf](/docs/maxif) | Retrieves the maximum (largest or latest) value in a column or group *when the specified condition is* `True`. |
| [Median](/docs/median) | Determines the median (midpoint) value of a column or group. |
| [Min](/docs/min) | Retrieves the minimum (smallest or earliest) value in a column or group. |
| [MinIf](/docs/minif) | Retrieves the minimum (smallest or earliest) value in a column or group *when the specified condition is* `True`. |
| [PercentileCont](/docs/percentilecont) | Calculates the continuous kth percentile of a column or group. |
| [PercentileDisc](/docs/percentiledisc) | Calculates the discrete kth percentile of a column or group. |
| [PercentOfTotal](/docs/percentoftotal) | Calculates the percentage a value contributes to the specified aggregate total. |
| [RegressionIntercept](/docs/regressionintercept) | Calculates the y-intercept of the linear regression line. |
| [RegressionR2](/docs/regressionr2) | Calculates the coefficient of determination of the linear regression line. |
| [RegressionSlope](/docs/regressionslope) | Calculates the slope of the linear regression line. |
| [StdDev](/docs/stddev) | Calculates the standard deviation of a column or group. |
| [Subtotal](/docs/subtotal) | Calculates the subtotal of a column or group. |
| [Sum](/docs/sum) | Calculates the sum of a column or group. |
| [SumIf](/docs/sumif) | Calculates the sum of a column or group *when the specified condition is* `True`. |
| [SumProduct](/docs/sumproduct) | Calculates the product of row values across specified columns, then calculates the sum of the resulting products for a column or group. |
| [Variance](/docs/variance) | Estimates the sample variance (spread of distribution) of a column or group. |
| [VariancePop](/docs/variancepop) | Calculates the population variance (spread of distribution) of a column or group. |

## Array functions

Array functions create, manage, and manipulate arrays (lists of indexed values).

|  |  |
| --- | --- |
| [Array](/docs/array) | Returns an array containing specified values. |
| [ArrayConcat](/docs/arrayconcat) | Combines multiple arrays into one array. |
| [ArrayContains](/docs/arraycontains) | Searches for a specific value in an array. If the value is found, the function returns `True`, otherwise it returns `False`. |
| [ArrayDistinct](/docs/arraydistinct) | Returns the array without duplicate values. |
| [ArrayExcept](/docs/arrayexcept) | Returns an array of all unique elements from one specified array not included in another specified array. |
| [ArrayIntersection](/docs/arrayintersection) | Compares two arrays and returns an array of all overlapping elements, without duplicates. |
| [ArrayJoin](/docs/arrayjoin) | Joins elements of an array into a single text string. |
| [ArrayLength](/docs/arraylength) | Determines the number of entries in an array, or list. |
| [ArraySlice](/docs/arrayslice) | Returns a portion of an array, defined by the starting index and length. |
| [Sequence](/docs/sequence) | Returns an arithmetic sequence as an array of integers based on a specified range and increment |
| [SplitToArray](/docs/splittoarray) | Splits a specified string by a given delimiter and returns an array of substrings. |
| [Sparkline (Beta)](/docs/sparkline) | Generates sparkline charts from an array of JSON objects. |
| [SparklineAgg (Beta)](/docs/sparklineagg) | Generates sparkline charts by aggregating values over time. |

The following [aggregate functions](#aggregate-functions) also create arrays:

|  |  |
| --- | --- |
| [ArrayAgg](/docs/arrayagg) | Identifies non-null row values in a column or group and aggregates them into a single array. |
| [ArrayAggDistinct](/docs/arrayaggdistinct) | Identifies distinct non-null row values in a column or group and aggregates them into a single array. |

## Date functions

Date functions evaluate, convert, and manipulate date and time values.

|  |  |
| --- | --- |
| [ConvertTimezone](/docs/converttimezone) | Converts date and time values to the specified time zone. |
| [DateAdd](/docs/dateadd) | Adds a specified quantity of time to a date. |
| [DateDiff](/docs/datediff) | Calculates the time difference between two dates. |
| [DateFormat](/docs/dateformat) | Formats a date value to text based on the format provided. |
| [DateFromUnix](datefromunix) | Converts a Unix timestamp to a date value. |
| [DateLookback](/docs/datelookback) | Returns the value of a variable at a previous point in time (or lookback period) determined by a specified date and offset. |
| [DatePart](/docs/datepart) | Extracts the specified date part from a date value. |
| [DateParse](/docs/dateparse) | Parses a text value in a specified format and returns a datetime value (date data type) in ISO format. |
| [DateTrunc](/docs/datetrunc) | Truncates the date to the specified date part. |
| [Day](/docs/day) | Returns the day of the month from a date value as a number. |
| [DayOfYear](/docs/dayofyear) | Returns the day of the year from a date value as a number. |
| [EndOfMonth](/docs/endofmonth) | Returns the last day of the month from a date value. |
| [Hour](/docs/hour) | Returns the hour component from a date value as a number. |
| [InDateRange](/docs/indaterange) | Determines if a date falls within a specified date range and returns `True` or `False`. |
| [InPriorDateRange](/docs/inpriordaterange) | Determines if a date falls within the date range of a prior period and returns `True` or `False`. |
| [LastDay](/docs/lastday) | Evaluates a specified component in a date value and returns the last datetime value of that component in ISO format. |
| [MakeDate](/docs/makedate) | Evaluates specified values representing year, month, and day units and returns a datetime value in ISO format. |
| [Minute](/docs/minute) | Returns an integer representing the minute component in a specified datetime value. |
| [Month](/docs/month) | Returns an integer representing the month component in a specified datetime value. |
| [MonthName](/docs/monthname) | Returns the name of the month component from a specified datetime value. |
| [Now](/docs/now) | Returns the current date and time using your organization's account timezone. |
| [Quarter](/docs/quarter) | Returns an integer representing the quarter component in a specified datetime value. |
| [Second](/docs/second) | Returns an integer representing the second component in a specified datetime value. |
| [Today](/docs/today) | Returns the current date using your organization's account timezone. |
| [Weekday](/docs/weekday) | Returns an integer representing the day of the week in a specified datetime value. |
| [WeekdayName](/docs/weekdayname) | Returns the name of the day of the week in a specified datetime value. |
| [Year](/docs/year) | Returns an integer representing the year component in a specified datetime value. |

## Financial functions

Financial functions evaluate and calculate data related to money, investments, interest rates, and other aspects of finance.

|  |  |
| --- | --- |
| [CAGR](/docs/cagr) | Returns the compound annual growth rate of an investment. |
| [Effect](/docs/effect) | Returns the effective annual interest rate. |
| [FV](/docs/fv) | Returns the future value of an investment. |
| [IPmt](/docs/ipmt) | Returns the interest portion of a periodic payment for a loan based on the amount, number of periods, and constant interest rate. The portion of the payment allocated to interest decreases over time. |
| [Nominal](/docs/nominal) | Returns the nominal annual interest rate. |
| [NPer](/docs/nper) | Returns the number of periods for a loan or investment based on known amount, interest rate, and periodic payment amount. |
| [Pmt](/docs/pmt) | Returns the periodic payment for a loan based on the amount, number of periods, and constant interest rate. |
| [PPmt](/docs/ppmt) | Returns the principal portion of a periodic payment for a loan based on the amount, number of periods, and constant interest rate. The portion of the payment allocated to principal increases over time. |
| [PV](/docs/pv) | Returns the present value of a loan or an investment, when using constant and regular periodic payments. |
| [XNPV](/docs/xnpv) | Returns the net present value of an investment for payments or incomes at irregular intervals. |

## Geography functions

> 📘
>
> Geography functions aren't compatible with all data platform connections. To check if your connection supports these functions, see [Supported data platforms and feature compatibility](/docs/region-warehouse-and-feature-support#supported-data-platforms-and-feature-compatibility).

Geography functions enable you to work with the [geography data type](/docs/data-types-and-formats#geography) to analyze locations, routes, and other geospatial data. For example, you can use geography functions to transform data into compatible formats for [geography maps](/docs/build-a-geography-map).

|  |  |
| --- | --- |
| [Area](/docs/area) | Calculates the area of a geography, in specified units. |
| [Centroid](/docs/centroid) | Calculates the geographic center of a geography. |
| [Distance](/docs/distance) | Calculates the minimum distance between two geographies, in specified units. |
| [Geography](/docs/geography) | Converts GeoJSON or WKT formats to the [geography data type](/docs/data-types-and-formats#geography). |
| [Intersects](/docs/intersects) | Determines if one geography intersects another geography. |
| [Json](/docs/json-geography) | Converts [geography data](/docs/data-types-and-formats#geography) to GeoJSON. |
| [Latitude](/docs/latitude) | Returns the latitude component of a point. |
| [Longitude](/docs/longitude) | Returns the longitude component of a point. |
| [MakeLine](/docs/makeline) | Constructs a line from a series of points and line segments. |
| [MakePoint](/docs/makepoint) | Constructs a point from latitude and longitude data. |
| [Perimeter](/docs/perimeter) | Calculates the perimeter of a geography, in specified units. |
| [Text](/docs/text-geography) | Converts [geography data](/docs/data-types-and-formats#geography) to WKT format. |
| [Within](/docs/within) | Determines if one geography is fully within another geography. |

## Join functions

Join functions retrieve data from target elements based on related columns in the local and target elements.

|  |  |
| --- | --- |
| [Lookup](/docs/lookup) | Finds a value in a specified target element column and returns the corresponding row value from another column in that element. |
| [Rollup](/docs/rollup) | Finds a value in a specified target element column and aggregates all corresponding row values from another column in that element. |

## Logical functions

Logical functions perform logical operations or evaluate conditional statements and typically return boolean (`true` or `false`) output.

|  |  |
| --- | --- |
| [Between](/docs/between) | Determines if a value is within the specified range; `True` or `False`. |
| [Choose](/docs/choose) | Given a specified index number, returns the matching value from a list. |
| [Coalesce](/docs/coalesce) | Returns the first non-Null value from a list. |
| [If](/docs/if) | Evaluates if one or more conditions are `true` or `false` and returns the corresponding value. |
| [In](/docs/in) | Determines if a specified value matches any candidate values; `True` or `False`. |
| [IsNotNull](/docs/isnotnull) | Determines if the cell has a value; `True` or `False`. |
| [IsNull](/docs/isnull) | Determines if the cell is Null; `True` or `False`. |
| [Switch](/docs/switch) | Using the SWITCH paradigm, tests the specified value against a list of conditions, and returns the matching response. |
| [Zn](/docs/zn) | Returns non-Null values, or 0 (zero) instead of Null values. |

## Math functions

Math functions perform mathematical operations, including arithmetic, trigonometric, rounding, statistical, and logarithmic calculations.

|  |  |
| --- | --- |
| [Abs](/docs/abs) | Returns the absolute value of a number. |
| [Acos](/docs/acos) | Returns the arccosine of an angle. |
| [Asin](/docs/asin) | Returns the arcsine of an angle. |
| [Atan](/docs/atan) | Returns the arctangent of an angle. |
| [Atan2](/docs/atan2) | Returns the arctangent of a coordinate pair. |
| [BinFixed](/docs/binfixed) | Calculates the bin of a value among the specified number of identically-sized bins. |
| [BinRange](/docs/binrange) | Calculates the bin for a value using the specified lower bounds. |
| [BitAnd](/docs/bitand) | Calculates the bitwise `AND` of two numbers. |
| [BitOr](/docs/bitor) | Calculates the bitwise `OR` of two numbers. |
| [Ceiling](/docs/ceiling) | Rounds the number up to the closest multiple of equal or greater value. |
| [Cos](/docs/cos) | Returns the cosine of an angle. |
| [Cot](/docs/cot) | Returns the cotangent of an angle. |
| [Degrees](/docs/degrees) | Converts the angle measurement from radians to degrees. |
| [DistanceGlobe](/docs/distanceglobe) | Calculates the distance between two points on the globe, in kilometers. |
| [DistancePlane](/docs/distanceplane) | Calculates the distance between two points on a plane. |
| [Div](/docs/div) | Returns the integer component of a division. |
| [Exp](/docs/exp) | Returns the mathematical constant `e`, or `2.71828`. |
| [Floor](/docs/floor) | Rounds the number down to the closest multiple of equal or lesser value. |
| [Greatest](/docs/greatest) | Returns the largest value from a list. |
| [Int](/docs/int) | Rounds the integer down to the largest integer of lesser or equal value. |
| [IsEven](/docs/iseven) | Returns True if the integer part of a number is even. |
| [IsOdd](/docs/isodd) | Returns True if the integer part of a number is odd. |
| [Least](/docs/least) | Returns the smallest value from a list. |
| [Ln](/docs/ln) | Calculates the natural logarithm of a number, `log_e(n)`. |
| [Log](/docs/log) | Calculates the logarithm of a number. Defaults to `log_10(n)`. |
| [Mod](/docs/mod) | Returns the remainder component of a division. |
| [MRound](/docs/mround) | Rounds the number down to the closest multiple of the specified number. |
| [Pi](/docs/pi) | Returns the mathematical constant `π`, or `3.14159...`. |
| [Power](/docs/power) | Calculates the result of a number raised to the specified power. |
| [Radians](/docs/radians) | Converts the angle measurement from degrees to radians. |
| [Round](/docs/round) | Calculates the number to the specified number of digits. |
| [RoundDown](/docs/rounddown) | Rounds a number down to the specified number of digits or decimal places. |
| [RoundUp](/docs/roundup) | Rounds a number up to the specified number of digits or decimal places. |
| [RowAvg](/docs/rowavg) | Calculates the average value of a list of numbers. |
| [Sign](/docs/sign) | Calculates the sign of a number. Returns `-1` if negative, `1` if positive, or `0` if zero. |
| [Sin](/docs/sin) | Calculates the sine of an angle. |
| [Sqrt](/docs/sqrt) | Calculates the square root of a number. |
| [Tan](/docs/tan) | Calculates the tangent of an angle. |
| [Trunc](/docs/trunc) | Truncates a number to the specified number of digits or decimal places. |

## Passthrough functions

Passthrough functions send requests to execute operations within your connected data platform, then return the response generated by your data platform's native functions.

|  |  |
| --- | --- |
| [AggDatetime](/docs/aggdatetime) | Calls a data platform aggregate function that returns a [date data type](/docs/data-types-and-formats#date). Aggregate version of [CallDatetime](/docs/calldatetime). |
| [AggGeography](/docs/agggeography) | Calls a data platform aggregate function that returns a [geography data type](/docs/data-types-and-formats#geography). Aggregate version of [CallGeography](/docs/callgeography). |
| [AggLogical](/docs/agglogical) | Calls a data platform aggregate function that returns a [logical data type](/docs/data-types-and-formats#logical). Aggregate version of [CallLogical](/docs/calllogical). |
| [AggNumber](/docs/aggnumber) | Calls a data platform aggregate function that returns a [number data type](/docs/data-types-and-formats#number). Aggregate version of [CallNumber](/docs/callnumber). |
| [AggText](/docs/aggtext) | Calls a data platform aggregate function that returns a [text data type](/docs/data-types-and-formats#text). Aggregate version of [CallText](/docs/calltext). |
| [AggVariant](/docs/aggvariant) | Calls a data platform aggregate function that returns a [variant data type](/docs/data-types-and-formats#variant). Aggregate version of [CallVariant](/docs/callvariant). |
| [CallDatetime](/docs/calldatetime) | Calls a data platform function that returns a [date data type](/docs/data-types-and-formats#date). |
| [CallGeography](/docs/callgeography) | Calls a data platform function that returns a [geography data type](/docs/data-types-and-formats#geography). |
| [CallLogical](/docs/calllogical) | Calls a data platform function that returns a [logical data type](/docs/data-types-and-formats#logical). |
| [CallNumber](/docs/callnumber) | Calls a data platform function that returns a [number data type](/docs/data-types-and-formats#number). |
| [CallText](/docs/calltext) | Calls a data platform function that returns a [text data type](/docs/data-types-and-formats#text). |
| [CallVariant](/docs/callvariant) | Calls a data platform function that returns a [variant data type](/docs/data-types-and-formats#variant). |

## System functions

System functions return information about your Sigma organization, including details about users and system configurations.

|  |  |
| --- | --- |
| [CurrentTimezone](/docs/currenttimezone) | Returns your organization's [IANA time zone](https://www.iana.org/time-zones) as configured in the **Administration** portal. |
| [CurrentUserAttributeText](/docs/currentuserattributetext) | Returns the value of a specific attribute for the current (signed-in) user. |
| [CurrentUserEmail](/docs/currentuseremail) | Returns the email address associated with the current (signed-in) user's account. |
| [CurrentUserFirstName](/docs/currentuserfirstname) | Returns the current (signed-in) user’s first name as configured in the user’s profile. |
| [CurrentUserFullName](/docs/currentuserfullname) | Returns the current (signed-in) user’s first and last name as configured in the user’s profile. |
| [CurrentUserInTeam](currentuserinteam) | Returns `true` if the current user is a member of a specific teams. |

## Text functions

Text functions evaluate or manipulate string data to perform operations like text modification, formatting, and extraction.

|  |  |
| --- | --- |
| [Concat](/docs/concat) | Combines multiple strings into a single text value. |
| [Contains](/docs/contains) | Searches for a specified substring in a text value. If the substring is found, the function returns `True`, otherwise it returns `False`. |
| [EndsWith](/docs/endswith) | Determines if a text value ends with a specified substring. If the substring is found at the end of the text value, the function returns `True`, otherwise it returns `False`. |
| [Find](/docs/find) | Returns the index where it first finds the specified substring within a string. Returns `0` if not found. |
| [ILike](/docs/ilike) | Returns `True` if the string matches the pattern. Case insensitive. |
| [Left](/docs/left) | Returns the left portion of the string (the beginning), up to specified number of characters. |
| [Len](/docs/len) | Returns the number of characters in a string, including spaces. |
| [Like](/docs/like) | Returns `True` if the string value matches the pattern. Case sensitive. |
| [LPad](/docs/lpad) | Sets the string to a desired length by adding or removing characters at the front. Uses an optional fill character or defaults to extra spaces. |
| [Lower](/docs/lower) | Converts a string to all lower case. |
| [LTrim](/docs/ltrim) | Removes leading spaces from a string. |
| [MD5](/docs/md5) | Calculates the hash value of a string for the [MD5](https://en.wikipedia.org/wiki/MD5) message-digest algorithm (hashing function). |
| [Mid](/docs/mid) | Returns a substring from a string, defined by offset and length. Same as [Substring](/docs/substring). |
| [Proper](/docs/proper) | Converts text to proper case, capitalizing the first letter of each word. |
| [RegexpExtract](/docs/regexpextract) | Returns the substring that matches a regular expression within a string. |
| [RegexpMatch](/docs/regexpmatch) | Returns `True` if a string matches a regular expression. |
| [RegexpReplace](/docs/regexpreplace) | Returns a string for a pattern and replaces it with a specified string. |
| [Repeat](/docs/repeat) | Returns the result of repeating the string a specified number of times. |
| [Replace](/docs/replace) | Replaces every instance of a specified string with a replacement string. |
| [Reverse](/docs/reverse) | Reverses the order of characters in a string. |
| [Right](/docs/right) | Returns the right portion of a string (the end), up to the specified number of characters. |
| [RPad](/docs/rpad) | Sets the string to a desired length by adding or removing characters at the end. Uses an optional fill character, or defaults to extra spaces. |
| [RTrim](/docs/rtrim) | Removes trailing spaces from the end of a string. |
| [SHA256](/docs/sha256) | Transforms text input into a 256-bit hash value. |
| [SplitPart](/docs/splitpart) | Splits the string into multiple parts at the positions of each appearance of the delimiter and returns the nth part of the string at the specified position. |
| [StartsWith](/docs/startswith) | Determines if a string starts with the specified substring. Returns `True` or `False`. |
| [Substring](/docs/substring) | Returns a substring from a string, defined by offset and length. Same as [Mid](/docs/mid). |
| [Trim](/docs/trim) | Removes both leading and trailing spaces from a string. |
| [Upper](/docs/upper) | Converts a string to upper case (all capital letters). |
| [UrlPart](/docs/urlpart) | Extracts a component from a URL. |

## Type functions

Type functions perform type casting or type conversion operations that transform values from one [data type](/docs/data-types-and-formats) to another.

|  |  |
| --- | --- |
| [Date](/docs/date) | Converts text or number values to the [date data type](/docs/data-types-and-formats#date) in [ISO](/docs/date) datetime format. |
| [JSON](/docs/json) | Converts values to the [variant data type](/docs/data-types-and-formats#variant) in JSON format. |
| [Logical](/docs/logical) | Converts values to the [logical data type](/docs/data-types-and-formats#logical) in boolean format (`true` or `false`). |
| [Number](/docs/number) | Converts values to the [number data type](/docs/data-types-and-formats#number). |
| [Text](/docs/text) | Converts values to the [text data type](/docs/data-types-and-formats#text). |
| [Variant](/docs/variant) | Converts text values to the [variant data type](/docs/data-types-and-formats#variant). |

The following [geography function](/docs/geography-functions) also transform values from one data type to another:

|  |  |
| --- | --- |
| [Geography](/docs/geography) | Converts GeoJSON or WKT formats to the [geography data type](/docs/data-types-and-formats#geography). |

## Window functions

Window functions perform operations across an entire table, table grouping (grouped rows), or defined window of rows. Sigma supports [cumulative](#cumulative-window-functions), [moving](#moving-window-functions), [shifting](#shifting-window-functions), and [ranking](#ranking-window-functions) window functions.

### Cumulative window functions

Cumulative window functions evaluate a specified column in a table or grouping and return the running total or cumulative value for all rows up to and including the current row. This differs from aggregate values that calculate a summary value for the entire table or grouping.

|  |  |
| --- | --- |
| [CumulativeAvg](/docs/cumulativeavg) | Calculates the running average up to and including the current row. |
| [CumulativeCorr](/docs/cumulativecorr) | Calculates the correlation coefficient between dependent and independent data columns up to and including the current row. |
| [CumulativeCount](/docs/cumulativecount) | Counts the number of non-null values up to and including the current row. |
| [CumeDist](/docs/cumedist) | Calculates the cumulative distribution of values relative to the current row value. |
| [CumulativeMax](/docs/cumulativemax) | Returns the largest value up to and including the current row. |
| [CumulativeMin](/docs/cumulativemin) | Returns the smallest value up to and including the current row. |
| [CumulativeStdDev](/docs/cumulativestddev) | Calculates the standard deviation of values up to and including the current row. |
| [CumulativeSum](/docs/cumulativesum) | Calculates the sum of values up to and including the current row. |
| [CumulativeVariance](/docs/cumulativevariance) | Calculates the variance of a column up to and including the current row. |

### Moving window functions

Moving window functions evaluate a specified column and return a value based on a defined window of rows that moves in relation to the current row.

|  |  |
| --- | --- |
| [MovingAvg](/docs/movingavg) | Calculates the numerical average of a column within a moving window. |
| [MovingCorr](/docs/movingcorr) | Calculates the correlation coefficient of two numerical columns within a moving window. See [Pearson (bivariate) correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) . |
| [MovingCount](/docs/movingcount) | Counts the number of non-Null values in a moving window. |
| [MovingMax](/docs/movingmax) | Finds the maximum value of a column within a moving window. |
| [MovingMin](/docs/movingmin) | Finds the minimum value of a column within a moving window. |
| [MovingStdDev](/docs/movingstddev) | Calculates the standard deviation of a column within a moving window. |
| [MovingSum](/docs/movingsum) | Calculates the sum of a column in a moving window. |
| [MovingVariance](/docs/movingvariance) | Calculates the statistical variance of a column in a moving window. |

### Shifting window functions

Shifting window functions evaluate a specified column in a table or grouping and return the value from a row that shifts in relation to the current row.

|  |  |
| --- | --- |
| [FillDown](/docs/filldown) | Replaces all `null` values in a column or grouping with the closest prior non-null value. |
| [First](/docs/first) | Returns the first row value of a column or grouping. |
| [FirstNonNull](/docs/firstnonnull) | Returns the first non-null value from a column or grouping. |
| [Lag](/docs/lag) | Returns the value from a preceding offset row in a column or grouping. |
| [Last](/docs/last) | Returns the last row value in a column or grouping. |
| [LastNonNull](/docs/lastnonnull) | Returns the last non-null value in a column or grouping. |
| [Lead](/docs/lead) | Returns the value from a subsequent offset row in a column or grouping. |
| [Nth](/docs/nth) | Returns the value from the nth row of a column or grouping. |

### Ranking window functions

Ranking window functions evaluate a specified column in a table or grouping and assign a rank to each row.

|  |  |
| --- | --- |
| [Ntile](/docs/ntile) | Assigns the specified rank, in order, to the column rows of a column, approximately equal number of rows for each rank. |
| [Rank](/docs/rank) | Assigns ranks to unique values in a column, from rank 1 onwards. Skips duplicate values. |
| [RankDense](/docs/rankdense) | Assigns ranks to all values in a column, from rank 1 onwards. Assigns the same rank to duplicate values. |
| [RankPercentile](/docs/rankpercentile) | Ranks the rows in the table by percentile. |
| [RowNumber](/docs/rownumber) | Numbers the table rows, starting with 1. |
| [VisibilityLimit](/docs/visibilitylimit) | Limits the values displayed in a column to the number of specified values according to an order calculated by another ranking function. |

Updated 3 days ago

---

[Download and export limitations](/docs/download-export-and-upload-limitations)[Aggregate functions](/docs/aggregate-functions)

* [Table of Contents](#)
* + [Aggregate functions](#aggregate-functions)
  + [Array functions](#array-functions)
  + [Date functions](#date-functions)
  + [Financial functions](#financial-functions)
  + [Geography functions](#geography-functions)
  + [Join functions](#join-functions)
  + [Logical functions](#logical-functions)
  + [Math functions](#math-functions)
  + [Passthrough functions](#passthrough-functions)
  + [System functions](#system-functions)
  + [Text functions](#text-functions)
  + [Type functions](#type-functions)
  + [Window functions](#window-functions)