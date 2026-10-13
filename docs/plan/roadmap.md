# Roadmap

Version 00 plan. The brief describes six stages. This document maps them to
versions, says which models come first and why, and fixes what "done" means
for every module.

## 1. Stages and versions

| Stage | Content | Versions |
|---|---|---|
| 1. Research and conceptual map | Field map, model catalogue, terminology, bibliography, experiments and open questions | **00** (this version) |
| 2. Architecture and specifications | [Architecture](architecture.md) and the [specification template](../specs/TEMPLATE.md) now; each module's specification at the start of its version | 00, then the start of 01, 02, 03 |
| 3. Minimum viable laboratory | Sandpile with branching process; Ising; Kuramoto | 01–03 |
| 4. Cross-model analysis | Finite-size scaling and power-law toolkit, sandpile variants, microscopic versus mean-field comparisons; then renormalization | 04–05 |
| 5. Expansion | Further models in priority order (Section 4) | 06 onwards |
| 6. Research documentation | Specifications, experiment records, open questions, bibliography | Every version |

## 2. The first three modules

### The recommendation

The preferred combination in the brief is kept: the BTW/Abelian sandpile, the
Ising model and the Kuramoto model. Each gets an exactly solvable mean-field
companion from the start:

| Module | Microscopic model | Mean-field companion | Strongest exact anchors |
|---|---|---|---|
| 01 | Abelian sandpile in Dhar's formulation; BTW's synchronous update as an option | Galton–Watson branching process | $\det\Delta$ and the burning test; height probabilities on $\mathbb{Z}^2$; mean toppling numbers $(\Delta^{-1})_{ij}$; Borel and $n^{-3/2}$ laws for the branching process |
| 02 | Ising model with Metropolis, heat-bath and Wolff dynamics | Curie–Weiss (exact for all-to-all coupling) and the Bethe approximation | Exact enumeration of small tori; Kaufman and Ferdinand–Fisher finite-size formulas; Onsager's $T_c$; Yang's magnetization; $U^{\ast}\approx0.6107$ |
| 03 | Kuramoto model with $N$ oscillators | Ott–Antonsen equations; the self-consistency equation | $K_c=2/(\pi g(0))$; $r=\sqrt{1-2\Delta/K}$ for Lorentzian frequencies |

### Why this set

- **Three kinds of dynamics, three kinds of verification.**
  - A driven threshold automaton out of equilibrium: integer bookkeeping and
    conservation laws.
  - An equilibrium Markov chain: error analysis of correlated Monte Carlo
    data.
  - A deterministic ODE system: integration accuracy and convergence.
- **Three routes to collective behaviour.** Self-organization to a critical
  state, a tuned critical point, and a bifurcation to synchronization.
- **Exact results strong enough to validate an implementation**, not just to
  illustrate it.
- **Mean-field theory built in from the start.** Each module has its limit
  equation next to the simulation, so the Stage 4 comparisons need no new
  models.
