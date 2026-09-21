# Lao Lottery (หวยลาว) Statistical Analysis & Backtest Toolkit

A Python + web-dashboard toolkit for a college research project analyzing
historical Lao lottery results. It is built around one honest research
question:

> **"Does the Lao lottery behave like a fair random process, and can any
> number-selection strategy actually beat chance over time?"**

It is **not** a number-prediction tool. Every strategy included in the
backtester is evaluated against a random baseline, and the expected
finding — consistent with the academic literature on lottery randomness
(see the companion research report) — is that **no strategy outperforms
random guessing over a large enough sample**. That null result *is* the
finding worth writing up.

## The real draw structure

Confirmed against a live sanook.com result page (16/9/69). There is only
**one draw per date**: a 6-digit number (`six_digit`). Every reported
prize category is the **trailing slice** of that same number:

```
358902   six_digit
 58902   five_digit   (last 5 digits)
  8902   four_digit   (last 4 digits)
   902   three_digit  (last 3 digits)
    02   two_digit    (last 2 digits)
```

None of these are separate, independent draws. The toolkit tests
`two_digit`/`three_digit`/`four_digit` as **joint/interaction**
distributions (do these digit *groups* line up uniformly, which can catch
correlation the single-digit-position tests miss) rather than as extra
independent draws — see `src/stats_analysis.py`.

## What's inside

```
lao_lottery_analysis/
├── data/
│   ├── sample_draws.csv        # SYNTHETIC demo data (400 draws) — full-featured demo
│   └── real_draws.csv          # REAL data — starts with 1 confirmed draw, grows via scraper
├── src/
│   ├── data_loader.py          # Load/validate draws, derive all sub-prizes
│   ├── stats_analysis.py       # Frequency, chi-square, runs test, autocorrelation
│   ├── strategies.py           # Example prediction strategies (all naive/baseline)
│   ├── backtest.py             # Walk-forward backtest engine (generalized to any target)
│   ├── report.py               # Static PNG charts for the markdown reports
│   └── dashboard.py            # Packages everything into the web dashboard's JSON
├── dashboard_template.html     # Self-contained interactive dashboard (edit freely)
├── scrape_today.py             # Real scraper — pulls today's result from sanook.com
├── main.py                     # Runs the full pipeline end-to-end
├── .github/workflows/analyze.yml  # Free scheduled scrape + analysis + auto-deploy
└── requirements.txt
```

## Two datasets, on purpose

- **`data/sample_draws.csv`** — 400 rows of synthetic random data, so the
  pipeline has something full-featured to demonstrate (charts, backtest,
  etc.) immediately. `python main.py` uses this by default.
- **`data/real_draws.csv`** — real data, starting from just the one draw
  confirmed by hand (16/9/69 → 358902). This is what the live dashboard
  on GitHub Pages runs on. It will be small for a while — the backtest
  and runs-test sections show a friendly "not enough data yet" message
  until there's enough (see below) — and grows by one real row every time
  `scrape_today.py` successfully runs.

## The scraper — real, but not yet verified end-to-end

`scrape_today.py` builds today's sanook.com URL
(`sanook.com/news/laolotto/DDMMYYYY/`, Buddhist-era year), fetches it,
extracts the `เลข 6 ตัว` number with a regex, and appends it to
`data/real_draws.csv`. If that URL doesn't resolve, it falls back to
searching sanook's lottery section listing page for a link to the right
date.

**I could not test this against the live site** — the sandbox this was
built in can only reach a short allow-list of software-package domains,
not news sites, so every request from here gets rejected before it even
reaches sanook.com. It's written defensively (logs every URL it tries and
why, and exits cleanly without crashing the rest of the pipeline if it
can't find a result), but the first real signal on whether the extraction
logic actually matches the live page will be the Actions log after your
first scheduled/manual run.

**If it doesn't work:** open the failed run in the **Actions** tab, open
the "Scrape today's result" step, and copy the log output back here —
especially the `GET ... -> status code` lines — so the extraction logic
can be fixed against real output instead of guessed blind.

## Running it locally

```bash
pip install -r requirements.txt
python main.py                           # uses data/sample_draws.csv (400 synthetic draws)
python main.py --data data/real_draws.csv # uses the real (currently tiny) dataset
python scrape_today.py                    # tries to scrape today's result into real_draws.csv
python scrape_today.py --date 2026-09-16  # scrape a specific past date instead
```

