#!/usr/bin/env python3
"""Pass 1 — render the 32 TABLE comments in corporate-finance-with-ai/chapters/."""
import re
from pathlib import Path

ROOT = Path(__file__).parent
CH = ROOT / "chapters"

TABLES = {}

# === Ch 01 ===
TABLES['five-job breakdown of "should we fund Plant 4'] = """| Job | The real question it asks | What data answers it | Owner of that data inside Halverson |
|---|---|---|---|
| **Capital allocation** | Does Plant 4 clear our hurdle rate vs. competing uses of the cash? | Project IRR vs. firm WACC; portfolio of competing projects | FP&A (Priya) |
| **Capital structure** | What does our current debt-to-capital ratio allow us to do without breaking the rating? | Existing leverage; rating-agency thresholds; covenant cushion | Treasury |
| **Cost of capital** | What rate should we discount the project at — firm WACC or project-specific? | Project risk profile relative to firm; comparable-firm betas | FP&A + Treasury |
| **Distribution / payout** | If we lever up for Plant 4, what does that constrain about the buyback program? | Forward cash projections; current authorization | CFO directly |
| **Operational** | What does the engineering / operations team actually believe about Plant 4's economics? | Construction timeline, ramp curve, labor and supply chain risk | Plant 4 program manager |"""

TABLES["three-beat method applied to Maya's memo"] = """| Beat | The question it answers | What failure looks like at Halverson | What success looks like |
|---|---|---|---|
| **Idea** | What is the question I have been asked? | Maya answers "should we fund Plant 4?" with a generic capital-budgeting analysis when Diane needed a debt-vs-equity recommendation | Maya restates the brief in writing back to Diane: *"You're asking whether to fund the $50M expansion with debt or equity, given the Cardinal advance, by Friday."* |
| **Execute** | What is the load-bearing analysis for that question? | Maya runs three analyses and chooses the one that confirms the answer the team is leaning toward | Maya names *one* analysis whose result, by itself, would change the recommendation — and runs it carefully |
| **Verify** | What would I want in writing if my recommendation turned out to be wrong? | The memo cites the FP&A WACC of 8% without naming the inputs or the date of last update | The memo carries the WACC inputs, the assumption sensitivities, and a *what-would-change-our-mind* sentence the audit committee can audit |"""

# === Ch 02 ===
TABLES["three-column summary of the three blind spots"] = """| Blind spot | What the outside analyst sees | What the inside view adds |
|---|---|---|
| **Accrual / cash divergence** | Net income from the income statement, OCF from the cash-flow statement, and the gap between them as a published number | The specific line items moving the gap (deferred revenue, accrued expenses, working-capital choices) and *why* — which choices were made deliberately by management to smooth or signal |
| **Accrual quality** | Reserve levels and revenue-recognition policies as disclosed; the auditor's signed opinion | Whether the reserve sizing is conservative or aggressive *given known operational realities* the public can't see (a customer about to file Chapter 11, a contract under renegotiation) |
| **Off-statement information** | The 10-K narrative; the earnings call; press releases | Internal forecasts, contract pipelines, customer-concentration data, the operations team's read on the next quarter — all the data that drives management's actual view of the firm |"""

TABLES["three-firm comparison — columns: Firm"] = """| Firm | Revenue trend | AR growth driver | Inside diagnostic | Interpretation of the gap |
|---|---|---|---|---|
| **Firm A** | Growing | New customers | AR aging skews to *current* (0–30 days) | Working-capital investment supporting genuine growth |
| **Firm B** | Stagnant | Slow payers | AR aging skews to 60–90 days | Bad debt accumulating; collections operationally broken |
| **Firm C** | Managed | Quarter-end contracts | AR spike concentrated in the final two weeks of the quarter | Earnings being misrepresented through aggressive cut-off practice |

*Identical summary numbers map to three entirely different business realities. Only the inside view distinguishes them.*"""

