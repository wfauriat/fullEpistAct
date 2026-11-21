# Formal & Architectural Bridges: Extending M1–M3 and Ch. 10–18

**Scope.** *Agir d’après une représentation du monde* (`livre.html`) anchors its argument in three compact models—**M1** (detection conditions, chains vs. cross-checks, sensitivity, escape probability), **M2** (one-shot asymmetric risk with omitted factor $z$ and humility buffer $b$), and **M3** (the finite frame $\Theta$ as common cause)—before analyzing software and AI agents (Ch. 10–18). Building on [cross_review_monograph.md](../../cross_review_monograph.md) and [synthesis.md](../../synthesis.md), this note constructs mathematically explicit bridges across three areas, stating exact assumptions and pinning down where each formalism **still hits the $\Theta$-boundary wall**.

---

## 1. Extending Model M2 Beyond Independence: Coupled Stress, Bounds, and Decision Rules

### 1.1 Exact Decomposition of M2 Under Dependence and Common Stress

In Model M2 (Ch. 17.1, Annexe A.4.2), a risky one-shot action yields gain $\Delta U > 0$ on success and loss $L > 0$ on failure, giving the Savage (1954) cutoff $p^* = \frac{\Delta U}{\Delta U + L}$. Let $F_M \in \{0,1\}$ denote failure from modeled causes ($p = \Pr(F_M = 1)$) and $F_O \in \{0,1\}$ denote failure from omitted causes ($z = \Pr(F_O = 1)$), so real-world failure is $F_w = \max(F_M, F_O)$ with $p_w = \Pr(F_M = 1 \text{ or } F_O = 1)$. Under M2's independence assumption ($F_M \perp F_O$), $p_w^{\perp} = 1 - (1 - p)(1 - z) = p + z - pz$, and the decision rule is $p + b < p^*$ for humility buffer $b \ge 0$.

Relaxing independence separates **two distinct mechanisms** that act in opposite directions if conflated:

1. **Event-level dependence at fixed marginals $(p, z)$ (Fréchet–Hoeffding bounds).**  
   For any joint distribution with marginals $(p, z)$, $\pi_{11} = \Pr(F_M = 1, F_O = 1)$ satisfies $\max(0, p + z - 1) \le \pi_{11} \le \min(p, z)$. Since $p_w = p + z - \pi_{11}$,
   $$\max(p, z) \le p_w \le \min(1,\, p + z).$$
   Writing $\pi_{11} = pz + \rho_{MO}\sqrt{p(1-p)z(1-z)}$ ($\rho_{MO} \in [-1,1]$) shows that at *fixed* $(p, z)$, positive event correlation ($\rho_{MO} > 0$) lowers the union probability $p_w$ toward $\max(p,z)$ (overlapping failures), whereas negative correlation ($\rho_{MO} < 0$) pushes $p_w$ toward $\min(1, p+z)$, eliminating M2's $-pz$ discount.

