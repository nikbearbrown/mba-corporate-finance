#!/usr/bin/env python3
"""Insert LLM Exercise blocks at the bottom of each of the 15 content chapters
of corporate-finance-with-ai. The Wayback Machine block already sits at EOF;
the LLM Exercise must precede it (LLM Exercise → Wayback, not the reverse).
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
CH = ROOT / "chapters"

EXERCISES = [
    (
        "01-the-cfos-first-question.md", "1", "The CFO's First Question",
        "The firm you'll analyze across the next fourteen chapters, Maya's *third Tuesday* version of the specification problem, and a decision frame that names the question precisely.",
        "Claude Project",
        """I'm starting a project that will run across the next fourteen chapters of *Corporate Finance with AI* by Nik Bear Brown. Across the chapters I will adopt Maya Chen's role at Halverson Industries and build one complete CFO board memo, section by section.

Either I'll use Halverson as the running case (Diane is CFO, the firm is mid-cap industrial, the live decisions are the Plant 4 expansion, the Cardinal Flow Systems acquisition, the FY26 capital plan, and the operational-risk position) or I'll substitute my own employer / a public mid-cap I care about. Paste the firm choice below; if I haven't, ask.

Help me set up Chapter 1's deliverable. Chapter 1 introduces the **specification gap** — the difference between the question Maya was asked and the question her education prepared her for — and the **inside-vs-outside** split.

Produce four things, in order:

1. **The firm, named precisely.** One paragraph. Industry, size (revenue, EBITDA, market cap), capital structure at a glance, the live decision the CFO is wrestling with this quarter. Use Halverson defaults if I gave you no other firm.

2. **The third-Tuesday decision.** One paragraph. The specific decision you'll be analyzing across the book — written as Diane (or your CFO) would phrase it in an email to Maya. Bad: "Look at our capital structure." Good: "By Friday I need a one-page case for whether we fund Plant 4's $50M expansion with new debt, an equity issuance, or a mix — and what the implications are for the Cardinal acquisition we're advancing in parallel."

3. **The four interdependent decisions Chapter 15 will integrate.** A short bullet list — capital allocation, capital structure, payout policy, risk position — each instantiated for *your* firm in one sentence. These four decisions are what the capstone holds at once.

4. **The "what would change my mind" sentence.** One sentence. The specific evidence that would flip the recommendation. The verify-step's anchor for the entire memo.

Format the output as a markdown document `01-decision-frame.md`. Be honest about uncertainty in the firm's numbers — pick figures you'd defend in a meeting, not figures that sound impressive.""",
        "A markdown document `01-decision-frame.md` containing the firm definition, the third-Tuesday decision, the four interdependent decisions, and the what-would-change-my-mind sentence. This document is the seed for every subsequent chapter's exercise.",
        "Not the right tool yet — pure markdown drafting.",
        "Create a Claude Project named *Halverson Memo — [your firm]*. Put in the system prompt: *every output is a section that will fit into a final 6–10 page integrated CFO board memo at Chapter 15*. Pin the four interdependent decisions list as a project file.",
        "First chapter — no prior exercise to build on. The firm chosen here governs every subsequent exercise.",
        "Chapter 2 takes the same firm and produces the *reading-the-firm-from-inside* section — the manager-eye financial-statement read that an outside analyst cannot do.",
    ),

    (
        "02-reading-the-firm-from-inside.md", "2", "Reading the Firm from Inside",
        "The Inside-View Read section of the memo: a manager-eye assessment of the firm's three financial statements, the operational reality behind them, and the institutional-memory questions only an insider can answer.",
        "Cowork",
        """I'm working on Halverson's Board Memo for the firm in `01-decision-frame.md`. Chapter 2 distinguished:

- The **outside-analyst view** — built from public data (10-K, earnings calls, EDGAR), with the verification loop running through cross-references
- The **inside-analyst view** — built from operational data, institutional memory, and people in the building, with the verification loop running through ownership of the underlying numbers

In **Cowork**, produce `02-inside-read.md` containing:

1. **The three-statement insider read.** Pull the most recent annual filing (10-K) and quarterly filing (10-Q) for your firm. For each statement, write 4–6 sentences that an analyst from outside the firm could *not* write — i.e., the inside-view interpretation. Examples:
   - **Income statement**: which revenue is the company internally calling *backlog conversion* vs. *new bookings*? Which margin is being protected by which operational lever?
   - **Balance sheet**: which receivables are the credit team flagging? Which inventory is the operations team writing down quietly?
   - **Cash flow statement**: which line of operating cash is being moved by working-capital choices vs. by underlying operational performance?

2. **The shadow numbers.** Three-to-five operational metrics the firm tracks internally that don't appear in any filing — backlog conversion rate, customer concentration, days of safety stock, average sales-cycle length, channel-mix shift. State each, give the latest internal value (or your best estimate), and explain why it matters for the third-Tuesday decision in `01-decision-frame.md`.

3. **The institutional-memory questions.** Three questions only an insider could answer that *should* be answered before the Chapter 15 board memo ships. Examples:
   - "Why was the Q3 2023 working-capital improvement reversed in Q1 2024?"
   - "What did Diane commit to the audit committee at the September meeting?"
   - "Who actually owns the customer-concentration policy?"

