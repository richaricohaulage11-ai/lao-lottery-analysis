"""
strategies.py
-------------
Example "number selection strategies" for the backtester, generalized to
work on any of the real, purchasable prize categories: two_digit,
three_digit, or four_digit — all trailing slices of the same 6-digit draw
(see data_loader.py).

Every strategy here is a common folk system (hot numbers, cold numbers,
repeat-recent). They are included specifically so the backtest can measure
whether any of them beat a random baseline — the academically expected
answer is no.

Each strategy is a callable: given the history of PAST draws only (no
lookahead), it returns a set of predicted number-strings (zero-padded to
the target column's width) of size `k` to bet on for the next draw.
"""
from __future__ import annotations

import random
from collections import Counter

import pandas as pd

TARGET_DIGITS = {
    "two_digit": 2,
    "three_digit": 3,
    "four_digit": 4,
}


def universe(target_column: str) -> list[str]:
    digits = TARGET_DIGITS[target_column]
    return [f"{i:0{digits}d}" for i in range(10 ** digits)]


class Strategy:
    name = "base"

    def __init__(self, target_column: str = "two_digit", k: int = 5):
        if target_column not in TARGET_DIGITS:
            raise ValueError(f"Unsupported target_column: {target_column}")
        self.target_column = target_column
        self.k = k

    def predict(self, history: pd.DataFrame) -> set[str]:
        raise NotImplementedError


class RandomBaseline(Strategy):
    """Control group: pick k numbers uniformly at random. Any strategy that
    cannot beat this over a large sample has no demonstrated edge."""

    name = "random_baseline"

    def __init__(self, target_column: str = "two_digit", k: int = 5, seed: int | None = None):
        super().__init__(target_column, k)
        self._rng = random.Random(seed)

    def predict(self, history: pd.DataFrame) -> set[str]:
        return set(self._rng.sample(universe(self.target_column), self.k))


class HotNumbers(Strategy):
    """Bet on the k most frequent numbers in a trailing window — the
    classic (fallacious) 'hot number' system."""

    name = "hot_numbers"

    def __init__(self, target_column: str = "two_digit", k: int = 5, window: int = 50):
        super().__init__(target_column, k)
        self.window = window

    def predict(self, history: pd.DataFrame) -> set[str]:
        recent = history.tail(self.window)
        counts = Counter(recent[self.target_column])
        for num in universe(self.target_column):
            counts.setdefault(num, 0)
        return set(num for num, _ in counts.most_common(self.k))


class ColdNumbers(Strategy):
    """Bet on the k least frequent ('overdue') numbers in a trailing
    window — the classic (fallacious) 'due number' / gambler's fallacy
    system."""

    name = "cold_numbers"

    def __init__(self, target_column: str = "two_digit", k: int = 5, window: int = 50):
        super().__init__(target_column, k)
        self.window = window

    def predict(self, history: pd.DataFrame) -> set[str]:
        recent = history.tail(self.window)
        counts = Counter(recent[self.target_column])
        for num in universe(self.target_column):
            counts.setdefault(num, 0)
        least_common = sorted(counts.items(), key=lambda kv: (kv[1], kv[0]))[: self.k]
        return {num for num, _ in least_common}


class LastDrawRepeat(Strategy):
    """Bet that recently-drawn numbers will repeat soon (a 'hot-hand'
    style system)."""

    name = "last_draw_repeat"

    def __init__(self, target_column: str = "two_digit", k: int = 5, lookback: int = 5):
        super().__init__(target_column, k)
        self.lookback = lookback

    def predict(self, history: pd.DataFrame) -> set[str]:
        recent_numbers = history.tail(self.lookback)[self.target_column].tolist()
        picks = list(dict.fromkeys(recent_numbers))
        if len(picks) < self.k:
            rng = random.Random(0)
            pool = [n for n in universe(self.target_column) if n not in picks]
            picks += rng.sample(pool, self.k - len(picks))
        return set(picks[: self.k])


ALL_STRATEGIES = [
    RandomBaseline,
    HotNumbers,
    ColdNumbers,
    LastDrawRepeat,
]