2. **Latent-regime coupling (common stress $S$).**  
   In real collapses (*Challenger* under cold weather, 2008 CDOs under nationwide housing contraction; [03_uq_robustness.md](../../research/03_uq_robustness.md)), a latent stress state $S \in \mathcal{S}$ jointly drives conditional failure rates $p(S) = \Pr(F_M = 1 \mid S)$ and $z(S) = \Pr(F_O = 1 \mid S)$. Even when $F_M \perp F_O \mid S = s$, conditional failure risk is $p_w(s) = p(s) + z(s) - p(s)z(s)$, and averaging over $S$ gives $\mathbb{E}_S[p_w(S)] = \bar{p} + \bar{z} - \bar{p}\bar{z} - \mathrm{Cov}_S(p(S), z(S))$.  
   Suppose calibration occurs in a benign regime $S = s_0$ ($p_0 = p(s_0)$, $z(s_0) \approx 0$). Under a bivariate copula $C(u, v)$ on stress ranks $U = F_p(p(S))$, $V = F_z(z(S))$:
   * A **Gaussian copula** (Li 2000) has upper tail dependence $\lambda_U = \lim_{u \to 1^-} \Pr(V > u \mid U > u) = 0$ for all $\rho < 1$, hiding joint stress spikes.
   * Under **positive tail dependence** ($\lambda_U > 0$, e.g., $t$-copula or survival Clayton), an extreme shift $s_0 \to s_1$ elevates *both* $p(s_1) \gg p_0$ and $z(s_1) \gg 0$. The **silent trap** ($p_0 + b < p^* \le p_w(s_1)$) triggers whenever:
     $$z(s_1) \ge \frac{p^* - p(s_1)}{1 - p(s_1)} \quad \text{while} \quad p_0 + b < p^*.$$
     Because $p(s_1) > p_0$, common stress compresses the safety margin from both sides simultaneously, and across $k$ redundant units exposed to $S$, Jensen's inequality gives $\mathbb{E}_S[p_w(S)^k] \ge (\mathbb{E}_S[p_w(S)])^k$, breaking independent redundancy bounds.

### 1.2 Formal Decision-Theoretic Foundations for Humility Buffer $b$

Five formalisms give Ch. 17.1's informal buffer $b$ explicit mathematical content while exposing residual $\Theta$-limits:

| Formalism | Exact Mapping to M2 & Buffer $b$ | Assumptions | Where It Hits the $\Theta$-Boundary Wall |
| :--- | :--- | :--- | :--- |
| **Imprecise Probabilities** (Walley 1991) | Credal set $\mathcal{P} \subset \Delta(\Omega)$ induces interval $[\underline{p}_w, \overline{p}_w]$. Under $\Gamma$-maximin, act iff $\overline{p}_w < p^*$, setting $b_{\text{IP}} = \overline{p}_w - p$. | Coherent lower/upper previsions over $\Omega$. | If $z$ lies outside $\Omega$, $\overline{p}_w$ bounds only in-frame parameters; conditioning can induce **dilation** (Walley; Seidenfeld), widening intervals to $[0,1]$. |
| **Partial Identification & Minimax Regret** (Manski) | For $p_w \in [\underline{p}_w, \overline{p}_w]$ ($\underline{p}_w \le p^* \le \overline{p}_w$), max regret of acting is $(\Delta U+L)(\overline{p}_w - p^*)$ and of abstaining is $(\Delta U+L)(p^* - \underline{p}_w)$. Minimax regret acts iff $\frac{\underline{p}_w + \overline{p}_w}{2} < p^*$. With $\underline{p}_w = p$, $b_{\text{MMR}} = \frac{\overline{p}_w - p}{2}$. | Data-consistent bounds $\overline{p}_w < 1$ under minimal assumptions. | Violates IIA; if unmodeled $z$ lacks an empirical ceiling ($\overline{p}_w = 1$), $b_{\text{MMR}} = \frac{1-p}{2}$ blocks any action with $L > \Delta U$ ($p^* < \frac{1}{2}$). |
| **Hansen–Sargent Robust Control** | Optimizing against $Q$ within KL ball $D_{\mathrm{KL}}(Q \| P_0) \le \eta$ (multiplier $\theta > 0$) exponentially tilts $P_0 = \text{Bern}(p)$ to $\frac{q^*}{1-q^*} = \frac{p}{1-p}\exp\!\big(\frac{\Delta U + L}{\theta}\big)$, yielding $b_{\text{HS}} = q^* - p$. | Nominal model $P_0$; absolute continuity $Q \ll P_0$; exogenous $\eta$ or $\theta$. | **Support-blindness:** $D_{\mathrm{KL}}(Q \| P_0) = +\infty$ wherever $P_0(\omega) = 0$. KL balls reweight *admitted* states in $\Theta$, assigning zero mass to unconceptualized mechanisms $z \notin \Theta$. |
| **Al-Najjar & Weinstein (2009)** | Multiple-prior ambiguity rules (MEU / static non-SEU $b$) cause **dynamic inconsistency**: a sophisticated ambiguity-averse agent anticipating preference reversals can **refuse free, informative signals**. | Sequential updating under non-SEU preferences. | Shows personal ambiguity margins are dynamically unstable; preventing information aversion requires **institutional pre-commitment**—grounding Ch. 17.2's mandatory *verrous*. |
| **Arrow–Fisher (1974) Quasi-Option Value** | When $a_1$ is irreversible at $t=0$ and $Z$-signals arrive before $t=1$, staging via a reversible *bac à sable* ($a_0$) yields $\text{QOV} = \mathbb{E}[\max_{a_1} U] - \max_{a_1} \mathbb{E}[U] \ge 0$ under risk-neutral SEU. | Reversible staging option and informative future signal on $Z$. | Grounded inside pure SEU without ambiguity aversion, *provided* $Z$ varies during staging; if $Z \approx z_0$ stays regime-locked in the sandbox, $\text{QOV} = 0$ on $Z$. |

