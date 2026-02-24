# The γ-Invariant of Goldbach–Frey Curves

**Paper #16 in the Titan Project series**

Cluster depths and conjectural bounds for the wild conductor at 2.

## Key Results

**Lemma 2.1 (Structural Lemma, proved):** For distinct odd primes p ≠ q, exactly one of v₂(p−q) and v₂(p+q) equals 1, and the other is ≥ 2.

**Conjecture 3.1 (γ-Conjecture):**
```
         ⎧ 8   if γ = 2   (conjectural, 5/5 Magma ✓)
  f₂ =  ⎨ 7   if γ = 3   (conjectural, 2/2 Magma ✓)
         ⎩ 4   if γ ≥ 4   (PROVED — Proposition 3.2)
```
where γ = max(v₂(p−q), v₂(p+q)).

**Proposition 3.2 (Stabilisation, proved unconditionally):**
For all γ ≥ 4, f₂ = 4. Proof uses:
- Paper #15: Jac(C) ~ E₁ × E₂, so f₂(Jac) = f₂(E₁) + f₂(E₂)
- j-invariant: v₂(j) = 6 − 2γ < 0 for γ ≥ 4
- Ogg's theorem: Kodaira type I_n* ⟹ f₂(E) = 2 at any prime
- Therefore f₂(Jac) = 2 + 2 = 4. No Magma dependency.

**Remark 3.4 (Phase transition):** v₂(j) = 6 − 2γ reveals:
- γ ≤ 3: potentially good reduction (wild ramification possible)
- γ ≥ 4: potentially multiplicative (Swan conductor vanishes)

**Important caveats (γ ≤ 3 only):**
- The cluster picture does *not* directly compute Swan at p=2
- Magma values rely on Ogg heuristic with no correctness guarantee at v₂(Δ) ≥ 12

## The Cluster Picture

The wild conductor is controlled by how close p and q are in the 2-adic metric:

```
γ ↑  ⟹  deeper cluster  ⟹  sw ↓  ⟹  f₂ ↓
```

The threshold at γ = 4 marks the transition from wild to tame semistable reduction.

## Repository Structure

```
├── paper/
│   ├── Wild_Conductor.pdf       Final paper (5 pages)
│   └── Wild_Conductor.tex       LaTeX source
├── figures/
│   ├── fig_wild_conductor.pdf   Figure 1: f₂ vs γ + density
│   └── fig_cluster_tree.pdf     Figure 2: cluster trees + γ distribution
├── scripts/
│   ├── wild_conductor.py        Main analysis
│   ├── cluster_picture.py       Cluster picture computation
│   └── fig_wild_conductor.py    Figure generation
├── README.md
└── LICENSE
```

## Series Context

| # | Paper | Key Result |
|---|-------|------------|
| 12 | True Conductor Validation | Cond_odd = [rad_odd(pqM\|p−q\|)]² |
| 13 | Universal Tame Semistability | f_r = 2 at all odd primes |
| 14 | Conductor Census | 425,082 pairs, bandwidth stability |
| 15 | Weil Restrictions | Jac(C) ~ Res(E), Asai lift |
| **16** | **Wild Conductor (this paper)** | **f₂(γ) = 8/7/4, complete formula** |

## License

MIT
