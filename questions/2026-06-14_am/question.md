---
name: "The Infinite Ensemble That Doesn't Help"
type: "ML/Stats"
tags: ["ensemble methods", "bias-variance tradeoff", "bagging", "correlation", "variance reduction"]
date: "2026-06-14"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Ch. 8 (Model Averaging and Bagging)"
---
# The Infinite Ensemble That Doesn't Help

Suppose you have infinitely many classifiers $h_1, h_2, h_3, \ldots$, each independently making a binary prediction $h_i(x) \in \{-1, +1\}$ for a fixed input $x$. Each classifier is **identically distributed** with:

$$P(h_i(x) = y^*) = p, \quad P(h_i(x) \neq y^*) = 1 - p$$

where $y^*$ is the true label, and $p > \frac{1}{2}$.

You form the **majority vote** classifier over all $n$ classifiers. By the Law of Large Numbers, as $n \to \infty$, the majority vote is correct with probability approaching 1. Great!

Now consider a twist: the classifiers are **not independent**, but instead all share a common "mistake variable." Specifically:

$$h_i(x) = \begin{cases} y^* & \text{with probability } p \\ -y^* & \text{with probability } 1-p \end{cases}$$

but **all classifiers make the same mistake**: if $h_1$ is wrong, then $h_2, h_3, \ldots$ are all wrong too (they are perfectly correlated).

**Question:** What is the error rate of the majority vote ensemble in this case, for any $n$?

Now generalize: suppose each classifier has error $\varepsilon_i$ decomposed as:

$$\text{error of } h_i = \text{bias}^2 + \text{variance}$$

Averaging $n$ such classifiers, what happens to the bias and variance components as $n \to \infty$? What does this tell you about when ensembling helps?
