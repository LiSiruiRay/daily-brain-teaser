---
name: "Olivier's Theorem: Decreasing Terms Are o(1/n)"
type: "analysis"
tags: ["series", "monotone sequences", "Cauchy criterion", "Cauchy condensation", "counterexample"]
date: "2026-10-26"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
---
# Olivier's Theorem: Decreasing Terms of a Convergent Series Are $o(1/n)$

Let $(a_n)_{n\ge 1}$ be a **non-increasing** sequence of real numbers such that $\sum_{n=1}^\infty a_n$ converges.

**(a)** Prove that
$$\lim_{n\to\infty} n\,a_n = 0.$$

**(b)** Show that monotonicity cannot be dropped. Give a sequence of **positive** terms with $\sum a_n < \infty$ but $n a_n \not\to 0$.

**(c)** Show that the converse of (a) fails. Give a non-increasing positive sequence with $n a_n \to 0$ but $\sum a_n = \infty$.

*(Think for 5 minutes. The whole of (a) fits in one line once you see which block of terms to look at.)*

---

**Field:** Real analysis (series)

**Why it's interesting:** Convergence of $\sum a_n$ alone only gives $a_n \to 0$, with no rate at all. Adding the purely qualitative hypothesis "monotone" upgrades this to a quantitative statement, $a_n = o(1/n)$. This is the germ of Cauchy condensation, and it is the reason the harmonic series sits exactly at the boundary of convergence.

**Difficulty:** 2 / 5
