"""
scrape_today.py
----------------
Scrapes recent Lao lottery results from sanook.com and appends any new
ones to a CSV in the format data_loader.py expects (draw_date, six_digit).

Why backfill multiple days instead of just "today":
- The workflow may run before today's result is posted, or on a day the
  site skips.
- Running it once catches up on anything missed, and skips whatever is
  already in the CSV, so it's safe to run repeatedly.

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
if extraction fails, check the Action's log output (this script logs what
it fetched and why extraction did/didn't succeed) and share it back for a
fix.

Strategy per date:
1. Build sanook's predictable date-slug URL
   (https://www.sanook.com/news/laolotto/DDMMYYYY/, Buddhist-era year)
   and follow redirects — sanook's CMS is expected to 30x-redirect this to
   the real numeric article URL (e.g. /news/9906791/).
2. If that doesn't yield a match, fall back to fetching sanook's lottery
   section listing page and looking for a link whose text/href references
   the target date, then fetching that article instead.
3. Check the page for an explicit "no draw today" notice (e.g.
   "งดออกรางวัล") and log that as a distinct, expected outcome rather
   than an extraction failure.
4. Extract the six-digit number via a regex anchored on the "เลข 6 ตัว"
   label.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
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


def extract_six_digit(soup: BeautifulSoup) -> tuple[str | None, bool]:
    """Returns (six_digit_or_None, no_draw_detected)."""
    text = soup.get_text(" ", strip=True)
    if NO_DRAW_RE.search(text):
        return None, True
    match = SIX_DIGIT_RE.search(text)
    if match:
        return match.group(1), False

    # DEBUG: extraction failed — dump what's actually on the page so the
    # regex can be fixed against real content instead of guessed blind.
    print("    [DEBUG] 'เลข 6 ตัว' not found. Page text around any 'เลข' occurrence:")
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
    # DEBUG: dump the first ~20 links' text + href so the real date format
    # used on the listing page can be seen and matched against.
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
    """Returns (six_digit_or_None, status) where status is one of:
    'found', 'no_draw', 'not_found'."""
    slug_url = f"https://www.sanook.com/news/laolotto/{to_buddhist_slug(target_date)}/"
    print("  Attempt 1: date-slug URL")
    soup = fetch(slug_url)
    if soup:
        six, no_draw = extract_six_digit(soup)
        if six:
            print(f"    Found six_digit={six}")
            return six, "found"
        if no_draw:
            print("    Page explicitly says no draw was held this date.")
            return None, "no_draw"
        print("    Page loaded but 'เลข 6 ตัว' pattern not found in it.")

    print("  Attempt 2: listing page fallback")
    article_url = find_via_listing(target_date)
    if article_url:
        soup = fetch(article_url)
        if soup:
            six, no_draw = extract_six_digit(soup)
            if six:
                print(f"    Found six_digit={six}")
                return six, "found"
            if no_draw:
                print("    Page explicitly says no draw was held this date.")
                return None, "no_draw"
            print("    Article loaded but 'เลข 6 ตัว' pattern not found in it.")

    return None, "not_found"


def load_existing_dates(csv_path: str) -> set[str]:
    existing = set()
    try:
        with open(csv_path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                existing.add(row["draw_date"])
    except FileNotFoundError:
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["draw_date", "six_digit"])
    return existing


def append_row(csv_path: str, draw_date: date, six_digit: str) -> None:
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([draw_date.isoformat(), six_digit])
    print(f"  Appended {draw_date.isoformat()},{six_digit} to {csv_path}")


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
        six_digit, status = scrape_for_date(target_date)

        if status == "found":
            append_row(args.out, target_date, six_digit)
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
