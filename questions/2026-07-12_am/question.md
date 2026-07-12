---
name: "AdaBoost Exponential Training Error Bound"
type: "ML/Stats"
tags: ["AdaBoost", "boosting", "exponential loss", "training error", "weak learners"]
date: "2026-07-12"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "The Elements of Statistical Learning, Hastie, Tibshirani, Friedman (2nd ed.), Chapter 10"
---
# The Boosting Paradox: Can a Committee of Weak Learners Beat a Strong One?

AdaBoost constructs a strong classifier by combining many **weak learners** — classifiers that do only slightly better than random guessing (error rate $\epsilon_t < 1/2$).

Each weak learner $h_t : \mathcal{X} \to \{-1, +1\}$ has weighted error $\epsilon_t$ on the current distribution, and is assigned weight

$$\alpha_t = \frac{1}{2} \ln\!\left(\frac{1 - \epsilon_t}{\epsilon_t}\right).$$

The final classifier is $H(x) = \text{sign}\!\left(\sum_{t=1}^T \alpha_t h_t(x)\right)$.

**Show that the training error of AdaBoost decreases exponentially fast:**

If each weak learner achieves error $\epsilon_t \leq \frac{1}{2} - \gamma$ for some fixed $\gamma > 0$, then after $T$ rounds the training error satisfies

$$\text{TrainingError}(H) \leq e^{-2\gamma^2 T}.$$

*Hint: Track the exponential loss $\frac{1}{n}\sum_{i=1}^n e^{-y_i F_T(x_i)}$ where $F_T(x) = \sum_{t=1}^T \alpha_t h_t(x)$, and show each round multiplies this quantity by at most $e^{-2\gamma^2}$.*
