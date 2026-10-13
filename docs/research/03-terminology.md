# 03 · Terminology: two ambiguous phrases and the BTW conventions

Version 00 research notes. The brief asked for two expressions to be checked
rather than assumed: "angle of drainage periodic function" and "self
sustained criticality". It also asked for the original Bak–Tang–Wiesenfeld
(BTW) model to be separated from the Abelian sandpile and from other variants
wherever the difference matters. The searches were made on 2026-10-13. The
BTW rules below are quoted from the original papers (BTW 1987, 1988), not
from secondary descriptions, because secondary sources disagree with each
other.

## 1. "Angle of drainage periodic function"

### What was searched

- The exact phrase, and "angle of drainage" together with "periodic
  function".
- "Angle of drainage" together with sandpile, granular and self-organized
  criticality.
- "Drained angle of repose", "drainage angle", and the Turkish
  "drenaj açısı".
- Related phenomena: periodic avalanches at the angle of repose, rotating
  drums, inertial sandpile automata, hourglass flow, branching angles of
  stream networks.

### Result

No source uses the phrase, or "angle of drainage" by itself, as a technical
term in physics or mathematics. I could not identify a recognized concept
under this name, and the lab does not invent one. Several established
concepts contain parts of the phrase. They are listed below, roughly from
most to least plausible as the intended meaning.

### Candidate readings

