---
name: "The Posterior That Forgets the Prior"
type: "ML/Stats"
tags: ["Bayesian inference", "posterior convergence", "Bernstein-von Mises", "prior vs likelihood", "Gaussian conjugate"]
date: "2026-09-06"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "The Elements of Statistical Learning, Hastie, Tibshirani, Friedman (2nd ed.) — related to Section 8.3 on Bayesian methods and posterior inference; classical Bernstein–von Mises theorem"
---
# The Posterior That Forgets the Prior: When Does the Likelihood Win?

Suppose you observe $n$ i.i.d. samples $X_1, \ldots, X_n \sim \mathcal{N}(\theta, 1)$ with unknown mean $\theta$.

You place two different priors on $\theta$:

- **Prior A:** $\theta \sim \mathcal{N}(0, \tau_A^2)$ with $\tau_A^2 = 1$
- **Prior B:** $\theta \sim \mathcal{N}(0, \tau_B^2)$ with $\tau_B^2 = 1000$

Let $\hat\theta_A$ and $\hat\theta_B$ be the corresponding posterior means.

**Question:** As $n \to \infty$, what happens to $\hat\theta_A - \hat\theta_B$? Does the choice of prior ever stop mattering?

Now consider the harder version: replace both priors by **any** fixed proper priors $\pi_A$ and $\pi_B$ (not necessarily Gaussian). Must the two posteriors always agree in the limit?

Give a clean argument and identify the precise condition that determines whether the prior is "washed out."
