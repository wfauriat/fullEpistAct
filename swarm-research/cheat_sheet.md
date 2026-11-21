# 5-Minute Plain-Language Cheat Sheet

**What tonight's whole research pass boils down to—in plain language, with zero homework attached.**

---

### 1. The Core Problem in One Sentence
Formal math, statistical confidence intervals, and AI fluency all check **how consistent a system is inside its own frame**—yet catastrophic failures happen from **what the frame leaves out**, **what errors get shared across producer and checker**, and **what happens when fluent output lulls humans into rubber-stamping**.

---

### 2. Four Things That Are Solidly Established
1. **Internal checks cannot catch missing variables.** If a factor stayed constant during training/testing (or wasn't in the model's inputs), re-running the same model, tightening error bars, or writing a Lean proof will never see it.
2. **"Independent" checks usually fail together.** Even without talking to each other, two reviewers or two AI models share blind spots whenever tasks vary in difficulty or share training data. Only checks that fail via a **genuinely different mechanism** (e.g., unit/compiler checks, physical experiments, unanchored humans) break that correlation.
3. **When stakes are huge and one-shot, statistics stops working.** If a mistake costs $10{,}000\times$ the upside, you need failure probability below $0.01\%$—too rare to verify from finite samples. Worse, tuning alarms to catch rare errors floods operators with false alarms until they start ignoring them.
4. **AI fluency quietly breaks human oversight.** Smooth text hides uncertainty, makes people *feel* 20% faster even when they slow down (METR 2025), and erodes hands-on vigilance over time unless friction is deliberately preserved where stakes are high.

---

### 3. Four Places Where the Picture Is More Nuanced Than "AI Bad"
1. **Iterative AI checking *does* work on messy reasoning inside the frame** (test-time compute, process reward models, grounded debate)—just not on unmodeled outside-the-frame risks or without external ground truth.
2. **Human + AI speedups are real on greenfield/junior tasks**, even though they reverse on mature, invariant-heavy codebases and complex clinical decisions.
3. **Shared foundation models often reduce *average* daily errors** even when they share blind spots—the danger is concentrated in **rare, correlated tail events** and **live web/RAG contamination**, not necessarily routine work.
4. **Heavy-handed human checklists backfire.** If you force slow cognitive friction everywhere, people get frustrated and route around your guardrails (*Shadow AI*). Friction only survives in real organizations if it is **saved for high-uncertainty or irreversible commits**.

---

### 4. Where Your Monograph (`livre.html`) Stands
Your book already got the **architecture, distinctions, and intellectual honesty** right (and its self-audit Conclusion is stronger than almost anything in the literature). It mainly just needs:
* a few **2021–2025 empirical anchors** (so Parts III–V don't lean on 2 studies),
* the **4 nuances above** (especially Gerstgrasser on collapse and risk-tiered friction vs. clutter), and
* **small visual/runnable entry doors** (like `explorer.html` or the upcoming Track 2 simulator) so peers can *feel* the dynamics in 2 minutes instead of climbing a 277-page mountain first.
