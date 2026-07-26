---
name: "The SVM That Saw Only Dot Products"
type: "ML/Stats"
tags: ["SVM", "kernel trick", "dual formulation", "Mercer kernel", "RKHS"]
date: "2026-07-26"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Hastie, Tibshirani, Friedman (2nd ed.), Chapter 12"
---
# The SVM That Saw Only Dot Products

You are given a training set $\{(x_i, y_i)\}_{i=1}^N$ with $x_i \in \mathbb{R}^p$ and $y_i \in \{-1, +1\}$. The soft-margin SVM solves

$$\min_{\beta, \beta_0} \frac{1}{2}\|\beta\|^2 + C\sum_{i=1}^N \xi_i \quad \text{subject to } y_i(x_i^T \beta + \beta_0) \geq 1 - \xi_i,\ \xi_i \geq 0.$$

After solving the dual, the decision function is

$$\hat{f}(x) = \sum_{i=1}^N \hat{\alpha}_i y_i \langle x_i, x \rangle + \hat{\beta}_0.$$

Now suppose instead of raw features $x$, you map every point to a very high-dimensional (even infinite-dimensional) feature space via $\phi: \mathbb{R}^p \to \mathcal{H}$, and you **only have access to** $k(x, x') = \langle \phi(x), \phi(x') \rangle_{\mathcal{H}}$ — you can never compute $\phi(x)$ explicitly.

**The question:** Can you still train and deploy the SVM decision function entirely using the kernel $k$, without ever computing $\phi(x)$ explicitly? If yes, write out the dual objective and decision function purely in terms of $k$, and explain conceptually why the geometry of the primal problem is fully captured by dot products alone.
