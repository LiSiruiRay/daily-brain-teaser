---
name: "FTA via Liouville's Theorem"
type: "Complex Analysis"
tags: ["Liouville", "Entire functions", "Fundamental theorem of algebra"]
date: "2026-03-26"
solved: false
comments: ""
related: []
redo: 0
---
# Fundamental Theorem of Algebra via Liouville

## Problem

Prove that every non-constant polynomial $p(z) \in \mathbb{C}[z]$ has at least one root in $\mathbb{C}$.

You may use **Liouville's Theorem**: *every bounded entire function is constant.*

---

## Field
Complex Analysis

## Why It's Beautiful

The Fundamental Theorem of Algebra is a statement about polynomials — pure algebra. Yet the cleanest proof is analytic, using a theorem about entire functions. The proof is essentially **three lines**, and the key move is a clever inversion: consider $1/p(z)$ instead of $p(z)$.

This is a canonical example of complex analysis reaching into algebra in a way that elementary methods cannot match.

## Key Idea / Trick

Suppose $p(z)$ has no root. Then $1/p(z)$ is entire. Since $|p(z)| \to \infty$ as $|z| \to \infty$, the function $1/p(z)$ is bounded. By Liouville, $1/p(z)$ is constant — contradicting that $p$ is non-constant.

## Difficulty
2 / 5

## Tags
Complex Analysis, Liouville's theorem, Entire functions, Fundamental theorem of algebra, Contradiction
