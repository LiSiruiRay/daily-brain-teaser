---
name: "A Polynomial That Lives on the Unit Circle"
type: "Complex Analysis"
tags: ["identity theorem", "reflection", "Blaschke product", "maximum modulus", "polynomials"]
date: "2026-10-22"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
---
# A Polynomial That Lives on the Unit Circle

Let $p$ be a complex polynomial that maps the unit circle into itself:

$$|p(z)| = 1 \quad \text{for all } |z| = 1.$$

**Prove that $p(z) = c\,z^n$ for some $n \ge 0$ and some constant $c$ with $|c| = 1$.**

*(Bonus: what is the analogous statement for rational functions $R$ with $|R(z)| = 1$ on $|z| = 1$?)*

---

**Field:** Complex Analysis

**Why it's interesting:** The hypothesis only concerns the values of $p$ on a circle. It says nothing about the coefficients, and nothing directly about the zeros. Yet it forces $p$ to be a pure monomial. The result illustrates a recurring theme in complex analysis: an equation that holds on a curve becomes an identity everywhere. Here the bridge is the observation that on the unit circle, complex conjugation coincides with inversion, since $\bar z = 1/z$. The bonus generalizes the result to finite Blaschke products, which are the building blocks of inner functions and of disk automorphisms.

**Estimated difficulty:** 2 / 5

**Hint (if you want one):** On $|z|=1$, rewrite $|p(z)|^2 = p(z)\overline{p(z)}$ using $\bar z = 1/z$.
