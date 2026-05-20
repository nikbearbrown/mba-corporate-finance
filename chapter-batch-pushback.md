# Pushback: I'm not drafting these chapters yet

You asked me to draft rough drafts for every chapter, follow the "new TOC" you pasted, use the attached as reference. Three problems make this the wrong move right now. Calling them out before I waste a 50,000-word draft.

## Problem 1: The "new TOC" you pasted contradicts the /l3 you just locked

The /l3 you saved twenty minutes ago locks a **15-chapter, three-act arc** for *Corporate Finance with AI*:

- Act 1 (Ch 1-3): Read the Firm
- Act 2 (Ch 4-8): Allocate Capital — including the Ch 7-8 paired pivot
- Act 3 (Ch 9-15): Distribute and Execute

The TOC you just pasted is **33 chapters** for a different book — *Corporate Finance with Excel, Python, and LLMs* — with a totally different structure: nine parts, chapters on Time Value of Money, Yield Curves, Bond Pricing, ML in Corporate Finance, NLP for Earnings Calls, etc. That's the old Berk-DeMarzo-style sequence, not the three-act CFO-recommendation arc.

These cannot both be the active outline. Which is it?

If the answer is "the new TOC supersedes the /l3," then the /l3 work was throwaway and I need to know that explicitly — `corporate-finance-with-ai/l3-arc.md` should be marked obsolete.

If the answer is "the /l3 is the real outline and I pasted the wrong reference," then I'm drafting 15 chapters under the three-act arc and ignoring the 33-chapter TOC entirely.

If the answer is "use the 33-chapter TOC's content but the /l3's structure," that's not a drafting job — that's a remapping job that has to happen before any chapter gets written, because half the 33-chapter topics don't fit cleanly into 15 act-defined slots.

## Problem 2: The reference material violates almost every CLAUDE.md hard rule

The reference chapters you pasted are exactly the kind of writing CLAUDE.md was written to prevent. Specifically:

- **Excel VBA dumps as pedagogy.** Chapter 1's reference is roughly 60% VBA macros for charting. CLAUDE.md and the /l3 explicitly say "at no point does the book retreat into Excel-based pedagogy." The attached reference is mostly Excel pedagogy.
- **No hooks, no specifications, no mechanism deep-dives.** The reference Ch 1 opens with "A corporation is a legal entity that exists separately from its owners." That's a textbook definition, not a Feynman opener. Every section is bullet-list definitions followed by code. No puzzle, no scene, no specification of what's being argued.
- **Forbidden phrases throughout.** "Stakeholders" used as the noun for people. "Robust" and "scalable" used without explanation. "Obviously" appears. The triangulation section in the Introduction makes the jaw-dropping unjustified assumption that "each LLM has an independent 90% accuracy rate" — that's not a heuristic, it's a probability calculation built on a fabricated premise the chapter never defends.
- **Generic LLM prompt templates instead of actual analysis.** Every section ends with a "Prompt for [X] analysis" that the student is supposed to paste verbatim. The /mega skill exists precisely so chapters don't do this — exercises live in their own file, with strategic context about *when* to compare LLMs vs use one. The reference smushes everything into one bloated chapter.
- **No primary sources.** The reference chapters cite no papers, no filings, no model cards. CLAUDE.md hard rule #2: primary sources where possible. Hard rule #3: every contestable factual claim carries a link.
- **The "Maya at the CFO's office" frame from /l3 doesn't appear once.** The reference is faceless textbook prose. The whole pedagogical innovation of Book 2 — the inside-the-firm CFO seat — is absent.

If I use this as reference, I produce content that would fail the workshop's own review on first pass.

## Problem 3: Drafting 15 (or 33) chapters in one go is the wrong unit of work anyway

Even if the TOC and reference were right, the /l3 you locked says four chapters consume 30-40% of writing effort:

- **Ch 1** — onboarding load (how does Maya get oriented? does the Book 1 returnee skip 30% of it? this is an unsolved structural problem your /l3 admits)
- **Ch 7 + Ch 8** — must be written together as a paired unit
- **Ch 15** — capstone synthesis

Drafting these four properly is two-to-three weeks of real work each if the standard is "publishable in a Northeastern MBA core." Drafting them as a batch in one shot guarantees Ch 1 doesn't get the onboarding-design attention it needs, the Ch 7-8 pair gets sequential not paired treatment, and Ch 15 is the throwaway it always becomes when you batch-write.

The other 11 chapters are also not equal — Ch 14 (Behavioral) has a known structural risk the /l3 admits and doesn't solve. Drafting it before resolving "is Ch 14 standalone or distributed through Acts 2-3" produces a chapter you'll throw out.

## What I'd do instead — three options

**Option A (cleanest): one chapter at a time, in order of load-bearing weight.** Start with Ch 1. Get the Maya CFO scene right. Get the verification-discipline thread right. Get the "works for both Book 1 returnees and fresh starters" mechanism right. That single chapter sets every voice and structural choice for the other 14. Once it's reviewed and you're happy, move to Ch 7-8 as a pair. Then Ch 15. Then fill in the Act 1 remainder, then Act 2 middle, then Act 3 sub-arcs.

**Option B (faster, lower quality): outline first, draft second.** I produce 15 *outlines* (one per chapter), each ~500 words, hitting the four moves with the hook scene specified, the mechanism named, the analogy chosen, the deep-dive identified. You review the outlines as a batch. Then I draft the actual chapters one at a time. This catches structural problems before they get embedded in 60,000 words of prose.

**Option C (if you really want batch drafting): pick three pilot chapters across the three acts.** Ch 1, Ch 7, Ch 12 maybe. Draft those. Review. Decide whether the voice and structure work before committing to the other 12.

**What I won't do:** silently produce 15 or 33 chapters that copy the structure of the reference material, because the reference material is the antithesis of what the workshop is for. That's not pushback for its own sake — it's the workshop's own /chapter skill telling me to flag, not pad.

## What I need from you

1. **Which TOC is active** — the locked /l3 fifteen-chapter arc, or the 33-chapter Excel/Python/LLMs sequence? They are not compatible.
2. **Is the Excel/Python/LLMs reference the voice you want, or the voice the workshop is meant to replace?** CLAUDE.md says replace. The reference says keep. One of those wins.
3. **A or B or C** — and which chapter(s) first?

Once those three answers land, I draft. Until then, I'd be producing throwaway work.
