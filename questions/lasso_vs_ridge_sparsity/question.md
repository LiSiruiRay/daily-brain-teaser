---
name: "Why LASSO Gives Sparsity but Ridge Does Not"
type: "ML/Stats"
tags: ["LASSO", "Ridge", "Sparsity", "Regularization", "Convex geometry"]
date: "2026-04-19"
solved: false
comments: ""
related: []
redo: 0
---
# Why Does LASSO Produce Sparse Solutions but Ridge Does Not?

---

## Problem

Consider minimizing a convex differentiable loss $L(\beta)$ (e.g. least squares) subject to a norm constraint on $\beta \in \mathbb{R}^d$:

$$\min_{\beta} L(\beta) \quad \text{subject to} \quad \|\beta\|_1 \leq t \qquad \text{(LASSO)}$$

$$\min_{\beta} L(\beta) \quad \text{subject to} \quad \|\beta\|_2^2 \leq t \qquad \text{(Ridge)}$$

**Question:** Give a geometric argument for why the LASSO constraint tends to produce solutions with exact zeros (sparse $\hat\beta$), while Ridge does not — even when the unconstrained minimizer $\hat\beta^{\text{OLS}}$ is the same for both.

---

## Why It's Interesting

This is one of the most fundamental and beautiful insights in modern ML. Sparsity is not an assumption baked in — it *emerges* purely from the geometry of the $L^1$ ball. The same loss, the same data, a different shape of constraint: one gives you feature selection for free, the other never does.

---

*Answer: [view](answer.md)*
