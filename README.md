# The γ-Invariant of Goldbach–Frey Curves

**Paper #16 in the Titan Project series**

Cluster depths and conjectural bounds for the wild conductor at 2.

## Key Results

**Lemma 2.1 (Structural Lemma, proved):** For distinct odd primes p ≠ q, exactly one of v₂(p−q) and v₂(p+q) equals 1, and the other is ≥ 2.

**Conjecture 3.1 (γ-Conjecture, 10/10 against Magma):**
```
         ⎧ 8   if γ = 2
  f₂ =  ⎨ 7   if γ = 3
         ⎩ 4   if γ ≥ 4
```
where γ = max(v₂(p−q), v₂(p+q)).

**Remark 3.2 (Conductor non-additivity, PARI/GP verified):**
Independent Tate algorithm computation shows f₂(E₁)+f₂(E₂) ≠ f₂(Jac) for all 10 test curves. Root cause: Q(i)/Q is ramified at p=2 (disc = −4), so conductor additivity fails at the ramified prime.

**Correct framework — Artin conductor formula for induced representations:**

Since Jac(C) ≅ Res_{Q(i)/Q}(E), the ℓ-adic representation V_ℓ(Jac) ≅ Ind_{G_K}^{G_F} V_ℓ(E). By Serre's formula:
```
  f₂(Jac) = dim(V_ℓ(E)) · v₂(D_{Q(i)/Q}) + f_𝔓(E/Q₂(i))
           =     2       ·       2          + f_𝔓(E)
           = 4 + f_𝔓(E)
```

Equivalent reformulation of the γ-conjecture:
- γ = 2: f_𝔓(E) = 4
- γ = 3: f_𝔓(E) = 3
- γ ≥ 4: f_𝔓(E) = 0 (E has good reduction over Q₂(i))

**Remark 3.3 (Patterns in PARI data):**
- f₂(E₂) = 4 is constant across all γ
- f₂(E₁) ∈ {3, 0, 1} for γ ∈ {2, 3, 4}, perfectly γ-determined
- These provide unconditional evidence that γ captures the 2-adic arithmetic

**Proposition 6.1 (Density, proved via PNT in APs):**
P(f₂=8) = 1/2, P(f₂=7) = 1/4, P(f₂=4) = 1/4. Verified on 425,082 pairs.

**Important caveats:**
- All three regimes of the γ-conjecture remain open (conjectural)
- Magma values rely on Ogg heuristic at v₂(Δ) ≥ 12
- Conductor additivity f_r(Jac) = f_r(E₁)+f_r(E₂) holds only at odd primes
- A proof requires computing f_𝔓(E/Q₂(i)) at 𝔓 = (1+i)

## The Cluster Picture

The wild conductor is controlled by how close p and q are in the 2-adic metric:

```
γ ↑  ⟹  deeper cluster  ⟹  f₂ ↓
```

The threshold at γ = 4 conjecturally marks the point where E acquires good reduction over Q₂(i), causing all wild ramification to vanish.

## Repository Structure

```
├── paper/
│   ├── Wild_Conductor.pdf       Final paper (7 pages)
│   └── Wild_Conductor.tex       LaTeX source
├── figures/
│   ├── fig_wild_conductor.pdf   Figure 1: f₂ vs γ + density
│   └── fig_cluster_tree.pdf     Figure 2: cluster trees + γ distribution
├── scripts/
│   ├── wild_conductor.py        Main γ-analysis and census
│   ├── cluster_picture.py       2-adic cluster picture computation
│   ├── fig_wild_conductor.py    Figure generation
│   ├── tate_verify.py           j-invariant analysis of E₁, E₂
│   └── tate_audit.gp            PARI/GP: rigorous elllocalred for all 10 curves
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
| **16** | **Wild Conductor (this paper)** | **γ-conjecture: f₂ = 8/7/4; Artin conductor formula** |

## License

MIT

