# Corporate Finance with AI

**Author:** Nik Bear Brown
**Status:** Rough first-pass drafts complete (April 2026). Not yet reviewed. Not published.
**Sibling project to:** *Computational Finance with AI* (Book 1)

---

## What this book is

A working CFO's textbook. Fifteen chapters that take the reader from "I know what stocks and bonds are but I have no idea how a CFO actually allocates capital" to "I can produce a defensible CFO recommendation that integrates investment, financing, and payout decisions."

Where Book 1 (*Computational Finance with AI*) taught the reader to analyze publicly traded assets from outside, this book sits the reader inside the CFO's office and teaches her to read the firm, allocate capital across investments and financing structures, and execute the strategic decisions that define the role.

The voice is Feynman-flavored — clarity as intellectual honesty, machinery visible, jargon stripped or taught, math on the page when the argument is quantitative, calibrated uncertainty over false confidence. The default tool is Claude with a verification discipline (the three-beat method: verify → calculate → sanity-check). At no point does the book retreat into Excel-based pedagogy.

## What this book is NOT

- Not a survey of corporate finance topics. The chapters are sequenced as a single arc, not a list.
- Not a popular-science skim. The mechanism is unpacked when it matters; the math goes on the page.
- Not jargon-dressed academic writing. Technical terms earn their place by doing work.
- Not AI-evangelism. When LLMs are the instrument, they get examined honestly — what they do well, what they fail at, and what verification protects against.

## Who this is for

MBA finance students who have completed an investments core (or Book 1: *Computational Finance with AI*). Readers should arrive knowing what stocks and bonds are, able to run a DCF on a public company, and comfortable with Claude as an analytical instrument under the three-beat method. Readers without the toolkit can still follow — Chapter 1 carries the onboarding load for both audiences.

The capability the book builds: produce an integrated capital allocation memo that a CFO would defend at a board meeting. Most readers will not become CFOs in the next decade — they will be analysts, founders, consultants, treasurers, and FP&A leads — but the capability serves all of them.

---

## The three-act arc

The fifteen chapters are organized into three acts of 3–5–7 chapters. Each act builds on the previous one and ends with an explicit transition into the next.

### Act 1 — Read the Firm (Chapters 1–3)

Establishes the inside-the-firm perspective. Where an outside analyst reads published statements as a finished product, the CFO reads them as a working document — and reads the operations, the controller's working file, and the daily cash report alongside. By the end of Act 1, the reader can read a company the way a CFO reads it.

**Closing capability:** Can read a firm's statements with the inside view, treats working capital as a daily reality, has the three-beat method as a working habit.

**Bridge to Act 2:** Working capital management frees up internal capital. The natural next question is: what should we do with it?

### Act 2 — Allocate Capital (Chapters 4–8)

Builds the capability to allocate capital across investments and financing structures. Both sides of the balance sheet — what to fund (Ch 4–6) and how to fund it (Ch 7–8). The conceptual pivot of the book lives in the Ch 7–8 paired chapters, which must be read in sequence: Ch 7 establishes Modigliani-Miller as the theoretical baseline and forces the reader to use the tax shield as a measuring stick; Ch 8 deviates from MM to show the frictions that produce real-world capital structures.

**Closing capability:** Can evaluate a firm-level capital project, calculate and apply cost of capital with risk adjustments, recommend a capital structure change with quantified value impact.

**Bridge to Act 3:** The firm now knows how to fund and structure its operations. What about returning capital to shareholders, raising external capital, or executing strategic transactions?

### Act 3 — Distribute and Execute (Chapters 9–15)

Synthesizes everything into the full CFO decision portfolio. Three sub-arcs:

- **Capital movement (Ch 9–10):** Cash flows out (payout) and in (security issuance).
- **Strategic transactions (Ch 11):** M&A as the largest single corporate finance decision, integrating every prior tool.
- **Risk, context, and integration (Ch 12–15):** Operational risk, international layer, behavioral honesty, and the integrated capstone.

**Closing capability:** Can integrate investment, financing, payout, and risk decisions into one defensible CFO recommendation. The capability the book promised in Chapter 1.

---

## Table of Contents

### Front matter

- **Front Matter** — Author bio, acknowledgments, dedication. *(file: `00-frontmatter.md`)*

### Act 1 — Read the Firm

- **Ch 1. The CFO's First Question** — Maya Chen's third week as a senior analyst at Halverson Industries. The CFO asks her to evaluate $50M debt vs. equity for a plant expansion. The chapter introduces the inside-the-firm perspective, the three-beat method rehearsed for CFO contexts, and the verification toolkit. Onboarding load chapter — works for Book 1 returnees and fresh starters. *(file: `01-the-cfos-first-question.md`)*

