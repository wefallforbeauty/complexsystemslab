# Model specification template

Every model in the laboratory gets a specification in `docs/models/<model>.md`
before any code is written. It is the reference for the implementation, the
tests and the app's Mathematics tab. Copy this file, keep all 14 sections,
and write "not applicable" with a reason where a section does not apply.

**Conventions.**

- Display equations go in fenced `math` blocks (they render on GitHub, and
  the app converts them for its own renderer).
- Inline mathematics uses single dollar signs. Inside them, avoid a backslash
  followed by punctuation such as `\{`, `\,` or `\|`; GitHub strips the
  backslash. Use `\lbrace`, `\rbrace`, `\lvert`, `\rvert` and `\Vert`
  instead.
- Every claim carries an evidence label from the
  [field map](../research/01-field-map.md#evidence-labels): **[proven]**,
  **[exact]**, **[approx]**, **[numerical]**, **[conjecture]**,
  **[heuristic]** or **[contested]**, together with a reference.

---

```text
# <Model name>

Status: draft | reviewed | implemented (version NN)
Module: complexsystemslab.models.<module>
Families: <families from the field map>
Main references: <author year; …>
```

## 1. State space

The configurations and the state variables: the set of sites or agents, the
local state space, the configuration space, and any auxiliary variables
(clocks, thresholds, random fields). State which configurations are allowed
(for example, stable sandpile configurations) and which are transient.

## 2. Parameters

| Symbol | Meaning | Units | Allowed range | Default | Notes |
|---|---|---|---|---|---|

Include system size, boundary choice and update scheme when they act as
parameters. State which parameters are redundant (for example, only $J/T$
matters in the Ising model).

## 3. Dynamics

The transition rule, recurrence, differential equation or transition
probabilities, written exactly, including:

- the update order (sequential, random sequential, synchronous) and what one
  unit of time means;
- how and when random numbers are drawn;
- what happens at the boundary.

## 4. Assumptions

The modelling choices and the conditions under which they are reasonable:
locality, homogeneity, time-scale separation, absence of inertia,
well-mixedness, and so on. Say which assumptions the model makes on purpose
and which are only conveniences.

## 5. Initial and boundary conditions

Exactly as implemented: their names in the code, how they are stored, and how
they enter the dynamics. Note naming conflicts with the literature (for
example "open" and "closed" boundaries in BTW's papers versus today's
usage).

## 6. Fixed points and stationary states

Absorbing states, invariant measures, steady states, periodic orbits; their
stability and how they are reached. Distinguish stationarity of a finite
system from statements about the infinite system.

## 7. Conservation laws and invariants

Which quantities are conserved, which are conserved except at boundaries or
sinks, and which are not conserved. Each invariant becomes a property-based
test.

## 8. Analytical results

Derivations, proofs (or proof sketches with references), stability analyses,
limiting cases, exact solutions. Each result has an evidence label and a
reference. Derivations go step by step, with every assumption stated where it
is used.

## 9. Approximate results

Mean-field, pair approximation, expansions, scaling arguments, each with its
assumptions (factorization, closure, homogeneity, the limit of large $N$,
exchangeability, time-scale separation) and its expected domain of validity.
Keep this section separate from Section 8.

## 10. Numerical implementation

Pseudocode for the reference implementation, with a line-by-line
correspondence to Section 3. Note:

- data types;
- the order of operations;
- how random numbers are consumed;
- complexity in time and memory;
- the conditions for accepting a faster kernel (equivalence tests).

## 11. Observables

For each observable: its definition, its estimator, its unit, why it is
relevant, and how its uncertainty is computed (independent replicas,
blocking, bootstrap).

## 12. Validation

| Check | Kind | Expected value or behaviour | Tolerance | Source |
|---|---|---|---|---|

Kinds are invariant, exact, statistical and regression. List the known
results the implementation must reproduce, and the conventions (update
rules, boundaries, sizes) under which they hold.

## 13. Limitations

Simplifying assumptions; computational limits (largest feasible sizes and
times on a laptop); interpretive pitfalls; disagreements in the literature.

## 14. References

The works cited in this specification, each with a DOI or a stable link,
checked as described in the [bibliography](../research/04-bibliography.md).

---

## Review checklist

- [ ] Every symbol is defined before it is used.
- [ ] The update order, time unit and random-number use are explicit.
- [ ] Every claim has an evidence label and a reference.
- [ ] Exact results (Section 8) and approximations (Section 9) are kept apart.
- [ ] Every invariant in Section 7 has a planned test.
- [ ] Section 12 has at least one exact or statistical check that would fail
      for a plausible implementation bug.
- [ ] Limitations include what the model cannot say about real systems.
