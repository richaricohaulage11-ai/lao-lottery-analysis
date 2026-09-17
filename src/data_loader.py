"""
data_loader.py
--------------
Load Lao lottery draw data from CSV.

CORRECTED draw structure: there is only ONE draw per date — a 4-digit
number (four_digit, d0 d1 d2 d3). Every reported sub-prize is a slice of
that same number:

    four_digit        d0 d1 d2 d3
    two_digit_bottom  d0 d1        <- "2 ตัวล่าง" = the LEADING 2 digits
    three_digit_top   d1 d2 d3     <- "3 ตัวบน"   = the trailing 3 digits
    two_digit_top     d2 d3        <- "2 ตัวบน"   = the trailing 2 digits

None of these are independent draws — they all come from one 4-digit
result. Statistically:
- The 4 digit positions (d0..d3) are the closest thing to independent
  atomic random variables (assuming each position is drawn from its own
  mechanism, as is typical for these lotteries).
- two_digit_top / two_digit_bottom / three_digit_top are useful to test
  too, but as JOINT-distribution (interaction) checks on pairs/triples of
  digit positions — e.g. does d0 correlate with d1 — not as additional
  independent draws. See stats_analysis.py for how this is framed.
"""
from __future__ import annotations

import pandas as pd


REQUIRED_COLUMNS = {"draw_date", "four_digit"}


def load_draws(csv_path: str) -> pd.DataFrame:
    """Load a draws CSV and return a tidy DataFrame with derived columns.

    Expected input columns:
        draw_date    YYYY-MM-DD
        four_digit   the 4-digit draw, as a 4-char string (keep as text
                     so leading zeros survive, e.g. "0894")

    Derived columns added: two_digit_bottom, three_digit_top, two_digit_top
    (see module docstring for exactly how each is sliced), per-position
    digit columns d0..d3 (d0 = leftmost), and weekday.
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

    df["two_digit_bottom"] = df["four_digit"].str[0:2]   # leading 2 (2 ตัวล่าง)
    df["three_digit_top"] = df["four_digit"].str[1:4]    # trailing 3 (3 ตัวบน)
    df["two_digit_top"] = df["four_digit"].str[2:4]       # trailing 2 (2 ตัวบน)

    for i in range(4):
        df[f"d{i}"] = df["four_digit"].str[i].astype(int)

    df["weekday"] = df["draw_date"].dt.day_name()

    return df


def basic_summary(df: pd.DataFrame) -> str:
    """Return a short plain-text summary of the loaded dataset."""
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
