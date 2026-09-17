"""
scraper_template.py
--------------------
TEMPLATE ONLY. This is not run inside this sandbox (its network is locked
to a short allow-list of package registries and cannot reach news/lottery
sites). Run this on your own machine after adjusting the CSS selectors to
match the page you're scraping — every site's HTML is different and can
change without notice, so treat the selectors below as a starting point,
not a working scraper.

Install first:
    pip install requests beautifulsoup4

Usage sketch:
    python scraper_template.py --url "<a single draw-result page URL>"

Ethics/practice notes (see README and companion research report):
- Check the site's robots.txt and terms of use before scraping.
- Throttle requests (e.g. time.sleep(1-2) between pages).
- Cross-check every draw against at least one independent source.
- Store the source URL and retrieval timestamp alongside every row.
"""
from __future__ import annotations

import argparse
import csv
import re
import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (research project data collection; contact: <your email>)"
    )
}


def fetch_page(url: str) -> BeautifulSoup:
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def extract_draw_numbers(soup: BeautifulSoup) -> dict | None:
    """PLACEHOLDER extraction logic.

    Real news/result pages usually show the numbers as plain text near
    labels like '4 ตัว' and '2 ตัวล่าง'. Inspect the actual page HTML
    (browser dev tools -> Elements) and replace this with selectors that
    target the right elements, e.g.:

        four = soup.select_one(".lottery-result .four-digit").get_text(strip=True)
        two_bottom = soup.select_one(".lottery-result .two-bottom").get_text(strip=True)

    As a rough fallback, this searches the page text for a 4-digit number
    near a "4 ตัว" label and a 2-digit number near a "2 ตัวล่าง" label —
    verify every result manually before use, since exact wording and page
    structure differ by site and can change without notice.
    """
    text = soup.get_text(" ", strip=True)
    four_match = re.search(r"4\s*ตัว[^0-9]{0,20}(\d{4})", text)
    bottom_match = re.search(r"2\s*ตัวล่าง[^0-9]{0,20}(\d{2})", text)
    if not four_match or not bottom_match:
        return None
    return {"four_digit": four_match.group(1), "two_digit_bottom": bottom_match.group(1)}


def scrape_one(url: str) -> dict:
    soup = fetch_page(url)
    numbers = extract_draw_numbers(soup)
    return {
        "source_url": url,
        "retrieved_at": datetime.utcnow().isoformat(),
        "four_digit": numbers["four_digit"] if numbers else None,
        "two_digit_bottom": numbers["two_digit_bottom"] if numbers else None,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="A single draw-result page URL")
    parser.add_argument("--out", default="scraped_draw.csv")
    args = parser.parse_args()

    result = scrape_one(args.url)
    print(result)

    if result["four_digit"] is None or result["two_digit_bottom"] is None:
        print(
            "WARNING: could not auto-extract both numbers from this page. "
            "Open the page's HTML and adjust extract_draw_numbers()."
        )
        return

    with open(args.out, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["source_url", "retrieved_at", "four_digit", "two_digit_bottom"]
        )
        if f.tell() == 0:
            writer.writeheader()
        writer.writerow(result)

    time.sleep(1)  # be polite if you loop this over many URLs


if __name__ == "__main__":
    main()
