---
name: "Bias-Variance Decomposition"
type: "ML/Stats"
tags: ["bias-variance tradeoff", "expected prediction error", "model complexity", "squared loss"]
date: "2026-05-10"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Hastie, Tibshirani, Friedman, 2nd ed., Section 2.9 / 7.3"
---
# The Bias-Variance Tradeoff Is an Exact Decomposition

Let $\hat{f}(x)$ be any estimator (fitted model) of a true function $f(x)$, trained on a random dataset. For a fixed test point $x_0$, define the **expected prediction error** under squared loss:

$$\text{EPE}(x_0) = \mathbb{E}\left[(Y - \hat{f}(x_0))^2\right]$$

where $Y = f(x_0) + \varepsilon$ with $\varepsilon \sim (0, \sigma^2)$ (mean-zero noise, independent of everything), and the expectation is over both the randomness in the training data **and** the noise $\varepsilon$.

**Show that EPE decomposes exactly as:**

$$\text{EPE}(x_0) = \sigma^2 + \text{Bias}^2(\hat{f}(x_0)) + \text{Var}(\hat{f}(x_0))$$

where:
- $\sigma^2$ is irreducible noise,
- $\text{Bias}(\hat{f}(x_0)) = \mathbb{E}[\hat{f}(x_0)] - f(x_0)$,
- $\text{Var}(\hat{f}(x_0)) = \mathbb{E}\left[(\hat{f}(x_0) - \mathbb{E}[\hat{f}(x_0)])^2\right]$.

Then answer: **why can't any single model simultaneously minimize all three terms?** Give a concrete example illustrating the tradeoff.
