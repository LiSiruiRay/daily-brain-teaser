---
name: "Variance of OLS Along Singular Directions and Ridge Shrinkage"
type: "ML/Stats"
tags: ["ridge regression", "SVD", "bias-variance tradeoff", "linear regression", "spectral geometry"]
date: "2026-05-17"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Hastie, Tibshirani, Friedman (2nd ed.), Chapter 3"
---
# The Variance of a Least-Squares Estimator: Why Does It Shrink Along High-Variance Directions?

Consider the standard linear regression model:

$$y = X\beta + \varepsilon, \quad \varepsilon \sim \mathcal{N}(0, \sigma^2 I)$$

where $X$ is an $n \times p$ matrix with SVD $X = UDV^T$ (singular values $d_1 \geq d_2 \geq \cdots \geq d_p > 0$).

The ordinary least-squares (OLS) estimator is $\hat{\beta} = (X^TX)^{-1}X^Ty$.

Now consider **ridge regression**:

$$\hat{\beta}_\lambda = (X^TX + \lambda I)^{-1}X^Ty$$

**Question:** Show that the variance of the OLS estimator, $\text{Var}(\hat{\beta})$, has its *largest* directions aligned with the *smallest* singular values of $X$. Then explain in one sentence why this makes ridge regression a natural fix: specifically, what does ridge do to these high-variance directions, and why is there a bias-variance trade-off?

*(You do not need to do any heavy computation — the key is a clean geometric/spectral insight.)*
