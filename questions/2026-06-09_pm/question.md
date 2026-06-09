---
name: "Hawaiian Earring Is Not Semi-Locally Simply Connected"
type: "topology"
tags: ["fundamental group", "covering spaces", "semi-local simple connectivity", "Hawaiian earring", "counterexample"]
date: "2026-06-09"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Munkres, Topology, §82; Lee, Introduction to Topological Manifolds, Ch. 12"
---
# The Hawaiian Earring Is Not Semi-Locally Simply Connected

Consider the **Hawaiian earring** $H$: the subspace of $\mathbb{R}^2$ defined as the union of circles

$$H = \bigcup_{n=1}^{\infty} C_n, \quad C_n = \left\{(x,y) : \left(x - \frac{1}{n}\right)^2 + y^2 = \frac{1}{n^2}\right\}.$$

All circles pass through the origin $p = (0,0)$, and the radii shrink to zero.

Show that $H$ is **not semi-locally simply connected** at $p$. That is, show that for every open neighborhood $U$ of $p$ in $H$, there exists a loop based at $p$ in $U$ whose homotopy class is **nontrivial** in $\pi_1(H, p)$.

Why does this matter? What classical theorem does it obstruct?
