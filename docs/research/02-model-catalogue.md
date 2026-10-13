# 02 · Model catalogue

Version 00 research notes. Candidate models, grouped by family, with what is
known about each of them, what can be measured, which exact results can
validate an implementation, and the usual pitfalls. The evidence labels are
defined in the [field map](01-field-map.md#evidence-labels). Numbers marked
"computed here" are recomputed by
[`scripts/verify_numbers.py`](../../scripts/verify_numbers.py).

Scales used in the entries and in the comparison table:

- **Difficulty** (1–5): 1 is a short, self-contained implementation; 3 needs
  careful numerics or statistics; 5 needs research-level care or long
  development.
- **Cost**: the computing effort to get publishable-quality statistics on an
  ordinary laptop. *Low* means seconds to minutes; *medium* means minutes to
  hours with compiled kernels; *high* means hours or more, or memory near the
  limit of a laptop.
- **Value**: mathematical substance plus the number of connections to the
  central themes of the lab (criticality, mean-field limits, renormalization,
  self-organization).

## A. Self-organized criticality and avalanche dynamics

### A1. Bak–Tang–Wiesenfeld sandpile and the Abelian sandpile model

- **State.** Stable configurations
  $z\in\lbrace0,1,2,3\rbrace^\Lambda$ on $\Lambda=\lbrace1,\dots,L\rbrace^2$,
  plus a sink vertex that receives every grain leaving the boundary.
- **Rule (Dhar's formulation).** Add a grain at a uniformly chosen site,
  $z_i\mapsto z_i+1$. While some site has $z_j\ge4$, topple it:
  $z_j\mapsto z_j-4$ and each of its four lattice neighbours gains one grain;
  grains sent outside $\Lambda$ are lost to the sink. On a general graph,
  toppling site $j$ is $z\mapsto z-\Delta e_j$, where the toppling matrix
  $\Delta$ is the graph Laplacian with the sink's row and column removed.
- **How the original BTW model differs.** Synchronous updating, a "slope"
  interpretation of $z$, measurements of the response of relaxed states to
  single perturbations, and boundary conventions whose names are the reverse
  of today's. Details in
  [terminology §3](03-terminology.md#3-btw-the-abelian-sandpile-and-related-variants).
- **Algebra and combinatorics.**
  - Abelian property: the final stable configuration and the number of
    topplings at every site do not depend on the order in which unstable
    sites are toppled **[proven: Dhar 1990]**.
  - The addition operators $a_i$ commute and generate a finite abelian group
    (the sandpile group) that acts freely and transitively on recurrent
    configurations; its order is $\det\Delta$. The stationary distribution of
    the driven chain is uniform on recurrent configurations
    **[proven: Dhar 1990]**.
  - Recurrence is decided by the burning algorithm, which also gives a
    bijection between recurrent configurations and spanning trees
    **[proven: Dhar 1990; Majumdar & Dhar 1992]**.
  - The expected number of topplings at $j$ caused by a grain added at $i$,
    averaged over the stationary state, is $(\Delta^{-1})_{ij}$
    **[proven: Dhar 1990]**. So the mean avalanche size is an explicit
    Green's-function sum and grows like $L^2$.
- **Exact numbers.**
  - On $\mathbb{Z}^2$, with heights written as $1,\dots,4$:
    $P(1)=2/\pi^2-4/\pi^3\approx0.0736$ **[exact: Majumdar & Dhar 1991]**;
    $P(2)\approx0.1739$, $P(3)\approx0.3063$, $P(4)\approx0.4462$ (closed
    forms from Priezzhev 1994, partly conjectural at the time; integrated
    exactly by Caracciolo & Sportiello 2012). The mean height is $25/8$
    **[proven: Poghosyan, Priezzhev & Ruelle 2011; Kenyon & Wilson 2015]**.
    The four values and their mean are checked here.
  - Recurrent configurations on the open $L\times L$ grid: 4, 192, 100352,
    557568000 for $L=1,2,3,4$ (computed here as $\det\Delta$).
    $L^{-2}\log\det\Delta$ tends to $4G/\pi\approx1.1662$, with $G$ Catalan's
    constant (the spanning-tree entropy of $\mathbb{Z}^2$); at $L=48$ it is
    still 1.177 (computed here), a reminder of how slowly boundary effects
    fade.
  - Repeatedly adding grains at one site cycles through recurrent
    configurations with a period equal to the order of $a_i$ in the group:
    224 for a corner and 16 for the centre of the $3\times3$ grid, 6600 for
    the $4\times4$ grid (computed here).
- **Mathematical frontier.** The pattern grown from a single source has a
  scaling limit **[proven: Pegden & Smart 2013]** with Apollonian structure
  **[proven: Levine, Pegden & Smart 2016, 2017]**; surveys: Járai 2018;
  Levine & Peres 2017.
- **Avalanche observables.** Size $s$ (number of topplings), area $a$
  (distinct sites toppled), duration $T$ (number of parallel update steps),
  linear extent, grains lost to the sink.
  - In two dimensions the exponents are not known exactly, and simple
    finite-size scaling fails; moment analysis shows multifractal scaling
    **[numerical: De Menech, Stella & Tebaldi 1998; Tebaldi, De Menech &
    Stella 1999]**. A proposed exact $\tau=6/5$ (Priezzhev, Ktitarev &
    Ivashkevich 1996) is not settled.
  - Avalanches decompose into waves of topplings whose statistics are
    exactly computable **[exact: Ivashkevich, Ktitarev & Priezzhev 1994;
    Ktitarev et al. 2000]**.
  - Mean-field exponents ($\tau=3/2$ for sizes, $2$ for durations) are
    expected above $d_c=4$ **[heuristic and numerical]**.
- **Pitfalls.** Mixing size, area and duration; boundary-dominated statistics
  on small lattices; transients from the initial configuration; parallel
  versus sequential durations; the one-dimensional BTW model is trivial (it
  relaxes to the single "minimally stable" state, BTW 1988).
- **Assessment.** Difficulty 2/5. Cost low to medium. Value very high: the
  richest exact structure of any SOC model, together with open questions.

### A2. Manna model

- **Rule.** A site holding at least two particles is active. A toppling moves
  two particles out of it, each to a neighbour chosen independently and
  uniformly. Manna's original two-state version (1991) moves all the particles
  of a doubly occupied site; Dhar (1999) studied the two-particle version and
  its Abelian property in distribution.
- **Behaviour.** Manna (conserved directed percolation) class; avalanche
  observables show clean finite-size scaling **[numerical: Lübeck 2004]**.
  Whether this class differs from directed percolation in one dimension is
  **[contested: Basu et al. 2012; Lee 2014]**.
- **Assessment.** Difficulty 2/5. Cost low to medium. Value high, as a
  contrast with BTW: same conservation and threshold, stochastic toppling,
  clean scaling.

### A3. Oslo model

- **Rule.** A one-dimensional pile of columns $h_1,\dots,h_L$ with slopes
  $z_i=h_i-h_{i+1}$ and $h_{L+1}=0$. Grains are added at the closed left
  end ($z_1\mapsto z_1+1$). Each site has a threshold $z_i^c\in\lbrace1,2\rbrace$.
  If $z_i>z_i^c$ the site relaxes: in the bulk $z_i\mapsto z_i-2$ and
  $z_{i\pm1}\mapsto z_{i\pm1}+1$; at $i=1$ only $z_2$ gains; at $i=L$ the
  grain leaves the system ($z_L\mapsto z_L-1$, $z_{L-1}\mapsto z_{L-1}+1$).
  After each relaxation a new threshold is drawn, usually each value with
  probability $1/2$.
- **Behaviour.** Clean finite-size scaling with $\tau\approx1.55$ and
  avalanche cutoff $s_c\sim L^{D}$, $D\approx2.25$ **[numerical: Christensen
  et al. 1996; Pruessner 2012]**; Manna class **[numerical]**. Designed after
  rice-pile experiments (Frette et al. 1996).
- **Assessment.** Difficulty 1/5. Cost low. Value high: genuinely SOC in one
  dimension (unlike the 1D BTW model), cheap, and ideal for learning data
  collapse.

### A4. Olami–Feder–Christensen (OFC) model

- **Rule.** Continuous forces $F_i\in[0,F_{th})$ on an $L\times L$ lattice are
  driven uniformly until the largest one reaches the threshold. An unstable
  site resets to zero and adds $\alpha F_i$ to each of its four neighbours,
  $0<\alpha\le1/4$; $\alpha=1/4$ conserves force and smaller $\alpha$
  dissipates.
- **Behaviour.** Whether the dissipative model is critical is
  **[contested]**. Power-law-like statistics appear with open boundaries
  (Olami, Feder & Christensen 1992; Lise & Paczuski 2001), but they are
  boundary-driven. With periodic boundaries the homogeneous model becomes
  periodic; open boundaries let a self-organized region invade the interior
  through synchronization of neighbouring sites (Middleton & Tang 1995; see
  also Socolar, Grinstein & Jayaprakash 1993). Bonachela & Muñoz (2009) argue
  that the model is self-organized *quasi*-critical.
- **Mapping.** A lattice of pulse-coupled integrate-and-fire oscillators
  (Corral et al. 1995).
- **Assessment.** Difficulty 2/5 (event-driven updating needs care). Cost
  medium. Value high: it connects SOC, conservation and synchronization.

### A5. Galton–Watson branching process: the mean-field avalanche

- **Definition.** $Z_0=1$ and $Z_{n+1}=\sum_{k=1}^{Z_n}\xi_{n,k}$ with
  independent offspring numbers of generating function
  $f(x)=\mathbb{E}x^{\xi}$ and mean $m=f'(1)$.
- **Exact results.**
  - The extinction probability is the smallest root of $f(q)=q$ in $[0,1]$;
    it equals 1 if and only if $m\le1$, except in the trivial case
    $P(\xi=1)=1$ **[proven: Harris 1963; Athreya & Ney 1972]**.
  - At $m=1$ with finite variance $\sigma^2$: $P(Z_n>0)\sim2/(\sigma^2n)$
    **[proven: Kolmogorov's estimate, see Athreya & Ney 1972]**, so the
    duration exponent is 2.
  - Total progeny: $P(S=n)=\frac1n P(\xi_1+\dots+\xi_n=n-1)$
    **[proven: Dwass 1969]**. With a local limit theorem this gives
    $P(S=n)\sim n^{-3/2}/(\sigma\sqrt{2\pi})$ at criticality (aperiodic
    offspring). For Poisson(1) offspring $S$ has the Borel distribution
    $P(S=n)=e^{-n}n^{n-1}/n!$; $n^{3/2}\sqrt{2\pi}P(S=n)\to1$ is checked here.
- **Role.** The exactly solvable reference against which "a power law at a
  critical point" can be tested with everything known. Self-organized
  branching processes let dissipation tune $m$ towards 1 (Zapperi, Lauritsen
  & Stanley 1995).
- **Assessment.** Difficulty 1/5. Cost low. Value high as a mean-field
  companion to A1.

### A6. Forest-fire model

- **Rule.** Sites are empty, tree or burning. Trees grow on empty sites with
  probability $p$ and lightning strikes a tree with probability $f$. In the
  Drossel–Schwabl limit $f\ll p\ll1$ the struck tree's whole cluster burns
  at once (Drossel & Schwabl 1992); Bak, Chen & Tang (1990) used fire
  propagation instead.
- **Behaviour.** Claimed to be SOC; large simulations show violations of
  simple scaling **[numerical: Grassberger 2002]**.
- **Assessment.** Difficulty 2/5. Cost medium. Value medium: a lesson in how
  scaling claims fail, and a link to percolation.

### A7. Bak–Sneppen model

- **Rule.** Sites on a ring carry fitnesses in $[0,1]$. At each step the
  minimum and its two neighbours receive new uniform random values.
- **Behaviour.** Extremal dynamics. Almost all fitnesses end above a threshold
  near $0.667$ in one dimension **[numerical: Bak & Sneppen 1993; Paczuski,
  Maslov & Bak 1996]**; rigorous results on thresholds and limit
  distributions exist **[proven: Meester & Znamenski 2003, 2004]**.
- **Assessment.** Difficulty 1/5. Cost low. Value medium.

### A8. Fixed-energy sandpiles

- **Rule.** The toppling rules of A1 or A2 on a torus with no drive and no
  dissipation. The control parameter is the particle density $\zeta$, and
  there is an absorbing-state transition at a threshold density
  **[numerical: Vespignani et al. 2000]**.
- **A sharp result.** For the deterministic rule on $\mathbb{Z}^2$, the
  stationary density of the driven–dissipative sandpile is exactly
  $17/8=2.125$ (heights $0$ to $3$), while the threshold density of the
  fixed-energy sandpile is $2.125288$ to six decimals
  **[numerical: Fey, Levine & Wilson 2010]**. They differ, against a widely
  used assumption of the absorbing-state picture of SOC.
- **Assessment.** Difficulty 2/5. Cost medium. Value high for research
  questions.

## B. Statistical mechanics and phase transitions

### B1. Ising model

- **State and energy.** $\sigma\in\lbrace-1,+1\rbrace^\Lambda$ on an
  $L\times L$ torus, with the Hamiltonian of the
  [field map](01-field-map.md#order-parameters-and-phase-transitions).
- **Exact results in two dimensions.**
  - $T_c=2J/(k_B\ln(1+\sqrt2))\approx2.269185\ J/k_B$ **[proven: Onsager
    1944; Kramers & Wannier 1941 located it by duality]**.
  - $m^{\ast}=(1-\sinh^{-4}(2\beta J))^{1/8}$ below $T_c$ **[proven: Yang 1952]**.
  - Exponents $\alpha=0$ (logarithmic), $\beta=1/8$, $\gamma=7/4$,
    $\delta=15$, $\nu=1$, $\eta=1/4$ **[exact; several proven]**.
  - Exact partition functions of finite tori **[exact: Kaufman 1949;
    Ferdinand & Fisher 1969]** and the exact density of states
    **[Beale 1996]**.
  - Binder-cumulant value at $T_c$ on the square torus $U^{\ast}\approx0.6107$
    **[exact: Salas & Sokal 2000; high-precision numerics: Kamieniarz &
    Blöte 1993]**.
  - Conformal invariance **[proven: Smirnov 2010; Chelkak, Hongler & Izyurov
    2015]**.
- **Mean-field companions.** Curie–Weiss self-consistency
  $m=\tanh(\beta(zJm+h))$ gives $T_c^{\mathrm{MF}}=zJ/k_B=4J/k_B$; the Bethe
  approximation gives $T_c=2J/(k_B\ln(z/(z-2)))=2J/(k_B\ln2)\approx2.885\ J/k_B$
  **[approx on $\mathbb{Z}^2$; exact on the complete graph and the Bethe
  lattice respectively]**.
- **Dynamics.** Metropolis (Metropolis et al. 1953), Glauber or heat bath
  (Glauber 1963), Swendsen–Wang (1987) and Wolff (1989) cluster updates. All
  sample the same Gibbs measure and differ as dynamics. Local updates suffer
  critical slowing down with dynamic exponent $z\approx2.17$
  **[numerical: Nightingale & Blöte 1996]**; cluster algorithms largely
  remove it.
- **Observables.** Energy; magnetization and $\lvert m\rvert$; specific heat
  and susceptibility from fluctuations; the Binder cumulant
  $U_4=1-\langle m^4\rangle/(3\langle m^2\rangle^2)$; the correlation function
  and the second-moment correlation length; integrated autocorrelation times;
  Fortuin–Kasteleyn cluster sizes.
- **Validation anchors.** Exact enumeration of the $2^{16}$ states of the
  $4\times4$ torus; the Kaufman and Ferdinand–Fisher formulas for any $L$;
  Onsager and Yang in the limit; detailed balance checked exactly on tiny
  systems.
- **Assessment.** Difficulty 2/5 (Metropolis) to 3/5 (cluster algorithms and
  error analysis). Cost medium. Value essential.

### B2. Potts model

- **Definition.** $q$ states per site and
  $H=-J\sum_{\langle i,j\rangle}\delta(\sigma_i,\sigma_j)$. The random-cluster
  representation joins $q=1$ (percolation), $q=2$ (Ising) and $q\to0$
  (spanning trees, hence sandpiles) (Fortuin & Kasteleyn 1972; Wu 1982).
- **Known in two dimensions.** Critical point at the self-dual value
  $\beta_cJ=\ln(1+\sqrt q)$ for $q\ge1$ **[proven: Beffara & Duminil-Copin
  2012]**; the transition is continuous for $1\le q\le4$ **[proven:
  Duminil-Copin, Sidoravicius & Tassion 2017]** and discontinuous for $q>4$
  **[proven: Duminil-Copin et al. 2021]**.
- **Assessment.** Difficulty 2/5. Cost medium. Value medium-high: how
  symmetry changes universality, and a first-order transition for contrast.

### B3. Percolation

- **Definition.** Each site (or bond) is open independently with
  probability $p$.
- **Exact results.**
  - Bond percolation on $\mathbb{Z}^2$: $p_c=1/2$ **[proven: Kesten 1980]**.
  - Site percolation on the triangular lattice: $p_c=1/2$
    **[proven; see Grimmett 1999]**.
  - Site percolation on $\mathbb{Z}^2$: $p_c\approx0.59274621(13)$
    **[numerical: Newman & Ziff 2000]**.
  - Exponents in two dimensions: $\nu=4/3$, $\beta=5/36$, $\gamma=43/18$,
    fractal dimension $91/48$, Fisher exponent $\tau=187/91$ **[exact;
    proven for site percolation on the triangular lattice: Smirnov & Werner
    2001]**.
  - Cardy's crossing formula **[exact: Cardy 1992; proven on the triangular
    lattice: Smirnov 2001]**.
- **Algorithm.** Newman–Ziff union–find covers every $p$ in one sweep
  (Newman & Ziff 2000, 2001).
- **Renormalization demonstration.** Three-site majority blocks on the
  triangular lattice give $p'=p^3+3p^2(1-p)$, with fixed point $p^{\ast}=1/2$
  (exact) and $\nu=\ln\sqrt3/\ln(3/2)\approx1.355$ against the exact $4/3$
  (computed here).
- **Assessment.** Difficulty 1/5. Cost low. Value very high: the cleanest
  place to learn finite-size scaling and real-space RG.

### B4. Contact process and directed percolation

- **Rule.** Each infected site recovers at rate 1 and infects each neighbour
  at rate $\lambda$.
- **Results.** A non-trivial $\lambda_c$ exists in every dimension
  **[proven: Harris 1974; Liggett 1985, 1999]**. In one dimension
  $\lambda_c\approx1.6489$ in this convention, that is $3.2978$ when
  $\lambda$ denotes the total infection rate **[numerical; see Hinrichsen
  2000]**. The rate equation $\dot\rho=\lambda z\rho(1-\rho)-\rho$ gives
  $\lambda_c=1/z$ **[approx]**, far from the one-dimensional value.
  Directed-percolation class **[conjecture, strongly supported]**.
- **Assessment.** Difficulty 2/5 (continuous-time simulation needs care).
  Cost medium. Value high: the paradigm of absorbing-state transitions and
  the companion of fixed-energy sandpiles.

## C. Mean-field theory: microscopic model and limit equation side by side

The brief asks for microscopic simulations next to their mean-field
predictions. These pairs are the most instructive, because in each the
mean-field equation is either a theorem in some limit or a clearly stated
approximation.

| Microscopic model | Mean-field object | Status | What the comparison teaches |
|---|---|---|---|
| Ising on $\mathbb{Z}^2$ | Curie–Weiss and Bethe self-consistency | **[approx]** on the lattice | $T_c$: 4 (mean field) and 2.885 (Bethe) against 2.269; wrong exponents in $d=2$ |
| Curie–Weiss with $N$ spins under heat-bath dynamics | $\dot m=-m+\tanh(\beta(Jm+h))$ | **[proven]** as $N\to\infty$ on finite times (Kurtz-type) | Finite $N$: switching between $\pm m^{\ast}$ over times exponential in $N$ |
| SIS or contact process on a lattice | $\dot\rho=\lambda z\rho(1-\rho)-\rho$ | **[approx]**; the pair approximation is better | Spatial correlations move $\lambda_c$ and change exponents |
| SIS on a complete graph | The same logistic ODE | **[proven]** (Kurtz 1970) | Finite $N$: quasi-stationary state and extinction after times exponential in $N$ |
| Kuramoto with $N$ oscillators | Ott–Antonsen ODE (Lorentzian); self-consistency equation (general $g$) | **[proven/exact]** as $N\to\infty$ | Fluctuations at finite $N$; how the sampling of frequencies changes finite-size scaling |
| Sandpile avalanches | Critical branching process | **[heuristic]**; exact on trees and expected for $d\ge d_c$ | $\tau=3/2$ against two-dimensional values; what spatial correlations do |
| Individual-based predator–prey | Lotka–Volterra ODE | **[proven]** LLN (Kurtz) | Demographic noise sustains cycles that the ODE does not have (McKane & Newman 2005) |

The assumptions that turn a microscopic model into a mean-field equation are
always some of the following. Each model specification states which ones it
uses:

1. **Factorization or closure**: $P(\sigma_i,\sigma_j)=P(\sigma_i)P(\sigma_j)$
   (single-site), or a closure of pair correlations in terms of triples
   (pair approximation).
2. **Homogeneity**: all sites are equivalent, so one density describes the
   system.
3. **Large-number limit**: fluctuations of order $N^{-1/2}$ are neglected.
4. **Exchangeability** of components (all-to-all coupling).
5. **Separation of time scales** (adiabatic elimination of fast variables).

## D. Renormalization group and scale dependence

The Ising model is the case study, surrounded by examples in which the
renormalization step is exact, controlled or merely illustrative.

| Example | What is computed | Status |
|---|---|---|
| Decimation of the 1D Ising chain ($b=2$) | $\tanh K'=\tanh^2K$; fixed points only at $K=0$ (stable) and $K=\infty$; a flow from $K=2$ reaches $0.32$ after five steps (computed here) | **[proven]**, exact |
| Majority-rule block spins on 2D Ising configurations | Pictures at successive scales; renormalized observables; effective couplings by matching correlations, or by Swendsen's Monte Carlo RG (Swendsen 1979, 1984) | **[numerical]**; the renormalized measure may be non-Gibbsian (Griffiths & Pearce 1979; van Enter, Fernández & Sokal 1993) |
| Migdal–Kadanoff bond moving, $d=2$, $b=2$ | $\tanh K'=\tanh^2(2K)$; $K^{\ast}\approx0.3047$ against the exact $0.4407$; $\nu\approx1.34$ against 1 (computed here) | **[approx]**, uncontrolled in $d=2$ (Kadanoff 1976) |
| Cell RG for triangular site percolation | $p^{\ast}=1/2$ exact, $\nu\approx1.355$ against $4/3$ | **[approx]** with an exact fixed point |
| Period doubling for unimodal maps | Feigenbaum constants $\delta\approx4.6692$, $\alpha\approx2.5029$ | **[proven, computer-assisted: Lanford 1982]** |
| Finite-size scaling and Binder crossings | $T_c$ and exponents from crossings and data collapse | **[numerical]**; phenomenological RG |

A block-spin picture that "looks critical" at every scale is a demonstration.
A quantitative RG statement needs a defined map on couplings, a fixed point,
its linearization, and an error analysis of the truncation.

## E. Cellular automata and emergent behaviour

### E1. Game of Life

- **Rule.** Two states on $\mathbb{Z}^2$, Moore neighbourhood, birth on
  exactly 3 live neighbours, survival on 2 or 3 (B3/S23).
- **Established.** Still lifes, oscillators and spaceships (the glider moves
  one cell diagonally every four generations); computational universality
  **[proven constructively: Berlekamp, Conway & Guy 1982; Rendell 2016]**.
  Universality implies that the eventual fate of a pattern is undecidable in
  general.
- **Not established by pictures.** Typical long-time densities and decay laws
  from random initial conditions are **[numerical]** observations.
- **Assessment.** Difficulty 1/5. Cost low. Value medium (strong for
  computation and decidability, weak for statistical physics).

### E2. Elementary cellular automata (Rules 30, 90, 110, 184)

- **Rule.** Two states, nearest neighbours, synchronous update; the rule
  number encodes the new state for the 8 neighbourhoods (Wolfram 1983).
- **Rule 90** is $x_i'=x_{i-1}\oplus x_{i+1}$, linear over $\mathbb{F}_2$;
  from a single live cell it draws Pascal's triangle modulo 2
  **[proven, elementary]**.
- **Rule 30** is $x_i'=x_{i-1}\oplus(x_i\vee x_{i+1})$. Whether its centre
  column is non-periodic, balanced, or computable faster than by simulation
  are open problems (Wolfram's 2019 Rule 30 prizes).
- **Rule 110** is Turing universal **[proven: Cook 2004]**.
- **Rule 184** conserves the number of ones and is a minimal traffic model.
- **Classifications.** Wolfram's four classes (Wolfram 1984) are
  **[heuristic]**; Langton's $\lambda$ parameter and the "edge of chaos"
  thesis (Langton 1990) are **[contested]** (Mitchell, Hraber & Crutchfield
  1993). Rigorous theory: Hedlund (1969), Kari (2005), Ceccherini-Silberstein
  & Coornaert (2010).
- **Assessment.** Difficulty 1/5. Cost low. Value medium-high: the cleanest
  place to separate proven facts from pictures.

### E3. Domany–Kinzel automaton

- **Rule.** A probabilistic one-dimensional automaton whose two parameters
  give the probability that a site becomes active with one or two active
  parents (Domany & Kinzel 1984). Its phase transition is in the
  directed-percolation class **[numerical; DP conjecture]**.
- **Assessment.** Difficulty 1/5. Cost low. Value high as the simplest
  absorbing-state model.

## F. Synchronization and collective dynamics

### F1. Kuramoto model

- **Equations.** $\dot\theta_i=\omega_i+\frac KN\sum_{j=1}^N\sin(\theta_j-\theta_i)$
  with natural frequencies drawn from a density $g$. The order parameter
  $re^{i\psi}=\frac1N\sum_je^{i\theta_j}$ turns the equations into
  $\dot\theta_i=\omega_i+Kr\sin(\psi-\theta_i)$: each oscillator feels only
  the mean field.
- **Results.**
  - For a symmetric unimodal $g$, incoherence loses stability at
    $K_c=2/(\pi g(0))$ (Kuramoto 1975; Strogatz 2000) **[exact as
    $N\to\infty$; rigorous bifurcation analysis: Chiba 2015]**. For a
    Gaussian of standard deviation $\sigma$,
    $K_c=\sqrt{8/\pi}\ \sigma\approx1.596\ \sigma$ (computed here).
  - For a Lorentzian of half-width $\Delta$, the Ott–Antonsen reduction gives
    $\dot r=-\Delta r+\frac K2r(1-r^2)$, so $r=\sqrt{1-2\Delta/K}$ for
    $K>K_c=2\Delta$ **[exact on the Ott–Antonsen manifold: Ott & Antonsen
    2008, 2009]**.
  - A uniform $g$ gives a discontinuous transition (Pazó 2005).
  - Below $K_c$, the fluctuations of $r$ at finite $N$ are of order $N^{-1/2}$
    (Daido 1990); the finite-size scaling at $K_c$ depends on how frequencies
    are sampled, with exponent $\bar\nu=5/2$ for random sampling
    **[numerical and analytical: Hong et al. 2007, 2015]**. Identical
    oscillators reduce to three dimensions **[proven: Watanabe & Strogatz
    1994]**. The incoherent state relaxes by Landau damping below threshold
    (Strogatz, Mirollo & Matthews 1992).
- **Assessment.** Difficulty 2/5. Cost low. Value very high: the cleanest
  example of an exact mean-field limit, with a genuine bifurcation.

### F2. Vicsek model

- **Rule.** Particles with positions $x_i$ and headings $\theta_i$ move at
  constant speed $v_0$. At each step each heading becomes the mean heading of
  the particles within distance $R$, plus noise of amplitude $\eta$.
  Order parameter: $\varphi=\lvert\frac1N\sum_ie^{i\theta_i}\rvert$.
- **Results.** Originally reported as a continuous transition (Vicsek et al.
  1995); large systems show a discontinuous transition with travelling bands
  **[numerical: Grégoire & Chaté 2004; Chaté et al. 2008; Solon, Chaté &
  Tailleur 2015]**. Hydrodynamic theory predicts true long-range order in two
  dimensions **[approx/RG: Toner & Tu 1995, 1998]**. Reviews: Vicsek &
  Zafeiris 2012; Ginelli 2016.
- **Assessment.** Difficulty 2/5 (neighbour search). Cost medium. Value high
  as non-equilibrium order with a famous correction to the original claim.

### F3. Boids

- Separation, alignment and cohesion rules from computer graphics
  (Reynolds 1987). Useful as an intuitive contrast; it has no standard order
  parameter or phase diagram. Difficulty 1/5. Value low to medium.

### F4. Synchronization on networks

- Kuramoto oscillators on Erdős–Rényi, small-world and scale-free graphs;
  the master stability function for identical systems (Pecora & Carroll
  1998); explosive synchronization when frequencies correlate with degrees
  (Gómez-Gardeñes et al. 2011). Reviews: Arenas et al. 2008; Dörfler & Bullo
  2014; Rodrigues et al. 2016. Difficulty 3/5. Value high, after F1.

### F5. Pulse-coupled oscillators

- Integrate-and-fire oscillators with excitatory pulses synchronize for
  almost all initial conditions **[proven: Mirollo & Strogatz 1990]**; the
  bridge to OFC (A4). Difficulty 2/5. Value medium-high.

## G. Reaction–diffusion systems and spatial self-organization

### G1. Turing instability (general two-species analysis)

- **Equations.** $u_t=f(u,v)+D_u\nabla^2u$, $v_t=g(u,v)+D_v\nabla^2v$,
  homogeneous steady state with Jacobian entries $f_u,f_v,g_u,g_v$.
- **Conditions.** The steady state is stable without diffusion
  ($f_u+g_v<0$, $f_ug_v-f_vg_u>0$) and unstable to a band of wavenumbers with
  diffusion when

```math
D_vf_u+D_ug_v>0\quad\text{and}\quad(D_vf_u+D_ug_v)^2>4D_uD_v\,(f_ug_v-f_vg_u),
```

  with critical wavenumber $k_c^2=\sqrt{(f_ug_v-f_vg_u)/(D_uD_v)}$ at onset
  **[proven: linear stability, e.g. Murray 2003]**. Concrete systems:
  Schnakenberg, Brusselator, Gierer–Meinhardt (1972).
- **Assessment.** Difficulty 2/5. Cost low to medium. Value high: the
  canonical derivation of self-organization without criticality.

### G2. Gray–Scott model

- **Equations.** $u_t=D_u\nabla^2u-uv^2+F(1-u)$,
  $v_t=D_v\nabla^2v+uv^2-(F+k)v$ (Gray & Scott 1983, 1984). Pearson (1993)
  mapped the $(F,k)$ plane into spots, stripes, self-replicating spots and
  other regimes **[numerical]**.
- **Numerics.** Explicit Euler with the five-point Laplacian is stable for
  the diffusion part only if $\Delta t\le\Delta x^2/(4D_{\max})$ in two
  dimensions **[proven for the heat equation by von Neumann analysis]**;
  semi-implicit and spectral methods are the alternatives.
- **Assessment.** Difficulty 3/5 (stability, boundary conditions, long
  transients). Cost medium. Value high.

### G3. Excitable media

- FitzHugh–Nagumo (FitzHugh 1961; Nagumo et al. 1962) and Barkley's fast
  model (Barkley 1991): travelling pulses, spiral waves, refractoriness.
  Difficulty 3/5. Value medium-high.

## H. Networks and agent-based systems

- **Erdős–Rényi $G(n,p)$.** With $p=c/n$ a giant component exists if and only
  if $c>1$, and its fraction solves $S=1-e^{-cS}$ **[proven: Erdős & Rényi
  1960]**. Difficulty 1/5.
- **Watts–Strogatz.** A ring lattice with rewiring probability $p$; short
  paths with high clustering for small $p$ **[numerical: Watts & Strogatz
  1998]**. Difficulty 1/5.
- **Barabási–Albert.** Preferential attachment; degree distribution
  $P(k)\sim k^{-3}$ **[proven: Bollobás et al. 2001]**. How common scale-free
  networks are in data is **[contested: Broido & Clauset 2019; Holme 2019]**.
  Difficulty 1/5.
- **Epidemics on networks.** Heterogeneous mean-field threshold
  $\lambda_c=\langle k\rangle/\langle k^2\rangle$ for SIS
  **[approx: Pastor-Satorras & Vespignani 2001]**; SIR with a fixed
  infectious period maps onto bond percolation (Grassberger 1983; Newman
  2002). Review: Pastor-Satorras et al. 2015. Difficulty 2/5.
- **Schelling segregation.** Two types of agents on a grid with vacancies;
  an agent is unhappy if the fraction of like neighbours is below a
  threshold, and unhappy agents move (Schelling 1971). Rigorous results in
  one dimension (Brandt et al. 2012); physical analogues (Vinković & Kirman
  2006; Grauwin et al. 2009). Difficulty 1/5. Value medium-high as the
  standard example of "emergent versus imposed".

Network models add NetworkX as a dependency and graph drawing, which is slow
for large graphs. They belong after the core modules.

## I. The additional models of the brief, ranked

Scores are 1–5. For difficulty, 1 means easiest.

| Rank | Model | Mathematical value | Conceptual diversity | Difficulty | Link to central themes | Why |
|---|---|---|---|---|---|---|
| 1 | Logistic map, bifurcation diagram, period doubling | 5 | 5 | 1 | 4 | Rigorous chaos theory (Li & Yorke 1975; Jakobson 1981; Lyubich 2002) and the one place where an RG fixed point is a theorem (Feigenbaum 1978; Lanford 1982) |
| 2 | Random walks and Lévy flights | 4 | 3 | 1 | 5 | Green's functions and loop-erased walks underlie the exact sandpile results; diffusion; first passage; anomalous diffusion (Metzler & Klafter 2000), with a contested application to foraging (Viswanathan et al. 1999; Edwards et al. 2007) |
| 3 | Lotka–Volterra, deterministic and individual-based | 4 | 4 | 2 | 5 | A structurally unstable ODE with a conserved quantity; Kurtz's theorem; demographic noise and quasi-cycles (McKane & Newman 2005); Gillespie's algorithm |
| 4 | Reaction–diffusion and activator–inhibitor models | 4 | 5 | 3 | 4 | Self-organization without criticality; Turing analysis (G1, G2) |
| 5 | Information-theoretic measures | 3 | 3 | 3 | 4 | A cross-cutting analysis layer; estimators are biased, which is itself instructive |
| 6 | Forest-fire and extremal models | 3 | 2 | 2 | 4 | Close to the sandpile; mainly a lesson about failed scaling (A6, A7) |
| 7 | Lorenz system | 4 | 3 | 2 | 2 | Sensitive dependence and a computer-assisted existence proof (Tucker 1999, 2002), but no many-body aspect |

## J. Candidates the brief did not list

| Model | Why it would add something | Key references |
|---|---|---|
| Oslo model (A3) | The cleanest SOC model for finite-size scaling | Christensen et al. 1996; Pruessner 2012 |
| Random-field Ising model at zero temperature | Avalanches and hysteresis at a *tuned* critical point: the control experiment for "self-organized versus tuned" | Sethna et al. 1993; Sethna, Dahmen & Myers 2001 |
| Domany–Kinzel automaton (E3) | The simplest directed-percolation model | Domany & Kinzel 1984; Hinrichsen 2000 |
| Voter model | Exactly solvable through duality with coalescing random walks; consensus in $d\le2$, coexistence in $d\ge3$ **[proven]** | Clifford & Sudbury 1973; Holley & Liggett 1975 |
| XY model and the BKT transition | A topological transition without long-range order; the equilibrium relative of Kuramoto and Vicsek | Kosterlitz & Thouless 1973; Mermin & Wagner 1966 |
| Eden, ballistic deposition, KPZ | Non-equilibrium growth with exact fluctuation results (Tracy–Widom) | Family & Vicsek 1985; Kardar, Parisi & Zhang 1986; Johansson 2000; Hairer 2013; Takeuchi & Sano 2010 |
| TASEP | Exactly solvable non-equilibrium steady states and boundary-driven transitions | Derrida, Evans, Hakim & Pasquier 1993 |
| DLA, internal DLA, rotor-router, chip-firing | Laplacian growth; the mathematical neighbours of sandpiles | Witten & Sander 1981; Lawler, Bramson & Griffeath 1992; Holroyd et al. 2008; Priezzhev et al. 1996; Levine & Peres 2017 |
| Random Boolean networks | "Criticality" in gene-network models; the annealed approximation gives critical connectivity $K=2$ for unbiased functions **[approx]** | Kauffman 1969; Derrida & Pomeau 1986 |
| Coupled map lattices | Spatiotemporal chaos and intermittency from coupled logistic maps | Kaneko 1985 |
| Swift–Hohenberg and complex Ginzburg–Landau equations | The normal forms of pattern formation | Swift & Hohenberg 1977; Cross & Hohenberg 1993; Aranson & Kramer 2002 |
| Kinetic Ising with conserved dynamics (Kawasaki) | Coarsening and phase-ordering kinetics | Bray 1994 |
| Spatial evolutionary games | Cooperation sustained by spatial structure | Nowak & May 1992 |
| Hopfield network | Statistical mechanics of associative memory | Hopfield 1982 |

## K. Comparison table

| Model | Family | Dynamics | Key observables | Exact anchor for validation | Difficulty | Cost | Value |
|---|---|---|---|---|---|---|---|
| BTW / Abelian sandpile | SOC | Threshold automaton, random drive | Sizes, areas, durations; heights | $\det\Delta$, burning test, height probabilities, $\langle s\rangle$ from $\Delta^{-1}$ | 2 | Low–med | Very high |
| Manna | SOC | Stochastic toppling | As above; FSS | Conservation; scaling collapse | 2 | Low–med | High |
| Oslo | SOC | 1D, random thresholds | Sizes; FSS; height profile | Conservation; scaling collapse | 1 | Low | High |
| OFC | SOC / sync | Continuous, dissipative | Sizes; synchronization | $\alpha=1/4$ conservative limit; periodic state with periodic boundaries | 2 | Med | High |
| Galton–Watson branching | Stochastic | Generations | Extinction; progeny; duration | Fixed point of $f$; Borel law; $n^{-3/2}$ | 1 | Low | High |
| Forest fire | SOC | Growth, lightning | Fire sizes | Percolation limits | 2 | Med | Medium |
| Bak–Sneppen | SOC | Extremal | Threshold, avalanches | Rigorous threshold bounds | 1 | Low | Medium |
| Fixed-energy sandpile | Absorbing states | Closed toppling | Activity versus density | $\zeta_s=17/8$ against $\zeta_c\approx2.125288$ | 2 | Med | High |
| Ising | Equilibrium SM | MCMC | $E$, $m$, $C$, $\chi$, $U_4$, $G(r)$ | Enumeration; Kaufman; Onsager; Yang | 2–3 | Med | Essential |
| Potts | Equilibrium SM | MCMC | As Ising; latent heat | Self-dual $\beta_c$ | 2 | Med | Med–high |
| Percolation | Geometry | Static | $R_L(p)$, $P_\infty$, $n_s$ | $p_c=1/2$ (bond, square); exact 2D exponents | 1 | Low | Very high |
| Contact process / DP | Absorbing states | Continuous-time Markov | Density, survival, spreading | Mean-field limit; DP exponents | 2 | Med | High |
| Curie–Weiss | Mean field | Exact / Glauber | $m(T,h)$, switching times | Self-consistency theorem | 1 | Low | High |
| Kuramoto | Synchronization | ODE | $r(t)$, $r(K)$, locked fraction | $K_c=2/(\pi g(0))$; Ott–Antonsen | 2 | Low | Very high |
| Vicsek | Collective motion | Discrete-time particles | $\varphi(\eta,\rho)$, bands | Noise-free and no-alignment limits | 2 | Med | High |
| Game of Life | CA | Deterministic CA | Density, objects | Known periodic objects | 1 | Low | Medium |
| ECA 30/90/110/184 | CA | Deterministic CA | Patterns, entropy | Rule 90 linearity; conservation in 184 | 1 | Low | Med–high |
| Gray–Scott | Pattern formation | PDE | Fields, spectra | Homogeneous steady states; linear stability | 3 | Med | High |
| Turing (two species) | Pattern formation | PDE | Wavelength, growth rate | Dispersion relation | 2 | Low–med | High |
| Networks (ER/WS/BA) | Networks | Graph growth | Degree distribution, giant component | $S=1-e^{-cS}$; $k^{-3}$ | 1 | Low | Medium |
| SIS / SIR on networks | Epidemics | Markov on graph | Prevalence, final size | Complete-graph limit; percolation mapping | 2 | Med | High |
| Schelling | ABM | Agent moves | Segregation indices | 1D rigorous results | 1 | Low | Med–high |
| Logistic map | Nonlinear dynamics | Map | Bifurcations, Lyapunov exponent | Feigenbaum constants; period-3 window | 1 | Low | Very high |
| Lorenz | Nonlinear dynamics | ODE | Lyapunov exponents, attractor | Fixed points and their stability | 2 | Low | Medium |
| Lotka–Volterra | Nonlinear / stochastic | ODE and Gillespie | Cycles, extinction | Conserved quantity of the ODE | 2 | Low | High |
| Random walks, Lévy flights | Stochastic | Markov chain | Displacement, first passage | Exact moments; Pólya recurrence | 1 | Low | High |
| RFIM at $T=0$ | Disorder, avalanches | Deterministic relaxation | Hysteresis loops, avalanches | Mean-field solution | 3 | Med | High |
| Voter model | Interacting particles | Markov | Consensus time, interfaces | Duality | 1 | Low | Medium |
| XY / BKT | Equilibrium SM | MCMC | Helicity modulus, vortices | Mermin–Wagner: no magnetization at $T>0$ | 3 | Med–high | High |
| KPZ / Eden | Growth | Stochastic growth | Roughness exponents | Exact 1D exponents | 2 | Med | High |

## L. Recommendation in one paragraph

The portfolio in the [roadmap](../plan/roadmap.md#2-the-first-three-modules)
starts with three models that differ in kind but share one theme, the
passage from microscopic rules to macroscopic laws: the Abelian sandpile with
its branching-process mean field (self-organized, threshold dynamics), the
Ising model with Curie–Weiss and Bethe (tuned, equilibrium, stochastic) and
the Kuramoto model with Ott–Antonsen (deterministic, synchronization). Each
has exact results strong enough to validate an implementation, and each has
an exactly solvable mean-field companion. Percolation and the logistic map
follow as the most valuable cheap additions, because they make finite-size
scaling and renormalization concrete before the block-spin experiments.