TABLES["conservative vs. aggressive accrual posture"] = """| Dimension | Conservative posture | Aggressive posture |
|---|---|---|
| **Reserve sizing** | Larger reserves for receivables, warranty, returns; pre-emptive write-downs | Reserves released into earnings opportunistically; write-downs deferred |
| **Revenue recognition timing** | Earlier-stage revenue deferred until risk is clearly transferred | Revenue recognized at the earliest defensible point in the contract |
| **Depreciation pace** | Shorter useful lives, faster expensing | Longer useful lives, slower expensing |
| **Earnings in good quarters** | Visibly understated; reserves built | Visibly amplified; reserves flat or released |
| **Earnings in bad quarters** | Cushioned by reserve releases; smoother trajectory | Visible drops with no buffer; volatility flows through |
| **Balance sheet resilience** | Higher reserves and lower book asset values; more room to absorb shocks | Tighter reserves and higher book asset values; less buffer |"""

# === Ch 03 ===
TABLES["Three-lever summary"] = """| Lever | Mechanism | Cash freed per day shortened | Key cost / risk |
|---|---|---|---|
| **DSO** | Tighten credit terms; improve collections | $3.8M | Customer attrition — the strict-terms version of *we're losing customers because we changed payment terms* |
| **DIO** | Faster inventory turns; just-in-time sourcing | $3.8M | Stockout exposure — single-source supply disruption hits the line |
| **DPO** | Extend supplier payment terms; renegotiate top-10 contracts | $3.8M | Supplier pricing increases; weakened relationships when supply tightens |

*The arithmetic is identical across levers. The organizational and strategic challenges are not.*"""

TABLES["AR aging schedule example for Halverson"] = """**Healthy book**

| Aging bucket | Balance ($M) | % of total AR | Healthy benchmark % |
|---|---|---|---|
| 0–30 days | 76 | 76% | 70–80% |
| 31–60 days | 18 | 18% | 15–20% |
| 61–90 days | 4 | 4% | 3–5% |
| 90+ days | 2 | 2% | < 3% |

**Deteriorating book**

| Aging bucket | Balance ($M) | % of total AR | Healthy benchmark % |
|---|---|---|---|
| 0–30 days | 52 | 52% | 70–80% |
| 31–60 days | 22 | 22% | 15–20% |
| 61–90 days | **18** | **18%** | 3–5% |
| 90+ days | **8** | **8%** | < 3% |

*The deteriorating book has the same total AR but the bulk has migrated past 60 days. The collections problem is diagnosable from the table alone.*"""

# === Ch 04 ===
TABLES["line-by-line FCFF build for Plant 4"] = """| | Year 0 | Year 1 | Year 2 | Year 3 |
|---|---|---|---|---|
| Revenue | $0 | $30M | $50M | $60M |
| EBIT | $0 | $8M | $18M | $25M |
| × (1 − tax rate) → NOPAT | $0 | $6.1M | $13.7M | $19.0M |
| + Depreciation | $0 | $5.0M | $5.0M | $5.0M |
| − Capex | **−$50M** | −$2M | −$2M | −$2M |
| − ΔWorking Capital | **−$5M** | −$3M | −$2M | −$1M |
| **= FCFF** | **−$55M** | $6.1M | $13.7M | $21.0M |

*Year 0 is large negative — construction plus the working-capital draw most analyses omit. Years 1–3 turn positive and grow as the ramp progresses.*"""

TABLES["the three failure modes side by side"] = """| Assumption | What the operations team modeled | What can go wrong | How to stress-test it | Owner of verification |
|---|---|---|---|---|
| **Utilization ramp** | 90% of nameplate capacity by month 18, sustained thereafter | Slower ramp (production yields, training, certification); capacity comes online but customers don't | Run NPV at 60% / 75% / 90% sustained utilization; identify the breakeven utilization | Plant 4 program manager + sales |
| **Cannibalization** | New capacity serves *new* demand — no overlap with existing plants | Customers who would have bought at higher margin from existing plants migrate to the lower-cost Plant 4 line | Estimate cannibalization at 0% / 10% / 25% of incremental volume | Sales operations |
| **Discount rate** | Firm WACC of 8.0%, applied uniformly | Project risk is higher than firm average (new-plant ramp, single customer concentration on the line) | Use a project-specific rate from comparable-firm betas; report NPV at firm WACC and project rate | FP&A |"""

