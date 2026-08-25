# Answer: Fundamental Group of RP²

## Key Idea / Intuition

The sphere $S^2$ is simply connected (every loop can be contracted), and it sits as a **2-sheeted covering space** over $\mathbb{RP}^2$. Covering space theory gives us a beautiful shortcut: the fundamental group of the base space is exactly the **group of deck transformations** of the covering, which here is $\mathbb{Z}/2\mathbb{Z}$ — the antipodal map and the identity. The surprise is geometric: walking a full loop in $\mathbb{RP}^2$ corresponds to a *path* (not a loop) in $S^2$ connecting antipodal points; walking it *twice* gives a genuine loop in $S^2$, which contracts — and this contraction projects down to a null-homotopy in $\mathbb{RP}^2$.

---

## Formal Proof / Solution

### Part (a): $q: S^2 \to \mathbb{RP}^2$ is a 2-sheeted covering

For any point $[x] \in \mathbb{RP}^2$, choose an open hemisphere $U \subset S^2$ containing $x$ (so small that it doesn't intersect its antipodal image $-U$). Then the open set $V = q(U) \subset \mathbb{RP}^2$ is evenly covered:

$$q^{-1}(V) = U \sqcup (-U),$$

and $q$ restricts to a homeomorphism on each sheet. Since every point has exactly 2 preimages ($x$ and $-x$), this is a 2-sheeted covering.

---

### Part (b): Computing $\pi_1(\mathbb{RP}^2)$

**Key theorem from covering space theory:** If $p: \tilde{X} \to X$ is a covering with $\tilde{X}$ simply connected, then

$$\pi_1(X, x_0) \cong \text{Deck}(\tilde{X}/X) \cong \text{Fiber}(x_0) = p^{-1}(x_0).$$

More precisely, there is an exact sequence

$$1 \to \pi_1(S^2) \to \pi_1(\mathbb{RP}^2) \to \mathbb{Z}/2\mathbb{Z} \to 1.$$

Since $S^2$ is simply connected, $\pi_1(S^2) = 1$, so:

$$\pi_1(\mathbb{RP}^2) \cong \mathbb{Z}/2\mathbb{Z}.$$

**Explicitly:** The generator $\gamma$ of $\pi_1(\mathbb{RP}^2)$ is the image of any path in $S^2$ from $x$ to $-x$ (the two antipodal preimages of a basepoint). This projects to a loop in $\mathbb{RP}^2$. Traversed twice, it lifts to a loop $x \to -x \to x$ in $S^2$, which is null-homotopic in $S^2$ (since $\pi_1(S^2) = 0$), and the null-homotopy projects down to a null-homotopy in $\mathbb{RP}^2$.

Hence $\gamma^2 = 1$ in $\pi_1(\mathbb{RP}^2)$, confirming $\pi_1(\mathbb{RP}^2) = \mathbb{Z}/2\mathbb{Z}$.

---

### Part (c): Why this is surprising

It seems paradoxical: going around a loop twice should "feel more non-trivial," not less. In $\mathbb{Z}$ (like $\pi_1(S^1)$), winding twice gives a strictly bigger element. But $\mathbb{Z}/2\mathbb{Z}$ is different: the only element of order 2 satisfies $\gamma + \gamma = 0$.

Geometrically: a single traversal lifts to a *path* (not a loop) in $S^2$, so it has no chance to be contracted *in* $S^2$. A double traversal lifts to an actual loop in $S^2$, and $S^2$ being simply connected means this loop contracts. The contraction in $S^2$ is equivariant enough to descend to one in $\mathbb{RP}^2$.

This is a manifestation of the general fact: **torsion in $\pi_1$ has no analogue in $\pi_1(S^1) \cong \mathbb{Z}$ (which is torsion-free), and $\mathbb{RP}^2$ provides the simplest compact surface with torsion fundamental group.**

---

## Summary

$$\boxed{\pi_1(\mathbb{RP}^2) \cong \mathbb{Z}/2\mathbb{Z}}$$

The 2-sheeted covering $S^2 \to \mathbb{RP}^2$ with simply connected total space forces the fundamental group to equal the fiber cardinality — the only group of order 2.

Written to: [questions/2026-08-16_pm.md](questions/2026-08-16_pm.md)