- **Ch 2. Reading the Firm from Inside** — What a CFO sees in the published statements that an outside analyst cannot. The divergence between accrual earnings and operating cash. Aaron the controller, his 87-tab close package, and the diagnostic question that begins every CFO orientation. *(file: `02-reading-the-firm-from-inside.md`)*

- **Ch 3. Working Capital Is Where the Cash Lives** — The cash conversion cycle as the operational lens. Tom the treasurer's daily cash report. DSO, DIO, DPO and the dollar amount of cash continuously locked into operations. Working capital as the cheapest source of internal financing. *(file: `03-working-capital-is-where-the-cash-lives.md`)*

### Act 2 — Allocate Capital

- **Ch 4. Capital Budgeting at the Firm Level** — NPV when the project is yours, not a public-company comparable. Cash flow projection construction from operating reality. Sunk costs, opportunity costs, terminal values, and the three ways NPV goes wrong even when the math is right. *(file: `04-capital-budgeting-at-the-firm-level.md`)*

- **Ch 5. The Cost of Capital and the WACC** — What "cost of capital" means in three different jobs the term is doing simultaneously. The WACC formula's six inputs, three of which are judgment calls. Why Halverson's "8% WACC" is not actually 8% under scrutiny. *(file: `05-the-cost-of-capital-and-the-wacc.md`)*

- **Ch 6. Risk-Adjusted Rates and Real Options** — Two errors in the standard NPV: using firm-average WACC when the project is riskier than average, and ignoring the option to defer/expand/abandon. Pure-play comparables for project-specific discount rates; decision trees for valuing flexibility. *(file: `06-risk-adjusted-rates-and-real-options.md`)*

- **Ch 7. Capital Structure Theory: The Modigliani-Miller World** — *Paired with Ch 8.* The MM propositions as a theoretical baseline. The chapter forces the reader to use MM as a measuring stick by quantifying the tax shield within the chapter itself. Concludes with the implication that 100% debt would be optimal — setting up Ch 8's frictions. *(file: `07-capital-structure-theory-the-modigliani-miller-world.md`)*

- **Ch 8. Capital Structure in the Real World** — *Paired with Ch 7.* The four frictions that push back against debt: financial distress costs, agency costs, asymmetric information, and the limits of the tax shield. The trade-off and pecking-order theories. Maya's recommendation for Plant 4 financing with quantified value impact. *(file: `08-capital-structure-in-the-real-world.md`)*

### Act 3 — Distribute and Execute

- **Ch 9. Returning Capital: Dividends, Buybacks, and the Choice Between Them** — Payout policy as three decisions, not one: amount, form, pattern. The Lintner stickiness of dividends, the flexibility and abuse risk of buybacks, the clientele effects that constrain policy changes. Halverson's capital allocation committee meeting. *(file: `09-returning-capital-dividends-buybacks-and-the-choice-between-them.md`)*

- **Ch 10. Raising Capital: IPOs, Secondaries, and the Cost of Going to Market** — The visible cost (underwriting fees) and the larger invisible costs (underpricing, announcement effect). The 7% solution puzzle in IPO underwriting. When external equity is the right move and when the pecking order says no. *(file: `10-raising-capital-ipos-secondaries-and-the-cost-of-going-to-market.md`)*

- **Ch 11. M&A: The Largest Decisions a CFO Makes** — Halverson considers acquiring Cardinal Flow Systems. Standalone DCF, precedent transactions, and synergy valuation. The empirical record on acquirer returns (sobering). Three diligence flags that shape the deal structure. The chapter where every prior tool gets used. *(file: `11-m-and-a-the-largest-decisions-a-cfo-makes.md`)*

- **Ch 12. Operational Risk Management** — Hedging interest rate, FX, and commodity exposure. The MM-style irrelevance result for hedging and the three deviations that give it economic content (distress costs, tax convexity, financing constraints). When to hedge, when to bear the risk, what derivatives actually cost. *(file: `12-operational-risk-management.md`)*

- **Ch 13. International Corporate Finance** — Halverson's UK subsidiary and the £25M repatriation decision. Currency exposure (transaction, translation, economic), country risk premiums, transfer pricing, and the tax planning that gets harder every year. When "international" is just "domestic with extra steps" and when it isn't. *(file: `13-international-corporate-finance.md`)*

- **Ch 14. Behavioral Corporate Finance** — Where rigorous analysis still produces poor outcomes. Overconfidence, anchoring, escalation of commitment, and confirmation bias as documented patterns in CFO decision-making. Reference class forecasting, pre-mortem analysis, and the verification countermoves. Maya's pre-mortem for the Cardinal integration. *(file: `14-behavioral-corporate-finance.md`)*