# === Ch 05 ===
TABLES["six-input inventory"] = """| Input | Halverson's value | Source | Degree of judgment |
|---|---|---|---|
| **E (market equity)** | $1,840M | Shares outstanding × current price | **Low** (looked up) |
| **D (market debt)** | $660M | YTM-implied market value of outstanding debt | **Low** |
| **R_d (pretax cost of debt)** | 5.2% | YTM on outstanding bonds | **Low** |
| **Tax rate (T)** | 24% | Marginal — federal + state, blended | Medium (statutory vs. effective is a judgment) |
| **Weights E/V and D/V** | 73.6% / 26.4% (book); 50/50 (target) | Book vs. target — the choice itself is a judgment | **High** |
| **R_e (cost of equity from CAPM)** | 9.8% | $r_f + \\beta(\\text{ERP})$ — beta = 1.1, ERP = 5.0%, $r_f$ = 4.2% | **High** (every input argued) |"""

TABLES["two-way sensitivity table"] = """| | ERP 4.5% | ERP 5.0% | ERP 6.0% |
|---|---|---|---|
| **β = 0.9** | 7.5% | 7.7% | 8.1% |
| **β = 1.1** (base) | 7.8% | **8.0%** | 8.6% |
| **β = 1.3** | 8.2% | 8.5% | 9.6% |

*The defensible WACC for Halverson runs roughly 7.5% to 9.6% depending on β and ERP. The base case of 8.0% sits near the optimistic corner of the grid — anyone arguing for a higher β or higher ERP would push the rate to 8.5–9.6%.*"""

# === Ch 06 ===
TABLES["Extend the three-row NPV summary table"] = """| Scenario | NPV finding | What error it corrects | What the board is actually being asked to approve |
|---|---|---|---|
| **Row 1** — Original analysis at firm WACC | Negative NPV ($-3M$) at firm WACC | (No correction) — the project is overpriced as proposed | Approve $50M of capital today |
| **Row 2** — Project-specific rate | Positive NPV ($+8M$) at project-specific rate of 9.5% | Corrects the discount-rate mismatch — the project's risk profile differs from the firm's | Approve $50M of capital today |
| **Row 3** — Project-specific rate + deferral option | Positive NPV ($+15M$); option value $+7M$ | Corrects both the rate *and* the timing — flexibility is worth pricing in | Approve up to $50M with six-month deferral right pending Q2 demand data |

*The third column makes visible that the recommendation's structure changes, not just the number.*"""

TABLES["Sensitivity table — rows: discount rate"] = """| Discount rate | NPV without optionality | NPV with deferral option | Option value |
|---|---|---|---|
| **8.5%** | +$12M | +$22M | $10M |
| **9.0%** | +$5M | +$15M | $10M |
| **9.5%** | +$0M | +$11M | $11M |
| **10.0%** | −$5M | +$8M | $13M |

*Both NPV and option value move with the discount rate. The option is *more* valuable as the rate rises — uncertainty becomes more expensive, so flexibility becomes more valuable.*"""

# === Ch 07 ===
TABLES["the four MM assumptions"] = """| Assumption | What it rules out | What happens to the proof when you relax it |
|---|---|---|
| **No taxes** | Government's preferential treatment of debt over equity | Tax shield on interest is real; debt creates value equal to $T_c \\cdot D$ — addressed in Ch 7 (taxes) and Ch 8 (real-world structure) |
| **No bankruptcy costs** | Direct legal/professional fees and indirect customer/supplier flight when a firm becomes distressed | Distress cost is real; trade-off theory emerges — Ch 8 |
| **No information asymmetry** | Management knows things the market doesn't | Issuance signals matter (pecking order, market timing) — Ch 8, Ch 10 |
| **Equal borrowing rates** | Investors can replicate corporate leverage at the same rate | Investor borrowing rate exceeds corporate; corporate leverage adds value the investor can't undo — Ch 8 |"""

