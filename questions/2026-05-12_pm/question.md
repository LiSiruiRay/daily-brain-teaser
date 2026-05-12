---
name: "Klein Bottle Is Non-Orientable and Doesn't Embed in R³"
type: "topology"
tags: ["Klein bottle", "orientability", "Möbius band", "surfaces", "embedding", "fundamental polygon"]
date: "2026-05-12"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "topology/Introduction to Topological Manifolds (John M. Lee).pdf"
---
# The Klein Bottle Has No Embedding in ℝ³

A **Klein bottle** $K$ is formed from a square $[0,1]^2$ by identifying sides as follows:
- $(x, 0) \sim (x, 1)$ (top and bottom glued in the same direction)
- $(0, y) \sim (1, 1-y)$ (left and right sides glued in *opposite* directions)

**Question:** Prove that the Klein bottle is **not orientable**, and use this to conclude it cannot be embedded as a closed surface in $\mathbb{R}^3$.

*Hint: Find a Möbius band inside $K$, and think about what orientability means for an atlas.*
