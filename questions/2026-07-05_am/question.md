---
name: "Curse of Dimensionality: Nearest Neighbor Bias"
type: "ML/Stats"
tags: ["curse of dimensionality", "nearest neighbor", "bias", "high dimensions", "local methods"]
date: "2026-07-05"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Hastie, Tibshirani, Friedman, 2nd ed., Section 2.5"
---
# The Blessing of Dimensions: When Does the Nearest Neighbor Lie?

You have $n$ training points drawn i.i.d. uniformly from the $d$-dimensional unit hypercube $[0,1]^d$, and you want to predict at the origin $\mathbf{0}$.

The **1-nearest neighbor** classifier uses the single closest training point to make its prediction.

To "capture" a fraction $r$ of the data (i.e., so that the expected number of training points within a ball of radius $\ell$ around the origin is $rn$), the required edge length $\ell$ of a sub-cube satisfies:

$$\ell = r^{1/d}.$$

**The puzzle:** Suppose you want to use the nearest $r = 1\%$ of the data to make a local estimate. Compute $\ell$ for $d = 1, 2, 10$ and explain what this reveals about nearest-neighbor methods in high dimensions. What is the conceptual implication for the bias of 1-NN?

*Note: Use $r = 0.01$ throughout.*
