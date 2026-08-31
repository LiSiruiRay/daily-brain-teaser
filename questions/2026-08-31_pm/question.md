---
name: "The Lebesgue Integral That Measures Its Own Level Sets"
type: "analysis"
tags: ["Lebesgue integration", "layer-cake formula", "Fubini-Tonelli", "measure theory", "level sets"]
date: "2026-08-31"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
---
# The Lebesgue Integral That Measures Its Own Level Sets

Let $f: [0,1] \to [0,\infty)$ be a non-negative measurable function. Prove that

$$\int_0^1 f(x)\, dx = \int_0^\infty m\!\left(\{x \in [0,1] : f(x) > t\}\right) dt,$$

where $m$ denotes Lebesgue measure.

Then use this identity to evaluate, almost effortlessly,

$$\int_0^1 x^n\, dx$$

by computing the right-hand side directly.
