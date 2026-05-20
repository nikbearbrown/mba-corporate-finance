#!/usr/bin/env python3
"""Pass 2 — generate 9 SVG+PNG figures for corporate-finance-with-ai."""
import re
from pathlib import Path
import cairosvg

ROOT = Path(__file__).parent
CH = ROOT / "chapters"
IMG = ROOT / "images"
IMG.mkdir(exist_ok=True)

INK = "#1a1714"
GRAY_DARK = "#4a4540"
GRAY_MID = "#8a8480"
GRAY_LIGHT = "#c8c4c0"
CREAM = "#f5f2ee"
WHITE = "#fdfcfb"
SERIF = "Georgia, 'Times New Roman', serif"

DEFS = """<defs>
  <marker id="arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
    <polygon points="0 0, 8 3, 0 6" fill="#1a1714"/>
  </marker>
</defs>"""


def open_svg(w, h):
    return [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">', DEFS,
            f'<rect x="0" y="0" width="{w}" height="{h}" fill="{WHITE}"/>']


# Ch 3 fig 01 — three-bucket cash-in-transit diagram
def fig_3_1():
    w, h = 700, 360
    out = open_svg(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Working capital is cash in transit</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Three buckets where cash sits between earning and spending. Each bucket is days of cash held still.</text>')
    buckets = [
        ("ACCOUNTS RECEIVABLE", 60, "Cash promised", "Not yet received", "→ inflow pending"),
        ("INVENTORY", 280, "Cash spent", "Not yet revenue", "→ outflow done"),
        ("ACCOUNTS PAYABLE", 500, "Cash owed", "Not yet paid", "← outflow pending"),
    ]
    for label, x, l1, l2, l3 in buckets:
        out.append(f'<rect x="{x}" y="120" width="160" height="160" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="{x+80}" y="148" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{GRAY_DARK}" text-anchor="middle" letter-spacing="1">{label}</text>')
        out.append(f'<line x1="{x+12}" y1="160" x2="{x+148}" y2="160" stroke="{GRAY_MID}" stroke-width="0.75"/>')
        out.append(f'<text x="{x+80}" y="188" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">{l1}</text>')
        out.append(f'<text x="{x+80}" y="212" font-family="{SERIF}" font-size="11" fill="{GRAY_DARK}" text-anchor="middle">{l2}</text>')
        out.append(f'<text x="{x+80}" y="252" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}" text-anchor="middle">{l3}</text>')
    out.append(f'<text x="{w/2}" y="320" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">CCC = DSO + DIO − DPO. Each lever is a different organizational fight.</text>')
    out.append('</svg>')
    return "\n".join(out)


# Ch 3 fig 02 — cash conversion cycle timeline
def fig_3_2():
    w, h = 700, 360
    h = 360
    out = open_svg(700, h)
    out.append(f'<text x="350" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">The cash conversion cycle as a timeline</text>')
    out.append(f'<text x="350" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">DPO of 35 days shortens net cash exposure to 85 days.</text>')
    axis_y = 200
    out.append(f'<line x1="80" y1="{axis_y}" x2="620" y2="{axis_y}" stroke="{INK}" stroke-width="1.5"/>')
    out.append(f'<path d="M614 {axis_y-4} L622 {axis_y} L614 {axis_y+4} Z" fill="{INK}"/>')
    # Pay materials/labor (day 0)
    out.append(f'<line x1="120" y1="{axis_y-10}" x2="120" y2="{axis_y+10}" stroke="{INK}" stroke-width="1.5"/>')
    out.append(f'<text x="120" y="{axis_y-18}" font-family="{SERIF}" font-size="10" fill="{INK}" text-anchor="middle">Day 0</text>')
    out.append(f'<text x="120" y="{axis_y-32}" font-family="{SERIF}" font-size="10" fill="{INK}" text-anchor="middle">Pay materials</text>')
    # Sale (day 60)
    out.append(f'<line x1="320" y1="{axis_y-10}" x2="320" y2="{axis_y+10}" stroke="{INK}" stroke-width="1.5"/>')
    out.append(f'<text x="320" y="{axis_y-18}" font-family="{SERIF}" font-size="10" fill="{INK}" text-anchor="middle">Day 60</text>')
    out.append(f'<text x="320" y="{axis_y-32}" font-family="{SERIF}" font-size="10" fill="{INK}" text-anchor="middle">Sale</text>')
    # Customer pays (day 120)
    out.append(f'<line x1="520" y1="{axis_y-10}" x2="520" y2="{axis_y+10}" stroke="{INK}" stroke-width="1.5"/>')
    out.append(f'<text x="520" y="{axis_y-18}" font-family="{SERIF}" font-size="10" fill="{INK}" text-anchor="middle">Day 120</text>')
    out.append(f'<text x="520" y="{axis_y-32}" font-family="{SERIF}" font-size="10" fill="{INK}" text-anchor="middle">Customer pays</text>')
    # Brackets
    # DIO 0->60
    out.append(f'<path d="M120 {axis_y+30} L120 {axis_y+50} L320 {axis_y+50} L320 {axis_y+30}" stroke="{INK}" stroke-width="1.5" fill="none"/>')
    out.append(f'<text x="220" y="{axis_y+72}" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">DIO = 60 days</text>')
    # DSO 60->120
    out.append(f'<path d="M320 {axis_y+30} L320 {axis_y+50} L520 {axis_y+50} L520 {axis_y+30}" stroke="{INK}" stroke-width="1.5" fill="none"/>')
    out.append(f'<text x="420" y="{axis_y+72}" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">DSO = 60 days</text>')
    # DPO 0->35 (above)
    out.append(f'<path d="M120 {axis_y-60} L120 {axis_y-80} L237 {axis_y-80} L237 {axis_y-60}" stroke="{INK}" stroke-width="1.5" fill="none" stroke-dasharray="4 3"/>')
    out.append(f'<text x="178" y="{axis_y-92}" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">DPO = 35 days</text>')
    out.append(f'<text x="178" y="{axis_y-106}" font-family="{SERIF}" font-size="9" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">(supplier credit)</text>')
    # Net exposure summary
    out.append(f'<text x="350" y="320" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">CCC = 60 + 60 − 35 = <tspan font-weight="bold">85 days</tspan> of net cash exposure</text>')
    out.append('</svg>')
    return "\n".join(out)


# Ch 3 fig 03 — org chart cross-functional tensions
def fig_3_3():
    w, h = 700, 420
    out = open_svg(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Working-capital levers cross organizational lines</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Each CCC component lives in a different function. Improvement is a cross-functional negotiation.</text>')
    cy = 220
    nodes = [
        ("DSO", 130, ["Sales", "Finance / Credit"]),
        ("DIO", 350, ["Operations", "Supply Chain"]),
        ("DPO", 570, ["Procurement", "Treasury"]),
    ]
    for label, cx, owners in nodes:
        out.append(f'<rect x="{cx-60}" y="{cy-32}" width="120" height="64" fill="{INK}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="{cx}" y="{cy+5}" font-family="{SERIF}" font-size="20" font-weight="bold" fill="{WHITE}" text-anchor="middle">{label}</text>')
        for i, o in enumerate(owners):
            out.append(f'<rect x="{cx-72}" y="{cy+60+i*36}" width="144" height="28" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
            out.append(f'<text x="{cx}" y="{cy+78+i*36}" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">{o}</text>')
            out.append(f'<line x1="{cx}" y1="{cy+32}" x2="{cx}" y2="{cy+60+i*36}" stroke="{GRAY_MID}" stroke-width="0.75" stroke-dasharray="3 3"/>' if i == 0 else '')
    # Cross-tension arrows
    for x1, x2, label in [(190, 290, "tighter terms vs. revenue"), (410, 510, "AP push vs. supplier risk")]:
        out.append(f'<path d="M{x1} {cy} L{x2} {cy}" stroke="{INK}" stroke-width="1" fill="none" stroke-dasharray="6 4" marker-end="url(#arrow)"/>')
        out.append(f'<text x="{(x1+x2)/2}" y="{cy-8}" font-family="{SERIF}" font-size="9" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">{label}</text>')
    out.append(f'<text x="{w/2}" y="394" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">The arithmetic is one cell in a spreadsheet. The execution is a cross-functional negotiation.</text>')
    out.append('</svg>')
    return "\n".join(out)


# Ch 5 fig 01 — discount-rate decision tree
def fig_5_1():
    w, h = 700, 480
    out = open_svg(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Choosing the right discount rate for a project</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Two questions, three outcomes. Most projects belong on the *use firm WACC* branch, but only after the questions have been asked.</text>')

    # Root
    out.append(f'<rect x="248" y="84" width="204" height="48" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="350" y="106" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">Project risk matches</text>')
    out.append(f'<text x="350" y="122" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">firm average?</text>')
    # Yes branch
    out.append(f'<path d="M260 132 L120 192" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<text x="178" y="170" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}">YES</text>')
    out.append(f'<rect x="40" y="192" width="200" height="48" fill="{INK}" stroke="{INK}"/>')
    out.append(f'<text x="140" y="214" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{WHITE}" text-anchor="middle">Use firm WACC</text>')
    out.append(f'<text x="140" y="230" font-family="{SERIF}" font-size="10" fill="{GRAY_LIGHT}" text-anchor="middle">(8.0% for Halverson)</text>')

    # No branch
    out.append(f'<path d="M440 132 L500 192" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<text x="475" y="170" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}">NO</text>')
    # Second question
    out.append(f'<rect x="408" y="192" width="240" height="48" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="528" y="214" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">Identifiable comparable</text>')
    out.append(f'<text x="528" y="230" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">firms exist?</text>')
    # Yes -> project beta
    out.append(f'<path d="M428 240 L300 308" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<text x="358" y="282" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}">YES</text>')
    out.append(f'<rect x="200" y="308" width="200" height="64" fill="{INK}" stroke="{INK}"/>')
    out.append(f'<text x="300" y="332" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{WHITE}" text-anchor="middle">Estimate project beta</text>')
    out.append(f'<text x="300" y="348" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{WHITE}" text-anchor="middle">from comps; build</text>')
    out.append(f'<text x="300" y="364" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{WHITE}" text-anchor="middle">project WACC</text>')
    # No -> management uplift
    out.append(f'<path d="M620 240 L620 308" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<text x="640" y="280" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}">NO</text>')
    out.append(f'<rect x="500" y="308" width="200" height="64" fill="{INK}" stroke="{INK}"/>')
    out.append(f'<text x="600" y="332" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{WHITE}" text-anchor="middle">Apply management</text>')
    out.append(f'<text x="600" y="348" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{WHITE}" text-anchor="middle">uplift (+200–300 bp)</text>')
    out.append(f'<text x="600" y="364" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{WHITE}" text-anchor="middle">over firm WACC</text>')
    out.append(f'<text x="{w/2}" y="416" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">The default is the firm WACC. The exceptions are where the FP&amp;A team has to defend a different number.</text>')
    out.append('</svg>')
    return "\n".join(out)


# Ch 6 fig 01 — unlevering / relevering beta diagram
def fig_6_1():
    w, h = 700, 420
    out = open_svg(700, h)
    out.append(f'<text x="350" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Same operations, different leverage, different equity beta</text>')
    out.append(f'<text x="350" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Unlever each firm to recover the asset beta — then relever to your project&#8217;s target structure.</text>')
    # Two firm boxes
    panels = [
        ("FIRM A — 20% debt", 56, "Lower equity β: 1.0", "Less leverage amplification"),
        ("FIRM B — 50% debt", 372, "Higher equity β: 1.5", "More leverage amplification"),
    ]
    for title, x, b1, b2 in panels:
        out.append(f'<rect x="{x}" y="80" width="272" height="100" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="{x+136}" y="106" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{GRAY_DARK}" text-anchor="middle" letter-spacing="1.2">{title}</text>')
        out.append(f'<text x="{x+136}" y="138" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">{b1}</text>')
        out.append(f'<text x="{x+136}" y="160" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">{b2}</text>')
    # Arrows down
    out.append(f'<path d="M192 180 Q192 230 280 230" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<path d="M508 180 Q508 230 420 230" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<text x="190" y="215" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}" text-anchor="end">unlever</text>')
    out.append(f'<text x="510" y="215" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}">unlever</text>')
    # Center: asset beta
    out.append(f'<rect x="280" y="220" width="140" height="60" fill="{INK}" stroke="{INK}"/>')
    out.append(f'<text x="350" y="244" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{WHITE}" text-anchor="middle">Asset β (shared)</text>')
    out.append(f'<text x="350" y="264" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{WHITE}" text-anchor="middle">≈ 0.85</text>')
    # Arrow down to relever
    out.append(f'<path d="M350 280 L350 320" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<text x="360" y="306" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}">relever to target</text>')
    out.append(f'<rect x="200" y="320" width="300" height="48" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="350" y="344" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">Project β at your target capital structure</text>')
    out.append(f'<text x="350" y="360" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">→ project-specific WACC</text>')
    out.append(f'<text x="350" y="404" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">$\\beta_\\text{{asset}} = \\beta_\\text{{equity}} / [1 + (1-T_c)(D/E)]$ — Hamada equation</text>')
    out.append('</svg>')
    return "\n".join(out)


# Ch 6 fig 02 — Plant 4 decision tree (defer option)
def fig_6_2():
    w, h = 700, 480
    out = open_svg(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Plant 4 — commit now or wait six months</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">The deferral option resolves Q2 demand uncertainty before the $50M is committed. Probabilities are placeholders.</text>')

    # Root (square = decision)
    out.append(f'<rect x="60" y="220" width="100" height="60" fill="{CREAM}" stroke="{INK}" stroke-width="2"/>')
    out.append(f'<text x="110" y="246" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">Today</text>')
    out.append(f'<text x="110" y="262" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}" text-anchor="middle">commit / wait?</text>')

    # Commit branch (top)
    out.append(f'<path d="M160 240 L290 140" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<text x="220" y="180" font-family="{SERIF}" font-size="10" fill="{INK}" text-anchor="middle">commit now</text>')
    out.append(f'<rect x="290" y="124" width="160" height="40" fill="{INK}" stroke="{INK}"/>')
    out.append(f'<text x="370" y="148" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{WHITE}" text-anchor="middle">NPV = +$25M</text>')

    # Wait branch (bottom)
    out.append(f'<path d="M160 260 L290 360" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<text x="220" y="320" font-family="{SERIF}" font-size="10" fill="{INK}" text-anchor="middle">wait 6 months</text>')

    # Chance node (circle)
    out.append(f'<circle cx="350" cy="380" r="34" fill="{CREAM}" stroke="{INK}" stroke-width="2"/>')
    out.append(f'<text x="350" y="376" font-family="{SERIF}" font-size="10" fill="{INK}" text-anchor="middle">Q2 demand</text>')
    out.append(f'<text x="350" y="390" font-family="{SERIF}" font-size="10" fill="{INK}" text-anchor="middle">data arrives</text>')

    # Strong / weak branches
    # Strong (up-right)
    out.append(f'<path d="M384 360 L500 280" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<text x="430" y="310" font-family="{SERIF}" font-size="10" fill="{INK}">strong (p=0.5)</text>')
    out.append(f'<rect x="500" y="252" width="170" height="56" fill="{INK}" stroke="{INK}"/>')
    out.append(f'<text x="585" y="276" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{WHITE}" text-anchor="middle">commit, NPV = +$80M</text>')
    out.append(f'<text x="585" y="294" font-family="{SERIF}" font-size="10" fill="{GRAY_LIGHT}" text-anchor="middle">net of 6-mo deferral cost</text>')

    # Weak (down-right)
    out.append(f'<path d="M384 400 L500 440" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<text x="430" y="440" font-family="{SERIF}" font-size="10" fill="{INK}">weak (p=0.5)</text>')
    out.append(f'<rect x="500" y="436" width="170" height="32" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="585" y="456" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">abandon, NPV = $0</text>')

    out.append(f'<text x="60" y="84" font-family="{SERIF}" font-size="11" font-style="italic" fill="{INK}">Wait branch EV = 0.5 × $80M + 0.5 × $0 = $40M</text>')
    out.append(f'<text x="60" y="100" font-family="{SERIF}" font-size="11" font-style="italic" fill="{INK}">Option value = $40M − $25M = $15M</text>')
    out.append('</svg>')
    return "\n".join(out)


# Ch 12 fig 01 — three imperfections panels
def fig_12_1():
    w, h = 700, 420
    out = open_svg(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Three frictions that make hedging valuable</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">In a frictionless world, shareholders hedge themselves and corporate hedging is irrelevant. These frictions break that.</text>')

    # Panel 1 — distress costs (nonlinear)
    out.append(f'<rect x="56" y="80" width="200" height="280" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="156" y="104" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{GRAY_DARK}" text-anchor="middle" letter-spacing="1">DISTRESS COSTS</text>')
    # nonlinear cost curve
    out.append(f'<line x1="76" y1="320" x2="236" y2="320" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<line x1="76" y1="320" x2="76" y2="140" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<path d="M76 320 Q160 314 180 290 Q200 240 236 140" stroke="{INK}" stroke-width="2" fill="none"/>')
    out.append(f'<line x1="190" y1="320" x2="190" y2="140" stroke="{GRAY_LIGHT}" stroke-width="0.75" stroke-dasharray="3 3"/>')
    out.append(f'<text x="190" y="338" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}" text-anchor="middle">threshold</text>')
    out.append(f'<text x="156" y="356" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}" text-anchor="middle">Costs explode past a leverage threshold</text>')

    # Panel 2 — tax convexity
    out.append(f'<rect x="276" y="80" width="200" height="280" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="376" y="104" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{GRAY_DARK}" text-anchor="middle" letter-spacing="1">TAX CONVEXITY</text>')
    # Two bars, volatile vs smooth
    out.append(f'<rect x="304" y="200" width="40" height="120" fill="{INK}"/>')
    out.append(f'<text x="324" y="338" font-family="{SERIF}" font-size="10" fill="{INK}" text-anchor="middle">volatile</text>')
    out.append(f'<text x="324" y="354" font-family="{SERIF}" font-size="9" fill="{GRAY_DARK}" text-anchor="middle">tax = $24M</text>')
    out.append(f'<rect x="404" y="220" width="40" height="100" fill="{GRAY_MID}"/>')
    out.append(f'<text x="424" y="338" font-family="{SERIF}" font-size="10" fill="{INK}" text-anchor="middle">smooth</text>')
    out.append(f'<text x="424" y="354" font-family="{SERIF}" font-size="9" fill="{GRAY_DARK}" text-anchor="middle">tax = $20M</text>')
    out.append(f'<text x="376" y="178" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}" text-anchor="middle">Same expected income,</text>')
    out.append(f'<text x="376" y="192" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}" text-anchor="middle">higher tax under volatility</text>')

    # Panel 3 — investment pipeline
    out.append(f'<rect x="496" y="80" width="200" height="280" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="596" y="104" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{GRAY_DARK}" text-anchor="middle" letter-spacing="1">INVESTMENT PIPELINE</text>')
    out.append(f'<path d="M520 280 L660 280" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<text x="540" y="270" font-family="{SERIF}" font-size="10" fill="{INK}" text-anchor="middle">capex</text>')
    # Cash shortfall cuts off the arrow
    out.append(f'<line x1="600" y1="240" x2="600" y2="320" stroke="{INK}" stroke-width="2" stroke-dasharray="3 3"/>')
    out.append(f'<text x="608" y="200" font-family="{SERIF}" font-size="10" fill="{INK}">cash shortfall</text>')
    out.append(f'<text x="608" y="214" font-family="{SERIF}" font-size="10" fill="{INK}">cuts off project</text>')
    out.append(f'<text x="596" y="356" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}" text-anchor="middle">Hedging preserves the pipeline</text>')

    out.append(f'<text x="{w/2}" y="394" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">All three frictions create a real reason for the firm to hedge — beyond what the shareholders could replicate.</text>')
    out.append('</svg>')
    return "\n".join(out)


# Ch 12 fig 02 — transaction vs translation exposure
def fig_12_2():
    w, h = 700, 420
    out = open_svg(700, h)
    out.append(f'<text x="350" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Transaction vs. translation FX exposure</text>')
    out.append(f'<text x="350" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Transaction is cash. Translation is accounting.</text>')

    # Transaction column
    out.append(f'<rect x="56" y="80" width="280" height="280" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="196" y="104" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{GRAY_DARK}" text-anchor="middle" letter-spacing="1.2">TRANSACTION EXPOSURE</text>')
    out.append(f'<text x="76" y="140" font-family="{SERIF}" font-size="11" fill="{INK}">£5M contract receipt — Day 0</text>')
    out.append(f'<line x1="76" y1="190" x2="316" y2="190" stroke="{INK}" stroke-width="1.5"/>')
    out.append(f'<line x1="76" y1="184" x2="76" y2="196" stroke="{INK}" stroke-width="1.5"/>')
    out.append(f'<line x1="316" y1="184" x2="316" y2="196" stroke="{INK}" stroke-width="1.5"/>')
    out.append(f'<text x="196" y="180" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}" text-anchor="middle">90 days</text>')
    out.append(f'<text x="76" y="216" font-family="{SERIF}" font-size="10" fill="{INK}">Day 90 — receive £5M</text>')
    out.append(f'<text x="316" y="216" font-family="{SERIF}" font-size="10" fill="{INK}" text-anchor="end">Convert to USD at spot</text>')
    out.append(f'<text x="76" y="252" font-family="{SERIF}" font-size="11" fill="{INK}">Forward contract neutralizes:</text>')
    out.append(f'<text x="76" y="270" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}">Sell £5M forward at Day 0 forward rate.</text>')
    out.append(f'<text x="76" y="286" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}">USD equivalent locked in regardless of spot.</text>')
    out.append(f'<text x="196" y="332" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">Cash-real. Hedgeable. HEDGE.</text>')

    # Translation column
    out.append(f'<rect x="364" y="80" width="280" height="280" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="504" y="104" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{GRAY_DARK}" text-anchor="middle" letter-spacing="1.2">TRANSLATION EXPOSURE</text>')
    out.append(f'<text x="384" y="140" font-family="{SERIF}" font-size="11" fill="{INK}">UK subsidiary: £40M net assets</text>')
    out.append(f'<text x="384" y="160" font-family="{SERIF}" font-size="11" fill="{INK}">on the consolidated balance sheet</text>')
    out.append(f'<line x1="384" y1="190" x2="624" y2="190" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="384" y="216" font-family="{SERIF}" font-size="11" fill="{INK}">GBP/USD moves down 10%</text>')
    out.append(f'<text x="384" y="236" font-family="{SERIF}" font-size="11" fill="{INK}">Reported book value drops</text>')
    out.append(f'<text x="384" y="256" font-family="{SERIF}" font-size="11" fill="{INK}">No actual cash moves</text>')
    out.append(f'<text x="384" y="288" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}">A hedge would create a real cash cost</text>')
    out.append(f'<text x="384" y="304" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}">to manage an accounting outcome.</text>')
    out.append(f'<text x="504" y="332" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">Accounting only. DO NOT HEDGE.</text>')
    out.append('</svg>')
    return "\n".join(out)


# Ch 15 fig 01 — four-quadrant interdependence
def fig_15_1():
    w, h = 700, 480
    out = open_svg(700, h)
    out.append(f'<text x="350" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">The four interdependent CFO decisions</text>')
    out.append(f'<text x="350" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Each decision constrains the other three. The capstone holds them all in tension at once.</text>')

    # Four quadrants
    quads = [
        ("CAPITAL ALLOCATION", "Plant 4 + Cardinal + WC", 130, 170),
        ("CAPITAL STRUCTURE", "Target debt-to-capital", 530, 170),
        ("PAYOUT POLICY", "Dividend + buyback", 130, 360),
        ("RISK POSITION", "Retain vs. transfer", 530, 360),
    ]
    for title, sub, cx, cy in quads:
        out.append(f'<rect x="{cx-100}" y="{cy-44}" width="200" height="88" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="{cx}" y="{cy-16}" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">{title}</text>')
        out.append(f'<text x="{cx}" y="{cy+8}" font-family="{SERIF}" font-size="11" fill="{GRAY_DARK}" text-anchor="middle">{sub}</text>')

    # Bidirectional arrows with labels
    edges = [
        # alloc <-> structure
        (230, 170, 430, 170, "allocation consumes debt capacity", -16),
        (230, 178, 430, 178, "structure limits projects", 18),
        # alloc <-> payout
        (130, 214, 130, 316, "allocation reduces payout dollars", -8, "vert"),
        # structure <-> risk
        (530, 214, 530, 316, "structure shapes risk capacity", -8, "vert"),
        # payout <-> risk
        (230, 360, 430, 360, "payout drains the risk-capital buffer", -16),
        (230, 368, 430, 368, "risk position constrains payout", 18),
        # diagonal alloc<->risk
        (200, 220, 460, 320, "risk forecasts feed allocation", 0, "diag"),
        # diagonal structure<->payout
        (460, 220, 200, 320, "structure caps total return", 0, "diag"),
    ]
    # Draw simple two-way arrows
    out.append(f'<path d="M230 174 L430 174" stroke="{INK}" stroke-width="1.2" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<path d="M430 178 L230 178" stroke="{INK}" stroke-width="1.2" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<text x="330" y="158" font-family="{SERIF}" font-size="9" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">consumes / limits</text>')

    out.append(f'<path d="M126 214 L126 316" stroke="{INK}" stroke-width="1.2" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<path d="M134 316 L134 214" stroke="{INK}" stroke-width="1.2" fill="none" marker-end="url(#arrow)"/>')

    out.append(f'<path d="M526 214 L526 316" stroke="{INK}" stroke-width="1.2" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<path d="M534 316 L534 214" stroke="{INK}" stroke-width="1.2" fill="none" marker-end="url(#arrow)"/>')

    out.append(f'<path d="M230 356 L430 356" stroke="{INK}" stroke-width="1.2" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<path d="M430 360 L230 360" stroke="{INK}" stroke-width="1.2" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<text x="330" y="346" font-family="{SERIF}" font-size="9" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">drains buffer / constrains</text>')

    # Diagonals (dashed)
    out.append(f'<path d="M210 220 L450 320" stroke="{INK}" stroke-width="1" fill="none" stroke-dasharray="4 3" marker-end="url(#arrow)"/>')
    out.append(f'<path d="M450 220 L210 320" stroke="{INK}" stroke-width="1" fill="none" stroke-dasharray="4 3" marker-end="url(#arrow)"/>')

    out.append(f'<text x="350" y="448" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">A memo that treats the four as separate is not yet integrated. The board catches the gaps.</text>')
    out.append('</svg>')
    return "\n".join(out)


FIGURES = [
    ("03-working-capital-is-where-the-cash-lives-fig-01", fig_3_1(),
     "Three-bucket diagram showing cash in transit through accounts receivable, inventory, and accounts payable",
     "Figure 3.1 — Working capital is cash in transit",
     "03-working-capital-is-where-the-cash-lives.md", "Three-bucket diagram"),
    ("03-working-capital-is-where-the-cash-lives-fig-02", fig_3_2(),
     "Cash conversion cycle as a horizontal timeline showing DSO, DIO, and DPO with a net 85-day exposure",
     "Figure 3.2 — The cash conversion cycle",
     "03-working-capital-is-where-the-cash-lives.md", "Horizontal timeline"),
    ("03-working-capital-is-where-the-cash-lives-fig-03", fig_3_3(),
     "Org-chart diagram mapping each CCC component to the business functions that own it, with cross-functional tension points",
     "Figure 3.3 — CCC as a cross-functional negotiation",
     "03-working-capital-is-where-the-cash-lives.md", "Org chart showing CCC components"),
    ("05-the-cost-of-capital-and-the-wacc-fig-01", fig_5_1(),
     "Decision tree for choosing the right discount rate: firm WACC, comparable-firm-derived project WACC, or management uplift",
     "Figure 5.1 — Choosing the right discount rate",
     "05-the-cost-of-capital-and-the-wacc.md", "decision tree for choosing the right discount rate"),
    ("06-risk-adjusted-rates-and-real-options-fig-01", fig_6_1(),
     "Two-firm leverage diagram showing the unlever-to-asset-beta-then-relever-to-target procedure for project beta",
     "Figure 6.1 — Unlevering and relevering project beta",
     "06-risk-adjusted-rates-and-real-options.md", "Side-by-side diagram of two identical firms"),
    ("06-risk-adjusted-rates-and-real-options-fig-02", fig_6_2(),
     "Decision tree for the Plant 4 deferral option, showing commit-now vs. wait-six-months with strong/weak demand branches",
     "Figure 6.2 — The Plant 4 deferral option",
     "06-risk-adjusted-rates-and-real-options.md", "Decision tree for Plant 4"),
    ("12-operational-risk-management-fig-01", fig_12_1(),
     "Three-panel diagram of the frictions that justify hedging: distress costs, tax convexity, and investment-pipeline preservation",
     "Figure 12.1 — Three frictions that make hedging valuable",
     "12-operational-risk-management.md", "Three-panel diagram showing the three imperfections"),
    ("12-operational-risk-management-fig-02", fig_12_2(),
     "Two-column diagram contrasting transaction FX exposure (cash-real, hedgeable) with translation FX exposure (accounting-only)",
     "Figure 12.2 — Transaction vs. translation FX exposure",
     "12-operational-risk-management.md", "Two-column diagram distinguishing transaction exposure from translation exposure"),
    ("15-the-capstone-an-integrated-cfo-recommendation-fig-01", fig_15_1(),
     "Four-quadrant diagram of the four interdependent CFO decisions — capital allocation, capital structure, payout policy, risk position — with bidirectional arrows showing how each constrains the others",
     "Figure 15.1 — The four interdependent CFO decisions",
     "15-the-capstone-an-integrated-cfo-recommendation.md", "Four-quadrant diagram"),
]


def write_pair(slug, svg_str):
    svg_path = IMG / f"{slug}.svg"
    png_path = IMG / f"{slug}.png"
    svg_path.write_text(svg_str)
    m = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg_str)
    vw, vh = int(m.group(1)), int(m.group(2))
    cairosvg.svg2png(bytestring=svg_str.encode('utf-8'),
                      output_width=vw*2, output_height=vh*2,
                      write_to=str(png_path))


def replace_in_chapter(ch_file, comment_key, slug, alt, title):
    path = CH / ch_file
    text = path.read_text()
    pat = re.compile(
        r'<!--\s*→\s*\[(?:IMAGE|FIGURE|DIAGRAM):.*?'
        + re.escape(comment_key)
        + r'.*?-->',
        re.DOTALL,
    )
    m = pat.search(text)
    if not m:
        print(f"!!! NO MATCH: {ch_file} | {comment_key!r}")
        return
    new_md = f"![{alt}](images/{slug}.png)\n*{title}*"
    new_text = text[:m.start()] + new_md + text[m.end():]
    path.write_text(new_text)
    print(f"  [{ch_file}] {comment_key[:40]} → {slug}.png")


def main():
    print("=== generating SVG/PNG ===")
    for slug, svg, *_ in FIGURES:
        write_pair(slug, svg)
    print("\n=== replacing in chapter files ===")
    for slug, _, alt, title, ch_file, comment_key in FIGURES:
        replace_in_chapter(ch_file, comment_key, slug, alt, title)


if __name__ == "__main__":
    main()
