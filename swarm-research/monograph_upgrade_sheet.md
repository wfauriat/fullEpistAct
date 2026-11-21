# Surgical Upgrade Sheet for *Agir d’après une représentation du monde* (`livre.html`)

**Purpose:** A 3-minute, high-ROI checklist of concrete revisions surfaced by our 9-domain synthesis, Hydrogen High refinement pass ([refinement_report.md](refinement_report.md)), and Track 1–2 formal/simulation validations ([Track 1](auto_research/track1_formal/RESULTS.md), [Track 2](auto_research/track2_sim/RESULTS.md)). Nothing here invalidates the book's core framework (**M1–M3**, the 5 detection conditions, or Ch. 13's matrix); each item sharpens scope or closes an empirical/formal gap.

---

### 1. Narrow Proposition 3(a) & Ch. 12.4 Against Inference-Time Search *(Scope Fix)*
* **Where:** Ch. 7 (*M3*), Ch. 12.4, and *Conclusion*.
* **Change:** Distinguish **in-frame salience elicitation** (where test-time compute scaling [Snell et al. 2024], Process Reward Models [Lightman et al. 2023/2024], and grounded debate [Khan et al. 2024] genuinely catch reasoning misses) from **out-of-frame omissions** ($z \notin \Theta$) and **unguided self-correction** (which fails without external verifiers, Kamoi et al. 2024).

### 2. Qualify Model Collapse in Ch. 16.3 *(Dissenting Result)*
* **Where:** Ch. 16.3 (*Blanchiment de provenance*).
* **Change:** Pair Shumailov et al. (2024) with **Gerstgrasser et al. (2024)**: recursive pretraining collapse requires *data replacement*; accumulating synthetic text alongside a retained human corpus bounds test error. Redirect the practical warning to **live post-2023 RAG/web contamination** where provenance is lost.

### 3. Anchor Ch. 15–16 with Verified 2021–2025 Empirical Studies *(Fills Conclusion's "Empirical Thinness")*
* **Where:** Ch. 15 & Ch. 16 (*Bibliographie* update).
* **Change:** Add these vetted studies alongside Becker et al. (2025) and Dell'Acqua et al. (2023)—noting moderators honestly:
  * **Skill decay:** Bastani et al. (*PNAS*, $\sim 1{,}000$ students: GPT Base `+48%` practice / `-17%` unaided exam vs. GPT Tutor `+127%` / no decay); Budzyń et al. (2025, *Lancet Gastroenterol. Hepatol.*, $N=1{,}443$: observational ADR drop `28.4% → 22.4%`).
  * **Human–AI synergy bifurcation:** Vaccaro et al. (2024, *Nat. Hum. Behav.*, $g = -0.23$ overall, positive on content creation); Goh et al. (2024, *JAMA Netw. Open* RCT, clinical diagnosis); vs. greenfield/junior coding speedups (Peng et al. 2023 `+55.8%`; Cui et al. 2024 `+26.08%` PRs/wk).
  * **Fluency & uncertainty:** Steyvers et al. (2025, *Nat. Mach. Intell.*, $N=301$, length bias); Kim et al. (2024, *ACM FAccT*, $N=404$, first-person hedges).
  * **Monoculture & equity trap:** Kleinberg & Raghavan (2021, *PNAS*); Wataoka et al. (2024/2025, perplexity self-preference); Liang et al. (2023, *Patterns*, `61.22%–97%+` false positives on TOEFL essays by AI detectors) + Liang et al. (2024, `6.5%–16.9%` LLM-modified peer reviews).

### 4. Clarify Coupled $p$–$z$ Stress in Model M2 & Cite Decision-Theory Anchors *(Ch. 17.1)*
* **Where:** Ch. 17.1 (*M2*) and Ch. 17.3 (*bacs à sable / verrous*).
* **Change:** Distinguish fixed-marginal event bounds ($\max(p,z) \le p_w \le \min(1, p+z)$) from latent common stress $S$ elevating *both* $p(S)$ and $z(S)$ simultaneously; note Track 1's copula finding that at $K \ge 100$ ($p^* \le 0.99\%$), safe margin $b_{\min}$ consumes $\sim 97\%$ of $p^*$ (`0.0096/0.0099`), mathematically forcing **verrous** over margin-tuning; connect *verrous* to neutralizing Al-Najjar & Weinstein's (2009) free-information aversion and *bacs à sable* to Arrow & Fisher's (1974) quasi-option value.

### 5. Address Friction–Bypass & Split Uncertainty-Gated CFFs From Stakes-Gated Locks *(Ch. 18)*
* **Where:** Ch. 18.1–18.3.
* **Change:** Acknowledge **Buçinca et al. (2021)** ($N=199$: CFFs cut overreliance *and* lower satisfaction, driving Shadow AI bypass) and **Rae, Provan & Dekker (2018)** (*safety clutter*). **Crucial Track 2 refinement:** do **not** trigger manual human CFFs on high stakes ($L/\Delta U > \tau_K$)—in 4,096 Sobol worlds that degenerated into static overload (`31.1%` bypass for $K > 500$). Trigger human CFFs **strictly on epistemic uncertainty** ($\hat{H}_t > \tau_H$: `1.30%` bypass, dominating `none` and `static` in `59.5%` of worlds), and enforce high-$K$ boundaries via non-bypassable orchestrator **verrous** (**CaMeL / VeriGuard** style).

### 6. Add Two Classic Micro-Foundations to Part II *(Ch. 6.4 & Ch. 8)*
* **Where:** Ch. 6.4 (*Challenger*) and Ch. 8.3 (Knight & Leveson).
* **Change:** Add **Eckhardt & Lee (1985)** / **Littlewood & Miller (1989)** (input-difficulty covariance proves *why* zero-communication checks correlate, grounding M1's parameter $c$) and **Diane Vaughan (1996)** (*normalization of deviance* explaining why organizational *prise en compte* fails).

### 7. Sharpen M1 Tipping Thresholds & Ground Ch. 18.3 Monitoring in SAVI *(Ch. 9, 16, 18)*
* **Where:** Ch. 9.5, Ch. 16.1, and Ch. 18.3 (*historique* & *erreurs injectées*).
* **Change:** Note Track 1's Z3-proven exact boundaries: M1's non-monotonic $R(p)$ inversion occurs **iff $s + f > 1$**, and in Ch. 16.1's monoculture scenario ($c=60\%$), shared AI beats the `10%` peer baseline **iff** producer error drops below **$p_{\text{crit}} = 6.15\%$**. In Ch. 18.3, cite **SAVI / e-values** (Ramdas et al. 2023) as the anytime-valid statistical engine allowing continuous escape monitoring without optional-stopping inflation.
