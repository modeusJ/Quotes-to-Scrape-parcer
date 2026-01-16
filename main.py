import requests
import csv
from bs4 import BeautifulSoup

base_url = "https://quotes.toscrape.com/"

def fetch_page(url:str) -> str:
    response = requests.get(url, timeout = 10)
    response.raise_for_status()
    return response.text

def parse_quotes_list(html:str) -> list[dict]:
    soup = BeautifulSoup(html, "lxml")

    quotes = []
    for div in soup.select("div.quote"):
        quote = div.select_one("span.text").get_text(strip=True)
        author = div.select_one("small.author").get_text(strip=True)
        tags = [a.get_text(strip=True) for a in div.select("a.tag")]


        quotes.append({"quote":quote, "author":author, "tags":tags})


    return quotes



def save_csv(items: list[dict], filename: str) -> None:
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["quote", "author", "tags"]
        )

        writer.writeheader()
        writer.writerows(items)

def build_page_url(page_number: int) -> str:
    if page_number == 1:
        return base_url
    return f"{base_url}page/{page_number}/"

def main():
    while True:
        try:
            pages_to_scrape = int(input("How many pages do you want to scrape? "))
            if pages_to_scrape < 1:
                print("Please enter a positive integer (1 or more).")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    all_quotes: list[dict] = []

    for page in range(1, pages_to_scrape + 1):
        url = build_page_url(page)
        print(f"Downloading page {page}: {url}")
        html = fetch_page(url)

        print(f"Parsing page {page}...")
        quotes = parse_quotes_list(html)
        print(f"Quotes found on page {page}: {len(quotes)}")

        all_quotes.extend(quotes)

    print(f"Total quotes collected: {len(all_quotes)}")

    print("Saving to CSV...")
    save_csv(all_quotes, "quotes.csv")

    print("Done! File saved as quotes.csv.")


if __name__ == "__main__":
    main()



