---
name: "Winding Number Is Always an Integer"
type: "Complex Analysis"
tags: ["winding number", "closed curve", "exponential", "log-derivative", "integrating factor"]
date: "2026-05-28"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Complex Analysis, Stein & Shakarchi, Chapter 1; mathematical folklore"
---
# The Winding Number Is Always an Integer

Let $\gamma: [0,1] \to \mathbb{C} \setminus \{0\}$ be a closed curve (i.e., $\gamma(0) = \gamma(1)$) that avoids the origin. The **winding number** of $\gamma$ around $0$ is defined by

$$n(\gamma, 0) = \frac{1}{2\pi i} \int_\gamma \frac{dz}{z}.$$

**Show that $n(\gamma, 0)$ is always an integer**, without invoking any machinery about branches of the logarithm or homotopy theory. Use only the following raw ingredients:

- Define $\phi(t) = \int_0^t \frac{\gamma'(s)}{\gamma(s)}\, ds$.
- Consider the function $h(t) = e^{-\phi(t)} \gamma(t)$.

Why must $n(\gamma, 0)$ be an integer?
