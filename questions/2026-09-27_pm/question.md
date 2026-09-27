---
name: "Precision Matrix and Conditional Independence"
type: "ML/Stats"
tags: ["Gaussian graphical models", "conditional independence", "precision matrix", "partial correlation", "graphical lasso"]
date: "2026-09-27"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Hastie, Tibshirani et al., 2nd ed., Chapter 17"
---
# The Covariance That Tells You the Graph

Suppose $X = (X_1, X_2, \ldots, X_p)$ is a multivariate Gaussian random vector with mean zero and covariance matrix $\Sigma$. Let $\Theta = \Sigma^{-1}$ be the **precision matrix**.

**The puzzle:** Show that $\theta_{ij} = 0$ (the $(i,j)$ entry of $\Theta$ is zero) if and only if $X_i \perp\!\!\!\perp X_j \mid X_{\text{rest}}$, i.e., $X_i$ and $X_j$ are **conditionally independent** given all other variables.

In other words: **the zeros of the precision matrix encode the conditional independence graph.** Why?
