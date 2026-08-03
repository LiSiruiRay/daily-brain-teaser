---
name: "Polynomials Dense: Orthogonality Forces Zero"
type: "analysis"
tags: ["Weierstrass approximation", "orthogonality", "substitution trick", "density of polynomials", "L2"]
date: "2026-08-03"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
---
# The Stone–Weierstrass Shortcut: Polynomials Dense, but How Dense?

Let $f : [0,1] \to \mathbb{R}$ be continuous and suppose

$$\int_0^1 f(x)\, x^n\, dx = 0 \quad \text{for all } n = 0, 1, 2, 3, \ldots$$

Prove that $f \equiv 0$ on $[0,1]$.

Now here is the twist: what if the condition only holds for all **even** $n = 0, 2, 4, 6, \ldots$? Must $f$ still be identically zero?
