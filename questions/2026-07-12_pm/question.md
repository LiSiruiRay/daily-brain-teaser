---
name: "Precision Matrix and Partial Correlations"
type: "ML/Stats"
tags: ["Gaussian graphical models", "conditional independence", "precision matrix", "partial correlation", "Schur complement"]
date: "2026-07-12"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "The Elements of Statistical Learning, 2nd ed. — Exercise 17.3 and Section 17.3"
---
# The Precision Matrix and Partial Correlations

Let $X = (X_1, X_2, \ldots, X_p)^T$ be a multivariate Gaussian random vector with covariance matrix $\Sigma$ (assumed invertible). Define the **precision matrix** $\Theta = \Sigma^{-1}$.

**Claim:** $X_i$ and $X_j$ are conditionally independent given all other variables $X_{\text{rest}}$ **if and only if** $\Theta_{ij} = 0$.

**Question:** Prove (or give a clean argument for) this claim. In particular, explain *why* zeros in the precision matrix — not in the covariance matrix — encode conditional independence. What does $\Theta_{ij} = 0$ geometrically mean about the conditional distribution?

As a warm-up: why does $\Sigma_{ij} = 0$ (zero covariance) **not** imply conditional independence in general?
