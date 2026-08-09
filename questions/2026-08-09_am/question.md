---
name: "The Variance That Vanishes: Why PCA Features Are Uncorrelated"
type: "ML/Stats"
tags: ["PCA", "covariance matrix", "spectral theorem", "dimensionality reduction", "decorrelation"]
date: "2026-08-09"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Ch. 3 & 14 (Hastie, Tibshirani, Friedman)"
---
# The Variance That Vanishes: Why PCA Features Are Uncorrelated

You fit PCA to a data matrix $X \in \mathbb{R}^{n \times p}$ (columns centered). Let $v_1, v_2, \ldots, v_p$ be the principal components (eigenvectors of the sample covariance matrix $S = \frac{1}{n}X^T X$, ordered by decreasing eigenvalue $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_p$).

Define the **scores** $z_k = X v_k \in \mathbb{R}^n$ for each $k$.

**(a)** Show that the sample variance of the scores $z_k$ equals $\lambda_k$.

**(b)** Show that the scores $z_j$ and $z_k$ are **sample-uncorrelated** for $j \neq k$, i.e., $z_j^T z_k = 0$.

**(c)** Here is the conceptual puzzle: the original features $x_1, \ldots, x_p$ (columns of $X$) may be highly correlated. PCA produces perfectly uncorrelated scores. **Where did the correlation go?** Give a one-paragraph intuitive explanation without formulas.
