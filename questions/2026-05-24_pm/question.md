---
name: "The Variance of Bagging"
type: "ML/Stats"
tags: ["bagging", "bias-variance", "bootstrap", "correlation", "ensemble methods"]
date: "2026-05-24"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Hastie, Tibshirani, Friedman, 2nd ed., Section 8.7"
---
# The Variance of Bagging

Let $\hat{f}_1, \hat{f}_2, \ldots, \hat{f}_B$ be $B$ identically distributed predictors, each with variance $\sigma^2$. Suppose any two distinct predictors have correlation $\rho \in [0,1]$.

The **bagged predictor** is the simple average:
$$\hat{f}_{\text{bag}} = \frac{1}{B} \sum_{b=1}^B \hat{f}_b.$$

**(a)** Compute $\mathrm{Var}(\hat{f}_{\text{bag}})$ as a function of $B$, $\sigma^2$, and $\rho$.

**(b)** What happens as $B \to \infty$? What does this tell you about when bagging helps and when it doesn't?

**(c)** Now suppose you use a **biased** base learner: each $\hat{f}_b$ has bias $\beta$ (i.e., $E[\hat{f}_b] = f^* + \beta$ where $f^*$ is the true function). Does averaging over $B$ bootstrapped copies reduce bias? What is the fundamental limitation of bagging?