- **Coverage.** The three modules touch six of the twelve families of the
  [field map](../research/01-field-map.md#4-the-twelve-families): SOC,
  statistical mechanics, mean-field theory, renormalization (through Ising),
  synchronization, and branching processes.

### Alternatives considered

- **Percolation instead of Kuramoto.** Cheaper, and the cleanest place to
  learn finite-size scaling and real-space RG, but it has no dynamics and no
  mean-field differential equation. It comes with the renormalization version
  (05) and as the first expansion.
- **Manna or Oslo instead of BTW** as the first SOC model. They scale more
  cleanly, but the exact algebra of the Abelian sandpile is the stronger
  check of an implementation. They arrive in 04 as variants that share the
  sandpile code, which is exactly where the contrast matters.
- **Contact process.** The paradigm of absorbing-state transitions. It
  follows percolation, together with fixed-energy sandpiles.

## 3. Versions and their acceptance criteria

A version is released only when every criterion is met or an unmet one is
reported in the update log with the reason.

### 01 · Infrastructure and the sandpile

- **Scope.**
  - Package skeleton; `core` (seeds, parameters, protocol, lattices);
    records and export; basic analysis (online statistics, autocorrelation,
    distributions).
  - Specifications `docs/models/sandpile.md` and `docs/models/branching.md`,
    written before the code.
  - Sandpile: reference sequential relaxation and synchronous relaxation;
    random, fixed-site and BTW-1987-style drives; sinks chosen per side;
    observables: size, area, duration, outflow.
  - Exact tools: $\det\Delta$, burning test, identity element, Green's
    function.
  - Branching process: exact progeny distributions for Poisson and binomial
    offspring, extinction probabilities, simulation.
  - App: home page and the sandpile page; validation report.
- **Acceptance.**
  - *Invariants* hold under property-based testing: grain conservation, the
    Abelian property for random toppling orders, stability after
    relaxation.
  - *Exact checks*:
    - the burning test counts 192 and 100352 recurrent configurations on the
      $2\times2$ and $3\times3$ grids;
    - addition periods are 224 and 16 on the $3\times3$ grid;
    - the identity element is idempotent and recurrent;
    - mean toppling numbers match $(\Delta^{-1})_{ij}$ within confidence
      intervals.
  - *Statistical checks*:
    - bulk height frequencies agree with the exact $P(h)$, and their
      dependence on $L$ is documented;
    - branching-process progeny agrees with the Borel law.
  - *Gates* 1 (frame rate) and 2 (kernel speed) of the
    [architecture](architecture.md) are measured and reported.

### 02 · Ising

- **Scope.** Checkerboard Metropolis, heat bath, Wolff; exact enumeration for
  $L\le4$; finite-size exact formulas; Onsager and Yang; Curie–Weiss and
  Bethe; autocorrelation and blocking; Binder cumulants; app page;
  specification.
- **Acceptance.**
  - Detailed balance is verified exactly on $2\times2$ and $3\times3$ tori.
  - Simulations agree with enumeration and with the finite-size formulas.
  - The Binder crossing is consistent with $T_c=2.269185$ and
    $U^{\ast}\approx0.6107$.
  - Metropolis and Wolff give the same equilibrium values within confidence
    intervals, and their autocorrelation times are reported.

### 03 · Kuramoto

- **Scope.** Fixed-step RK4 with a convergence test; Lorentzian, Gaussian
  and uniform frequency distributions; $K_c$, the self-consistency solution
  and the Ott–Antonsen equations; experiments at finite $N$; an optional noise
  term (Euler–Maruyama), which links the model to the mean-field XY model;
  app page; specification.
- **Acceptance.**
  - $r(K)$ agrees with Ott–Antonsen (Lorentzian) and with the
    self-consistency solution (Gaussian) within the bands expected at finite $N$.
  - The uniform distribution shows its discontinuous transition.
  - Fluctuations of $r$ below $K_c$ scale like $N^{-1/2}$.
  - Results converge as $\Delta t$ is halved.

### 04 · Cross-model analysis

- The finite-size scaling and data-collapse toolkit; moment analysis.
- The full power-law procedure of the
  [experiments notes](../research/05-experiments-and-open-questions.md#claiming-a-power-law),
  with the skepticism experiment E10.
- Manna and Oslo as variants of the sandpile module (experiment E2).
- Microscopic versus mean-field views for all three modules; sensitivity to
  boundaries, update order and seeds.

### 05 · Renormalization

- Exact 1D decimation; majority-rule block spins ($b=2,3$); renormalized
  observables; Swendsen's Monte Carlo RG; the Migdal–Kadanoff recursion.
- The percolation cell RG, with a minimal percolation sampler.
- Period doubling in the logistic map (Feigenbaum constants) as the rigorous
  counterpart of the heuristic block-spin picture.

## 4. Expansion order from 06

1. **Percolation**, as a full module (Newman–Ziff, finite-size scaling).
2. **Logistic map and Lorenz system**, if not completed in 05.
3. **Contact process, directed percolation and fixed-energy sandpiles**
   (experiment E3).
4. **Cellular automata**: elementary rules, Game of Life, Domany–Kinzel.
5. **Reaction–diffusion**: Turing analysis, Gray–Scott, excitable media.
6. **Networks**: Erdős–Rényi, Watts–Strogatz, Barabási–Albert; SIS and SIR;
   Kuramoto on networks.
7. **Collective motion**: Vicsek, with Boids as a contrast.
8. **Agent-based models**: Schelling, voter model.
9. **Further candidates** from the catalogue: OFC, forest fire, random-field
   Ising model, KPZ and Eden growth, TASEP.

**The rule for adding a model.** A model enters only after four things have
been written and reviewed: its mathematical specification, what the
visualization should show, its validation criteria, and its implementation
requirements.

## 5. Definition of done for a module

- [ ] Specification complete in all 14 parts of the
      [template](../specs/TEMPLATE.md), with evidence labels.
- [ ] Reference implementation; compiled kernels only with equivalence tests.
- [ ] Tests: rules, invariants, exact comparisons, statistics, regression.
- [ ] A validation report generated by `python -m complexsystemslab.validate`.
- [ ] App page with the five tabs; a notebook that uses the same code.
- [ ] Experiment records for every number quoted in the documentation.
- [ ] `UPDATE_LOG.md`, README and bibliography updated.

## 6. Proposals that need a decision

These are suggestions beyond the brief. None of them will be implemented
without a decision.

| # | Proposal | Why |
|---|---|---|
| P1 | A two-angle or inertial sandpile (experiment E12) | Tests the crossover from scale-free to periodic avalanches; tied to the "angle of drainage" question |
| P2 | A random-field Ising module (experiment E11) | A tuned-criticality control for every SOC claim |
| P3 | Continuous integration (GitHub Actions) running the fast tests on Windows, macOS and Linux | Catches platform-specific failures |
| P4 | A licence | Without one, others may read the code but not reuse it |
| P5 | A lock file for exact environments | Makes bitwise reproduction easier |
