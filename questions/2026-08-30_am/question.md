---
name: "LOO Risk That Knows Its Smoother"
type: "ML/Stats"
tags: ["linear smoother", "hat matrix", "cross-validation", "leverage", "fixed-point argument"]
date: "2026-08-30"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "The Elements of Statistical Learning, Hastie, Tibshirani & Friedman, 2nd ed., Exercise 5.13 and Section 5.4"
---
# The LOO Risk That Knows Its Smoother

Suppose you fit a **linear smoother** to data $(x_1, y_1), \ldots, (x_n, y_n)$, meaning the fitted values satisfy

$$\hat{\mathbf{y}} = \mathbf{H} \mathbf{y}$$

for some **hat matrix** $\mathbf{H}$ that does **not** depend on $\mathbf{y}$ (e.g., smoothing splines, kernel regression, ridge regression, local linear fits).

The leave-one-out (LOO) cross-validated residual for observation $i$ is

$$\hat{e}_i^{(-i)} = y_i - \hat{y}_i^{(-i)},$$

where $\hat{y}_i^{(-i)}$ is the prediction at $x_i$ from the model trained **without** observation $i$.

**Show that**

$$\hat{e}_i^{(-i)} = \frac{y_i - \hat{y}_i}{1 - H_{ii}},$$

where $H_{ii}$ is the $i$-th diagonal element of $\mathbf{H}$.

This is remarkable: you get **exact** LOO error for **all** $n$ folds from a **single** model fit.