Thus $b$ decomposes into (i) Arrow–Fisher QOV when staging is reversible, (ii) an in-frame minimax-regret or KL-tilted margin inside $\Theta$, and (iii) externally enforced *verrous* (Ch. 17.2) that neutralize Al-Najjar–Weinstein dynamic inconsistency.

---

## 2. $\mathcal{M}$-Open Statistics & Calibration Bridges (Ch. 3, Ch. 5 & Ch. 18)

Proposition 1 (Ch. 5.4) uses $\mathrm{Var}(Y) = \mathbb{E}_\theta[\mathrm{Var}(Y \mid \theta)] + \mathrm{Var}_\theta(\mathbb{E}[Y \mid \theta])$ ($\theta \in \Theta$) to prove that quantitative error bars measure only dispersion *inside* $\Theta$. Modern $\mathcal{M}$-open statistics ($P^* \notin \mathcal{M}$; Bernardo & Smith 1994) formalizes every face of this wall.

### 2.1 Misspecification, Discrepancy, and Uncertainty Leakage (Ch. 5)

1. **Kleijn & van der Vaart (2012):** Under parametric misspecification ($P^* \notin \{P_\theta : \theta \in \Theta\}$), the posterior concentrates at $\theta^* = \arg\min_{\theta \in \Theta} D_{\mathrm{KL}}(P^* \| P_\theta)$ with covariance $I_{\theta^*}^{-1}$, whereas the true sampling covariance is the sandwich $I_{\theta^*}^{-1}\Sigma_{\theta^*} I_{\theta^*}^{-1}$ ($\Sigma_{\theta^*} = \mathrm{Cov}_{P^*}(\nabla \log p_{\theta^*})$). Because $I_{\theta^*} \neq \Sigma_{\theta^*}$, Bayesian credible intervals lose frequentist coverage even as $n \to \infty$—formalizing Proposition 1 asymptotically.
2. **Grünwald & van Ommen (2017) — SafeBayes:** Standard Bayes ($\eta = 1$) and BMA can be **inconsistent** under simple misspecification (e.g., homoscedastic models on heteroscedastic data) via *hypercompression*. **SafeBayes** uses a tempered posterior $\pi_n^{(\eta)}(\theta) \propto \pi_0(\theta)\prod_{i=1}^n p_\theta(y_i \mid x_i)^\eta$, tuning $\eta \in (0, 1]$ via sequential predictive risk (complemented by **Bayesian stacking**, Yao et al. 2018). *$\Theta$-wall:* Tempering $\eta < 1$ curbs in-frame overconfidence, yet $\pi_n^{(\eta)}$ stays supported on $\Theta$ and cannot detect an omitted $Z_t \approx z_0$ constant in-sample.
3. **Kennedy & O'Hagan (2001) & Brynjarsdóttir & O'Hagan (2014):** Adding a GP discrepancy $\delta(x)$ to simulator $\eta(x, \theta)$ via $y(x) = \eta(x, \theta) + \delta(x) + \varepsilon$ formalizes M3's $Y = g(x, z)$ inside $\Theta$, *but* causes **parameter–discrepancy unidentifiability**: $\delta(x)$ absorbs bias by distorting $\theta$, and outside observed support $x_{\text{new}}$, $\delta(x_{\text{new}})$ reverts to its prior mean—failing silently under out-of-sample $z$-shifts.
4. **Wimmer et al. (2023):** Translating Eq. (5.1) into ML entropy decompositions $H[Y \mid x] = \mathbb{E}_\theta[H[Y \mid x, \theta]] + I(Y; \theta \mid x)$ violates monotonicity axioms for second-order uncertainty. Coupled with **identifiability leakage** ([03_uq_robustness.md](../../research/03_uq_robustness.md)), structural $\mathcal{M}$-open bias from omitted $z$ leaks into the aleatory noise head $H[Y \mid x, \theta]$, hiding missing structure as irreducible noise (formalizing Ch. 5.4, *Nuance*).

