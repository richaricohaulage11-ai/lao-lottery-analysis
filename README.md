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

There is only **one draw per date**: a 4-digit number (`four_digit`).
Every reported prize category is a slice of that same number — none of
them are separate, independent draws:

```
four_digit         d0 d1 d2 d3
two_digit_bottom   d0 d1          <- "2 ตัวล่าง" = the LEADING 2 digits
three_digit_top    d1 d2 d3       <- "3 ตัวบน"   = the trailing 3 digits
two_digit_top      d2 d3          <- "2 ตัวบน"   = the trailing 2 digits
```

This matters statistically: `two_digit_top` and `two_digit_bottom` share
a digit (d1 is not in either — check your source's exact rule if it
differs), and none of the three should be treated as if they were drawn
independently of `four_digit`. The toolkit tests them as **joint/
interaction** distributions (do these digit *pairs* line up uniformly,
which can catch correlation the single-digit tests miss) rather than as
extra independent draws — see `src/stats_analysis.py`.

## What's inside

```
lao_lottery_analysis/
├── data/
│   └── sample_draws.csv        # SYNTHETIC demo data — replace with real draws
├── src/
│   ├── data_loader.py          # Load/validate draws, derive all sub-prizes
│   ├── stats_analysis.py       # Frequency, chi-square, runs test, autocorrelation
│   ├── strategies.py           # Example prediction strategies (all naive/baseline)
│   ├── backtest.py             # Walk-forward backtest engine (generalized to any target)
│   ├── report.py               # Static PNG charts for the markdown reports
│   └── dashboard.py            # Packages everything into the web dashboard's JSON
├── dashboard_template.html     # Self-contained interactive dashboard (edit freely)
├── scraper_template.py         # TEMPLATE ONLY — not run here, see note below
├── main.py                     # Runs the full pipeline end-to-end
├── .github/workflows/analyze.yml  # Free scheduled runs + auto-deploy to GitHub Pages
└── requirements.txt
```

## Getting real data (important)

This sandbox's network is locked to a short allow-list of software-package
domains and **cannot reach lottery result sites**, so this toolkit ships
with **synthetic random demo data** in `data/sample_draws.csv` just so the
pipeline runs end-to-end out of the box.