# === Ch 08 ===
TABLES["four-row inventory of dropped MM assumptions"] = """| Assumption | Why MM made it | What happens when you drop it |
|---|---|---|
| **Costless bankruptcy** | To isolate the financing decision from operational consequences of distress | Distress costs (direct + indirect + pre-distress operational distortions) become a real offset to the tax shield → trade-off theory |
| **No agency conflicts** | To treat manager-shareholder and shareholder-bondholder relations as frictionless | Debt disciplines free cash flow (Jensen); but debt also creates risk-shifting and underinvestment — agency costs of debt and of equity |
| **Symmetric information** | To treat the market as knowing everything management knows | Issuance becomes a signal: equity issuance signals overvaluation; debt issuance signals confidence — pecking-order theory and market-timing behavior |
| **No personal taxes** | To isolate corporate taxation as the only friction | Personal-tax wedge (dividends taxed differently from capital gains) reshapes payout policy — Miller (1977) corrects the tax-shield magnitude |"""

TABLES["three-category distress cost summary"] = """| Category | Description | Approximate magnitude | When it appears |
|---|---|---|---|
| **Direct costs** | Legal, professional, accounting, court-administration fees during the bankruptcy process itself | 3–7% of pre-distress enterprise value | At the filing — visible on the docket |
| **Indirect costs** | Customer flight, employee attrition, supplier tightening of terms when distress becomes visible | 10–25% of pre-distress enterprise value | During visible distress, often pre-filing |
| **Pre-distress operational distortions** | Underinvestment (deferred capex), forced asset sales, risk-shifting (high-variance projects to "swing for the fences") | Hard to estimate; can be the largest of the three | Before any filing — sometimes years before |

*The visible legal costs — what most analyses cite — are the smallest of the three. The pre-distress operational distortions are the largest and the hardest to see.*"""

TABLES["three-firm optimal leverage comparison"] = """| Firm type | Cash flow stability | Asset tangibility | Distress cost severity | Tax shield availability | Approximate optimal D/C range |
|---|---|---|---|---|---|
| **Halverson-type manufacturer** | Stable | High | Moderate | Full | **25–40%** |
| **High-growth software firm** | Volatile | Low | Very high (customers flee at first signal) | Limited (often no taxable income) | **5–15%** |
| **Regulated utility** | Contractually stable | High | Very low (regulator structure prevents most distress) | Full | **50–60%** |

*Same four-force framework; very different optimal structures depending on operating characteristics.*"""

# === Ch 09 ===
TABLES["Three-friction summary"] = """| Friction | What it is | How it favors dividends | How it favors buybacks | Who it affects most |
|---|---|---|---|---|
| **Taxes** | Personal-tax wedge between dividend income and capital gains | Tax-exempt holders (pension funds, endowments) are indifferent or prefer dividends for predictable distributions | Taxable holders prefer buybacks because deferral lowers effective tax rate | Mix of taxable and tax-exempt shareholders |
| **Information** | Management knows more about firm value than the market | Dividend smoothing creates a credible commitment about future cash flow | A buyback announcement is a managerial claim that the stock is undervalued | Firms whose stock price is most likely to be misvalued |
| **Clientele effects** | Different shareholder types prefer different distribution patterns | Income-seeking retail and pension investors prefer regular dividends | Growth-oriented institutional investors prefer buybacks (deferred tax + signaling) | Firms whose investor base is more homogeneous along income/growth dimension |"""

TABLES["Payout pattern comparison"] = """| Pattern | Commitment level | Tax efficiency | Signal content | Investor base it attracts | Flexibility to pause |
|---|---|---|---|---|---|
| **Regular quarterly dividend** | High — implicit contract that cuts are punished | Lower (taxed as income for taxable holders) | Strong, durable; cuts carry stigma | Income-seeking retail, dividend-focused funds | Low — pause is read as crisis |
| **Variable buyback program** | Low — discretionary at management's call | Higher (deferred capital-gains taxation) | Confidence in current valuation; can be paused without stigma | Growth and value-tilted institutional | High — easily paused |
| **Special dividend** | Single-event — no implicit commitment | Lower | Surprise distribution of exceptional cash | Mixed; reads as one-time | Trivial — by definition single-event |"""

