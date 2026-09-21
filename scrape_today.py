"""
scrape_today.py
----------------
Scrapes today's (or a given date's) Lao lottery result from sanook.com and
appends it to a CSV in the format data_loader.py expects (draw_date,
six_digit).

Confirmed page format (verified against a live page, 16/9/69):

    ผลหวยลาววันนี้ 16/9/69 ออกอะไรบ้าง
    • เลข 6 ตัว : 358902
    • เลข 5 ตัว : 58902
    • เลข 4 ตัว : 8902
    • เลข 3 ตัว : 902
    • เลข 2 ตัว : 02

We only need the six_digit line — everything else is derived by
data_loader.py automatically.

IMPORTANT: this has NOT been tested against a live network call (the
sandbox this was written in cannot reach sanook.com). It should work
against GitHub Actions runners, which do have normal internet access, but
if the extraction fails, check the Action's log output (this script logs
what it fetched and why extraction did/didn't succeed) and share it back
for a fix.

Strategy:
1. Build sanook's predictable date-slug URL for the target date
   (https://www.sanook.com/news/laolotto/DDMMYYYY/, Buddhist-era year)
   and follow redirects — sanook's CMS is expected to 30x-redirect this to
   the real numeric article URL (e.g. /news/9906791/).
2. If that doesn't yield a match, fall back to fetching sanook's lottery
   section listing page and looking for a link whose text/href references
   the target date, then fetching that article instead.
3. Extract the six-digit number via a regex anchored on the "เลข 6 ตัว"
   label, which is the only number this project actually needs.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import time
from datetime import date, datetime, timedelta

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    )
}

SIX_DIGIT_RE = re.compile(r"เลข\s*6\s*ตัว\s*:?\s*(\d{6})")
LISTING_URL = "https://www.sanook.com/news/laolotto/"


def to_buddhist_slug(d: date) -> str:
    """e.g. 2026-09-16 -> '16092569' (day, month, Buddhist-era year)."""
    be_year = d.year + 543
    return f"{d.day:02d}{d.month:02d}{be_year}"


def fetch(url: str) -> BeautifulSoup | None:
    try:
        resp = requests.get(url, headers=HEADERS, timeout=20, allow_redirects=True)
        print(f"  GET {url} -> {resp.status_code} (final url: {resp.url})")
        if resp.status_code != 200:
            return None
        return BeautifulSoup(resp.text, "html.parser")
    except requests.RequestException as e:
        print(f"  GET {url} -> FAILED: {e}")
        return None


def extract_six_digit(soup: BeautifulSoup) -> str | None:
    text = soup.get_text(" ", strip=True)
    match = SIX_DIGIT_RE.search(text)
    return match.group(1) if match else None


def find_via_listing(target_date: date) -> str | None:
    """Fallback: search the lottery section listing for a link mentioning
    the target date, then fetch that article."""
    soup = fetch(LISTING_URL)
    if soup is None:
        return None

    # Thai date strings this might appear as, e.g. "16/9/69" or "16 ก.ย. 69"
    be_year_2digit = str((target_date.year + 543) % 100).zfill(2)
    date_needle = f"{target_date.day}/{target_date.month}/{be_year_2digit}"

    for a in soup.find_all("a", href=True):
        if date_needle in a.get_text(" ", strip=True):
            href = a["href"]
            if href.startswith("/"):
                href = "https://www.sanook.com" + href
            print(f"  Listing match for {date_needle}: {href}")
            return href
    print(f"  No listing link found containing '{date_needle}'")
    return None


def scrape_for_date(target_date: date) -> str | None:
    slug_url = f"https://www.sanook.com/news/laolotto/{to_buddhist_slug(target_date)}/"
    print(f"Attempt 1: date-slug URL")
    soup = fetch(slug_url)
    if soup:
        six = extract_six_digit(soup)
        if six:
            print(f"  Found six_digit={six}")
            return six
        print("  Page loaded but 'เลข 6 ตัว' pattern not found in it.")

    print(f"Attempt 2: listing page fallback")
    article_url = find_via_listing(target_date)
    if article_url:
        soup = fetch(article_url)
        if soup:
            six = extract_six_digit(soup)
            if six:
                print(f"  Found six_digit={six}")
                return six
            print("  Article loaded but 'เลข 6 ตัว' pattern not found in it.")

    return None


def append_if_new(csv_path: str, draw_date: date, six_digit: str) -> bool:
    """Append a row unless that date is already present. Returns True if written."""
    date_str = draw_date.isoformat()
    existing_dates = set()
    try:
        with open(csv_path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                existing_dates.add(row["draw_date"])
    except FileNotFoundError:
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["draw_date", "six_digit"])

    if date_str in existing_dates:
        print(f"{date_str} already present in {csv_path}, skipping.")
        return False

    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([date_str, six_digit])
    print(f"Appended {date_str},{six_digit} to {csv_path}")
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", help="YYYY-MM-DD (default: today)")
    parser.add_argument("--out", default="data/real_draws.csv")
    args = parser.parse_args()

    target_date = (
        datetime.strptime(args.date, "%Y-%m-%d").date() if args.date else date.today()
    )

    print(f"Scraping Lao lottery result for {target_date.isoformat()}...")
    six_digit = scrape_for_date(target_date)

    if six_digit is None:
        print(
            "Could not find a result for this date (maybe no draw that day, "
            "or the site's page structure changed). Exiting without error "
            "so the rest of the pipeline still runs on existing data."
        )
        sys.exit(0)

    append_if_new(args.out, target_date, six_digit)


if __name__ == "__main__":
    main()
