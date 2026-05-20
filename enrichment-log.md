# Enrichment + Cleanup Log

Run: 2026-05-04 — corporate-finance-with-ai

## What changed

### Build infrastructure added

`bash build.sh` now produces `output/corporate-finance-with-ai.epub` and `output/corporate-finance-with-ai.html`. Build verified clean: 17 chapter splits (frontmatter + preface + 15 content chapters).

Files added: `metadata.yaml`, `styles/kindle.css`, `styles/kindle-book.css`, `build.sh` (executable), `images/` directory.

### Pass 3 — 15 portrait stubs inserted

| Ch | Subject | Era | Source type |
|---|---|---|---|
| 1 | Donaldson Brown (1885–1965) | c. 1920s | photograph |
| 2 | Mary Harris Smith (1844–1934) | c. 1920 | photograph |
| 3 | John Hicks (1904–1989) | c. 1940s | photograph |
| 4 | Joel Dean (1906–1979) | c. 1950s | photograph |
| 5 | Fischer Black (1938–1995) | c. 1980s | photograph |
| 6 | Irving Fisher (1867–1947) | c. 1920s | photograph |
| 7 | Merton Miller (1923–2000) | c. 1990 | photograph |
| 8 | Adolf A. Berle (1895–1971) | c. 1940s | photograph |
| 9 | Gardiner C. Means (1896–1988) | c. 1940s | photograph |
| 10 | Maggie Lena Walker (1864–1934) | c. 1910 | photograph |
| 11 | Edith Penrose (1914–1996) | c. 1960s | photograph |
| 12 | Karl Borch (1919–1986) | c. 1970s | photograph |
| 13 | Susan Strange (1923–1998) | c. 1980s | photograph |
| 14 | Daniel Bernoulli (1700–1782) | c. 1750 | **engraving** (pre-1850s) |
| 15 | Joseph Schumpeter (1883–1950) | c. 1940s | photograph |

### Pass 1 — 32 tables rendered

Distribution: Ch 1 (2), Ch 2 (3), Ch 3 (2), Ch 4 (2), Ch 5 (2), Ch 6 (2), Ch 7 (1), Ch 8 (3), Ch 9 (3), Ch 10 (1), Ch 11 (2), Ch 12 (1), Ch 13 (3), Ch 14 (3), Ch 15 (2). Highlights: the five-job decomposition of "should we fund Plant 4 with debt or equity?" and the three-beat method applied to Maya's memo (Ch 1); the conservative-vs-aggressive accrual posture and the three-firm AR-aging-tells-three-stories table (Ch 2); the three-lever / cash-freed-per-day comparison (Ch 3); the Plant 4 FCFF build and the three-failure-mode pre-flight checklist (Ch 4); the WACC sensitivity grid (Ch 5); the four-MM-assumptions table (Ch 7); the three-firm optimal-leverage comparison showing how the same framework yields 25–40% / 5–15% / 50–60% (Ch 8); Maya's payout recommendation summary (Ch 9); the synergy haircut model (Ch 11); the Halverson hedging program summary (Ch 12); the three-types-of-FX-exposure comparison (Ch 13); the pre-mortem-vs-standard-risk-section table and the five pre-mortem scenarios with named indicators and predetermined responses (Ch 14); the capital-deployment summary and the payout-with-decision-triggers table (Ch 15).

### Pass 2 — 9 SVG/PNG figures generated

All figures in editorial monochrome warm-grayscale, Georgia serif, 1px borders, no rounded corners or gradients. PNGs at 2× the SVG viewBox.

| Slug | Topic |
|---|---|
| 03-…-fig-01 | Three-bucket cash-in-transit diagram (AR / Inventory / AP) |
| 03-…-fig-02 | Cash conversion cycle as a horizontal timeline (60 + 60 − 35 = 85 days) |
| 03-…-fig-03 | Org-chart mapping CCC components to functions with cross-tension arrows |
| 05-…-fig-01 | Decision tree for choosing the right discount rate (firm WACC / project β / management uplift) |
| 06-…-fig-01 | Unlevering / relevering project beta via Hamada |
| 06-…-fig-02 | Plant 4 deferral-option decision tree with strong / weak demand branches |
| 12-…-fig-01 | Three frictions that make hedging valuable (distress / tax convexity / pipeline preservation) |
| 12-…-fig-02 | Transaction (cash-real, hedge) vs. translation (accounting, do not hedge) FX exposure |
| 15-…-fig-01 | Four-quadrant diagram of the four interdependent CFO decisions with bidirectional arrows |

