---
name: "Monotone Convergence Fails for Decreasing Sequences Without Integrability"
type: "analysis"
tags: ["measure theory", "MCT", "Fatou's lemma", "dominated convergence", "counterexample"]
date: "2026-06-08"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Rudin Real and Complex Analysis, Chapter 1; Stein & Shakarchi Real Analysis Chapter 2"
---
# The Monotone Convergence Fails for Decreasing Sequences Without Integrability

Consider the sequence of functions $f_n : \mathbb{R} \to \mathbb{R}$ defined by

$$f_n(x) = \mathbf{1}_{[n, \infty)}(x), \quad n = 1, 2, 3, \ldots$$

(a) Show that $f_n(x) \to 0$ pointwise for every $x \in \mathbb{R}$.

(b) Show that $\int_{\mathbb{R}} f_n \, d\mu = +\infty$ for every $n$.

(c) Now consider instead $g_n(x) = \mathbf{1}_{[0,n]}(x)$. Show that $g_n \nearrow \mathbf{1}_{[0,\infty)}$ and that the Monotone Convergence Theorem applies correctly here.

**The real question:** Why does Fatou's Lemma give only an inequality for the $f_n$ sequence, and what hypothesis of the Monotone Convergence Theorem does the $f_n$ sequence violate?
