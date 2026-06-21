---
name: "SVM Margin Width: Why 2/‖β‖?"
type: "ML/Stats"
tags: ["SVM", "margin", "convex optimization", "geometric intuition", "normalization"]
date: "2026-06-21"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Hastie, Tibshirani & Friedman, 2nd ed., Section 12.2"
---
# The SVM Margin Width: Why Does the Distance Equal 2/‖β‖?

You train a hard-margin linear SVM on a linearly separable dataset in $\mathbb{R}^d$. The decision boundary is $\{x : x^\top \beta + \beta_0 = 0\}$, with the two class constraints:

$$y_i(x_i^\top \beta + \beta_0) \geq 1, \quad \forall i.$$

**Question:** Support vectors of the positive class satisfy $x^\top \beta + \beta_0 = +1$, and support vectors of the negative class satisfy $x^\top \beta + \beta_0 = -1$.

(a) Show that the **geometric margin** (Euclidean distance between the two parallel hyperplanes $x^\top\beta + \beta_0 = +1$ and $x^\top\beta + \beta_0 = -1$) equals $\dfrac{2}{\|\beta\|}$.

(b) Hence, explain intuitively why maximizing the margin is equivalent to minimizing $\|\beta\|^2$, and why this turns into the clean convex problem:

$$\min_{\beta,\beta_0} \frac{1}{2}\|\beta\|^2 \quad \text{subject to } y_i(x_i^\top\beta + \beta_0) \geq 1, \; \forall i.$$

(c) **Surprise twist:** If you rescale $\beta \mapsto 2\beta$ and $\beta_0 \mapsto 2\beta_0$ (keeping the same decision boundary), what happens to the margin? And what happens to the constraint values $y_i(x_i^\top \beta + \beta_0) \geq 1$? What does this tell you about the role of the normalization $\|f(x_{\text{sv}})\| = 1$?