Output (in `output/`): `dashboard.html` (the interactive dashboard),
`randomness_report.md`, `backtest_report.md`, and two PNG charts.

## The web dashboard

`output/dashboard.html` is a single self-contained file — all analysis
results are embedded directly in it as inert JSON (inside a
`<script type="application/json">` tag, parsed defensively), so it works
by just opening it in a browser, with no server and no build step. If the
embedded data is ever malformed for any reason, the page shows a visible
on-page error instead of silently rendering blank. It shows:
- **§1** Per-digit uniformity — 6 mini bar charts + chi-square verdict
  (one per digit position of `six_digit`)
- **§2** Joint distribution — a heatmap + chi-square verdict, tabs for
  2/3/4 ตัว
- **§3** Runs test & autocorrelation summary table
- **§4** Backtest comparison — strategy table + cumulative-bankroll line
  chart, tabs per target category (shows a "not enough data yet" message
  until `real_draws.csv` has grown past the warm-up threshold)

Regenerate it any time with `python main.py` — it's a build output, so
edit `dashboard_template.html` (not `output/dashboard.html` directly) to
change the page itself.

## Methods included

**Randomness tests** (`stats_analysis.py`):
- Marginal chi-square goodness-of-fit vs. uniform, per digit position of
  `six_digit` (6 tests)
- Joint chi-square on `two_digit` (00–99), `three_digit` (000–999), and
  `four_digit` (0000–9999) — catches correlation between digit positions
  the marginal tests alone would miss
- Wald–Wolfowitz runs test (odd/even and above/below-median) on
  `two_digit` and `three_digit`
- Autocorrelation (ACF) on both, lags 1–10

All of the above gracefully report "not enough data yet" instead of
crashing when `real_draws.csv` is still small.

**Backtest strategies** (`strategies.py`) — all included specifically so
the backtest can show they do *not* beat chance:
- `RandomBaseline`, `HotNumbers`, `ColdNumbers`, `LastDrawRepeat`

**Backtest engine** (`backtest.py`): walk-forward evaluation, run once for
`two_digit` and once for `three_digit` — each strategy only ever sees
draws *before* the one it's predicting (no lookahead bias), computes hit
rate and ROI, and reports a binomial 95% confidence interval.

## Suggested structure for your college report

1. **Data & methodology** — cite your real sources, date range, and the
   confirmed draw structure (see the companion research report).
2. **Descriptive statistics** — frequency tables/heatmaps (dashboard §1–2).
3. **Randomness testing** — chi-square, runs test, autocorrelation and
   what they do/don't imply (dashboard §2–3, `randomness_report.md`).
4. **Backtest results** — hit rates, ROI, confidence intervals per
   strategy (dashboard §4, `backtest_report.md`).
5. **Discussion** — tie back to the literature (gambler's fallacy,
   hot-hand fallacy, negative expected value) on *why* the results come
   out the way they do.

## Running it for free on GitHub, with a live dashboard

**1. Push this code** (upload every file/folder inside
`lao_lottery_analysis/`, including the hidden `.github` folder).

**2. GitHub Actions runs it for free:**
`.github/workflows/analyze.yml` scrapes today's result, re-runs the full
analysis on `data/real_draws.csv`, and commits the results — on a
schedule (edit the `cron` line), on every push, or manually via **Run
workflow** in the **Actions** tab. 2,000 free minutes/month, unlimited on
public repos.

**3. GitHub Pages serves the live dashboard:**
The workflow copies `output/dashboard.html` to `docs/index.html` and
commits it. **Settings → Pages → Deploy from a branch → main → /docs →
Save.** After the next run, your dashboard is live at
`https://<username>.github.io/<repo>/`.

## Limitations to state explicitly in your writeup

- `two_digit`, `three_digit`, and `four_digit` are NOT independent draws —
  they're trailing slices of one 6-digit number. Their chi-square tests
  are joint/interaction checks, not additional independent randomness
  tests; keep that framing in your writeup too.
- The scraper's extraction logic was written against one confirmed
  example page and has not been verified across many dates — check the
  Actions log periodically to confirm it's still finding results
  correctly, especially if sanook changes its page layout.
- A backtest showing "no edge" over N draws does not prove no edge could
  ever exist in principle — it demonstrates none exists in this sample,
  which is the expected, theoretically predicted result for a fair,
  independent random process.
