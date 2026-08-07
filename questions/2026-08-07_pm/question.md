---
name: "Integer-Valued Polynomials and the Binomial Basis"
type: "Putnam"
tags: ["integer-valued polynomials", "Newton forward differences", "binomial coefficients", "change of basis", "algebra"]
date: "2026-08-07"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Mathematical folklore / Putnam training; see also Cahen-Chabert 'Integer-Valued Polynomials'"
---
# The Polynomial Divisibility Chain

Let $p(x)$ be a polynomial with integer coefficients such that $p(0) = 0$ and $p(1) = 1$. Prove that for every positive integer $n$, there exists an integer $k$ such that

$$p(k) \equiv 0 \pmod{n!}$$

Wait — let's make this a concrete and beautiful puzzle first.

**The Problem (Putnam 1990, B-1 flavored):**

Show that if $p(x)$ is a polynomial with real coefficients such that $p(n) \in \mathbb{Z}$ for every integer $n \geq 0$, then $p(n) \in \mathbb{Z}$ for every integer $n$ (including negative integers).

**Bonus observation:** Find the "right" basis of polynomials that makes this completely transparent.
