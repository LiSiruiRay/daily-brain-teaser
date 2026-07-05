---
name: "Ridge Regression as Augmented OLS"
type: "ML/Stats"
tags: ["ridge regression", "data augmentation", "shrinkage", "normal equations", "regularization"]
date: "2026-07-05"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, 2nd ed., Hastie, Tibshirani, Friedman — Ex. 3.12"
---
# Ridge Regression as Augmented OLS: The Data-Augmentation Trick

Recall that the ridge regression estimator for $y = X\beta + \varepsilon$ minimizes

$$\text{RSS}_\lambda(\beta) = \|y - X\beta\|^2 + \lambda\|\beta\|^2.$$

**Problem:** Show that this is *exactly equivalent* to performing ordinary least squares (no penalty at all) on an augmented dataset $(\tilde{X}, \tilde{y})$, where

$$\tilde{X} = \begin{pmatrix} X \\ \sqrt{\lambda}\, I_p \end{pmatrix}, \qquad \tilde{y} = \begin{pmatrix} y \\ 0 \end{pmatrix}.$$

That is, show that $\hat{\beta}_{\text{ridge}} = (\tilde{X}^T \tilde{X})^{-1}\tilde{X}^T \tilde{y}$.

**Bonus reflection:** What does this say conceptually about what ridge regression is *doing* to the data?
