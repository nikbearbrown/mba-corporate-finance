#!/usr/bin/env python3
"""Insert portrait stubs into all 15 Wayback Machine sections."""
import re
from pathlib import Path

ROOT = Path(__file__).parent
CH = ROOT / "chapters"

SUBJECTS = [
    ("01-the-cfos-first-question.md",                                            "Donaldson Brown",     "c. 1920s",  "photograph", "portrait", "donaldson-brown.jpg"),
    ("02-reading-the-firm-from-inside.md",                                       "Mary Harris Smith",   "c. 1920",   "photograph", "portrait", "mary-harris-smith.jpg"),
    ("03-working-capital-is-where-the-cash-lives.md",                            "John Hicks",          "c. 1940s",  "photograph", "portrait", "john-hicks.jpg"),
    ("04-capital-budgeting-at-the-firm-level.md",                                "Joel Dean",           "c. 1950s",  "photograph", "portrait", "joel-dean.jpg"),
    ("05-the-cost-of-capital-and-the-wacc.md",                                   "Fischer Black",       "c. 1980s",  "photograph", "portrait", "fischer-black.jpg"),
    ("06-risk-adjusted-rates-and-real-options.md",                               "Irving Fisher",       "c. 1920s",  "photograph", "portrait", "irving-fisher.jpg"),
    ("07-capital-structure-theory-the-modigliani-miller-world.md",               "Merton Miller",       "c. 1990",   "photograph", "portrait", "merton-miller.jpg"),
    ("08-capital-structure-in-the-real-world.md",                                "Adolf A. Berle",      "c. 1940s",  "photograph", "portrait", "adolf-a-berle.jpg"),
    ("09-returning-capital-dividends-buybacks-and-the-choice-between-them.md",   "Gardiner C. Means",   "c. 1940s",  "photograph", "portrait", "gardiner-c-means.jpg"),
    ("10-raising-capital-ipos-secondaries-and-the-cost-of-going-to-market.md",   "Maggie Lena Walker",  "c. 1910",   "photograph", "portrait", "maggie-lena-walker.jpg"),
    ("11-m-and-a-the-largest-decisions-a-cfo-makes.md",                          "Edith Penrose",       "c. 1960s",  "photograph", "portrait", "edith-penrose.jpg"),
    ("12-operational-risk-management.md",                                        "Karl Borch",          "c. 1970s",  "photograph", "portrait", "karl-borch.jpg"),
    ("13-international-corporate-finance.md",                                    "Susan Strange",       "c. 1980s",  "photograph", "portrait", "susan-strange.jpg"),
    ("14-behavioral-corporate-finance.md",                                       "Daniel Bernoulli",    "c. 1750",   "engraving",  "portrait", "daniel-bernoulli.jpg"),
    ("15-the-capstone-an-integrated-cfo-recommendation.md",                      "Joseph Schumpeter",   "c. 1940s",  "photograph", "portrait", "joseph-schumpeter.jpg"),
]


def insert_stub(filename, name, era, src_type, img_type, jpg_filename):
    path = CH / filename
    text = path.read_text()
    header_idx = text.find("## AI Wayback Machine")
    if header_idx == -1:
        print(f"!!! no Wayback in {filename}")
        return False
    run_idx = text.find("**Run this:**", header_idx)
    if run_idx == -1:
        print(f"!!! no Run-this in {filename}")
        return False
    section_text = text[header_idx:run_idx]
    if re.search(r'!\[' + re.escape(name), section_text):
        print(f"  SKIP (stub already): {filename}")
        return False
    stub = (
        f"![{name}, {era}. AI-generated {img_type} based on a public domain {src_type} (Wikimedia Commons).]"
        f"(images/{jpg_filename})\n"
        f"*{name}, {era}. AI-generated {img_type} based on a public domain {src_type}.*\n\n"
    )
    before = text[:run_idx].rstrip() + "\n\n" + stub
    after = text[run_idx:]
    path.write_text(before + after)
    print(f"  inserted stub for {name} in {filename}")
    return True


def main():
    n = 0
    for entry in SUBJECTS:
        if insert_stub(*entry): n += 1
    print(f"\ntotal: {n}")


if __name__ == "__main__":
    main()
