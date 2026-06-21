---
name: "KDE Bandwidth Bias-Variance Tradeoff"
type: "ML/Stats"
tags: ["kernel density estimation", "bias-variance tradeoff", "nonparametric statistics", "bandwidth selection", "MSE"]
date: "2026-06-21"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "The Elements of Statistical Learning, Ch. 6 (Hastie, Tibshirani, Friedman)"
---
# Kernel Density Estimation: The Bandwidth Dilemma

You are estimating a probability density $f$ on $\mathbb{R}$ from $n$ i.i.d. samples $X_1, \ldots, X_n$ using a kernel density estimator (KDE):

$$\hat{f}_h(x) = \frac{1}{nh} \sum_{i=1}^n K\!\left(\frac{x - X_i}{h}\right)$$

where $K$ is a symmetric kernel with $\int K(u)\,du = 1$, $\int u K(u)\,du = 0$, and $\int u^2 K(u)\,du = \sigma_K^2 < \infty$.

**(a)** Show that the pointwise bias of $\hat{f}_h(x)$ is approximately

$$\text{Bias}[\hat{f}_h(x)] \approx \frac{h^2 \sigma_K^2}{2} f''(x)$$

for small $h$.

**(b)** Without calculation, explain why the variance of $\hat{f}_h(x)$ behaves as $\sim \frac{1}{nh}$ for large $n$.

**(c)** Hence, what is the optimal bandwidth $h^*$ (in terms of $n$) that minimizes the mean squared error (MSE), and what is the resulting rate at which the MSE decays?

**The punchline:** What fundamental statistical trade-off does this reveal, and why can't you simply take $h \to 0$?
