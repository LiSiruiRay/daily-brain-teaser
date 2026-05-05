---
name: "Orthogonality to All Monomials Forces Zero"
type: "analysis"
tags: ["Weierstrass approximation", "Orthogonality", "Density argument", "L2"]
date: "2026-03-30"
solved: false
comments: ""
related: []
redo: 0
---
# Orthogonality to All Monomials Forces Zero

## Problem

Let $f: [0,1] \to \mathbb{R}$ be continuous. Suppose that
$$\int_0^1 f(x)\, x^n\, dx = 0 \quad \text{for every integer } n \geq 0.$$

Prove that $f(x) = 0$ for all $x \in [0,1]$.

---

## Field
Real Analysis

## Why It's Beautiful

The hypothesis looks weak — you only know that $f$ is "orthogonal" to each monomial $1, x, x^2, x^3, \ldots$ But the conclusion is as strong as it gets: $f$ must be identically zero.

The proof is a beautiful two-step argument: first extend the orthogonality from monomials to **all polynomials** (by linearity), then from polynomials to **$f$ itself** (by the Weierstrass Approximation Theorem). The key move is choosing the approximating polynomial to be $f$ itself — giving $\int_0^1 f^2 \approx 0$, and since $f^2 \geq 0$, this forces $f = 0$.

It's an elegant example of how a **density argument** (dense subsets of function spaces) turns a hypothesis about a small class of functions into a global conclusion.

## Key Idea / Trick

1. By linearity, $\int_0^1 f(x) p(x)\, dx = 0$ for every polynomial $p$.
2. By Weierstrass, there exist polynomials $p_k \to f$ uniformly on $[0,1]$.
3. Then $\int_0^1 f(x)^2\, dx = \lim_{k\to\infty} \int_0^1 f(x) p_k(x)\, dx = 0$.
4. Since $f^2 \geq 0$ and continuous with zero integral, $f \equiv 0$.

## Difficulty
3 / 5

## Tags
Real Analysis, Weierstrass approximation theorem, Orthogonality, Continuous functions, Density argument, $L^2$
