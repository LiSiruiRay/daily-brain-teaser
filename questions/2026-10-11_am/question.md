---
name: "Gradient Boosting Secret: Why Each Tree Fits Residuals"
type: "ML/Stats"
tags: ["gradient boosting", "gradient descent", "loss functions", "function space", "pseudo-residuals"]
date: "2026-10-11"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Hastie, Tibshirani, Friedman (2nd ed.), Chapter 10"
---
# The Gradient Boosting Secret: Why Each Tree Fits Residuals

You are building a regression model with squared error loss $L(y, F) = \frac{1}{2}(y - F)^2$.

**Gradient boosting** works by starting with an initial model $F_0(x)$ and then iteratively adding new trees $h_m(x)$:
$$F_m(x) = F_{m-1}(x) + \eta \cdot h_m(x)$$

At each step $m$, gradient boosting fits the new tree $h_m$ to the **negative gradient** of the loss evaluated at the current prediction $F_{m-1}$.

**Show** that for squared error loss, the negative gradient at observation $i$ is exactly the residual $r_i = y_i - F_{m-1}(x_i)$.

Then explain: **why is this a surprising and powerful idea?** In particular, what does it reveal about gradient boosting as a general framework?

*(Hint: think about what happens when you replace squared error with, say, absolute error or log-loss — can you still "fit residuals"?)*