## Per-chapter results

00-frontmatter.md — 0 tables, 0 figures, no Wayback (front matter)
00-preface-and-toc.md — 0 tables, 0 figures, no Wayback (preface)
01-the-cfos-first-question.md — 2 tables, 0 figures, Wayback: stub inserted (Donaldson Brown)
02-reading-the-firm-from-inside.md — 3 tables, 0 figures, Wayback: stub inserted (Mary Harris Smith)
03-working-capital-is-where-the-cash-lives.md — 2 tables, 3 figures, Wayback: stub inserted (John Hicks)
04-capital-budgeting-at-the-firm-level.md — 2 tables, 0 figures, Wayback: stub inserted (Joel Dean)
05-the-cost-of-capital-and-the-wacc.md — 2 tables, 1 figure, Wayback: stub inserted (Fischer Black)
06-risk-adjusted-rates-and-real-options.md — 2 tables, 2 figures, Wayback: stub inserted (Irving Fisher)
07-capital-structure-theory-the-modigliani-miller-world.md — 1 table, 0 figures, Wayback: stub inserted (Merton Miller)
08-capital-structure-in-the-real-world.md — 3 tables, 0 figures, Wayback: stub inserted (Adolf A. Berle)
09-returning-capital-dividends-buybacks-and-the-choice-between-them.md — 3 tables, 0 figures, Wayback: stub inserted (Gardiner C. Means)
10-raising-capital-ipos-secondaries-and-the-cost-of-going-to-market.md — 1 table, 0 figures, Wayback: stub inserted (Maggie Lena Walker)
11-m-and-a-the-largest-decisions-a-cfo-makes.md — 2 tables, 0 figures, Wayback: stub inserted (Edith Penrose)
12-operational-risk-management.md — 1 table, 2 figures, Wayback: stub inserted (Karl Borch)
13-international-corporate-finance.md — 3 tables, 0 figures, Wayback: stub inserted (Susan Strange)
14-behavioral-corporate-finance.md — 3 tables, 0 figures, Wayback: stub inserted (Daniel Bernoulli)
15-the-capstone-an-integrated-cfo-recommendation.md — 2 tables, 1 figure, Wayback: stub inserted (Joseph Schumpeter)

## Summary

Total chapters processed: 17
Total tables rendered: 32
Total figures generated (SVG+PNG pairs): 9
Total Wayback Machine portrait stubs inserted: 15
Total Wayback Machine subject replacements: 0

## Setup notes / spec interpretations

- **Bernoulli (Ch 14) is pre-1850s.** Stub uses `engraving` and `portrait` per the spec.
- **`INFOGRAPHIC` / `CHART` comments left untouched.** The book has 13 INFOGRAPHIC and 14 CHART comments, all out of scope per the spec's literal Pass-2 token list. If the intent was to render these too, expand the token list and re-run.
- **Preface H1 mismatch (same bug as the comp-finance book).** `chapters/00-preface-and-toc.md` opens with `# Causal Inference with Case Studies` — a leftover heading from another book. Not in the spec's edit scope, but the EPUB chapter list shows that title in slot ch002.

## Action items

### 1. Generate 15 Wayback portrait .jpg files

`donaldson-brown.jpg`, `mary-harris-smith.jpg`, `john-hicks.jpg`, `joel-dean.jpg`, `fischer-black.jpg`, `irving-fisher.jpg`, `merton-miller.jpg`, `adolf-a-berle.jpg`, `gardiner-c-means.jpg`, `maggie-lena-walker.jpg`, `edith-penrose.jpg`, `karl-borch.jpg`, `susan-strange.jpg`, `daniel-bernoulli.jpg` (engraving source), `joseph-schumpeter.jpg`.

### 2. Add a cover image

`build.sh` looks for `cover.jpg` at the book root for KDP upload (1600×2560 JPEG).

### 3. Fix the preface H1

`chapters/00-preface-and-toc.md` line 1 currently reads `# Causal Inference with Case Studies`. One-line fix.

### 4. INFOGRAPHIC / CHART comments out of literal scope

13 INFOGRAPHIC + 14 CHART comments remain across the book. Expanding the Pass-2 token list to include these would generate ~27 additional figures.

## Build commands

```
cd books/corporate-finance-with-ai
./build.sh
```

Outputs land in `output/`: `corporate-finance-with-ai.epub`, `corporate-finance-with-ai.html`, and `combined.md` (archival concatenated source).
