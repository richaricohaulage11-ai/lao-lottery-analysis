"""
data_loader.py
--------------
Load Lao lottery draw data from CSV.

CONFIRMED draw structure (verified against REAL scraped page content,
14/9/69 and 18/9/69 — see scrape_today.py debug log history): there is
only ONE draw per date — a 4-digit number (four_digit, labeled
"เลขท้าย 4 ตัว" on sanook.com). The lower prizes are trailing slices:

    four_digit    3502   ("เลขท้าย 4 ตัว")
    three_digit    502   ("เลขท้าย 3 ตัว" — last 3 digits)
    two_digit       02   ("เลขท้าย 2 ตัว" — last 2 digits)

None of these are independent draws — they all come from one 4-digit
result. Statistically:
- The 4 digit positions (d0..d3) are the closest thing to independent
  atomic random variables.
- two_digit / three_digit are useful to test too, but as JOINT-
  distribution (interaction) checks on trailing groups of digit
  positions, not as additional independent draws. See stats_analysis.py.

(The source page also reports a "ชื่อนามสัตว์" zodiac-animal name derived
from the 2-digit number, and a separate "หวยลาวพัฒนา" 5-number game — both
out of scope for this toolkit, which focuses on the 4-digit chain.)
"""
from __future__ import annotations

import pandas as pd


REQUIRED_COLUMNS = {"draw_date", "four_digit"}


def load_draws(csv_path: str) -> pd.DataFrame:
    """Load a draws CSV and return a tidy DataFrame with derived columns.

    Expected input columns:
        draw_date    YYYY-MM-DD
        four_digit   the 4-digit draw, as a 4-char string (keep as text so
                     leading zeros survive, e.g. "0344")

    Derived columns added: three_digit, two_digit (trailing slices of
    four_digit), per-position digit columns d0..d3 (d0 = leftmost), and
    weekday.
    """
    df = pd.read_csv(csv_path, dtype={"four_digit": str})

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"CSV is missing required column(s): {missing}")

    df["four_digit"] = df["four_digit"].str.strip().str.zfill(4)

    bad = df[~df["four_digit"].str.fullmatch(r"\d{4}")]
    if len(bad):
        raise ValueError(
            f"{len(bad)} row(s) have a four_digit value that is not exactly "
            f"4 digits, e.g.: {bad['four_digit'].head().tolist()}"
        )

    df["draw_date"] = pd.to_datetime(df["draw_date"])
    df = df.sort_values("draw_date").reset_index(drop=True)
    df = df.drop_duplicates(subset="draw_date", keep="last").reset_index(drop=True)

    df["three_digit"] = df["four_digit"].str[1:]
    df["two_digit"] = df["four_digit"].str[2:]

    for i in range(4):
        df[f"d{i}"] = df["four_digit"].str[i].astype(int)

    df["weekday"] = df["draw_date"].dt.day_name()

    return df


def basic_summary(df: pd.DataFrame) -> str:
    lines = [
        f"Draws loaded: {len(df)}",
        f"Date range: {df['draw_date'].min().date()} to {df['draw_date'].max().date()}",
        f"Weekday counts: {df['weekday'].value_counts().to_dict()}",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    import sys

    path = sys.argv[1] if len(sys.argv) > 1 else "data/sample_draws.csv"
    data = load_draws(path)
    print(basic_summary(data))
    print(data.head())
