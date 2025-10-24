# Text

# Text

The **Text** function converts values to text strings (or [WKT](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) format when converting geography data).

## Syntax

```
Text(input)
```

Function arguments:

input
:   (required) The text, date, geography, or number data that must be converted to text
:   Sigma converts dates to text as a full ISO date-timestamp.

## Notes

* On connections that support geography, the **Text** function can be used to convert valid geography data to [Well-known text](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) (WKT) format. For more information, see the second example in [examples](#examples).

## Example

```
Text(1)
```

Converts the number `1` to text, and returns `1` as text data.

```
Text(MakePoint(179, 90))
```

Converts the geography point (179, 90) to WKT, and returns `POINT(179 90)` as text data.

Updated 3 days ago

---

Related resources

* [MonthName](/docs/monthname)
* [WeekdayName](/docs/weekdayname)

* [Table of Contents](#)
* + [Syntax](#syntax)
  + [Notes](#notes)
  + [Example](#example)