---
name: "Suspension Kills Fundamental Group"
type: "topology"
tags: ["fundamental group", "Van Kampen", "suspension", "simply connected", "algebraic topology"]
date: "2026-06-23"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Munkres, Topology; standard algebraic topology folklore"
---
# The Suspension of a Space and Its Fundamental Group

Let $X$ be any path-connected topological space. The **suspension** of $X$, denoted $SX$, is the quotient of $X \times [-1, 1]$ obtained by collapsing $X \times \{1\}$ to a single point (call it $N$, the "north pole") and $X \times \{-1\}$ to another point (call it $S$, the "south pole").

**Prove that $\pi_1(SX) = 0$ for any path-connected $X$.**

In other words: no matter how complicated $\pi_1(X)$ is, suspending once kills it entirely.

*(Bonus to think about: $S^1 = S(\text{two points})$, but $\pi_1(S^1) = \mathbb{Z} \neq 0$. Is there a contradiction? Why not?)*
