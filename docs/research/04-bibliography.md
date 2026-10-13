# 04 · Bibliography

Version 00 research notes. Part 1 is a short annotated list to start from.
Part 2 lists every work cited in the research notes, grouped by topic.

**How the entries were checked (2026-10-13).** Every DOI below was looked up
in the Crossref registry, and its title, authors, journal, volume and pages
were compared with the entry; entries that did not match were corrected.
arXiv identifiers were checked on arxiv.org, and web links were opened.
Nothing was added from memory without such a check.
[`scripts/check_references.py`](../../scripts/check_references.py) repeats
the DOI check. The two BTW papers were read in full; for most other papers
the notes rely on abstracts, reviews and standard textbook accounts, as the
annotations say.

Kinds of source: **P** primary research paper, **R** review or survey,
**T** textbook or monograph, **M** rigorous mathematics, **C** critique or
correction of an earlier claim, **W** free web resource.

## Part 1 · Shortlist

### Where to start

1. **Pruessner, G. (2012).** *Self-Organised Criticality: Theory, Models and
   Characterisation.* Cambridge University Press.
   [doi:10.1017/CBO9780511977671](https://doi.org/10.1017/CBO9780511977671)
   — T. The most careful book on SOC: definitions, models (BTW, Manna, Oslo,
   OFC, forest fire), numerical methods, moment analysis, and an honest
   account of what is and is not established.
2. **Járai, A. A. (2018).** Sandpile models. *Probability Surveys* 15,
   243–306. [doi:10.1214/14-PS228](https://doi.org/10.1214/14-PS228),
   [arXiv:1401.0354](https://arxiv.org/abs/1401.0354) — R, M. Rigorous survey
   of the Abelian sandpile: group structure, burning algorithm, spanning
   trees, infinite-volume limits. Free.
3. **Dhar, D. (2006).** Theoretical studies of self-organized criticality.
   *Physica A* 369, 29–70.
   [doi:10.1016/j.physa.2006.04.004](https://doi.org/10.1016/j.physa.2006.04.004)
   — R. Review by the author of the Abelian formulation; exact results and
   their limits.
4. **Friedli, S. & Velenik, Y. (2017).** *Statistical Mechanics of Lattice
   Systems: A Concrete Mathematical Introduction.* Cambridge University Press.
   [doi:10.1017/9781316882603](https://doi.org/10.1017/9781316882603);
   [free online version](https://www.unige.ch/math/folks/velenik/smbook/)
   — T, M. Rigorous statistical mechanics for mathematicians: Curie–Weiss,
   Ising, Gibbs measures, Peierls argument, correlation inequalities.
5. **Sethna, J. P. (2021).** *Statistical Mechanics: Entropy, Order
   Parameters, and Complexity*, 2nd ed. Oxford University Press.
   [doi:10.1093/oso/9780198865247.001.0001](https://doi.org/10.1093/oso/9780198865247.001.0001);
   [author's page with free PDF](https://sethna.lassp.cornell.edu/statistical_mechanics/)
   — T. Physical intuition for criticality, RG, crackling noise; excellent
   exercises.
6. **Newman, M. E. J. & Barkema, G. T. (1999).** *Monte Carlo Methods in
   Statistical Physics.* Oxford University Press.
   [doi:10.1093/oso/9780198517962.001.0001](https://doi.org/10.1093/oso/9780198517962.001.0001)
   — T. Metropolis, cluster algorithms, error analysis; the practical manual
   for the Ising module.
7. **Cardy, J. (1996).** *Scaling and Renormalization in Statistical
   Physics.* Cambridge University Press.
   [doi:10.1017/CBO9781316036440](https://doi.org/10.1017/CBO9781316036440)
   — T. The standard short course on scaling, real-space and field-theoretic
   RG, and finite-size scaling.
8. **Strogatz, S. H. (2000).** From Kuramoto to Crawford: exploring the onset
   of synchronization in populations of coupled oscillators. *Physica D* 143,
   1–20.
   [doi:10.1016/S0167-2789(00)00094-4](https://doi.org/10.1016/S0167-2789(00)00094-4)
   — R. The Kuramoto model, its self-consistency theory and the stability
   problem, told as a mathematical story.
9. **Ott, E. & Antonsen, T. M. (2008).** Low dimensional behavior of large
   systems of globally coupled oscillators. *Chaos* 18, 037113.
   [doi:10.1063/1.2930766](https://doi.org/10.1063/1.2930766) — P. The exact
   low-dimensional reduction used to validate the Kuramoto module.
10. **Clauset, A., Shalizi, C. R. & Newman, M. E. J. (2009).** Power-law
    distributions in empirical data. *SIAM Review* 51, 661–703.
    [doi:10.1137/070710111](https://doi.org/10.1137/070710111) — P, C. The
    reference method for fitting and testing power laws; why log–log
    regression is not enough.
11. **Watkins, N. W., Pruessner, G., Chapman, S. C., Crosby, N. B. & Jensen,
    H. J. (2016).** 25 years of self-organized criticality: concepts and
    controversies. *Space Science Reviews* 198, 3–44.
    [doi:10.1007/s11214-015-0155-x](https://doi.org/10.1007/s11214-015-0155-x)
    — R. The controversies around SOC, laid out fairly.
12. **Cross, M. C. & Hohenberg, P. C. (1993).** Pattern formation outside of
    equilibrium. *Reviews of Modern Physics* 65, 851–1112.
    [doi:10.1103/RevModPhys.65.851](https://doi.org/10.1103/RevModPhys.65.851)
    — R. The standard review of pattern formation and amplitude equations.
13. **Strogatz, S. H. (2015/2018).** *Nonlinear Dynamics and Chaos*, 2nd ed.
    CRC Press. [doi:10.1201/9780429492563](https://doi.org/10.1201/9780429492563)
    — T. Bifurcations, the logistic map, Lorenz, oscillators.

### The original papers the lab starts from

14. **Bak, P., Tang, C. & Wiesenfeld, K. (1987).** Self-organized
    criticality: An explanation of the 1/f noise. *Phys. Rev. Lett.* 59,
    381–384.
    [doi:10.1103/PhysRevLett.59.381](https://doi.org/10.1103/PhysRevLett.59.381)
    — P. The original model (read in full; see
    [terminology §3](03-terminology.md#3-btw-the-abelian-sandpile-and-related-variants)).
15. **Bak, P., Tang, C. & Wiesenfeld, K. (1988).** Self-organized
    criticality. *Phys. Rev. A* 38, 364–374.
    [doi:10.1103/PhysRevA.38.364](https://doi.org/10.1103/PhysRevA.38.364)
    — P. The full paper: 1D and 2D rules, boundary conventions, protocols, the
    angle of repose and the hourglass analogy (read in full).
16. **Dhar, D. (1990).** Self-organized critical state of sandpile automaton
    models. *Phys. Rev. Lett.* 64, 1613–1616.
    [doi:10.1103/PhysRevLett.64.1613](https://doi.org/10.1103/PhysRevLett.64.1613)
    — P, M. The Abelian formulation, the sandpile group, $\det\Delta$,
    uniform stationary measure.
17. **Onsager, L. (1944).** Crystal statistics. I. A two-dimensional model
    with an order-disorder transition. *Phys. Rev.* 65, 117–149.
    [doi:10.1103/PhysRev.65.117](https://doi.org/10.1103/PhysRev.65.117) — P.
18. **Kuramoto, Y. (1975).** Self-entrainment of a population of coupled
    non-linear oscillators. In *International Symposium on Mathematical
    Problems in Theoretical Physics*, Lecture Notes in Physics 39, 420–422.
    Springer. [doi:10.1007/BFb0013365](https://doi.org/10.1007/BFb0013365) — P.
19. **Kurtz, T. G. (1970).** Solutions of ordinary differential equations as
    limits of pure jump Markov processes. *J. Appl. Prob.* 7, 49–58.
    [doi:10.2307/3212147](https://doi.org/10.2307/3212147) — P, M. The theorem
    behind "the mean-field equation is the limit of large $N$".

### Free resources on the web

20. **Lyons, R. & Peres, Y.** *Probability on Trees and Networks.*
    [Free book](https://rdlyons.pages.iu.edu/prbtree/)
    ([doi:10.1017/9781316672815](https://doi.org/10.1017/9781316672815)) — T, M,
    W. Random walks, electrical networks, spanning trees, percolation on
    trees.
21. **Levin, D. A. & Peres, Y.** *Markov Chains and Mixing Times*, 2nd ed.
    [Free book](https://pages.uoregon.edu/dlevin/MARKOV/)
    ([doi:10.1090/mbk/107](https://doi.org/10.1090/mbk/107)) — T, M, W.
    Convergence of MCMC; Glauber dynamics; coupling.
22. **Grimmett, G.** *Probability on Graphs*.
    [Free book](https://www.statslab.cam.ac.uk/~grg/books/pgs.html) — T, M, W.
    Percolation, random-cluster model, Ising, contact process.
23. **van der Hofstad, R.** *Random Graphs and Complex Networks.*
    [Free notes](https://www.win.tue.nl/~rhofstad/NotesRGCN.html)
    ([doi:10.1017/9781316779422](https://doi.org/10.1017/9781316779422)) — T,
    M, W.
24. **Barabási, A.-L.** *Network Science.*
    [Free book](https://networksciencebook.com/) — T, W.
25. **Baxter, R. J. (1982).** *Exactly Solved Models in Statistical
    Mechanics.* Academic Press.
    [Free PDF from ANU](https://physics.anu.edu.au/theophys/_files/Exactly.pdf)
    — T, W. Transfer matrices, the 2D Ising model, Potts and vertex models.
26. **Duminil-Copin, H. (2017).** Lectures on the Ising and Potts models on
    the hypercubic lattice. [arXiv:1707.00520](https://arxiv.org/abs/1707.00520)
    — R, M, W. **Duminil-Copin, H. (2018).** Sixty years of percolation.
    [arXiv:1712.04651](https://arxiv.org/abs/1712.04651) — R, M, W.
27. **Dhar, D. (1999).** Studying self-organized criticality with exactly
    solved models. Lecture notes.
    [arXiv:cond-mat/9909009](https://arxiv.org/abs/cond-mat/9909009) — R, W.
28. **Clauset, A.** [Power-law distributions in empirical data: code and
    data](https://aaronclauset.github.io/powerlaws/) — W. Reference
    implementations of the 2009 methods.
29. Software documentation used by the architecture:
    [NumPy random: parallel streams](https://numpy.org/doc/stable/reference/random/parallel.html),
    [Numba](https://numba.readthedocs.io/en/stable/),
    [Streamlit `st.fragment`](https://docs.streamlit.io/develop/api-reference/execution-flow/st.fragment),
    [Panel](https://panel.holoviz.org/), [marimo](https://docs.marimo.io/),
    [NetworkX](https://networkx.org/),
    [powerlaw (Python)](https://github.com/jeffalstott/powerlaw) — W.
30. Visual introductions (not sources for claims):
    [Xmorphia, Gray–Scott parameter map](https://mrob.com/pub/comp/xmorphia/),
    [Karl Sims, reaction–diffusion tutorial](https://www.karlsims.com/rd.html),
    [David Perkinson's sandpile pages](https://people.reed.edu/~davidp/sand/),
    [ChaosBook](https://chaosbook.org/),
    [Complexity Explorer (Santa Fe Institute)](https://www.complexityexplorer.org/) — W.

## Part 2 · All works cited, by topic

### Self-organized criticality, sandpiles and avalanches

- Alstrøm, P. (1988). Mean-field exponents for self-organized critical phenomena. *Phys. Rev. A* 38, 4905–4906. [doi:10.1103/PhysRevA.38.4905](https://doi.org/10.1103/PhysRevA.38.4905) — P.
- Bak, P. (1996). *How Nature Works.* Copernicus/Springer. [doi:10.1007/978-1-4757-5426-1](https://doi.org/10.1007/978-1-4757-5426-1) — T (popular; claims to be read critically).
- Bak, P., Chen, K. & Tang, C. (1990). A forest-fire model and some thoughts on turbulence. *Phys. Lett. A* 147, 297–300. [doi:10.1016/0375-9601(90)90451-S](https://doi.org/10.1016/0375-9601(90)90451-S) — P.
- Bak, P. & Sneppen, K. (1993). Punctuated equilibrium and criticality in a simple model of evolution. *Phys. Rev. Lett.* 71, 4083–4086. [doi:10.1103/PhysRevLett.71.4083](https://doi.org/10.1103/PhysRevLett.71.4083) — P.
- Bak, P. & Tang, C. (1989). Earthquakes as a self-organized critical phenomenon. *J. Geophys. Res.* 94, 15635–15637. [doi:10.1029/JB094iB11p15635](https://doi.org/10.1029/JB094iB11p15635) — P.
- Basu, M., Basu, U., Bondyopadhyay, S., Mohanty, P. K. & Hinrichsen, H. (2012). Fixed-energy sandpiles belong generically to directed percolation. *Phys. Rev. Lett.* 109, 015702. [doi:10.1103/PhysRevLett.109.015702](https://doi.org/10.1103/PhysRevLett.109.015702) — P (one side of a debate).
- Bonachela, J. A. & Muñoz, M. A. (2009). Self-organization without conservation: true or just apparent scale-invariance? *J. Stat. Mech.* P09009. [doi:10.1088/1742-5468/2009/09/P09009](https://doi.org/10.1088/1742-5468/2009/09/P09009) — P, C.
- Caracciolo, S. & Sportiello, A. (2012). Exact integration of height probabilities in the Abelian sandpile model. *J. Stat. Mech.* P09013. [doi:10.1088/1742-5468/2012/09/P09013](https://doi.org/10.1088/1742-5468/2012/09/P09013) — P.
- Christensen, K., Corral, Á., Frette, V., Feder, J. & Jøssang, T. (1996). Tracer dispersion in a self-organized critical system. *Phys. Rev. Lett.* 77, 107–110. [doi:10.1103/PhysRevLett.77.107](https://doi.org/10.1103/PhysRevLett.77.107) — P (the Oslo model).
- Christensen, K. & Moloney, N. R. (2005). *Complexity and Criticality.* Imperial College Press. [doi:10.1142/p365](https://doi.org/10.1142/p365) — T.
- Corral, Á., Pérez, C. J., Díaz-Guilera, A. & Arenas, A. (1995). Self-organized criticality and synchronization in a lattice model of integrate-and-fire oscillators. *Phys. Rev. Lett.* 74, 118–121. [doi:10.1103/PhysRevLett.74.118](https://doi.org/10.1103/PhysRevLett.74.118) — P.
- de Carvalho, J. X. & Prado, C. P. C. (2000). Self-organized criticality in the Olami–Feder–Christensen model. *Phys. Rev. Lett.* 84, 4006–4009. [doi:10.1103/PhysRevLett.84.4006](https://doi.org/10.1103/PhysRevLett.84.4006) — P.
- De Menech, M., Stella, A. L. & Tebaldi, C. (1998). Rare events and breakdown of simple scaling in the Abelian sandpile model. *Phys. Rev. E* 58, R2677–R2680. [doi:10.1103/PhysRevE.58.R2677](https://doi.org/10.1103/PhysRevE.58.R2677) — P, C.
- Dhar, D. (1999). Some results and a conjecture for Manna's stochastic sandpile model. *Physica A* 270, 69–81. [doi:10.1016/S0378-4371(99)00149-1](https://doi.org/10.1016/S0378-4371(99)00149-1) — P.
- Dhar, D. & Ramaswamy, R. (1989). Exactly solved model of self-organized critical phenomena. *Phys. Rev. Lett.* 63, 1659–1662. [doi:10.1103/PhysRevLett.63.1659](https://doi.org/10.1103/PhysRevLett.63.1659) — P.
- Dickman, R., Muñoz, M. A., Vespignani, A. & Zapperi, S. (2000). Paths to self-organized criticality. *Braz. J. Phys.* 30, 27–41. [doi:10.1590/S0103-97332000000100004](https://doi.org/10.1590/S0103-97332000000100004) — R.
- Dickman, R., Vespignani, A. & Zapperi, S. (1998). Self-organized criticality as an absorbing-state phase transition. *Phys. Rev. E* 57, 5095–5105. [doi:10.1103/PhysRevE.57.5095](https://doi.org/10.1103/PhysRevE.57.5095) — P.
- di Santo, S., Burioni, R., Vezzani, A. & Muñoz, M. A. (2016). Self-organized bistability associated with first-order phase transitions. *Phys. Rev. Lett.* 116, 240601. [doi:10.1103/PhysRevLett.116.240601](https://doi.org/10.1103/PhysRevLett.116.240601) — P.
- Drossel, B. & Schwabl, F. (1992). Self-organized critical forest-fire model. *Phys. Rev. Lett.* 69, 1629–1632. [doi:10.1103/PhysRevLett.69.1629](https://doi.org/10.1103/PhysRevLett.69.1629) — P.
- Fey, A., Levine, L. & Peres, Y. (2010). Growth rates and explosions in sandpiles. *J. Stat. Phys.* 138, 143–159. [doi:10.1007/s10955-009-9899-6](https://doi.org/10.1007/s10955-009-9899-6) — M.
- Fey, A., Levine, L. & Wilson, D. B. (2010). Driving sandpiles to criticality and beyond. *Phys. Rev. Lett.* 104, 145703. [doi:10.1103/PhysRevLett.104.145703](https://doi.org/10.1103/PhysRevLett.104.145703) — P, C. Threshold density 2.125288 versus stationary density 17/8 (values read in the paper).
- Fey, A., Levine, L. & Wilson, D. B. (2010). Approach to criticality in sandpiles. *Phys. Rev. E* 82, 031121. [doi:10.1103/PhysRevE.82.031121](https://doi.org/10.1103/PhysRevE.82.031121) — P.
- Grassberger, P. (1994). Efficient large-scale simulations of a uniformly driven system. *Phys. Rev. E* 49, 2436–2444. [doi:10.1103/PhysRevE.49.2436](https://doi.org/10.1103/PhysRevE.49.2436) — P.
- Grassberger, P. (2002). Critical behaviour of the Drossel–Schwabl forest fire model. *New J. Phys.* 4, 17. [doi:10.1088/1367-2630/4/1/317](https://doi.org/10.1088/1367-2630/4/1/317) — P, C.
- Head, D. A. & Rodgers, G. J. (1997). Crossover to self-organized criticality in an inertial sandpile model. *Phys. Rev. E* 55, 2573–2579. [doi:10.1103/PhysRevE.55.2573](https://doi.org/10.1103/PhysRevE.55.2573) — P.
- Hwa, T. & Kardar, M. (1989). Dissipative transport in open systems: An investigation of self-organized criticality. *Phys. Rev. Lett.* 62, 1813–1816. [doi:10.1103/PhysRevLett.62.1813](https://doi.org/10.1103/PhysRevLett.62.1813) — P.
- Ivashkevich, E. V., Ktitarev, D. V. & Priezzhev, V. B. (1994). Waves of topplings in an Abelian sandpile. *Physica A* 209, 347–360. [doi:10.1016/0378-4371(94)90188-0](https://doi.org/10.1016/0378-4371(94)90188-0) — P.
- Jensen, H. J. (1998). *Self-Organized Criticality.* Cambridge University Press. [doi:10.1017/CBO9780511622717](https://doi.org/10.1017/CBO9780511622717) — T.
- Jensen, H. J., Christensen, K. & Fogedby, H. C. (1989). 1/f noise, distribution of lifetimes, and a pile of sand. *Phys. Rev. B* 40, 7425–7427. [doi:10.1103/PhysRevB.40.7425](https://doi.org/10.1103/PhysRevB.40.7425) — P, C. The flow of sand in the BTW automaton has a $1/f^2$ spectrum (abstract).
- Kadanoff, L. P., Nagel, S. R., Wu, L. & Zhou, S. (1989). Scaling and universality in avalanches. *Phys. Rev. A* 39, 6524–6537. [doi:10.1103/PhysRevA.39.6524](https://doi.org/10.1103/PhysRevA.39.6524) — P.
- Kenyon, R. W. & Wilson, D. B. (2015). Spanning trees of graphs on surfaces and the intensity of loop-erased random walk on planar graphs. *J. Amer. Math. Soc.* 28, 985–1030. [doi:10.1090/S0894-0347-2014-00819-5](https://doi.org/10.1090/S0894-0347-2014-00819-5) — M.
- Ktitarev, D. V., Lübeck, S., Grassberger, P. & Priezzhev, V. B. (2000). Scaling of waves in the Bak–Tang–Wiesenfeld sandpile model. *Phys. Rev. E* 61, 81–92. [doi:10.1103/PhysRevE.61.81](https://doi.org/10.1103/PhysRevE.61.81) — P.
- Laurson, L., Alava, M. J. & Zapperi, S. (2005). Power spectra of self-organized critical sandpiles. *J. Stat. Mech.* L11001. [doi:10.1088/1742-5468/2005/11/L11001](https://doi.org/10.1088/1742-5468/2005/11/L11001), [arXiv:cond-mat/0509401](https://arxiv.org/abs/cond-mat/0509401) — P. Avalanche power spectra decay as $1/f^{\alpha}$ with $\alpha<2$, equal to the size–duration exponent (abstract).
- Lee, S. B. (2014). Universality class of the conserved Manna model in one dimension. *Phys. Rev. E* 89, 060101. [doi:10.1103/PhysRevE.89.060101](https://doi.org/10.1103/PhysRevE.89.060101) — P (the other side of the debate).
- Levine, L., Pegden, W. & Smart, C. K. (2016). Apollonian structure in the Abelian sandpile. *Geom. Funct. Anal.* 26, 306–336. [doi:10.1007/s00039-016-0358-7](https://doi.org/10.1007/s00039-016-0358-7) — M.
- Levine, L., Pegden, W. & Smart, C. K. (2017). The Apollonian structure of integer superharmonic matrices. *Ann. of Math.* 186, 1–67. [doi:10.4007/annals.2017.186.1.1](https://doi.org/10.4007/annals.2017.186.1.1) — M.
- Levine, L. & Peres, Y. (2017). Laplacian growth, sandpiles, and scaling limits. *Bull. Amer. Math. Soc.* 54, 355–382. [doi:10.1090/bull/1573](https://doi.org/10.1090/bull/1573) — R, M.
- Lise, S. & Paczuski, M. (2001). Self-organized criticality and universality in a nonconservative earthquake model. *Phys. Rev. E* 63, 036111. [doi:10.1103/PhysRevE.63.036111](https://doi.org/10.1103/PhysRevE.63.036111) — P.
- Lübeck, S. (2004). Universal scaling behavior of non-equilibrium phase transitions. *Int. J. Mod. Phys. B* 18, 3977–4118. [doi:10.1142/S0217979204027748](https://doi.org/10.1142/S0217979204027748) — R.
- Lübeck, S. & Usadel, K. D. (1997). Numerical determination of the avalanche exponents of the Bak–Tang–Wiesenfeld model. *Phys. Rev. E* 55, 4095–4099. [doi:10.1103/PhysRevE.55.4095](https://doi.org/10.1103/PhysRevE.55.4095) — P.
- Majumdar, S. N. & Dhar, D. (1991). Height correlations in the Abelian sandpile model. *J. Phys. A* 24, L357–L362. [doi:10.1088/0305-4470/24/7/008](https://doi.org/10.1088/0305-4470/24/7/008) — P.
- Majumdar, S. N. & Dhar, D. (1992). Equivalence between the Abelian sandpile model and the q→0 limit of the Potts model. *Physica A* 185, 129–145. [doi:10.1016/0378-4371(92)90447-X](https://doi.org/10.1016/0378-4371(92)90447-X) — P.
- Manna, S. S. (1991). Two-state model of self-organized criticality. *J. Phys. A* 24, L363–L369. [doi:10.1088/0305-4470/24/7/009](https://doi.org/10.1088/0305-4470/24/7/009) — P.
- Marković, D. & Gros, C. (2014). Power laws and self-organized criticality in theory and nature. *Phys. Rep.* 536, 41–74. [doi:10.1016/j.physrep.2013.11.002](https://doi.org/10.1016/j.physrep.2013.11.002) — R.
- Meester, R. & Znamenski, D. (2003). Limit behavior of the Bak–Sneppen evolution model. *Ann. Probab.* 31, 1986–2002. [doi:10.1214/aop/1068646375](https://doi.org/10.1214/aop/1068646375) — M.
- Meester, R. & Znamenski, D. (2004). Critical thresholds and the limit distribution in the Bak–Sneppen model. *Commun. Math. Phys.* 246, 63–86. [doi:10.1007/s00220-004-1044-4](https://doi.org/10.1007/s00220-004-1044-4) — M.
- Middleton, A. A. & Tang, C. (1995). Self-organized criticality in nonconserved systems. *Phys. Rev. Lett.* 74, 742–745. [doi:10.1103/PhysRevLett.74.742](https://doi.org/10.1103/PhysRevLett.74.742) — P.
- Olami, Z., Feder, H. J. S. & Christensen, K. (1992). Self-organized criticality in a continuous, nonconservative cellular automaton modeling earthquakes. *Phys. Rev. Lett.* 68, 1244–1247. [doi:10.1103/PhysRevLett.68.1244](https://doi.org/10.1103/PhysRevLett.68.1244) — P.
- Paczuski, M., Maslov, S. & Bak, P. (1996). Avalanche dynamics in evolution, growth, and depinning models. *Phys. Rev. E* 53, 414–443. [doi:10.1103/PhysRevE.53.414](https://doi.org/10.1103/PhysRevE.53.414) — P.
- Pegden, W. & Smart, C. K. (2013). Convergence of the Abelian sandpile. *Duke Math. J.* 162, 627–642. [doi:10.1215/00127094-2079677](https://doi.org/10.1215/00127094-2079677) — M.
- Poghosyan, V. S., Priezzhev, V. B. & Ruelle, P. (2011). Return probability for the loop-erased random walk and mean height in the Abelian sandpile model: a proof. *J. Stat. Mech.* P10004. [doi:10.1088/1742-5468/2011/10/P10004](https://doi.org/10.1088/1742-5468/2011/10/P10004) — M.
- Prado, C. P. C. & Olami, Z. (1992). Inertia and break of self-organized criticality in sandpile cellular-automata models. *Phys. Rev. A* 45, 665–669. [doi:10.1103/PhysRevA.45.665](https://doi.org/10.1103/PhysRevA.45.665) — P.
- Priezzhev, V. B. (1994). Structure of two-dimensional sandpile. I. Height probabilities. *J. Stat. Phys.* 74, 955–979. [doi:10.1007/BF02188212](https://doi.org/10.1007/BF02188212) — P.
- Priezzhev, V. B., Dhar, D., Dhar, A. & Krishnamurthy, S. (1996). Eulerian walkers as a model of self-organized criticality. *Phys. Rev. Lett.* 77, 5079–5082. [doi:10.1103/PhysRevLett.77.5079](https://doi.org/10.1103/PhysRevLett.77.5079) — P.
- Priezzhev, V. B., Ktitarev, D. V. & Ivashkevich, E. V. (1996). Formation of avalanches and critical exponents in an Abelian sandpile model. *Phys. Rev. Lett.* 76, 2093–2096. [doi:10.1103/PhysRevLett.76.2093](https://doi.org/10.1103/PhysRevLett.76.2093) — P.
- Socolar, J. E. S., Grinstein, G. & Jayaprakash, C. (1993). On self-organized criticality in nonconserving systems. *Phys. Rev. E* 47, 2366–2376. [doi:10.1103/PhysRevE.47.2366](https://doi.org/10.1103/PhysRevE.47.2366) — P.
- Tebaldi, C., De Menech, M. & Stella, A. L. (1999). Multifractal scaling in the Bak–Tang–Wiesenfeld sandpile and edge events. *Phys. Rev. Lett.* 83, 3952–3955. [doi:10.1103/PhysRevLett.83.3952](https://doi.org/10.1103/PhysRevLett.83.3952) — P, C.
- Vespignani, A., Dickman, R., Muñoz, M. A. & Zapperi, S. (2000). Absorbing-state phase transitions in fixed-energy sandpiles. *Phys. Rev. E* 62, 4564–4582. [doi:10.1103/PhysRevE.62.4564](https://doi.org/10.1103/PhysRevE.62.4564) — P.
- Zapperi, S., Lauritsen, K. B. & Stanley, H. E. (1995). Self-organized branching processes: mean-field theory for avalanches. *Phys. Rev. Lett.* 75, 4071–4074. [doi:10.1103/PhysRevLett.75.4071](https://doi.org/10.1103/PhysRevLett.75.4071) — P.
- Zhang, Y.-C. (1989). Scaling theory of self-organized criticality. *Phys. Rev. Lett.* 63, 470–473. [doi:10.1103/PhysRevLett.63.470](https://doi.org/10.1103/PhysRevLett.63.470) — P.

### Applications of SOC and its critics

- Beggs, J. M. & Plenz, D. (2003). Neuronal avalanches in neocortical circuits. *J. Neurosci.* 23, 11167–11177. [doi:10.1523/JNEUROSCI.23-35-11167.2003](https://doi.org/10.1523/JNEUROSCI.23-35-11167.2003) — P.
- Burridge, R. & Knopoff, L. (1967). Model and theoretical seismicity. *Bull. Seismol. Soc. Am.* 57, 341–371. [doi:10.1785/BSSA0570030341](https://doi.org/10.1785/BSSA0570030341) — P.
- Carlson, J. M. & Langer, J. S. (1989). Properties of earthquakes generated by fault dynamics. *Phys. Rev. Lett.* 62, 2632–2635. [doi:10.1103/PhysRevLett.62.2632](https://doi.org/10.1103/PhysRevLett.62.2632) — P.
- Gutenberg, B. & Richter, C. F. (1944). Frequency of earthquakes in California. *Bull. Seismol. Soc. Am.* 34, 185–188. [doi:10.1785/BSSA0340040185](https://doi.org/10.1785/BSSA0340040185) — P.
- Moretti, P. & Muñoz, M. A. (2013). Griffiths phases and the stretching of criticality in brain networks. *Nat. Commun.* 4, 2521. [doi:10.1038/ncomms3521](https://doi.org/10.1038/ncomms3521) — P.
- Muñoz, M. A. (2018). Colloquium: Criticality and dynamical scaling in living systems. *Rev. Mod. Phys.* 90, 031001. [doi:10.1103/RevModPhys.90.031001](https://doi.org/10.1103/RevModPhys.90.031001) — R.
- Sethna, J. P., Dahmen, K. A. & Myers, C. R. (2001). Crackling noise. *Nature* 410, 242–250. [doi:10.1038/35065675](https://doi.org/10.1038/35065675) — R.
- Sornette, A. & Sornette, D. (1989). Self-organized criticality and earthquakes. *Europhys. Lett.* 9, 197–202. [doi:10.1209/0295-5075/9/3/002](https://doi.org/10.1209/0295-5075/9/3/002) — P.
- Sornette, D. (2006). *Critical Phenomena in Natural Sciences*, 2nd ed. Springer. [doi:10.1007/3-540-33182-4](https://doi.org/10.1007/3-540-33182-4) — T.
- Sornette, D., Johansen, A. & Dornic, I. (1995). Mapping self-organized criticality onto criticality. *J. Phys. I France* 5, 325–335. [doi:10.1051/jp1:1995129](https://doi.org/10.1051/jp1:1995129) — P.
- Touboul, J. & Destexhe, A. (2017). Power-law statistics and universal scaling in the absence of criticality. *Phys. Rev. E* 95, 012413. [doi:10.1103/PhysRevE.95.012413](https://doi.org/10.1103/PhysRevE.95.012413) — P, C.
- Wilting, J. & Priesemann, V. (2019). 25 years of criticality in neuroscience — established results, open controversies, novel concepts. *Curr. Opin. Neurobiol.* 58, 105–111. [doi:10.1016/j.conb.2019.08.002](https://doi.org/10.1016/j.conb.2019.08.002) — R.

### Granular matter, the angle of repose and drainage

- Aranson, I. S. & Tsimring, L. S. (2006). Patterns and collective behavior in granular media: Theoretical concepts. *Rev. Mod. Phys.* 78, 641–692. [doi:10.1103/RevModPhys.78.641](https://doi.org/10.1103/RevModPhys.78.641) — R.
- Beakawi Al-Hashemi, H. M. & Baghabra Al-Amoudi, O. S. (2018). A review on the angle of repose of granular materials. *Powder Technol.* 330, 397–417. [doi:10.1016/j.powtec.2018.02.003](https://doi.org/10.1016/j.powtec.2018.02.003) — R.
- Bouchaud, J.-P., Cates, M. E., Ravi Prakash, J. & Edwards, S. F. (1994). A model for the dynamics of sandpile surfaces. *J. Phys. I France* 4, 1383–1410. [doi:10.1051/jp1:1994195](https://doi.org/10.1051/jp1:1994195) — P.
- Bretz, M., Cunningham, J. B., Kurczynski, P. L. & Nori, F. (1992). Imaging of avalanches in granular materials. *Phys. Rev. Lett.* 69, 2431–2434. [doi:10.1103/PhysRevLett.69.2431](https://doi.org/10.1103/PhysRevLett.69.2431) — P.
- Devauchelle, O., Petroff, A. P., Seybold, H. F. & Rothman, D. H. (2012). Ramification of stream networks. *PNAS* 109, 20832–20836. [doi:10.1073/pnas.1215218109](https://doi.org/10.1073/pnas.1215218109) — P.
- Evesque, P. & Rajchenbach, J. (1989). Instability in a sand heap. *Phys. Rev. Lett.* 62, 44–46. [doi:10.1103/PhysRevLett.62.44](https://doi.org/10.1103/PhysRevLett.62.44) — P.
- Frette, V., Christensen, K., Malthe-Sørenssen, A., Feder, J., Jøssang, T. & Meakin, P. (1996). Avalanche dynamics in a pile of rice. *Nature* 379, 49–52. [doi:10.1038/379049a0](https://doi.org/10.1038/379049a0) — P.
- GDR MiDi (2004). On dense granular flows. *Eur. Phys. J. E* 14, 341–365. [doi:10.1140/epje/i2003-10153-0](https://doi.org/10.1140/epje/i2003-10153-0) — P.
- Held, G. A., Solina, D. H., Keane, D. T., Haag, W. J., Horn, P. M. & Grinstein, G. (1990). Experimental study of critical-mass fluctuations in an evolving sandpile. *Phys. Rev. Lett.* 65, 1120–1123. [doi:10.1103/PhysRevLett.65.1120](https://doi.org/10.1103/PhysRevLett.65.1120) — P.
- Jaeger, H. M., Liu, C. & Nagel, S. R. (1989). Relaxation at the angle of repose. *Phys. Rev. Lett.* 62, 40–43. [doi:10.1103/PhysRevLett.62.40](https://doi.org/10.1103/PhysRevLett.62.40) — P.
- Jaeger, H. M., Nagel, S. R. & Behringer, R. P. (1996). Granular solids, liquids, and gases. *Rev. Mod. Phys.* 68, 1259–1273. [doi:10.1103/RevModPhys.68.1259](https://doi.org/10.1103/RevModPhys.68.1259) — R.
- Mehta, A. & Barker, G. C. (1994). The dynamics of sand. *Rep. Prog. Phys.* 57, 383–416. [doi:10.1088/0034-4885/57/4/002](https://doi.org/10.1088/0034-4885/57/4/002) — R.
- Nagel, S. R. (1992). Instabilities in a sandpile. *Rev. Mod. Phys.* 64, 321–325. [doi:10.1103/RevModPhys.64.321](https://doi.org/10.1103/RevModPhys.64.321) — R.
- Rinaldo, A., Rodríguez-Iturbe, I., Rigon, R., Bras, R. L., Ijjasz-Vasquez, E. & Marani, A. (1992). Minimum energy and fractal structures of drainage networks. *Water Resour. Res.* 28, 2183–2195. [doi:10.1029/92WR00801](https://doi.org/10.1029/92WR00801) — P.
- Rinaldo, A., Rodríguez-Iturbe, I., Rigon, R., Ijjasz-Vasquez, E. & Bras, R. L. (1993). Self-organized fractal river networks. *Phys. Rev. Lett.* 70, 822–825. [doi:10.1103/PhysRevLett.70.822](https://doi.org/10.1103/PhysRevLett.70.822) — P.
- Rodríguez-Iturbe, I. & Rinaldo, A. (1997). *Fractal River Basins: Chance and Self-Organization.* Cambridge University Press. — T (no DOI found).
- Schick, K. L. & Verveen, A. A. (1974). 1/f noise with a low frequency white noise limit. *Nature* 251, 599–601. [doi:10.1038/251599a0](https://doi.org/10.1038/251599a0) — P (hourglass flow; cited by BTW 1988).
- Seybold, H., Rothman, D. H. & Kirchner, J. W. (2017). Climate's watermark in the geometry of stream networks. *Geophys. Res. Lett.* 44, 2272–2280. [doi:10.1002/2016GL072089](https://doi.org/10.1002/2016GL072089) — P.
- Wu, X.-l., Måløy, K. J., Hansen, A., Ammi, M. & Bideau, D. (1993). Why hour glasses tick. *Phys. Rev. Lett.* 71, 1363–1366. [doi:10.1103/PhysRevLett.71.1363](https://doi.org/10.1103/PhysRevLett.71.1363) — P.

### Equilibrium statistical mechanics, Ising and Potts models, Monte Carlo

- Aizenman, M. (1982). Geometric analysis of φ⁴ fields and Ising models. Parts I and II. *Commun. Math. Phys.* 86, 1–48. [doi:10.1007/BF01205659](https://doi.org/10.1007/BF01205659) — M.
- Aizenman, M. & Duminil-Copin, H. (2021). Marginal triviality of the scaling limits of critical 4D Ising and φ⁴₄ models. *Ann. of Math.* 194, 163–235. [doi:10.4007/annals.2021.194.1.3](https://doi.org/10.4007/annals.2021.194.1.3) — M.
- Beale, P. D. (1996). Exact distribution of energies in the two-dimensional Ising model. *Phys. Rev. Lett.* 76, 78–81. [doi:10.1103/PhysRevLett.76.78](https://doi.org/10.1103/PhysRevLett.76.78) — P.
- Beffara, V. & Duminil-Copin, H. (2012). The self-dual point of the two-dimensional random-cluster model is critical for q ≥ 1. *Probab. Theory Relat. Fields* 153, 511–542. [doi:10.1007/s00440-011-0353-8](https://doi.org/10.1007/s00440-011-0353-8) — M.
- Bethe, H. A. (1935). Statistical theory of superlattices. *Proc. R. Soc. Lond. A* 150, 552–575. [doi:10.1098/rspa.1935.0122](https://doi.org/10.1098/rspa.1935.0122) — P.
- Binder, K. (1981). Finite size scaling analysis of Ising model block distribution functions. *Z. Phys. B* 43, 119–140. [doi:10.1007/BF01293604](https://doi.org/10.1007/BF01293604) — P.
- Chelkak, D., Hongler, C. & Izyurov, K. (2015). Conformal invariance of spin correlations in the planar Ising model. *Ann. of Math.* 181, 1087–1138. [doi:10.4007/annals.2015.181.3.5](https://doi.org/10.4007/annals.2015.181.3.5) — M.
- Duminil-Copin, H., Gagnebin, M., Harel, M., Manolescu, I. & Tassion, V. (2021). Discontinuity of the phase transition for the planar random-cluster and Potts models with q > 4. *Ann. Sci. Éc. Norm. Supér.* 54, 1363–1413. [doi:10.24033/asens.2485](https://doi.org/10.24033/asens.2485) — M.
- Duminil-Copin, H., Sidoravicius, V. & Tassion, V. (2017). Continuity of the phase transition for planar random-cluster and Potts models with 1 ≤ q ≤ 4. *Commun. Math. Phys.* 349, 47–107. [doi:10.1007/s00220-016-2759-8](https://doi.org/10.1007/s00220-016-2759-8) — M.
- Ellis, R. S. (2006). *Entropy, Large Deviations, and Statistical Mechanics* (Classics in Mathematics reprint of the 1985 edition). Springer. [doi:10.1007/3-540-29060-5](https://doi.org/10.1007/3-540-29060-5) — T, M.
- Ferdinand, A. E. & Fisher, M. E. (1969). Bounded and inhomogeneous Ising models. I. Specific-heat anomaly of a finite lattice. *Phys. Rev.* 185, 832–846. [doi:10.1103/PhysRev.185.832](https://doi.org/10.1103/PhysRev.185.832) — P.
- Fortuin, C. M. & Kasteleyn, P. W. (1972). On the random-cluster model. I. Introduction and relation to other models. *Physica* 57, 536–564. [doi:10.1016/0031-8914(72)90045-6](https://doi.org/10.1016/0031-8914(72)90045-6) — P.
- Glauber, R. J. (1963). Time-dependent statistics of the Ising model. *J. Math. Phys.* 4, 294–307. [doi:10.1063/1.1703954](https://doi.org/10.1063/1.1703954) — P.
- Griffiths, R. B. (1964). Peierls proof of spontaneous magnetization in a two-dimensional Ising ferromagnet. *Phys. Rev.* 136, A437–A439. [doi:10.1103/PhysRev.136.A437](https://doi.org/10.1103/PhysRev.136.A437) — M.
- Ising, E. (1925). Beitrag zur Theorie des Ferromagnetismus. *Z. Phys.* 31, 253–258. [doi:10.1007/BF02980577](https://doi.org/10.1007/BF02980577) — P.
- Kamieniarz, G. & Blöte, H. W. J. (1993). Universal ratio of magnetization moments in two-dimensional Ising models. *J. Phys. A* 26, 201–212. [doi:10.1088/0305-4470/26/2/009](https://doi.org/10.1088/0305-4470/26/2/009) — P.
- Kaufman, B. (1949). Crystal statistics. II. Partition function evaluated by spinor analysis. *Phys. Rev.* 76, 1232–1243. [doi:10.1103/PhysRev.76.1232](https://doi.org/10.1103/PhysRev.76.1232) — P.
- Kosterlitz, J. M. & Thouless, D. J. (1973). Ordering, metastability and phase transitions in two-dimensional systems. *J. Phys. C* 6, 1181–1203. [doi:10.1088/0022-3719/6/7/010](https://doi.org/10.1088/0022-3719/6/7/010) — P.
- Kramers, H. A. & Wannier, G. H. (1941). Statistics of the two-dimensional ferromagnet. Part I. *Phys. Rev.* 60, 252–262. [doi:10.1103/PhysRev.60.252](https://doi.org/10.1103/PhysRev.60.252) — P.
- Krauth, W. (2006). *Statistical Mechanics: Algorithms and Computations.* Oxford University Press. [doi:10.1093/oso/9780198515357.001.0001](https://doi.org/10.1093/oso/9780198515357.001.0001) — T.
- Landau, D. P. & Binder, K. (2021). *A Guide to Monte Carlo Simulations in Statistical Physics*, 5th ed. Cambridge University Press. [doi:10.1017/9781108780346](https://doi.org/10.1017/9781108780346) — T.
- Lebowitz, J. L. & Penrose, O. (1966). Rigorous treatment of the van der Waals–Maxwell theory of the liquid-vapor transition. *J. Math. Phys.* 7, 98–113. [doi:10.1063/1.1704821](https://doi.org/10.1063/1.1704821) — M.
- Mermin, N. D. & Wagner, H. (1966). Absence of ferromagnetism or antiferromagnetism in one- or two-dimensional isotropic Heisenberg models. *Phys. Rev. Lett.* 17, 1133–1136. [doi:10.1103/PhysRevLett.17.1133](https://doi.org/10.1103/PhysRevLett.17.1133) — M.
- Metropolis, N., Rosenbluth, A. W., Rosenbluth, M. N., Teller, A. H. & Teller, E. (1953). Equation of state calculations by fast computing machines. *J. Chem. Phys.* 21, 1087–1092. [doi:10.1063/1.1699114](https://doi.org/10.1063/1.1699114) — P.
- Nightingale, M. P. & Blöte, H. W. J. (1996). Dynamic exponent of the two-dimensional Ising model and Monte Carlo computation of the subdominant eigenvalue of the stochastic matrix. *Phys. Rev. Lett.* 76, 4548–4551. [doi:10.1103/PhysRevLett.76.4548](https://doi.org/10.1103/PhysRevLett.76.4548) — P.
- Peierls, R. (1936). On Ising's model of ferromagnetism. *Math. Proc. Cambridge Philos. Soc.* 32, 477–481. [doi:10.1017/S0305004100019174](https://doi.org/10.1017/S0305004100019174) — P.
- Salas, J. & Sokal, A. D. (2000). Universal amplitude ratios in the critical two-dimensional Ising model on a torus. *J. Stat. Phys.* 98, 551–588. [doi:10.1023/A:1018611122166](https://doi.org/10.1023/A:1018611122166) — P.
- Smirnov, S. (2010). Conformal invariance in random cluster models. I. Holomorphic fermions in the Ising model. *Ann. of Math.* 172, 1441–1473. [doi:10.4007/annals.2010.172.1441](https://doi.org/10.4007/annals.2010.172.1441) — M.
- Swendsen, R. H. & Wang, J.-S. (1987). Nonuniversal critical dynamics in Monte Carlo simulations. *Phys. Rev. Lett.* 58, 86–88. [doi:10.1103/PhysRevLett.58.86](https://doi.org/10.1103/PhysRevLett.58.86) — P.
- Weiss, P. (1907). L'hypothèse du champ moléculaire et la propriété ferromagnétique. *J. Phys. Théor. Appl.* 6, 661–690. [doi:10.1051/jphystap:019070060066100](https://doi.org/10.1051/jphystap:019070060066100) — P.
- Wolff, U. (1989). Collective Monte Carlo updating for spin systems. *Phys. Rev. Lett.* 62, 361–364. [doi:10.1103/PhysRevLett.62.361](https://doi.org/10.1103/PhysRevLett.62.361) — P.
- Wu, F. Y. (1982). The Potts model. *Rev. Mod. Phys.* 54, 235–268. [doi:10.1103/RevModPhys.54.235](https://doi.org/10.1103/RevModPhys.54.235) — R.
- Yang, C. N. (1952). The spontaneous magnetization of a two-dimensional Ising model. *Phys. Rev.* 85, 808–816. [doi:10.1103/PhysRev.85.808](https://doi.org/10.1103/PhysRev.85.808) — P.

### Renormalization group and universality

- Fisher, M. E. (1998). Renormalization group theory: Its basis and formulation in statistical physics. *Rev. Mod. Phys.* 70, 653–681. [doi:10.1103/RevModPhys.70.653](https://doi.org/10.1103/RevModPhys.70.653) — R.
- Goldenfeld, N. (1992; reissued 2018). *Lectures on Phase Transitions and the Renormalization Group.* CRC Press. [doi:10.1201/9780429493492](https://doi.org/10.1201/9780429493492) — T.
- Griffiths, R. B. & Pearce, P. A. (1979). Mathematical properties of position-space renormalization-group transformations. *J. Stat. Phys.* 20, 499–545. [doi:10.1007/BF01012897](https://doi.org/10.1007/BF01012897) — M, C.
- Kadanoff, L. P. (1966). Scaling laws for Ising models near Tc. *Physics Physique Fizika* 2, 263–272. [doi:10.1103/PhysicsPhysiqueFizika.2.263](https://doi.org/10.1103/PhysicsPhysiqueFizika.2.263) — P.
- Kadanoff, L. P. (1976). Notes on Migdal's recursion formulas. *Ann. Phys.* 100, 359–394. [doi:10.1016/0003-4916(76)90066-X](https://doi.org/10.1016/0003-4916(76)90066-X) — P.
- Kardar, M. (2007). *Statistical Physics of Fields.* Cambridge University Press. [doi:10.1017/CBO9780511815881](https://doi.org/10.1017/CBO9780511815881) — T.
- Koch-Janusz, M. & Ringel, Z. (2018). Mutual information, neural networks and the renormalization group. *Nat. Phys.* 14, 578–582. [doi:10.1038/s41567-018-0081-4](https://doi.org/10.1038/s41567-018-0081-4) — P.
- Kos, F., Poland, D., Simmons-Duffin, D. & Vichi, A. (2016). Precision islands in the Ising and O(N) models. *JHEP* 2016(8), 36. [doi:10.1007/JHEP08(2016)036](https://doi.org/10.1007/JHEP08(2016)036) — P.
- Ma, S.-k. (1976). Renormalization group by Monte Carlo methods. *Phys. Rev. Lett.* 37, 461–464. [doi:10.1103/PhysRevLett.37.461](https://doi.org/10.1103/PhysRevLett.37.461) — P.
- Mehta, P. & Schwab, D. J. (2014). An exact mapping between the variational renormalization group and deep learning. [arXiv:1410.3831](https://arxiv.org/abs/1410.3831) — P (contested claim).
- Niemeijer, Th. & van Leeuwen, J. M. J. (1973). Wilson theory for spin systems on a triangular lattice. *Phys. Rev. Lett.* 31, 1411–1414. [doi:10.1103/PhysRevLett.31.1411](https://doi.org/10.1103/PhysRevLett.31.1411) — P.
- Reynolds, P. J., Stanley, H. E. & Klein, W. (1980). Large-cell Monte Carlo renormalization group for percolation. *Phys. Rev. B* 21, 1223–1245. [doi:10.1103/PhysRevB.21.1223](https://doi.org/10.1103/PhysRevB.21.1223) — P.
- Stanley, H. E. (1999). Scaling, universality, and renormalization: Three pillars of modern critical phenomena. *Rev. Mod. Phys.* 71, S358–S366. [doi:10.1103/RevModPhys.71.S358](https://doi.org/10.1103/RevModPhys.71.S358) — R.
- Swendsen, R. H. (1979). Monte Carlo renormalization group. *Phys. Rev. Lett.* 42, 859–861. [doi:10.1103/PhysRevLett.42.859](https://doi.org/10.1103/PhysRevLett.42.859) — P.
- Swendsen, R. H. (1984). Monte Carlo calculation of renormalized coupling parameters. *Phys. Rev. Lett.* 52, 1165–1168. [doi:10.1103/PhysRevLett.52.1165](https://doi.org/10.1103/PhysRevLett.52.1165) — P.
- van Enter, A. C. D., Fernández, R. & Sokal, A. D. (1993). Regularity properties and pathologies of position-space renormalization-group transformations: Scope and limitations of Gibbsian theory. *J. Stat. Phys.* 72, 879–1167. [doi:10.1007/BF01048183](https://doi.org/10.1007/BF01048183) — M, C.
- Wilson, K. G. (1971). Renormalization group and critical phenomena. I. Renormalization group and the Kadanoff scaling picture. *Phys. Rev. B* 4, 3174–3183. [doi:10.1103/PhysRevB.4.3174](https://doi.org/10.1103/PhysRevB.4.3174) — P.
- Wilson, K. G. (1971). Renormalization group and critical phenomena. II. Phase-space cell analysis of critical behavior. *Phys. Rev. B* 4, 3184–3205. [doi:10.1103/PhysRevB.4.3184](https://doi.org/10.1103/PhysRevB.4.3184) — P.
- Wilson, K. G. & Kogut, J. (1974). The renormalization group and the ε expansion. *Phys. Rep.* 12, 75–199. [doi:10.1016/0370-1573(74)90023-4](https://doi.org/10.1016/0370-1573(74)90023-4) — R.

### Percolation, growth and interacting particle systems

- Cardy, J. L. (1992). Critical percolation in finite geometries. *J. Phys. A* 25, L201–L206. [doi:10.1088/0305-4470/25/4/009](https://doi.org/10.1088/0305-4470/25/4/009) — P.
- Clifford, P. & Sudbury, A. (1973). A model for spatial conflict. *Biometrika* 60, 581–588. [doi:10.1093/biomet/60.3.581](https://doi.org/10.1093/biomet/60.3.581) — P.
- Derrida, B., Evans, M. R., Hakim, V. & Pasquier, V. (1993). Exact solution of a 1D asymmetric exclusion model using a matrix formulation. *J. Phys. A* 26, 1493–1517. [doi:10.1088/0305-4470/26/7/011](https://doi.org/10.1088/0305-4470/26/7/011) — P.
- Domany, E. & Kinzel, W. (1984). Equivalence of cellular automata to Ising models and directed percolation. *Phys. Rev. Lett.* 53, 311–314. [doi:10.1103/PhysRevLett.53.311](https://doi.org/10.1103/PhysRevLett.53.311) — P.
- Family, F. & Vicsek, T. (1985). Scaling of the active zone in the Eden process on percolation networks and the ballistic deposition model. *J. Phys. A* 18, L75–L81. [doi:10.1088/0305-4470/18/2/005](https://doi.org/10.1088/0305-4470/18/2/005) — P.
- Grassberger, P. (1982). On phase transitions in Schlögl's second model. *Z. Phys. B* 47, 365–374. [doi:10.1007/BF01313803](https://doi.org/10.1007/BF01313803) — P.
- Grimmett, G. (1999). *Percolation*, 2nd ed. Springer. [doi:10.1007/978-3-662-03981-6](https://doi.org/10.1007/978-3-662-03981-6) — T, M.
- Hairer, M. (2013). Solving the KPZ equation. *Ann. of Math.* 178, 559–664. [doi:10.4007/annals.2013.178.2.4](https://doi.org/10.4007/annals.2013.178.2.4) — M.
- Harris, T. E. (1974). Contact interactions on a lattice. *Ann. Probab.* 2(6). [doi:10.1214/aop/1176996493](https://doi.org/10.1214/aop/1176996493) — M.
- Henkel, M., Hinrichsen, H. & Lübeck, S. (2008). *Non-Equilibrium Phase Transitions. Volume 1: Absorbing Phase Transitions.* Springer. [doi:10.1007/978-1-4020-8765-3](https://doi.org/10.1007/978-1-4020-8765-3) — T.
- Hinrichsen, H. (2000). Non-equilibrium critical phenomena and phase transitions into absorbing states. *Adv. Phys.* 49, 815–958. [doi:10.1080/00018730050198152](https://doi.org/10.1080/00018730050198152) — R.
- Holley, R. A. & Liggett, T. M. (1975). Ergodic theorems for weakly interacting infinite systems and the voter model. *Ann. Probab.* 3(4). [doi:10.1214/aop/1176996306](https://doi.org/10.1214/aop/1176996306) — M.
- Holroyd, A. E., Levine, L., Mészáros, K., Peres, Y., Propp, J. & Wilson, D. B. (2008). Chip-firing and rotor-routing on directed graphs. In *In and Out of Equilibrium 2*, Progress in Probability 60, 331–364. Birkhäuser. [doi:10.1007/978-3-7643-8786-0_17](https://doi.org/10.1007/978-3-7643-8786-0_17) — M.
- Janssen, H. K. (1981). On the nonequilibrium phase transition in reaction-diffusion systems with an absorbing stationary state. *Z. Phys. B* 42, 151–154. [doi:10.1007/BF01319549](https://doi.org/10.1007/BF01319549) — P.
- Johansson, K. (2000). Shape fluctuations and random matrices. *Commun. Math. Phys.* 209, 437–476. [doi:10.1007/s002200050027](https://doi.org/10.1007/s002200050027) — M.
- Kardar, M., Parisi, G. & Zhang, Y.-C. (1986). Dynamic scaling of growing interfaces. *Phys. Rev. Lett.* 56, 889–892. [doi:10.1103/PhysRevLett.56.889](https://doi.org/10.1103/PhysRevLett.56.889) — P.
- Kesten, H. (1980). The critical probability of bond percolation on the square lattice equals 1/2. *Commun. Math. Phys.* 74, 41–59. [doi:10.1007/BF01197577](https://doi.org/10.1007/BF01197577) — M.
- Lawler, G. F., Bramson, M. & Griffeath, D. (1992). Internal diffusion limited aggregation. *Ann. Probab.* 20(4). [doi:10.1214/aop/1176989542](https://doi.org/10.1214/aop/1176989542) — M.
- Liggett, T. M. (1985). *Interacting Particle Systems.* Springer. [doi:10.1007/978-1-4613-8542-4](https://doi.org/10.1007/978-1-4613-8542-4) — T, M.
- Liggett, T. M. (1999). *Stochastic Interacting Systems: Contact, Voter and Exclusion Processes.* Springer. [doi:10.1007/978-3-662-03990-8](https://doi.org/10.1007/978-3-662-03990-8) — T, M.
- Marro, J. & Dickman, R. (1999). *Nonequilibrium Phase Transitions in Lattice Models.* Cambridge University Press. [doi:10.1017/CBO9780511524288](https://doi.org/10.1017/CBO9780511524288) — T.
- Newman, M. E. J. & Ziff, R. M. (2000). Efficient Monte Carlo algorithm and high-precision results for percolation. *Phys. Rev. Lett.* 85, 4104–4107. [doi:10.1103/PhysRevLett.85.4104](https://doi.org/10.1103/PhysRevLett.85.4104) — P.
- Newman, M. E. J. & Ziff, R. M. (2001). Fast Monte Carlo algorithm for site or bond percolation. *Phys. Rev. E* 64, 016706. [doi:10.1103/PhysRevE.64.016706](https://doi.org/10.1103/PhysRevE.64.016706) — P.
- Ódor, G. (2004). Universality classes in nonequilibrium lattice systems. *Rev. Mod. Phys.* 76, 663–724. [doi:10.1103/RevModPhys.76.663](https://doi.org/10.1103/RevModPhys.76.663) — R.
- Schramm, O. (2000). Scaling limits of loop-erased random walks and uniform spanning trees. *Israel J. Math.* 118, 221–288. [doi:10.1007/BF02803524](https://doi.org/10.1007/BF02803524) — M.
- Smirnov, S. (2001). Critical percolation in the plane: conformal invariance, Cardy's formula, scaling limits. *C. R. Acad. Sci. Paris Sér. I* 333, 239–244. [doi:10.1016/S0764-4442(01)01991-7](https://doi.org/10.1016/S0764-4442(01)01991-7) — M.
- Smirnov, S. & Werner, W. (2001). Critical exponents for two-dimensional percolation. *Math. Res. Lett.* 8, 729–744. [doi:10.4310/MRL.2001.v8.n6.a4](https://doi.org/10.4310/MRL.2001.v8.n6.a4) — M.
- Stauffer, D. & Aharony, A. (1994; reissued 2018). *Introduction to Percolation Theory*, 2nd ed. Taylor & Francis. [doi:10.1201/9781315274386](https://doi.org/10.1201/9781315274386) — T.
- Takeuchi, K. A., Kuroda, M., Chaté, H. & Sano, M. (2007). Directed percolation criticality in turbulent liquid crystals. *Phys. Rev. Lett.* 99, 234503. [doi:10.1103/PhysRevLett.99.234503](https://doi.org/10.1103/PhysRevLett.99.234503) — P.
- Takeuchi, K. A. & Sano, M. (2010). Universal fluctuations of growing interfaces: evidence in turbulent liquid crystals. *Phys. Rev. Lett.* 104, 230601. [doi:10.1103/PhysRevLett.104.230601](https://doi.org/10.1103/PhysRevLett.104.230601) — P.
- Witten, T. A. & Sander, L. M. (1981). Diffusion-limited aggregation, a kinetic critical phenomenon. *Phys. Rev. Lett.* 47, 1400–1403. [doi:10.1103/PhysRevLett.47.1400](https://doi.org/10.1103/PhysRevLett.47.1400) — P.

### Mean-field limits, stochastic processes and epidemics

- Athreya, K. B. & Ney, P. E. (1972). *Branching Processes.* Springer. [doi:10.1007/978-3-642-65371-1](https://doi.org/10.1007/978-3-642-65371-1) — T, M.
- Dobrushin, R. L. (1979). Vlasov equations. *Funct. Anal. Appl.* 13, 115–123. [doi:10.1007/BF01077243](https://doi.org/10.1007/BF01077243) — M.
- Dwass, M. (1969). The total progeny in a branching process and a related random walk. *J. Appl. Prob.* 6, 682–686. [doi:10.2307/3212112](https://doi.org/10.2307/3212112) — M.
- Gillespie, D. T. (1977). Exact stochastic simulation of coupled chemical reactions. *J. Phys. Chem.* 81, 2340–2361. [doi:10.1021/j100540a008](https://doi.org/10.1021/j100540a008) — P.
- Grassberger, P. (1983). On the critical behavior of the general epidemic process and dynamical percolation. *Math. Biosci.* 63, 157–172. [doi:10.1016/0025-5564(82)90036-0](https://doi.org/10.1016/0025-5564(82)90036-0) — P.
- Harris, T. E. (1963). *The Theory of Branching Processes.* Springer. [doi:10.1007/978-3-642-51866-9](https://doi.org/10.1007/978-3-642-51866-9) — T, M.
- Keeling, M. J. (1999). The effects of local spatial structure on epidemiological invasions. *Proc. R. Soc. Lond. B* 266, 859–867. [doi:10.1098/rspb.1999.0716](https://doi.org/10.1098/rspb.1999.0716) — P (pair approximation).
- Kermack, W. O. & McKendrick, A. G. (1927). A contribution to the mathematical theory of epidemics. *Proc. R. Soc. Lond. A* 115, 700–721. [doi:10.1098/rspa.1927.0118](https://doi.org/10.1098/rspa.1927.0118) — P.
- Kurtz, T. G. (1971). Limit theorems for sequences of jump Markov processes approximating ordinary differential processes. *J. Appl. Prob.* 8, 344–356. [doi:10.2307/3211904](https://doi.org/10.2307/3211904) — M.
- Lawler, G. F. & Limic, V. (2010). *Random Walk: A Modern Introduction.* Cambridge University Press. [doi:10.1017/CBO9780511750854](https://doi.org/10.1017/CBO9780511750854) — T, M.
- McKane, A. J. & Newman, T. J. (2005). Predator-prey cycles from resonant amplification of demographic stochasticity. *Phys. Rev. Lett.* 94, 218102. [doi:10.1103/PhysRevLett.94.218102](https://doi.org/10.1103/PhysRevLett.94.218102) — P.
- Metzler, R. & Klafter, J. (2000). The random walk's guide to anomalous diffusion: a fractional dynamics approach. *Phys. Rep.* 339, 1–77. [doi:10.1016/S0370-1573(00)00070-3](https://doi.org/10.1016/S0370-1573(00)00070-3) — R.
- Norris, J. R. (1997). *Markov Chains.* Cambridge University Press. [doi:10.1017/CBO9780511810633](https://doi.org/10.1017/CBO9780511810633) — T, M.
- Sznitman, A.-S. (1991). Topics in propagation of chaos. In *École d'Été de Probabilités de Saint-Flour XIX*, Lecture Notes in Mathematics 1464, 165–251. Springer. [doi:10.1007/BFb0085169](https://doi.org/10.1007/BFb0085169) — M.
- Viswanathan, G. M., Buldyrev, S. V., Havlin, S., da Luz, M. G. E., Raposo, E. P. & Stanley, H. E. (1999). Optimizing the success of random searches. *Nature* 401, 911–914. [doi:10.1038/44831](https://doi.org/10.1038/44831) — P.
- Edwards, A. M. et al. (2007). Revisiting Lévy flight search patterns of wandering albatrosses, bumblebees and deer. *Nature* 449, 1044–1048. [doi:10.1038/nature06199](https://doi.org/10.1038/nature06199) — P, C.

### Synchronization and collective motion

- Acebrón, J. A., Bonilla, L. L., Pérez Vicente, C. J., Ritort, F. & Spigler, R. (2005). The Kuramoto model: A simple paradigm for synchronization phenomena. *Rev. Mod. Phys.* 77, 137–185. [doi:10.1103/RevModPhys.77.137](https://doi.org/10.1103/RevModPhys.77.137) — R.
- Arenas, A., Díaz-Guilera, A., Kurths, J., Moreno, Y. & Zhou, C. (2008). Synchronization in complex networks. *Phys. Rep.* 469, 93–153. [doi:10.1016/j.physrep.2008.09.002](https://doi.org/10.1016/j.physrep.2008.09.002) — R.
- Chaté, H., Ginelli, F., Grégoire, G. & Raynaud, F. (2008). Collective motion of self-propelled particles interacting without cohesion. *Phys. Rev. E* 77, 046113. [doi:10.1103/PhysRevE.77.046113](https://doi.org/10.1103/PhysRevE.77.046113) — P.
- Chiba, H. (2015). A proof of the Kuramoto conjecture for a bifurcation structure of the infinite-dimensional Kuramoto model. *Ergodic Theory Dynam. Systems* 35, 762–834. [doi:10.1017/etds.2013.68](https://doi.org/10.1017/etds.2013.68) — M.
- Daido, H. (1990). Intrinsic fluctuations and a phase transition in a class of large populations of interacting oscillators. *J. Stat. Phys.* 60, 753–800. [doi:10.1007/BF01025993](https://doi.org/10.1007/BF01025993) — P.
- Dörfler, F. & Bullo, F. (2014). Synchronization in complex networks of phase oscillators: A survey. *Automatica* 50, 1539–1564. [doi:10.1016/j.automatica.2014.04.012](https://doi.org/10.1016/j.automatica.2014.04.012) — R.
- Ginelli, F. (2016). The physics of the Vicsek model. *Eur. Phys. J. Spec. Top.* 225, 2099–2117. [doi:10.1140/epjst/e2016-60066-8](https://doi.org/10.1140/epjst/e2016-60066-8) — R.
- Gómez-Gardeñes, J., Gómez, S., Arenas, A. & Moreno, Y. (2011). Explosive synchronization transitions in scale-free networks. *Phys. Rev. Lett.* 106, 128701. [doi:10.1103/PhysRevLett.106.128701](https://doi.org/10.1103/PhysRevLett.106.128701) — P.
- Grégoire, G. & Chaté, H. (2004). Onset of collective and cohesive motion. *Phys. Rev. Lett.* 92, 025702. [doi:10.1103/PhysRevLett.92.025702](https://doi.org/10.1103/PhysRevLett.92.025702) — P, C.
- Hong, H., Chaté, H., Park, H. & Tang, L.-H. (2007). Entrainment transition in populations of random frequency oscillators. *Phys. Rev. Lett.* 99, 184101. [doi:10.1103/PhysRevLett.99.184101](https://doi.org/10.1103/PhysRevLett.99.184101) — P.
- Hong, H., Chaté, H., Tang, L.-H. & Park, H. (2015). Finite-size scaling, dynamic fluctuations, and hyperscaling relation in the Kuramoto model. *Phys. Rev. E* 92, 022122. [doi:10.1103/PhysRevE.92.022122](https://doi.org/10.1103/PhysRevE.92.022122) — P.
- Kuramoto, Y. (1984). *Chemical Oscillations, Waves, and Turbulence.* Springer. [doi:10.1007/978-3-642-69689-3](https://doi.org/10.1007/978-3-642-69689-3) — T.
- Lancellotti, C. (2005). On the Vlasov limit for systems of nonlinearly coupled oscillators without noise. *Transport Theory Stat. Phys.* 34, 523–535. [doi:10.1080/00411450508951152](https://doi.org/10.1080/00411450508951152) — M.
- Mirollo, R. E. & Strogatz, S. H. (1990). Synchronization of pulse-coupled biological oscillators. *SIAM J. Appl. Math.* 50, 1645–1662. [doi:10.1137/0150098](https://doi.org/10.1137/0150098) — M.
- Ott, E. & Antonsen, T. M. (2009). Long time evolution of phase oscillator systems. *Chaos* 19, 023117. [doi:10.1063/1.3136851](https://doi.org/10.1063/1.3136851) — P.
- Ottino-Löffler, B. & Strogatz, S. H. (2016). Kuramoto model with uniformly spaced frequencies: Finite-N asymptotics of the locking threshold. *Phys. Rev. E* 93, 062220. [doi:10.1103/PhysRevE.93.062220](https://doi.org/10.1103/PhysRevE.93.062220) — P.
- Pazó, D. (2005). Thermodynamic limit of the first-order phase transition in the Kuramoto model. *Phys. Rev. E* 72, 046211. [doi:10.1103/PhysRevE.72.046211](https://doi.org/10.1103/PhysRevE.72.046211) — P.
- Pecora, L. M. & Carroll, T. L. (1998). Master stability functions for synchronized coupled systems. *Phys. Rev. Lett.* 80, 2109–2112. [doi:10.1103/PhysRevLett.80.2109](https://doi.org/10.1103/PhysRevLett.80.2109) — P.
- Pikovsky, A., Rosenblum, M. & Kurths, J. (2001). *Synchronization: A Universal Concept in Nonlinear Sciences.* Cambridge University Press. [doi:10.1017/CBO9780511755743](https://doi.org/10.1017/CBO9780511755743) — T.
- Reynolds, C. W. (1987). Flocks, herds and schools: A distributed behavioral model. *ACM SIGGRAPH Computer Graphics* 21(4), 25–34. [doi:10.1145/37402.37406](https://doi.org/10.1145/37402.37406) — P.
- Rodrigues, F. A., Peron, T. K. D., Ji, P. & Kurths, J. (2016). The Kuramoto model in complex networks. *Phys. Rep.* 610, 1–98. [doi:10.1016/j.physrep.2015.10.008](https://doi.org/10.1016/j.physrep.2015.10.008) — R.
- Solon, A. P., Chaté, H. & Tailleur, J. (2015). From phase to microphase separation in flocking models: The essential role of nonequilibrium fluctuations. *Phys. Rev. Lett.* 114, 068101. [doi:10.1103/PhysRevLett.114.068101](https://doi.org/10.1103/PhysRevLett.114.068101) — P.
- Strogatz, S. H. & Mirollo, R. E. (1991). Stability of incoherence in a population of coupled oscillators. *J. Stat. Phys.* 63, 613–635. [doi:10.1007/BF01029202](https://doi.org/10.1007/BF01029202) — P.
- Strogatz, S. H., Mirollo, R. E. & Matthews, P. C. (1992). Coupled nonlinear oscillators below the synchronization threshold: Relaxation by generalized Landau damping. *Phys. Rev. Lett.* 68, 2730–2733. [doi:10.1103/PhysRevLett.68.2730](https://doi.org/10.1103/PhysRevLett.68.2730) — P.
- Toner, J. & Tu, Y. (1995). Long-range order in a two-dimensional dynamical XY model: How birds fly together. *Phys. Rev. Lett.* 75, 4326–4329. [doi:10.1103/PhysRevLett.75.4326](https://doi.org/10.1103/PhysRevLett.75.4326) — P.
- Toner, J. & Tu, Y. (1998). Flocks, herds, and schools: A quantitative theory of flocking. *Phys. Rev. E* 58, 4828–4858. [doi:10.1103/PhysRevE.58.4828](https://doi.org/10.1103/PhysRevE.58.4828) — P.
- Vicsek, T., Czirók, A., Ben-Jacob, E., Cohen, I. & Shochet, O. (1995). Novel type of phase transition in a system of self-driven particles. *Phys. Rev. Lett.* 75, 1226–1229. [doi:10.1103/PhysRevLett.75.1226](https://doi.org/10.1103/PhysRevLett.75.1226) — P.
- Vicsek, T. & Zafeiris, A. (2012). Collective motion. *Phys. Rep.* 517, 71–140. [doi:10.1016/j.physrep.2012.03.004](https://doi.org/10.1016/j.physrep.2012.03.004) — R.
- Watanabe, S. & Strogatz, S. H. (1994). Constants of motion for superconducting Josephson arrays. *Physica D* 74, 197–253. [doi:10.1016/0167-2789(94)90196-1](https://doi.org/10.1016/0167-2789(94)90196-1) — P.

### Pattern formation and reaction–diffusion

- Aranson, I. S. & Kramer, L. (2002). The world of the complex Ginzburg–Landau equation. *Rev. Mod. Phys.* 74, 99–143. [doi:10.1103/RevModPhys.74.99](https://doi.org/10.1103/RevModPhys.74.99) — R.
- Barkley, D. (1991). A model for fast computer simulation of waves in excitable media. *Physica D* 49, 61–70. [doi:10.1016/0167-2789(91)90194-E](https://doi.org/10.1016/0167-2789(91)90194-E) — P.
- Castets, V., Dulos, E., Boissonade, J. & De Kepper, P. (1990). Experimental evidence of a sustained standing Turing-type nonequilibrium chemical pattern. *Phys. Rev. Lett.* 64, 2953–2956. [doi:10.1103/PhysRevLett.64.2953](https://doi.org/10.1103/PhysRevLett.64.2953) — P.
- Cross, M. & Greenside, H. (2009). *Pattern Formation and Dynamics in Nonequilibrium Systems.* Cambridge University Press. [doi:10.1017/CBO9780511627200](https://doi.org/10.1017/CBO9780511627200) — T.
- FitzHugh, R. (1961). Impulses and physiological states in theoretical models of nerve membrane. *Biophys. J.* 1, 445–466. [doi:10.1016/S0006-3495(61)86902-6](https://doi.org/10.1016/S0006-3495(61)86902-6) — P.
- Gierer, A. & Meinhardt, H. (1972). A theory of biological pattern formation. *Kybernetik* 12, 30–39. [doi:10.1007/BF00289234](https://doi.org/10.1007/BF00289234) — P.
- Gray, P. & Scott, S. K. (1983). Autocatalytic reactions in the isothermal, continuous stirred tank reactor. *Chem. Eng. Sci.* 38, 29–43. [doi:10.1016/0009-2509(83)80132-8](https://doi.org/10.1016/0009-2509(83)80132-8) — P.
- Gray, P. & Scott, S. K. (1984). Autocatalytic reactions in the isothermal, continuous stirred tank reactor (second paper). *Chem. Eng. Sci.* 39, 1087–1097. [doi:10.1016/0009-2509(84)87017-7](https://doi.org/10.1016/0009-2509(84)87017-7) — P.
- Hoyle, R. (2006). *Pattern Formation: An Introduction to Methods.* Cambridge University Press. [doi:10.1017/CBO9780511616051](https://doi.org/10.1017/CBO9780511616051) — T.
- Lee, K. J., McCormick, W. D., Ouyang, Q. & Swinney, H. L. (1993). Pattern formation by interacting chemical fronts. *Science* 261, 192–194. [doi:10.1126/science.261.5118.192](https://doi.org/10.1126/science.261.5118.192) — P.
- Murray, J. D. (2003). *Mathematical Biology II: Spatial Models and Biomedical Applications*, 3rd ed. Springer. [doi:10.1007/b98869](https://doi.org/10.1007/b98869) — T.
- Nagumo, J., Arimoto, S. & Yoshizawa, S. (1962). An active pulse transmission line simulating nerve axon. *Proc. IRE* 50, 2061–2070. [doi:10.1109/JRPROC.1962.288235](https://doi.org/10.1109/JRPROC.1962.288235) — P.
- Ouyang, Q. & Swinney, H. L. (1991). Transition from a uniform state to hexagonal and striped Turing patterns. *Nature* 352, 610–612. [doi:10.1038/352610a0](https://doi.org/10.1038/352610a0) — P.
- Pearson, J. E. (1993). Complex patterns in a simple system. *Science* 261, 189–192. [doi:10.1126/science.261.5118.189](https://doi.org/10.1126/science.261.5118.189) — P.
- Raspopovic, J., Marcon, L., Russo, L. & Sharpe, J. (2014). Digit patterning is controlled by a Bmp-Sox9-Wnt Turing network modulated by morphogen gradients. *Science* 345, 566–570. [doi:10.1126/science.1252960](https://doi.org/10.1126/science.1252960) — P.
- Swift, J. & Hohenberg, P. C. (1977). Hydrodynamic fluctuations at the convective instability. *Phys. Rev. A* 15, 319–328. [doi:10.1103/PhysRevA.15.319](https://doi.org/10.1103/PhysRevA.15.319) — P.
- Turing, A. M. (1952). The chemical basis of morphogenesis. *Phil. Trans. R. Soc. Lond. B* 237, 37–72. [doi:10.1098/rstb.1952.0012](https://doi.org/10.1098/rstb.1952.0012) — P.

### Nonlinear dynamics and chaos

- Collet, P. & Eckmann, J.-P. (1980; reissued 2009). *Iterated Maps on the Interval as Dynamical Systems.* Birkhäuser. [doi:10.1007/978-0-8176-4927-2](https://doi.org/10.1007/978-0-8176-4927-2) — T, M.
- de Melo, W. & van Strien, S. (1993). *One-Dimensional Dynamics.* Springer. [doi:10.1007/978-3-642-78043-1](https://doi.org/10.1007/978-3-642-78043-1) — T, M.
- Feigenbaum, M. J. (1978). Quantitative universality for a class of nonlinear transformations. *J. Stat. Phys.* 19, 25–52. [doi:10.1007/BF01020332](https://doi.org/10.1007/BF01020332) — P.
- Graczyk, J. & Świątek, G. (1997). Generic hyperbolicity in the logistic family. *Ann. of Math.* 146(1). [doi:10.2307/2951831](https://doi.org/10.2307/2951831) — M.
- Guckenheimer, J. & Holmes, P. (1983). *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields.* Springer. [doi:10.1007/978-1-4612-1140-2](https://doi.org/10.1007/978-1-4612-1140-2) — T, M.
- Jakobson, M. V. (1981). Absolutely continuous invariant measures for one-parameter families of one-dimensional maps. *Commun. Math. Phys.* 81, 39–88. [doi:10.1007/BF01941800](https://doi.org/10.1007/BF01941800) — M.
- Kaneko, K. (1985). Spatiotemporal intermittency in coupled map lattices. *Prog. Theor. Phys.* 74, 1033–1044. [doi:10.1143/PTP.74.1033](https://doi.org/10.1143/PTP.74.1033) — P.
- Lanford, O. E., III (1982). A computer-assisted proof of the Feigenbaum conjectures. *Bull. Amer. Math. Soc.* 6, 427–435. [doi:10.1090/S0273-0979-1982-15008-X](https://doi.org/10.1090/S0273-0979-1982-15008-X) — M.
- Li, T.-Y. & Yorke, J. A. (1975). Period three implies chaos. *Amer. Math. Monthly* 82, 985–992. [doi:10.1080/00029890.1975.11994008](https://doi.org/10.1080/00029890.1975.11994008) — M.
- Lorenz, E. N. (1963). Deterministic nonperiodic flow. *J. Atmos. Sci.* 20, 130–141. [doi:10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2](https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2) — P.
- Lotka, A. J. (1920). Analytical note on certain rhythmic relations in organic systems. *PNAS* 6, 410–415. [doi:10.1073/pnas.6.7.410](https://doi.org/10.1073/pnas.6.7.410) — P.
- Lyubich, M. (2002). Almost every real quadratic map is either regular or stochastic. *Ann. of Math.* 156, 1–78. [doi:10.2307/3597183](https://doi.org/10.2307/3597183) — M.
- May, R. M. (1976). Simple mathematical models with very complicated dynamics. *Nature* 261, 459–467. [doi:10.1038/261459a0](https://doi.org/10.1038/261459a0) — R.
- Ott, E. (2002). *Chaos in Dynamical Systems*, 2nd ed. Cambridge University Press. [doi:10.1017/CBO9780511803260](https://doi.org/10.1017/CBO9780511803260) — T.
- Tucker, W. (1999). The Lorenz attractor exists. *C. R. Acad. Sci. Paris Sér. I* 328, 1197–1202. [doi:10.1016/S0764-4442(99)80439-X](https://doi.org/10.1016/S0764-4442(99)80439-X) — M.
- Tucker, W. (2002). A rigorous ODE solver and Smale's 14th problem. *Found. Comput. Math.* 2, 53–117. [doi:10.1007/s002080010018](https://doi.org/10.1007/s002080010018) — M.
- Volterra, V. (1926). Fluctuations in the abundance of a species considered mathematically. *Nature* 118, 558–560. [doi:10.1038/118558a0](https://doi.org/10.1038/118558a0) — P.

### Cellular automata and computation

- Berlekamp, E. R., Conway, J. H. & Guy, R. K. (1982). *Winning Ways for Your Mathematical Plays*, Vol. 2, ch. 25. Academic Press. — T (universality of Life, sketched; no DOI).
- Ceccherini-Silberstein, T. & Coornaert, M. (2010). *Cellular Automata and Groups.* Springer. [doi:10.1007/978-3-642-14034-1](https://doi.org/10.1007/978-3-642-14034-1) — T, M.
- Cook, M. (2004). Universality in elementary cellular automata. *Complex Systems* 15, 1–40. [doi:10.25088/ComplexSystems.15.1.1](https://doi.org/10.25088/ComplexSystems.15.1.1) — M.
- Gardner, M. (1970). Mathematical Games: The fantastic combinations of John Conway's new solitaire game "life". *Scientific American* 223(4), 120–123. [doi:10.1038/scientificamerican1070-120](https://doi.org/10.1038/scientificamerican1070-120) — P (popular).
- Hedlund, G. A. (1969). Endomorphisms and automorphisms of the shift dynamical system. *Math. Systems Theory* 3, 320–375. [doi:10.1007/BF01691062](https://doi.org/10.1007/BF01691062) — M.
- Kari, J. (2005). Theory of cellular automata: A survey. *Theor. Comput. Sci.* 334, 3–33. [doi:10.1016/j.tcs.2004.11.021](https://doi.org/10.1016/j.tcs.2004.11.021) — R, M.
- Kauffman, S. A. (1969). Metabolic stability and epigenesis in randomly constructed genetic nets. *J. Theor. Biol.* 22, 437–467. [doi:10.1016/0022-5193(69)90015-0](https://doi.org/10.1016/0022-5193(69)90015-0) — P.
- Derrida, B. & Pomeau, Y. (1986). Random networks of automata: a simple annealed approximation. *Europhys. Lett.* 1, 45–49. [doi:10.1209/0295-5075/1/2/001](https://doi.org/10.1209/0295-5075/1/2/001) — P.
- Langton, C. G. (1990). Computation at the edge of chaos: Phase transitions and emergent computation. *Physica D* 42, 12–37. [doi:10.1016/0167-2789(90)90064-V](https://doi.org/10.1016/0167-2789(90)90064-V) — P.
- Mitchell, M., Hraber, P. T. & Crutchfield, J. P. (1993). Revisiting the edge of chaos: Evolving cellular automata to perform computations. *Complex Systems* 7, 89–130. [Journal page](https://www.complex-systems.com/abstracts/v07_i02_a01/), [arXiv:adap-org/9303003](https://arxiv.org/abs/adap-org/9303003) — P, C.
- Nowak, M. A. & May, R. M. (1992). Evolutionary games and spatial chaos. *Nature* 359, 826–829. [doi:10.1038/359826a0](https://doi.org/10.1038/359826a0) — P.
- Rendell, P. (2016). *Turing Machine Universality of the Game of Life.* Springer. [doi:10.1007/978-3-319-19842-2](https://doi.org/10.1007/978-3-319-19842-2) — M.
- Wolfram, S. (1983). Statistical mechanics of cellular automata. *Rev. Mod. Phys.* 55, 601–644. [doi:10.1103/RevModPhys.55.601](https://doi.org/10.1103/RevModPhys.55.601) — P.
- Wolfram, S. (1984). Universality and complexity in cellular automata. *Physica D* 10, 1–35. [doi:10.1016/0167-2789(84)90245-8](https://doi.org/10.1016/0167-2789(84)90245-8) — P.
- Wolfram, S. (2019). [Announcing the Rule 30 prizes](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/). — W (statement of three open problems).

### Networks and agent-based models

- Albert, R. & Barabási, A.-L. (2002). Statistical mechanics of complex networks. *Rev. Mod. Phys.* 74, 47–97. [doi:10.1103/RevModPhys.74.47](https://doi.org/10.1103/RevModPhys.74.47) — R.
- Barabási, A.-L. & Albert, R. (1999). Emergence of scaling in random networks. *Science* 286, 509–512. [doi:10.1126/science.286.5439.509](https://doi.org/10.1126/science.286.5439.509) — P.
- Bollobás, B., Riordan, O., Spencer, J. & Tusnády, G. (2001). The degree sequence of a scale-free random graph process. *Random Struct. Algorithms* 18, 279–290. [doi:10.1002/rsa.1009](https://doi.org/10.1002/rsa.1009) — M.
- Brandt, C., Immorlica, N., Kamath, G. & Kleinberg, R. (2012). An analysis of one-dimensional Schelling segregation. In *Proc. 44th ACM Symposium on Theory of Computing*, 789–804. [doi:10.1145/2213977.2214048](https://doi.org/10.1145/2213977.2214048) — M.
- Broido, A. D. & Clauset, A. (2019). Scale-free networks are rare. *Nat. Commun.* 10, 1017. [doi:10.1038/s41467-019-08746-5](https://doi.org/10.1038/s41467-019-08746-5) — P, C.
- Dorogovtsev, S. N., Goltsev, A. V. & Mendes, J. F. F. (2008). Critical phenomena in complex networks. *Rev. Mod. Phys.* 80, 1275–1335. [doi:10.1103/RevModPhys.80.1275](https://doi.org/10.1103/RevModPhys.80.1275) — R.
- Durrett, R. (2006). *Random Graph Dynamics.* Cambridge University Press. [doi:10.1017/CBO9780511546594](https://doi.org/10.1017/CBO9780511546594) — T, M.
- Erdős, P. & Rényi, A. (1959). On random graphs. I. *Publ. Math. Debrecen* 6, 290–297. [doi:10.5486/PMD.1959.6.3-4.12](https://doi.org/10.5486/PMD.1959.6.3-4.12) — M.
- Erdős, P. & Rényi, A. (1960). On the evolution of random graphs. *Publ. Math. Inst. Hung. Acad. Sci.* 5, 17–61. [PDF at the Rényi Institute](https://www.renyi.hu/~p_erdos/1960-10.pdf) — M.
- Grauwin, S., Bertin, E., Lemoy, R. & Jensen, P. (2009). Competition between collective and individual dynamics. *PNAS* 106, 20622–20626. [doi:10.1073/pnas.0906263106](https://doi.org/10.1073/pnas.0906263106) — P.
- Holme, P. (2019). Rare and everywhere: Perspectives on scale-free networks. *Nat. Commun.* 10, 1016. [doi:10.1038/s41467-019-09038-8](https://doi.org/10.1038/s41467-019-09038-8) — R.
- Newman, M. E. J. (2002). Spread of epidemic disease on networks. *Phys. Rev. E* 66, 016128. [doi:10.1103/PhysRevE.66.016128](https://doi.org/10.1103/PhysRevE.66.016128) — P.
- Newman, M. E. J. (2003). The structure and function of complex networks. *SIAM Rev.* 45, 167–256. [doi:10.1137/S003614450342480](https://doi.org/10.1137/S003614450342480) — R.
- Newman, M. (2018). *Networks*, 2nd ed. Oxford University Press. [doi:10.1093/oso/9780198805090.001.0001](https://doi.org/10.1093/oso/9780198805090.001.0001) — T.
- Pastor-Satorras, R., Castellano, C., Van Mieghem, P. & Vespignani, A. (2015). Epidemic processes in complex networks. *Rev. Mod. Phys.* 87, 925–979. [doi:10.1103/RevModPhys.87.925](https://doi.org/10.1103/RevModPhys.87.925) — R.
- Pastor-Satorras, R. & Vespignani, A. (2001). Epidemic spreading in scale-free networks. *Phys. Rev. Lett.* 86, 3200–3203. [doi:10.1103/PhysRevLett.86.3200](https://doi.org/10.1103/PhysRevLett.86.3200) — P.
- Schelling, T. C. (1971). Dynamic models of segregation. *J. Math. Sociol.* 1, 143–186. [doi:10.1080/0022250X.1971.9989794](https://doi.org/10.1080/0022250X.1971.9989794) — P.
- Vinković, D. & Kirman, A. (2006). A physical analogue of the Schelling model. *PNAS* 103, 19261–19265. [doi:10.1073/pnas.0609371103](https://doi.org/10.1073/pnas.0609371103) — P.
- Watts, D. J. & Strogatz, S. H. (1998). Collective dynamics of "small-world" networks. *Nature* 393, 440–442. [doi:10.1038/30918](https://doi.org/10.1038/30918) — P.

### Disorder, memory and other models mentioned

- Hopfield, J. J. (1982). Neural networks and physical systems with emergent collective computational abilities. *PNAS* 79, 2554–2558. [doi:10.1073/pnas.79.8.2554](https://doi.org/10.1073/pnas.79.8.2554) — P.
- Bray, A. J. (1994). Theory of phase-ordering kinetics. *Adv. Phys.* 43, 357–459. [doi:10.1080/00018739400101505](https://doi.org/10.1080/00018739400101505) — R.
- Sethna, J. P., Dahmen, K., Kartha, S., Krumhansl, J. A., Roberts, B. W. & Shore, J. D. (1993). Hysteresis and hierarchies: Dynamics of disorder-driven first-order phase transformations. *Phys. Rev. Lett.* 70, 3347–3350. [doi:10.1103/PhysRevLett.70.3347](https://doi.org/10.1103/PhysRevLett.70.3347) — P.

### Statistics of heavy tails, information and complexity

- Alstott, J., Bullmore, E. & Plenz, D. (2014). powerlaw: A Python package for analysis of heavy-tailed distributions. *PLoS ONE* 9, e85777. [doi:10.1371/journal.pone.0085777](https://doi.org/10.1371/journal.pone.0085777) — P (software).
- Anderson, P. W. (1972). More is different. *Science* 177, 393–396. [doi:10.1126/science.177.4047.393](https://doi.org/10.1126/science.177.4047.393) — P (essay).
- Barnett, L., Lizier, J. T., Harré, M., Seth, A. K. & Bossomaier, T. (2013). Information flow in a kinetic Ising model peaks in the disordered phase. *Phys. Rev. Lett.* 111, 177203. [doi:10.1103/PhysRevLett.111.177203](https://doi.org/10.1103/PhysRevLett.111.177203) — P, C.
- Bedau, M. A. (1997). Weak emergence. *Noûs* 31 (Philosophical Perspectives 11), 375–399. [doi:10.1111/0029-4624.31.s11.17](https://doi.org/10.1111/0029-4624.31.s11.17) — P (philosophy).
- Bialek, W., Nemenman, I. & Tishby, N. (2001). Predictability, complexity, and learning. *Neural Comput.* 13, 2409–2463. [doi:10.1162/089976601753195969](https://doi.org/10.1162/089976601753195969) — P.
- Cover, T. M. & Thomas, J. A. (2005). *Elements of Information Theory*, 2nd ed. Wiley. [doi:10.1002/047174882X](https://doi.org/10.1002/047174882X) — T.
- Crutchfield, J. P. & Young, K. (1989). Inferring statistical complexity. *Phys. Rev. Lett.* 63, 105–108. [doi:10.1103/PhysRevLett.63.105](https://doi.org/10.1103/PhysRevLett.63.105) — P.
- Deluca, A. & Corral, Á. (2013). Fitting and goodness-of-fit test of non-truncated and truncated power-law distributions. *Acta Geophys.* 61, 1351–1394. [doi:10.2478/s11600-013-0154-9](https://doi.org/10.2478/s11600-013-0154-9) — P.
- Falconer, K. (2003). *Fractal Geometry: Mathematical Foundations and Applications*, 2nd ed. Wiley. [doi:10.1002/0470013850](https://doi.org/10.1002/0470013850) — T, M.
- Feldman, D. P. & Crutchfield, J. P. (1998). Measures of statistical complexity: Why? *Phys. Lett. A* 238, 244–252. [doi:10.1016/S0375-9601(97)00855-4](https://doi.org/10.1016/S0375-9601(97)00855-4) — C.
- Grassberger, P. (1986). Toward a quantitative theory of self-generated complexity. *Int. J. Theor. Phys.* 25, 907–938. [doi:10.1007/BF00668821](https://doi.org/10.1007/BF00668821) — P.
- Grassberger, P. & Procaccia, I. (1983). Characterization of strange attractors. *Phys. Rev. Lett.* 50, 346–349. [doi:10.1103/PhysRevLett.50.346](https://doi.org/10.1103/PhysRevLett.50.346) — P.
- Halsey, T. C., Jensen, M. H., Kadanoff, L. P., Procaccia, I. & Shraiman, B. I. (1986). Fractal measures and their singularities: The characterization of strange sets. *Phys. Rev. A* 33, 1141–1151. [doi:10.1103/PhysRevA.33.1141](https://doi.org/10.1103/PhysRevA.33.1141) — P.
- Lempel, A. & Ziv, J. (1976). On the complexity of finite sequences. *IEEE Trans. Inf. Theory* 22, 75–81. [doi:10.1109/TIT.1976.1055501](https://doi.org/10.1109/TIT.1976.1055501) — P.
- López-Ruiz, R., Mancini, H. L. & Calbet, X. (1995). A statistical measure of complexity. *Phys. Lett. A* 209, 321–326. [doi:10.1016/0375-9601(95)00867-5](https://doi.org/10.1016/0375-9601(95)00867-5) — P.
- Schreiber, T. (2000). Measuring information transfer. *Phys. Rev. Lett.* 85, 461–464. [doi:10.1103/PhysRevLett.85.461](https://doi.org/10.1103/PhysRevLett.85.461) — P.
- Shannon, C. E. (1948). A mathematical theory of communication. *Bell Syst. Tech. J.* 27, 379–423. [doi:10.1002/j.1538-7305.1948.tb01338.x](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x) — P.
- Stumpf, M. P. H. & Porter, M. A. (2012). Critical truths about power laws. *Science* 335, 665–666. [doi:10.1126/science.1216142](https://doi.org/10.1126/science.1216142) — C.
