# Answer: Torus Minus a Point Deformation Retracts onto Wedge

## Key Idea / Intuition

The torus has a beautiful CW structure: one 0-cell, two 1-cells (the longitude and meridian circles), and one 2-cell whose boundary is glued according to $aba^{-1}b^{-1}$. When you remove a point from the interior of the 2-cell, that 2-cell — now punctured — can be **collapsed**: a disk minus an interior point deformation retracts onto its boundary circle. So the whole space collapses onto the 1-skeleton, which is exactly $S^1 \vee S^1$.

The key insight is purely combinatorial/topological: **removing a point from the top-dimensional cell allows that cell to retract to its boundary**, leaving only the lower-dimensional skeleton.

---

## Formal Proof / Solution

**Step 1: CW structure of $T$.**

Give $T$ the standard CW structure:
- One 0-cell: $e^0 = \{p_0\}$
- Two 1-cells: $e^1_a$ and $e^1_b$ (representing the two generating loops)
- One 2-cell: $e^2$ attached via the word $aba^{-1}b^{-1}$

The 1-skeleton is $e^0 \cup e^1_a \cup e^1_b \cong S^1 \vee S^1$.

**Step 2: Remove a point from the interior of $e^2$.**

Choose $p \in \mathrm{Int}(e^2)$, i.e., a point in the open 2-cell. The resulting space is:
$$T \setminus \{p\} = (S^1 \vee S^1) \cup (e^2 \setminus \{p\})$$

**Step 3: The punctured 2-cell retracts to its boundary.**

The open 2-cell $e^2$ is homeomorphic to an open disk $D^2$. Removing a point $p$ from its interior gives a space homeomorphic to $D^2 \setminus \{0\}$, which deformation retracts onto $\partial D^2 = S^1$ by the straight-line retraction:
$$H(x, t) = \frac{(1-t)x + t \cdot \frac{x}{|x|}}{|(1-t)x + t \cdot \frac{x}{|x|}|} \cdot \text{(scaled appropriately)}$$

More precisely, define $r: D^2 \setminus \{0\} \to S^1$ by $r(x) = x/|x|$, and the deformation retraction
$$H(x,t) = \frac{x}{|x|^t}$$
which at $t=0$ is the identity and at $t=1$ is $r$.

**Step 4: The retraction is compatible with the attaching map.**

Since the retraction $H$ fixes $\partial D^2$ pointwise (because $|x| = 1$ on the boundary), it is compatible with the attaching map $\varphi: \partial D^2 \to S^1 \vee S^1$. Therefore, the deformation retraction of $e^2 \setminus \{p\}$ onto $\partial e^2$ induces a deformation retraction of the entire space $T \setminus \{p\}$ onto the 1-skeleton.

**Step 5: Conclusion.**

We have a deformation retraction:
$$T \setminus \{p\} \;\simeq\; S^1 \vee S^1$$

In particular, $\pi_1(T \setminus \{p\}) \cong \pi_1(S^1 \vee S^1) \cong \mathbb{Z} * \mathbb{Z}$, the **free group on two generators** — a dramatic contrast with $\pi_1(T) \cong \mathbb{Z} \times \mathbb{Z}$, which is abelian. Removing just one point from the torus makes the fundamental group non-abelian!