TABLES["Maya's recommendation summary"] = """| Action | Action recommended | Rationale | What it signals | What it avoids |
|---|---|---|---|---|
| **Dividends** | Maintain $0.32/share quarterly; raise to $0.36 in Q1 2027 | Implicit-contract preservation; modest growth signals confidence | Continued cash-flow stability | The asymmetric punishment of a dividend cut |
| **Buybacks** | Authorize $200M program for 2027; deploy opportunistically | Tax efficiency; flexibility against Cardinal cash needs | Management's view that the stock is reasonably valued | Locking in distribution at a level that constrains the Cardinal financing |
| **Remaining cash** | Apply to debt paydown and Plant 4 funding | Capital structure work in Ch 8; Plant 4 portfolio decision in Ch 4 | Disciplined deployment | A balance-sheet build with no clear use |
| **Special dividend (rejected)** | Not recommended | One-time spike rewards short-term holders without changing the long-term commitment | (Not signaled) | Disrupting the dividend narrative |
| **Debt-funded buyback (rejected)** | Not recommended | Cardinal will consume the debt capacity; double-deploying would strain target leverage | (Not signaled) | Capital-structure incoherence |"""

# === Ch 10 ===
TABLES["IPO vs. SEO side-by-side"] = """| Cost component | Typical IPO | Typical SEO |
|---|---|---|
| **Gross spread** | 6–7% | 3–5% |
| **Average underpricing** | 10–20% (sometimes much higher) | 2–4% |
| **Announcement effect** | Initial-day pop; lockup-expiry pressure | Negative 1–3% on announcement |
| **Key driver of each cost** | Information asymmetry between issuer and market — who is the firm? | Information asymmetry already largely resolved |
| **Information asymmetry level** | High (no prior trading history) | Lower (price discovery has been happening) |

*Every cost is lower for SEOs because the prior trading history has already done some of the price-discovery work.*"""

# === Ch 11 ===
TABLES["synergy haircut model"] = """| Synergy category | Gross estimate | Haircut rationale | Haircut range | Haircutted NPV |
|---|---|---|---|---|
| **Cost synergies** — procurement, duplicate functions, plant rationalization | $200–300M | Empirically reliable; under management control; realized 60–90% of stated value in comparable deals | 70–80% retention | $140–240M |
| **Revenue synergies** — cross-selling through Halverson distribution | $40–80M | Requires customer behavior change the acquirer cannot control; realized 20–40% in comparable deals | 30–50% retention | $12–40M |

*The haircut asymmetry materially changes the deal economics and is not arbitrary. Revenue synergies routinely fail to materialize; cost synergies routinely do.*"""

TABLES["three diligence flags and structural mitigations"] = """| Risk | Mechanism by which it damages deal economics | Proposed structural mitigation |
|---|---|---|
| **Customer concentration** (35% of Cardinal revenue in two accounts) | If either account leaves post-close, revenue synergies erode and the standalone case weakens; combined entity may need to absorb the loss | Earnout / escrow tied to top-2-customer retention through 24 months post-close |
| **Integration timeline slippage** | Halverson has not done a deal this size in a decade; functions are stretched; synergy NPV decays at 24+ months delay | Name an integration lead with explicit accountability; quarterly board-level integration tracking with named milestones |
| **Seller information advantage** | Founder has 28 years of operational knowledge; hidden liabilities or dependency risks may surface post-close | 24-month transition agreement with milestone-linked retention; reps & warranties insurance for known-risk categories |"""

# === Ch 12 ===
TABLES["Halverson hedging program summary"] = """| Risk | Exposure size | Recommended instrument | Hedge ratio | Annual cost | Primary value-creation argument |
|---|---|---|---|---|---|
| **Interest Rate Risk** | $400M floating-rate debt | Pay-fixed swap on 50% of notional, 5-year tenor | 50% | $0.4M | Distress avoidance |
| **FX Transaction Risk** | $80M EUR-denominated annual revenue | Rolling 12-month forwards | 70% | $0.6M | Pipeline preservation — supports the customer-quoted price |
| **FX Translation Risk** | €40M net assets in UK subsidiary | **Do not hedge** | 0% | $0 | (No real cash-flow value; translation is an accounting artifact) |
| **Commodity Risk** | $25M annual specialty-polymer purchases | 6-month forward purchase contracts | 60% | $0.3M | Pipeline preservation — locks margin on quoted-price contracts |
| **Counterparty Risk** | Top-10 customer credit exposure | Trade-credit insurance on top-3 accounts | 100% | $0.4M | Distress avoidance + tax (deductible premium) |"""

