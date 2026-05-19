---
name: "Hairy Ball Theorem via Degree Theory"
type: "topology"
tags: ["degree of a map", "homotopy", "vector fields", "S^2", "hairy ball theorem", "Poincaré-Hopf"]
date: "2026-05-19"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Mathematical folklore / Topology (Munkres), algebraic topology standard results"
---
# The Hairy Ball Theorem: No Smooth Combing

Let $S^2$ denote the 2-sphere in $\mathbb{R}^3$. A **tangent vector field** on $S^2$ is a continuous map $v: S^2 \to \mathbb{R}^3$ such that $v(x) \perp x$ for every $x \in S^2$ (i.e., $v(x)$ lies in the tangent plane at $x$).

**Prove that any continuous tangent vector field on $S^2$ must vanish somewhere.**

In other words: you cannot comb a hairy ball flat without creating a cowlick.

*(Hint: Suppose $v(x) \neq 0$ for all $x$. Use this to construct a homotopy between the identity map and the antipodal map on $S^2$, then derive a contradiction using the degree of these maps.)*