**1. BTW's own picture: the angle of repose, the outflow of sand, and pendula
that turn by one period.** *Established; primary source.* In the 1988 paper
that introduced SOC in full, Bak, Tang and Wiesenfeld describe building a
pile grain by grain until "the slope will reach a critical value (called the
'angle of repose')". The quantity they say shows $1/f$ noise "is simply the
flow of the sand falling off the pile (this is analogous to the situation in
an hour glass)". The same model "can be thought of as a model of a sand pile,
or alternatively as modeling an array of coupled pendula". In the 1987 paper
the motivating system is a chain of damped pendula with angles $u_n$
connected by torsion springs, whose metastable states have $u_n\approx2\pi N$
with $N$ an integer. The gravitational torque on a pendulum is a
$2\pi$-periodic function of its angle (our gloss; the papers do not use the
phrase "periodic function"), and an unstable site corresponds to a pendulum
that "rotates one revolution" (BTW 1988). The cellular variable "may be thought of as the force
on an individual pendulum, or the local slope of the sand pile (the 'hour
glass')" (BTW 1987). This reading accounts for all three words, an angle
(repose angle or pendulum angle), drainage (sand flowing off the pile, the
hourglass) and periodicity (rotation through a full period). It points
straight at the founding papers. In the lab it is the BTW model itself, with
the outflow of grains at the boundary as an observable. Note that the $1/f$
claim attached to that outflow did not survive: the flow of sand in the BTW
automaton has a $1/f^2$ power spectrum (Jensen, Christensen & Fogedby 1989).

**2. Real sandpiles: the slope oscillates between two angles.** *Established
physics.* A real pile driven slowly, by tilting it or by turning it in a
drum, does not stay at one critical slope. Its surface angle grows until it
reaches the maximum angle of stability $\theta_m$; a large avalanche then
brings it down to the angle of repose $\theta_r<\theta_m$, and the cycle
repeats (Jaeger, Liu & Nagel 1989; Evesque & Rajchenbach 1989; reviewed by
Nagel 1992). In an idealized form, for a drum turning at angular speed
$\Omega$,

```math
\theta(t) = \theta_r + \big(\Omega t \bmod (\theta_m-\theta_r)\big),
\qquad \text{period } T=\frac{\theta_m-\theta_r}{\Omega},
```

a periodic sawtooth function of time **[heuristic; in experiments $\theta_m$
fluctuates from one avalanche to the next]**. The gap $\theta_m-\theta_r$ is
usually a few degrees (Aranson & Tsimring 2006). This hysteresis is the main
reason ordinary sand does not show BTW-type SOC. Adding inertia to sandpile
automata can likewise destroy the self-organized critical state (Prado &
Olami 1992; Head & Rodgers 1997). Piles of elongated rice grains, on the
other hand, do show power-law avalanches (Frette et al. 1996). Jensen,
Christensen & Fogedby (1989) note that the flow over the rim of the BTW
automaton behaves like the transport Jaeger, Liu and Nagel measured.

**3. The "drained" angle of repose.** *Established term in powder and
bulk-solids technology.* It is measured on the conical surface that remains
in a flat-bottomed container after the material has flowed out through an
orifice in its base, and it is distinguished from the "poured" angle of a
heap built by pouring. I found this definition in secondary sources
(bulk-solids handbook excerpts) rather than in a standard. Measured angles of
repose depend on the method (Beakawi Al-Hashemi & Baghabra Al-Amoudi 2018).
Nothing periodic is involved. Relevance to the lab: indirect.

**4. Drainage networks and their branching angles.** *Established
(geomorphology).* River networks are a standard example of self-organization
(Rinaldo et al. 1992, 1993; Rodríguez-Iturbe & Rinaldo 1997). Streams fed by
groundwater branch at a characteristic angle $2\pi/5=72^\circ$; the mean of
about 5,000 measured junctions in Florida is $71.9^\circ\pm0.8^\circ$
(Devauchelle et al. 2012). Branching angles also vary with climate (Seybold,
Rothman & Kirchner 2017). There is no standard "periodic function" here.

**5. Periodicity inside the Abelian sandpile.** *Exact.* The boundary drains
grains into the sink. Adding grains again and again at one site cycles
through the recurrent configurations with a period equal to the order of the
addition operator $a_i$ in the sandpile group (Dhar 1990). For the
$3\times3$ grid the period is 224 at a corner and 16 at the centre (computed
here by `scripts/verify_numbers.py`). This is a precise sense in which
sandpile dynamics is periodic, but I found no source that connects it with an
angle.

**6. Periodic boundary conditions and periodic states in the OFC model.**
*Established.* With periodic boundaries the homogeneous
Olami–Feder–Christensen model becomes periodic and neutrally stable; with
open boundaries a self-organized region invades the interior (Middleton &
Tang 1995; see also Socolar, Grinstein & Jayaprakash 1993). The "drainage" would be
the dissipation $\alpha<1/4$.

**7. Granular drainage through an orifice: ticking hourglasses.**
*Established.* In a range of parameters the flow of sand out of an hourglass
is oscillatory, because the sand flow couples to air convection through the
grains (Wu et al. 1993). An
hourglass flow measurement (Schick & Verveen 1974) is one of the $1/f$
examples BTW cite.

**8. A phase angle with a periodic coupling function.** *Established.* In the
Kuramoto model the coupling $\sin(\theta_j-\theta_i)$ is a $2\pi$-periodic
function of the difference of two phase angles. This is already in the
portfolio.

**9. The "drainage angle" of the eye.** *Established medical term* for the
iridocorneal angle, through which aqueous humour drains. Unrelated.

### Assessment and what the lab does with it

Readings 1 and 2 are the most plausible, and a blend of them fits the phrase
best: the angle of repose (BTW's threshold slope), the sand that drains off
the pile (BTW's hourglass analogy), and periodicity (the pendulum turning
through a full period, or real piles avalanching periodically between two
angles). Reading 1 is literally in the founding papers; reading 2 is the
experimental counterpoint to them.

Concretely:

- the sandpile module records the outflow at the boundary as a time series
  and reports its power spectrum next to the avalanche statistics;
- an experiment on the crossover from scale-free to periodic avalanches (a
  pile with two angles, or with inertia) is listed as a proposal in the
  [experiments notes](05-experiments-and-open-questions.md), not as planned
  work;
- if the phrase came from a specific lecture, book or video, that source
  decides which reading is meant.

## 2. "Self-sustained criticality"

### What was searched

The exact phrase, and the phrase together with neuronal avalanches and
self-organized criticality.

### Result

The phrase is used mainly in nuclear engineering, where a reactor is
"critical" when its fission chain reaction is exactly self-sustaining: each
fission produces on average one further fission, $k_{\mathrm{eff}}=1$. I
found no definition of "self-sustained criticality" in the complex-systems
literature, and it is not a synonym of self-organized criticality.

### How it relates to branching processes and to SOC

The nuclear meaning is the critical case of a branching process. For a
Galton–Watson process with mean offspring $m$ (the analogue of
$k_{\mathrm{eff}}$):

| Regime | Behaviour | Status |
|---|---|---|
| $m<1$, subcritical | $P(Z_n>0)\le m^n$: activity dies out exponentially fast | **[proven]** |
| $m=1$, critical | dies out with probability 1, but $P(Z_n>0)\sim2/(\sigma^2n)$ and the total progeny has a tail $P(S=n)\sim n^{-3/2}/(\sigma\sqrt{2\pi})$ | **[proven]** (Athreya & Ney 1972; Dwass 1969) |
| $m>1$, supercritical | survives forever with positive probability $1-q$ | **[proven]** |

Self-organized criticality (BTW 1987, 1988) is a different statement: it is
about the stationary state of a slowly driven, spatially extended system. Its
mean-field avalanches are critical branching processes (Alstrøm 1988), and
models exist in which dissipation drives the branching ratio towards 1
(Zapperi, Lauritsen & Stanley 1995). So "self-sustained criticality" reads
like a mix of "self-organized criticality" and "self-sustaining (critical)
chain reaction". The two meet at $m=1$, but they are not the same concept.

### Established terms in the neighbourhood

| Term | Meaning | Source |
|---|---|---|
| Self-organized criticality | Slow drive and threshold relaxation lead to a critical stationary state without tuning (beyond the separation of time scales) | BTW 1987, 1988; Pruessner 2012 |
| Critical branching | Mean offspring exactly 1 | Harris 1963; Athreya & Ney 1972 |
| Self-organized quasi-criticality | Non-conservative systems that hover around, but not at, a critical point | Bonachela & Muñoz 2009 |
| Self-organized bistability | The analogue of SOC for a first-order (discontinuous) transition | di Santo et al. 2016 |
| Griffiths phases | Extended critical-like regions caused by quenched heterogeneity | Moretti & Muñoz 2013 |
| Tuned criticality | A parameter (temperature, coupling) is set to its critical value | Any equilibrium transition |
| Self-sustained oscillations or activity | Persistent oscillations (limit cycles) or activity without external input; not a statement about criticality | Dynamical-systems usage |

**Recommendation.** Use "self-organized criticality" for the BTW concept and
"critical branching" for $m=1$. Avoid "self-sustained criticality" unless it
is defined in the text that uses it.

## 3. BTW, the Abelian sandpile and related variants

### 3.1 What BTW actually specified

**The 1987 letter (BTW 1987).** "In two dimensions $z$ is updated
synchronously as follows:"

```math
z(x,y)\to z(x,y)-4,\qquad z(x\pm1,y)\to z(x\pm1,y)+1,\qquad z(x,y\pm1)\to z(x,y\pm1)+1,
```

"if $z$ exceeds a critical value $K$. There are no parameters since a shift
in $K$ simply shifts $z$. Fixed boundary conditions are used, i.e., $z=0$ on
boundaries." The procedure was not slow driving: "The system is set up with
random initial conditions $z\gg K$, and then simply evolves until it stops",
after which "the dynamics is then probed by measurement of the response of
the resulting state to small local random perturbations". Cluster sizes were
obtained "simply by our counting the number of affected sites generated from
a seed at one site and averaging over many arrays".

**The 1988 paper (BTW 1988).**

- *One dimension.* $z_n=h(n)-h(n+1)$ is a height difference. Adding sand at
  $n$ means $z_n\to z_n+1$, $z_{n-1}\to z_{n-1}-1$. When $z_n>z_c$:
  $z_n\to z_n-2$, $z_{n\pm1}\to z_{n\pm1}+1$. The left end is closed
  ($z_0=0$) and the right end open. The 1D model is "a trivial critical
  state with no spatial patterns": it relaxes to the single minimally
  stable state.
- *Two dimensions.* Adding a unit is rule (3.1),
  $z(x-1,y)\to z(x-1,y)-1$, $z(x,y-1)\to z(x,y-1)-1$, $z(x,y)\to z(x,y)+2$,
  a change of *slopes*. Toppling is rule (3.2): $z(x,y)\to z(x,y)-4$ and
  $+1$ for each of the four neighbours, when $z(x,y)>z_c$. The authors stress
  that $z$ is a "slope" in the diagonal direction and that they "are
  interested in the general behavior of nonlinear diffusion dynamics such as
  Eq. (3.2), and not in sand piles, per se."
- *"Closed" boundaries:* $z(0,y)=z(x,0)=z(N+1,y)=z(x,N+1)=0$. In the
  $z$ variable this is dissipative on all four sides; "closed" refers to sand
  not leaving the box in the slope picture. Two protocols: (a) relax from
  $z>z_c$ everywhere, then perturb each minimally stable site ($z=z_c$) by
  applying (3.2) there, count the "slidings", restore the original state and
  move to the next site; (b) start flat and add $z(x,y)\to z(x,y)+1$
  (rule 3.8) at random positions, relaxing after each addition. The size
  distribution of (b) was "indistinguishable" from that of (a).
- *"Open" boundaries:* particles leave at the two edges $x=N$ and $y=N$,
  with modified rules $z(N,y)\to z(N,y)-3$, $z(x,N)\to z(x,N)-3$,
  $z(N,N)\to z(N,N)-2$; the drive is rule (3.1); the recorded signal is "the
  flow $f(t)$ of sand that falls off the edges of the box".
- *Observables:* size $s$ = total number of slidings; lifetime $T$; a
  lifetime distribution "weighted by the average response $s/T$"; the power
  spectrum of the superposed dissipation signal.
- *Reported numbers:* $\tau\approx1.0$ in 2D ($0.98$ in 1987) and $1.37$ in
  3D; lifetime exponents giving spectra $f^{-1.57}$ (2D) and $f^{-1.08}$ (3D)
  in the closed case and $f^{-0.95}$ for the open-edge flow. These early
  values came from $50\times50$ and $75\times75$ lattices and coarse-grained
  histograms. They are not comparable with modern estimates unless the
  definitions match.

### 3.2 Dhar's Abelian sandpile

Dhar (1990) defined the model on any finite set of sites with a toppling
matrix $\Delta$:

```math
\Delta_{jj}>0,\qquad \Delta_{jk}\le 0\ (j\neq k),\qquad \sum_k\Delta_{jk}\ge0,
\qquad z\ \mapsto\ z-\Delta e_j\quad\text{whenever } z_j\ge\Delta_{jj},
```

with strict inequality in the row sums at enough sites ("dissipative" sites
connected to every other site) for every avalanche to stop. On the
$L\times L$ square grid, $\Delta_{jj}=4$ and $\Delta_{jk}=-1$ for neighbours;
the row sums are 1 at edge sites and 2 at corners, the grains lost to the
sink. Grains are added at random sites, one at a time, and the system relaxes
completely between additions.

The two height conventions in use are stable heights $0,1,2,3$ (topple at
$z\ge4$) and $1,2,3,4$ (topple at $z>4$). They differ by a shift of 1, so the
mean height on $\mathbb{Z}^2$ is $17/8$ in one convention and $25/8$ in the
other.

### 3.3 What the differences change

| Choice | BTW 1987/1988 | Abelian sandpile (Dhar 1990) | What it affects |
|---|---|---|---|
| Update order | Synchronous | Any order; the result does not depend on it | Durations and temporal profiles only. Final configurations, sizes and areas are order-independent (Abelian property) |
| Drive and measurement | Perturbations of relaxed states with restoration (1987; 1988 protocol a); random addition (1988 protocol b); slope addition (1988, open case) | Random single-grain addition, full relaxation in between | The ensemble of states that is probed; only random addition samples the stationary measure |
| Boundaries | "Closed": $z=0$ outside, so $z$ leaves on all four sides; "open": two edges with modified rules | Sink attached to boundary sites, usually on all four sides, nowadays called "open" | Everything. The names are reversed between the two conventions |
| Variable | Slope, force on a pendulum | Number of grains (height) | Interpretation only |
| Threshold | $z>K$ or $z>z_c$, arbitrary shift | $z_j\ge\Delta_{jj}$ | Nothing, after a shift |
| Avalanche size | Slidings (1988); "affected sites" (1987 wording) | Topplings $s$; area $a$ = distinct toppled sites | Exponents and moments; $s\ge a$ |

### 3.4 Other variants and why they matter

| Variant | What changes | Consequence |
|---|---|---|
| Manna (1991); Dhar (1999) | Random destinations for toppled grains | Different universality class; clean scaling |
| Oslo (Christensen et al. 1996) | 1D, random thresholds | Genuinely critical in one dimension |
| Zhang (1989) | Continuous energies, non-Abelian | Different scaling theory |
| OFC (Olami, Feder & Christensen 1992) | Continuous and non-conservative | Criticality contested; synchronization |
| Directed sandpile (Dhar & Ramaswamy 1989) | Grains move in one preferred direction | Exactly solvable |
| Kadanoff et al. (1989) | Local, non-local, limited and unlimited 1D slope rules | Exponents depend on the rule |
| Fixed-energy sandpiles (Vespignani et al. 2000) | Torus, no drive, no dissipation | An absorbing-state transition in the density |

Not every avalanche model is self-organized critical: the 1D BTW model is
trivial, OFC is contested, and the forest-fire model violates simple
scaling.

### 3.5 The lab's conventions for the sandpile module

- **Reference model:** Dhar's formulation with heights $0$ to $3$, threshold 4,
  and a sink attached to the boundary.
- **Options, all recorded in every run:**
  - update scheme: sequential (stack or queue) or synchronous as in BTW;
  - drive: random addition, fixed-site addition, or the BTW 1987
    perturbation of relaxed states with restoration;
  - boundary sinks chosen per side, which includes BTW's 1988 "open on two
    edges" case.
- **Observables:** size, area, duration in synchronous steps, number of
  waves, and grains lost to the sink per avalanche (the outflow).

## 4. Other terms that are easy to confuse

| Term | Meanings that get mixed up | Convention in this lab |
|---|---|---|
| Critical | (a) at a continuous phase transition; (b) branching ratio exactly 1; (c) the critical slope or angle of a pile; (d) a critical mass or reactor | Always say which |
| Power law, scale-free, heavy-tailed | A power law $P(s)\propto s^{-\tau}$ is one heavy tail among many (log-normal, stretched exponential, truncated power law). "Scale-free" in network science means a power-law degree distribution | Claim a power law only after the model comparison of the [experiments notes](05-experiments-and-open-questions.md) |
| Mean-field | Single-site approximation; exact all-to-all solution; $N\to\infty$ limit equation; Landau theory | State which (see the [field map](01-field-map.md#mean-field-theory-means-four-different-things)) |
| Universality | Same exponents and scaling functions, not "same behaviour" | Compare universal quantities only |
| Renormalization | Exact decimation; approximate real-space RG; perturbative field theory; rigorous RG | Label the status every time |
| Phase transition | A singularity of the infinite system; finite systems only show smooth crossovers | Say "finite-size crossover" for a finite simulation |
| Emergence | Weak emergence (derivable in principle) versus strong | Weak emergence only |
| Self-organization | Pattern formation without external imposition; not necessarily critical | Never used as a synonym for SOC |
| Chaos, randomness, complexity | Deterministic sensitivity; stochasticity; structure that is neither periodic nor random | Kept apart |
| Ergodicity | Time averages equal ensemble averages; broken in the infinite system below $T_c$, and effectively broken in long but finite runs | Report run lengths and autocorrelation times |
| Detailed balance, stationarity | Detailed balance implies stationarity, not conversely | Stated per algorithm |
| Avalanche size, area, duration | Topplings; distinct sites; time steps (scheme-dependent) | Always all three, with definitions |
| $1/f$ noise | A spectrum $S(f)\propto f^{-\beta}$ with $\beta$ near 1; which signal is meant matters | Name the signal and fit $\beta$ |
