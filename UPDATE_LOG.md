# Update log

## 00 (2026-10-13)

Pull request #1. The research map and the plan. There is no simulation code
yet; the first module comes with 01.

### Research notes

- **A map of the field.** The micro-to-macro question; four mechanisms
  (laws of large numbers, phase transitions, instabilities, slow driving with
  threshold relaxation); precise definitions of order parameters, scaling,
  universality, the four meanings of "mean-field", absorbing states and
  self-organized criticality; twelve families of models; a table of the
  links between them with their status, from theorems to contested
  analogies; evidence labels used in all later documents.
- **Model catalogue.** About forty models with rules, exact results,
  observables, validation anchors and pitfalls; microscopic models paired
  with their mean-field equations; renormalization examples ranked by rigour;
  a comparison table; a ranking of the brief's additional models (the
  logistic map first); fourteen candidates the brief did not list.
- **Terminology.**
  - "Angle of drainage periodic function" is not an established term. The
    most plausible readings come from the BTW papers themselves: the angle of
    repose as the threshold slope, the sand flowing off the pile (their
    hourglass analogy), and pendula that turn through a full period. Real
    piles, which avalanche periodically between two angles, are another
    candidate. Seven further readings are listed and assessed.
  - "Self-sustained criticality" is a nuclear-engineering phrase (a chain
    reaction with $k_{\mathrm{eff}}=1$), i.e. critical branching. It is not a
    synonym of self-organized criticality.
  - The original BTW rules are quoted from the 1987 and 1988 papers, which
    were read in full: synchronous updating, perturbations of relaxed states,
    a slope variable, and boundary names that are the reverse of today's.
    They are compared with Dhar's Abelian sandpile, with a table of which
    observables each difference affects.
- **Bibliography.** A short annotated list (30 entries) and about 300 cited
  works. Every DOI was checked against Crossref; arXiv identifiers and web
  links were opened.
- **Experiments and open questions.** The experiment protocol; a procedure
  for power-law claims (maximum likelihood, goodness of fit, alternative
  distributions, finite-size scaling); twelve experiments; ten open
  questions; twelve misconceptions.

### Plan

- **Architecture.** Python 3.12 or newer with NumPy and SciPy; Numba only
  after profiling; Matplotlib; Streamlit for the app, Jupyter for notebooks,
  one shared package with one-way dependencies; the reproducibility policy
  (spawned seed sequences, metadata with every result); reference
  implementations with equivalence tests for fast kernels; six layers of
  tests; two measurable gates for 01 (frame rate of the live view, speed of
  the sandpile kernel).
- **Roadmap.** Versions 01–05 with acceptance criteria, the expansion order
  from 06, the definition of done for a module, and five proposals that need
  a decision.
- **Specification template.** The 14 sections of the brief, with writing
  conventions and a review checklist.

### Checks

- `scripts/verify_numbers.py` recomputes 29 numbers quoted in the notes
  (critical points, sandpile height probabilities, $\det\Delta$ counts,
  addition periods, branching asymptotics, RG fixed points); all agree.
- `scripts/check_references.py` looks up the 324 DOI links of the
  bibliography on Crossref; all titles match.
- Formulas were checked with GitHub's own Markdown renderer.

### Open

- What "angle of drainage periodic function" referred to: the source of the
  phrase would settle it.
- Proposals P1–P5 in the roadmap.
