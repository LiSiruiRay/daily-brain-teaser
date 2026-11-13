---
name: "Maximize I(f) − J(f): Pointwise Optimization"
type: "Putnam"
tags: ["pointwise optimization", "completing the square", "functionals", "calculus of variations"]
date: "2026-11-13"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Putnam 2006 B5 (materials/putnam/2006.pdf)"
---
# Maximize $I(f)-J(f)$ Over All Continuous $f$

For each continuous function $f:[0,1]\to\mathbb{R}$, define

$$
I(f)=\int_0^1 x^2 f(x)\,dx, \qquad J(f)=\int_0^1 x\,\big(f(x)\big)^2\,dx.
$$

Find the maximum value of $I(f)-J(f)$ over all such $f$, and find the function $f$ that achieves it.

---

**Field:** Analysis / optimization (calculus of variations, in its simplest form)

**Why it's interesting:** It looks like a calculus-of-variations problem. You might expect Euler–Lagrange equations, Cauchy–Schwarz, or a clever test function. None of that is needed. The functional contains no derivatives of $f$, so the values $f(x)$ at different points never interact. The infinite-dimensional problem therefore breaks into infinitely many one-variable problems. Each one is a high-school exercise in maximizing a quadratic.

**Difficulty:** 2 / 5

**Tags:** pointwise optimization, completing the square, functionals

**Source:** Putnam 2006, Problem B5 (`materials/putnam/2006.pdf`)
