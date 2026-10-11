---
name: "Precision Matrix and Conditional Independence"
type: "ML/Stats"
tags: ["Gaussian graphical models", "precision matrix", "conditional independence", "partial correlation", "Schur complement"]
date: "2026-10-11"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "The Elements of Statistical Learning, Chapter 17 (Hastie, Tibshirani, Friedman)"
---
# The Precision Matrix Miracle: Why Zero Entries Mean Independence

Let $X = (X_1, X_2, \ldots, X_p)^T \sim \mathcal{N}(\mu, \Sigma)$ be a multivariate Gaussian, with $\Sigma$ positive definite. Let $\Theta = \Sigma^{-1}$ be the **precision matrix**.

**Show that $X_i$ and $X_j$ are conditionally independent given all other variables $X_{-ij}$ if and only if $\Theta_{ij} = 0$.**

In other words: the sparsity pattern of $\Theta^{-1}$, not $\Sigma$, encodes the conditional independence graph.

Why is this surprising? Give a simple $3$-variable example where $\Sigma_{ij} \neq 0$ (so $X_i, X_j$ are marginally correlated) but $\Theta_{ij} = 0$ (so $X_i \perp X_j \mid X_k$).
