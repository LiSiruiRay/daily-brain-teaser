---
name: "The Fraction That Eventually Stops Simplifying"
type: "Putnam"
tags: ["number theory", "monovariant", "infinite descent", "gcd", "odd part"]
date: "2026-10-30"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Putnam 2025 A1 (materials/putnam/2025s.pdf, solutions by Bhargava, Kedlaya, Ng)"
---
# The Fraction That Eventually Stops Simplifying

Let $m_0$ and $n_0$ be **distinct** positive integers. For every $k \ge 1$, define $m_k$ and $n_k$ to be the relatively prime positive integers such that

$$\frac{m_k}{n_k} = \frac{2m_{k-1}+1}{2n_{k-1}+1}.$$

In words: apply $x \mapsto 2x+1$ to the numerator and the denominator, then reduce to lowest terms.

**Prove** that $2m_k+1$ and $2n_k+1$ are relatively prime for all but finitely many $k$. Equivalently, after finitely many steps, the reduction step never cancels anything again.

*Example:* $\frac14 \to \frac39 = \frac13 \to \frac37 \to \frac7{15} \to \cdots$. Here cancellation happens once, at the first step, and never again.

---

**Field:** Number theory / elementary arguments

**Why it's interesting:** The process looks chaotic, because it is hard to predict when $2m+1$ and $2n+1$ share a factor. Yet a single well-chosen quantity tames it completely. The problem is a clean example of a *monovariant*: you find a positive integer that can never increase and strictly decreases whenever cancellation occurs. Infinite descent then finishes the proof.

**Difficulty:** 2 / 5

**Source:** Putnam 2025, Problem A1 (solutions by Bhargava, Kedlaya, Ng; `materials/putnam/2025s.pdf`).
