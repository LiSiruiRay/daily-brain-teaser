---
name: "EM Algorithm's Hidden Monotonicity"
type: "ML/Stats"
tags: ["EM algorithm", "Jensen's inequality", "KL divergence", "latent variables", "likelihood"]
date: "2026-08-23"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "The Elements of Statistical Learning, Hastie, Tibshirani et al., Chapter 8"
---
# The EM Algorithm's Hidden Monotonicity

You are fitting a latent variable model with observed data $X$, latent variables $Z$, and parameters $\theta$. The EM algorithm alternates between:

- **E-step:** Compute $Q(\theta, \theta^{\text{old}}) = \mathbb{E}_{Z|X,\theta^{\text{old}}}[\log p(X, Z \mid \theta)]$
- **M-step:** Set $\theta^{\text{new}} = \arg\max_\theta Q(\theta, \theta^{\text{old}})$

**Prove** that the observed-data log-likelihood $\ell(\theta) = \log p(X \mid \theta)$ is **non-decreasing** at every EM step:

$$\ell(\theta^{\text{new}}) \geq \ell(\theta^{\text{old}}).$$

The key insight is not about optimization tricks — it is a direct consequence of a classical inequality. What is that inequality, and why does it apply here?
