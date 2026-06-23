---
name: "Hawaiian Earring vs Infinite Wedge: Compact vs Not"
type: "topology"
tags: ["compactness", "Hawaiian earring", "wedge sum", "CW topology", "homeomorphism invariants"]
date: "2026-06-23"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Topology (Munkres); Introduction to Topological Manifolds (John M. Lee), Ch. 4"
---
# The Hawaiian Earring's Sibling: The Wedge of Infinitely Many Circles

Consider two spaces:

- **Space A**: The **Hawaiian Earring** $H$ — the union of circles $C_n$ in $\mathbb{R}^2$, where $C_n$ has center $(1/n, 0)$ and radius $1/n$, all passing through the origin.

- **Space B**: The **infinite wedge** $W = \bigvee_{n=1}^{\infty} S^1$ — the countably infinite wedge sum of circles, each attached at a single basepoint.

These two spaces look similar at a glance: both are countably many circles joined at a point. Yet they are **not homeomorphic**.

**Question:** Prove that $H$ and $W$ are not homeomorphic by showing their topologies differ at the basepoint. Specifically, show that the basepoint $p = (0,0) \in H$ does **not** have a neighborhood basis of open sets $U$ such that $U \setminus \{p\}$ is disconnected in the same way as in $W$.

*Alternatively (equivalent formulation):* Show that $H$ is **compact** while $W$ (with the standard CW or quotient topology) is **not compact**, thereby distinguishing them topologically.