### 2.2 Rare-Event Scoring & Conformal Limits (Ch. 3 & Ch. 5)

5. **Barber, Candès, Ramdas & Tibshirani (2019–2021):** Under exchangeability, conformal prediction (Vovk et al. 2005; Angelopoulos & Bates 2023) achieves marginal coverage $\mathbb{P}(Y_{n+1} \in \widehat{C}_n(X_{n+1})) \ge 1 - \alpha$. Barber et al. prove exact **pointwise $X$-conditional coverage** $\mathbb{P}(Y_{n+1} \in \widehat{C}_n(X_{n+1}) \mid X_{n+1} = x) \ge 1 - \alpha$ for all $x$ is impossible distribution-free without infinite-width intervals—exposing how marginal guarantees mask tail-subgroup miscoverage and break when $z$-shift violates exchangeability.
6. **Lerch et al. (2017) & Gneiting & Ranjan (2011):** Ch. 3.3's puzzle (M. X at $5\%$ vs. M. Y at $0.1\%$) reflects the **Forecaster's Dilemma**: scoring forecasts *conditionally* on extreme realizations ($y > r$) **destroys strict propriety** and rewards alarmism ("crying wolf"), whereas unconditional proper scores (Gneiting & Raftery 2007) lack power on rare tails. Gneiting & Ranjan (2011) preserve propriety via **threshold-weighted CRPS**:
   $$\mathrm{twCRPS}(F, y) = \int_{-\infty}^{\infty} \big(F(t) - \mathbb{I}(y \le t)\big)^2 w(t)\,dt, \qquad w(t) \ge 0,$$
   weighting predictive CDF tails ($w(t) = \mathbb{I}(t \ge r)$) without outcome conditioning. *$\Theta$-wall:* twCRPS still requires sufficient extreme realizations and cannot flag dormant $Z_0$ before shift.

### 2.3 Online Falsification via SAVI / E-Values (Ch. 18.3)

To operationalize Ch. 3.4's *historique* and Ch. 18.3's longitudinal monitoring (Gelman & Shalizi 2013; Mayo 2018) under continuous peeking, **Safe Anytime-Valid Inference (SAVI)** (Ramdas, Grünwald, Vovk & Shafer 2023) uses non-negative **e-processes** $(E_t)_{t \ge 0}$ satisfying $\mathbb{E}_P[E_\tau] \le 1$ for all $P \in H_0$ and all stopping times $\tau$, giving $\sup_{P \in H_0} \Pr_P(\exists t : E_t \ge 1/\alpha) \le \alpha$ by Ville's inequality. For binary failure or *erreur injectée* escapes $X_t \in \{0,1\}$ against claimed bound $H_0: p \le p_0$:
$$E_t = \prod_{i=1}^t \left[1 + \lambda_i\left(\frac{X_i}{p_0} - 1\right)\right], \qquad \lambda_i \in [0, 1/p_0) \text{ predictable},$$
permits an automated *verrou* to halt deployment whenever $E_t \ge 1/\alpha$ without optional-stopping bias. *$\Theta$-wall:* SAVI falsifies $H_0$ only on monitored observables $X_t$ *after* errors manifest; it cannot anticipate silent $Z_0$ prior to activation.