# === Ch 13 ===
TABLES["the five international dimensions"] = """| Dimension | Analytically new vs. administrative overlay | What it changes in the analysis | Halverson UK exposure level |
|---|---|---|---|
| **Currency** | **New** | Cash flows must be denominated; discount rate must match currency; hedging is a real cost | **High** (UK subsidiary generates £-denominated revenue) |
| **Country risk** | **New** | Discount rate carries a country-risk premium; political and contract-enforcement risk priced explicitly | Low (UK is investment-grade sovereign) |
| **Tax (foreign jurisdiction)** | Administrative overlay | Effective tax rate changes; repatriation rules layer in | Medium (UK corporate tax + repatriation) |
| **Transfer pricing** | Administrative overlay | Where profit is booked vs. where it's earned; arm's-length-pricing documentation | Medium-High (intercompany IP licensing flows) |
| **Repatriation** | Administrative overlay | Withholding tax on dividends; cash trapped in subsidiary | Low (UK-US treaty is favorable) |"""

TABLES["three types of FX exposure compared"] = """| Exposure type | What drives it | Affects cash flows? | Hedgeable financially? | Halverson's response |
|---|---|---|---|---|
| **Transaction** | Specific contracts denominated in non-USD currency, settling in the future | **Yes** — currency move directly hits realized cash | **Yes** — forwards, futures, options | Hedge 70% via rolling 12-month forwards |
| **Translation** | Consolidation of foreign-subsidiary financial statements into USD | No — accounting artifact only | No (not really — only cosmetically) | Do not hedge |
| **Economic** | Long-run shift in competitive position from currency moves | **Yes** — but slowly, through margin compression and volume changes | Partial (operational hedges: matching cost and revenue currencies) | Address via operational footprint over time, not financial hedge |"""

TABLES["indicative country risk premiums"] = """| Country | Approximate CRP (bps) | Discount rate if base WACC is 8% | Primary driver of premium |
|---|---|---|---|
| **United States** | 0 | 8.0% | (Reference) |
| **United Kingdom** | 30 | 8.3% | Macro; mild contract-enforcement uncertainty post-Brexit |
| **Germany** | 50 | 8.5% | Macro; FX |
| **Brazil** | 250 | 10.5% | FX; political |
| **Argentina** | 800 | 16.0% | FX; macro; contract enforcement |
| **Russia** | 900+ | 17%+ | Political; contract enforcement |
| **Venezuela** | 1500+ | 23%+ | Political; FX; macro |

*The CRP is a bundled number masking several distinct risk types. For a real deployment in a high-CRP country, the bundling should be unbundled and each component priced separately.*"""

# === Ch 14 ===
TABLES["two-column contrast of the two behavioral finance"] = """| Dimension | Market behavioral finance | Corporate behavioral finance |
|---|---|---|
| **Subject** | Investors in capital markets | Managers and analysts inside firms |
| **Core claim** | Prices wrong in systematic ways | Capital allocators making systematic errors |
| **Observable evidence** | Return anomalies, momentum, post-earnings drift | Acquisition underperformance, project overruns, anchored discount rates |
| **Correction** | Trading strategy designed to exploit the anomaly | Deliberate process discipline (pre-mortem, devil's advocate, range over point) |"""

TABLES["pre-mortem vs. standard risk section"] = """| Dimension | Standard risk section | Pre-mortem |
|---|---|---|
| **Framing** | Risks to the current recommendation | Causes of an *assumed* failure two years from now |
| **Generation process** | Analyst identifies risks in the current plan | Analyst works backward from a stipulated failure to its causes |
| **Output specificity** | Often general ("execution risk") and quickly mitigated | Specific named mechanisms with early indicators |
| **Confirmation-bias pressure** | High — analyst is motivated to minimize | Low — failure is stipulated, the analyst's task is explanation |
| **Typical omissions** | Risks that, if surfaced, would change the recommendation | Risks already handled in the plan (so no need to revisit) |"""

