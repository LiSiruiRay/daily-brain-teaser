---
name: "The Holomorphic Function That Knows Its Zeros Are Real"
type: "Complex Analysis"
tags: ["Gauss-Lucas", "roots of polynomials", "convex hull", "unit circle", "derivative"]
date: "2026-10-01"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Mathematical folklore / classical complex analysis"
---
# The Holomorphic Function That Knows Its Zeros Are Real

Let $f$ be an entire function satisfying:
1. $f$ has only real zeros,
2. $\overline{f(z)} = f(\bar{z})$ for all $z \in \mathbb{C}$ (the **symmetry condition**),
3. $f$ has infinitely many zeros $x_1, x_2, \ldots \in \mathbb{R}$.

Now consider a much simpler question:

**Suppose $f$ is a polynomial with real coefficients, and all zeros of $f$ lie on the unit circle $|z|=1$. Prove that all zeros of $f'$ also lie on the unit circle.**

Wait — is that even true? **Find a counterexample or prove it.**

Actually, let's make the problem precise and beautiful:

> **Problem.** Let $p(z)$ be a polynomial of degree $n \geq 2$ with **all roots on the unit circle** $|z|=1$. Must all roots of $p'(z)$ also lie on the unit circle?

If false, give a counterexample. If true, prove it. What is the correct statement?
