---
name: "Covering Space of Wedge of Circles Has Larger Fundamental Group"
type: "topology"
tags: ["covering spaces", "fundamental group", "free groups", "Nielsen-Schreier", "graphs"]
date: "2026-07-28"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Introduction to Topological Manifolds, John M. Lee; also Algebraic Topology folklore"
---
# The Covering Space of a Wedge of Circles

Consider the space $X = S^1 \vee S^1$ (two circles joined at a point). Label the two loops $a$ and $b$, so $\pi_1(X, x_0) \cong F_2 = \langle a, b \rangle$, the free group on two generators.

Now consider the following 2-sheeted covering space $\tilde{X}$ of $X$:

- Two vertices $\tilde{x}_0$ and $\tilde{x}_1$.
- The loop $a$ at $x_0$ lifts to an edge from $\tilde{x}_0$ to $\tilde{x}_1$ (and back), i.e., $a$ **swaps** the two sheets.
- The loop $b$ at $x_0$ lifts to a loop at $\tilde{x}_0$ and a loop at $\tilde{x}_1$, i.e., $b$ **fixes** each sheet.

**Question:** What is the fundamental group $\pi_1(\tilde{X}, \tilde{x}_0)$? Identify it explicitly as a subgroup of $F_2 = \langle a, b \rangle$, and explain why this example is surprising.

*Hint: Use the theory of covering spaces — the fundamental group of the covering space corresponds to a subgroup of $\pi_1(X)$ via the induced map.*
