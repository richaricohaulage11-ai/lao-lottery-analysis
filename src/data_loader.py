"""
data_loader.py
--------------
Load Lao lottery draw data from CSV.

CONFIRMED draw structure (verified against a live sanook.com result page,
16/9/69): there is only ONE draw per date — a 6-digit number (six_digit).
Every reported prize category is the TRAILING slice of that same number:

    six_digit    358902
    five_digit    58902   (last 5 digits)
    four_digit     8902   (last 4 digits)
    three_digit     902   (last 3 digits)
    two_digit        02   (last 2 digits)

None of these are independent draws — they all come from one 6-digit
result. Statistically:
- The 6 digit positions (d0..d5) are the closest thing to independent
  atomic random variables.
- two_digit / three_digit / four_digit are useful to test too, but as
  JOINT-distribution (interaction) checks on trailing groups of digit
  positions, not as additional independent draws. See stats_analysis.py.
"""
from __future__ import annotations

import pandas as pd


REQUIRED_COLUMNS = {"draw_date", "six_digit"}


def load_draws(csv_path: str) -> pd.DataFrame:
    """Load a draws CSV and return a tidy DataFrame with derived columns.

    Expected input columns:
        draw_date   YYYY-MM-DD
        six_digit   the 6-digit draw, as a 6-char string (keep as text so
                    leading zeros survive, e.g. "058902")

    Derived columns added: five_digit, four_digit, three_digit, two_digit
    (all trailing slices of six_digit), per-position digit columns d0..d5
    (d0 = leftmost), and weekday.
    """
    df = pd.read_csv(csv_path, dtype={"six_digit": str})

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"CSV is missing required column(s): {missing}")

    df["six_digit"] = df["six_digit"].str.strip().str.zfill(6)

    bad = df[~df["six_digit"].str.fullmatch(r"\d{6}")]
    if len(bad):
        raise ValueError(
            f"{len(bad)} row(s) have a six_digit value that is not exactly "
            f"6 digits, e.g.: {bad['six_digit'].head().tolist()}"
        )

    df["draw_date"] = pd.to_datetime(df["draw_date"])
    df = df.sort_values("draw_date").reset_index(drop=True)
    df = df.drop_duplicates(subset="draw_date", keep="last").reset_index(drop=True)

    df["five_digit"] = df["six_digit"].str[1:]
    df["four_digit"] = df["six_digit"].str[2:]
    df["three_digit"] = df["six_digit"].str[3:]
    df["two_digit"] = df["six_digit"].str[4:]

    for i in range(6):
        df[f"d{i}"] = df["six_digit"].str[i].astype(int)

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
