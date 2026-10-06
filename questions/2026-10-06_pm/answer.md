# Answer: Cofinite Topology: Compact but Not Closed

## Key Idea / Intuition

In the cofinite topology, open sets are "almost everything" — so any two non-empty open sets must overlap (their complements are finite, so they can't cover the whole space while being disjoint). This destroys the Hausdorff property. But it also forces every open cover to be "wasteful": a single open set already covers all but finitely many points, so any cover reduces to a finite one almost immediately. Compactness follows for free, yet compact sets aren't closed in the usual sense.

---

## Formal Proof / Solution

Let $X = \mathbb{Z}_{>0}$ with the cofinite topology $\tau$.

### Part (a): $T_1$ but not Hausdorff

**$T_1$:** We need every singleton $\{n\}$ to be closed, i.e., $X \setminus \{n\}$ is open. Indeed, $X \setminus (X \setminus \{n\}) = \{n\}$ is finite, so $X \setminus \{n\}$ is cofinite, hence open. ✓

**Not Hausdorff:** Suppose $U, V$ are non-empty open sets with $U \cap V = \emptyset$. Then

$$X = (X \setminus U) \cup (X \setminus V)$$

so $X$ is a union of two finite sets (since $U$ and $V$ are non-empty open, their complements are finite). But $X = \mathbb{Z}_{>0}$ is infinite — contradiction. So no two non-empty open sets are disjoint, and we cannot separate any two distinct points. ✗

### Part (b): Every subset is compact

Let $A \subseteq X$ with the subspace topology (which is again cofinite: relatively open sets in $A$ are $\emptyset$ or sets with finite complement in $A$). Let $\{U_\alpha\}$ be an open cover of $A$.

Pick any single $U_{\alpha_0}$ in the cover with $U_{\alpha_0} \neq \emptyset$. Then

$$A \setminus U_{\alpha_0}$$

is finite (it has finite complement in $A$, since $U_{\alpha_0}$ is relatively open and non-empty). Say $A \setminus U_{\alpha_0} = \{a_1, a_2, \ldots, a_k\}$. For each $a_i$, pick some $U_{\alpha_i}$ in the cover containing $a_i$.

Then $\{U_{\alpha_0}, U_{\alpha_1}, \ldots, U_{\alpha_k}\}$ is a finite subcover. Since the cover was arbitrary, $A$ is compact. ✓

### Part (c): Compact $\not\Rightarrow$ Closed (without Hausdorff)

Take any finite set, say $A = \{1, 2, 3\}$. Its complement is infinite and hence not cofinite (it doesn't have a finite complement), so $A$ is **not** open, meaning $X \setminus A$ is not closed... wait, let's be precise:

$A$ is closed iff $X \setminus A$ is open iff $X \setminus (X \setminus A) = A$ is finite. So finite sets **are** closed.

More strikingly: take $A = \{1, 3, 5, 7, \ldots\}$ (the odd positive integers). Then $A$ is infinite, so $X \setminus A$ (the even positive integers) is also infinite — hence $X \setminus A$ is **not** cofinite, so it's **not** open, so $A$ is **not closed**.

Yet by Part (b), $A$ is **compact**.

So in $(X, \tau)$:

$$A = \{1, 3, 5, 7, \ldots\} \text{ is compact but NOT closed.}$$

This contrasts sharply with the Hausdorff case, where every compact subset of a Hausdorff space is closed (the standard proof: for each point outside, use disjoint open sets to separate, then extract a finite subcover to build an open set around the exterior point). The cofinite topology on an infinite set is the "canonical" example showing Hausdorff is essential. $\blacksquare$

**Summary table:**

| Property | Cofinite on $\mathbb{Z}_{>0}$ |
|---|---|
| $T_1$ | ✓ |
| Hausdorff ($T_2$) | ✗ |
| Every subset compact | ✓ |
| Compact $\Rightarrow$ Closed | ✗ |
