# CDC COVID-19 FAQ web scraper

This is a basic web scraper for Centers of Disease Control and Prevention (CDC) frequently asked questions pages related to the COVID-19 outbreak.

The scraper is directed at the [main FAQ page](https://www.cdc.gov/coronavirus/2019-ncov/faq.html), but it should work on other pages that use the same `.accordion` CSS classes by replacing or adding the other URLs.

The scraper outputs a CSV file with the questions and answers in separate columns.

## Dependencies
- python
- pandas
- requests
- beautiful soup (bs4)
- time
- unicodedata

## Enhancements needed
~~The script strips out custom attribute markup, but it doesn't yet remove the text replacements for external link and pdf icons. Those still show up in the text as `external icon` and `pdf icon`, respectively.~~ Fixed 5/2/20
