# 05 · Experiments, open questions and misconceptions

Version 00 research notes. These are the experiments the laboratory is built
to run, the open problems close enough to reach from it, and the
misconceptions it should help to avoid. Evidence labels as in the
[field map](01-field-map.md#evidence-labels).

## 1. How an experiment is run in this lab

Every experiment follows the same protocol. The experiment panel of the app
and the command-line runner will both enforce it.

1. **Question and hypothesis, written before running.** Include a
   prediction that could fail, for example "the mean height in the bulk
   converges to $17/8$ and the deviation decays at least like $1/L$".
2. **Configuration.** Model, parameters, system sizes, boundary and initial
   conditions, update order, time unit, number of replicas, root seed. All of
   it is stored in a configuration file under version control.
3. **Equilibration or transient removal.** The criterion is stated (for
   example, discard the first $20\tau_{\mathrm{int}}$ sweeps, or the first
   $10L^2$ grains).
4. **Measurement with uncertainty.** Independent replicas from spawned seeds;
   binning or blocking for correlated time series; bootstrap or jackknife for
   derived quantities.
5. **Comparison with theory.** Exact values, mean-field predictions or
   published numerical values, with their conventions.
6. **Sensitivity.** At least one change of system size, and where relevant of
   boundary conditions, update order and seed.
7. **Conclusion with its evidence label.** What is supported, what is merely
   consistent, what remains speculative.

### Claiming a power law

Straight lines on log–log plots are not evidence (Clauset, Shalizi & Newman
2009; Stumpf & Porter 2012). The lab uses this procedure, and a power-law
claim must survive all of it:

1. **Estimate by maximum likelihood**, for discrete data with the discrete
   likelihood, above a lower cutoff $s_{\min}$ chosen by minimizing the
   Kolmogorov–Smirnov distance (Clauset, Shalizi & Newman 2009); report the
   fitting range explicitly. With an upper cutoff, use a truncated power law
   (Deluca & Corral 2013).
2. **Goodness of fit** by a parametric bootstrap of the KS statistic.
3. **Compare with alternatives** (log-normal, exponential, stretched
   exponential, power law with exponential cutoff) by likelihood ratios with
   the Vuong correction for non-nested models.
4. **Uncertainty**: bootstrap confidence intervals for the exponent and for
   $s_{\min}$.
5. **Finite-size scaling**: in a critical system the cutoff must grow with
   $L$. Use data collapse $P(s;L)=s^{-\tau}\mathcal{G}(s/L^{D})$ and moment
   analysis $\langle s^q\rangle\sim L^{\sigma(q)}$, with $\sigma(q)$ linear in
   $q$ for simple scaling (De Menech, Stella & Tebaldi 1998; Pruessner 2012).
6. **State what is not shown**: a good power-law fit over two decades does
   not establish criticality, let alone SOC (Touboul & Destexhe 2017).

## 2. Experiments, in roughly the order the modules make them possible

### E1. Exact sandpile statistics as a test of the simulation

- **Question.** Does the simulated stationary state of the Abelian sandpile
  reproduce the exact height probabilities $P(h)$ on $\mathbb{Z}^2$ and the
  exact count of recurrent configurations?
- **Method.** Burning-test every configuration of the $2\times2$ and
  $3\times3$ grids and compare the counts with $\det\Delta=192$ and $100352$.
  Measure height frequencies in a central window of $L\times L$ lattices for
  increasing $L$ and compare with $P(1),\dots,P(4)$. Measure the mean number
  of topplings at $j$ caused by additions at $i$ and compare with
  $(\Delta^{-1})_{ij}$.
- **Known answer.** **[proven]** values (Dhar 1990; Majumdar & Dhar 1991;
  Poghosyan, Priezzhev & Ruelle 2011; Kenyon & Wilson 2015).
- **What it teaches.** How finite-size and boundary effects decay, and how
  slowly; how to attach honest error bars to correlated samples.

### E2. BTW versus Manna versus Oslo versus a critical branching process

- **Question.** Which avalanche statistics obey simple finite-size scaling?
- **Method.** Moment analysis $\sigma(q)$ for sizes, areas and durations;
  data collapse; the size–duration relation
  $\langle s\rangle(T)\sim T^{\gamma}$ and the consistency relation
  $\gamma=(\alpha-1)/(\tau-1)$ between exponents.
- **Expected.** Clean scaling for Manna and Oslo, multifractal moments for
  the 2D BTW model **[numerical]**, exact $\tau=3/2$ and duration exponent 2
  for the branching process **[proven]**.
- **Why it matters.** It shows that "SOC" is not one universality class, and
  it makes the mean-field limit concrete.

### E3. Does the sandpile organize to the absorbing-state threshold?

- **Question.** Compare the stationary density of the driven–dissipative
  sandpile ($17/8$ on $\mathbb{Z}^2$, heights $0$ to $3$) with the threshold
  density of the fixed-energy sandpile on tori of increasing size.
- **Known.** They differ: $2.125288$ against $2.125$ **[numerical: Fey,
  Levine & Wilson 2010]**.
- **Research angle.** Reproduce the difference, then explore other graphs and
  the stochastic (Manna) rule. This is a research-level experiment.

### E4. The outflow signal and the $1/f$ claim

- **Question.** What is the power spectrum of the number of grains leaving
  the system per unit time, and of the toppling activity?
- **Expected.** $1/f^2$ for the flow of sand (Jensen, Christensen & Fogedby
  1989); $1/f^{\alpha}$ with $\alpha<2$ tied to the size–duration exponent for
  avalanche activity (Laurson, Alava & Zapperi 2005).
- **Why it matters.** It tests the original BTW claim with the observable BTW
  used, the sand falling off the pile, and it is the observable behind one
  reading of "angle of drainage" (see the
  [terminology notes](03-terminology.md)).

### E5. Ising: from exact enumeration to Onsager

- **Question.** Do Metropolis, heat-bath and Wolff dynamics reproduce exact
  finite-lattice values and extrapolate to the exact critical point?
- **Method.** Exact enumeration for $L\le4$; Kaufman/Ferdinand–Fisher values
  for larger $L$; Binder-cumulant crossings and data collapse with
  $\nu=1$, $\gamma/\nu=7/4$, $\beta/\nu=1/8$.
- **Expected.** Agreement within error bars; $U^{\ast}\approx0.6107$ at the
  crossing **[exact]**; integrated autocorrelation times growing like
  $L^{z}$ with $z\approx2.17$ for local dynamics **[numerical]** and far more
  slowly for Wolff.
- **What it teaches.** The difference between the equilibrium measure (one
  answer) and the dynamics used to sample it (several speeds).

### E6. Mean-field versus microscopic Ising

- **Question.** Where does Curie–Weiss theory fail on $\mathbb{Z}^2$, and how
  much does the Bethe approximation recover?
- **Method.** Compare $m(T)$, $\chi(T)$ and $T_c$ (4, 2.885 and 2.269) for
  the lattice model, the complete-graph model with $N$ spins, and the two
  self-consistency equations; then compare the complete-graph simulation with
  its exact $N\to\infty$ limit.
- **What it teaches.** That mean-field theory is exact for one model and an
  approximation for another, and that the difference is fluctuations.

### E7. Block-spin renormalization: a demonstration and its limits

- **Question.** What does majority-rule coarse-graining do to Ising
  configurations above, at and below $T_c$, and how far can effective
  couplings be estimated?
- **Method.** Coarse-grain configurations by blocks of $2\times2$ or
  $3\times3$; compare renormalized observables (magnetization, Binder
  cumulant, nearest-neighbour correlation) with those of a directly simulated
  smaller lattice; estimate effective couplings by matching correlations and
  by Swendsen's method; trace the flow away from and towards $K_c$.
- **Controls.** The exact 1D decimation; Migdal–Kadanoff's recursion
  ($K^{\ast}\approx0.3047$ against $0.4407$); the triangular percolation cell
  ($p^{\ast}=1/2$ exactly, $\nu\approx1.355$ against $4/3$).
- **Caveat stated in the results.** The renormalized measure may be
  non-Gibbsian (Griffiths & Pearce 1979; van Enter, Fernández & Sokal 1993).

### E8. Kuramoto: theory, finite size and the sampling of frequencies

- **Question.** How close does a population of $N$ oscillators get to the
  $N\to\infty$ theory, and how does the answer depend on $g$ and on how
  frequencies are sampled?
- **Method.** $r(K)$ for Lorentzian $g$ against $\sqrt{1-2\Delta/K}$; for
  Gaussian $g$ against the numerical solution of the self-consistency
  equation; for uniform $g$, look for the discontinuity (Pazó 2005). Compare
  random sampling of the $\omega_i$ with deterministic quantile sampling, and
  measure the fluctuations of $r$ below $K_c$ as a function of $N$.
- **Expected.** $K_c=2/(\pi g(0))$; fluctuations of order $N^{-1/2}$ below
  $K_c$; finite-size scaling that depends on the sampling (Hong et al. 2007,
  2015; Ottino-Löffler & Strogatz 2016).

### E9. Universality, tested

- **Question.** Do two microscopically different models have the same
  critical exponents?
- **Method.** Ising on the square and on the triangular lattice (same class,
  different $T_c$); 3-state Potts (different class); bond and site
  percolation (same class, different $p_c$).
- **What it teaches.** What exactly "universal" means and which quantities
  are not universal.

### E10. Power-law skepticism

- **Question.** How often does a naive log–log fit "find" a power law in data
  that has none?
- **Method.** Generate log-normal, stretched-exponential, truncated and
  mixture samples of realistic size; run naive regression and the full
  procedure of Section 1.
- **What it teaches.** The size of the problem, measured rather than asserted.

### E11. Self-organized versus tuned avalanches

- **Question.** Can the avalanche statistics of an SOC model be told apart
  from those of a system tuned to a critical point, such as the zero-temperature
  random-field Ising model at its critical disorder (Sethna et al. 1993)?
- **Status.** A proposal; it needs the RFIM module, which is not planned yet.

### E12. From scale-free to periodic avalanches (proposal)

- **Question.** What happens to the sandpile when each site has two
  thresholds, a starting slope and a stopping slope, mimicking the maximum
  angle of stability and the angle of repose of real sand?
- **Expected.** A crossover from scale-free avalanches to quasi-periodic
  system-spanning ones as the gap grows, as in experiments (Jaeger, Liu &
  Nagel 1989) and inertial automata (Prado & Olami 1992; Head & Rodgers
  1997).
- **Status.** A proposal connected to the "angle of drainage" reading;
  nothing is implemented before the question of what the phrase meant is
  settled.

## 3. Open questions within reach of the lab

| Question | Status | Sources |
|---|---|---|
| Exact avalanche exponents of the 2D BTW model, and the right scaling theory for its multifractal statistics | Open; $\tau=6/5$ proposed | Priezzhev, Ktitarev & Ivashkevich 1996; Tebaldi, De Menech & Stella 1999 |
| Is the Manna class different from directed percolation in one dimension? | **[contested]** | Basu et al. 2012; Lee 2014 |
| When does a driven–dissipative sandpile sit exactly at the threshold of its fixed-energy version? | Answered negatively for many graphs; the general picture is open | Fey, Levine & Wilson 2010 |
| Is the non-conservative OFC model critical? | **[contested]** | Middleton & Tang 1995; de Carvalho & Prado 2000; Bonachela & Muñoz 2009 |
| Exact critical exponents of the 3D Ising model | Open; conformal bootstrap gives very precise values | Kos et al. 2016 |
| A rigorous renormalization group for block spins | Open in general; known pathologies | Griffiths & Pearce 1979; van Enter, Fernández & Sokal 1993 |
| Theory of the Kuramoto transition at finite $N$ | Partly understood | Hong et al. 2007, 2015; Ottino-Löffler & Strogatz 2016 |
| Rule 30: non-periodicity, balance and cost of computing its centre column | Open | Wolfram 2019 |
| Is the brain near a critical point, and of which kind? | **[contested]** | Beggs & Plenz 2003; Wilting & Priesemann 2019; Muñoz 2018 |
| How common are scale-free networks in data? | **[contested]** | Broido & Clauset 2019; Holme 2019 |

## 4. Common misconceptions this lab should prevent

1. **"A straight line on a log–log plot proves a power law."** It does not
   (Section 1).
2. **"A power law proves criticality, and criticality proves SOC."** Neither
   step holds (Touboul & Destexhe 2017).
3. **"Every sandpile is self-organized critical."** The 1D BTW model is
   trivial; the forest-fire model fails simple scaling; real sand has two
   angles and periodic avalanches.
4. **"SOC needs no tuning."** It needs vanishing driving and dissipation
   rates: a separation of time scales.
5. **"BTW showed that SOC produces $1/f$ noise."** The sand flow of their
   model has a $1/f^2$ spectrum.
6. **"Mean-field theory is a crude approximation."** It is exact for
   complete graphs, above the upper critical dimension and in many
   $N\to\infty$ limits; it is wrong for low-dimensional critical behaviour.
   Both statements are theorems in the right setting.
7. **"Monte Carlo dynamics is the physical dynamics."** Metropolis and Wolff
   sample the same equilibrium and differ completely as dynamics.
8. **"Block spins at $T_c$ prove scale invariance."** They illustrate it.
9. **"A finite simulation shows a phase transition."** It shows a crossover
   whose sharpening with $L$ is the evidence.
10. **"Complex-looking automata are computationally universal."** Only proofs
    show that (Cook 2004 for Rule 110).
11. **"Information processing peaks at criticality."** Not in general
    (Barnett et al. 2013).
12. **"Self-organization means criticality."** Turing patterns, flocking and
    synchronization are self-organized and not critical.
