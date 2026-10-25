---
name: "Nearest Neighbor Is Never More Than Twice as Bad as Bayes"
type: "ML/Stats"
tags: ["nearest-neighbors", "Bayes error", "Cover-Hart", "Jensen inequality", "nonparametric classification"]
date: "2026-10-25"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Hastie, Tibshirani, Friedman — The Elements of Statistical Learning (2nd ed.), §13.3; Cover & Hart (1967)"
---
# Nearest Neighbor Is Never More Than Twice as Bad as Bayes

**Field:** ML / Statistics (nonparametric classification)
**Estimated difficulty:** 2 / 5

### Setup

Consider two-class classification. A feature vector $X \in \mathbb{R}^p$ has a density, and the label is $Y \in \{0,1\}$. Write
$$\eta(x) = P(Y=1 \mid X=x)$$
for the posterior, and assume $\eta$ is continuous.

- The **Bayes classifier** predicts $1$ exactly when $\eta(x) > 1/2$. Its error rate is
$$R^* = \mathbb{E}\big[\min(\eta(X),\, 1-\eta(X))\big].$$
- The **1-nearest-neighbor (1-NN) classifier** is trained on $N$ i.i.d. pairs $(X_i, Y_i)$. At a query point $x$, it predicts the label of the training point closest to $x$.

As $N \to \infty$, the nearest neighbor $X_{(1)}$ of $x$ converges to $x$. Take this as given.

### Questions

**(a)** Show that the asymptotic 1-NN error rate is
$$R_{NN} = \mathbb{E}\big[\,2\,\eta(X)\,(1-\eta(X))\,\big].$$

**(b)** Prove the Cover–Hart bounds
$$R^* \;\le\; R_{NN} \;\le\; 2R^*(1-R^*) \;\le\; 2R^*.$$

**(c)** *(Bonus)* Now allow $K$ classes with posteriors $p_k(x)$. Show that
$$R_{NN} \;\le\; R^*\left(2 - \frac{K}{K-1}\,R^*\right).$$

### Why this is interesting

The 1-NN rule has no model, no parameters, and no training. Yet with infinite data it is guaranteed to lose at most a factor of 2 against the best possible classifier, whatever the distribution. Informally: half of all the classification information in the world is contained in the label of your nearest neighbor. The proof is a short pointwise inequality followed by one application of Jensen's inequality.

*Reference:* Hastie, Tibshirani, Friedman, *The Elements of Statistical Learning* (2nd ed.), §13.3 (the 1-NN asymptotic error bound and the $K$-class formula). Original result: T. Cover & P. Hart, "Nearest neighbor pattern classification," *IEEE Trans. Inf. Theory*, 1967.
