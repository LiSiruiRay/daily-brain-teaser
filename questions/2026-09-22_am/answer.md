# Answer: Cofinite Topology: Compact but Not Hausdorff

## Key Idea / Intuition

The cofinite topology is the "minimal" topology that makes all finite sets closed. Any open cover of an infinite cofinite space can be collapsed to a single open set — because the first open set you pick already covers all but finitely many points, and a finite family handles the rest. This gives compactness almost for free.

For Hausdorff failure: two points cannot be separated because any two nonempty open sets must intersect (their complements are finite, so they cannot partition an infinite space).

Part (c) illustrates a fundamental theorem: a continuous bijection from a compact space to a Hausdorff space is automatically a homeomorphism. The cofinite topology example makes this vivid.

---

## Formal Proof / Solution

### Part (a): $X$ is compact

Let $\{U_\alpha\}$ be an open cover of $X$. Pick any one nonempty set $U_{\alpha_0}$ from the cover. By definition of the cofinite topology, $X \setminus U_{\alpha_0}$ is **finite**, say $X \setminus U_{\alpha_0} = \{x_1, \ldots, x_n\}$.

For each $x_i$, pick some $U_{\alpha_i}$ from the cover containing $x_i$. Then

$$X = U_{\alpha_0} \cup U_{\alpha_1} \cup \cdots \cup U_{\alpha_n}$$

is a **finite subcover**. $\blacksquare$

---

### Part (b): $X$ is not Hausdorff

Take any two distinct points $x, y \in X$. Suppose $U \ni x$ and $V \ni y$ are open sets. Since $X$ is infinite and both $X \setminus U$ and $X \setminus V$ are finite,

$$X \setminus (U \cap V) = (X \setminus U) \cup (X \setminus V)$$

is a **finite** union of finite sets, hence finite. Since $X$ is infinite, $U \cap V$ must be infinite, in particular **nonempty**.

Therefore no two points can be separated by disjoint open sets, so $X$ is **not Hausdorff**. $\blacksquare$

---

### Part (c): $f$ must be a homeomorphism

**Theorem (standard):** A continuous bijection from a compact space to a Hausdorff space is a homeomorphism.

**Proof:** It suffices to show $f$ is a **closed map** (then $f^{-1}$ is continuous).

Let $C \subseteq X$ be closed. Since $X$ is compact and $C$ is a closed subset of a compact space, $C$ is **compact**. The continuous image of a compact set is compact, so $f(C)$ is compact in $Y$. Since $Y$ is Hausdorff, every compact subset of a Hausdorff space is **closed**. Hence $f(C)$ is closed in $Y$. $\blacksquare$

**Consequence for our example:** The cofinite topology on an infinite set $X$ cannot be homeomorphic to **any** Hausdorff topology on $X$ via the identity map, since the identity from $(X, \mathcal{T}_{\text{cofinite}})$ to $(X, \mathcal{T}_{\text{discrete}})$ (which is Hausdorff) is continuous (every cofinite-open set is discrete-open) and bijective, yet **its inverse** (identity from discrete to cofinite) is not continuous — sending a non-cofinite open set to something not open. This is consistent: compact $\not\to$ Hausdorff here because the **discrete** topology on an infinite set is **not** compact.

The deep takeaway: **compact + Hausdorff** is a "just right" pairing — any continuous bijection between such spaces is rigid (a homeomorphism), leaving no room for strictly coarser or finer topologies.