To do real analysis:
1. On your own machine, use `scraper_template.py` as a starting point (it
   needs `requests` + `beautifulsoup4`; its extraction logic is a rough
   placeholder you'll need to adjust to whichever site you scrape, since
   each site's HTML differs and can change over time).
2. Or manually collect draws into the CSV format below from at least two
   independent sources per draw, cross-checked.
3. Replace `data/sample_draws.csv` with your real file, or pass
   `--data path/to/your.csv` to `main.py`.

**CSV format** (one row per draw — only two columns needed, everything
else is derived automatically):
```
draw_date,four_digit
2026-09-16,3721
2026-09-14,0894
```
`draw_date` is `YYYY-MM-DD`. Keep `four_digit` as **text**, zero-padded to
4 characters (e.g. `0894`, not `894`) — the loader zero-pads automatically,
but keep the CSV column as text/string dtype in Excel/pandas or leading
zeros get stripped before the loader ever sees them.

## Running it

```bash
pip install -r requirements.txt
python main.py                          # uses the bundled sample data
python main.py --data data/real.csv     # uses your own data
```

This produces, in `output/`:
- **`dashboard.html`** — the interactive web dashboard (open it directly in
  a browser, no server needed)
- `randomness_report.md` — chi-square, runs test, and autocorrelation
  results with interpretation
- `backtest_report.md` — hit rates and ROI for every strategy vs. the
  random baseline, for both `two_digit_bottom` and `two_digit_top`
- `frequency_charts.png`, `backtest_curve.png` — static chart versions for
  pasting into a Word doc/PDF report

## The web dashboard

`output/dashboard.html` is a single self-contained file — all analysis
results are embedded directly in it as JSON, so it works by just opening
it in a browser, with no server, no build step, and no separate data file
to keep track of. It shows:
- **§1** Per-digit uniformity — 4 mini bar charts + chi-square verdict
- **§2** Joint distribution — a 10×10 heatmap + chi-square verdict, with
  tabs for 2 ตัวล่าง / 2 ตัวบน / 3 ตัวบน
- **§3** Runs test & autocorrelation summary table
- **§4** Backtest comparison — strategy table (hit rate, 95% CI, ROI,
  verdict) + cumulative-bankroll line chart, with tabs per target category

Every "significant" vs. "consistent with random" verdict is color-coded
(muted red vs. green) so a reader can scan the whole page at a glance.
Regenerate it any time by re-running `python main.py` — it's a build
output, so edit `dashboard_template.html` (not `output/dashboard.html`
directly) if you want to change the page itself.

## Methods included

**Randomness tests** (`stats_analysis.py`):
- Marginal chi-square goodness-of-fit vs. uniform, per digit position of
  `four_digit` (4 tests)
- Joint chi-square on `two_digit_bottom`, `two_digit_top` (00–99) and
  `three_digit_top` (000–999) — catches correlation between digit
  positions that the marginal tests alone would miss
- Wald–Wolfowitz runs test (odd/even and above/below-median) on
  `two_digit_bottom` and `two_digit_top`
- Autocorrelation (ACF) on both, lags 1–10

**Backtest strategies** (`strategies.py`) — all included specifically so
the backtest can show they do *not* beat chance:
- `RandomBaseline` — picks numbers uniformly at random (the control group)
- `HotNumbers` — bets on the N most frequent numbers in a trailing window
- `ColdNumbers` — bets on the N least frequent numbers ("overdue" logic)
- `LastDrawRepeat` — bets that recent numbers will repeat

**Backtest engine** (`backtest.py`): walk-forward evaluation, run once for
`two_digit_bottom` and once for `two_digit_top` — each strategy only ever
sees draws *before* the one it's predicting (no lookahead bias), computes
hit rate and ROI, and reports a binomial 95% confidence interval so you
can say whether any observed edge is statistically distinguishable from
noise.

## Suggested structure for your college report

1. **Data & methodology** — cite your real sources, date range, and which
   draw structure you confirmed (see the companion research report).
2. **Descriptive statistics** — frequency tables/heatmaps (dashboard §1–2).
3. **Randomness testing** — chi-square, runs test, autocorrelation and
   what they do/don't imply (dashboard §2–3, `randomness_report.md`).
4. **Backtest results** — hit rates, ROI, confidence intervals per
   strategy (dashboard §4, `backtest_report.md`).
5. **Discussion** — tie back to the literature (gambler's fallacy,
   hot-hand fallacy, negative expected value) on *why* the results come
   out the way they do.

## Running it for free on GitHub, with a live dashboard

**1. Create the repo and push this code** (see the step-by-step no-terminal
walkthrough from earlier in this conversation if you haven't used GitHub
before — upload every file/folder *inside* `lao_lottery_analysis/`,
including the hidden `.github` folder).

**2. Run it automatically for free with GitHub Actions:**
`.github/workflows/analyze.yml` runs on a schedule (edit the `cron` line to
match the real draw days), or manually via the **Run workflow** button in
the **Actions** tab. Every account gets **2,000 free minutes/month**
(unlimited on public repos) — this workflow finishes in well under a
minute per run. It installs dependencies, runs `main.py`, and commits the
updated `output/` files straight back to your repo.

**3. Get a live, shareable dashboard link with GitHub Pages:**
The workflow also copies `output/dashboard.html` to `docs/index.html` and
commits it. To turn that into a public link:
- Go to your repo's **Settings → Pages**
- Under **Build and deployment → Source**, choose **Deploy from a branch**
- Branch: `main`, folder: **`/docs`** → **Save**
- After the next workflow run, GitHub shows you a URL like
  `https://<username>.github.io/lao-lottery-analysis/` — that's your live,
  auto-updating dashboard. Share this link with your advisor instead of a
  file.

**4. Getting real scraped data to run in the cloud:**
This sandbox's network can't reach lottery sites, but **GitHub's own
runners have normal internet access**, so that's the right place to run a
real scraper. Adapt `scraper_template.py` into a working scraper for your
chosen source (test it locally first), then uncomment the "Scrape latest
draw" step in `analyze.yml` so each scheduled run appends that day's
result to your dataset before re-running the analysis and updating the
dashboard. Over a few months this builds a real, continuously-growing
dataset for free, with the dashboard staying current automatically.

## Limitations to state explicitly in your writeup

- The bundled sample data is **synthetic**, for pipeline demonstration
  only — all real conclusions must come from data you collect yourself.
- `two_digit_bottom`, `two_digit_top`, and `three_digit_top` are NOT
  independent draws — they're slices of one 4-digit number. The dashboard
  frames their chi-square tests as joint/interaction checks, not as
  additional independent randomness tests; keep that framing in your
  writeup too.
- The `three_digit_top` joint test needs roughly 5,000+ draws for reliable
  expected cell counts (1,000 categories × 5 minimum) — with a realistic
  sample size, treat that specific test's result cautiously and say so.
- A backtest showing "no edge" over N draws does not prove no edge could
  ever exist in principle — it demonstrates none exists in this sample,
  which is the expected, theoretically predicted result for a fair,
  independent random process.
