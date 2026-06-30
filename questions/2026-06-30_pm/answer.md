# Answer: Fundamental Group of Doubly Punctured Plane

## Key Idea / Intuition

Removing one point from the plane gives a space homotopy equivalent to a circle — so one "hole" means $\pi_1 \cong \mathbb{Z}$. Removing two points gives a space homotopy equivalent to a **figure-eight** $S^1 \vee S^1$: you can imagine shrinking the plane so the two punctures become the two loops. The figure-eight's fundamental group is computed by Van Kampen's theorem — and the answer is the **free group on two generators**, which is *non-abelian*. This is the first natural example showing that $\pi_1$ need not be abelian.

---

## Formal Proof / Solution

### Step 1: Homotopy Equivalence

Remove $p_1$ and $p_2$ from $\mathbb{R}^2$. We construct a deformation retraction of $\mathbb{R}^2 \setminus \{p_1, p_2\}$ onto the figure-eight $S^1 \vee S^1$.

Concretely: place $p_1 = (-1, 0)$ and $p_2 = (1, 0)$. Consider two small circles $C_1$ centered at $p_1$ and $C_2$ centered at $p_2$, joined at the origin. The region $\mathbb{R}^2 \setminus \{p_1, p_2\}$ deformation retracts onto $C_1 \vee C_2 = S^1 \vee S^1$ by pushing outward from each puncture (radially) and collapsing the "exterior" to the boundary circles. This is the same argument as how $\mathbb{R}^2 \setminus \{p\} \simeq S^1$.

Therefore:
$$\pi_1(\mathbb{R}^2 \setminus \{p_1, p_2\}) \cong \pi_1(S^1 \vee S^1).$$

### Step 2: Van Kampen's Theorem on $S^1 \vee S^1$

Write $S^1 \vee S^1$ as the union of two open sets:
- $U_1 = $ a small open neighborhood of the first circle (a circle with an open arc removed from the second, so $U_1 \simeq S^1$),
- $U_2 = $ a small open neighborhood of the second circle (similarly $U_2 \simeq S^1$),
- $U_1 \cap U_2 = $ a small open arc around the wedge point, which is **contractible**.

By Van Kampen's theorem:
$$\pi_1(S^1 \vee S^1) \cong \pi_1(U_1) *_{\pi_1(U_1 \cap U_2)} \pi_1(U_2) \cong \mathbb{Z} *_{\{e\}} \mathbb{Z} = \mathbb{Z} * \mathbb{Z}.$$

### Step 3: The Answer

**(a)** $\pi_1(\mathbb{R}^2 \setminus \{p_1, p_2\}) \cong \mathbb{Z} * \mathbb{Z}$, the **free group on two generators** $a, b$.

Concretely: $a$ is a loop winding once around $p_1$, $b$ is a loop winding once around $p_2$. Every element is a word like $a^2 b^{-1} a b^3 \cdots$.

**(b)** Is it abelian? **No.** The free group $\mathbb{Z} * \mathbb{Z}$ is non-abelian: the commutator $aba^{-1}b^{-1} \neq e$. Geometrically, "loop around $p_1$ then $p_2$" is genuinely different from "loop around $p_2$ then $p_1$".

**(c) Generalization.** For $\mathbb{R}^2$ with $n$ points removed:
$$\pi_1(\mathbb{R}^2 \setminus \{p_1,\ldots,p_n\}) \cong \underbrace{\mathbb{Z} * \mathbb{Z} * \cdots * \mathbb{Z}}_{n \text{ copies}} = F_n,$$
the free group on $n$ generators. The space deformation retracts onto the $n$-fold wedge $S^1 \vee \cdots \vee S^1$, and Van Kampen gives the free product inductively.

---

### Summary Table

| Punctures | Homotopy type | $\pi_1$ | Abelian? |
|-----------|--------------|---------|---------|
| 0 | $\mathbb{R}^2$ | trivial | yes |
| 1 | $S^1$ | $\mathbb{Z}$ | yes |
| 2 | $S^1 \vee S^1$ | $\mathbb{Z} * \mathbb{Z}$ | **no** |
| $n$ | $\bigvee_n S^1$ | $F_n$ | **no** |

The jump from one to two punctures is the jump from commutativity to its failure.