---

## 3. Micro-Foundations of CCF ($c$ in M1) & Agentic Containment (Ch. 14)

### 3.1 Deriving M1's Parameter $c$ from Difficulty-Induced Correlation

In M1 (Ch. 9.5, Ch. 16.1, Annexe A.7.3), producer error rate $P(E)$ meets a checker of sensitivity $s = (1 - c)(1 - m)$, yielding escape probability $1 - su$ and residual risk $R = P(E)(1 - su)$. **Eckhardt & Lee (1985)** and **Littlewood & Miller (1989)** provide the exact micro-foundation for $c$ behind Knight & Leveson's (1986) empirical finding.

Let inputs $X \sim \mu$ vary over $\mathcal{X}$, and let zero-communication producer and checker methodologies have input-conditional **difficulty functions** $\theta(x) = \Pr(E \mid X = x)$ and $\psi(x) = \Pr(\bar{C}_{\text{detect}} \mid X = x, E)$, with marginals $P(E) = \mathbb{E}_X[\theta(X)]$ and $\bar{m} = \mathbb{E}_X[\psi(X)]$. Even under **conditional independence given $x$** ($E \perp \bar{C}_{\text{detect}} \mid X = x$), unconditional joint escape is:
$$\Pr(E \cap \bar{C}_{\text{detect}}) = \mathbb{E}_X\big[\theta(X)\psi(X)\big] = P(E)\,\bar{m} + \mathrm{Cov}_X\big(\theta(X), \psi(X)\big).$$
Matching $\Pr(\bar{C}_{\text{detect}} \mid E) = 1 - s = c + (1 - c)\bar{m}$ yields:
$$c_{\text{eff}} = \frac{\mathrm{Cov}_X\big(\theta(X), \psi(X)\big)}{P(E)(1 - \bar{m})}.$$
Three M1 regimes follow immediately:
1. **Shared-methodology correlation (Eckhardt & Lee 1985):** When $\psi \approx \theta$ (same LLM family or *prêteur unique*, Ch. 16.1), $\mathrm{Cov}_X(\theta, \psi) \approx \mathrm{Var}_X(\theta(X)) > 0$ forces $c_{\text{eff}} > 0$ with zero communication; on low-entropy misconceptions ($\theta(x) \in \{0,1\}$; Farquhar et al. 2024), $c_{\text{eff}} \to 1$.
2. **Forced diversity (Littlewood & Miller 1989):** Pairing an LLM producer ($\theta(x)$) with an orthogonal formal/deterministic checker ($\psi(x) \approx 0$ on syntax, units, or proofs where $\theta(x)$ is high) yields $\mathrm{Cov}_X(\theta, \psi) \le 0$ and $c_{\text{eff}} \le 0$, breaking M1's escape floor $1 - s \ge c$ on that error class.
3. **M3 Collapse:** On omitted $z \notin \Theta$ shared by both methodologies, $\theta(x, z) = \psi(x, z) = 1$ on $z$-failures, driving $c_{\text{eff}} \to 1$.

### 3.2 Mapping Ch. 14's *Blanchiment* & Inverted Guarantees to Agentic Architectures