TABLES["five pre-mortem scenarios"] = """| Scenario | Mechanism by which it damages deal economics | Early indicator trigger | Predetermined response |
|---|---|---|---|
| **Customer consolidation** | Top-2 Cardinal accounts merge or are acquired; combined buying power forces price renegotiation | Customer M&A activity in the segment; renegotiation requests within 6 months of close | Reopen synergy assumptions; size the price-concession reserve in the integration plan |
| **Management bandwidth exhaustion** | Halverson integration team can't run integration *and* core operations; product roadmap slips | Two consecutive quarters of integration milestones missed | Bring in external integration support; reduce the Q4 product release to defer roadmap pressure |
| **Founder departure** | Cardinal founder, despite retention agreement, accelerates departure; institutional knowledge walks | Founder-engagement metrics drop (meeting attendance, decision frequency) | Activate the 24-month transition agreement's milestone-payment clawback; accelerate knowledge-transfer to named internal owners |
| **Macro compression** | Industrial demand softens; both standalone and synergy projections weaken | Two-quarter compression in industry order books > 8% | Revisit the integration spend pace; defer non-essential capex; hold the buyback authorization |
| **Undisclosed liability** | Pre-close diligence missed an environmental, IP, or customer claim that surfaces post-close | Counsel notification of any claim within 18 months post-close | R&W insurance claim activation; reserve build; named legal-defense owner with quarterly board update |"""

# === Ch 15 ===
TABLES["Capital deployment summary"] = """| Investment | Capital deployed | Projected incremental EBITDA | Required EBITDA at 9% hurdle | Status vs. hurdle |
|---|---|---|---|---|
| **Plant 4** | $50M | $20–25M | $4.5M | **Clears** with substantial margin |
| **Cardinal Acquisition** | $700M | $50–60M (synergized) | $63M | **Borderline** — clears at the upper end of synergy realization, fails at the lower end |
| **Working Capital Program** | ($30M released) | $2.7M (interest savings on the freed capital) | n/a (capital-released, not capital-deployed) | **Net positive** |
| **Portfolio total** | **$720M (net)** | **$70–85M** | **~$65M** | **Clears in expectation; vulnerable on Cardinal alone** |"""

TABLES["Payout recommendation summary"] = """| Element | Amount | Rationale | Condition that changes it |
|---|---|---|---|
| **Dividend (current)** | $0.32 / share quarterly | Continuation of the current implicit contract | n/a |
| **Dividend (proposed)** | $0.36 / share quarterly beginning Q1 2027 | Modest growth signals confidence and tracks the EBITDA growth from Cardinal | If FY26 free cash flow falls below $400M, hold dividend flat at $0.32 |
| **Buyback (remaining authorization)** | $80M | Existing program; deploy opportunistically into FY26 weakness | n/a |
| **Buyback (new 2027 program)** | $200M | Tax-efficient capital return; flexibility against Cardinal cash needs | If leverage exceeds 3.5× EBITDA at any quarter-end, suspend buybacks |
| **Total capital return — 2026 actual** | $245M | Within target return band | n/a |
| **Total capital return — 2027 projected** | $310M | Within target return band assuming dividend raise + new buyback authorization | The leverage trigger above; the dividend trigger above |"""


def apply():
    pat = re.compile(r'<!--\s*→\s*\[TABLE:([^]]*?)(?:\]\s*-->|-->)', re.DOTALL)
    files = sorted(CH.glob('*.md'))
    total = 0
    miss = []
    for f in files:
        text = f.read_text()
        def replace(m):
            nonlocal total
            comment = m.group(0)
            for key, table in TABLES.items():
                if key in comment:
                    total += 1
                    return table
            miss.append((f.name, comment[:80]))
            return comment
        new_text = pat.sub(replace, text)
        if new_text != text:
            f.write_text(new_text)
    print(f"replaced: {total} tables")
    if miss:
        print(f"\nMISSED ({len(miss)}):")
        for fn, c in miss:
            print(f"  {fn}: {c}")


if __name__ == "__main__":
    apply()
