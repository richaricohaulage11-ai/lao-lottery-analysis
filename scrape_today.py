"""
scrape_today.py
----------------
Scrapes recent Lao lottery results from sanook.com and appends any new
ones to a CSV in the format data_loader.py expects (draw_date,
four_digit).

Why backfill multiple days instead of just "today":
- The workflow may run before today's result is posted, or on a day the
  site skips.
- Running it once catches up on anything missed, and skips whatever is
  already in the CSV, so it's safe to run repeatedly.

CONFIRMED page format (verified against REAL scraped content, 14/9/69 and
18/9/69 — via sanook.com/news/laolotto/DDMMYYYY/):

    ลาว 18 กันยายน 2569 เลขท้าย 4 ตัว 3502 ชื่อนามสัตว์ : หอย
    เลขท้าย 3 ตัว 502 เลขท้าย 2 ตัว 02 หวยลาวพัฒนา 31 24 44 10 11

We only need the "เลขท้าย 4 ตัว" number — เลขท้าย 3/2 ตัว are just its
trailing digits, already derived automatically by data_loader.py. (The
page also reports a "ชื่อนามสัตว์" zodiac-animal name and a separate
"หวยลาวพัฒนา" 5-number game — both out of scope here.)

Strategy per date:
1. Build sanook's predictable date-slug URL
   (https://www.sanook.com/news/laolotto/DDMMYYYY/, Buddhist-era year)
   and follow redirects.
2. If that doesn't yield a match, fall back to fetching sanook's lottery
   section listing page and looking for a link whose text/href references
   the target date, then fetching that article instead.
3. Check the page for an explicit "no draw today" notice (e.g.
   "งดออกรางวัล") and log that as a distinct, expected outcome rather
   than an extraction failure.
4. Extract the 4-digit number via a regex anchored on the "เลขท้าย 4 ตัว"
   label.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import time
from datetime import date, timedelta

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    )
}

FOUR_DIGIT_RE = re.compile(r"เลขท้าย\s*4\s*ตัว\s*(\d{4})")
NO_DRAW_RE = re.compile(r"งดออกรางวัล|งดจำหน่าย|ไม่มีการออกรางวัล")
LISTING_URL = "https://www.sanook.com/news/laolotto/"


def to_buddhist_slug(d: date) -> str:
    """e.g. 2026-09-16 -> '16092569' (day, month, Buddhist-era year)."""
    be_year = d.year + 543
    return f"{d.day:02d}{d.month:02d}{be_year}"


def fetch(url: str) -> BeautifulSoup | None:
    try:
        resp = requests.get(url, headers=HEADERS, timeout=20, allow_redirects=True)
        print(f"    GET {url} -> {resp.status_code} (final url: {resp.url})")
        if resp.status_code != 200:
            return None
        return BeautifulSoup(resp.text, "html.parser")
    except requests.RequestException as e:
        print(f"    GET {url} -> FAILED: {e}")
        return None


def extract_four_digit(soup: BeautifulSoup) -> tuple[str | None, bool]:
    """Returns (four_digit_or_None, no_draw_detected)."""
    text = soup.get_text(" ", strip=True)
    if NO_DRAW_RE.search(text):
        return None, True
    match = FOUR_DIGIT_RE.search(text)
    if match:
        return match.group(1), False

    # DEBUG: extraction failed — dump what's actually on the page so the
    # regex can be fixed against real content instead of guessed blind.
    print("    [DEBUG] 'เลขท้าย 4 ตัว' not found. Page text around any 'เลข' occurrence:")
    found_any = False
    for m in re.finditer("เลข", text):
        start = max(0, m.start() - 20)
        end = min(len(text), m.start() + 80)
        print(f"      ...{text[start:end]}...")
        found_any = True
    if not found_any:
        print("    [DEBUG] No occurrence of 'เลข' anywhere on the page at all.")
        print(f"    [DEBUG] First 1500 chars of page text: {text[:1500]}")

    return None, False


def find_via_listing(target_date: date) -> str | None:
    """Fallback: search the lottery section listing for a link mentioning
    the target date, then fetch that article."""
    soup = fetch(LISTING_URL)
    if soup is None:
        return None

    be_year_2digit = str((target_date.year + 543) % 100).zfill(2)
    date_needle = f"{target_date.day}/{target_date.month}/{be_year_2digit}"

    for a in soup.find_all("a", href=True):
        if date_needle in a.get_text(" ", strip=True):
            href = a["href"]
            if href.startswith("/"):
                href = "https://www.sanook.com" + href
            print(f"    Listing match for {date_needle}: {href}")
            return href

    print(f"    No listing link found containing '{date_needle}'")
    links = soup.find_all("a", href=True)
    print(f"    [DEBUG] Page has {len(links)} links total. First 20 with non-empty text:")
    shown = 0
    for a in links:
        text = a.get_text(" ", strip=True)
        if text and shown < 20:
            print(f"      href={a['href']!r}  text={text[:80]!r}")
            shown += 1
    return None


def scrape_for_date(target_date: date) -> tuple[str | None, str]:
    """Returns (four_digit_or_None, status) where status is one of:
    'found', 'no_draw', 'not_found'."""
    slug_url = f"https://www.sanook.com/news/laolotto/{to_buddhist_slug(target_date)}/"
    print("  Attempt 1: date-slug URL")
    soup = fetch(slug_url)
    if soup:
        four, no_draw = extract_four_digit(soup)
        if four:
            print(f"    Found four_digit={four}")
            return four, "found"
        if no_draw:
            print("    Page explicitly says no draw was held this date.")
            return None, "no_draw"
        print("    Page loaded but 'เลขท้าย 4 ตัว' pattern not found in it.")

    print("  Attempt 2: listing page fallback")
    article_url = find_via_listing(target_date)
    if article_url:
        soup = fetch(article_url)
        if soup:
            four, no_draw = extract_four_digit(soup)
            if four:
                print(f"    Found four_digit={four}")
                return four, "found"
            if no_draw:
                print("    Page explicitly says no draw was held this date.")
                return None, "no_draw"
            print("    Article loaded but 'เลขท้าย 4 ตัว' pattern not found in it.")

    return None, "not_found"


def load_existing_dates(csv_path: str) -> set[str]:
    existing = set()
    try:
        with open(csv_path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                existing.add(row["draw_date"])
    except FileNotFoundError:
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["draw_date", "four_digit"])
    return existing


def append_row(csv_path: str, draw_date: date, four_digit: str) -> None:
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([draw_date.isoformat(), four_digit])
    print(f"  Appended {draw_date.isoformat()},{four_digit} to {csv_path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--start-offset", type=int, default=1,
        help="Days before today to START backfilling from (default 1 = yesterday, "
             "since today's result may not be posted yet when this runs)."
    )
    parser.add_argument(
        "--days-back", type=int, default=7,
        help="How many calendar days to check, counting back from --start-offset "
             "(default 7, so ~3 draw days are covered even with weekends skipped)."
    )
    parser.add_argument("--out", default="data/real_draws.csv")
    parser.add_argument(
        "--delay", type=float, default=1.0,
        help="Seconds to wait between each date's requests (politeness delay for "
             "large backfills — only applies between dates that actually get "
             "scraped, not skipped ones)."
    )
    args = parser.parse_args()

    existing_dates = load_existing_dates(args.out)

    found_count = 0
    no_draw_count = 0
    missed_count = 0
    already_have_count = 0

    for i in range(args.start_offset, args.start_offset + args.days_back):
        target_date = date.today() - timedelta(days=i)
        date_str = target_date.isoformat()

        if date_str in existing_dates:
            print(f"{date_str}: already in {args.out}, skipping")
            already_have_count += 1
            continue

        if target_date.weekday() not in (0, 2, 4):  # Mon/Wed/Fri only
            print(f"{date_str}: not a scheduled draw day (Mon/Wed/Fri only), skipping")
            no_draw_count += 1
            continue

        print(f"{date_str}: scraping...")
        four_digit, status = scrape_for_date(target_date)
        time.sleep(args.delay)

        if status == "found":
            append_row(args.out, target_date, four_digit)
            existing_dates.add(date_str)
            found_count += 1
        elif status == "no_draw":
            print(f"{date_str}: no draw held this date (confirmed by page) — not an error")
            no_draw_count += 1
        else:
            print(f"{date_str}: could not find or extract a result — leaving for next run")
            missed_count += 1

    print(
        f"\nSummary: {found_count} new draw(s) added, {no_draw_count} confirmed "
        f"no-draw day(s), {missed_count} unresolved, {already_have_count} already "
        f"had data."
    )
    # Always exit 0 — a scrape miss should never fail the whole pipeline;
    # the rest of the workflow still runs on whatever data already exists.
    sys.exit(0)


if __name__ == "__main__":
    main()