Ch. 14 diagnoses (a) free-text **blanchiment** (Ch. 14.3), which strips conditions and provenance, inflating comparison blind spot $B_{\text{cmp}}$ in Eq. (8.2) ($B_{\text{croisé}} = B_1 \cap (B_2 \cup B_{\text{cmp}})$), and (b) **inverted execution authority** (Ch. 14.4), letting uncontracted agents mutate external state faster than human uptake $u$. Four architectures operationalize Ch. 14's containment—each bounded by a $\Theta$-wall:

| Ch. 13–14 Mechanism | Formalism / Architecture | How It Restores $C_1$–$C_5$ / Cuts $c$ | Residual $\Theta$-Boundary Wall |
| :--- | :--- | :--- | :--- |
| **Anti-*blanchiment* & provenance** (Ch. 14.3) | **Dual LLM & CaMeL** (Debenedetti et al. 2025) | Separates *Privileged LLM* (control flow from trusted prompt) from *Quarantined LLM* (untrusted data parsing without tool rights). A deterministic interpreter tracks **capability metadata and taint tags**, blocking prompt injections from altering control flow. | Vulnerable to **data-channel smuggling** (malicious payload mapped into an authorized structured field); bounded by engineer-authored capability policies. |
| **Execution contracts & timing** (Ch. 14.4, 17.2) | **AgentSpec** (Wang et al. 2025) & **VeriGuard** (Miculicich et al. 2025) | *AgentSpec* enforces *Trigger–Predicate–Enforcement* DSL guards before side effects. *VeriGuard* verifies policies **offline** formally and runs a deterministic millisecond **online** monitor (zero LLM in hot path, restoring $C_4$, $C_5$, and $c \approx 0$ on policy checks). | Protects only *formalizable, anticipated* rules; blind to unmodeled semantic harms or shifting deployment intent outside the verified spec. |
| **Continuous shields** (Ch. 13.3 Simplex) | **Control Barrier Functions (CBFs)** | Solves an online QP over safe set $\mathcal{S} = \{x : h(x) \ge 0\}$ perturbing $u_{\text{ML}}$ to enforce $\dot{h}(x,u) + \alpha(h(x)) \ge 0$. | Breaks via (1) unmodeled dynamics $z$, (2) QP infeasibility under actuator saturation, (3) myopic dead-ends, and (4) **learned-CBF circularity** (neural $h$ restores $c > 0$). |
| **Autoformalization** (Ch. 13.1, M3) | **Lean 4** (Moura & Ullrich 2021; Wu et al. 2022) | Audited kernel gives $m \approx 0, c \approx 0$ for syntactic derivation $\vdash \phi_{\text{formal}}$ inside $\Theta$. | **Proof-driven statement distortion & implicit hypothesis alteration**: RL provers weaken $\phi_{\text{formal}}$ to pass compilation (inflating $B_{\text{cmp}}$). Round-trip $\text{NL}\to\text{Lean}\to\text{NL}'$ shares Eckhardt–Lee blind spots ($c>0$); needs counterexample fuzzing + human statement audit. |

---

## Verified References