- **Ch 15. The Capstone: An Integrated CFO Recommendation** — The November board memo. Four interrelated decisions held simultaneously: capital allocation, capital structure, payout, and risk position. The verification chain made explicit. Three tensions the integrated recommendation must hold without resolving. The defensible artifact the book has been building toward. *(file: `15-the-capstone-an-integrated-cfo-recommendation.md`)*

---

## The running narrative

Every chapter threads through one protagonist and one firm:

- **Maya Chen** — A senior analyst in the CFO's office, first year out of an MBA program. Has Book 1's three-beat method installed and a Claude account from her investments coursework. Begins the book unable to write a debt-vs-equity memo. Ends the book as the lead drafter of Halverson's annual integrated capital memo.

- **Halverson Industries** — A mid-cap public industrial firm headquartered in Cleveland, ~$2B revenue, manufacturing industrial pumps and flow-control equipment. Stable cash flows, modest leverage, an underutilized debt capacity, a UK subsidiary, an active capex program, and (in Chapter 11) a strategic acquisition target.

- **Diane Park** — Halverson's CFO. Maya's manager. Assigns the memos, reads the drafts, edits, and signs.

- **Tom (Treasurer)** — Operational financial discipline. Daily cash report. Where Maya learns that strategic decisions live downstream of cash management.

- **Aaron (Controller)** — The 87-tab close package. Where Maya learns that published statements are the output, not the input.

- **Cardinal Flow Systems** — The acquisition target introduced in Chapter 11. A privately held competitor with a founder considering retirement.

The narrative is not a frame. It is the pedagogy. CFO work is contextual; the analysis depends on the firm's specific position; the recommendation has to be defensible to specific people at a specific board meeting. The running characters and firm let every chapter's analysis land in a defensible specific situation rather than in the abstract.

---

## Voice and method

The voice baseline lives in the workshop's root `style/` folder and in `CLAUDE.md`. Per-book voice samples (when added) will live in `style/` under this book's folder and override the root on conflict. As of April 2026, the per-book `style/` is empty; the first review pass should calibrate voice deliberately. Drafts produced before that pass are flagged `voice-unanchored` at the top of each chapter file.

The method is Feynman's four-move pedagogical arc, applied to each chapter:

1. **Hook with a genuine puzzle.** Maya facing a specific problem, a dated event, a number that doesn't add up, a question that looks obvious until you try to answer it. Never opens in abstraction.
2. **Unfold the subject — force the concept specific.** Pull apart the vague terms. "Cost of capital" means three different things; "working capital" needs respecification.
3. **Deep-dive on one mechanism.** The heart of each chapter. One thing explained well. Math on the page when the argument is quantitative. Celebrate the clever; admit the ugly.
4. **Synthesize, hand to reader, close with clarity.** Return to the puzzle with the new understanding. Name what the evidence does and does not settle.

Every chapter ends with two commitments:

- **What would change my mind** — The specific evidence or argument that would cause the chapter's reading to revise.
- **Still puzzling** — The honest admission of what the author does not yet fully understand. Feynman's move.

---

## Relationship to Book 1

Book 2 is a sibling, not a sequel. The reader can pick up Book 2 directly. But significant pedagogical capital was built in Book 1 that Book 2 inherits:

- **The three-beat method** (verify → calculate → sanity-check) is rehearsed in Book 2's Chapter 1 for CFO contexts.
- **The verification toolkit** (Claude account, primary source discipline, "show the work" expectations) carries over directly.
- **Maya as protagonist** — Book 1 readers know her. Book 2 begins with her stepping into a different role at a different firm.
- **The Excel-rejection thesis** is inherited and reinforced — Book 1 made the case; Book 2 lives it.

Readers without Book 1 should expect Chapter 1 to do extra onboarding work. Book 1 returnees can move through Chapter 1 quickly and arrive at the inside-the-firm distinction without re-installing the toolkit.

---

## Adoption notes

The act structure means this book is adoptable in fragments, with caveats:

- **Full course (Ch 1–15).** A semester MBA Corporate Finance core. The whole arc.
- **Two-semester split.** Ch 1–8 in fall (read the firm + allocate capital); Ch 9–15 in spring (distribute and execute). Note: the natural break leaves the integration capstone for the second semester. Faculty teaching only the first half should be aware that semester 1 ends before any of the strategic-transaction or capstone material.
- **Three-week module (Ch 1–3 only).** "Reading the firm as a CFO" — a teachable unit on its own, suitable as introductory content.
- **Capital allocation module (Ch 4–8).** Investment and financing decisions, common scope in MBA programs that split corporate finance across two terms.

Adopters should note: the Ch 7–8 paired pivot must be read in sequence. Ch 7 alone does not work — its lessons are unstable until Ch 8 establishes the frictions context. The book's documentation flags this explicitly at the top of both chapters.

---

## Repository structure

