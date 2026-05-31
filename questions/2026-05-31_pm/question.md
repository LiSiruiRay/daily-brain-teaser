---
name: "The Blessing of Averaging: Boosting Margins"
type: "ML/Stats"
tags: ["boosting", "AdaBoost", "margins", "generalization", "overfitting", "ensemble methods"]
date: "2026-05-31"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "The Elements of Statistical Learning, Hastie, Tibshirani & Friedman, 2nd ed., Chapter 10; Schapire et al. (1998) margin theory"
---
# The Blessing of Averaging: Why Does Boosting Not Overfit Like a Single Deep Tree?

A single decision tree grown to full depth memorizes the training data — it achieves zero training error but generalizes poorly. Boosting (e.g., AdaBoost or gradient boosting) also uses many complex trees, yet it often **keeps improving on the test set even after training error hits zero**, rather than overfitting immediately.

Here is a simplified version of the puzzle:

Suppose we run AdaBoost for $T$ rounds on a binary classification problem, producing classifiers $h_1, h_2, \ldots, h_T$ with weighted training errors $\varepsilon_t \leq \frac{1}{2} - \gamma$ for some fixed margin $\gamma > 0$.

**(a)** Show that after $T$ rounds, the training error of the final ensemble $H(x) = \text{sign}\!\left(\sum_{t=1}^T \alpha_t h_t(x)\right)$ satisfies:

$$\text{Training error} \leq \exp\!\left(-2\gamma^2 T\right)$$

so training error goes to zero **exponentially fast**.

**(b)** Given part (a), why does it seem paradoxical that boosting does not immediately overfit once training error reaches zero? What is the real quantity that keeps improving, and what does this suggest about the right way to think about model complexity in boosting?

*(You do not need to know VC theory — reason from the margin distribution and the idea that the ensemble vote becomes more "confident" over time.)*