* Al-Najjar, N. I., & Weinstein, J. (2009). The ambiguity aversion literature. *Economics & Philosophy*, 25(3), 249–284.
* Angelopoulos, A. N., & Bates, S. (2023). Conformal prediction: A gentle introduction. *Found. Trends Mach. Learn.*, 16(4), 494–591.
* Arrow, K. J., & Fisher, A. C. (1974). Environmental preservation, uncertainty, and irreversibility. *QJE*, 88(2), 312–319.
* Barber, R. F., Candès, E. J., Ramdas, A., & Tibshirani, R. J. (2021). Limits of distribution-free conditional predictive inference. *Information and Inference*, 10(2), 455–482.
* Bernardo, J. M., & Smith, A. F. M. (1994). *Bayesian Theory*. Wiley.
* Brynjarsdóttir, J., & O'Hagan, A. (2014). Learning about physical parameters: Model discrepancy. *Inverse Problems*, 30(11), 114007.
* Debenedetti, E., et al. (2025). Defeating prompt injections by design (*CaMeL*). Google DeepMind & ETH Zurich.
* Eckhardt, D. E., & Lee, L. D. (1985). Theoretical basis for multiversion software subject to coincident errors. *IEEE TSE*, SE-11(12), 1511–1517.
* Farquhar, S., Kossen, J., Kuhn, L., & Gal, Y. (2024). Detecting hallucinations in LLMs using semantic entropy. *Nature*, 630, 625–630.
* Fauriat, W. *Agir d’après une représentation du monde* (`livre.html`).
* Gelman, A., & Shalizi, C. R. (2013). Philosophy and the practice of Bayesian statistics. *BJMSP*, 66(1), 8–38.
* Gneiting, T., & Raftery, A. E. (2007). Strictly proper scoring rules. *JASA*, 102(477), 359–378.
* Gneiting, T., & Ranjan, R. (2011). Comparing density forecasts using threshold- and quantile-weighted scoring rules. *JBES*, 29(3), 411–422.
* Grünwald, P., & van Ommen, T. (2017). Inconsistency of Bayesian inference for misspecified linear models (*SafeBayes*). *Bayesian Analysis*, 12(4), 1069–1103.
* Kennedy, M. C., & O'Hagan, A. (2001). Bayesian calibration of computer models. *JRSS-B*, 63(3), 425–464.
* Kleijn, B. J. K., & van der Vaart, A. W. (2012). Bernstein-von-Mises theorem under misspecification. *Electron. J. Stat.*, 6, 354–381.
* Knight, J. C., & Leveson, N. G. (1986). Assumption of independence in multiversion programming. *IEEE TSE*, SE-12(1), 96–109.
* Lerch, S., Thorarinsdottir, T. L., Ravazzolo, F., & Gneiting, T. (2017). Forecaster's dilemma. *Statistical Science*, 32(1), 106–127.
* Li, D. X. (2000). On default correlation: A copula function approach. *J. Fixed Income*, 9(4), 43–54.
* Littlewood, B., & Miller, D. R. (1989). Conceptual modeling of coincident failures in multi-version software. *IEEE TSE*, 15(12), 1596–1614.
* Mayo, D. G. (2018). *Statistical Inference as Severe Testing*. Cambridge University Press.
* Miculicich, L., et al. (2025). Enhancing LLM agent safety via verified code generation (*VeriGuard*). Google DeepMind / Google Cloud AI Research.
* Moura, L. de, & Ullrich, S. (2021). The Lean 4 theorem prover and programming language. *CADE-28*.
* Ramdas, A., Grünwald, P., Vovk, V., & Shafer, G. (2023). Game-theoretic statistics and safe anytime-valid inference (*SAVI*). *Statistical Science*, 38(4), 576–601.
* Savage, L. J. (1954). *The Foundations of Statistics*. Wiley.
* Sha, L. (2001). Using simplicity to control complexity (*Simplex*). *IEEE Software*, 18(4), 20–28.
* Vovk, V., Gammerman, A., & Shafer, G. (2005). *Algorithmic Learning in a Random World*. Springer.
* Walley, P. (1991). *Statistical Reasoning with Imprecise Probabilities*. Chapman and Hall.
* Wang, H., Poskitt, C. M., & Sun, J. (2025). *AgentSpec*: Customizable runtime enforcement for LLM agents. SMU.
* Wimmer, L., Sale, Y., Hofman, P., Bischl, B., & Hüllermeier, E. (2023). Quantifying aleatoric and epistemic uncertainty in ML. *UAI 2023*.
* Wu, Y., et al. (2022). Autoformalization with large language models. *NeurIPS 2022*.
* Yao, Y., Vehtari, A., Simpson, D., & Gelman, A. (2018). Using stacking to average Bayesian predictive distributions. *Bayesian Analysis*, 13(3), 917–1007.
