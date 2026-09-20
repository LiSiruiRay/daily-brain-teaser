---
name: "PCR Bias-Variance per Principal Component"
type: "ML/Stats"
tags: ["PCA", "regression", "bias-variance tradeoff", "singular values", "dimensionality reduction"]
date: "2026-09-20"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "The Elements of Statistical Learning, Chapter 3 (Hastie, Tibshirani, Friedman)"
---
# The Eigenvalue That Explodes: Why PCA Features Hurt Regression

Suppose you have $n$ observations and $p$ features. You run OLS regression of $y$ on $X$, where $X$ has the SVD $X = UDV^\top$. The OLS fitted values are

$$\hat{y} = X\hat{\beta} = \sum_{j=1}^{p} u_j \frac{u_j^\top y}{d_j} \cdot d_j = \sum_{j=1}^p u_j (u_j^\top y).$$

Now suppose instead of using all $p$ principal components, you use **only the first $M < p$ components** (i.e., PCR — Principal Components Regression). The fitted values become

$$\hat{y}^{\text{PCR}} = \sum_{j=1}^{M} u_j (u_j^\top y).$$

**The puzzle:** OLS is unbiased for $X\beta$. PCR discards components — so it introduces bias. Yet in high dimensions or near-multicollinearity, PCR often **beats OLS in prediction**. 

Here is the concrete question: Write the **mean squared prediction error** of OLS (in-sample, as an estimator of $X\beta$) in terms of the singular values $d_j$ and signal components, and explain precisely why **small singular values are dangerous**. Then show that PCR's bias-variance tradeoff is controlled by a single threshold $M$: what is the **exact bias and variance** of each principal component's contribution?

Assume the model $y = X\beta + \varepsilon$ with $\varepsilon \sim (0, \sigma^2 I)$, and $X$ fixed.
