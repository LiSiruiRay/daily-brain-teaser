---
name: "Lp Norm → L∞"
type: "analysis"
tags: ["Lp norm", "Limit", "Squeeze Theorem"]
date: "2026-03-09"
solved: false
comments: ""
related: []
redo: 0
---
# $L^p$ Norm $\to$ $L^\infty$

---

Let $(X, \mathcal{M}, \mu)$ be a measure space with $\mu(X) < \infty$, and let $f \in L^\infty(\mu)$.

**Show that:**

$$\lim_{p \to \infty} \|f\|_p = \|f\|_\infty$$

where

$$\|f\|_p = \left(\int_X |f|^p \, d\mu\right)^{1/p}, \qquad \|f\|_\infty = \operatorname{ess\,sup}_{x \in X} |f(x)|.$$
