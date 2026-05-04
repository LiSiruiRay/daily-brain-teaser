# Dini's Theorem: When Pointwise Becomes Uniform

**Type:** Real Analysis
**Tags:** Uniform convergence, Pointwise convergence, Compactness, Dini, Continuity
**Date:** 2026-04-25
**Difficulty:** 2/5

---

## Problem

We know that pointwise convergence of continuous functions does **not** in general imply uniform convergence. (Classic counterexample: $f_n(x) = x^n$ on $[0,1]$.)

But now suppose the convergence is **monotone**. Prove:

> Let $f_n : [0,1] \to \mathbb{R}$ be continuous, and suppose $f_n \searrow f$ pointwise (i.e. $f_1 \geq f_2 \geq \cdots$ and $f_n(x) \to f(x)$ for each $x$). If $f$ is also continuous, then $f_n \to f$ **uniformly**.

---

## Why It's Interesting

The counterexample $x^n \to 0$ shows that continuity + pointwise convergence is not enough. Dini's theorem says that one extra assumption — monotonicity — tips the balance. The proof is a slick application of compactness that makes you appreciate why compactness is so powerful. It is also a cautionary reminder: drop any one of the three conditions (compact domain / monotone / continuous limit) and the conclusion fails.

---

*Answer: [view](answer.md)*
