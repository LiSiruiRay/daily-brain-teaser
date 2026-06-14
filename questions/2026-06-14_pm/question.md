---
name: "Curse of Dimensionality: Volume Collapse"
type: "ML/Stats"
tags: ["curse of dimensionality", "k-NN", "local methods", "high dimensions", "nonparametric"]
date: "2026-06-14"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Hastie, Tibshirani, Friedman (2nd ed.), Section 2.5"
---
# The Blessing of Dimensionality: Why Nearest-Neighbor Fails in High Dimensions

You have $n$ training points drawn uniformly from the $p$-dimensional unit hypercube $[0,1]^p$, and you want to predict at the origin using the $k$-nearest neighbors within a small neighborhood.

To capture a fraction $r$ of the data (so that you have enough neighbors for a stable estimate), you need a hypercubic neighborhood of side length

$$\ell(p, r) = r^{1/p}.$$

**The question:** Suppose you want to capture just $r = 1\%$ of the data ($r = 0.01$). How large must the side length $\ell$ be when $p = 10$? When $p = 100$?

Now here is the real puzzle: **even if you are willing to use a neighborhood that covers 10% of the range in each dimension ($\ell = 0.1$), what fraction of the data does this neighborhood contain as $p \to \infty$?**

What does this say about the fundamental challenge of local methods (like $k$-NN or local regression) in high dimensions?
