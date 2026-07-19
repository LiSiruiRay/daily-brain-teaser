---
name: "Temperature Scaling and Softmax Saturation"
type: "ML/Stats"
tags: ["softmax", "cross-entropy", "temperature scaling", "calibration", "information theory"]
date: "2026-07-19"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Hastie-Tibshirani-Friedman (2nd ed.); widely known ML folklore"
---
# The Blessing of Normalization: Why Softmax Probabilities Saturate

You have a $K$-class classifier that outputs a score vector $\mathbf{z} = (z_1, z_2, \ldots, z_K) \in \mathbb{R}^K$. The softmax function converts these to probabilities:

$$p_k = \frac{e^{z_k}}{\sum_{j=1}^{K} e^{z_j}}.$$

**Question:** Suppose class 1 is the true class, and you scale all scores by a constant $T > 0$ (i.e., replace $\mathbf{z}$ by $\mathbf{z}/T$). This is called **temperature scaling**.

1. What happens to the softmax probabilities as $T \to 0^+$? As $T \to \infty$?
2. Now consider the **cross-entropy loss** for the true class:
$$\mathcal{L}(T) = -\log p_1(T) = -\log \frac{e^{z_1/T}}{\sum_{j=1}^K e^{z_j/T}}.$$
Show that $\mathcal{L}(T) \to 0$ as $T \to 0^+$ *if and only if* $z_1 > z_j$ for all $j \neq 1$ (i.e., class 1 has the strictly highest score).

3. What is $\lim_{T \to \infty} \mathcal{L}(T)$? Interpret this.
