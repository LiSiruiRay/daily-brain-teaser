---
name: "Vanishing Integral on All Measurable Sets"
type: "analysis"
tags: ["Lebesgue integration", "measure theory", "differentiation theorem", "null sets"]
date: "2026-05-18"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
---
# The Lebesgue Density Theorem's Sharpest Failure

Let $f : [0,1] \to \mathbb{R}$ be a measurable function satisfying:

$$\int_a^b f(x)\, dx = 0 \quad \text{for every } 0 \le a \le b \le 1.$$

**Prove that $f = 0$ almost everywhere.**

Now here is the twist: exhibit a *non-zero* measurable function $g : [0,1] \to \mathbb{R}$ such that

$$\int_E g(x)\, dx = 0$$

for **every measurable set** $E \subseteq [0,1]$... or explain carefully why no such $g$ can exist.
