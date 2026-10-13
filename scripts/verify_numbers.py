"""Recompute the numbers quoted in the version 00 research notes.

Every value below appears in docs/research or docs/plan and can be obtained
from a closed formula or from a small exact computation. The script prints
each value next to the one quoted in the documents and exits with status 1 if
any of them disagree.

Requires Python 3.12+ and NumPy.  Run from the repository root:

    python scripts/verify_numbers.py
"""

from __future__ import annotations

import math
import sys

import numpy as np

RESULTS: list[tuple[str, float, float, float]] = []


def check(label: str, computed: float, quoted: float, tol: float) -> None:
    """Record a computed value against the value quoted in the documents."""
    RESULTS.append((label, computed, quoted, tol))


# --- Two-dimensional Ising model (J = k_B = 1) -------------------------------

K_c = 0.5 * math.log(1 + math.sqrt(2))
check("Ising: K_c = ln(1 + sqrt 2) / 2", K_c, 0.4407, 5e-5)
check("Ising: T_c = 1 / K_c", 1 / K_c, 2.269185, 5e-7)
check("Ising: Bethe T_c = 2 / ln(z / (z - 2)), z = 4", 2 / math.log(2), 2.885, 5e-4)
U_star = 1 - 1 / (3 * 0.856216)  # Q = <m^2>^2 / <m^4> from Kamieniarz & Blote (1993)
check("Ising: Binder cumulant at T_c, U* = 1 - 1/(3Q)", U_star, 0.6107, 5e-5)

# --- Abelian sandpile on Z^2: height probabilities (heights 1..4) ----------

pi = math.pi
P = [
    2 / pi**2 - 4 / pi**3,
    1 / 4 - 1 / (2 * pi) - 3 / pi**2 + 12 / pi**3,
    3 / 8 + 1 / pi - 12 / pi**3,
    3 / 8 - 1 / (2 * pi) + 1 / pi**2 + 4 / pi**3,
]
for h, (p, quoted) in enumerate(zip(P, (0.0736, 0.1739, 0.3063, 0.4462)), start=1):
    check(f"Sandpile: P({h})", p, quoted, 5e-5)
check("Sandpile: sum of P(h)", sum(P), 1.0, 1e-12)
check("Sandpile: mean height (heights 1..4) = 25/8", sum(h * p for h, p in enumerate(P, 1)), 25 / 8, 1e-12)


def toppling_matrix(L: int) -> np.ndarray:
    """Reduced Laplacian of the L x L grid with a sink attached to the boundary."""
    n = L * L
    D = np.zeros((n, n))
    for x in range(L):
        for y in range(L):
            i = x * L + y
            D[i, i] = 4
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                u, v = x + dx, y + dy
                if 0 <= u < L and 0 <= v < L:
                    D[i, u * L + v] = -1
    return D


for L, quoted in ((1, 4), (2, 192), (3, 100352), (4, 557568000)):
    check(f"Sandpile: recurrent configurations, det(Delta), L = {L}", round(np.linalg.det(toppling_matrix(L))), quoted, 0)

catalan = 0.915965594177219015
check("Sandpile: 4G/pi (spanning-tree entropy of Z^2)", 4 * catalan / pi, 1.1662, 5e-5)
check("Sandpile: log det(Delta) / L^2 at L = 48", np.linalg.slogdet(toppling_matrix(48))[1] / 48**2, 1.177, 5e-4)


def stabilize(z: np.ndarray) -> np.ndarray:
    """Topple synchronously until stable (heights 0..3, threshold 4, sink at the edge)."""
    z = z.copy()
    while True:
        unstable = (z >= 4).astype(np.int64)
        if not unstable.any():
            return z
        z -= 4 * unstable
        z[1:, :] += unstable[:-1, :]
        z[:-1, :] += unstable[1:, :]
        z[:, 1:] += unstable[:, :-1]
        z[:, :-1] += unstable[:, 1:]


def addition_period(L: int, site: tuple[int, int]) -> int:
    """Number of additions at `site` after which the all-3 configuration recurs."""
    start = np.full((L, L), 3, dtype=np.int64)
    z = start.copy()
    k = 0
    while True:
        z[site] += 1
        z = stabilize(z)
        k += 1
        if np.array_equal(z, start):
            return k


check("Sandpile: addition period, 3 x 3 grid, corner", addition_period(3, (0, 0)), 224, 0)
check("Sandpile: addition period, 3 x 3 grid, centre", addition_period(3, (1, 1)), 16, 0)
check("Sandpile: addition period, 4 x 4 grid, corner", addition_period(4, (0, 0)), 6600, 0)

# --- Branching process: Borel distribution of the total progeny -------------

for n in (100, 1000, 10000):
    log_p = -n + (n - 1) * math.log(n) - math.lgamma(n + 1)
    check(f"Branching: n^(3/2) sqrt(2 pi) P(S = n) for Poisson(1), n = {n}", math.exp(log_p) * n**1.5 * math.sqrt(2 * pi), 1.0, 1e-2)

# --- Kuramoto ----------------------------------------------------------------

g0 = 1 / math.sqrt(2 * pi)  # Gaussian density at 0, sigma = 1
check("Kuramoto: K_c = 2 / (pi g(0)), Gaussian, sigma = 1", 2 / (pi * g0), 1.596, 5e-4)
check("Kuramoto: sqrt(8 / pi)", math.sqrt(8 / pi), 1.596, 5e-4)

# --- Renormalization examples -------------------------------------------------

lam = 6 * 0.5 * 0.5  # derivative of p^3 + 3 p^2 (1 - p) at p = 1/2
check("Percolation cell RG: p* = 1/2 is a fixed point", 0.5**3 + 3 * 0.5**2 * 0.5, 0.5, 1e-15)
check("Percolation cell RG: nu = ln sqrt 3 / ln(3/2)", math.log(math.sqrt(3)) / math.log(lam), 1.355, 5e-4)


def mk(K: float) -> float:
    """Migdal-Kadanoff recursion for the 2D Ising model with b = 2."""
    return math.atanh(math.tanh(2 * K) ** 2)


lo, hi = 0.1, 1.0
for _ in range(200):
    mid = 0.5 * (lo + hi)
    lo, hi = (lo, mid) if mk(mid) > mid else (mid, hi)
K_star = 0.5 * (lo + hi)
slope = (mk(K_star + 1e-7) - mk(K_star - 1e-7)) / 2e-7
check("Migdal-Kadanoff: fixed point K*", K_star, 0.3047, 5e-5)
check("Migdal-Kadanoff: nu = ln 2 / ln(dK'/dK)", math.log(2) / math.log(slope), 1.34, 5e-3)

K = 2.0
for _ in range(5):
    K = math.atanh(math.tanh(K) ** 2)
check("1D Ising decimation: K after five steps from K = 2", K, 0.32, 5e-3)

# --- Report ------------------------------------------------------------------

failures = 0
width = max(len(label) for label, *_ in RESULTS)
for label, computed, quoted, tol in RESULTS:
    ok = abs(computed - quoted) <= tol
    failures += not ok
    print(f"{'ok      ' if ok else 'MISMATCH'}  {label:<{width}}  computed {computed:.6g}  quoted {quoted:.6g}")
print(f"\n{len(RESULTS) - failures} of {len(RESULTS)} values agree with the documents.")
sys.exit(1 if failures else 0)
