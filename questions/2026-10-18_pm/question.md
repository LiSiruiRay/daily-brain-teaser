---
name: "Ridge Regression with Cloned Features"
type: "ML/Stats"
tags: ["ridge regression", "lasso", "symmetry", "strict convexity", "grouping effect", "regularization"]
date: "2026-10-18"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning (2nd ed.), Hastie, Tibshirani & Friedman, Exercise 3.29"
---
# Ridge Regression with Cloned Features

Let $x \in \mathbb{R}^N$ be a nonzero feature vector and $y \in \mathbb{R}^N$ a response. There is no intercept. Fix $\lambda > 0$.

**(a)** Ridge regression on the single feature $x$,
$$\min_{\beta}\ \|y - x\beta\|^2 + \lambda \beta^2,$$
gives coefficient $a = \dfrac{x^\top y}{x^\top x + \lambda}$.

Now duplicate the feature: the design matrix becomes $X = [\,x \mid x \mid \cdots \mid x\,]$, with $m$ identical columns. Refit ridge regression with the same $\lambda$:
$$\min_{\beta \in \mathbb{R}^m}\ \|y - X\beta\|^2 + \lambda \|\beta\|_2^2 .$$

Show that all $m$ coefficients are equal, and find their common value. What is the total effect $\sum_i \beta_i$? Interpret the result in terms of an "effective" regularization parameter.

**(b)** Answer the same question for the lasso, where the penalty is $\lambda\|\beta\|_1$. Is the solution still unique?

*Try to do (a) without differentiating anything.*
