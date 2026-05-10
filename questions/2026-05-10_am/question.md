---
name: "Optimism of Training Error"
type: "ML/Stats"
tags: ["bias", "overfitting", "model selection", "degrees of freedom", "covariance"]
date: "2026-05-10"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "The Elements of Statistical Learning, Hastie, Tibshirani, Friedman, 2nd ed., Section 7.4–7.5"
---
# The Optimism of Training Error

You fit a model to training data $(x_1, y_1), \ldots, (x_N, y_N)$, producing predictions $\hat{y}_i$. Define:

- **Training error:** $\overline{\text{err}} = \frac{1}{N} \sum_{i=1}^N L(y_i, \hat{y}_i)$
- **True (in-sample) error:** $\text{Err}_{\text{in}} = \frac{1}{N} \sum_{i=1}^N \mathbb{E}_{Y^0}\left[L(Y_i^0, \hat{y}_i)\right]$, where $Y_i^0$ is a **fresh** response at $x_i$, independent of the training data.

Using squared error loss $L(y, \hat{y}) = (y - \hat{y})^2$, show that:

$$\mathbb{E}\left[\text{Err}_{\text{in}} - \overline{\text{err}}\right] = \frac{2}{N} \sum_{i=1}^N \text{Cov}(\hat{y}_i, y_i)$$

This quantity is called the **optimism** of the training error. What does it tell you conceptually?
