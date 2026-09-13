---
name: "The Gaussian That Knows Its Own Variance"
type: "ML/Stats"
tags: ["bias-variance tradeoff", "MLE", "MSE", "chi-squared", "shrinkage", "admissibility"]
date: "2026-09-13"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Hastie–Tibshirani–Friedman (2nd ed.); statistical folklore"
---
# The Gaussian That Knows Its Own Variance

Suppose you observe a single data point $x$ drawn from a Gaussian with **known mean** $\mu = 0$ but **unknown variance** $\sigma^2$. You want to estimate $\sigma^2$.

The MLE gives $\hat{\sigma}^2_{\text{MLE}} = x^2$.

Now consider the family of estimators $\hat{\sigma}^2_c = c \cdot x^2$ for some constant $c > 0$.

**Question:** Find the value of $c^*$ that minimizes the **mean squared error** $\text{MSE}(c) = \mathbb{E}\left[(c x^2 - \sigma^2)^2\right]$.

Is $c^* = 1$ (the MLE)? If not, which direction does the optimal $c^*$ move, and why does this make intuitive sense?
