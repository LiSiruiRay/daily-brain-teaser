---
name: "The Ghost Feature: Useless Predictor Inflates OLS Variance"
type: "ML/Stats"
tags: ["OLS", "degrees of freedom", "projection", "variance estimation", "overfitting"]
date: "2026-08-09"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "The Elements of Statistical Learning, Hastie, Tibshirani, Friedman (2nd ed.) — Ch. 3"
---
# The Ghost Feature: When a Useless Predictor Inflates OLS Variance

You have a response $Y \in \mathbb{R}^n$ and a design matrix $X \in \mathbb{R}^{n \times p}$ with $p < n$, full column rank. You fit OLS and get coefficient estimates $\hat{\beta} = (X^\top X)^{-1} X^\top Y$.

Now you add a new predictor column $z \in \mathbb{R}^n$ that is **completely independent of $Y$** (i.e., $z$ carries zero signal: the true coefficient of $z$ is 0). You refit OLS on the augmented design $\tilde{X} = [X \mid z]$.

**Question:** Show that the residual sum of squares (RSS) of the augmented model satisfies

$$\widetilde{\text{RSS}} \leq \text{RSS},$$

with equality if and only if $z$ is orthogonal to the residual vector $\hat{e} = Y - X\hat{\beta}$.

Then explain the following **seeming paradox**: adding a useless predictor *decreases* RSS (or keeps it the same), yet it *increases* the unbiased estimate of $\sigma^2$. How can removing signal make our noise estimate go up?

*Hint for the paradox: think about what the unbiased estimator of $\sigma^2$ looks like in each model.*