Save as `02-inside-read.md`. The verification loop here is *ownership-based* — for each claim, the inside view names *who you'd ask* to confirm it.""",
        "A markdown document `02-inside-read.md` containing the three-statement insider read, three-to-five shadow numbers, and the institutional-memory questions that only an insider can answer.",
        "Not needed for the prose; Cowork's filing-pull is the load-bearing tool.",
        "Cowork is the right tool — it can pull the 10-K and 10-Q from EDGAR (or from a local file) and assemble the read in one session. The Project context inherits the firm choice.",
        "Chapter 1 named the firm and the decision; Chapter 2 reads the firm from the inside, distinguishing what the public can see from what only Maya can.",
        "Chapter 3 zooms in on working capital — the part of the firm where cash actually lives — and produces the cash-conversion-cycle analysis.",
    ),

    (
        "03-working-capital-is-where-the-cash-lives.md", "3", "Working Capital Is Where the Cash Lives",
        "The Working-Capital Reality section of the memo: a cash-conversion-cycle analysis with the binding line item identified and an improvement plan that names dollar impact and an accountable owner.",
        "Claude Project",
        """I'm working on Halverson's Board Memo. The inside-view read is in `02-inside-read.md`.

Chapter 3 taught:
- **The cash conversion cycle**: $\\text{CCC} = \\text{DSO} + \\text{DIO} - \\text{DPO}$
- **The trade-off between liquidity and yield**: a firm holding more working capital than it needs is forgoing return on that capital
- **The structural reasons a profitable firm runs out of cash**: receivables stretch, inventory builds, payables compress

Produce `03-working-capital.md` containing:

1. **The cash-conversion-cycle calculation.** Pull DSO, DIO, DPO from the filings (or from your firm's internal data). Compute CCC. Compare to the prior year and to two named industry peers. Show the arithmetic.

2. **The binding line item.** Of DSO / DIO / DPO, which one is dragging the cycle most? Name it specifically. Do not say "we should improve all three" — name the one that is binding and explain why.

3. **The dollar impact of a one-day improvement on the binding line.** If we cut DSO by one day, that releases (Daily revenue) × 1 day in cash. If we cut DIO by one day, that releases (Daily COGS) × 1 day. Compute the dollar number for *your* firm. State the assumption (e.g., "annual revenue $1.8B implies daily revenue $4.9M, so one DSO day = $4.9M of cash released").

4. **The improvement plan.** Three-to-five specific moves: change credit terms with the top-5 customers; tighten inventory safety-stock policy; renegotiate top-10 supplier payment terms. For each, specify the named operational owner (CFO, COO, controller, head of supply chain) and the expected dollar impact.

5. **The risk side.** One paragraph. What would go wrong if you executed this plan? Customer relationships, supplier reliability, stockout risk on the inventory side. The CFO who proposes a working-capital improvement plan without naming the operational risk is *moving cash, not creating it*.""",
        "A markdown document `03-working-capital.md` containing the CCC calculation, the binding line item, the dollar impact of a one-day improvement, the named improvement plan, and the operational-risk paragraph.",
        "Optional — Claude Code can scaffold `analysis/03-ccc.py` that pulls DSO/DIO/DPO from a CSV or directly from EDGAR and computes the year-over-year deltas.",
        "Append to the project. The cash released here may fund Plant 4 (Ch 4) without new debt — flag the linkage.",
        "Chapter 2 read the firm; Chapter 3 finds the cash hiding inside it.",
        "Chapter 4 takes the firm to capital budgeting — building the NPV-ranked portfolio of projects competing for the freed-up working capital.",
    ),

    (
        "04-capital-budgeting-at-the-firm-level.md", "4", "Capital Budgeting at the Firm Level",
        "The Capital-Budgeting Portfolio section of the memo: an NPV-ranked list of candidate projects under a budget constraint, with the prioritization defended and the binding constraint named.",
        "Claude Code",
        """I'm working on Halverson's Board Memo. Sections so far: `01-decision-frame.md`, `02-inside-read.md`, `03-working-capital.md`.

Chapter 4 taught:
- **NPV** as the primary decision rule (positive NPV = creates value, negative = destroys it)
- **The firm-level portfolio problem**: not one project at a time but the prioritization-under-budget problem
- **The difference between accept/reject and rank-under-constraint**

Scaffold `analysis/04-budget-portfolio.py`:

1. **Define the candidate-project set.** 6–10 projects the firm is currently considering. For Halverson use Plant 4 ($50M, projected $20M EBITDA), Cardinal acquisition ($700M, projected $50M synergized EBITDA), plus 4–6 organic projects you make up at plausible scales. For another firm: pull from the latest investor-day deck or 10-K capital-allocation discussion.

2. **For each project**, define: initial investment, year-by-year cash-flow forecast (5–10 years), terminal value, and a project-specific discount rate (use the firm WACC for now — Chapter 5 refines this; Chapter 6 adjusts for project risk).

3. **Compute NPV, IRR, profitability index** for each. Save as a CSV.

4. **Solve the budget knapsack.** Given a total capital budget — pick a number consistent with the firm's recent cash flow plus available debt capacity — find the subset of projects that maximizes total NPV subject to the budget constraint. Use `scipy.optimize.milp` or `pulp`.

5. **Identify the binding constraint.** The capital budget? Engineering capacity (Plant 4 needs the same engineering team as Project X)? Management bandwidth (the Penrose effect — see Ch 11's Wayback figure)? State the binding constraint explicitly.

6. **Produce `analysis/04-portfolio-ranked.md`** containing: the NPV-ranked list, the recommended portfolio under the budget, the binding constraint, and a one-paragraph defense of the prioritization that an audit-committee chair could read in 90 seconds.

The script runs with `python analysis/04-budget-portfolio.py --budget [DOLLARS] --wacc [RATE]`.""",
        "A runnable script `analysis/04-budget-portfolio.py` plus a results file `analysis/04-portfolio-ranked.md` containing the NPV ranking, the knapsack solution, the binding constraint, and a defensible prioritization.",
        "Right tool — NPV portfolio + integer-program knapsack is exactly Claude Code's wheelhouse. Use `pulp` or `scipy.optimize.milp`.",
        "Append the portfolio markdown to the project. The recommended portfolio's total dollar amount becomes a constraint Chapter 5's WACC analysis must support and Chapter 8's capital structure must finance.",
        "Chapter 3 freed up working capital; Chapter 4 deploys it (and more) across an NPV-ranked portfolio.",
        "Chapter 5 stress-tests the WACC that Chapter 4 used as the discount rate — and sees how much the prioritization moves under ±100bp shifts.",
    ),

    (
        "05-the-cost-of-capital-and-the-wacc.md", "5", "The Cost of Capital and the WACC",
        "The WACC Section of the memo: the firm WACC computed from first principles, stress-tested against ±100bp on each input, and defended against the FP&A footnote version.",
        "Claude Code",
        """I'm working on Halverson's Board Memo. The capital-budget portfolio is in `analysis/04-portfolio-ranked.md`.

Chapter 5 taught:
- **The three meanings of cost of capital** — provider required return, hurdle rate, weighted-average cost — and how they drift apart in real firms
- **The WACC formula**: $\\text{WACC} = (E/V) \\cdot r_e + (D/V) \\cdot r_d \\cdot (1-T_c)$
- **Sensitivity** — small input changes can move the WACC by 100+ bp, which moves NPV by double-digit percentages

Scaffold `analysis/05-wacc.py`:

1. **Compute the cost of equity via CAPM.** $r_e = r_f + \\beta \\cdot (E[r_m] - r_f)$. Pull β by regressing your firm's monthly returns on the S&P 500 over the last 5 years (use `yfinance`). Use the current 10-year Treasury for $r_f$. Use 5.5% as the historical equity risk premium (or defend a different number).

2. **Compute the cost of debt.** Average yield-to-maturity on the firm's outstanding debt, from the 10-K's debt schedule. If unavailable, use the rating-implied yield (BBB ≈ Treasury + 150bp; BB ≈ Treasury + 350bp).

3. **Compute the WACC.** Use the *target* debt-to-capital ratio (not the book ratio) — pull from the firm's stated capital-structure policy or use the trailing 5-year average.

4. **Stress-test.** Build a ±100bp sensitivity table: rows are each input ($r_f$, β, equity risk premium, $r_d$, target debt weight, marginal tax rate), columns are -100bp / -50bp / 0 / +50bp / +100bp. Cells are the resulting WACC.

5. **Re-rank the Chapter 4 portfolio at the new WACC.** Take the corner of the sensitivity table that most plausibly represents *the WACC the FP&A team should be using next quarter*. Re-run the knapsack from `analysis/04-budget-portfolio.py`. Did the prioritization change? Which projects moved into or out of the recommended set?

6. **Produce `analysis/05-wacc.md`** containing: the WACC point estimate with provenance for each input, the sensitivity table, the alternative-WACC re-ranking, and a one-paragraph defense of the WACC the board memo will adopt.

Run with `python analysis/05-wacc.py --ticker [TICKER]`.""",
        "A runnable script `analysis/05-wacc.py` plus `analysis/05-wacc.md` containing the WACC point estimate, the sensitivity table, the impact on the Chapter 4 portfolio, and the defended adopted rate.",
        "Right tool — pulling beta from `yfinance`, building the sensitivity table, and re-ranking the portfolio is multi-step quantitative work.",
        "Append to the project. The defended WACC here is the headline rate the rest of the memo discounts at.",
        "Chapter 4 used a placeholder WACC; Chapter 5 produces the defended rate and shows what changes when the rate moves.",
        "Chapter 6 asks whether *the same* WACC is the right rate for *every* project — or whether some projects (high-risk, optionality-heavy) need their own rate.",
    ),

    (
        "06-risk-adjusted-rates-and-real-options.md", "6", "Risk-Adjusted Rates and Real Options",
        "The Project-Specific-Rate and Real-Options section of the memo: the projects in your portfolio that need a risk-adjusted rate, and the real-option value of the most flexibility-rich project.",
        "Claude Code",
        """I'm working on Halverson's Board Memo. The WACC is defended in `analysis/05-wacc.md`.

Chapter 6 taught:
- **One discount rate doesn't always work** — projects with risk profiles different from the firm's average require project-specific rates
- **Real options** — defer, abandon, expand, contract — have value that NPV alone misses
- **The optionality premium** — flexibility is worth paying for when forecast uncertainty is high

Scaffold `analysis/06-real-options.py`:

1. **Identify the projects in your portfolio that have meaningfully different risk than the firm average.** For Halverson: a venture-style growth project has higher risk than a maintenance capex; a regulated utility build has lower risk. For each project, name its risk profile relative to the firm and recommend either *firm WACC* or *project-specific rate*.

2. **Estimate one project-specific rate.** For the project whose risk profile is most different from the firm average, build a comparable-firm beta proxy (pull pure-play comparables from the same industry segment), unlever and relever beta against the project's target capital structure, and compute a project-specific cost of capital.

3. **Identify the project with the most real-option content.** Look for: a project that can be deferred at low cost; a project that can be abandoned partway through with significant residual value; a project that creates a follow-on opportunity (an *expand* option). Pick one.

4. **Quantify the real-option value.** Use either a binomial tree (Cox-Ross-Rubinstein) or a Black-Scholes analog. State the inputs: underlying value (the project's NPV today), exercise price (the cost to expand / continue), volatility (your best estimate of the underlying business's annualized vol), time to expiration (when the decision gates close).

5. **Produce `analysis/06-real-options.md`** containing: the project-by-project risk-rate assignment, the one project-specific rate computed, the real-option valuation, and a one-paragraph case for whether the option value is large enough to change the Chapter 4 portfolio recommendation.

Run with `python analysis/06-real-options.py --portfolio analysis/04-portfolio-ranked.md`.""",
        "A runnable script `analysis/06-real-options.py` plus `analysis/06-real-options.md` containing the project-rate assignments, one project-specific rate, one real-option valuation, and the impact on the portfolio recommendation.",
        "Right tool. Implementing the binomial tree and the comparable-firm beta unlever/relever is short but precise.",
        "Append to the project. If real-option value is material, it goes in the *Recommendation* section of the Chapter 15 board memo as an explicit modifier on Chapter 4's NPV ranking.",
        "Chapter 5 produced one rate for the firm; Chapter 6 names where that one rate is wrong and what to use instead.",
        "Chapter 7 takes a step back from project-level analysis to the firm-level capital-structure question — beginning with the Modigliani-Miller baseline.",
    ),

    (
        "07-capital-structure-theory-the-modigliani-miller-world.md", "7", "Capital Structure Theory: The Modigliani-Miller World",
        "The MM Baseline section of the memo: a precise statement of the MM theorem applied to your firm, with each of the four assumptions stress-tested for fit.",
        "Claude Project",
        """I'm working on Halverson's Board Memo. The portfolio (`04`) and WACC (`05`) sections are in.

Chapter 7 taught:
- **MM Proposition I (frictionless)**: under no taxes, no bankruptcy costs, no information asymmetry, and equal borrowing rates, firm value is independent of capital structure
- **MM Proposition II**: as leverage rises, expected return on equity rises proportionally — the cost of equity is increasing in the debt ratio
- The point is *not* that MM is true in the real world — it's that MM identifies which frictions matter

Produce `07-mm-baseline.md` containing:

1. **State MM precisely for your firm.** One paragraph. "If Halverson operated in the MM world, its enterprise value would be \\$X billion regardless of whether it carried 20% debt or 80% debt or zero debt. The cash flows from operations are the only thing that matters."

2. **Walk through each of the four assumptions and ask: does it hold?**
   - **No corporate taxes.** Halverson pays a 24% marginal tax rate. *Assumption violated; tax shield is real.*
   - **No bankruptcy costs.** Halverson is investment-grade; bankruptcy costs are low but not zero. *Assumption partially violated.*
   - **No information asymmetry.** Halverson management knows things the market doesn't (covenant cushion, customer concentration trajectory). *Assumption clearly violated.*
   - **Equal borrowing rates for firm and investors.** Halverson borrows at 5.2% (Chapter 5); a retail investor borrows at 8% on margin. *Assumption clearly violated.*

3. **Rank the violations by impact on Halverson's specific capital-structure choice.** Which violation matters most for *your* firm? An investment-grade industrial: tax shield dominates. A growth-stage tech firm: information asymmetry dominates. A real-estate firm: bankruptcy cost dominates.

4. **State the MM-derived value of debt.** Present value of the tax shield = $T_c \\cdot D$ at the simplest treatment. Compute this number for your firm at the current debt level and at a +20% debt level. The difference is the *MM-with-taxes* case for adding debt.

5. **The closing sentence.** The MM baseline tells you that adding debt to Halverson is worth approximately $T_c \\cdot \\Delta D$ in tax-shield value, *before* considering bankruptcy cost, agency cost, and signaling — which is what Chapter 8 takes up.""",
        "A markdown document `07-mm-baseline.md` containing the precise MM statement, the four-assumption stress-test ranked by impact on your firm, the MM-with-taxes tax-shield value, and the framing for Chapter 8.",
        "Not needed for this section.",
        "Append to the project. The MM baseline is the foundation — Chapter 8 builds the real-world adjustments on top of it.",
        "Chapters 1–6 analyzed projects; Chapter 7 starts the firm-level financing analysis with the simplest possible baseline.",
        "Chapter 8 takes the MM baseline and adds back the frictions — producing the recommended target debt-to-capital ratio for the firm.",
    ),

    (
        "08-capital-structure-in-the-real-world.md", "8", "Capital Structure in the Real World",
        "The Target Capital Structure section of the memo: a defended target debt-to-capital ratio, with the trade-offs (tax shield, distress cost, financial flexibility, signaling) priced explicitly.",
        "Claude Project",
        """I'm working on Halverson's Board Memo. The MM baseline is in `07-mm-baseline.md`.

Chapter 8 taught:
- **Trade-off theory**: optimal debt level balances the tax shield against distress costs
- **Pecking order theory**: managers prefer internal funds → debt → equity (in that order) because of information asymmetry
- **Agency costs**: debt disciplines free cash flow; equity dilutes incentive
- **Market timing**: managers issue equity when they think it's overvalued
- **Financial flexibility**: keeping debt capacity in reserve has option value

Produce `08-target-structure.md` containing:

1. **The current capital structure.** From the latest 10-K balance sheet, compute the firm's debt-to-capital ratio (book) and debt-to-enterprise-value ratio (market). State both. Compare to the firm's stated target (if disclosed in the 10-K) and to the industry median.

2. **The four-pillar trade-off analysis.** For each of the four real-world frictions, quantify or qualify its impact on your firm's optimal capital structure:
   - **Tax shield** (from Chapter 7): present value of $T_c \\cdot D$ at the candidate debt levels
   - **Distress cost**: probability of distress (use the firm's credit rating to map to historical default rates) times estimated distress cost (use ~25% of pre-distress firm value as a default; defend if you use a different number)
   - **Financial flexibility**: what option value does the firm forgo by levering up? Quantify in the spirit of Chapter 6
   - **Signaling**: what does an issuance of debt vs. equity tell the market about management's view of firm value?

3. **The recommended target.** A specific debt-to-capital ratio (e.g., "30–35% debt-to-capital, mid-investment-grade target rating BBB+"). Defend it in two paragraphs.

4. **The path to the target.** If current ≠ target, what's the plan? Issue debt, retire equity, or both? Over what time horizon? Reference the financing chapters to come (Ch 9 payout, Ch 10 issuance).

5. **The flexibility statement.** One sentence. The maximum debt the firm could take on without breaching its target rating — i.e., the *unused debt capacity* that is the optionality the recommendation is buying.""",
        "A markdown document `08-target-structure.md` containing the current vs. target capital structure, the four-pillar trade-off analysis, the recommended target ratio, the path to it, and the unused-debt-capacity statement.",
        "Optional — Claude Code can build `analysis/08-tradeoff.py` that maps credit rating to default probability and computes the tax-shield-vs-distress-cost trade-off across a range of debt levels.",
        "Append to the project. The target capital structure is one of the four interdependent decisions Chapter 15 must integrate.",
        "Chapter 7 stated the MM baseline; Chapter 8 adds the real-world frictions and produces a target debt-to-capital ratio with each trade-off explicitly priced.",
        "Chapter 9 turns to the other side of the financing decision — what to do with capital the firm is *not* keeping: dividends and buybacks.",
    ),

    (
        "09-returning-capital-dividends-buybacks-and-the-choice-between-them.md", "9", "Returning Capital",
        "The Payout Policy section of the memo: a recommended FY26 payout policy (dividends + buybacks), sized against forward cash flow, and defended against the alternative dispositions of the same cash.",
        "Claude Project",
        """I'm working on Halverson's Board Memo. The target capital structure is in `08-target-structure.md`.

Chapter 9 taught:
- **Dividend smoothing** (Lintner): managers smooth dividends because cuts are punished asymmetrically
- **Buybacks as flexible payout**: faster, no implicit commitment, signaling content
- **The tax wedge**: dividends taxed as ordinary income (in some regimes) vs. capital gains for buybacks
- **Signaling content**: a buyback announcement is a managerial claim that the stock is undervalued

Produce `09-payout-policy.md` containing:

1. **The FY26 forward cash forecast.** Pull from the firm's most recent guidance or build from the trend: operating cash flow, capex, working-capital change. The residual is *cash available for return to shareholders + investment opportunities + balance sheet*.

2. **The capital-allocation pie for FY26.** Of the cash available, how much goes to: investment (Chapter 4 portfolio), debt paydown / capacity (Chapter 8), payout, balance-sheet build? State each as a dollar amount and as a fraction of operating cash flow.

3. **The payout split.** Of the payout dollars, how much is dividend, how much is buyback? Defend with reference to:
   - Current dividend policy and shareholders' implicit-contract expectations
   - Buyback authorization remaining (or to be requested at the board meeting)
   - Stock price relative to your management view of intrinsic value (a buyback is more attractive when the stock is cheaper)
   - Tax considerations for the marginal shareholder
   - Signaling — what a 10% increase in the dividend says vs. a $200M buyback authorization

4. **The recommended FY26 policy.** Specific numbers: dividend per share, total buyback authorization, expected timing. State the policy in the language a press release would use.

5. **The reversal trigger.** What would make us reduce or pause this policy? Specific named conditions — typically a leverage breach, a customer-concentration shock, or a downgrade. The reversal trigger is what makes the policy a *recommendation* rather than a *forecast*.""",
        "A markdown document `09-payout-policy.md` containing the FY26 cash forecast, the capital-allocation pie, the dividend/buyback split, the recommended policy, and the reversal trigger.",
        "Optional — `analysis/09-payout.py` can model alternative payout splits against forward cash projections and report the residual balance-sheet impact under each.",
        "Append to the project. Payout is the third of the four interdependent decisions in Chapter 15.",
        "Chapter 8 set the target capital structure; Chapter 9 splits the capital that's coming back out of the firm between dividends and buybacks.",
        "Chapter 10 turns to the other direction — when the firm needs to *raise* capital — and asks how to do it efficiently.",
    ),

    (
        "10-raising-capital-ipos-secondaries-and-the-cost-of-going-to-market.md", "10", "Raising Capital",
        "The Issuance Plan section of the memo: a financing-options memo for the capital the firm needs to raise (debt issuance, equity issuance, convertible, private placement), with the recommended structure defended against the alternatives.",
        "Claude Project",
        """I'm working on Halverson's Board Memo. The target capital structure is in `08-target-structure.md`; the FY26 payout in `09-payout-policy.md`.

Chapter 10 taught:
- **The IPO process**: registration, roadshow, book-building, allocation, lockup
- **Secondary offerings**: how follow-on equity issuance differs from an IPO
- **Underpricing**: typical IPO leaves 10–20% on the table — a real cost of going to market
- **Alternatives**: PIPE, private placement, convertible note, secured vs. unsecured debt issuance

Most firms in this book are public, so the relevant exercise is *secondary issuance vs. debt issuance vs. convertible*. (For a private firm, run the IPO version and substitute equity proceeds at a defended valuation.)

Produce `10-issuance-plan.md` containing:

1. **The capital-raising need.** From Chapter 4 (the portfolio cost) and Chapter 8 (the path to target capital structure), state the dollar amount of new capital the firm needs to raise in the next 12–18 months. Be specific.

2. **Three financing options.** For each of: (a) senior unsecured debt issuance, (b) secondary equity offering, (c) convertible note, build a one-page summary including:
   - The all-in cost (yield + fees for debt; underpricing + fees for equity; coupon + dilution-on-conversion for convertible)
   - The capital-structure impact (does it move the firm toward or away from the Chapter 8 target?)
   - The signaling content
   - The market-window considerations (current credit spreads, current equity valuation, current convertible-bond appetite)

3. **The recommended structure.** Pick one (or a mix). Defend against the two not chosen. The case for *not* doing this issuance at all is also a defensible answer — name what the firm gives up by deferring.

4. **The execution plan.** Lead bookrunner, timing, indicative pricing range, lockup structure if applicable. The level of detail should be enough that the audit-committee chair could ask "what's our backup plan if the deal is undersubscribed?" and you'd have an answer.""",
        "A markdown document `10-issuance-plan.md` containing the capital-raising need, the three-option comparison, the recommended structure, and the execution plan.",
        "Not needed.",
        "Append to the project. The chosen issuance structure interacts with Chapter 9's payout policy (issuing while paying out is a red flag) — flag the linkage.",
        "Chapter 9 returned capital; Chapter 10 raises it. The two together are the firm's external-capital interface.",
        "Chapter 11 turns to the largest single decisions a CFO makes: M&A. Maya's Cardinal valuation is the worked exercise.",
    ),

    (
        "11-m-and-a-the-largest-decisions-a-cfo-makes.md", "11", "M&A",
        "The M&A Valuation and Recommendation section of the memo: a defensible valuation of a target across three approaches (DCF, comps, precedents), the synergy assumptions, and a recommendation that survives the empirical record on acquirer underperformance.",
        "Claude Code",
        """I'm working on Halverson's Board Memo. Sections 1–10 are in the project.

Chapter 11 taught:
- **The empirical record**: acquirers, on average, underperform — the deal premium plus integration costs frequently exceeds realized synergies
- **Three valuation approaches**: DCF, trading comparables, precedent transactions
- **Synergy realization**: the gap between projected and delivered synergies is the graveyard of acquisition theses

For Halverson the running case is the **Cardinal Flow Systems** acquisition ($400M revenue, $80M EBITDA, ~$700M enterprise value under discussion). For your own firm: pick a real target your firm has discussed (in the press, on earnings calls, or internally) or pick a public target that fits your firm's strategic logic.

Scaffold `analysis/11-ma-valuation.py`:

1. **Pull the target's financials.** Revenue, EBITDA, EBIT, free cash flow for the last 5 years. Build a 10-year forecast.

2. **DCF valuation.** Discount the projected FCF at a target-specific WACC. State the terminal-value method (Gordon growth or exit-multiple) and defend the parameters. Output a point estimate and a 5×5 sensitivity table on discount rate × terminal growth.

3. **Trading comparables.** Identify 4–6 publicly traded comparables. Pull current EV/EBITDA, EV/Revenue, P/E. Apply the median multiple to the target's metrics. Output a multiples-implied valuation range.

4. **Precedent transactions.** Identify 4–6 comparable M&A transactions in the last 5–7 years. Pull the announced enterprise-value-to-EBITDA multiples. Apply the median to the target. Output a precedent-implied valuation range.

5. **The synergy assessment.** What synergies are claimed? Cost-side (procurement, headcount, facilities, IT) and revenue-side (cross-sell, geographic, channel). For each, ask: is this realistically deliverable? At what cost-to-achieve? Discount the gross synergy by a realization factor (50–70% is honest for most deals).

6. **The recommendation.** Pay no more than X. The X is the lowest of the three approaches' midpoints, less the integration cost, less a risk discount for the empirical-acquirer-underperformance prior. Compare to the deal price under discussion.

7. **Save `analysis/11-ma-recommendation.md`** with the three valuations, the synergy table, the recommended maximum bid, and the named conditions that would change the recommendation (target restatement, customer concentration discovery, regulator concern).""",
        "A runnable script `analysis/11-ma-valuation.py` plus `analysis/11-ma-recommendation.md` containing the three valuations, the synergy assessment, the recommended maximum bid, and the change-our-mind conditions.",
        "Right tool — three-approach valuation with sensitivity tables, comparable pulls, and synergy modeling is the canonical Claude Code use case for finance.",
        "Append to the project. The M&A valuation interacts with Chapter 4 (it's the largest line in the portfolio), Chapter 8 (it consumes debt capacity), and Chapter 9 (it may force a payout reduction). Flag all three linkages.",
        "Chapter 11 is where every prior chapter's tool gets used at once on a single decision.",
        "Chapter 12 takes a step back to the firm-wide risk position and asks which operational risks the firm should retain vs. transfer.",
    ),

    (
        "12-operational-risk-management.md", "12", "Operational Risk Management",
        "The Risk Position section of the memo: a risk register with the top 5–10 operational risks priced (probability × impact), each with a retain-vs-transfer disposition and the resulting risk-capital allocation.",
        "Claude Project",
        """I'm working on Halverson's Board Memo. Sections 1–11 are in the project.

Chapter 12 taught:
- **Enterprise risk vs. operational risk**: the latter is what this chapter focuses on
- **The retain-vs-transfer decision** (Borch theorem in spirit): which risks does the firm retain, which does it transfer through insurance / hedging / contractual allocation?
- **Risk capital as a real budget item**: every retained risk is implicitly funded by equity capital

Produce `12-risk-register.md` containing:

1. **The top 5–10 operational risks.** For your firm, brainstorm:
   - **Demand risk**: customer concentration, end-market cyclicality
   - **Supply risk**: single-source supplier, raw-material price, logistics disruption
   - **Operational risk**: a specific plant going down, a labor action, a system outage
   - **Financial risk**: interest rate exposure, FX exposure, refinancing risk
   - **Legal/regulatory risk**: environmental, antitrust, IP, employment

   For each, name it specifically (not "supply chain risk" but "single-source supplier for the X polymer used in 60% of products").

2. **Price each.** Probability (low / medium / high, with a percentage), impact ($ at stake), expected loss = P × I. Sort by expected loss.

3. **The retain-vs-transfer disposition.** For each, recommend one of:
   - **Retain** — the firm absorbs the loss; price it into the equity-capital budget
   - **Transfer (insurance)** — buy a policy with the named premium and coverage limits
   - **Transfer (hedge)** — use a financial derivative to lay off the exposure
   - **Transfer (contractual)** — push the risk to a counterparty (supplier, customer, joint-venture partner)
   - **Mitigate** — operational change that reduces P or I (build a second source, lengthen the contract, add redundancy)

4. **The risk-capital number.** Sum the retained-risk expected losses. This is the implicit equity capital being held against operational risk. State it as a fraction of total equity. Flag if it's larger than the firm's stated risk appetite.

5. **The named owner per risk.** Each risk needs an accountable executive — head of operations, head of supply chain, GC, CFO. The risk-register-without-owners is a forecast, not a policy.""",
        "A markdown document `12-risk-register.md` containing the prioritized risks, the retain-vs-transfer dispositions, the implicit risk-capital number, and the named owners.",
        "Optional — `analysis/12-risk-capital.py` can run a Monte Carlo over the retained risks to produce a 95th-percentile retained-loss estimate.",
        "Append to the project. The risk position is the fourth of the four interdependent decisions in Chapter 15.",
        "Chapter 11 valued the largest single decision; Chapter 12 prices the firm-wide risk position that supports every decision.",
        "Chapter 13 broadens the risk view to international exposures — currency, transfer pricing, country risk.",
    ),

    (
        "13-international-corporate-finance.md", "13", "International Corporate Finance",
        "The International Risk Section of the memo: identification of the firm's currency and country exposures, with a hedging program and a transfer-pricing posture defended.",
        "Claude Code",
        """I'm working on Halverson's Board Memo. The risk register is in `12-risk-register.md`.

Chapter 13 taught:
- **Three currency exposures**: transaction (specific contracts), translation (consolidating financials), economic (long-run competitive impact)
- **Cross-border capital flows**: transfer pricing, repatriation, withholding tax
- **Country risk**: political, regulatory, expropriation, sovereign

Scaffold `analysis/13-international.py`:

1. **Map the firm's geographic footprint.** Revenue by geography, costs by geography, assets by geography. From the segment disclosure in the 10-K. Most US-listed industrials report in 4–8 segments.

2. **Identify the currency exposures.** For each non-USD currency:
   - **Transaction exposure** = next 12 months of contractually committed FX-denominated cash flows
   - **Translation exposure** = net assets denominated in that currency on the consolidated balance sheet
   - **Economic exposure** = impact on competitive position if that currency moves significantly (qualitative)

3. **Quantify the FX-at-risk.** For the top 2–3 currencies, compute a 1-year 95th-percentile loss given the historical volatility of the FX pair. This is the FX exposure measured in dollars.

4. **Design a hedging program.** For each currency, recommend:
   - **Hedge ratio**: percentage of transaction exposure to hedge (typically 50–80% rolling forward)
   - **Instrument**: forwards, options, or natural hedges (matching FX-denominated revenue with FX-denominated costs)
   - **Cost**: the all-in cost of the hedging program (forward points + bid-ask + program management)
   - **What's left unhedged**: the residual exposure the firm consciously accepts

5. **The transfer-pricing posture.** One paragraph. Where does the firm book profit relative to where the operations actually generate it? What's the firm's stated transfer-pricing policy? Are there currently open audits or controversies?

6. **Save `analysis/13-international.md`** containing the geographic footprint, the FX exposure quantification, the hedging program, and the transfer-pricing posture.

Run with `python analysis/13-international.py --ticker [TICKER]`.""",
        "A runnable script `analysis/13-international.py` plus `analysis/13-international.md` containing the geographic footprint, FX exposures, the hedging program, and the transfer-pricing posture.",
        "Right tool — pulling segment disclosures, computing FX-at-risk via historical vol, and modeling alternative hedge ratios is multi-step quantitative work.",
        "Append to the project. The hedging program goes in the Chapter 15 *risk position* section and interacts with the Chapter 12 risk register.",
        "Chapter 12 priced operational risk; Chapter 13 prices the international slice of it explicitly.",
        "Chapter 14 turns inward — to the behavioral biases that distort the recommendations Chapters 1–13 produced.",
    ),

    (
        "14-behavioral-corporate-finance.md", "14", "Behavioral Corporate Finance",
        "The Debiasing section of the memo: a structured pre-mortem on Maya's draft recommendation, identifying the specific managerial biases most likely affecting it and the protocol to surface them before the board reads the memo.",
        "Claude Project",
        """I'm working on Halverson's Board Memo. Sections 1–13 are drafted.

Chapter 14 taught:
- **Managerial overconfidence** — the most-replicated finding in behavioral corporate finance
- **Anchoring** — early numbers in a process disproportionately influence later ones
- **Sunk-cost fallacy** — we keep funding projects that should be killed because of money already spent
- **Market timing** — managers issue equity when they think it's overvalued (and they're often wrong)
- **Confirmation bias** — we collect evidence that supports the conclusion we've already reached

Produce `14-debiasing.md` containing:

1. **The pre-mortem.** Imagine it is two years from now and the recommendation in this memo turned out badly. Why did it fail? Brainstorm 5–8 named failure modes — specific, not generic. Bad: "Cardinal didn't perform." Good: "Cardinal's largest customer chose to dual-source after announcement, eroding 20% of projected revenue, and Halverson's integration team was diverted from product roadmap by the IT consolidation, costing market share to AmericanBlower in Q4."

2. **The bias audit.** For each of the four major sections of the memo (Capital Allocation Ch 4, Capital Structure Ch 8, Payout Policy Ch 9, M&A Ch 11), ask:
   - **What anchor was in place when the analysis started?** (e.g., the FP&A WACC of 8% — was it questioned?)
   - **What confirming evidence got more weight than disconfirming?** (e.g., synergy estimates that supported the deal vs. data points that didn't)
   - **What sunk-cost dynamic might be operating?** (e.g., Cardinal CEO has been talking with our CEO for 6 months — does that history make declining the deal harder?)
   - **What managerial overconfidence shows up in our forecasts?** (compare projected revenue growth to industry growth — is the "we'll outgrow the market" claim defensible?)

3. **Three concrete debiasing moves to install before the board reads the memo.**
   - **Devil's-advocate review**: name a person inside or outside the firm whose explicit job is to argue against the recommendation. Insist on a written counter-memo.
   - **Pre-mortem with named owners**: each failure mode in #1 gets a named *what would we do?* response, not a hand-wave.
   - **Range, not point**: every projection in the memo carries a 90% confidence interval, not a single number. The board reads the range; the management team reads the inputs that move it.

4. **The honest closing paragraph.** What is the strongest argument *against* the memo's recommendation that you have not already addressed? Write it. If you can't write it, the memo is not yet ready.""",
        "A markdown document `14-debiasing.md` containing the pre-mortem, the bias audit by section, the three debiasing moves, and the honest closing paragraph naming the strongest counter-argument.",
        "Not needed for this section — the work is reflective, not computational.",
        "Append to the project. The debiasing pass produces edits that propagate back into Chapters 4, 8, 9, and 11 — be ready to revise prior sections based on what surfaces here.",
        "Chapters 1–13 produced the analysis; Chapter 14 stress-tests the analysis against the predictable cognitive errors of the people who produced it.",
        "Chapter 15 — the capstone — assembles every prior chapter's section into one integrated 6-page board memo with decision triggers.",
    ),

    (
        "15-the-capstone-an-integrated-cfo-recommendation.md", "15", "The Capstone",
        "The complete 6–10 page integrated CFO board memo, holding all four interdependent decisions (capital allocation, capital structure, payout policy, risk position) at once, with named decision triggers, an audit record, and a named accountable owner.",
        "Cowork",
        """I'm working on Halverson's Board Memo. Every prior section is in the project: `01-decision-frame.md` through `14-debiasing.md`, plus the analysis files in `analysis/`.

Chapter 15 taught:
- **The four interdependent decisions**: capital allocation, capital structure, payout policy, risk position — *not sequential, simultaneous*
- **The board memo as the integrated artifact**: every prior chapter's analysis fits into a 6–10 page document the audit-committee chair will read line by line
- **Decision triggers**: a memo without named conditions for reversal is a forecast, not a recommendation
- **Audit record + named accountable owner**: the recommendation is owned by a person and supported by traceable analysis

In **Cowork**, assemble `report/15-board-memo.md`:

**Structure** (6–10 pages):

1. **Executive summary** (½ page). The four headline decisions, each in one sentence with the magnitude. The single largest risk to the integrated package. The what-would-change-our-mind sentence from `01-decision-frame.md`, refined.

2. **The four interdependent decisions** (4–6 pages, distributed):
   - **Capital Allocation** (1 page) — adapted from `analysis/04-portfolio-ranked.md` and `analysis/06-real-options.md` and `analysis/11-ma-recommendation.md`. The portfolio recommendation, the binding constraint, the largest single decision (M&A) embedded.
   - **Capital Structure** (1 page) — adapted from `08-target-structure.md` and `10-issuance-plan.md`. The target debt-to-capital, the path to it, the FY26 issuance plan.
   - **Payout Policy** (½–1 page) — adapted from `09-payout-policy.md`. FY26 dividend, FY26 buyback authorization, the reversal trigger.
   - **Risk Position** (1 page) — adapted from `12-risk-register.md` and `analysis/13-international.md`. The top retained risks, the hedging program, the named owners.

3. **Tensions named** (1 page). The three places where the four decisions pull against each other: the Cardinal acquisition consumes debt capacity that constrains the buyback; the FY26 capex peak conflicts with the working-capital improvement timing; the FX hedge cost competes with the Plant 4 IRR. Each tension named, each handled.

4. **Decision triggers** (½ page). For each of the four decisions, the named conditions that would force a reversal. *Example: "If Cardinal's top customer announces dual-sourcing within 90 days, we pause the buyback and reassess the synergy plan."* Five to seven specific triggers total.

5. **The audit record** (½ page). For each decision, the analysis files that support it. The audit-committee chair could pull `analysis/05-wacc.md` and verify the WACC of 8.4% if she wanted to.

6. **Named accountable owner.** *This recommendation is owned by [CFO name], dated [date]. The audit trail is at [path]. The recommendation will be reviewed against the named triggers monthly and against the integrated package at the next board meeting.*

**The Q&A audit.** After Cowork generates the draft, run a critique pass: the audit-committee chair reads this and asks the three hardest questions she would ask. Rewrite any section that doesn't already answer those questions.""",
        "A complete 6–10 page integrated CFO board memo as `report/15-board-memo.md`, plus a Q&A audit, plus a named-owner block. This is the deliverable the entire course was building toward.",
        "Optional — Claude Code can render the memo to PDF via Pandoc as `report/15-board-memo.pdf` for board distribution.",
        "Cowork is the right tool — it can read every chapter's output file, compose the integrated memo, and run the Q&A critique pass in one session. The accumulated Project context is the input.",
        "Every prior chapter contributed one section; Chapter 15 assembles them into the artifact the entire course was building toward.",
        "This is the final chapter. Your deliverable is now a complete board memo that the audit committee can read in fifteen minutes and either agree with or disagree with on specific named points — the closure of the specification problem introduced in Chapter 1.",
    ),
]


