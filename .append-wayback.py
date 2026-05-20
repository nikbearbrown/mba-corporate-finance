#!/usr/bin/env python3
"""Append `## AI Wayback Machine` blocks to each of the 15 content chapters
of corporate-finance-with-ai. Spec says insert after the LLM Exercise block;
this book has none, so anchor at end-of-file.

All figures are pre-2001 dead OR foundational pre-2001 work, none overlapping
the rosters of botspeak / branding-and-ai / computational-skepticism-for-ai /
living-models / computational-finance-with-ai.
"""
from pathlib import Path

ROOT = Path(__file__).parent
CH = ROOT / "chapters"

ENTRIES = [
    (
        "01-the-cfos-first-question.md",
        "Donaldson Brown",
        "designing the financial control system at DuPont in the 1910s and at General Motors in the 1920s — including the *DuPont identity* every CFO still asks first about return on equity",
        "the CFO's first question and the financial-control framing that produces it",
        "Who was Donaldson Brown, and how does his work designing the DuPont financial control system — and the *DuPont decomposition* of return on equity — connect to the chapter's argument that a CFO's first question is not *what's the number?* but *what does the number require to mean what it claims to mean?* Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Donaldson Brown",
        "Ask it to explain the *DuPont identity* in plain language, as if you've never seen ROE decomposed",
        "Ask it to compare Brown's 1920s GM control system to a modern CFO's monthly review",
        'Add a constraint: "Answer as if you\'re writing the rationale for the CFO\'s first three questions in any new fiscal year"',
    ),
    (
        "02-reading-the-firm-from-inside.md",
        "Mary Harris Smith",
        "becoming, in 1919, the first woman chartered accountant in the world — over four decades after she had already been doing the work without being credentialed for it",
        "reading a firm's books from inside, with the discipline that distinguishes a manager's view from an outside analyst's",
        "Who was Mary Harris Smith, and how does her career — including the four-decade gap between her competence and her credentialing — connect to the chapter's argument that *reading the firm from inside* requires both technical accounting fluency and the practitioner-level access that historically gated who could exercise it? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.",
        "Mary Harris Smith",
        "Ask it to explain why the *insider's view of the books* is structurally different from the *analyst's view*, in plain language",
        "Ask it to compare the credentialing barriers Smith fought to the access barriers a modern non-finance manager hits when reading their own firm",
        'Add a constraint: "Answer as if you\'re writing the introduction to a chapter on reading financial statements as a manager, not as an analyst"',
    ),
    (
        "03-working-capital-is-where-the-cash-lives.md",
        "John Hicks",
        "publishing *Value and Capital* in 1939 — including the *liquidity preference* framework that explains why firms hold cash even when cash earns less than other assets",
        "working capital management and the structural reasons firms hold the liquidity they do",
        "Who was John Hicks, and how does his concept of *liquidity preference* — the framework explaining why economic actors hold low-yielding cash even when alternatives exist — connect to the chapter's treatment of working capital and the trade-offs in the cash conversion cycle? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "John Hicks economist",
        "Ask it to explain *liquidity preference* in plain language, as if you've never seen Keynes",
        "Ask it to compare Hicks's framework to the modern question of why a profitable firm chooses to carry $5B in cash on its balance sheet",
        'Add a constraint: "Answer as if you\'re writing the rationale for a target cash balance in a treasury policy"',
    ),
    (
        "04-capital-budgeting-at-the-firm-level.md",
        "Joel Dean",
        "publishing *Capital Budgeting* in 1951 — the foundational text that brought NPV and IRR out of the journals and into corporate practice",
        "capital budgeting at the firm level, with NPV as the primary decision rule",
        "Who was Joel Dean, and how does his 1951 book *Capital Budgeting* — translating present-value mathematics into a corporate decision rule — connect to the chapter's argument that NPV is not just a math technique but the structural form of every honest investment decision a firm makes? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Joel Dean economist",
        "Ask it to explain *NPV vs. IRR* in plain language, as if you've never run a capital-budgeting analysis",
        "Ask it to compare Dean's 1951 framework to the modern stage-gate process at a Fortune 500 firm",
        'Add a constraint: "Answer as if you\'re writing the policy memo establishing capital-budgeting standards for a new business unit"',
    ),
    (
        "05-the-cost-of-capital-and-the-wacc.md",
        "Fischer Black",
        "co-developing the option-pricing apparatus, *and* — less famously — extending CAPM into the *zero-beta model* in 1972, which is the foundational case for how a firm's cost of capital is actually estimated when borrowing rates differ from the textbook risk-free rate",
        "the cost of capital and the weighted average cost of capital (WACC)",
        "Who was Fischer Black, and how does his 1972 *zero-beta CAPM* — extending Sharpe's model to handle the realistic case where borrowing and lending rates differ — connect to the chapter's apparatus for estimating a firm's cost of equity, cost of debt, and weighted average cost of capital? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Fischer Black",
        "Ask it to explain *the zero-beta CAPM* in plain language, as if you've already seen the standard CAPM",
        "Ask it to compare Black's adjustment to the practical case where a firm's borrowing rate is 7% and the risk-free Treasury is 3%",
        'Add a constraint: "Answer as if you\'re writing the cost-of-capital methodology section of a corporate finance policy"',
    ),
    (
        "06-risk-adjusted-rates-and-real-options.md",
        "Irving Fisher",
        "publishing *The Theory of Interest* in 1930 — the foundational treatment of how rational actors trade present consumption against uncertain future cash flows, the structural ancestor of every risk-adjusted discount rate and every real-option valuation",
        "risk-adjusted rates and real options",
        "Who was Irving Fisher, and how does his 1930 *Theory of Interest* — the formal account of intertemporal choice under uncertainty — connect to the chapter's apparatus for risk-adjusted discount rates and the real-options framework for projects whose value depends on flexibility, not certainty? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Irving Fisher",
        "Ask it to explain *Fisher's separation theorem* in plain language, as if you've never read intertemporal choice theory",
        "Ask it to compare Fisher's discounting framework to the modern real-options approach for an R&D investment",
        'Add a constraint: "Answer as if you\'re writing the discount-rate justification for a project with deferred information value"',
    ),
    (
        "07-capital-structure-theory-the-modigliani-miller-world.md",
        "Merton Miller",
        "co-publishing the *Modigliani-Miller theorem* in 1958 — the result that, under specific frictionless-market assumptions, the value of a firm is independent of how it is financed",
        "capital structure theory in the Modigliani-Miller world",
        "Who was Merton Miller, and how does the 1958 *Modigliani-Miller theorem* — that under perfect-market assumptions a firm's value is independent of its debt-equity mix — connect to the chapter's argument that the MM result is most useful as a *baseline* whose required violations name the real determinants of capital structure? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Merton Miller",
        "Ask it to explain *the MM irrelevance theorem* in plain language, as if you've never seen capital-structure mathematics",
        "Ask it to compare Miller's 1958 paper to the messier 1963 paper accounting for taxes — what changed and why it matters",
        'Add a constraint: "Answer as if you\'re writing the case for *why MM is the right baseline* in a corporate finance class"',
    ),
    (
        "08-capital-structure-in-the-real-world.md",
        "Adolf A. Berle",
        "co-authoring *The Modern Corporation and Private Property* in 1932 with Gardiner Means — the foundational analysis of what *capital structure in the real world* actually looks like once ownership and control separate",
        "real-world capital structure, the agency problem, and the determinants of debt-equity choice that MM rules out by assumption",
        "Who was Adolf A. Berle, and how does his 1932 analysis of the modern corporation — particularly the separation of ownership from control — connect to the chapter's argument that real-world capital structure is shaped by agency costs, asymmetric information, and managerial entrenchment that the Modigliani-Miller world rules out by assumption? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Adolf A. Berle",
        "Ask it to explain *the separation of ownership and control* in plain language, as if you've never read corporate governance",
        "Ask it to compare Berle's 1932 description of the modern corporation to a 21st-century private-equity-owned firm",
        'Add a constraint: "Answer as if you\'re writing the real-world-frictions paragraph in a capital-structure memo"',
    ),
    (
        "09-returning-capital-dividends-buybacks-and-the-choice-between-them.md",
        "Gardiner C. Means",
        "documenting in the 1930s — at the same time as his co-author Berle — the empirical patterns of corporate dividend policy and the way managers use distributions as signals to a market they cannot fully control",
        "returning capital through dividends and buybacks, and the choice between them",
        "Who was Gardiner C. Means, and how does his empirical work on corporate dividend policy — and the related concept of *administered prices* in modern firms — connect to the chapter's argument that the choice between dividends and buybacks is a signaling decision as much as a tax decision? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Gardiner Means",
        "Ask it to explain *administered prices* in plain language, as if you've only ever read about competitive markets",
        "Ask it to compare Means's 1930s observation of corporate dividend smoothing to a modern buyback program",
        'Add a constraint: "Answer as if you\'re writing the case for a buyback over a dividend in a board-room recommendation"',
    ),
    (
        "10-raising-capital-ipos-secondaries-and-the-cost-of-going-to-market.md",
        "Maggie Lena Walker",
        "founding *St. Luke Penny Savings Bank* in 1903 — becoming the first African-American woman to charter and run a US bank, raising capital from communities the established financial system was designed to exclude",
        "raising capital through public markets and the costs of going to them",
        "Who was Maggie Lena Walker, and how does her early-twentieth-century work mobilizing capital from a community the formal capital markets did not serve — through a chartered bank, an insurance company, and a department store — connect to the chapter's treatment of the costs of going to market and the structural barriers to raising capital that the standard IPO framework treats as fixed? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.",
        "Maggie Lena Walker",
        "Ask it to explain why *who has access to capital markets* is a structural question rather than a regulatory one, in plain language",
        "Ask it to compare Walker's St. Luke Penny Savings Bank to a modern community development financial institution (CDFI)",
        'Add a constraint: "Answer as if you\'re writing the chapter introduction to a section on the structural costs of accessing public markets"',
    ),
    (
        "11-m-and-a-the-largest-decisions-a-cfo-makes.md",
        "Edith Penrose",
        "publishing *The Theory of the Growth of the Firm* in 1959 — the foundational case that a firm's growth is bounded by its *managerial capacity*, not by its capital, and that this constraint is what determines when an acquisition creates value and when it destroys it",
        "M&A and the question of when a deal creates rather than destroys value",
        "Who was Edith Penrose, and how does her 1959 *Theory of the Growth of the Firm* — the argument that managerial capacity, not capital, is the binding constraint on growth — connect to the chapter's analysis of when an M&A deal creates value (the acquirer can manage what it just bought) and when it destroys value (it cannot)? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.",
        "Edith Penrose",
        "Ask it to explain *the Penrose effect* in plain language, as if you've never read theory of the firm",
        "Ask it to compare Penrose's 1959 framing to a modern post-merger-integration failure",
        'Add a constraint: "Answer as if you\'re writing the case against a strategically-attractive but managerially-overstretched acquisition"',
    ),
    (
        "12-operational-risk-management.md",
        "Karl Borch",
        "founding modern actuarial science as a quantitative discipline in the 1960s and 1970s — particularly his theorem that determines, mathematically, how much risk a firm should retain versus transfer through insurance",
        "operational risk management and the retain-vs-transfer decision",
        "Who was Karl Borch, and how does his foundational work on the economics of insurance — particularly the *Borch theorem* on optimal risk sharing — connect to the chapter's framework for deciding which operational risks a firm should retain on its balance sheet and which it should transfer through insurance, hedging, or contractual allocation? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Karl Borch",
        "Ask it to explain *the Borch theorem on Pareto-optimal risk sharing* in plain language, as if you've never read actuarial mathematics",
        "Ask it to compare Borch's 1960s framework to a modern enterprise-risk-management committee's retain-vs-transfer decision",
        'Add a constraint: "Answer as if you\'re writing the risk-allocation policy for a manufacturer with global operations"',
    ),
    (
        "13-international-corporate-finance.md",
        "Susan Strange",
        "founding *international political economy* as a discipline in the 1970s and 1980s — including her account of *casino capitalism* and *mad money*, the foundational analyses of how international financial flows actually move and what they cost the firms exposed to them",
        "international corporate finance, currency exposure, and the political economy of cross-border capital",
        "Who was Susan Strange, and how does her work on the *political economy of international finance* — including her analyses of casino capitalism, mad money, and the structural power that international financial flows give certain actors — connect to the chapter's treatment of currency hedging, transfer pricing, and the real costs of operating a firm across borders? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.",
        "Susan Strange",
        "Ask it to explain *structural power in international finance* in plain language, as if you've never read political economy",
        "Ask it to compare Strange's 1980s account of cross-border capital flows to a modern multinational's currency-hedging policy",
        'Add a constraint: "Answer as if you\'re writing the case for treating FX exposure as a strategic, not just operational, decision"',
    ),
    (
        "14-behavioral-corporate-finance.md",
        "Daniel Bernoulli",
        "publishing the *Exposition of a New Theory on the Measurement of Risk* in 1738 — the foundational treatment of expected utility, the St. Petersburg paradox, and the gap between mathematical expected value and actual human decision-making under uncertainty",
        "behavioral corporate finance and the systematic deviations from rational-actor models",
        "Who was Daniel Bernoulli, and how does his 1738 *Exposition of a New Theory on the Measurement of Risk* — including the St. Petersburg paradox and the case for expected *utility* over expected *value* — connect to the chapter's argument that behavioral corporate finance is largely a catalog of where actual managerial decisions deviate from the rational-actor benchmarks the prior chapters built? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Daniel Bernoulli",
        "Ask it to explain *the St. Petersburg paradox* in plain language, as if you've never seen utility theory",
        "Ask it to compare Bernoulli's 1738 framing of risk aversion to Kahneman and Tversky's prospect theory",
        'Add a constraint: "Answer as if you\'re writing the historical preface to a chapter on managerial overconfidence"',
    ),
    (
        "15-the-capstone-an-integrated-cfo-recommendation.md",
        "Joseph Schumpeter",
        "publishing *The Theory of Economic Development* in 1911 — the foundational integrated account of how capital decisions, entrepreneurial activity, and *creative destruction* interact at the level of a firm and an economy",
        "an integrated CFO recommendation that holds every prior chapter's tools at once",
        "Who was Joseph Schumpeter, and how does his integrated theory — *creative destruction*, the entrepreneur as the agent of capital reallocation, the firm as the unit of decision under genuine uncertainty — connect to the chapter's capstone argument that a real CFO recommendation cannot be assembled by stacking the prior chapters' techniques but only by holding them all in tension at once? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Joseph Schumpeter",
        "Ask it to explain *creative destruction* in plain language, as if you've only ever read efficient-markets theory",
        "Ask it to compare Schumpeter's account of the entrepreneur-CEO to the role of a modern integrated CFO",
        'Add a constraint: "Answer as if you\'re writing the case for treating the CFO\'s integrated recommendation as a creative act, not a calculation"',
    ),
]


BLOCK = """
---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **{name}** was {framing} decades before most people had heard of {concept}. Here's a prompt to find out more — and then make it better.

**Run this:**

```
{prompt}
```

→ Search **"{search}"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- {v1}
- {v2}
- {v3}

What changes? What gets better? What gets worse?
"""


def main():
    seen = set()
    for entry in ENTRIES:
        filename, name, framing, concept, prompt, search, v1, v2, v3 = entry
        if name in seen:
            print(f"!!! DUPLICATE: {name}")
        seen.add(name)
        path = CH / filename
        text = path.read_text()
        if "## AI Wayback Machine" in text:
            print(f"  SKIP (already present): {filename}")
            continue
        block = BLOCK.format(name=name, framing=framing, concept=concept,
                             prompt=prompt, search=search, v1=v1, v2=v2, v3=v3)
        new_text = text.rstrip() + "\n" + block + "\n"
        path.write_text(new_text)
        print(f"  appended Wayback ({name}) to {filename}")
    print(f"\nfigures included: {len(seen)} unique")


if __name__ == "__main__":
    main()