```
corporate-finance-with-ai/
├── README.md                              # this file
├── book.md                                # book metadata: audience, scope, voice notes
├── outline.md                             # chapter list with one-sentence purposes
├── l3-arc.md                              # the three-act arc spec (locked)
├── l3-arc-pushback.md                     # structural critique of the /l3 (unresolved)
├── chapter-batch-pushback.md              # critique of the initial chapter-batch brief
├── rename-chapters.sh                     # utility for renaming chapter files
├── chapters/                              # chapter drafts
│   ├── 00-frontmatter.md
│   ├── 01-the-cfos-first-question.md
│   ├── 02-reading-the-firm-from-inside.md
│   ├── 03-working-capital-is-where-the-cash-lives.md
│   ├── 04-capital-budgeting-at-the-firm-level.md
│   ├── 05-the-cost-of-capital-and-the-wacc.md
│   ├── 06-risk-adjusted-rates-and-real-options.md
│   ├── 07-capital-structure-theory-the-modigliani-miller-world.md
│   ├── 08-capital-structure-in-the-real-world.md
│   ├── 09-returning-capital-dividends-buybacks-and-the-choice-between-them.md
│   ├── 10-raising-capital-ipos-secondaries-and-the-cost-of-going-to-market.md
│   ├── 11-m-and-a-the-largest-decisions-a-cfo-makes.md
│   ├── 12-operational-risk-management.md
│   ├── 13-international-corporate-finance.md
│   ├── 14-behavioral-corporate-finance.md
│   └── 15-the-capstone-an-integrated-cfo-recommendation.md
├── essays/                                # chapter-adjacent longreads (planned)
├── exercises/                             # /mega LLM-exercise sets (planned)
├── bookmaps/                              # /bookmap analyses of source books (planned)
├── style/                                 # per-book voice samples (currently empty)
├── images/                                # hero image briefs (planned)
└── research/                              # primary-source research notes per chapter (planned)
```

---

## Status

**April 2026.** All 15 chapters drafted as rough first passes. Each draft is marked `voice-unanchored` at the top because per-book `style/` samples have not yet been populated. Each draft uses `[verify]` flags inline for specific statistics and citations that need source-checking before publication.

**Three structural concerns remain unresolved** (documented in `l3-arc-pushback.md`):

1. The 3–5–7 act asymmetry creates an awkward two-semester split with all integration content in semester 2.
2. The Ch 14 (Behavioral) → Ch 15 (Capstone) sequencing risks Ch 14 being skimmed because the capstone is looming. Distributing behavioral discipline through Acts 2–3 is the proposed alternative.
3. The Ch 15 capstone integrates a lot. Splitting into capstone framework + applied case is the proposed alternative.

These should be resolved before any chapter moves toward final review.

**Nothing has been published from this folder. The human review gate is inviolable.** Drafts are produced for Nik's review, not in Nik's place.

---

## Who This Book Is For

reader's roadmap)

This file is a stub. Sections 1–10 and 12–13 are placeholders for a later pass.
Section 11 (A note about AI) is substantive and written.

A good model for the full version: Pearl's "The Mind Over Data" introduction,
Molnar's Interpretable ML introduction. Both are argument-first and tell the
reader exactly what to expect from each chapter.
-->

# Introduction

<!-- [1] COLD OPEN
     A specific named scene with real stakes.
     No "this book will...", no throat-clearing.

---

## How to Read It

<!-- TODO: populate from chapter content -->

---

## Signature Simulations

<!-- TODO: populate from chapter content -->

---

## About the Author

**Nik Bear Brown** teaches at Northeastern University and advises early-stage startups in AI, analytics, and machine learning through [Bear Brown & Company](https://www.bearbrown.co/). His MBA from Northeastern and his PhD in Computer Science from UCLA both inform the financial-and-technical hybrid lens this book brings to corporate finance.

He is the founder of [Humanitarians AI](https://www.humanitarians.ai/) and the author of the *with LLMs* textbook series, of which the *with AI* variant for corporate finance is part.

He works in Boston. [nikbearbrown.com](https://www.nikbearbrown.com) · [irreducibly.xyz](https://irreducibly.xyz) · [skepticism.ai](https://www.skepticism.ai)

---

## Copyright

Copyright © 2026 Nik Bear Brown. All rights reserved.

Published by Bear Brown, LLC.

No part of this publication may be reproduced, distributed, or transmitted in
any form or by any means without the prior written permission of the publisher,
except in the case of brief quotations in critical reviews and certain other
noncommercial uses permitted by copyright law.

ISBN: [INSERT ISBN]

First edition: 2026

---

*This README is itself an essai — the current best reading of what the book is and how it works. When chapter drafts reveal that something here is wrong or missing, this file gets updated, and the change gets logged.*
