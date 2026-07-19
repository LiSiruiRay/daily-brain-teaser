---
name: "Curse of Dimensionality: Nearest Neighbor Becomes Global"
type: "ML/Stats"
tags: ["curse of dimensionality", "k-nearest neighbor", "bias-variance", "high dimensions", "EPE"]
date: "2026-07-19"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Hastie, Tibshirani, Friedman (2nd ed.), Section 2.5, Figure 2.9"
---
# The Curse of Dimensionality: When Your "Nearest" Neighbor Is Far Away

Suppose you have $n$ training points drawn uniformly from the $p$-dimensional unit hypercube $[0,1]^p$, and you want to use the **1-nearest-neighbor** rule to predict at the center point $x_0 = (1/2, 1/2, \ldots, 1/2)$.

To "capture" a fraction $r$ of the data (i.e., the expected fraction of training points within a hypercubic neighborhood of $x_0$), you need a neighborhood of edge length $\ell$ where $\ell^p = r$, so $\ell = r^{1/p}$.

**Question:** For $r = 0.01$ (capturing 1% of the data), compute $\ell$ for $p = 1, 2, 10$. What happens as $p \to \infty$?

Then explain: why does this imply that **1-nearest-neighbor in high dimensions is essentially a global method, not a local one**?

Finally, consider the expected prediction error (EPE) of 1-NN relative to OLS when the true model is linear: $f(x) = x_1$. The EPE ratio starts at approximately $2$ in low dimensions. Give an intuitive explanation for why this ratio is **at least 2** even in $p=1$.
