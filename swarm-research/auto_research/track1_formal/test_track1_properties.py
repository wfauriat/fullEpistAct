"""
Property-based differential fuzzing suite (Hypothesis + Pytest) for Track 1.
Runs >10,000 randomized evaluations across M1, M2, M3, Eckhardt-Lee, and SAVI invariants.
"""

from __future__ import annotations

import math
from hypothesis import given, settings, strategies as st
import numpy as np


@settings(max_examples=2500)
@given(
    p=st.floats(min_value=1e-5, max_value=1.0 - 1e-5),
    c=st.floats(min_value=0.0, max_value=0.999),
    m=st.floats(min_value=0.0, max_value=0.999),
    f=st.floats(min_value=1e-5, max_value=0.999),
)
def test_m1_residual_risk_bounds(p: float, c: float, m: float, f: float) -> None:
    s = (1.0 - c) * (1.0 - m)
    vpp = (p * s) / (p * s + (1.0 - p) * f)
    esc = 1.0 - s * vpp
    r = p * esc
    assert 0.0 <= vpp <= 1.0 + 1e-12
    assert 1.0 - s - 1e-12 <= esc <= 1.0 + 1e-12
    assert 0.0 <= r <= p + 1e-12


@settings(max_examples=2500)
@given(
    p=st.floats(min_value=0.0, max_value=1.0),
    z=st.floats(min_value=0.0, max_value=1.0),
    u=st.floats(min_value=0.0, max_value=1.0),
)
def test_m2_frechet_hoeffding_fuzz(p: float, z: float, u: float) -> None:
    pi_lo = max(0.0, p + z - 1.0)
    pi_hi = min(p, z)
    pi11 = pi_lo + u * (pi_hi - pi_lo)
    pw = p + z - pi11
    pw_indep = p + z - p * z
    assert max(p, z) - 1e-12 <= pw <= min(1.0, p + z) + 1e-12
    assert max(p, z) - 1e-12 <= pw_indep <= min(1.0, p + z) + 1e-12


@settings(max_examples=2500)
@given(
    N=st.integers(min_value=1, max_value=30),
    p=st.floats(min_value=0.0, max_value=0.5),
    q=st.floats(min_value=0.0, max_value=0.5),
)
def test_chain_vs_crosscheck_dominance(N: int, p: float, q: float) -> None:
    fail_unc = 1.0 - ((1.0 - p) ** N) * (1.0 - q)
    fail_chk = 1.0 - ((1.0 - p * p) ** N) * (1.0 - q)
    assert q - 1e-12 <= fail_chk <= fail_unc + 1e-12


@settings(max_examples=2500)
@given(
    qh=st.floats(min_value=0.05, max_value=0.95),
    th1=st.floats(min_value=0.01, max_value=0.99),
    th2=st.floats(min_value=0.01, max_value=0.99),
    ps1=st.floats(min_value=0.01, max_value=0.99),
    ps2=st.floats(min_value=0.01, max_value=0.99),
)
def test_eckhardt_lee_identity_fuzz(qh: float, th1: float, th2: float, ps1: float, ps2: float) -> None:
    pe = qh * th1 + (1.0 - qh) * th2
    m_bar = qh * ps1 + (1.0 - qh) * ps2
    joint = qh * th1 * ps1 + (1.0 - qh) * th2 * ps2
    cov = joint - pe * m_bar
    c_eff = cov / (pe * (1.0 - m_bar))
    one_minus_s = c_eff + (1.0 - c_eff) * m_bar
    assert math.isclose(one_minus_s, joint / pe, rel_tol=1e-11, abs_tol=1e-12)
    assert c_eff <= 1.0 + 1e-11


@settings(max_examples=2000)
@given(
    theta0=st.floats(min_value=0.01, max_value=0.5),
    lam_frac=st.floats(min_value=0.0, max_value=0.99),
    p_true=st.floats(min_value=0.0, max_value=0.5),
)
def test_savi_supermartingale_step(theta0: float, lam_frac: float, p_true: float) -> None:
    if p_true > theta0:
        return
    lam = lam_frac / theta0
    m1 = 1.0 + lam * (1.0 - theta0)
    m0 = 1.0 + lam * (0.0 - theta0)
    assert m1 >= 0.0 and m0 > 0.0
    assert p_true * m1 + (1.0 - p_true) * m0 <= 1.0 + 1e-12
