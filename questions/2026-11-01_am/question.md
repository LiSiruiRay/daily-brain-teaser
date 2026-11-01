---
name: "The Bootstrap That Fools Itself: 1-NN on Pure Noise"
type: "ML/Stats"
tags: ["bootstrap", "error estimation", "nearest neighbor", "overfitting", "0.632 rule"]
date: "2026-11-01"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Hastie, Tibshirani, Friedman — The Elements of Statistical Learning (2nd ed.), Section 7.11 (Bootstrap Methods)"
---
# The Bootstrap That Fools Itself: 1-Nearest Neighbor on Pure Noise

You have $N$ training points $(x_i, y_i)$, $i=1,\dots,N$. The $x_i \in \mathbb{R}^p$ are distinct, and the labels $y_i \in \{0,1\}$ are **pure noise**. Each label is an independent fair coin flip, independent of $x$. The classifier is **1-nearest neighbor (1-NN)**. Its true test error is exactly $1/2$.

To estimate the error you draw $B$ bootstrap samples. Each one consists of $N$ draws **with replacement** from the training set. Let $\hat f^{*b}$ be the 1-NN classifier fit on bootstrap sample $b$.

**(a)** Show that the probability that a fixed observation $i$ appears in a given bootstrap sample tends to $1 - e^{-1} \approx 0.632$ as $N \to \infty$.

**(b)** The *naive bootstrap* error estimate tests every bootstrap model on the **original** training set:
$$
\widehat{\mathrm{Err}}_{\text{boot}} = \frac{1}{B}\frac{1}{N}\sum_{b=1}^{B}\sum_{i=1}^{N} \mathbf 1\{\hat f^{*b}(x_i) \neq y_i\}.
$$
Compute its expected value as $N, B \to \infty$. Is it close to the true error $1/2$?

**(c)** A natural fix is the *leave-one-out bootstrap* $\widehat{\mathrm{Err}}^{(1)}$. It scores observation $i$ only with bootstrap models whose sample does **not** contain $i$. Efron's **.632 estimator** combines this with the training error $\overline{\mathrm{err}}$:
$$
\widehat{\mathrm{Err}}^{(.632)} = 0.368\,\overline{\mathrm{err}} + 0.632\,\widehat{\mathrm{Err}}^{(1)}.
$$
What value does the .632 estimator give in this example? What does this tell you?
