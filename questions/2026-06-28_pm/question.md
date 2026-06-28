---
name: "The Irrelevant Feature Paradox: When Adding Noise Helps OLS"
type: "ML/Stats"
tags: ["overfitting", "bias-variance", "OLS", "degrees of freedom", "optimism"]
date: "2026-06-28"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Hastie, Tibshirani, Friedman, Section 7.3–7.6"
---
# The Irrelevant Feature Paradox: When Adding Noise Helps OLS

Suppose you are fitting a linear model with OLS on a fixed design matrix $X \in \mathbb{R}^{n \times p}$, where $p < n$, to predict $y = X\beta^* + \varepsilon$ with $\varepsilon \sim \mathcal{N}(0, \sigma^2 I)$.

Now consider adding $q$ **pure noise features** — columns $Z \in \mathbb{R}^{n \times q}$ drawn independently of everything else — so your new design matrix is $[X \mid Z]$, and you re-fit OLS on this expanded matrix.

**Question:** What happens to the **expected in-sample (training) MSE** as $q$ increases? Does it go up, go down, or stay the same? What about the **expected out-of-sample (test) MSE** on a new draw from the same distribution?

Give a crisp explanation of the paradox and what drives it.
