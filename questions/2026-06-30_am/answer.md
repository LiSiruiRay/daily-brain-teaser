# Answer: Quotient of Interval Gives Circle

## Key Idea / Intuition

The interval $[0,1]$ wraps around the circle if we glue its two endpoints together — this is geometrically obvious. The analytic map $t \mapsto e^{2\pi i t}$ does exactly this gluing. The key topological insight is that a **continuous bijection from a compact space to a Hausdorff space is automatically a homeomorphism** — so we don't need to construct the inverse explicitly; compactness does the work for us.

---

## Formal Proof / Solution

**Step 1: Define the candidate map.**

Consider the map $f: [0,1] \to S^1$ defined by

$$f(t) = e^{2\pi i t}.$$

This is continuous, and $f(0) = f(1) = 1 \in S^1$, so $f$ is constant on the equivalence class $\{0, 1\}$ and constant (trivially) on every singleton $\{t\}$ for $t \in (0,1)$.

**Step 2: Factor through the quotient.**

Since $f$ is constant on each equivalence class of $\sim$, the universal property of the quotient topology gives a unique continuous map

$$\tilde{f}: X/{\sim} \;\longrightarrow\; S^1$$

such that $\tilde{f} \circ q = f$, where $q: X \to X/{\sim}$ is the quotient map.

Explicitly, $\tilde{f}([t]) = e^{2\pi i t}$.

**Step 3: $\tilde{f}$ is a bijection.**

- *Surjective:* Every point $e^{2\pi i t} \in S^1$ is hit by some $t \in [0,1]$.
- *Injective:* If $\tilde{f}([s]) = \tilde{f}([t])$, then $e^{2\pi i s} = e^{2\pi i t}$, so $s - t \in \mathbb{Z}$. Since $s, t \in [0,1]$, this forces either $s = t$ or $\{s,t\} = \{0,1\}$. In either case $[s] = [t]$ in $X/{\sim}$.

**Step 4: Apply the compact-to-Hausdorff theorem.**

- $X/{\sim}$ is **compact**: it is the continuous image of the compact space $[0,1]$ under $q$.
- $S^1 \subset \mathbb{R}^2$ is **Hausdorff**.

Now use the following standard theorem:

> **Theorem.** A continuous bijection from a compact space to a Hausdorff space is a homeomorphism.

*Proof sketch:* Let $C \subseteq X/{\sim}$ be closed, hence compact. Its image $\tilde{f}(C)$ is compact, hence closed in the Hausdorff space $S^1$. So $\tilde{f}$ sends closed sets to closed sets, i.e., $(\tilde{f}^{-1})$ is continuous. $\square$

**Conclusion.**

$\tilde{f}: X/{\sim} \xrightarrow{\;\sim\;} S^1$ is a homeomorphism. Geometrically: collapsing the two endpoints of $[0,1]$ to a single point is exactly the same as bending the interval into a circle and gluing the ends. $\blacksquare$

---

**Why does this matter?**

The compact-to-Hausdorff trick is ubiquitous in topology. It saves you from ever having to verify continuity of an inverse directly — compactness is doing the real work. The same argument shows, for instance, that $[0,1]^2 / \partial([0,1]^2) \cong S^2$, or that $\mathbb{R}/\mathbb{Z} \cong S^1$.
