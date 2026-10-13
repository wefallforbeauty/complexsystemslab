# complexsystemslab 00

An interactive mathematical laboratory for complex systems: self-organized
criticality, phase transitions, mean-field theory, renormalization,
synchronization and pattern formation. The aim is to investigate established
models: change their parameters, watch their dynamics, state hypotheses, test
them with reproducible computational experiments, and compare what the
simulations show with what the mathematics proves or predicts.

The project grows version by version. **00** is the research map and the
plan; it contains no simulation code yet. **01** will bring the first
module, the Abelian sandpile with its branching-process mean field. What
changed in this version: [UPDATE_LOG.md](UPDATE_LOG.md).

## What version 00 contains

Research notes in [`docs/research`](docs/research):

- [**01 · A map of the field**](docs/research/01-field-map.md): how
  microscopic rules produce macroscopic laws; four mechanisms (mean-field
  limits, criticality, instabilities, slow driving); twelve families of
  models; which links between them are theorems, which are approximations
  and which are analogies.
- [**02 · Model catalogue**](docs/research/02-model-catalogue.md): about
  forty candidate models with their rules, exact results, observables,
  validation anchors and pitfalls; a comparison table; a ranking of the
  additional models; candidates the brief did not list.
- [**03 · Terminology**](docs/research/03-terminology.md): what "angle of
  drainage periodic function" and "self-sustained criticality" can and
  cannot mean; the original BTW rules quoted from the 1987 and 1988 papers
  and how they differ from Dhar's Abelian sandpile.
- [**04 · Bibliography**](docs/research/04-bibliography.md): a short
  annotated list to start from, then every work cited, all checked against
  the DOI registry.
- [**05 · Experiments, open questions and
  misconceptions**](docs/research/05-experiments-and-open-questions.md):
  the experiment protocol, the procedure for claiming a power law, twelve
  experiments, open problems and common mistakes.

Plan in [`docs/plan`](docs/plan) and [`docs/specs`](docs/specs):

- [**Architecture**](docs/plan/architecture.md): Python with NumPy and
  SciPy; Numba only after profiling; Streamlit for the app, Jupyter for
  research notebooks, one shared package; the reproducibility, testing and
  performance policies.
- [**Roadmap**](docs/plan/roadmap.md): the six stages, versions 01 to 05 with
  acceptance criteria, the expansion order, and proposals that need a
  decision.
- [**Specification template**](docs/specs/TEMPLATE.md): the 14-part
  mathematical specification every model gets before it is coded.

## The first modules

| Version | Model | Mean-field companion | Exact results used for validation |
|---|---|---|---|
| 01 | Abelian (BTW) sandpile | Galton–Watson branching process | Number of recurrent configurations $\det\Delta$; height probabilities on $\mathbb{Z}^2$; mean toppling numbers; the $n^{-3/2}$ law |
| 02 | Ising model | Curie–Weiss and Bethe | Exact enumeration; Kaufman and Ferdinand–Fisher; Onsager; Yang |
| 03 | Kuramoto model | Ott–Antonsen equations | $K_c=2/(\pi g(0))$; $r=\sqrt{1-2\Delta/K}$ for Lorentzian frequencies |

Version 04 adds finite-size scaling, power-law statistics and the Manna and
Oslo sandpiles; 05 adds renormalization (block spins, exact decimation,
percolation cells, period doubling). The reasons for this order are in the
[roadmap](docs/plan/roadmap.md#2-the-first-three-modules).

## Principles

1. **Specification before code.** A model is coded only after its
   mathematics, assumptions, observables and validation criteria are written
   down.
2. **Evidence labels.** Every claim is marked as proven, exact, approximate,
   numerical, conjectured, heuristic or contested, with a source.
3. **Validation against exact results**, not only against pictures.
4. **Reproducibility.** Versioned configurations, explicit seeds, metadata
   with every result.
5. **Honest statistics.** No power law from a straight line on a log–log
   plot; error bars and fitting ranges are always reported.

## Reading the documents

The documents are Markdown with LaTeX formulas and Mermaid diagrams. GitHub
renders both. Other Markdown viewers need math support enabled to show the
formulas.

## Checking the documents yourself

Two scripts repeat the checks behind the notes. They need Python 3.12 or
newer.

```sh
python -m venv .venv
# Activate it
#   Windows (PowerShell):  .venv\Scripts\Activate.ps1
#   macOS and Linux:       source .venv/bin/activate
pip install numpy
python scripts/verify_numbers.py      # recomputes the numbers quoted in the notes
python scripts/check_references.py    # looks up every DOI in the bibliography (needs internet)
```

On systems where `python` points to Python 2 or is missing, use `python3`.