BLOCK_TEMPLATE = """
---

###  LLM Exercise — Chapter {n}: {title}

**Project:** Halverson's Board Memo, Built Across the Course
**What you're building this chapter:** {what}
**Tool:** {tool}

---

**The Prompt:**

```
{prompt}
```

---

**What this produces:** {produces}

**How to adapt this prompt:**

- *For your own project:* Substitute your firm for Halverson where Halverson appears; the exercise structure is firm-agnostic. Halverson's named cast (Diane / Priya / Cardinal) is scaffolding — replace as needed.
- *For ChatGPT / Gemini:* Works as-is. For ChatGPT, save the running memo to a Custom GPT instead of a Claude Project. For Gemini, paste the project's accumulated section files into the context window each session.
- *For Claude Code:* {how_code}
- *For a Claude Project:* {how_project}

**Connection to previous chapters:** {connection}

**Preview of next chapter:** {preview}
"""


def main():
    for entry in EXERCISES:
        (filename, n, title, what, tool, prompt, produces,
         how_code, how_project, connection, preview) = entry
        path = CH / filename
        text = path.read_text()
        if "###  LLM Exercise — Chapter" in text or "### LLM Exercise — Chapter" in text:
            print(f"  SKIP (already has LLM Exercise): {filename}")
            continue
        block = BLOCK_TEMPLATE.format(
            n=n, title=title, what=what, tool=tool, prompt=prompt,
            produces=produces, how_code=how_code, how_project=how_project,
            connection=connection, preview=preview,
        )
        # Insert BEFORE the existing Wayback Machine section so the order is
        # chapter content → LLM Exercise → Wayback Machine.
        wb_marker = "## AI Wayback Machine"
        if wb_marker in text:
            wb_idx = text.index(wb_marker)
            before = text[:wb_idx].rstrip()
            after = text[wb_idx:]
            if before.endswith("---"):
                before = before[:-3].rstrip()
            new_text = before + "\n" + block + "\n---\n\n" + after
        else:
            new_text = text.rstrip() + "\n" + block + "\n"
        path.write_text(new_text)
        print(f"  appended LLM Exercise to {filename}")


if __name__ == "__main__":
    main()
