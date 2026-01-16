Quotes Parser

This project downloads and parses public quotes from https://quotes.toscrape.com/

1) Page fetching with user-defined depth  
   The script first asks the user how many pages to scrape.  
   Based on this number, it builds page URLs in the form:

       Page 1: https://quotes.toscrape.com/
       Page 2: https://quotes.toscrape.com/page/2/
       Page 3: https://quotes.toscrape.com/page/3/
       ...

   The `fetch_page()` function sends HTTP requests, checks for errors, and
   returns the raw HTML for each page.

2) Parsing quotes from each page  
   The `parse_quotes_list()` function parses the downloaded HTML with
   BeautifulSoup and extracts for every quote:

       quote   — the quote text
       author  — the author’s name
       tags    — a list (later stored as a comma-separated string)

   All quotes from all pages are collected into a single Python list.

3) Exporting data to CSV  
   The `save_csv()` function writes the aggregated quote data into
   a CSV file named `quotes.csv`. Each row contains:

       quote, author, tags

   Tags are stored as a comma-separated string so that the file is easy
   to work with in Excel, Google Sheets, or other tools.

4) Script entry point  
   The `main()` function orchestrates the whole workflow:

       - prompts the user for the number of pages to scrape
       - downloads each page
       - parses all quotes
       - prints progress and statistics
       - saves the final dataset to `quotes.csv`

The end result is a compact CSV dataset with quotes, authors, and
topic tags collected from multiple pages, suitable for scraping practice,
text analysis, or basic NLP experiments.
